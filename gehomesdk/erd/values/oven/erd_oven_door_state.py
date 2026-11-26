import enum
from typing import Optional


@enum.unique
class ErdOvenDoorState(enum.Enum):
    UNKNOWN = 0
    OPEN = 1
    CLOSED = 2
    INITIAL_INSPECTION = 3

    def boolify(self) -> Optional[bool]:
        if self == ErdOvenDoorState.OPEN:
            return True
        if self == ErdOvenDoorState.CLOSED:
            return False
        return None

    def stringify(self, **kwargs) -> str:
        return self.name.replace("_", " ").title()
