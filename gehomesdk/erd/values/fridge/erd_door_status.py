import enum

@enum.unique
class ErdDoorStatus(enum.Enum):
    """Fridge door status"""
    CLOSED = "00"
    OPEN = "01"
    NA = "FF"

    def boolify(self) -> bool | None:
        if self == ErdDoorStatus.NA:
            return None
        return self == ErdDoorStatus.OPEN

    def stringify(self, **kwargs) -> str | None:
        if self == ErdDoorStatus.NA:
            return None
        return self.name.title()
