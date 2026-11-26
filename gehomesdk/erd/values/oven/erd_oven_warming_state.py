import enum

@enum.unique
class ErdOvenWarmingState(enum.Enum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    NOT_AVAILABLE = 255

    def boolify(self) -> bool | None:
        return self != ErdOvenWarmingState.OFF

    def stringify(self, **kwargs):
        return self.name.title()
