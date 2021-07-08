import enum
from typing import Optional

@enum.unique
class ErdWaterFilterLeakDetected(enum.Enum):
    HAS_LEAK = "01"
    NO_LEAK = "00"

    def boolify(self) -> Optional[bool]:
        return self.value == ErdWaterFilterLeakDetected.HAS_LEAK