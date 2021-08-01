import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdFanSetting(enum.Enum):
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
class ErdWacOperationMode(enum.Enum):
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
class ErdWacFilterStatus(enum.Enum):
    OK = 0
    CLEAN = 1
    DEFAULT = -1

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

    def boolify(self) -> Optional[bool]:
        return self.value != ErdWacFilterStatus.OK

@enum.unique
class ErdWacDemandResponseState(enum.Enum):
    NOT_AVAILABLE = 255
    NOT_IN_DEMAND_RESPONSE = 0
    IN_DEMAND_RESPONSE = 1
    TEMPORARY_LOAD_REDUCTION = 2

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()
