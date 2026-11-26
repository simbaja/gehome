from datetime import timedelta
from typing import NamedTuple

from .erd_toaster_oven_cook_mode import ErdToasterOvenCookMode
from .erd_toaster_oven_size import ErdToasterOvenSize


class ToasterOvenCookSetting(NamedTuple):
    """
    Cleaner representation of the toaster oven cook setting ERDs (0x9207/0x9208):
    target temperature, cook time, cook mode, and the mode-specific fields
    (shade, size, count, preferences) used by only some cook modes.
    """
    cook_mode: ErdToasterOvenCookMode | None = None
    temperature: int = 0
    cook_time: timedelta = timedelta(0)
    shade: int = 0
    size: ErdToasterOvenSize | None = None
    item_count: int = 0
    preferences: int = 0
    raw_string: str | None = None

    def stringify(self, **kwargs) -> str | None:
        """Format ToasterOvenCookSetting values nicely."""
        if self.cook_mode is None:
            return None

        temp_units = kwargs.get("temp_units", "°")
        temp_str = f" ({self.temperature}{temp_units})" if self.temperature else ""

        return f"{self.cook_mode.stringify(**kwargs)}{temp_str}"

    def __str__(self) -> str:
        return self.stringify() or ""
