import enum
from typing import Optional

@enum.unique
class ErdHoodLightLevel(enum.Enum):
    OFF = 0
    DIM = 1
    HIGH = 2

    def boolify(self) -> Optional[bool]:
        return self != ErdHoodLightLevel.OFF

    def stringify(self, **kwargs):
        return self.name.title()

@enum.unique
class ErdHoodFanSpeed(enum.Enum):
    OFF    = 0
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3
    BOOST  = 4

    def boolify(self) -> Optional[bool]:
        return self != ErdHoodFanSpeed.OFF

    def stringify(self, **kwargs):
        return self.name.title()
