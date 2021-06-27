from .laundry_enums import ErdTemperatureOption, ErdTemperatureNewOption
from .temperature_option import TemperatureOption

TEMPERATURE_OPTION_MAP = {
    ErdTemperatureOption.INVALID: TemperatureOption.DASH,
    ErdTemperatureOption.NO_HEAT: TemperatureOption.DASH,
    ErdTemperatureOption.EXTRA_LOW: TemperatureOption.EXTRA_LOW,
    ErdTemperatureOption.LOW: TemperatureOption.LOW,
    ErdTemperatureOption.MEDIUM: TemperatureOption.MEDIUM,
    ErdTemperatureOption.HIGH: TemperatureOption.HIGH
}

TEMPERATURENEW_OPTION_MAP = {
    ErdTemperatureNewOption.INVALID: TemperatureOption.DASH,
    ErdTemperatureNewOption.NO_HEAT: TemperatureOption.DASH,
    ErdTemperatureNewOption.EXTRA_LOW: TemperatureOption.EXTRA_LOW,
    ErdTemperatureNewOption.LOW: TemperatureOption.LOW,
    ErdTemperatureNewOption.MEDIUM: TemperatureOption.MEDIUM,
    ErdTemperatureNewOption.HIGH: TemperatureOption.HIGH
}
