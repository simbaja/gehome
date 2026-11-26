from datetime import timedelta
from typing import NamedTuple

class ErdAdvantiumCookTimeMinMax(NamedTuple):
    """Defines min/max cook times in various modes (in seconds)"""
    is_valid: bool
    convection_min_time: timedelta | None = None
    convection_max_time: timedelta | None = None
    broil_min_time: timedelta | None = None
    broil_max_time: timedelta | None = None
    warm_min_time: timedelta | None = None
    warm_max_time: timedelta | None = None
    proof_min_time: timedelta | None = None
    proof_max_time: timedelta | None = None
    slow_cook_min_time: timedelta | None = None
    slow_cook_max_time: timedelta | None = None

    raw_value: str | None = None
