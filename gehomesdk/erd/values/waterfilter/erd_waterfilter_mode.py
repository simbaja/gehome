import enum

@enum.unique
class ErdWaterFilterMode(enum.Enum):
    BYPASS = "00"
    OFF = "01"
    FILTERED = "02"
    UNKNOWN = "-1"