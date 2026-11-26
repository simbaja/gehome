from datetime import timedelta
from typing import NamedTuple

class ErdAdvantiumMicrowaveMinMax(NamedTuple):
    """Defines min/max microwave settings"""
    is_valid: bool
    min_time: timedelta | None = None
    max_time: timedelta | None = None
    slow_cook_min_time: timedelta | None = None
    slow_cook_max_time: timedelta | None = None

    raw_value: str | None = None
