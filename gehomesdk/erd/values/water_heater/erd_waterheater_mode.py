import enum
from typing import Optional, NamedTuple


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

class ErdWaterHeaterAvailableModes(NamedTuple):
    has_hybrid: bool
    has_standard_electric: bool
    has_e_heat: bool
    has_hi_demand: bool
    has_vacation: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"Hybrid: {self.has_hybrid}, \
            Standard Electric: {self.has_standard_electric}, \
            E-Heat: {  self.has_e_heat}, \
            HiDemand {self.has_hi_demand}, \
            Vacation: {self.has_vacation}"