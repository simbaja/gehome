from .erd_temperature_option import ErdTemperatureOption
from .temperature_option import TemperatureOption

TEMPERATURE_OPTION_MAP = {
    ErdTemperatureOption.INVALID: TemperatureOption.DASH,
    ErdTemperatureOption.NO_HEAT: TemperatureOption.DASH,
    ErdTemperatureOption.EXTRA_LOW: TemperatureOption.EXTRA_LOW,
    ErdTemperatureOption.LOW: TemperatureOption.LOW,
    ErdTemperatureOption.MEDIUM: TemperatureOption.MEDIUM,
    ErdTemperatureOption.HIGH: TemperatureOption.HIGH
}
