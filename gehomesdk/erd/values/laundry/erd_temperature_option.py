import enum

@enum.unique
class ErdTemperatureOption(enum.Enum):
    NO_HEAT = 0
    EXTRA_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    INVALID = 5

@enum.unique
class ErdTemperatureNewOption(enum.Enum):
    INVALID = 0
    NO_HEAT = 1
    EXTRA_LOW = 2
    LOW = 3
    MEDIUM = 4
    HIGH = 5
