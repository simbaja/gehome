"""Base client for GE ERD APIs"""

import abc
from gehomesdk.clients.async_login_flows import async_get_oauth2_token, async_refresh_oauth2_token
from aiohttp import ClientSession
import asyncio
from collections import defaultdict
from datetime import datetime, timedelta
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

from ..erd import ErdCode, ErdCodeType
from ..exception import *
from ..ge_appliance import GeAppliance
from .const import (
    EVENT_APPLIANCE_INITIAL_UPDATE,
    EVENT_APPLIANCE_AVAILABLE,
    EVENT_APPLIANCE_UNAVAILABLE, 
    EVENT_CONNECTED, 
    EVENT_DISCONNECTED, 
    EVENT_STATE_CHANGED,
    MAX_RETRIES, 
    RETRY_INTERVAL,
)
from .states import GeClientState

_LOGGER = logging.getLogger(__name__)

class GeBaseClient(metaclass=abc.ABCMeta):
    """Abstract base class for GE ERD APIs"""

    client_priority = 0  # Priority of this client class.  Higher is better.

    def __init__(self, username: str, password: str, event_loop: Optional[asyncio.AbstractEventLoop] = None):
        self.account_username = username
        self.account_password = password
        self._credentials = None  # type: Optional[Dict]
        self._session = None # type: Optional[ClientSession]

        self._access_token = None
        self._refresh_token = None
        self._token_expiration_time = datetime.now()

        self._state = GeClientState.INITIALIZING
        self._disconnect_requested = asyncio.Event()
        self._retries_since_last_connect = -1
        self._has_successful_connect = False
        self._loop = event_loop
        self._appliances = {}  # type: Dict[str, GeAppliance]
        self._initialize_event_handlers()

    @property
    def credentials(self) -> Optional[Dict]:
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: Dict):
        self._credentials = credentials

    @property
    def appliances(self) -> Dict[str, GeAppliance]:
        return self._appliances

    @property
    def user_id(self) -> Optional[str]:
        try:
            return self.credentials['userId']
        except (TypeError, KeyError):
            raise GeNotAuthenticatedError

    @property
    def state(self) -> GeClientState:
        return self._state

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop

    @property
    def connected(self) -> bool:
        """ Indicates whether the client is in a connected state """
        return self._state not in [GeClientState.DISCONNECTING, GeClientState.DISCONNECTED]
    
    @property
    def available(self) -> bool:
        """ Indicates whether the client is available for sending/receiving commands """
        return self._state == GeClientState.CONNECTED

    @property
    def event_handlers(self) -> Dict[str, List[Callable]]:
        return self._event_handlers

    async def async_event(self, event: str, *args, **kwargs):
        """Trigger event callbacks sequentially"""
        for cb in self.event_handlers[event]:
            asyncio.ensure_future(cb(*args, **kwargs), loop=self.loop)

    def add_event_handler(self, event: str, callback: Callable, disposable: bool = False):
        if disposable:
            raise NotImplementedError('Support for disposable callbacks not yet implemented')
        self.event_handlers[event].append(callback)

    def remove_event_handler(self, event: str, callback: Callable):
        try:
            self.event_handlers[event].remove(callable)
        except:
            _LOGGER.warn(f"could not remove event handler {event}-{callable}")

    def clear_event_handlers(self):
        self._initialize_event_handlers()

    async def async_get_credentials_and_run(self, session: ClientSession):
        """Do a full login flow and run the client."""
        await self.async_get_credentials(session)
        await self.async_run_client()

    async def async_run_client(self):
        #reset the disconnect event
        self._disconnect_requested.clear()

        _LOGGER.info('Starting GE Appliances client')
        while not self._disconnect_requested.is_set():
            if self._retries_since_last_connect > MAX_RETRIES:
                _LOGGER.debug(f'Tried auto-reconnecting {MAX_RETRIES} times, giving up.')
                break
            try:
                await self._async_run_client()
            except GeNeedsReauthenticationError:
                _LOGGER.info('Reauthentication needed')
            except GeRequestError as err:
                _LOGGER.info(f'Error executing request {err}')
            except Exception as err:
                if not self._has_successful_connect:
                    _LOGGER.warn(f'Unhandled exception on first connect attempt: {err}, disconnecting')
                    break
                _LOGGER.info(f'Unhandled exception while running client: {err}, ignoring and restarting')  
            finally:
                if not self._disconnect_requested.is_set():
                    await self._set_state(GeClientState.DROPPED)
                    await self._set_state(GeClientState.WAITING)
                    _LOGGER.debug('Waiting before reconnecting')
                    await asyncio.sleep(RETRY_INTERVAL)
                    _LOGGER.debug('Refreshing authentication before reconnecting')
                    try:
                        await self.async_do_refresh_login_flow()
                    except Exception as err:
                        #if there was an error refreshing the authentication, break the loop and kill the client
                        _LOGGER.warn(f'Error refreshing authentication: {err}')
                        break
                self._retries_since_last_connect += 1

        #initiate the disconnection            
        await self.disconnect()

    @abc.abstractmethod
    async def _async_run_client(self):
        """ Internal method to run the client """

    @abc.abstractmethod
    async def async_set_erd_value(self, appliance: GeAppliance, erd_code: ErdCodeType, erd_value: Any):
        """
        Send a new erd value to the appliance
        :param appliance: The appliance being updated
        :param erd_code: The ERD code to update
        :param erd_value: The new value to set
        """
        pass

    @abc.abstractmethod
    async def async_request_update(self, appliance: GeAppliance):
        """Request the appliance send a full state update"""
        pass

    async def async_request_features(self, appliance: GeAppliance):
        """Request the appliance send a features state update"""
        pass

    async def async_request_message(self, appliance: GeAppliance):
        """Request notification history"""
        pass

    async def async_get_credentials(self, session: ClientSession):
        """Get updated credentials"""
        self._session = session
        await self.async_do_full_login_flow()
        
    async def async_do_full_login_flow(self) -> Dict[str, str]:
        """Do the full login flow for this client"""
        self.credentials = await self._async_do_full_login_flow()
        return self.credentials

    @abc.abstractmethod
    async def _async_do_full_login_flow(self) -> Dict[str, str]:
        """Internal full login flow"""
        pass

    async def async_do_refresh_login_flow(self) -> Dict[str, str]:
        """Do the refresh login flow for this client"""
        self.credentials = await self._async_do_refresh_login_flow()
        return self.credentials

    @abc.abstractmethod
    async def _async_do_refresh_login_flow(self) -> Dict[str, str]:
        """Internal refresh login flow"""
        pass

    async def _async_get_oauth2_token(self):
        """Get the OAuth2 token based on the username and password"""

        await self._set_state(GeClientState.AUTHORIZING_OAUTH)

        oauth_token = await async_get_oauth2_token(self._session, self.account_username, self.account_password)

        try:
            self._access_token = oauth_token['access_token']
            self._token_expiration_time = datetime.now() + timedelta(seconds=(oauth_token['expires_in'] - 120))
            self._refresh_token = oauth_token['refresh_token']
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')

    async def _async_refresh_oauth2_token(self):
        """ Refreshes an OAuth2 Token based on a refresh token """

        await self._set_state(GeClientState.AUTHORIZING_OAUTH)

        oauth_token = await async_refresh_oauth2_token(self._session, self._refresh_token)

        try:
            self._access_token = oauth_token['access_token']
            self._token_expiration_time = datetime.now() + timedelta(seconds=(oauth_token['expires_in'] - 120))
            self._refresh_token = oauth_token.get('refresh_token', self._refresh_token)
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')

    async def _maybe_trigger_appliance_init_event(self, data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
        """
        Trigger the appliance_got_type event if appropriate

        :param data: GeAppliance updated and the updates
        """
        appliance, state_changes = data
        if ErdCode.APPLIANCE_TYPE in state_changes and not appliance.initialized:
            _LOGGER.debug(f'Got initial appliance type for {appliance:s}')
            appliance.initialized = True
            await self.async_event(EVENT_APPLIANCE_INITIAL_UPDATE, appliance)

    async def _set_appliance_availability(self, appliance: GeAppliance, available: bool):
        if available and not appliance.available:
            appliance.set_available()
            await self.async_event(EVENT_APPLIANCE_AVAILABLE, appliance)
        elif not available and appliance.available:
            appliance.set_unavailable()
            await self.async_event(EVENT_APPLIANCE_UNAVAILABLE, appliance)

    async def _set_appliance_features(self, appliance: GeAppliance, features: List[str]):
        appliance.features = features

    async def _set_state(self, new_state: GeClientState) -> bool:
        """ Indicate that the state changed and raise an event """
        if self._state != new_state:
            old_state = self._state
            self._state = new_state
            await self.async_event(EVENT_STATE_CHANGED, old_state, new_state)
            return True
        return False            

    def _initialize_event_handlers(self):
        self._event_handlers = defaultdict(list)  # type: Dict[str, List[Callable]]
        self.add_event_handler(EVENT_STATE_CHANGED, self._on_state_change)
        pass

    async def _on_state_change(self, old_state: GeClientState, new_state: GeClientState):
        _LOGGER.debug(f'Client changed state: {old_state} to {new_state}')

        if new_state == GeClientState.CONNECTED:
            await self.async_event(EVENT_CONNECTED, None)
        if new_state == GeClientState.DISCONNECTED:
            await self.async_event(EVENT_DISCONNECTED, None)

    async def disconnect(self):
        """Disconnect and cleanup."""
        if not self._disconnect_requested.is_set():
            _LOGGER.info("Disconnecting")
            await self._set_state(GeClientState.DISCONNECTING)         
            self._disconnect_requested.set()
            await self._disconnect()
            await self._set_state(GeClientState.DISCONNECTED) 

    async def _set_connected(self):
        self._retries_since_last_connect = -1
        self._has_successful_connect = True
        await self._set_state(GeClientState.CONNECTED)

    @abc.abstractmethod
    async def _disconnect(self) -> None:
        pass
