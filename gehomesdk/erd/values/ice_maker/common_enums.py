import enum
from typing import Optional

@enum.unique
class ErdOimStatus(enum.Enum):
    MAKING_ICE = 0
    DEFROSTING = 1
    CLEANING = 2
    ICE_BIN_FULL = 3
    ADD_WATER = 4
    ICE_BIN_MISSING = 5
    IDLE = 6

    UNKNOWN = 255

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

@enum.unique
class ErdOimLightLevel(enum.Enum):
    OFF = 0
    ON = 1
    DIM = 2

    def boolify(self) -> Optional[bool]:
        return self != ErdOimLightLevel.OFF

    def stringify(self, **kwargs):
        return self.name.title()

@enum.unique
class ErdOimFilterStatus(enum.Enum):
    OK = 0
    EXPIRED = 1

    def boolify(self) -> Optional[bool]:
        return self != ErdOimFilterStatus.OK

    def stringify(self, **kwargs):
        return self.name.title()
