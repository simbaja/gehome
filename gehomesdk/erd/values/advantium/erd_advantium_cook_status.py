from typing import NamedTuple, Optional
from .advantium_enums import *

class ErdAdvantiumCookStatus (NamedTuple):
    cook_action: AdvantiumCookAction = AdvantiumCookAction.STOP
    cook_mode: AdvantiumCookMode = AdvantiumCookMode.NO_MODE
    termination_reason: AdvantiumTerminationReason = AdvantiumTerminationReason.UNKNOWN
    preheat_status: AdvantiumPreheatStatus = AdvantiumPreheatStatus.NO_PREHEAT
    temperature: int = 0
    power_level: int = 0
    door_status: AdvantiumDoorStatus = AdvantiumDoorStatus.CLOSED
    sensing_active: AdvantiumSensingActive = AdvantiumSensingActive.INACTIVE
    cooling_fan_status: AdvantiumCoolingFanStatus = AdvantiumCoolingFanStatus.OFF
    oven_light_status: AdvantiumOvenLightStatus = AdvantiumOvenLightStatus.OFF
    warm_status: AdvantiumWarmStatus = AdvantiumWarmStatus.OFF
    raw_value: Optional[str] = None
