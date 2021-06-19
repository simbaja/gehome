from datetime import timedelta
from typing import NamedTuple, Optional

class ErdAdvantiumCookTimeMinMax(NamedTuple):
    """Defines min/max cook times in various modes (in seconds)"""
    is_valid: bool
    convection_min_time: timedelta
    convection_max_time: timedelta
    broil_min_time: timedelta
    broil_max_time: timedelta
    warm_min_time: timedelta
    warm_max_time: timedelta
    proof_min_time: timedelta
    proof_max_time: timedelta
    slow_cook_min_time: timedelta
    slow_cook_max_time: timedelta

    raw_value: Optional[str]
