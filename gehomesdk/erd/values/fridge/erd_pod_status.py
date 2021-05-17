import enum

@enum.unique
class ErdPodStatus(enum.Enum):
    REPLACE = "00"
    READY = "01"
    NA = "FF"
