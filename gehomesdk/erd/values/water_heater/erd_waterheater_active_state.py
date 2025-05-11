import enum
from typing import Optional


@enum.unique
class ErdWaterHeaterActiveState(enum.Enum):
    OFF = 0
    ON = 1
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterActiveState.UNKNOWN:
            return None
        return self.name.title()