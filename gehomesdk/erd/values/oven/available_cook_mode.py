from typing import NamedTuple
from .erd_oven_cook_mode import ErdOvenCookMode

class AvailableCookMode(NamedTuple):
    """Parsing helper for Available Cook Modes"""
    byte: int
    mask: int
    cook_mode: ErdOvenCookMode
