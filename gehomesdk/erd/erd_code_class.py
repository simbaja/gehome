import enum
from enum import auto

@enum.unique
class ErdCodeClass(enum.IntFlag):
    NONE = auto()
    GENERAL = auto()
    CLOCK = auto()
    TIMER = auto()
    COUNTER = auto()
    NON_ZERO_TEMPERATURE = auto()
    RAW_TEMPERATURE = auto()
    DOOR = auto()
    BATTERY = auto()
    LOCK_CONTROL = auto()
    SABBATH_CONTROL = auto()
    COOLING_CONTROL = auto()
    TEMPERATURE_CONTROL = auto()
    PERCENTAGE = auto()
    FLOW_RATE = auto()
    OVEN_SENSOR = auto()
    FRIDGE_SENSOR = auto()
    FREEZER_SENSOR = auto()
    DISPENSER_SENSOR = auto()
    DISHWASHER_SENSOR = auto() 
    LAUNDRY_SENSOR = auto() 
    MICROWAVE_SENSOR = auto()
    ADVANTIUM_SENSOR = auto()
    WATERFILTER_SENSOR = auto()
