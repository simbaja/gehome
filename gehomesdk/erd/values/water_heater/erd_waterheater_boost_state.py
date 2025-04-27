import enum
from typing import Optional


@enum.unique
class ErdWaterHeaterBoostState(enum.Enum):
    DISABLED = 0
    ENABLED = 1
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterBoostState.UNKNOWN:
            return None
        return self.name.title()
