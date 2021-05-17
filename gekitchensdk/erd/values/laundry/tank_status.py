import enum

@enum.unique
class TankStatus(enum.Enum):
    STATUS_EMPTY = "Empty"
    STATUS_75PERCENT = "75%"
    STATUS_50PERCENT = "50%"
    STATUS_25PERCENT = "25%"
    STATUS_FULL = "Full"
