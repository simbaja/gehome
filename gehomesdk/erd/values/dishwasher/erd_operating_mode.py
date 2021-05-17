import enum

@enum.unique
class ErdOperatingMode(enum.Enum):
    LOW_POWER = 0
    POWER_UP = 1
    STANDBY = 2
    DELAY_START = 3
    PAUSE = 4
    CYCLE_ACTIVE = 5
    EOC = 6
    DOWNLOAD_MODE = 7
    SENSOR_CHECK_MODE = 8
    LOAD_ACTIVATION_MODE = 9
    MC_ONLY_MODE = 17
    WARNING_MODE = 18
    CONTROL_LOCKED = 19
    CSM_TRIPPED = 20
    INVALID = 255

