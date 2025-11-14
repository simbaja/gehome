from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumMicrowaveMinMax(NamedTuple):
    """Defines min/max microwave settings"""
    is_valid: bool
    min_time: Optional[timedelta] = None
    max_time: Optional[timedelta] = None
    slow_cook_min_time: Optional[timedelta] = None
    slow_cook_max_time: Optional[timedelta] = None

    raw_value: Optional[str] = None
