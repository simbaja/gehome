import enum

@enum.unique
class ErdTemperatureOption(enum.Enum):
    NO_HEAT = 0
    EXTRA_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    INVALID = 5
