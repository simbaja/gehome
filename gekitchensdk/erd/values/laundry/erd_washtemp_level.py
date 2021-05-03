import enum

@enum.unique
class ErdWashTempLevel(enum.Enum):
    TAP_COLD_1 = 0
    COLD_1 = 1
    WARM_1 = 2
    HOT_1 = 3
    EXTRAHOT__1 = 4
    INVALID = 6
    TAP_COLD_2 = 16
    COLD_2 = 17
    COOL_2 = 18
    COLORS_2 = 19
    WARM_2 = 20
    HOT_2 = 21
    EXTRA_HOT_2 = 22
