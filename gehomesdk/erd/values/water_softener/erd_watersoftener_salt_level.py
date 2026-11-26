import enum

@enum.unique
class ErdWaterSoftenerSaltLevel(enum.Enum):
    LOW_SALT = "01"
    OK = "00"

    def stringify(self, **kwargs) -> str | None:
        return self.name.replace("_"," ").title()

    def boolify(self) -> bool | None:
        return self == ErdWaterSoftenerSaltLevel.OK
