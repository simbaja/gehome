import enum
from typing import NamedTuple, Optional

@enum.unique
class UserSetting(enum.Enum):
    DISABLE = 0
    ENABLE = 1
    INVALID = 255

@enum.unique
class UserCycleSetting(enum.Enum):
    AUTO = 0
    INTENSE = 1
    NORMAL = 2
    DELICATE = 3
    THIRTY_MIN = 4
    ECO = 5
    RINSE = 6

@enum.unique
class UserWashTempSetting(enum.Enum):
    NORMAL = 0
    BOOST = 1
    SANITIZE = 2
    BOOST_AND_SANITIZE = 3

@enum.unique
class UserDryOptionSetting(enum.Enum):
    OFF = 0
    POWER_DRY = 1
    MAX_DRY = 2

@enum.unique
class UserWashZoneSetting(enum.Enum):
    BOTH = 0
    LOWER = 1
    UPPER = 2

class ErdUserSetting (NamedTuple):
    mute: UserSetting = UserSetting.DISABLE
    demo_mode: UserSetting = UserSetting.DISABLE
    lock_control: UserSetting = UserSetting.DISABLE
    sabbath: UserSetting = UserSetting.DISABLE
    cycle_mode: UserCycleSetting = UserCycleSetting.AUTO
    presoak: UserSetting = UserSetting.DISABLE
    bottle_jet: UserSetting = UserSetting.DISABLE
    wash_temp: UserWashTempSetting = UserWashTempSetting.NORMAL
    rinse_aid: UserSetting = UserSetting.DISABLE
    dry_option: UserDryOptionSetting = UserDryOptionSetting.OFF
    wash_zone: UserWashZoneSetting = UserWashZoneSetting.BOTH
    delay_hours: int = 0
    raw_value: Optional[str] = None
