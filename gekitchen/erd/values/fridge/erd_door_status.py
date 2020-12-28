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
        if self.value == ErdDoorStatus.NA:
            return None
        return self.value == ErdDoorStatus.OPEN
