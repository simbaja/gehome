import enum
from typing import Optional

@enum.unique
class ErdCooktopGasValveLockRequest(enum.Enum):
    DO_NOTHING = 0
    REQUEST_LOCK = 1

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_"," ").title()
