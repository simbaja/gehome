from .laundry_enums import ErdTankStatus
from .tank_status import TankStatus

TANK_STATUS_MAP = {
    ErdTankStatus.FULL: TankStatus.STATUS_FULL,
    ErdTankStatus.PERCENT_75: TankStatus.STATUS_75PERCENT,
    ErdTankStatus.PERCENT_50: TankStatus.STATUS_50PERCENT,
    ErdTankStatus.PERCENT_25: TankStatus.STATUS_25PERCENT,
    ErdTankStatus.EMPTY: TankStatus.STATUS_EMPTY
}
