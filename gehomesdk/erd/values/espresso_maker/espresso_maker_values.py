import enum
from typing import FrozenSet, NamedTuple, Optional

@enum.unique
class ErdEspressoBrewType(enum.Enum):
    ESPRESSO = 0
    AMERICANO = 1
    LUNGO = 2
    HOT_WATER = 3
    STEAM = 4
    RISTRETTO = 5
    DOPPIO = 6
    TRIPLE_SHOT = 7
    RED_EYE = 8
    MY_CUP = 9

    UNKNOWN = 255

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdEspressoBrewType.MY_CUP:
            return "MyCup"
        return self.name.replace("_", " ").title()

@enum.unique
class ErdEspressoWaterHardness(enum.Enum):
    VERY_SOFT = 0
    SOFT = 1
    HARD = 2
    VERY_HARD = 3

    UNKNOWN = 255

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_", " ").title()

@enum.unique
class ErdEspressoSteamKnobPosition(enum.Enum):
    OFF = 0
    STEAM = 1
    HOT_WATER = 2

    UNKNOWN = 255

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_", " ").title()

class ErdEspressoBrewParameters(NamedTuple):
    """Current/requested brew (0x901D/0x901E, 0x904A/0x904B)"""
    temperature: float = 0          # Celsius
    brew_type: ErdEspressoBrewType = ErdEspressoBrewType.UNKNOWN
    volume: int = 0                 # mL
    grind_time: float = 0           # seconds
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return f"{self.brew_type.stringify()}, {self.volume} mL, {self.temperature:.1f} C, {self.grind_time:.1f} s grind"

class ErdEspressoDrinkParameters(NamedTuple):
    """Per-drink stored parameters (0x9029-0x9041, odd = current, even = requested)"""
    temperature: float = 0          # Celsius
    grind_time: float = 0           # seconds
    volume: int = 0                 # mL
    my_cup_button: bool = False
    min_temperature: float = 0
    max_temperature: float = 0
    min_grind_time: float = 0
    max_grind_time: float = 0
    min_volume: int = 0
    max_volume: int = 0
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return f"{self.volume} mL, {self.temperature:.1f} C, {self.grind_time:.1f} s grind"

class ErdEspressoRange(NamedTuple):
    """A current value with its allowed limits (steam duration, rinse volume, standby timeout)"""
    value: int = 0
    min: int = 0
    max: int = 0
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return str(self.value)

class ErdEspressoSupportedBrewTypes(NamedTuple):
    brew_types: FrozenSet[ErdEspressoBrewType] = frozenset()
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        return ", ".join(b.stringify() or "" for b in sorted(self.brew_types, key=lambda b: b.value))

class ErdEspressoSupportedFeatures(NamedTuple):
    my_cup: bool = False
    my_brew: bool = False
    steam: bool = False
    raw_value: Optional[str] = None

    def stringify(self, **kwargs) -> Optional[str]:
        features = [n for n, v in (("MyCup", self.my_cup), ("MyBrew", self.my_brew), ("Steam", self.steam)) if v]
        return ", ".join(features)
