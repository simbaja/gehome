import enum

@enum.unique
class ErdOperatingMode(enum.Enum):
    NA = "FF"
    PAUSE = "04"
    LOW_POWER = "00"
    POWER_UP = "01"
    STANDBY = "02"
    DELAY_START = "03"
    CYCLE_ACTIVE = "05"
    EOC = "06"
    DOWNLOAD_MODE = "07"
    SENSOR_CHECK_MODE = "08"
    LOAD_ACTIVATION_MODE = "09"
    MC_ONLY_MODE = "11"
    WARNING_MODE = "12"
    CONTROL_LOCKED = "13"
    CSM_TRIPPED = "14"

