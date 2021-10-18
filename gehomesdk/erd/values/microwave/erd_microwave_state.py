from typing import NamedTuple, Optional

from .microwave_enums import ErdMicrowaveCookMode, ErdMicrowaveCookStatus, ErdMicrowaveDoorStatus

class ErdMicrowaveState(NamedTuple):
    status: ErdMicrowaveCookStatus   
    cook_mode: ErdMicrowaveCookMode
    door_status: ErdMicrowaveDoorStatus
    power_level: int
    temperature: int

    raw_value: Optional[str]