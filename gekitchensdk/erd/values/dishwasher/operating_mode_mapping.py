from .erd_operating_mode import ErdOperatingMode
from .operating_mode import OperatingMode

OPERATING_MODE_MAP = {
    ErdOperatingMode.NA: OperatingMode.STATUS_DASH,
    ErdOperatingMode.PAUSE: OperatingMode.STATUS_PAUSED,
    ErdOperatingMode.LOW_POWER: OperatingMode.STATUS_OFF,
    ErdOperatingMode.POWER_UP: OperatingMode.STATUS_OFF,
    ErdOperatingMode.STANDBY: OperatingMode.STATUS_OFF,
    ErdOperatingMode.DELAY_START: OperatingMode.STATUS_DELAY,
    ErdOperatingMode.CYCLE_ACTIVE: OperatingMode.STATUS_CYCLE_ACTIVE,
    ErdOperatingMode.EOC: OperatingMode.STATUS_OFF,
    ErdOperatingMode.DOWNLOAD_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.SENSOR_CHECK_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.LOAD_ACTIVATION_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.MC_ONLY_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.WARNING_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.CONTROL_LOCKED: OperatingMode.CONTROL_LOCKED,
    ErdOperatingMode.CSM_TRIPPED: OperatingMode.STATUS_OFF
}
