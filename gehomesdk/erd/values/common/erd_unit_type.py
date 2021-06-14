import enum

@enum.unique
class ErdUnitType(enum.Enum):
    UNKNOWN = 0
    TYPE_120V_CAFE = 1
    TYPE_120V_MONOGRAM = 2
    TYPE_UNKNOWN03 = 3
    TYPE_UNKNOWN04 = 4
    TYPE_240V_MONOGRAM = 9
    TYPE_240V_CAFE = 10
