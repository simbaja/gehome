from .erd_cycle_state import ErdCycleState, ErdCycleStateRaw

CYCLE_STATE_RAW_MAP = {
    ErdCycleStateRaw.PREWASH: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.PREWASH1: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.AUTO_HOT_START1: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.AUTO_HOT_START2: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.AUTO_HOT_START3: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.END_PREWASH1: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.SENSING: ErdCycleState.SENSING,
    ErdCycleStateRaw.MAIN_WASH: ErdCycleState.MAIN_WASH,
    ErdCycleStateRaw.DIVERTER_CAL: ErdCycleState.MAIN_WASH,
    ErdCycleStateRaw.DRYING: ErdCycleState.DRYING,
    ErdCycleStateRaw.SANITIZING: ErdCycleState.SANITIZING,
    ErdCycleStateRaw.RINSING: ErdCycleState.RINSING,
    ErdCycleStateRaw.TURBIDITY_CAL: ErdCycleState.RINSING,
    ErdCycleStateRaw.FINAL_RINSE: ErdCycleState.RINSING,
    ErdCycleStateRaw.FINAL_RINSE_FILL: ErdCycleState.RINSING,
    ErdCycleStateRaw.PAUSE: ErdCycleState.PAUSE,
    ErdCycleStateRaw.STATE_17: ErdCycleState.NA,
    ErdCycleStateRaw.STATE_18: ErdCycleState.NA,
    ErdCycleStateRaw.CYCLE_INACTIVE: ErdCycleState.NA,
    ErdCycleStateRaw.MAX: ErdCycleState.NA,
    ErdCycleStateRaw.INVALID: ErdCycleState.NA
}
