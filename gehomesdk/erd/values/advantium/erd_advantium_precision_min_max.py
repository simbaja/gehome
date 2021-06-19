from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumPrecisionMinMax(NamedTuple):
    """Defines min/max precision cook settings"""
    is_valid: bool
    min_time: timedelta
    max_time: timedelta
    custom_low_min_time: timedelta
    custom_low_max_time: timedelta
    custom_high_min_time: timedelta
    custom_high_max_time: timedelta

    raw_value: Optional[str]
