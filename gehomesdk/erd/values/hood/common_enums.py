import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdHoodLightSetting(enum.Enum):
    OFF = 0
    DIM = 1
    HIGH = 2

    def boolify(self) -> Optional[bool]:
        return self != ErdHoodLightStatus.OFF

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

@enum.unique
class ErdHoodFanSetting(enum.Enum):
    OFF    = 0
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3
    BOOST  = 4

    def boolify(self) -> Optional[bool]:
        return self != ErdHoodLightStatus.OFF

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()
