# WIP

import enum

@enum.unique
class ErdClosedLoopCookingConfiguration(enum.Enum):
    MODE_NOT_SUPPORTED_CLOSED_LOOP_COOKTOP = -1   
    OLD_PRECISION_COOKING = 1
    NEW_CLOSED_LOOP_COOKTOP = 2
    MODE_NOT_SUPPORTED_ALL = 3
