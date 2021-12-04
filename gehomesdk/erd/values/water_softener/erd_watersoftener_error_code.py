import enum
from typing import Optional

@enum.unique
class ErdWaterSoftenerErrorCode(enum.Enum):
    UNKNOWN = 255
    NO_ERROR = 0
    NO_POSITION_SWITCH_DETECTED = 1
    RESERVED = 2
    CANNOT_FIND_SERVICE_POSITION = 3
    POSITION_SWITCH = 4
    BAD_PRINTED_WIRE_ASSEMBLY = 5
    SHUTOFF_VALVE_NOT_CLOSED_TIMEOUT = 6
    SHUTOFF_VALVE_OPENED_TIMEOUT = 7
    
    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterSoftenerErrorCode.UNKNOWN:
            return None
        return self.name.replace("_", " ").title()
