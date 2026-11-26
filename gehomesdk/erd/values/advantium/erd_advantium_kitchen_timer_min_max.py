from datetime import timedelta
from typing import NamedTuple


class ErdAdvantiumKitchenTimerMinMax(NamedTuple):
    """Defines min/max kitchen timer settings"""
    min_time: timedelta | None = None
    max_time: timedelta | None = None
    raw_value: str | None = None
