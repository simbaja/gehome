import enum

@enum.unique
class ErdMicrowaveCookMode(enum.Enum):
    NO_MODE = "00"
    TIMED = "01"
    POPCORN = "02"
    POTATO = "03"
    FROZEN_VEGETABLES = "04"
    FRESH_VEGETABLES = "05"
    PIZZA = "06"
    REHEAT = "07"
    DINNER_PLATE = "08"
    BEVERAGE = "09"
    DEFROST_BY_WEIGHT = "0A"
    DEFROST_BY_TIME = "0B"
    WARM = "0C"
    CONVECTION_BAKE = "0D"
    CONVECTION_ROAST = "OE"
    BROIL = "0F"
    BROIL_WITH_TIME = "BROIL_WITH_TIME"
    SENSOR_COOK = "10"
    AUTO_ROAST = "11"
    AUTO_BAKE = "12"
    AUTO_DEFROST = "13"
    WARM_BROIL_SENSED = "WARM_BROIL_SENSED"
    WARM_BROIL_LOW = "WARM_BROIL_LOW"
    WARM_BROIL_MEDIUM = "WARM_BROIL_MEDIUM"
    WARM_BROIL_HIGH = "WARM_BROIL_HIGH"
    DASH = "FF"

@enum.unique
class ErdMicrowaveCookStatus(enum.Enum):
    OFF = "00"
    ON = "01"
    PAUSED = "02"
    COMPLETED = "03"    
    UNKNOWN = "FF"