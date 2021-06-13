from typing import NamedTuple, Optional


class ErdAdvantiumKitchenTimerMinMax(NamedTuple):
    #time in seconds
    min_time: int
    max_time: int
    raw_value: Optional[str]
