import enum
from typing import Optional

@enum.unique
class ErdOnOff(enum.Enum):
    ON = "01"
    OFF = "00"
    NA = "FF"

    def boolify(self) -> Optional[bool]:
        return self == ErdOnOff.ON   