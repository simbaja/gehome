import enum
from typing import Optional


@enum.unique
class ErdWaterHeaterMode(enum.Enum):
    HYBRID = 0
    STANDARD_ELECTRIC = 1
    HEAT_PUMP = 2
    HIGH_DEMAND = 3
    VACATION = 4
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterMode.UNKNOWN:
            return None
        return self.name.title().replace("_", " ")
