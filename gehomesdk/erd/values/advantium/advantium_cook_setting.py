import enum
from enum import auto
from typing import NamedTuple, Optional
from .advantium_enums import *

@enum.unique
class CookClass(enum.Enum):
    MICROWAVE = auto(),


class AdvantiumCookSetting(NamedTuple):
    cook_mode: CookMode = CookMode.NO_MODE
    warm_status: Optional[WarmStatus] = None
    target_temperature_120v_f: Optional[int] = None
    target_temperature_240v_f: Optional[int] = None
    target_power_level: Optional[int] = None
    default_cook_time: int = 0
    allow_temperature_set: bool = False
