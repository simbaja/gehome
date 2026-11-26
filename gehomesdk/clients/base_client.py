"""Base client for GE ERD APIs"""

import abc
from aiohttp import ClientError, ClientSession
import asyncio
from collections import defaultdict
from datetime import datetime, timedelta
import logging
from typing import Any
from collections.abc import Callable

from ..erd import ErdCode, ErdCodeType
from ..exception import (
    GeAuthFailedError,
    GeGeneralServerError,
    GeNeedsReauthenticationError,
    GeNotAuthenticatedError,
    GeRequestError,
)
from ..ge_appliance import GeAppliance
from .async_login_flows import async_get_oauth2_token, async_refresh_oauth2_token
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

    def __init__(
        self,
        username: str,
        password: str,
        region: str = "US",
        event_loop: asyncio.AbstractEventLoop | None = None,
        refresh_token: str | None = None,
    ):
        self.account_username = username
        self.account_password = password
        self.account_region = region
        self._credentials: dict[str, str] = {}
        self._session: ClientSession | None = None

        self._access_token: str | None = None
        # A previously-obtained refresh token (e.g. persisted by the calling
        # application from an earlier `GeSmartHqLogin`/full login) can be
        # seeded here so `async_get_credentials` reconnects without
        # repeating the full login flow, which would re-trigger an MFA
        # challenge for accounts that have it enabled.
        self._refresh_token: str | None = refresh_token
        self._token_expiration_time = datetime.now()

        self._state = GeClientState.INITIALIZING
        self._disconnect_requested = asyncio.Event()
        self._retries_since_last_connect = -1
        self._has_successful_connect = False
        self._loop = event_loop
        self._appliances: dict[str, GeAppliance] = {} 
        self._initialize_event_handlers()

    @property
    def credentials(self) -> dict[str, str]:
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: dict[str, str]):
        self._credentials = credentials

    @property
    def refresh_token(self) -> str | None:
        """The current OAuth2 refresh token, if any.

        The SDK rotates this during logins/reconnects, so the calling
        application should re-read this (e.g. after `async_get_credentials`
        or on disconnect) and persist it if it wants to avoid a full
        (possibly MFA) login on the next reconnect.
        """
        return self._refresh_token

    @property
    def appliances(self) -> dict[str, GeAppliance]:
        return self._appliances

    @property
    def user_id(self) -> str | None:
        if "userId" not in self.credentials:
            raise GeNotAuthenticatedError()
        return self.credentials['userId']

    @property
    def state(self) -> GeClientState:
        return self._state

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_running_loop()
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
    def event_handlers(self) -> dict[str, list[Callable]]:
        return self._event_handlers

    async def async_event(self, event: str, *args, **kwargs):
        _LOGGER.debug("received event: %s, processing callbacks...", event)
        """Schedule event callbacks"""
        for cb in self.event_handlers[event]:
            _LOGGER.debug("scheduling callback: %s", cb)
            self.loop.create_task(cb(*args, **kwargs))

    def add_event_handler(self, event: str, callback: Callable, disposable: bool = False):
        if disposable:
            raise NotImplementedError('Support for disposable callbacks not yet implemented')
        self.event_handlers[event].append(callback)

    def remove_event_handler(self, event: str, callback: Callable):
        try:
            self.event_handlers[event].remove(callback)
        except Exception:
            _LOGGER.warning("could not remove event handler %s-%s", event, callback)

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
                _LOGGER.debug("Tried auto-reconnecting %s times, giving up.", MAX_RETRIES)
                break
            try:
                await self._async_run_client()
            except GeNeedsReauthenticationError:
                _LOGGER.info('Reauthentication needed')
            except GeRequestError as err:
                _LOGGER.info("Error executing request %s", err)
            except Exception as err:
                if not self._has_successful_connect:
                    _LOGGER.warning("Unhandled exception on first connect attempt: %s, disconnecting", err)
                    break
                _LOGGER.exception(err)
                _LOGGER.info('Unhandled exception while running client, ignoring and restarting')

            if self._disconnect_requested.is_set():
                break

            refreshed = False
            while (
                not self._disconnect_requested.is_set()
                and self._retries_since_last_connect <= MAX_RETRIES
            ):
                await self._set_state(GeClientState.DROPPED)
                await self._set_state(GeClientState.WAITING)
                _LOGGER.debug('Waiting before reconnecting')
                await asyncio.sleep(RETRY_INTERVAL)
                _LOGGER.debug('Refreshing authentication before reconnecting')
                try:
                    await self.async_do_refresh_login_flow()
                    refreshed = True
                    break
                except (ClientError, asyncio.TimeoutError, GeGeneralServerError, GeRequestError) as err:
                    # Transient network/server errors during reconnect should not kill the loop
                    _LOGGER.warning("Transient error refreshing authentication, will retry: %s", err)
                    self._retries_since_last_connect += 1
                except Exception as err:
                    # if there was an auth or fatal error refreshing the authentication, stop and disconnect the client
                    _LOGGER.warning("Error refreshing authentication: %s", err)
                    break

            if not refreshed:
                break

            self._retries_since_last_connect += 1

        #initiate the disconnection            
        await self.disconnect()

    @abc.abstractmethod
    async def _async_run_client(self) -> None:
        """ Internal method to run the client """
        pass

    @abc.abstractmethod
    async def async_set_erd_value(self, appliance: GeAppliance, erd_code: ErdCodeType, erd_value: Any) -> None:
        """
        Send a new erd value to the appliance
        :param appliance: The appliance being updated
        :param erd_code: The ERD code to update
        :param erd_value: The new value to set
        """
        pass

    @abc.abstractmethod
    async def async_request_update(self, appliance: GeAppliance) -> None:
        """Request the appliance send a full state update"""
        pass

    async def async_request_features(self, appliance: GeAppliance) -> None:
        """Request the appliance send a features state update"""
        pass

    async def async_request_message(self, appliance: GeAppliance) -> None:
        """Request notification history"""
        pass

    async def async_get_credentials(self, session: ClientSession) -> None:
        """Get updated credentials.

        If a refresh token was seeded (via the `refresh_token` constructor
        argument) or obtained from a previous login, it is used to
        reconnect without repeating the full login flow, which for MFA
        accounts would re-trigger the verification-code challenge. Falls
        back to the full login flow if there is no refresh token, or if it
        has expired/been revoked.
        """
        self._session = session
        if self._refresh_token:
            try:
                await self.async_do_refresh_login_flow()
                return
            except (GeAuthFailedError, GeNeedsReauthenticationError) as exc:
                _LOGGER.warning("Seeded refresh token invalid, falling back to full login: %s", exc)
        await self.async_do_full_login_flow()
        
    async def async_do_full_login_flow(self) -> dict[str, str]:
        """Do the full login flow for this client"""
        self.credentials = await self._async_do_full_login_flow()
        return self.credentials

    @abc.abstractmethod
    async def _async_do_full_login_flow(self) -> dict[str, str]:
        """Internal full login flow"""
        pass

    async def async_do_refresh_login_flow(self) -> dict[str, str]:
        """Do the refresh login flow for this client"""
        self.credentials = await self._async_do_refresh_login_flow()
        return self.credentials

    @abc.abstractmethod
    async def _async_do_refresh_login_flow(self) -> dict[str, str]:
        """Internal refresh login flow"""
        pass

    async def _async_get_oauth2_token(self) -> dict:
        """Get the OAuth2 token based on the username and password"""

        await self._set_state(GeClientState.AUTHORIZING_OAUTH)

        if not self._session:
            raise GeAuthFailedError('Must have a valid session')
        
        oauth_token = await async_get_oauth2_token(
            self._session, 
            self.account_username, 
            self.account_password, 
            self.account_region)

        try:
            self._access_token = oauth_token['access_token']
            self._token_expiration_time = datetime.now() + timedelta(seconds=(oauth_token['expires_in'] - 120))
            self._refresh_token = oauth_token['refresh_token']
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')
        
        return oauth_token

    async def _async_refresh_oauth2_token(self) -> None:
        """ Refreshes an OAuth2 Token based on a refresh token """

        await self._set_state(GeClientState.AUTHORIZING_OAUTH)

        if not self._session:
            raise GeAuthFailedError('Must have a valid session.')

        oauth_token: dict

        # first try the standard refresh token if available
        # only fall back to full login if the refresh token itself was rejected
        if self._refresh_token:
            try:
                oauth_token = await async_refresh_oauth2_token(self._session, self._refresh_token)
            except GeAuthFailedError as exc:
                _LOGGER.warning("Refresh token failed, falling back to full login: %s", exc)
                oauth_token = await self._async_get_oauth2_token()
        else:
            # No refresh token, do full login
            oauth_token = await self._async_get_oauth2_token()

        try:
            self._access_token = oauth_token['access_token']
            self._token_expiration_time = datetime.now() + timedelta(seconds=(oauth_token['expires_in'] - 120))
            self._refresh_token = oauth_token.get('refresh_token', self._refresh_token)
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a token: {oauth_token}')

    async def _maybe_trigger_appliance_init_event(self, data: tuple[GeAppliance, dict[ErdCodeType, Any]]) -> None:
        """
        Trigger the appliance_got_type event if appropriate

        :param data: GeAppliance updated and the updates
        """
        appliance, state_changes = data
        if ErdCode.APPLIANCE_TYPE in state_changes and not appliance.initialized:
            _LOGGER.debug("Got initial appliance type for %s", appliance)
            appliance.initialized = True
            await self.async_event(EVENT_APPLIANCE_INITIAL_UPDATE, appliance)

    async def _set_appliance_availability(self, appliance: GeAppliance, available: bool) -> None:
        if available and not appliance.available:
            appliance.set_available()
            await self.async_event(EVENT_APPLIANCE_AVAILABLE, appliance)
        elif not available and appliance.available:
            appliance.set_unavailable()
            await self.async_event(EVENT_APPLIANCE_UNAVAILABLE, appliance)

    async def _set_appliance_features(self, appliance: GeAppliance, features: list[str]) -> None:
        appliance.features = features

    async def _set_state(self, new_state: GeClientState) -> bool:
        """ Indicate that the state changed and raise an event """
        if self._state != new_state:
            old_state = self._state
            self._state = new_state
            await self.async_event(EVENT_STATE_CHANGED, old_state, new_state)
            return True
        return False            

    def _initialize_event_handlers(self) -> None:
        self._event_handlers: dict[str, list[Callable[..., Any]]] = defaultdict(list)
        self.add_event_handler(EVENT_STATE_CHANGED, self._on_state_change)

    async def _on_state_change(self, old_state: GeClientState, new_state: GeClientState) -> None:
        _LOGGER.debug("Client changed state: %s to %s", old_state, new_state)

        if new_state == GeClientState.CONNECTED:
            await self.async_event(EVENT_CONNECTED, None)
        if new_state == GeClientState.DISCONNECTED:
            await self.async_event(EVENT_DISCONNECTED, None)

    async def disconnect(self) -> None:
        """Disconnect and cleanup."""
        if not self._disconnect_requested.is_set():
            _LOGGER.info("Disconnecting")
            await self._set_state(GeClientState.DISCONNECTING)         
            self._disconnect_requested.set()
            await self._disconnect()
            await self._set_state(GeClientState.DISCONNECTED) 

    async def _set_connected(self) -> None:
        self._retries_since_last_connect = -1
        self._has_successful_connect = True
        await self._set_state(GeClientState.CONNECTED)

    @abc.abstractmethod
    async def _disconnect(self) -> None:
        pass
