import enum

@enum.unique
class ErdWaterFilterPosition(enum.Enum):
    BYPASS = 0
    OFF = 1
    FILTERED = 2
    READY = 3
    UNKNOWN = -1

    def stringify(self, **kwargs) -> str | None:
        return self.name.title()
