from .erd_soil_level import ErdLaundrySoilLevel
from .soil_level import LaundrySoilLevel

LAUNDRY_SOIL_LEVEL_MAP = {
    ErdLaundrySoilLevel.EXTRA_LIGHT: LaundrySoilLevel.SOIL_EXTRA_LIGHT,
    ErdLaundrySoilLevel.LIGHT: LaundrySoilLevel.SOIL_LIGHT,
    ErdLaundrySoilLevel.NORMAL: LaundrySoilLevel.SOIL_NORMAL,
    ErdLaundrySoilLevel.HEAVY: LaundrySoilLevel.SOIL_HEAVY,
    ErdLaundrySoilLevel.EXTRA_HEAVY: LaundrySoilLevel.SOIL_EXTRA_HEAVY
}
