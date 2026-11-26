import enum

@enum.unique
class ErdConvertableDrawerMode(enum.Enum):
    UNKNOWN0 = "00"
    UNKNOWN1 = "01"
    SOFT_FREEZE = "02"
    MEAT = "03"
    BEVERAGE = "04"
    SNACK = "05"
    WINE = "06"
    NA = "FF"

    def stringify(self, **kwargs) -> str | None:
        if(self == ErdConvertableDrawerMode.NA):
            return "N/A"
        return self.name.title()
