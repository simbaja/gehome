from typing import NamedTuple
from .erd_filter_status import ErdFilterStatus

class FridgeWaterFilterStatus(NamedTuple):
    status: ErdFilterStatus
    percent_remaining: int
    days_remaining: int
    days_since_expired: int
    dispenses_since_expired: int
