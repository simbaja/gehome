import enum
from typing import Optional, NamedTuple

@enum.unique
class ErdCcmBrewStrength(enum.Enum):
    LIGHT = 1
    MEDIUM = 2
    BOLD = 3
    GOLD = 4

    UNKNOWN = 255

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

class ErdCcmBrewTemperatureRange(NamedTuple):
    min: int
    max: int
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"min: {self.min}, max: {self.max}"

class ErdCcmBrewSettings(NamedTuple):
    number_of_cups: int = 0
    brew_strength: ErdCcmBrewStrength = ErdCcmBrewStrength.UNKNOWN
    brew_temperature: int = 0
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return f"number of cups: {self.number_of_cups}, srength: {self.brew_strength}, temperature: {self.brew_temperature}"