import enum
from typing import NamedTuple, Optional

@enum.unique
class ErdAcFanSetting(enum.Enum):
    DEFAULT = 0
    AUTO = 1
    LOW = 2
    LOW_AUTO = 3
    MED = 4
    MED_AUTO = 5
    HIGH = 8
    HIGH_AUTO = 9

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()      

@enum.unique
class ErdAcOperationMode(enum.Enum):
    COOL = 0
    FAN_ONLY = 1
    ENERGY_SAVER = 2
    HEAT = 3
    DRY = 4
    AUTO = 5
    TURBO_COOL = 6
    SILENT = 7
    DEFAULT = 9

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

@enum.unique
class ErdAcFilterStatus(enum.Enum):
    OK = 0
    CLEAN = 1
    DEFAULT = -1

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

    def boolify(self) -> Optional[bool]:
        return self != ErdAcFilterStatus.OK

@enum.unique
class ErdAcTurboQuietMode(enum.Enum):
    NORMAL: 0
    TURBO: 1
    QUIET: 2
    UNAVAILABLE: 255

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()

class ErdAcAvailableModes(NamedTuple):
    has_heat: bool
    has_dry: bool
    has_eco: bool
    has_turbo_cool: bool
    has_silent: bool
    has_auto: bool
    has_cool: bool
    has_fan: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return (
            f"heat: {self.has_heat}, "
            f"dry: {self.has_dry}, "
            f"eco: {self.has_eco}, "
            f"turbo_cool: {self.has_turbo_cool}, "
            f"silent: {self.has_silent}, "
            f"auto: {self.has_auto}, "
            f"cool: {self.has_cool}, "
            f"fan: {self.has_fan}"
        )

class ErdAcAvailableFanSpeeds(NamedTuple):
    has_auto: bool
    has_high: bool
    has_medium: bool
    has_low: bool
    has_smart_dry: bool
    has_reserved: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return (
            f"auto: {self.has_auto}, "
            f"high: {self.has_high}, "
            f"medium: {self.has_medium}, "
            f"low: {self.has_low}, "
            f"smart_dry: {self.has_smart_dry}, "
            f"reserved: {self.has_reserved}"
        )

class ErdAcAvailableTurboQuietModes(NamedTuple):
    has_normal: bool
    has_turbo: bool
    has_quiet: bool
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return (
            f"normal: {self.has_normal}, "
            f"turbo: {self.has_turbo}, "
            f"quiet: {self.has_quiet}, "
        )