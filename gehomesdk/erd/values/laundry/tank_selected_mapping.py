from .laundry_enums import ErdTankSelected
from .tank_selected import TankSelected

TANK_SELECTED_MAP = {
    ErdTankSelected.INVALID: TankSelected.DASH,
    ErdTankSelected.DETERGENT: TankSelected.DETERGENT,
    ErdTankSelected.SOFTENER: TankSelected.SOFTENER,
    ErdTankSelected.BLEACH: TankSelected.BLEACH,
    ErdTankSelected.OTHER: TankSelected.OTHER
}
