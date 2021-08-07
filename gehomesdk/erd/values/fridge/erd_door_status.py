import enum
from logging import setLoggerClass
from typing import Optional

@enum.unique
class ErdDoorStatus(enum.Enum):
    """Fridge door status"""
    CLOSED = "00"
    OPEN = "01"
    NA = "FF"

    def boolify(self) -> Optional[bool]:
        if self == ErdDoorStatus.NA:
            return None
        return self == ErdDoorStatus.OPEN

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdDoorStatus.NA:
            return None
        return self.name.title()
