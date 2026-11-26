import enum

@enum.unique
class ErdWaterFilterLeakValidity(enum.Enum):
    HAS_LEAK = "01"
    NO_LEAK = "00"

    def boolify(self) -> bool | None:
        return self == ErdWaterFilterLeakValidity.HAS_LEAK