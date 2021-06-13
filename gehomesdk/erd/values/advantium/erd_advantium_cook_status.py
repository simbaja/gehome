from typing import NamedTuple, Optional
from .advantium_enums import *

class ErdAdvantiumCookStatus (NamedTuple):
    cook_action: CookAction
    cook_mode: CookMode
    termination_reason: TerminationReason
    preheat_status: PreheatStatus
    temperature: int
    power_level: int
    door_status: DoorStatus
    sensing_active: SensingActive
    cooling_fan_status: CoolingFanStatus
    oven_light_status: OvenLightStatus
    warm_status: WarmStatus
    raw_value: Optional[str]
