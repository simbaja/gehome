import enum

@enum.unique
class ErdWaterFilterManualMode(enum.Enum):
    MANUAL = "01"
    NOT_MANUAL = "00"