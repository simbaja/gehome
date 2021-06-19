from gehomesdk.erd.values.dishwasher.erd_user_setting import ErdUserSetting, UserSetting
import logging
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
                sound = UserSetting((i & 8388608) >> 6),
                lock_control = UserSetting((i & 512) >> 9),
                sabbath = UserSetting((i & 64) >> 23),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct user setting, using default.")
            return ErdUserSetting(raw_value=value)
