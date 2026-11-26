import enum

@enum.unique
class ErdDishwasherDoorStatus(enum.Enum):
    """Dishwasher door status"""
    CLOSED = 1
    OPEN = 0
    NA = 255

    def boolify(self) -> bool | None:
        if self == ErdDishwasherDoorStatus.NA:
            return None
        return self == ErdDishwasherDoorStatus.OPEN

    def stringify(self, **kwargs) -> str | None:
        if self == ErdDishwasherDoorStatus.NA:
            return None
        return self.name.title()
