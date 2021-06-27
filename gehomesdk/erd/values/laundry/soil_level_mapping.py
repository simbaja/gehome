from .laundry_enums import ErdSoilLevel
from .soil_level import SoilLevel

SOIL_LEVEL_MAP = {
    ErdSoilLevel.EXTRA_LIGHT: SoilLevel.EXTRA_LIGHT,
    ErdSoilLevel.LIGHT: SoilLevel.LIGHT,
    ErdSoilLevel.NORMAL: SoilLevel.NORMAL,
    ErdSoilLevel.HEAVY: SoilLevel.HEAVY,
    ErdSoilLevel.EXTRA_HEAVY: SoilLevel.EXTRA_HEAVY,
    ErdSoilLevel.INVALID: SoilLevel.DASH
}

