import enum
from typing import Optional

@enum.unique
class ErdWaterFilterManualMode(enum.Enum):
    MANUAL = "01"
    NOT_MANUAL = "00"

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_"," ").title()

    def boolify(self) -> Optional[bool]:
        return self.value == ErdWaterFilterManualMode.MANUAL