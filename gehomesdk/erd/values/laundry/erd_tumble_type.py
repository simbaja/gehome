import enum

@enum.unique
class ErdTumbleType(enum.Enum):
    INVALID = 255
    LEGACY = 1
    NEW = 0

