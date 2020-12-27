import enum

@enum.unique
class ErdCooktopStatus(enum.Enum):
    DASH = 255
    OFF = 0
    BURNERS_ON = 1