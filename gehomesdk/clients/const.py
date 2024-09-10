"""Constants"""

# OAuth2 credentials
FIELD_TRIAL = True

if FIELD_TRIAL:
  OAUTH2_APP_ID = "com.ge.kitchen.wca.prd.android"
  OAUTH2_CLIENT_ID= "55527330624d73306a63565a554f612b337a3842"
  OAUTH2_CLIENT_SECRET = "714c6574425736715763426e35554778625351684b4f654f3847654d7343733d"
  OAUTH2_REDIRECT_URI ="brillion.6c454f4c53673173385179514c4348616e452b63://oauth/redirect"
  LOGIN_URL = "https://accounts-fld.brillion.geappliances.com"
  API_URL = "https://api-fld.brillion.geappliances.com"
else:
  OAUTH2_APP_ID = "com.ge.kitchen.wca.prd.android"
  OAUTH2_CLIENT_ID = "564c31616c4f7474434b307435412b4d2f6e7672"
  OAUTH2_CLIENT_SECRET = "6476512b5246446d452f697154444941387052645938466e5671746e5847593d"
  OAUTH2_REDIRECT_URI = "brillion.4e617a766474657344444e562b5935566e51324a://oauth/redirect"
  LOGIN_URL = "https://accounts.brillion.geappliances.com"
  API_URL = "https://api.brillion.geappliances.com"

SECURE_URL = "https://secure.brillion.geappliances.com"

LOGIN_REGIONS = {
  "US": "us-east-1",
  "EU": "eu-west-1"
}
LOGIN_REGION_COOKIE_NAME = "abgea_region"
LOGIN_COOKIE_DOMAIN = "accounts.brillion.geappliances.com"

MAX_RETRIES = 1
RETRY_INTERVAL = 10

EVENT_ADD_APPLIANCE = "add_appliance"
EVENT_APPLIANCE_INITIAL_UPDATE = "appliance_got_type"
EVENT_APPLIANCE_STATE_CHANGE = "appliance_state_change"
EVENT_APPLIANCE_AVAILABLE = "appliance_available"
EVENT_APPLIANCE_UNAVAILABLE = "appliance_unavailable"
EVENT_APPLIANCE_UPDATE_RECEIVED = "appliance_update_received"
EVENT_APPLIANCE_NOTIFICATION_RECEIVED = "appliance_notification_received"
EVENT_CONNECTED = "connected"
EVENT_DISCONNECTED = "disconnected"
EVENT_GOT_APPLIANCE_LIST = "got_appliance_list"
EVENT_GOT_APPLIANCE_FEATURES = "got_appliance_features"
EVENT_STATE_CHANGED = "state_changed"
