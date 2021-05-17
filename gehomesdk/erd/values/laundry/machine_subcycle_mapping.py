from .erd_machine_subcycle import ErdMachineSubCycle
from .machine_subcycle import MachineSubCycle

MACHINE_SUBCYCLE_MAP = {
    ErdMachineSubCycle.NA: MachineSubCycle.DASH,
    ErdMachineSubCycle.FILL: MachineSubCycle.FILL,
    ErdMachineSubCycle.SOAK: MachineSubCycle.SOAK,
    ErdMachineSubCycle.WASH: MachineSubCycle.WASH,
    ErdMachineSubCycle.RINSE: MachineSubCycle.RINSE,
    ErdMachineSubCycle.SPIN: MachineSubCycle.SPIN,
    ErdMachineSubCycle.DRAIN: MachineSubCycle.DRAIN,
    ErdMachineSubCycle.EXTRA_SPIN: MachineSubCycle.EXTRA_SPIN,
    ErdMachineSubCycle.EXTRA_RINSE: MachineSubCycle.EXTRA_RINSE,
    ErdMachineSubCycle.TUMBLE: MachineSubCycle.TUMBLE,
    ErdMachineSubCycle.LOAD_SIZE_DETECTION: MachineSubCycle.LOAD_SIZE_DETECTION,
    ErdMachineSubCycle.DRYING: MachineSubCycle.DRYING,
    ErdMachineSubCycle.MIST_STEAM: MachineSubCycle.MIST_STEAM,
    ErdMachineSubCycle.COOL_DOWN: MachineSubCycle.COOL_DOWN,
    ErdMachineSubCycle.EXTENDED_TUMBLE: MachineSubCycle.EXTENDED_TUMBLE,
    ErdMachineSubCycle.DAMP: MachineSubCycle.DAMP,
    ErdMachineSubCycle.AIR_FLUFF: MachineSubCycle.AIR_FLUFF
}
