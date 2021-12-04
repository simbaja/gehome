import enum
from typing import Optional

@enum.unique
class ErdWaterSoftenerSaltLevel(enum.Enum):
    LOW_SALT = "01"
    OK = "00"

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_"," ").title()

    def boolify(self) -> Optional[bool]:
        return self == ErdWaterSoftenerSaltLevel.OK
