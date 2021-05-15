import enum

@enum.unique
class ErdMachineSubCycle(enum.Enum):
    NA = 0
    FILL = 1
    SOAK = 2
    WASH = 3
    RINSE = 4
    SPIN = 5
    DRAIN = 6
    EXTRA_SPIN = 7
    EXTRA_RINSE = 8
    TUMBLE = 9
    LOAD_SIZE_DETECTION = 10
    DRYING = 128
    MIST_STEAM = 129
    COOL_DOWN = 130
    EXTENDED_TUMBLE = 131
    DAMP = 132
    AIR_FLUFF = 133
