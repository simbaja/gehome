import enum

@enum.unique
class ErdRemoteStatus(enum.Enum):
    DISABLE = 0
    ENABLED = 1
    NOT_SUPPORTED = 255
