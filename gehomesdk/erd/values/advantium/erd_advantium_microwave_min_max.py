from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumMicrowaveMinMax(NamedTuple):
    """Defines min/max microwave settings"""
    is_valid: bool
    min_time: timedelta
    max_time: timedelta
    slow_cook_min_time: timedelta
    slow_cook_max_time: timedelta

    raw_value: Optional[str]
