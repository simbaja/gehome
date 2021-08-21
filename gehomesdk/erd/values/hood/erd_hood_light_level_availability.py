from typing import NamedTuple

class ErdHoodLightLevelAvailability(NamedTuple):
    off_available: bool = False
    dim_available: bool = False
    on_available: bool = False
    raw_value: str = None
