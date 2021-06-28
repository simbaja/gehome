import enum
from typing import Optional

@enum.unique
class ErdWaterFilterLeakValidity(enum.Enum):
    HAS_LEAK = "01"
    NONE = "00"

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.title()