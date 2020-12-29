from .erd_cycle_state import ErdCycleState, ErdCycleStateRaw

CYCLE_STATE_RAW_MAP = {
    ErdCycleStateRaw.STATE_01: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_02: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_03: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_04: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_05: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_06: ErdCycleState.PRE_WASH,
    ErdCycleStateRaw.STATE_07: ErdCycleState.SENSING,
    ErdCycleStateRaw.STATE_08: ErdCycleState.MAIN_WASH,
    ErdCycleStateRaw.STATE_09: ErdCycleState.MAIN_WASH,
    ErdCycleStateRaw.STATE_10: ErdCycleState.DRYING,
    ErdCycleStateRaw.STATE_11: ErdCycleState.SANITIZING,
    ErdCycleStateRaw.STATE_12: ErdCycleState.RINSING,
    ErdCycleStateRaw.STATE_13: ErdCycleState.RINSING,
    ErdCycleStateRaw.STATE_14: ErdCycleState.RINSING,
    ErdCycleStateRaw.STATE_15: ErdCycleState.RINSING,
    ErdCycleStateRaw.STATE_16: ErdCycleState.PAUSE,
    ErdCycleStateRaw.STATE_17: ErdCycleState.NA,
    ErdCycleStateRaw.STATE_18: ErdCycleState.NA
}
