from .laundry_enums import ErdSpinSpeedOption
from .spinspeed_option import SpinSpeedOption

SPINSPEED_OPTION_MAP = {
    ErdSpinSpeedOption.NO_SPIN: SpinSpeedOption.NO_SPIN,
    ErdSpinSpeedOption.FIVEHUNDRED: SpinSpeedOption.FIVEHUNDRED,
    ErdSpinSpeedOption.EIGHTHUNDRED: SpinSpeedOption.EIGHTHUNDRED,
    ErdSpinSpeedOption.ELEVENHUNDRED: SpinSpeedOption.ELEVENHUNDRED,
    ErdSpinSpeedOption.FOURTEENHUNDRED: SpinSpeedOption.FOURTEENHUNDRED
}
