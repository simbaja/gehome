import enum

@enum.unique
class ErdCycleStateRaw(enum.Enum):
    STATE_01 = "01"
    STATE_02 = "02"
    STATE_03 = "03"
    STATE_04 = "04"
    STATE_05 = "05"
    STATE_06 = "06"
    STATE_07 = "07"
    STATE_08 = "08"
    STATE_09 = "09"
    STATE_10 = "10"
    STATE_11 = "11"
    STATE_12 = "12"
    STATE_13 = "13"
    STATE_14 = "14"
    STATE_15 = "15"
    STATE_16 = "16"
    STATE_17 = "17"
    STATE_18 = "18"

@enum.unique
class ErdCycleState(enum.Enum):
    NA = -1
    PRE_WASH = 1
    SENSING = 2
    MAIN_WASH = 3
    DRYING = 4
    SANITIZING = 5
    RINSING = 6
    PAUSE = 7
