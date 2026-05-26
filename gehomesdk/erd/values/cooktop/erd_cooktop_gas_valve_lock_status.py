import enum
from typing import Optional

@enum.unique
class ErdCooktopGasValveLockStatus(enum.Enum):
    INITIALIZING = 0
    UNLOCKED = 1
    TRANSITIONING = 2
    LOCKED = 3
    UNKNOWN = 255

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_"," ").title()
    
    def boolify(self) -> Optional[bool]:
        return self == ErdCooktopGasValveLockStatus.LOCKED