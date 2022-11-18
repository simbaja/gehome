import enum

@enum.unique
class ErdCycleStateRaw(enum.Enum):
    NO_CHANGE = 0
    PREWASH = 1
    SENSING = 2
    MAIN_WASH = 3
    DRYING = 4
    SANITIZING = 5
    TURBIDITY_CAL = 6
    DIVERTER_CAL = 7
    PAUSE = 8
    RINSING = 9
    PREWASH1 = 10
    FINAL_RINSE = 11
    END_PREWASH1 = 12
    AUTO_HOT_START1 = 13
    AUTO_HOT_START2 = 14
    AUTO_HOT_START3 = 15
    FINAL_RINSE_FILL = 16
    STATE_17 = 17
    STATE_18 = 18
    CYCLE_INACTIVE = 26
    MAX = 27
    INVALID = 255

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

    def stringify(self, **kwargs):
        if self == ErdCycleState.NA:
            return "N/A"
        return self.name.replace("_"," ").title()    
