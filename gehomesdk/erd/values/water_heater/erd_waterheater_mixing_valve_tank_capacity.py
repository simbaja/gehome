import enum
from typing import Optional, NamedTuple


@enum.unique
class ErdWaterHeaterMixingValveTankCapacity(enum.Enum):
    NORMAL = 0
    HIGH = 1
    X_HIGH = 2
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterMixingValveTankCapacity.UNKNOWN:
            return None
        return self.name.title().replace("_", "-")
    
class ErdWaterHeaterMixingValveAvailableTankCapacities(NamedTuple):
    has_normal: bool
    has_high: bool
    has_x_high: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"Normal: {self.has_normal}, High: {self.has_high}, X-High: {self.has_x_high}"
