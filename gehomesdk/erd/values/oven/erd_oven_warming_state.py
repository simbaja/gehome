import enum
from typing import Optional

@enum.unique
class ErdOvenWarmingState(enum.Enum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    NOT_AVAILABLE = 255

    def boolify(self) -> Optional[bool]:
        return self != ErdOvenWarmingState.OFF

    def stringify(self, **kwargs):
        return self.name.title()
