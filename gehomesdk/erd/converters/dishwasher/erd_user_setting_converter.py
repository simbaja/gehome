import logging
from gehomesdk.erd.values.dishwasher.erd_user_setting import (
    ErdUserSetting, 
    UserSetting, 
    UserCycleSetting, 
    UserWashTempSetting,
    UserDryOptionSetting,
    UserWashZoneSetting
)
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.dishwasher import ErdUserSetting

_LOGGER = logging.getLogger(__name__)

class ErdUserSettingConverter(ErdReadOnlyConverter[ErdUserSetting]):
    def erd_decode(self, value: str) -> ErdUserSetting:
        if not value:
            return ErdUserSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return ErdUserSetting(
                bottle_jet = UserSetting(i & 1),
                cycle_mode = UserCycleSetting(i & 14 >> 1),
                sabbath = UserSetting((i & 64) >> 6),
                presoak = UserSetting((i & 256) >> 8),
                lock_control = UserSetting((i & 512) >> 9),
                dry_option = UserDryOptionSetting((i & 3072) >> 10),
                wash_temp = UserWashTempSetting((i & 12288) >> 12),
                delay_hours = (i & 983040) >> 16,
                wash_zone = UserWashZoneSetting((i & 3145728) >> 20),
                sound = UserSetting((i & 8388608) >> 23),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct user setting, using default.")
            return ErdUserSetting(raw_value=value)
