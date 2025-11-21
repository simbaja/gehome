import enum

@enum.unique
class ErdRemoteCommand(enum.Enum):
    NO_OPERATION = 0
    START_RESUME = 1
    CANCEL = 2
    PAUSE = 3

    UNKNOWN = 255

    def stringify(self, **kwargs):
        return self.name.replace("_"," ").title()