from typing import Any
from .erd_code_class import ErdCodeClass
from .erd_codes import ErdCode
from .converters import *

class ErdConfigurationEntry:
    def __init__(self, erd_code: ErdCode, converter: ErdValueConverter, code_class: ErdCodeClass) -> None:
        super().__init__()
        self.erd_code = erd_code
        self.converter = converter
        self.code_class = code_class
        self.converter.erd_code = self.erd_code

    @property
    def can_decode(self) -> bool:
        return self.converter.can_decode
    @property
    def can_encode(self) -> bool:
        return self.converter.can_encode
        
    def erd_decode(self, value: str) -> Any:
        return self.converter.erd_decode(value)
    def erd_encode(self, value: Any) -> str:
        return self.converter.erd_encode(value)
        
_configuration = [
    #Universal
    ErdConfigurationEntry(ErdCode.APPLIANCE_TYPE, ErdApplianceTypeConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.MODEL_NUMBER, ErdModelSerialConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.SERIAL_NUMBER, ErdModelSerialConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.SABBATH_MODE, ErdBoolConverter(), ErdCodeClass.SABBATH_CONTROL),
    ErdConfigurationEntry(ErdCode.ACM_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.APPLIANCE_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.LCD_UPDATING, ErdReadOnlyBoolConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.CLOCK_FORMAT, ErdClockFormatConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.END_TONE, ErdEndToneConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.SOUND_LEVEL, ErdSoundLevelConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.TEMPERATURE_UNIT, ErdMeasurementUnitsConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.APPLIANCE_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.APPLIANCE_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.LCD_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.LCD_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.WIFI_MODULE_SW_VERSION, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.WIFI_MODULE_SW_VERSION_AVAILABLE, ErdSoftwareVersionConverter(), ErdCodeClass.GENERAL),

    #Fridge
    ErdConfigurationEntry(ErdCode.HOT_WATER_SET_TEMP, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.HOT_WATER_IN_USE, ErdReadOnlyBoolConverter(), ErdCodeClass.DISPENSER_SENSOR),
    ErdConfigurationEntry(ErdCode.TURBO_FREEZE_STATUS, ErdBoolConverter(), ErdCodeClass.FREEZER_SENSOR),
    ErdConfigurationEntry(ErdCode.TURBO_COOL_STATUS, ErdBoolConverter(), ErdCodeClass.FRIDGE_SENSOR),
    ErdConfigurationEntry(ErdCode.DOOR_STATUS, FridgeDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.HOT_WATER_STATUS, HotWaterStatusConverter(), ErdCodeClass.DISPENSER_SENSOR),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_BUCKET_STATUS, FridgeIceBucketStatusConverter(), ErdCodeClass.FREEZER_SENSOR),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_CONTROL, IceMakerControlStatusConverter(), ErdCodeClass.FREEZER_SENSOR),
    ErdConfigurationEntry(ErdCode.AIR_FILTER_STATUS, ErdFilterStatusConverter(), ErdCodeClass.FRIDGE_SENSOR),
    ErdConfigurationEntry(ErdCode.WATER_FILTER_STATUS, ErdFilterStatusConverter(), ErdCodeClass.FRIDGE_SENSOR),
    ErdConfigurationEntry(ErdCode.SETPOINT_LIMITS, FridgeSetPointLimitsConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.CURRENT_TEMPERATURE, FridgeSetPointsConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.TEMPERATURE_SETTING, FridgeSetPointsConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.FRIDGE_MODEL_INFO, FridgeModelInfoConverter(), ErdCodeClass.GENERAL),
    
    #Oven
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.OVEN_SENSOR),

    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.RAW_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.OVEN_SENSOR),

    ErdConfigurationEntry(ErdCode.CONVECTION_CONVERSION, ErdBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.HOUR_12_SHUTOFF_ENABLED, ErdBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.OVEN_CONFIGURATION, OvenConfigurationConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.OVEN_MODE_MIN_MAX_TEMP, OvenRangesConverter(), ErdCodeClass.RAW_TEMPERATURE),

    ErdConfigurationEntry(ErdCode.COOKTOP_CONFIG, ErdCooktopConfigConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.COOKTOP_STATUS, CooktopStatusConverter(), ErdCodeClass.GENERAL),

    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_CONTROL_MODE, ErdPrecisionCookingAppProbeControlModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_STATUS, ErdReadOnlyIntConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_TARGET, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_CURRENT, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_TARGET, ErdTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS, ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_CURRENT, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TARGET_TIME_REACHED, ErdPrecisionCookingProbeTargetTimeReachedConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_BATTERY_STATUS, ErdPrecisionCookingProbeBatteryStatusConverter(), ErdCodeClass.BATTERY),

    # Dishwasher
    ErdConfigurationEntry(ErdCode.CYCLE_NAME, ErdReadOnlyStringConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.PODS_REMAINING_VALUE, ErdIntConverter(), ErdCodeClass.COUNTER),
    ErdConfigurationEntry(ErdCode.TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.CYCLE_STATE, ErdCycleStateConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.OPERATING_MODE, OperatingModeConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.RINSE_AGENT, ErdRinseAgentConverter(), ErdCodeClass.DISHWASHER_SENSOR)
]
