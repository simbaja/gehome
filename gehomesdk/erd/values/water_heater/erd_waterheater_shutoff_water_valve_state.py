import enum


@enum.unique
class ErdWaterHeaterShutoffWaterValveState(enum.Enum):
    NOT_FITTED = 0
    CLOSED = 1
    OPEN = 2
    TRANSITION = 3
    UNKNOWN = -1

    def stringify(self, **kwargs) -> str | None:
        if self == ErdWaterHeaterShutoffWaterValveState.UNKNOWN:
            return None
        return self.name.title().replace("_", " ")