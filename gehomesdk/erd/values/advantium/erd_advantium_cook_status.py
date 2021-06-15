from typing import NamedTuple, Optional
from .advantium_enums import *

class ErdAdvantiumCookStatus (NamedTuple):
    cook_action: CookAction = CookAction.STOP
    cook_mode: CookMode = CookMode.NO_MODE
    termination_reason: TerminationReason = TerminationReason.UNKNOWN
    preheat_status: PreheatStatus = PreheatStatus.NO_PREHEAT
    temperature: int = 0
    power_level: int = 0
    door_status: DoorStatus = DoorStatus.CLOSED
    sensing_active: SensingActive = SensingActive.INACTIVE
    cooling_fan_status: CoolingFanStatus = CoolingFanStatus.OFF
    oven_light_status: OvenLightStatus = OvenLightStatus.OFF
    warm_status: WarmStatus = WarmStatus.OFF
    raw_value: Optional[str] = None
