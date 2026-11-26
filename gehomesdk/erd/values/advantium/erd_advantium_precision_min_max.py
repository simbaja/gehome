from datetime import timedelta
from typing import NamedTuple

class ErdAdvantiumPrecisionMinMax(NamedTuple):
    """Defines min/max precision cook settings"""
    is_valid: bool
    min_time: timedelta | None = None
    max_time: timedelta | None = None
    custom_low_min_time: timedelta | None = None
    custom_low_max_time: timedelta | None = None
    custom_high_min_time: timedelta | None = None
    custom_high_max_time: timedelta | None = None

    raw_value: str | None = None
