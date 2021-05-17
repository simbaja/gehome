from .erd_operating_mode import ErdOperatingMode
from .operating_mode import OperatingMode

OPERATING_MODE_MAP = {
    ErdOperatingMode.DOWNLOAD_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.SENSOR_CHECK_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.LOAD_ACTIVATION_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.MC_ONLY_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.WARNING_MODE: OperatingMode.STATUS_OFF,
    ErdOperatingMode.CSM_TRIPPED: OperatingMode.STATUS_OFF,
    ErdOperatingMode.INVALID: OperatingMode.STATUS_DASH,
    ErdOperatingMode.STANDBY: OperatingMode.STATUS_DASH,
    ErdOperatingMode.LOW_POWER: OperatingMode.STATUS_DASH,
    ErdOperatingMode.POWER_UP: OperatingMode.STATUS_DASH,
    ErdOperatingMode.PAUSE: OperatingMode.STATUS_PAUSED,
    ErdOperatingMode.DELAY_START: OperatingMode.STATUS_DELAY,
    ErdOperatingMode.CYCLE_ACTIVE: OperatingMode.STATUS_CYCLE_ACTIVE,
    ErdOperatingMode.EOC: OperatingMode.STATUS_CYCLE_COMPLETE,
    ErdOperatingMode.CONTROL_LOCKED: OperatingMode.CONTROL_LOCKED
}
