import enum

@enum.unique
class ErdSpinTimeLevel(enum.Enum):
    NO_SPIN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EXTRA_HIGH = 4
    DISABLE = 5
