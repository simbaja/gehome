from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumPrecisionMinMax(NamedTuple):
    """Defines min/max precision cook settings"""
    is_valid: bool
    min_time: Optional[timedelta] = None
    max_time: Optional[timedelta] = None
    custom_low_min_time: Optional[timedelta] = None
    custom_low_max_time: Optional[timedelta] = None
    custom_high_min_time: Optional[timedelta] = None
    custom_high_max_time: Optional[timedelta] = None

    raw_value: Optional[str] = None
