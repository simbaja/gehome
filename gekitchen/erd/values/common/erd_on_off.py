import enum

@enum.unique
class ErdOnOff(enum.Enum):
    ON = "01"
    OFF = "00"
    NA = "FF"
