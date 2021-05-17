import enum

@enum.unique
class ErdPresent(enum.Enum):
    PRESENT = "01"
    NOT_PRESENT = "00"
    NA = "FF"