from .laundry_enums import ErdMachineState
from .machine_state import MachineState

MACHINE_STATE_MAP = {
    ErdMachineState.IDLE: MachineState.STATUS_OFF,
    ErdMachineState.STANDBY: MachineState.STATUS_STANDBY,
    ErdMachineState.RUN: MachineState.STATUS_RUN,
    ErdMachineState.PAUSE: MachineState.STATUS_PAUSED,
    ErdMachineState.END_OF_CYCLE: MachineState.STATUS_CYCLE_COMPLETE,
    ErdMachineState.DSM_DELAY_RUN: MachineState.STATUS_DELAY_RUN,
    ErdMachineState.DELAY_RUN: MachineState.STATUS_DELAY_RUN,
    ErdMachineState.DELAY_PAUSE: MachineState.STATUS_DELAY_PAUSED,
    ErdMachineState.DRAIN_TIMEOUT: MachineState.STATUS_DRAIN_TIMEOUT,
    ErdMachineState.COMMISSIONING: MachineState.STATUS_COMMISSIONING,
    ErdMachineState.BULK_FLUSH: MachineState.STATUS_BULK_FLUSH,
    ErdMachineState.CLEAN_SPEAK: MachineState.STATUS_CLEAN_SPEAK
}
