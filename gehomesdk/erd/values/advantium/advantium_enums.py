import enum
from typing import Optional

@enum.unique
class CoolingFanStatus(enum.Enum):
    OFF = 0
    ON = 1

    def boolify(self) -> Optional[bool]:
        return self == CoolingFanStatus.ON

@enum.unique
class TerminationReason(enum.Enum):
    UNKNOWN = 0
    COOK_TIME_COMPLETE = 1
    USER_CANCELED = 2
    MAX_TIME_SHUTOFF = 3
    DOOR_OPENENED_WHILE_SENSING = 4
    FAULT = 5

@enum.unique
class WarmStatus(enum.Enum):
    OFF = 0
    CRISP = 1
    MOIST = 2,
    UNKNOWN = 255

@enum.unique
class DoorStatus(enum.Enum):
    OPEN = 0
    CLOSED = 1

    def boolify(self) -> Optional[bool]:
        return self == DoorStatus.OPEN    

@enum.unique
class CookAction(enum.Enum):
    STOP = 0
    START = 1
    UPDATED = 2
    PAUSE = 3
    RESUME = 4,
    UNKNOWN = 255

@enum.unique
class CookMode(enum.Enum):
    NO_MODE = 0
    CONVECTION_BAKE = 1
    BROIL = 2
    MICROWAVE = 3
    MICROWAVE_SENSOR = 4
    MICROWAVE_STAGED = 5
    PRECISION_COOK = 6
    PRECISION_COOK_STAGED = 7
    PRECISION_COOK_CUSTOM = 8
    WARM = 9
    PROOF = 10
    TOAST = 11
    STEAM_CLEAN = 12
    MICROWAVE_SLOW_COOK = 13,
    UNKNOWN = 255

@enum.unique
class OvenLightStatus(enum.Enum):
    OFF = 0
    ON = 1

    def boolify(self) -> Optional[bool]:
        return self == OvenLightStatus.ON    

@enum.unique
class PreheatStatus(enum.Enum):
    NO_PREHEAT = 0
    PREHEAT_ACTIVE = 1
    PREHEAT_COMPLETE = 2

@enum.unique
class SensingActive(enum.Enum):
    INACTIVE = 0
    ACTIVE = 1

    def boolify(self) -> Optional[bool]:
        return self == SensingActive.ACTIVE    
