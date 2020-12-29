import enum

@enum.unique
class ErdClockFormat(enum.Enum):
    TWELVE_HOUR = "00"
    TWENTY_FOUR_HOUR = "01"
    NO_DISPLAY = "02"
