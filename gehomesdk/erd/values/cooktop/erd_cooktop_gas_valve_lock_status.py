import enum

@enum.unique
class ErdCooktopGasValveLockStatus(enum.Enum):
    INITIALIZING = 0
    UNLOCKED = 1
    TRANSITIONING = 2
    LOCKED = 3
    UNKNOWN = 255

    def stringify(self, **kwargs) -> str | None:
        return self.name.replace("_"," ").title()
    
    def boolify(self) -> bool | None:
        return self == ErdCooktopGasValveLockStatus.LOCKED