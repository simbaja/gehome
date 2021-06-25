import enum

@enum.unique
class ErdWaterFilterLeakValidity(enum.Enum):
    HAS_LEAK = "01"
    NONE = "00"