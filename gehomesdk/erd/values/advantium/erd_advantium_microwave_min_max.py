from typing import NamedTuple, Optional

class ErdAdvantiumMicrowaveMinMax(NamedTuple):
    is_valid: bool
    min_time: int
    max_time: int
    slow_cook_min_time: int
    slow_cook_max_time: int

    raw_value: Optional[str]
