import enum
from typing import Optional


@enum.unique
class ErdWaterHeaterBoostControl(enum.Enum):
    OFF = 0
    ON = 1
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterBoostControl.UNKNOWN:
            return None
        return self.name.title()

    def boolify(self) -> Optional[bool]:
        return self == ErdWaterHeaterBoostControl.ON   