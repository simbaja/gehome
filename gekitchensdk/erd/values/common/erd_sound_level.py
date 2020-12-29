import enum

@enum.unique
class ErdSoundLevel(enum.Enum):
    OFF = 0
    LOW = 1
    STANDARD = 2
    HIGH = 3