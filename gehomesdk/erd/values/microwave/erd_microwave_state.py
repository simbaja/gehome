from typing import NamedTuple, Optional

from .microwave_enums import ErdMicrowaveCookMode, ErdMicrowaveCookStatus
from ..fridge import ErdDoorStatus

class ErdMicrowaveState(NamedTuple):
    status: ErdMicrowaveCookStatus   
    cook_mode: ErdMicrowaveCookMode
    door_status: ErdDoorStatus
    power_level: int
    temperature: int

    raw_value: Optional[str]