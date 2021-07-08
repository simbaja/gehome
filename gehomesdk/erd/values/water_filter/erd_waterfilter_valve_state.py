import enum
from typing import Optional

@enum.unique
class ErdWaterFilterValveState(enum.Enum):
    BYPASS = 0
    OFF = 1
    FILTERED = 2
    MANUAL_OVERRIDE = 3
    DRIVING = 4
    FAULT = 5
    INVALID = 6

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_"," ").title()
