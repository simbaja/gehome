from .laundry_enums import ErdRinseOption
from .rinse_option import RinseOption

RINSE_OPTION_MAP = {
    ErdRinseOption.INVALID: RinseOption.INVALID,
    ErdRinseOption.NORMAL: RinseOption.NORMAL,
    ErdRinseOption.EXTRA: RinseOption.EXTRA,
    ErdRinseOption.MAX: RinseOption.MAX,
    ErdRinseOption.HEAVY: RinseOption.HEAVY,
    ErdRinseOption.EXTRA_HEAVY: RinseOption.EXTRA_HEAVY
}
