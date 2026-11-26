import enum

@enum.unique
class ErdCooktopGasValveLockRequest(enum.Enum):
    DO_NOTHING = 0
    REQUEST_LOCK = 1

    def stringify(self, **kwargs) -> str | None:
        return self.name.replace("_"," ").title()
