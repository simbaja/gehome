import enum
from typing import Optional

@enum.unique
class ErdWaterFilterMode(enum.Enum):
    BYPASS = 0
    OFF = 1
    FILTERED = 2
    TRANSITION = 3
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self.value == ErdWaterFilterMode.UNKNOWN:
            return None
        return self.name.title()
