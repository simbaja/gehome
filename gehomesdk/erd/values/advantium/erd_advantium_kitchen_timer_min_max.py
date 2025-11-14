from datetime import timedelta
from typing import NamedTuple, Optional


class ErdAdvantiumKitchenTimerMinMax(NamedTuple):
    """Defines min/max kitchen timer settings"""
    min_time: Optional[timedelta] = None
    max_time: Optional[timedelta] = None
    raw_value: Optional[str] = None
