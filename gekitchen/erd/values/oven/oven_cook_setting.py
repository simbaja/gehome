from typing import NamedTuple, Optional
from .oven_cook_mode import OvenCookMode 

class OvenCookSetting(NamedTuple):
    """Cleaner representation of ErdOvenCookMode"""
    cook_mode: OvenCookMode
    temperature: int
    raw_bytes: Optional[bytes] = None

