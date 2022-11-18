import logging
from gehomesdk.erd.values.dishwasher.erd_user_setting import (
    ErdUserSetting, 
    UserSetting, 
    UserCycleSetting, 
    UserWashTempSetting,
    UserDryOptionSetting,
    UserWashZoneSetting
)
from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values.dishwasher import ErdUserSetting

_LOGGER = logging.getLogger(__name__)

class ErdUserSettingConverter(ErdReadWriteConverter[ErdUserSetting]):
    def erd_decode(self, value: str) -> ErdUserSetting:
        if not value:
            return ErdUserSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return ErdUserSetting(
                bottle_jet = UserSetting(i & 1),
                cycle_mode = UserCycleSetting((i & 14) >> 1),   #missing brackets added by Nick
                sabbath = UserSetting((i & 64) >> 6),
                presoak = UserSetting((i & 256) >> 8),
                lock_control = UserSetting((i & 512) >> 9),
                dry_option = UserDryOptionSetting((i & 3072) >> 10),
                wash_temp = UserWashTempSetting((i & 12288) >> 12),
                rinse_aid = UserSetting((i & 32768) >> 15),
                delay_hours = (i & 983040) >> 16,
                wash_zone = UserWashZoneSetting((i & 3145728) >> 20),
                demo_mode = UserSetting((i & 4194304) >> 22),
                mute = UserSetting((i & 8388608) >> 23),
                raw_value=value
            )
        except Exception as ex: 
            _LOGGER.exception("Could not construct user setting, using default.")
            return ErdUserSetting(raw_value=value)
            
    def erd_encode(self, value: int) -> str:
        """
        return the Dishwasher user setting value
        """
        return '{:06X}'.format(value)
            
class ErdUserCycleSettingConverter(ErdReadWriteConverter[UserCycleSetting]):
    def erd_decode(self, value: str) -> UserCycleSetting:
        if not value:
            return UserCycleSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return UserCycleSetting(i)
        except Exception as ex: 
            _LOGGER.exception("Could not construct user cycle setting, using default.")
            return UserCycleSetting(raw_value=value)
            
    def erd_encode(self, value: UserCycleSetting) -> str:
        """
        return the Dishwasher cycle setting value
        """
        return (
            '{:02d}'.format(value.value)
        )
        
class ErdUserTemperatureSettingConverter(ErdReadWriteConverter[UserWashTempSetting]):
    def erd_decode(self, value: str) -> UserWashTempSetting:
        if not value:
            return UserWashTempSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return UserWashTempSetting(i)
        except Exception as ex: 
            _LOGGER.exception("Could not construct user cycle setting, using default.")
            return UserWashTempSetting(raw_value=value)
            
    def erd_encode(self, value: UserWashTempSetting) -> str:
        """
        return the Dishwasher temperature setting value
        """
        return (
            '{:02d}'.format(value.value)
        )
        
class ErdUserDryingSettingConverter(ErdReadWriteConverter[UserDryOptionSetting]):
    def erd_decode(self, value: str) -> UserDryOptionSetting:
        if not value:
            return UserDryOptionSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return UserDryOptionSetting(i)
        except Exception as ex: 
            _LOGGER.exception("Could not construct user cycle setting, using default.")
            return UserDryOptionSetting(raw_value=value)
            
    def erd_encode(self, value: UserDryOptionSetting) -> str:
        """
        return the Dishwasher drying setting value
        """
        return (
            '{:02d}'.format(value.value)
        )
        
class ErdUserZoneSettingConverter(ErdReadWriteConverter[UserWashZoneSetting]):
    def erd_decode(self, value: str) -> UserWashZoneSetting:
        if not value:
            return UserWashZoneSetting()
        
        try:
            #convert to int
            i = erd_decode_int(value)
            
            return UserWashZoneSetting(i)
        except Exception as ex: 
            _LOGGER.exception("Could not construct user cycle setting, using default.")
            return UserWashZoneSetting(raw_value=value)
            
    def erd_encode(self, value: UserWashZoneSetting) -> str:
        """
        return the Dishwasher wash zone setting value
        """
        return (
            '{:02d}'.format(value.value)
        )
