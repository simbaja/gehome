import enum

@enum.unique
class ErdWaterSoftenerShutoffValveState(enum.Enum):
    OPEN = 0
    CLOSED = 1
    TRANSITION = 2
    UNKNOWN = 255

    def stringify(self, **kwargs) -> str | None:
        return self.name.replace("_"," ").title()
