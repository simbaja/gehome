import enum
from logging import setLoggerClass
from typing import Optional

@enum.unique
class ErdDishwasherDoorStatus(enum.Enum):
    """Dishwasher door status"""
    CLOSED = 1
    OPEN = 0
    NA = 255

    def boolify(self) -> Optional[bool]:
        if self == ErdDishwasherDoorStatus.NA:
            return None
        return self == ErdDishwasherDoorStatus.OPEN

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdDishwasherDoorStatus.NA:
            return None
        return self.name.title()
