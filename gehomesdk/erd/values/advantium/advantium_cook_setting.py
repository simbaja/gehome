import enum
from enum import auto
from typing import NamedTuple
from .advantium_enums import AdvantiumCookMode, AdvantiumWarmStatus

@enum.unique
class CookClass(enum.Enum):
    MICROWAVE = auto(),


class AdvantiumCookSetting(NamedTuple):
    cook_mode: AdvantiumCookMode = AdvantiumCookMode.NO_MODE
    warm_status: AdvantiumWarmStatus | None = None
    target_temperature_120v_f: int | None = None
    target_temperature_240v_f: int | None = None
    target_power_level: int | None = None
    default_cook_time: int = 0
    allow_temperature_set: bool = False
