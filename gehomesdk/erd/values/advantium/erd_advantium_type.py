import enum

@enum.unique
class ErdAdvantiumType(enum.Enum):
    UNKNOWN = 0,
    TYPE_120V_CAFE = 1,
    TYPE_120V_MONOGRAM = 2,
    TYPE_240V_MONOGRAM = 9,
    TYPE_240V_CAFE = 10  
