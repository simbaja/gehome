from typing import NamedTuple, Optional

class ErdAdvantiumPrecisionMinMax(NamedTuple):
    is_valid: bool
    min_time: int
    max_time: int
    custom_low_min_time: int
    custom_low_max_time: int
    custom_high_min_time: int
    custom_high_max_time: int

    raw_value: Optional[str]
