import enum

@enum.unique
class ErdEndTone(enum.Enum):
    BEEP = "00"
    REPEATED_BEEP = "01"
    NA = "FF"
