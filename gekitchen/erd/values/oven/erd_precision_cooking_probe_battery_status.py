import enum

@enum.unique
class ErdPrecisionCookingProbeBatteryStatus(enum.Enum):
    NA = -1
    OK = 0
    LOW = 1