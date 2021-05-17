import enum

@enum.unique
class ErdTankStatus(enum.Enum):
    FULL = 100
    PERCENT_75 = 75
    PERCENT_50 = 50
    PERCENT_25 = 25
    EMPTY = 0

