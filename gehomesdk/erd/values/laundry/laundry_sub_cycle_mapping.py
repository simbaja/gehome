from .laundry_enums import ErdLaundrySubCycle
from .laundry_sub_cycle import LaundrySubCycle

LAUNDRY_SUB_CYCLE_MAP = {
    ErdLaundrySubCycle.CYCLE_NONE: LaundrySubCycle.DASH,
    ErdLaundrySubCycle.FILL: LaundrySubCycle.FILL,
    ErdLaundrySubCycle.SOAK: LaundrySubCycle.SOAK,
    ErdLaundrySubCycle.WASH: LaundrySubCycle.WASH,
    ErdLaundrySubCycle.RINSE: LaundrySubCycle.RINSE,
    ErdLaundrySubCycle.SPIN: LaundrySubCycle.SPIN,
    ErdLaundrySubCycle.DRAIN: LaundrySubCycle.DRAIN,
    ErdLaundrySubCycle.EXTRA_SPIN: LaundrySubCycle.EXTRA_SPIN,
    ErdLaundrySubCycle.EXTRA_RINSE: LaundrySubCycle.EXTRA_RINSE,
    ErdLaundrySubCycle.TUMBLE: LaundrySubCycle.TUMBLE,
    ErdLaundrySubCycle.LOAD_SIZE_DETECTION: LaundrySubCycle.LOAD_SIZE_DETECTION,
    ErdLaundrySubCycle.DRYING: LaundrySubCycle.DRYING,
    ErdLaundrySubCycle.MIST_STEAM: LaundrySubCycle.MIST_STEAM,
    ErdLaundrySubCycle.COOL_DOWN: LaundrySubCycle.COOL_DOWN,
    ErdLaundrySubCycle.EXTENDED_TUMBLE: LaundrySubCycle.EXTENDED_TUMBLE,
    ErdLaundrySubCycle.DAMP: LaundrySubCycle.DAMP,
    ErdLaundrySubCycle.AIR_FLUFF: LaundrySubCycle.AIR_FLUFF
}
