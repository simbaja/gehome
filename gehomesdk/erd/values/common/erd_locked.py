import enum

@enum.unique
class ErdInterfaceLocked(enum.Enum):
    DEFAULT = 0
    LOCKED = 1
    UNLOCKED = 2
