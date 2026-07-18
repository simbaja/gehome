import enum
from typing import Optional


@enum.unique
class ErdToasterOvenState(enum.Enum):
    """Current state values for `ErdCode.TOASTER_OVEN_CURRENT_STATE` (0x9209)."""
    SLEEP = 0
    STANDBY = 1
    INITIALIZATION = 2
    COOKING = 3
    PREHEATING = 4
    IDLE = 5
    TEMPERATURE_ACHIEVED = 6
    COOKING_COMPLETE = 7
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        return self.stringify() or ""
