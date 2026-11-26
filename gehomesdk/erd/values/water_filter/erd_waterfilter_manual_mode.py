import enum

@enum.unique
class ErdWaterFilterManualMode(enum.Enum):
    MANUAL = "01"
    NOT_MANUAL = "00"

    def stringify(self, **kwargs) -> str | None:
        return self.name.replace("_"," ").title()

    def boolify(self) -> bool | None:
        return self == ErdWaterFilterManualMode.MANUAL