import enum
from typing import NamedTuple, Optional


@enum.unique
class ErdCcmGrindBrewStrength(enum.Enum):
    LIGHT = 0
    MEDIUM = 1
    BOLD = 2
    GOLD = 3

    UNKNOWN = 255

    def stringify(self, **kwargs) -> str:
        return self.name.replace("_", " ").title()


class ErdCcmGrindBrewSettings(NamedTuple):
    """12-byte adhoc brew settings for Cafe Speciality Grind & Brew (ERD 0x9051)."""

    gold_toggle: bool = False
    bloom_toggle: bool = False
    single_toggle: bool = False
    brew_strength: ErdCcmGrindBrewStrength = ErdCcmGrindBrewStrength.MEDIUM
    brew_temperature: int = 200
    ounces: int = 10
    number_of_cups: int = 6
    bloom_time: int = 0
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return (
            f"cups: {self.number_of_cups}, "
            f"strength: {self.brew_strength.stringify()}, "
            f"temperature: {self.brew_temperature}"
        )
