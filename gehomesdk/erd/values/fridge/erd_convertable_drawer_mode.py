import enum
from typing import Optional

@enum.unique
class ErdConvertableDrawerMode(enum.Enum):
    UNKNOWN0 = "00"
    UNKNOWN1 = "01"
    MEAT = "03"
    BEVERAGE = "04"
    SNACK = "05"
    WINE = "06"
    NA = "FF"

    def stringify(self, **kwargs) -> Optional[str]:
        if(self == ErdConvertableDrawerMode.NA):
            return "N/A"
        return self.name.title()
