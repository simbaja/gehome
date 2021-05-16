import enum

@enum.unique
class ErdTankSelected(enum.Enum):
    DETERGENT = 0
    SOFTENER = 1
    BLEACH = 2
    OTHER = 3
    INVALID = 4
