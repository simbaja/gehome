import enum

@enum.unique
class ErdMachineState(enum.Enum):
    IDLE = 0
    STANDBY = 1
    RUN = 2
    PAUSE = 3
    END_OF_CYCLE = 4
    DSM_DELAY_RUN = 5
    DELAY_RUN = 6
    DELAY_PAUSE = 7
    DRAIN_TIMEOUT = 8
    COMMISSIONING = 9
    BULK_FLUSH = 10
    CLEAN_SPEAK = 128

