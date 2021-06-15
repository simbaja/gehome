"""GE Client implementations"""

import logging
from .const import (
    EVENT_ADD_APPLIANCE,
    EVENT_APPLIANCE_INITIAL_UPDATE,
    EVENT_APPLIANCE_STATE_CHANGE,
    EVENT_APPLIANCE_AVAILABLE,
    EVENT_APPLIANCE_UNAVAILABLE,
    EVENT_APPLIANCE_UPDATE_RECEIVED,
    EVENT_CONNECTED,
    EVENT_DISCONNECTED,
    EVENT_GOT_APPLIANCE_LIST,
    EVENT_GOT_APPLIANCE_FEATURES,
    EVENT_STATE_CHANGED 
)
from .base_client import GeBaseClient
from .websocket_client import GeWebsocketClient
from .async_login_flows import async_get_oauth2_token, async_refresh_oauth2_token

_LOGGER = logging.getLogger(__name__)

try:
    from .xmpp_client import GeXmppClient
except ImportError:
    _LOGGER.info("XMPP client not avaible.  You may need to install slximpp.")
