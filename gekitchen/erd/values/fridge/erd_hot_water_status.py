import enum

@enum.unique
class ErdHotWaterStatus(enum.Enum):
    NOT_HEATING = "00"
    HEATING = "01"
    READY = "02"
    FAULT_NEED_CLEARED = "FD"
    FAULT_LOCKED_OUT = "FE"
    NA = "NA"
