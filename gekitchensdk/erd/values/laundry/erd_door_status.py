import enum
from logging import setLoggerClass
from typing import Optional

@enum.unique
class ErdDoorStatus(enum.Enum):
    """Fridge door status"""
    CLOSED = "01"
    OPEN = "00"
    NA = "FF"

    def boolify(self) -> Optional[bool]:
        if self.value == ErdDoorStatus.NA:
            return None
        return self.value == ErdDoorStatus.OPEN

    def stringify(self, **kwargs) -> Optional[str]:
        if self.value == ErdDoorStatus.NA:
            return None
        return self.name.title()
