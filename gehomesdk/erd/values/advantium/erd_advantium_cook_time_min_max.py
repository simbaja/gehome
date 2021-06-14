from typing import NamedTuple, Optional

class ErdAdvantiumCookTimeMinMax(NamedTuple):
    is_valid: bool
    convection_min_time: int
    convection_max_time: int
    broil_min_time: int
    broil_max_time: int
    warm_min_time: int
    warm_max_time: int
    proof_min_time: int
    proof_max_time: int
    slow_cook_min_time: int
    slow_cook_max_time: int

    raw_value: Optional[str]
