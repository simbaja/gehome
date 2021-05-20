import enum

@enum.unique
class ErdUnitType(enum.Enum):
    UNKNOWN = "00"
    TYPE_120V_CAFE = "01"
    TYPE_120V_MONOGRAM = "02"
    TYPE_240V_MONOGRAM = "09"
    TYPE_240V_CAFE = "10"
