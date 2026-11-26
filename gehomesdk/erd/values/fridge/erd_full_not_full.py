import enum

@enum.unique
class ErdFullNotFull(enum.Enum):
    FULL = "01"
    NOT_FULL = "00"
    NA = "NA"

    def boolify(self) -> bool | None:
        if self == ErdFullNotFull.NA:
            return None
        return self == ErdFullNotFull.FULL
