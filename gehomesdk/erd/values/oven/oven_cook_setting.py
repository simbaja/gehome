from datetime import time, timedelta
from typing import NamedTuple, Optional

from .const import *
from .oven_cook_mode import OvenCookMode 
from .erd_oven_state import ErdOvenState

class OvenCookSetting(NamedTuple):
    """Cleaner representation of ErdOvenCookMode"""
    cook_mode: OvenCookMode = OvenCookMode(ErdOvenState.NO_MODE, False, False, False)
    temperature: int = 0
    cook_time: timedelta = timedelta(0)
    probe_temperature: int = 0
    delay_time: timedelta = timedelta(0)
    two_temp_cook_temperature: int = 0
    two_temp_cook_time: timedelta = timedelta(0)
    raw_string: str = None
    raw_bytes: Optional[bytes] = None

    def stringify(self, **kwargs) -> Optional[str]:
        """Format OvenCookSetting values nicely."""
        cook_state = self.cook_mode.oven_state
        temp_units = kwargs.get("temp_units", "°")

        modifiers = []
        if self.cook_mode.timed:
            modifiers.append(STATE_OVEN_TIMED)
        if self.cook_mode.delayed:
            modifiers.append(STATE_OVEN_DELAY)
        if self.cook_mode.probe:
            modifiers.append(STATE_OVEN_PROBE)
        if self.cook_mode.sabbath:
            modifiers.append(STATE_OVEN_SABBATH)

        temp_str = f" ({self.temperature}{temp_units})" if self.temperature > 0 else ""
        modifier_str = f" ({', '.join(modifiers)})" if modifiers else ""
        display_state = cook_state.stringify(**kwargs)

        if display_state in [STATE_OVEN_UNKNOWN, STATE_OVEN_OFF]:
            return display_state
            
        return f"{display_state}{temp_str}{modifier_str}"
    def __str__(self) -> str:
        return self.stringify() or ""
