import enum

@enum.unique
class ErdSoilLevel(enum.Enum):
    EXTRA_LIGHT = 0
    LIGHT = 1
    NORMAL = 2
    HEAVY = 3
    EXTRA_HEAVY = 4
    INVALID = 5
