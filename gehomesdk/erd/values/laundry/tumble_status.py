import enum

@enum.unique
class TumbleStatus(enum.Enum):
    NOT_AVAILABLE = "N/A"
    ENABLE = "Enabled"
    DISABLE = "Disabled"
