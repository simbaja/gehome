from typing import NamedTuple, Optional

class ErdMicrowaveAvailableModes(NamedTuple):
    is_valid: bool   
    has_warm: bool
    has_convection_bake: bool
    has_convection_roast: bool
    has_broil: bool

    raw_value: Optional[str]