import enum
from typing import Optional

@enum.unique
class ErdWaterFilterPosition(enum.Enum):
    BYPASS = 0
    OFF = 1
    FILTERED = 2
    READY = 3
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.title()
