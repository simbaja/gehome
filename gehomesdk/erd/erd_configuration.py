from gehomesdk.erd.converters.advantium.erd_advantium_cook_status_converter import ErdAdvantiumCookStatusConverter
from gehomesdk.erd.values.advantium.erd_advantium_kitchen_timer_min_max import ErdAdvantiumKitchenTimerMinMax
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
    ErdConfigurationEntry(ErdCode.USER_INTERFACE_LOCKED, ErdBoolConverter(), ErdCodeClass.LOCK_CONTROL),
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
    ErdConfigurationEntry(ErdCode.UNIT_TYPE, ErdUnitTypeConverter(), ErdCodeClass.GENERAL),

    #Fridge
    ErdConfigurationEntry(ErdCode.HOT_WATER_SET_TEMP, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE),
    ErdConfigurationEntry(ErdCode.HOT_WATER_IN_USE, ErdReadOnlyBoolConverter(), ErdCodeClass.DISPENSER_SENSOR),
    ErdConfigurationEntry(ErdCode.TURBO_FREEZE_STATUS, ErdBoolConverter(), ErdCodeClass.COOLING_CONTROL),
    ErdConfigurationEntry(ErdCode.TURBO_COOL_STATUS, ErdBoolConverter(), ErdCodeClass.COOLING_CONTROL),
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
    ErdConfigurationEntry(ErdCode.DISHWASHER_CYCLE_NAME, CycleNameConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_PODS_REMAINING_VALUE, ErdIntConverter(), ErdCodeClass.COUNTER),
    ErdConfigurationEntry(ErdCode.DISHWASHER_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.DISHWASHER_CYCLE_STATE, ErdCycleStateConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_OPERATING_MODE, OperatingModeConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_RINSE_AGENT, ErdRinseAgentConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_DOOR_STATUS, ErdDishwasherDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_USER_SETTING, ErdUserSettingConverter(), ErdCodeClass.DISHWASHER_SENSOR),

    # Laundry
    ErdConfigurationEntry(ErdCode.LAUNDRY_MACHINE_STATE, MachineStateConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_SUB_CYCLE, LaundrySubCycleConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_END_OF_CYCLE, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_TIME_REMAINING, ErdTimeSpanSecondsConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DELAY_TIME_REMAINING, ErdTimeSpanSecondsConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DOOR, LaundryDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_CYCLE, LaundryCycleConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_REMOTE_STATUS, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),

    # Laundry - Washer
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_DOOR_LOCK, ErdReadOnlyBoolConverter(), ErdCodeClass.LOCK_CONTROL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TANK_STATUS, ErdReadOnlyIntConverter(), ErdCodeClass.PERCENTAGE),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TANK_SELECTED, TankSelectedConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SOIL_LEVEL, SoilLevelConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_WASHTEMP_LEVEL, WashTempLevelConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SPINTIME_LEVEL, SpinTimeLevelConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_RINSE_OPTION, RinseOptionConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TIMESAVER, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_POWERSTEAM, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_PREWASH, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TUMBLECARE, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),

    # Laundry - Dryer
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_DRYNESS_LEVEL, DrynessLevelConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_DRYNESSNEW_LEVEL, DrynessNewLevelConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TUMBLE_STATUS, TumbleStatusConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TUMBLENEW_STATUS, TumbleStatusConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TEMPERATURE_OPTION, TemperatureOptionConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TEMPERATURENEW_OPTION, TemperatureNewOptionConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_LEVEL_SENSOR_DISABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_SHEET_USAGE_CONFIGURATION, SheetUsageConfigurationConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_SHEET_INVENTORY, ErdIntConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_ECODRY_STATUS, EcoDryStatusConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_WASHERLINK_STATUS, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),

    # Microwave
    ErdConfigurationEntry(ErdCode.MICROWAVE_REMOTE_ENABLE, ErdReadOnlyBoolConverter(), ErdCodeClass.MICROWAVE_SENSOR),

    # Advantium
    ErdConfigurationEntry(ErdCode.ADVANTIUM_KITCHEN_TIME_REMAINING, ErdReadOnlyTimeSpanSecondsConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_REMAINING, ErdAdvantiumCookTimeRemainingConverter(), ErdCodeClass.TIMER),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_ADJUST, ErdAdvantiumCookTimeAdjustConverter() , ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_REMOTE_COOK_MODE_CONFIG, ErdAdvantiumRemoteCookModeConfigConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_STATUS, ErdAdvantiumCookStatusConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_SETTING, ErdReadOnlyBytesConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_PRECISION_VERSION, ErdReadOnlyBytesConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_KITCHEN_TIMER_MIN_MAX, ErdAdvantiumKitchenTimerMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_PRECISION_MIN_MAX, ErdAdvantiumPrecisionMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_MICROWAVE_MIN_MAX, ErdAdvantiumMicrowaveMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_MIN_MAX, ErdAdvantiumCookTimeMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),

    # Water Filter
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_RATE, ErdWaterFilterFlowConverter(), ErdCodeClass.FLOW_RATE),
    ErdConfigurationEntry(ErdCode.WH_FILTER_VALVE_STATE, ErdFilterValveStateConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_MODE, ErdFilterModeConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_DAY_USAGE, ErdReadOnlyIntConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_ALERT, ErdFilterAlertStateConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_ALERT_SETTINGS, ErdWaterFilterAlertSettingsConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_LEAK_VALIDITY, ErdFilterLeakValidityConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_MANUAL_MODE, ErdFilterManualModeConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_LIFE_REMAINING, ErdWaterFilterLifeRemainingConverter(), ErdCodeClass.PERCENTAGE),
    ErdConfigurationEntry(ErdCode.WH_FILTER_POSITION, ErdFilterPositionConverter(), ErdCodeClass.WATERFILTER_SENSOR),
]
