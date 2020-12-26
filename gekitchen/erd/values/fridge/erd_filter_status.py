import enum

@enum.unique
class ErdFilterStatus(enum.Enum):
    GOOD = "00"
    REPLACE = "01"
    EXPIRED = "02"
    UNFILTERED = "03"
    LEAK_DETECTED = "04"
    NA = "FF"
