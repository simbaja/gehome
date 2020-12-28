from typing import Any
from .erd_code_class import ErdCodeClass
from .erd_codes import ErdCode
from .converters import *

class ErdConfigurationEntry:
    def __init__(self, erd_code: ErdCode, converter: ErdValueConverter, code_class: ErdCodeClass, can_boolify: bool = False) -> None:
        super().__init__()
        self.erd_code = erd_code
        self.converter = converter
        self.code_class = code_class
        self._can_boolify = can_boolify
        self.converter.erd_code = self.erd_code

    @property
    def can_decode(self) -> bool:
        return self.converter.can_decode
    @property
    def can_encode(self) -> bool:
        return self.converter.can_encode
    @property
    def can_boolify(self) -> bool:
        return self._can_boolify
        
    def erd_decode(self, value: str) -> Any:
        return self.converter.erd_decode(value)
    def erd_encode(self, value: Any) -> str:
        return self.converter.erd_encode(value)
        
_configuration = [
    #Universal
    ErdConfigurationEntry(ErdCode.APPLIANCE_TYPE, ErdApplianceTypeConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.MODEL_NUMBER, ErdModelSerialConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.SERIAL_NUMBER, ErdModelSerialConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.SABBATH_MODE, ErdBoolConverter(), ErdCodeClass.SABBATH_CONTROL, False),
    ErdConfigurationEntry(ErdCode.ACM_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, True),
    ErdConfigurationEntry(ErdCode.APPLIANCE_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, True),
    ErdConfigurationEntry(ErdCode.LCD_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, True),
    ErdConfigurationEntry(ErdCode.CLOCK_FORMAT, ErdClockFormatConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.END_TONE, ErdEndToneConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.SOUND_LEVEL, ErdSoundLevelConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.TEMPERATURE_UNIT, ErdMeasurementUnitsConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.APPLIANCE_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.APPLIANCE_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LCD_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LCD_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.WIFI_MODULE_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.WIFI_MODULE_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL, False),

    #Fridge
    ErdConfigurationEntry(ErdCode.HOT_WATER_SET_TEMP, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.HOT_WATER_IN_USE, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, True),
    ErdConfigurationEntry(ErdCode.TURBO_FREEZE_STATUS, ErdBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.TURBO_COOL_STATUS, ErdBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.DOOR_STATUS, FridgeDoorStatusConverter(), ErdCodeClass.DOOR, True),
    ErdConfigurationEntry(ErdCode.HOT_WATER_STATUS, HotWaterStatusConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_BUCKET_STATUS, FridgeIceBucketStatusConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_CONTROL, IceMakerControlStatusConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.WATER_FILTER_STATUS, ErdFilterStatusConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.SETPOINT_LIMITS, FridgeSetPointLimitsConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.CURRENT_TEMPERATURE, FridgeSetPointsConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.TEMPERATURE_SETTING, FridgeSetPointsConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),

    #Oven
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.GENERAL, False),

    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.STANDARD_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.GENERAL, False),

    ErdConfigurationEntry(ErdCode.CONVECTION_CONVERSION, ErdBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.HOUR_12_SHUTOFF_ENABLED, ErdBoolConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.OVEN_CONFIGURATION, OvenConfigurationConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.OVEN_MODE_MIN_MAX_TEMP, OvenRangesConverter(), ErdCodeClass.GENERAL, False),

    ErdConfigurationEntry(ErdCode.COOKTOP_CONFIG, ErdCooktopConfigConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.COOKTOP_STATUS, CooktopStatusConverter(), ErdCodeClass.GENERAL, False),

    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_CONTROL_MODE, ErdPrecisionCookingAppProbeControlModeConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_STATUS, ErdReadOnlyIntConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_TARGET, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_CURRENT, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_TARGET, ErdTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS, ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_CURRENT, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TARGET_TIME_REACHED, ErdPrecisionCookingProbeTargetTimeReachedConverter(), ErdCodeClass.GENERAL, True),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_BATTERY_STATUS, ErdPrecisionCookingProbeBatteryStatusConverter(), ErdCodeClass.GENERAL, False),

    # Dishwasher
    ErdConfigurationEntry(ErdCode.CYCLE_NAME, ErdReadOnlyStringConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.PODS_REMAINING_VALUE, ErdIntConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, False),
    ErdConfigurationEntry(ErdCode.CYCLE_STATE, ErdCycleStateConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.OPERATING_MODE, OperatingModeConverter(), ErdCodeClass.GENERAL, False),
    ErdConfigurationEntry(ErdCode.RINSE_AGENT, ErdRinseAgentConverter(), ErdCodeClass.GENERAL, False)
]
