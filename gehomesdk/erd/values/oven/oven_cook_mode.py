from typing import NamedTuple
from .erd_oven_state import ErdOvenState

class OvenCookMode(NamedTuple):
    """Named tuple to represent ErdOvenCookMode for easier formatting later"""
    oven_state: ErdOvenState
    delayed: bool = False
    timed: bool = False
    probe: bool = False
    warm: bool = False
    sabbath: bool = False
