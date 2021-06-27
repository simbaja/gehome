from .laundry_enums import ErdSpinTimeLevel
from .spintime_level import SpinTimeLevel

SPINTIME_LEVEL_MAP = {
    ErdSpinTimeLevel.NO_SPIN: SpinTimeLevel.NO_SPIN,
    ErdSpinTimeLevel.LOW: SpinTimeLevel.LOW,
    ErdSpinTimeLevel.MEDIUM: SpinTimeLevel.MEDIUM,
    ErdSpinTimeLevel.HIGH: SpinTimeLevel.HIGH,
    ErdSpinTimeLevel.EXTRA_HIGH: SpinTimeLevel.EXTRA_HIGH,
    ErdSpinTimeLevel.DISABLE: SpinTimeLevel.DASH
}
