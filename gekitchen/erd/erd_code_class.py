import enum

@enum.unique
class ErdCodeClass(enum.IntFlag):
    NONE = 0
    GENERAL = 1
    CLOCK = 2
    TIMER = 4
    NON_ZERO_TEMPERATURE = 8
    RAW_TEMPERATURE = 16
    DOOR = 32
    LOCK_CONTROL = 64
    SABBATH_CONTROL = 128 

    TEMPERATURE = NON_ZERO_TEMPERATURE | RAW_TEMPERATURE
    