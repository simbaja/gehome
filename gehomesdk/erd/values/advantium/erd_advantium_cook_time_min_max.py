from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumCookTimeMinMax(NamedTuple):
    """Defines min/max cook times in various modes (in seconds)"""
    is_valid: bool
    convection_min_time: Optional[timedelta] = None
    convection_max_time: Optional[timedelta] = None
    broil_min_time: Optional[timedelta] = None
    broil_max_time: Optional[timedelta] = None
    warm_min_time: Optional[timedelta] = None
    warm_max_time: Optional[timedelta] = None
    proof_min_time: Optional[timedelta] = None
    proof_max_time: Optional[timedelta] = None
    slow_cook_min_time: Optional[timedelta] = None
    slow_cook_max_time: Optional[timedelta] = None

    raw_value: Optional[str] = None
