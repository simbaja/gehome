import enum

@enum.unique
class ErdWaterFilterMode(enum.Enum):
    BYPASS = 0
    OFF = 1
    FILTERED = 2
    TRANSITION = 3
    UNKNOWN = -1

    def stringify(self, **kwargs) -> str | None:
        if self == ErdWaterFilterMode.UNKNOWN:
            return None
        return self.name.title()
