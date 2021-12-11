import enum
from enum import auto

@enum.unique
class ErdDataType(enum.IntFlag):
    STRING = auto()
    BOOL = auto()
    INT = auto()
    FLOAT = auto()
    DATE = auto()
    DATETIME = auto()
    TIMESPAN = auto()

