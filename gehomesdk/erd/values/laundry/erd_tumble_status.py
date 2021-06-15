import enum

@enum.unique
class ErdTumbleStatus(enum.Enum):
    NOT_AVAILABLE = 255
    ENABLE = 1
    DISABLE = 0

