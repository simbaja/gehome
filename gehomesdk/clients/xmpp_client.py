import asyncio
import logging
from typing import Any, Dict, Optional, Union

import slixmpp
from lxml import etree
from ..erd import ErdCode, ErdCodeType
from ..exception import *
from ..ge_appliance import GeAppliance
from .base_client import GeBaseClient
from .const import *
from .ge_client_xmpp import (
    GeClientXMPP, 
    XMPP_EVENT_MESSAGE, 
    XMPP_EVENT_PRESENCE_AVAILABLE, 
    XMPP_EVENT_PRESENCE_UNAVAILABLE, 
    XMPP_EVENT_SESSION_START
)
from .states import GeClientState

try:
    import ujson as json
except ImportError:
    import json

_LOGGER = logging.getLogger(__name__)

def _first_or_none(lst: list) -> Any:
    try:
        return lst[0]
    except IndexError:
        return None

class GeXmppClient(GeBaseClient):
    client_priority = 1

    def __init__(self, username: str, password: str, event_loop: Optional[asyncio.AbstractEventLoop]):
        super().__init__(username, password, event_loop=event_loop)
        self._client = None  # type: Optional[GeClientXMPP]

    def _get_xmpp_client(self) -> GeClientXMPP:
        client = GeClientXMPP(self.credentials['jid'], self.credentials['password'])
        client.add_external_event_handler(XMPP_EVENT_SESSION_START, self._on_start)
        client.add_external_event_handler(XMPP_EVENT_MESSAGE, self._on_message)
        client.add_external_event_handler(XMPP_EVENT_PRESENCE_AVAILABLE, self._on_presence_available)
        client.add_external_event_handler(XMPP_EVENT_PRESENCE_UNAVAILABLE, self._on_presence_unavailable)

        return client

    async def _async_do_full_login_flow(self) -> Dict[str,str]:
        """Perform a complete login flow, returning credentials."""

        _LOGGER.debug('Getting OAuth2 token')
        await self._async_get_oauth2_token()

        _LOGGER.debug('Getting mobile device token')
        mdt = await self._async_get_mobile_device_token()

        _LOGGER.debug('Getting GE token')
        ge_token = await self._async_get_ge_token(mdt)

        _LOGGER.debug('Getting XMPP credentials')
        return await self._async_get_xmpp_credentials(ge_token)
    
    async def _async_do_refresh_login_flow(self) -> Dict[str, str]:
        """Perform a refresh login flow, returning credentials"""

        _LOGGER.debug('Refreshing OAuth2 token')
        await self._async_refresh_oauth2_token()

        _LOGGER.debug('Getting mobile device token')
        mdt = await self._async_get_mobile_device_token()

        _LOGGER.debug('Getting GE token')
        ge_token = await self._async_get_ge_token(mdt)

        _LOGGER.debug('Getting XMPP credentials')
        return await self._async_get_xmpp_credentials(ge_token)

    async def _async_get_mobile_device_token(self) -> str:
        """Get a mobile device token"""
        await self._set_state(GeClientState.AUTHORIZING_CLIENT)

        mdt_data = {
            'kind': 'mdt#login',
            'app': OAUTH2_APP_ID,
            'os': 'google_android'
        }
        auth_header = { 'Authorization': 'Bearer ' + self._access_token }

        async with self._session.post(f'{API_URL}/v1/mdt', json=mdt_data, headers=auth_header) as resp:
            if resp.status != 200:
                raise GeAuthFailedError(await resp.text())
            results = await resp.json()
        try:
            return results['mdt']
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a mobile device token: {results}')

    async def _async_get_ge_token(self, mobile_device_token: str) -> str:
        """Get the GE token that we can use to get XMPP credentials"""
        params = {
            'client_id': OAUTH2_CLIENT_ID,
            'client_secret': OAUTH2_CLIENT_SECRET,
            'mdt': mobile_device_token
        }
        auth_header = { 'Authorization': 'Bearer ' + self._access_token }

        async with self._session.post(f'{LOGIN_URL}/oauth2/getoken', params=params, headers=auth_header) as resp:
            if 400 <= resp.status < 500:
                raise GeAuthFailedError(await resp.text())
            if resp.status >= 500:
                raise GeGeneralServerError(await resp.text())
            results = await resp.json()

        try:
            return results['access_token']
        except KeyError:
            raise GeAuthFailedError(f'Failed to get a GE token: {results}')

    async def _async_get_xmpp_credentials(self, ge_token: str) -> Dict:
        """Get XMPP credentials"""
        uri = f'{API_URL}/v1/mdt/credentials'
        headers = {'Authorization': f'Bearer {ge_token}'}
        async with self._session.get(uri, headers=headers) as resp:
            if 400 <= resp.status < 500:
                raise GeAuthFailedError(await resp.text())
            if resp.status >= 500:
                raise GeGeneralServerError(await resp.text())
            return await resp.json()

    async def _async_run_client(self):
        """Run the client."""
        try:
            await self._set_state(GeClientState.CONNECTING)
            address = (self._credentials['address'], self._credentials['port'])
            self._client = self._get_xmpp_client()
            self._client.connect(address=address)
            #run the loop
            await asyncio.ensure_future(self._client.disconnected, loop=self.loop)
        #TODO: better exception handling
        except Exception as err:
            _LOGGER.error(f"Exception while processing XMPP loop: {err}")
        finally:
            self._disconnect()

    async def _disconnect(self) -> None:
        if self._client:
            await self._client.disconnect()
        self._client = None

    async def _add_appliance(self, jid: str):
        """Add an appliance to the registry and request an update."""
        mac_addr = jid.split('_')[0]
        if jid in self.appliances:
            raise GeDuplicateApplianceError(f'Attempted to add duplicate appliances {mac_addr} ({jid})')
        new_appliance = GeAppliance(mac_addr, self)

        _LOGGER.info(f'Adding appliance {jid}')
        self.appliances[jid] = new_appliance
        await self.async_event(EVENT_ADD_APPLIANCE, new_appliance)
        await new_appliance.async_request_update()

    async def _maybe_add_appliance(self, jid: str):
        """Add an appliance, suppressing the error if it already exists."""
        try:
            await self._add_appliance(jid)
        except GeDuplicateApplianceError as err:
            _LOGGER.warn(f'{err}')
            pass

    async def _on_presence_available(self, evt: slixmpp.ElementBase):
        """Perform actions when notified of an available JID."""
        await asyncio.sleep(2)  # Wait 2 seconds to give it time to register
        jid = slixmpp.JID(evt['from']).bare

        if jid == self._client.boundjid.bare:
            return
        try:
            await self._set_appliance_availability(self.appliances[jid], True)            
        except KeyError:
            await self._add_appliance(jid)
            self.appliances[jid].set_available()

    async def _on_presence_unavailable(self, evt):
        """When appliance is no longer available, mark it as such."""
        jid = slixmpp.JID(evt['from']).bare

        if jid == self._client.boundjid.bare:
            return
        try:
            self._set_appliance_availability(self.appliances[jid], False)
        except KeyError:
            pass

    async def _on_message(self, event):
        """Handle incoming messages."""

        msg = str(event)
        msg_from = slixmpp.JID(event['from']).bare
        try:
            message_data = self._extract_message_json(msg)
        except ValueError:
            _LOGGER.info(f"From: {msg_from}: Not a GE message")
            return
        try:
            appliance = self.appliances[msg_from]
            state_changes = appliance.update_erd_values(message_data)
            if state_changes:
                await self.async_event(EVENT_APPLIANCE_STATE_CHANGE, [appliance, state_changes])
            await self.async_event(EVENT_APPLIANCE_UPDATE_RECEIVED, [appliance, message_data])
        except KeyError:
            _LOGGER.warning('Received json message from unregistered appliance')

    async def _on_start(self, event):
        _LOGGER.debug('Starting session: ' + str(event))
        self._client.send_presence('available')
        await asyncio.sleep(5)
        await self._set_connected()
        await self.async_event(EVENT_GOT_APPLIANCE_LIST, None)

    def _complete_jid(self, jid) -> str:
        """Make a complete jid from a username"""
        if "@" in jid:
            return jid
        return f"{jid}@{self._client.boundjid.host}"

    def _get_appliance_jid(self, appliance: GeAppliance) -> str:
        return self._complete_jid(f"{appliance.mac_addr}_{self.user_id}")

    def _send_raw_message(self, mto: slixmpp.JID, mbody: str, mtype: str = 'chat', msg_id: Optional[str] = None):
        """TODO: Use actual xml for this instead of hacking it.  Then again, this is what GE does in the app."""
        try:
            if not self._client:
                raise RuntimeError('Client connection is not available')

            if msg_id is None:
                msg_id = self._client.new_id()
            raw_message = (
                f'<message type="{mtype}" from="{self._client.boundjid.bare}" to="{mto}" id="{msg_id}">'
                f'<body>{mbody}</body>'
                f'</message>'
            )
            
            self._client.send_raw(raw_message)
        except Exception as err:
            raise GeRequestError from err

    def _send_request(
            self, appliance: GeAppliance, method: str, uri: str, key: Optional[str] = None,
            value: Optional[str] = None, message_id: Optional[str] = None):
        """
        Send a pseudo-http request to the appliance
        :param appliance: GeAppliance, the appliance to send the request to
        :param method: str, Usually "GET" or "POST"
        :param uri: str, the "endpoint" for the request, usually of the form "/UUID/erd/{erd_code}"
        :param key: The json key to set in a POST request.  Usually a four-character hex string with leading "0x".
        :param value: The value to set, usually encoded as a hex string without a leading "0x"
        :param message_id:
        """
        if method.lower() != 'post' and (key is not None or value is not None):
            raise RuntimeError('Values can only be set in a POST request')

        if message_id is None:
            message_id = self._client.new_id()
        message_body = self._format_request(message_id, uri, method, key, value)
        jid = slixmpp.JID(self._get_appliance_jid(appliance))
        self._send_raw_message(jid, message_body)

    async def async_request_update(self, appliance: GeAppliance):
        """
        Request a full update from the appliance.
        TODO: This doesn't seem to do a full request.  Need to investigate if this is possible.
        """
        self._send_request(appliance, 'GET', '/UUID/cache')

    async def async_set_erd_value(self, appliance: GeAppliance, erd_code: ErdCodeType, erd_value: Any):
        """
        Send a new erd value to the appliance
        :param appliance: GeAppliance, the appliance to update
        :param erd_code: The ERD code to update
        :param erd_value: The new value to set
        """
        if isinstance(erd_code, ErdCode):
            raw_erd_code = erd_code.value
        else:
            raw_erd_code = erd_code

        uri = f'/UUID/erd/{raw_erd_code}'
        self._send_request(appliance, 'POST', uri, raw_erd_code, erd_value)

    @staticmethod
    def _extract_message_json(message: str) -> Dict:
        """The appliances send messages that don't play nice with slixmpp, so let's do this."""
        etr = etree.XML(message)
        json_elem = _first_or_none(etr.xpath('//json'))
        if json_elem is None:
            raise ValueError('Not a GE appliance message')

        data = _first_or_none(json_elem.xpath('text()'))
        data = json.loads(data)
        return data

    @staticmethod
    def _format_request(
            msg_id: Union[int, str], uri: str, method: str, key: Optional[str] = None, value: Optional[str] = None) -> str:
        """Format a XMPP pseudo-HTTP request."""
        if method.lower() == 'post':
            post_body = f"<json>{json.dumps({key:value})}</json>"
        else:
            post_body = ""
        message = (
            f"<request><id>{msg_id}</id>"
            f"<method>{method}</method>"
            f"<uri>{uri}</uri>"
            f"{post_body}"
            "</request>"  # [sic.]
        )
        return message
