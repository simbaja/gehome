import enum

@enum.unique
class ErdRinseOption(enum.Enum):
    INVALID = 0
    NORMAL = 1
    EXTRA = 2
    MAX = 3
    HEAVY = 4
    EXTRA_HEAVY = 5
