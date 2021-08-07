import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdAcFanSetting(enum.Enum):
    DEFAULT = 0
    AUTO = 1
    LOW = 2
    LOW_AUTO = 3
    MED = 4
    MED_AUTO = 5
    HIGH = 8
    HIGH_AUTO = 9

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()      

@enum.unique
class ErdAcOperationMode(enum.Enum):
    COOL = 0
    FAN_ONLY = 1
    ENERGY_SAVER = 2
    HEAT = 3
    DRY = 4
    AUTO = 5
    DEFAULT = 9

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

@enum.unique
class ErdAcFilterStatus(enum.Enum):
    OK = 0
    CLEAN = 1
    DEFAULT = -1

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

    def boolify(self) -> Optional[bool]:
        return self != ErdAcFilterStatus.OK