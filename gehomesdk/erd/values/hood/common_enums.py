import enum

@enum.unique
class ErdHoodLightLevel(enum.Enum):
    OFF = 0
    DIM = 1
    HIGH = 2
    MED = 3

    def boolify(self) -> bool | None:
        return self != ErdHoodLightLevel.OFF

    def stringify(self, **kwargs):
        return self.name.title()
    
@enum.unique
class ErdHoodLightLevelNew(enum.Enum):
    OFF = 0
    L1 = 1
    L2 = 2
    L3 = 3

    def boolify(self) -> bool | None:
        return self != ErdHoodLightLevel.OFF

    def stringify(self, **kwargs):
        return self.name.title()    

@enum.unique
class ErdHoodFanSpeed(enum.Enum):
    OFF    = 0
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3
    BOOST  = 4

    def boolify(self) -> bool | None:
        return self != ErdHoodFanSpeed.OFF

    def stringify(self, **kwargs):
        return self.name.title()
