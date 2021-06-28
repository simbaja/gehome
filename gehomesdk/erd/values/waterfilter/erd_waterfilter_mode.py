import enum
from typing import Optional

@enum.unique
class ErdWaterFilterMode(enum.Enum):
    BYPASS = "00"
    OFF = "01"
    FILTERED = "02"
    UNKNOWN = "-1"

    def stringify(self, **kwargs) -> Optional[str]:
        if self.value == ErdWaterFilterMode.UNKNOWN:
            return None
        return self.name.title()