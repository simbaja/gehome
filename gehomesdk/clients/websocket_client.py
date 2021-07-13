import asyncio
import logging
import websockets
from typing import Any, Dict, List, Optional, Tuple

from ..erd import ErdCode, ErdCodeType
from ..exception import *
from ..ge_appliance import GeAppliance

from .async_helpers import CancellableAsyncIterator
from .base_client import GeBaseClient
from .const import (
    API_URL,
    EVENT_ADD_APPLIANCE, 
    EVENT_APPLIANCE_STATE_CHANGE,
    EVENT_APPLIANCE_UPDATE_RECEIVED,
    EVENT_GOT_APPLIANCE_LIST,
    EVENT_GOT_APPLIANCE_FEATURES,
)
from .states import GeClientState

try:
    import ujson as json
except ImportError:
    import json

ALL_ERD = "allErd"
API_HOST = API_URL[8:]  # Drop the https://
LIST_APPLIANCES = "List-appliances"
REQUEST_FEATURES = "Request-features"
SET_ERD = "setErd"

KEEPALIVE_TIMEOUT = 30
LIST_APPLIANCES_FREQUENCY = 600

_LOGGER = logging.getLogger(__name__)

class GeWebsocketClient(GeBaseClient):
    """
    Client for GE's Websocket pseudo-MQTT API.
    """
    client_priority = 2  # This should be the primary client

    def __init__(self, username: str, password: str, event_loop: Optional[asyncio.AbstractEventLoop] = None, keepalive: Optional[int] = KEEPALIVE_TIMEOUT, list_frequency: Optional[int] = LIST_APPLIANCES_FREQUENCY):
        super().__init__(username, password, event_loop)
        self._endpoint = None  # type: Optional[str]
        self._socket = None  # type: Optional[websockets.client.WebSocketClientProtocol]
        self._pending_erds = {}  # type: Dict[Tuple[str, str], str]
        self._keepalive_timeout = keepalive
        self._keepalive_fut = None  # type: Optional[asyncio.Future]
        self._list_frequency = list_frequency
        self._list_fut = None # type: Optional[asyncio.Future]

    @property
    def available(self) -> bool:
        """ Indicates whether the client is available for sending/receiving commands """
        return self._socket and not self._socket.closed

    async def _async_do_full_login_flow(self) -> Dict[str,str]:
        """Perform a complete login flow, returning credentials."""

        _LOGGER.debug('Getting OAuth2 token')
        await self._async_get_oauth2_token()

        _LOGGER.debug('Getting WS credentials')
        return await self._async_get_wss_credentials()
    
    async def _async_do_refresh_login_flow(self) -> Dict[str, str]:
        """Perform a refresh login flow, returning credentials"""

        _LOGGER.debug('Refreshing OAuth2 token')
        await self._async_refresh_oauth2_token()

        _LOGGER.debug('Getting WS credentials')
        return await self._async_get_wss_credentials()

    async def _async_get_wss_credentials(self) -> Dict[str,str]:
        """Get WSS credentials"""

        await self._set_state(GeClientState.AUTHORIZING_CLIENT)

        uri = f'{API_URL}/v1/websocket'
        auth_header = { 'Authorization': 'Bearer ' + self._access_token }
        async with self._session.get(uri, headers=auth_header) as resp:
            if 400 <= resp.status < 500:
                raise GeAuthFailedError(await resp.text())
            if resp.status >= 500:
                raise GeGeneralServerError(await resp.text())
            return await resp.json()
        
    @property
    def endpoint(self) -> str:
        try:
            return self.credentials['endpoint']
        except (TypeError, KeyError):
            raise GeNotAuthenticatedError

    @property
    def websocket(self):
        return self._socket

    def _initialize_event_handlers(self):
        super()._initialize_event_handlers()
        self.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, self._maybe_trigger_appliance_init_event)

    async def _async_run_client(self):
        """Run the client."""
        try:
            await self._set_state(GeClientState.CONNECTING)
            async with websockets.connect(self.endpoint) as socket:
                self._socket = socket
                self._setup_futures()
                await self._subscribe_all()
                await self._set_connected()
                await self._get_appliance_list()
                try:
                    async for message in CancellableAsyncIterator(socket, self._disconnect_requested):
                        try:
                            await self._process_message(message)
                        except GeRequestError as err:
                            _LOGGER.exception("Could not process request")
                except websockets.WebSocketException:
                    _LOGGER.error("Unknown error reading socket")
                except RuntimeError as err:
                    #do nothing if it's a StopAsyncIteration, we just stopped the iteration
                    #as part of the disconnect
                    if not isinstance(err.__cause__, StopAsyncIteration):
                        raise
        finally:
            self._teardown_futures()
            await self._disconnect()

    async def async_set_erd_value(self, appliance: GeAppliance, erd_code: ErdCodeType, erd_value: Any):
        if isinstance(erd_code, ErdCode):
            raw_erd_code = erd_code.value
        else:
            raw_erd_code = erd_code
        raw_erd_code = raw_erd_code.upper().replace("0X", "0x")

        mac_addr = appliance.mac_addr

        request_body = {
            "kind": "appliance#erdListEntry",
            "userId": self.user_id,
            "applianceId": appliance.mac_addr,
            "erd": raw_erd_code,
            "value": erd_value,
            "ackTimeout": 10,
            "delay": 0,
        }

        msg_dict = {
            "kind": "websocket#api",
            "action": "api",
            "host": API_HOST,
            "method": "POST",
            "path": f"/v1/appliance/{mac_addr}/erd/{raw_erd_code}",
            "id": f"{mac_addr}-{SET_ERD}-{raw_erd_code}",
            "body": request_body,
        }
        self._pending_erds[(mac_addr, raw_erd_code)] = erd_value
        await self._send_dict(msg_dict)

    async def async_request_update(self, appliance: GeAppliance):
        """Request an appliance send a full update."""
        _LOGGER.debug(f"Requesting update for client {appliance.mac_addr}")
        msg_dict = {
            "kind": "websocket#api",
            "action": "api",
            "host": API_HOST,
            "method": "GET",
            "path": f"/v1/appliance/{appliance.mac_addr}/erd",
            "id": f"{appliance.mac_addr}-{ALL_ERD}"
        }
        await self._send_dict(msg_dict)

    async def async_request_message(self, appliance: GeAppliance):
        """Request an appliance get notification history"""
        _LOGGER.debug(f"Requesting notification history for client {appliance.mac_addr}")
        msg_dict = {
            "kind": "websocket#api",
            "action": "api",
            "host": API_HOST,
            "method": "GET",
            "path": f"/v1/appliance/{appliance.mac_addr}/message",
            "id": f"{appliance.mac_addr}"
        }
        await self._send_dict(msg_dict)

    async def async_request_features(self, appliance: GeAppliance):
        """Request an appliance send features."""
        _LOGGER.debug(f"Requesting features for client {appliance.mac_addr}")
        msg_dict = {
            "kind": "websocket#api",
            "action": "api",
            "host": API_HOST,
            "method": "GET",
            "path": f"/v1/appliance/{appliance.mac_addr}/feature",
            "id": f"{REQUEST_FEATURES}"
        }
        await self._send_dict(msg_dict)

    def _setup_futures(self):
        if self._keepalive_timeout:
            self._keepalive_fut = asyncio.ensure_future(self._keep_alive(self._keepalive_timeout), loop=self.loop)
        if self._list_frequency:
            self._list_fut = asyncio.ensure_future(self._refresh_appliances(self._list_frequency), loop=self.loop)

    def _teardown_futures(self):
        if self._keepalive_fut is not None:
            self._keepalive_fut.cancel()
        if self._list_fut is not None:
            self._list_fut.cancel()

    async def _disconnect(self):
        """Disconnect and cleanup."""
        if self._socket and not self._socket.closed:
            await self._socket.close()
        self._socket = None

    async def _process_pending_erd(self, message_id: str):
        id_parts = message_id.split("-")
        if id_parts[1] != SET_ERD:
            raise ValueError("Invalid message id")
        mac_addr = id_parts[0]
        raw_erd_code = id_parts[2]
        erd_value = self._pending_erds.get((mac_addr, raw_erd_code))
        if erd_value is not None:
            _LOGGER.debug(f"")
            try:
                await self._update_appliance_state(mac_addr, {raw_erd_code: erd_value})
            except KeyError:
                pass

    async def _process_message(self, message: str):
        """
        Process an incoming message.
        """
        message_dict = json.loads(message)  # type: Dict
        try:
            kind = message_dict['kind']
        except KeyError:
            _LOGGER.debug(f"Could not get message kind, skipping message: {message_dict}")
            return

        #if we have a response that indicates success, check it
        if message_dict.get("success", True) != True or message_dict.get("code", 200) != 200:
            if message_dict.get("code") in [401,403] or message_dict.get("reason") == "Access token expired":
                raise GeNeedsReauthenticationError
            raise GeRequestError(message, message_dict.get("code"), message_dict.get("reason"))

        if kind.lower() == "publish#erd":
            await self._process_erd_update(message_dict)
        elif kind.lower() == "websocket#api":
            try:
                message_id = message_dict["id"]
            except KeyError:
                return
            if message_id == LIST_APPLIANCES:
                await self._process_appliance_list(message_dict)
            elif message_id == REQUEST_FEATURES:
                await self._process_appliance_features(message_dict)
            elif f"-{SET_ERD}-" in message_id:
                await self._process_pending_erd(message_id)
            elif f"-{ALL_ERD}" in message_id:
                await self._process_cache_update(message_dict)
            else:
                _LOGGER.debug(f"Unknown message received: {message_dict}")

    async def _process_appliance_list(self, message_dict: Dict):
        """
        Process the appliance list.

        These messages should take the form::

            {"kind": "websocket#api",
             "id": "List-appliances",
             "request":{...},
             "success": True,
             "code": 200,
             "body": {
                "kind": "appliance#applianceList",
                "userId": "USER_ID",
                "items":[
                    {"applianceId": "MAC_ADDR_1",
                     "type": "TYPE_1",
                     "brand": "Unknown",
                     "jid":"<MAC_ADDR_1>_<USER_ID>",
                     "nickname":"NICKNAME",
                     "online":"ONLINE"
                    },
                    ...,
                ],
            }

        :param message_dict:
        """
        body = message_dict["body"]
        if body.get("kind") != "appliance#applianceList":
            raise ValueError("Not an applianceList")
        items = body["items"]
        for item in items:
            mac_addr = item["applianceId"].upper()
            online = item['online'].upper() == "ONLINE"

            #if we already have the appliance, just update it's online status
            if mac_addr in self.appliances:
                await self._set_appliance_availability(self.appliances[mac_addr], online)
                continue

            await self._add_appliance(mac_addr, online)
        await self.async_event(EVENT_GOT_APPLIANCE_LIST, items)

    async def _process_appliance_features(self, message_dict: Dict):
        """
        Process the appliance features.

        These messages should take the form::

            {"kind": "websocket#api",
             "id": "Request-features",
             "request":{...},
             "success": True,
             "code": 200,
             "body": {
                "kind": "appliance#applianceFeature",
                "userId": "USER_ID",
                "applianceId": "APPLIANCE_MAC",
                "features":[
                    "CLOTHES_WASHER_V1_SMART_DISPENSE",
                     "CLOTHES_WASHER_V1_WASHER_LINK",
                     "MORE_FEATURES_IF_AVAILABLE"
                    ],
                },
            }

        :param message_dict:
        """
        body = message_dict["body"]
        if body.get("kind") != "appliance#applianceFeature":
            raise ValueError("Not an applianceFeature")
        items = body["features"]
        mac_addr = body["applianceId"].upper()
        _LOGGER.debug(f'Received features {items} for {mac_addr}')
        if mac_addr in self.appliances:
            await self._set_appliance_features(self.appliances[mac_addr], items)        

        await self.async_event(EVENT_GOT_APPLIANCE_FEATURES, items)

    async def _process_cache_update(self, message_dict: Dict):
        """
        Process an appliance's full cache update.
        
        These messages should take the form::

            {
                "body": {
                    "applianceId": "MAC_ADDRESS",
                    "items": [
                        {"erd": "ERD_CODE_1", "time": "UPDATE_TIMESTAMP_1", "value": "VALUE_1"},
                        ...,
                        {"erd": "ERD_CODE_N", "time": "UPDATE_TIMESTAMP_N", "value": "VALUE_N"},
                    ],
                    "kind": "appliance#erdList",
                    "userId": "USER_ID"
                },
                "code": 200,
                "id": "<MAC_ADDRESS>-allErd",
                "kind": "websocket#api",
                "request": {...},
                "success": True,
            }
        """
        body = message_dict["body"]
        if body.get("kind") != "appliance#erdList":
            raise ValueError("Not an erdList")
        mac_addr = body["applianceId"].upper()
        updates = {i["erd"]: i["value"] for i in body["items"]}
        await self._update_appliance_state(mac_addr, updates)

    async def _process_erd_update(self, message_dict: Dict):
        """
        Process an ERD update (pseudo-HTTP PUBLISH).

        These messages should be in the form::

            {
                "item": {
                    "applianceId": "MAC_ADDRESS",
                    "erd": "ERD_CODE",
                    "time": "UPDATE_TIMESTAMP",
                    "value": "SOME_VALUE",
                },
                "resource": "/appliance/<MAC_ADDRESS>/erd/<ERD_CODE>",
                "kind": "publish#erd",
                "userId":"USER_ID"
            }

        :param message_dict: dict, the json-decoded message.
        """
        item = message_dict["item"]
        mac_addr = item["applianceId"].upper()
        update = {item['erd']: item['value']}
        await self._update_appliance_state(mac_addr, update)

    async def _update_appliance_state(self, mac_addr: str, updates: Dict[ErdCodeType, str]):
        """Update appliance state, performing callbacks if necessary."""
        try:
            appliance = self.appliances[mac_addr]
        except KeyError:
            return
        state_changes = appliance.update_erd_values(updates)
        if state_changes:
            await self.async_event(EVENT_APPLIANCE_STATE_CHANGE, [appliance, state_changes])
        await self.async_event(EVENT_APPLIANCE_UPDATE_RECEIVED, [appliance, updates])

    async def _send_dict(self, msg_dict: Dict[str, Any]):
        """JSON encode a dictionary and send it."""
        payload = json.dumps(msg_dict)
        try:
            #if there's no socket, assume the connection is closed
            if not self.websocket:
                raise websockets.ConnectionClosedOK(1001, 'Socket disconnected')    

            await self.websocket.send(payload)
        except websockets.ConnectionClosed:
            _LOGGER.info("Tried to send a message, but connection already closed.")

    async def _keep_alive(self, keepalive: int = KEEPALIVE_TIMEOUT):
        """Send periodic pings to keep the connection alive."""
        while self.available:
            await asyncio.sleep(keepalive)
            if self.available:
                _LOGGER.debug("Sending keepalive ping")
                await self._send_ping()

    async def _refresh_appliances(self, frequency: int = LIST_APPLIANCES_FREQUENCY):
        """Refresh the appliances list to detect changes over time."""
        while self.available:
            await asyncio.sleep(frequency)
            if self.available:
                _LOGGER.debug("Refreshing appliance list/state")
                await self._get_appliance_list()

    async def _subscribe_all(self):
        """Subscribe to all appliances."""
        msg_dict = {"kind": "websocket#subscribe", "action": "subscribe", "resources": ["/appliance/*/erd/*"]}
        await self._send_dict(msg_dict)   

    async def _subscribe_appliances(self, appliances: List[GeAppliance]):
        """Subscribe to a list of appliances."""
        msg_dict = {
            "kind": "websocket#subscribe",
            "action": "subscribe",
            "resources": [f"/appliance/{appliance.mac_addr}/erd/*" for appliance in appliances]
        }
        await self._send_dict(msg_dict)

    async def _get_appliance_list(self):
        """Request the list of appliances on this account."""
        msg_dict = {
            "kind": "websocket#api",
            "action": "api",
            "host": API_HOST,
            "method": "GET",
            "path": "/v1/appliance",
            "id": LIST_APPLIANCES,
        }
        await self._send_dict(msg_dict)

    async def _send_ping(self):
        """Send a ping."""
        msg_dict = {
            "kind": "websocket#ping",
            "id": "keepalive-ping",
            "action": "ping",
        }
        await self._send_dict(msg_dict)

    async def _add_appliance(self, mac_addr: str, set_online: bool = True):
        """Add an appliance to the registry and request an update."""
        mac_addr = mac_addr.upper()
        if mac_addr in self.appliances:
            raise GeDuplicateApplianceError(f'Trying to add duplicate appliance {mac_addr}')
        new_appliance = GeAppliance(mac_addr, self)
        if set_online:
            new_appliance.set_available()

        _LOGGER.debug(f'Adding appliance {mac_addr}')
        self.appliances[mac_addr] = new_appliance
        await self.async_event(EVENT_ADD_APPLIANCE, new_appliance)
        await self.async_request_update(new_appliance)
        await self.async_request_features(new_appliance)
