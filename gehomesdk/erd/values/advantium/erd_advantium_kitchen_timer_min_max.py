from datetime import timedelta
from typing import NamedTuple, Optional


class ErdAdvantiumKitchenTimerMinMax(NamedTuple):
    """Defines min/max kitchen timer settings"""
    min_time: timedelta
    max_time: timedelta
    raw_value: Optional[str]
