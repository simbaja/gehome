from typing import Any

from .erd_data_type import ErdDataType
from .erd_code_class import ErdCodeClass
from .erd_codes import ErdCode
from .converters import *

class ErdConfigurationEntry:
    def __init__(self, erd_code: ErdCode, converter: ErdValueConverter, code_class: ErdCodeClass, data_type: ErdDataType = ErdDataType.STRING) -> None:
        super().__init__()
        self.erd_code = erd_code
        self.converter = converter
        self.code_class = code_class
        self.converter.erd_code = self.erd_code
        self.data_type = data_type

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
    ErdConfigurationEntry(ErdCode.HOT_WATER_SET_TEMP, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.HOT_WATER_IN_USE, ErdReadOnlyBoolConverter(), ErdCodeClass.DISPENSER_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.TURBO_FREEZE_STATUS, ErdBoolConverter(), ErdCodeClass.COOLING_CONTROL, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.TURBO_COOL_STATUS, ErdBoolConverter(), ErdCodeClass.COOLING_CONTROL, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.DOOR_STATUS, FridgeDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.HOT_WATER_STATUS, HotWaterStatusConverter(), ErdCodeClass.DISPENSER_SENSOR),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_BUCKET_STATUS, FridgeIceBucketStatusConverter(), ErdCodeClass.FREEZER_SENSOR),
    ErdConfigurationEntry(ErdCode.ICE_MAKER_CONTROL, IceMakerControlStatusConverter(), ErdCodeClass.FREEZER_SENSOR),
    ErdConfigurationEntry(ErdCode.AIR_FILTER_STATUS, ErdFilterStatusConverter(), ErdCodeClass.FRIDGE_SENSOR),
    ErdConfigurationEntry(ErdCode.WATER_FILTER_STATUS, ErdFilterStatusConverter(), ErdCodeClass.FRIDGE_SENSOR),
    ErdConfigurationEntry(ErdCode.SETPOINT_LIMITS, FridgeSetPointLimitsConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.CURRENT_TEMPERATURE, FridgeSetPointsConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.TEMPERATURE_SETTING, FridgeSetPointsConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.FRIDGE_MODEL_INFO, FridgeModelInfoConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.INTERIOR_LIGHT, ErdIntConverter(length=1), ErdCodeClass.LIGHT, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.PROXIMITY_LIGHT, ErdOnOffConverter(), ErdCodeClass.LIGHT),
    ErdConfigurationEntry(ErdCode.CONVERTABLE_DRAWER_MODE, ErdConvertableDrawerModeConverter(), ErdCodeClass.FRIDGE_SENSOR),

    #Oven
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_EXTENDED_COOK_MODES, ErdExtendedCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_LIGHT, ErdOvenLightLevelConverter(), ErdCodeClass.LIGHT),
    ErdConfigurationEntry(ErdCode.LOWER_OVEN_LIGHT_AVAILABILITY, ErdOvenLightLevelAvailabilityConverter(), ErdCodeClass.OVEN_SENSOR),

    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_REMOTE_ENABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.OVEN_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DISPLAY_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_PROBE_DISPLAY_TEMP, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_RAW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_USER_TEMP_OFFSET, ErdIntConverter(), ErdCodeClass.RAW_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_DELAY_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_ELAPSED_COOK_TIME, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_KITCHEN_TIMER, ErdTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_CURRENT_STATE, ErdOvenStateConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_AVAILABLE_COOK_MODES, ErdAvailableCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_EXTENDED_COOK_MODES, ErdExtendedCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_COOK_MODE, OvenCookModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_LIGHT, ErdOvenLightLevelConverter(), ErdCodeClass.LIGHT),
    ErdConfigurationEntry(ErdCode.UPPER_OVEN_LIGHT_AVAILABILITY, ErdOvenLightLevelAvailabilityConverter(), ErdCodeClass.OVEN_SENSOR),

    ErdConfigurationEntry(ErdCode.CONVECTION_CONVERSION, ErdBoolConverter(), ErdCodeClass.OVEN_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.HOUR_12_SHUTOFF_ENABLED, ErdBoolConverter(), ErdCodeClass.OVEN_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.OVEN_CONFIGURATION, OvenConfigurationConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.OVEN_MODE_MIN_MAX_TEMP, OvenRangesConverter(), ErdCodeClass.OVEN_SENSOR),

    ErdConfigurationEntry(ErdCode.COOKTOP_CONFIG, ErdCooktopConfigConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.COOKTOP_STATUS, CooktopStatusConverter(), ErdCodeClass.GENERAL),

    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_CONTROL_MODE, ErdPrecisionCookingAppProbeControlModeConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_STATUS, ErdReadOnlyIntConverter(), ErdCodeClass.OVEN_SENSOR),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_TARGET, ErdIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TEMP_CURRENT, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_TARGET, ErdTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS, ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TIME_CURRENT, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_TARGET_TIME_REACHED, ErdPrecisionCookingProbeTargetTimeReachedConverter(), ErdCodeClass.GENERAL),
    ErdConfigurationEntry(ErdCode.PRECISION_COOKING_PROBE_BATTERY_STATUS, ErdPrecisionCookingProbeBatteryStatusConverter(), ErdCodeClass.BATTERY),

    # Dishwasher
    ErdConfigurationEntry(ErdCode.DISHWASHER_CYCLE_NAME, CycleNameConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_PODS_REMAINING_VALUE, ErdIntConverter(), ErdCodeClass.COUNTER, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.DISHWASHER_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.DISHWASHER_CYCLE_STATE, ErdCycleStateConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_OPERATING_MODE, OperatingModeConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_RINSE_AGENT, ErdRinseAgentConverter(), ErdCodeClass.DISHWASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_DOOR_STATUS, ErdDishwasherDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.DISHWASHER_USER_SETTING, ErdUserSettingConverter(), ErdCodeClass.DISHWASHER_SENSOR),

    # Laundry
    ErdConfigurationEntry(ErdCode.LAUNDRY_MACHINE_STATE, MachineStateConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_SUB_CYCLE, LaundrySubCycleConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_END_OF_CYCLE, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_TIME_REMAINING, ErdTimeSpanConverter(uom="seconds"), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DELAY_TIME_REMAINING, ErdTimeSpanConverter(uom="minutes"), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DOOR, LaundryDoorStatusConverter(), ErdCodeClass.DOOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_CYCLE, LaundryCycleConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_REMOTE_STATUS, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_REMOTE_DELAY_CONTROL, ErdTimeSpanConverter(), ErdCodeClass.LAUNDRY_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_REMOTE_POWER_CONTROL, ErdOnOffConverter(), ErdCodeClass.LAUNDRY_SENSOR),

    # Laundry - Washer
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_DOOR_LOCK, ErdReadOnlyBoolConverter(), ErdCodeClass.LOCK_CONTROL, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TANK_STATUS, ErdReadOnlyIntConverter(), ErdCodeClass.PERCENTAGE),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TANK_SELECTED, TankSelectedConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SOIL_LEVEL, SoilLevelConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_WASHTEMP_LEVEL, WashTempLevelConverter(), ErdCodeClass.TEMPERATURE_CONTROL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SPINTIME_LEVEL, SpinTimeLevelConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_RINSE_OPTION, RinseOptionConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SMART_DISPENSE_TANK_STATUS, SmartDispenseTankStatusConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_SMART_DISPENSE, SmartDispenseConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TIMESAVER, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_POWERSTEAM, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_PREWASH, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_WASHER_TUMBLECARE, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_WASHER_SENSOR),

    # Laundry - Dryer
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_DRYNESS_LEVEL, DrynessLevelConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_DRYNESSNEW_LEVEL, DrynessNewLevelConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TUMBLE_STATUS, TumbleStatusConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TUMBLENEW_STATUS, TumbleStatusConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TEMPERATURE_OPTION, TemperatureOptionConverter(), ErdCodeClass.TEMPERATURE_CONTROL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_TEMPERATURENEW_OPTION, TemperatureNewOptionConverter(), ErdCodeClass.TEMPERATURE_CONTROL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_LEVEL_SENSOR_DISABLED, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_SHEET_USAGE_CONFIGURATION, SheetUsageConfigurationConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_SHEET_INVENTORY, ErdIntConverter(), ErdCodeClass.COUNTER, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_ECODRY_STATUS, EcoDryStatusConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR),
    ErdConfigurationEntry(ErdCode.LAUNDRY_DRYER_WASHERLINK_STATUS, ErdReadOnlyBoolConverter(), ErdCodeClass.LAUNDRY_DRYER_SENSOR, ErdDataType.BOOL),

    # Microwave
    ErdConfigurationEntry(ErdCode.MICROWAVE_REMOTE_ENABLE, ErdReadOnlyBoolConverter(), ErdCodeClass.MICROWAVE_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.MICROWAVE_COOK_SETTING, ErdMicrowaveCookSettingConverter(), ErdCodeClass.MICROWAVE_SENSOR),
    ErdConfigurationEntry(ErdCode.MICROWAVE_AVAILABLE_MODES, ErdMicrowaveAvailableModesConverter(), ErdCodeClass.MICROWAVE_SENSOR),
    ErdConfigurationEntry(ErdCode.MICROWAVE_STATE, ErdMicrowaveStateConverter(), ErdCodeClass.MICROWAVE_SENSOR),
    ErdConfigurationEntry(ErdCode.MICROWAVE_COOK_TIMER, ErdMicrowaveCookTimerConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.MICROWAVE_KITCHEN_TIMER, ErdMicrowaveCookTimerConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),

    # Advantium
    ErdConfigurationEntry(ErdCode.ADVANTIUM_KITCHEN_TIME_REMAINING, ErdReadOnlyTimeSpanConverter(uom="seconds"), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_REMAINING, ErdAdvantiumCookTimeRemainingConverter(), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_ADJUST, ErdAdvantiumCookTimeAdjustConverter() , ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_REMOTE_COOK_MODE_CONFIG, ErdAdvantiumRemoteCookModeConfigConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_STATUS, ErdAdvantiumCookStatusConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_SETTING, ErdAdvantiumCookSettingConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_PRECISION_VERSION, ErdReadOnlyBytesConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_KITCHEN_TIMER_MIN_MAX, ErdAdvantiumKitchenTimerMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_PRECISION_MIN_MAX, ErdAdvantiumPrecisionMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_MICROWAVE_MIN_MAX, ErdAdvantiumMicrowaveMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),
    ErdConfigurationEntry(ErdCode.ADVANTIUM_COOK_TIME_MIN_MAX, ErdAdvantiumCookTimeMinMaxConverter(), ErdCodeClass.ADVANTIUM_SENSOR),

    # Water Filter
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_RATE, ErdWaterFilterFlowConverter(), ErdCodeClass.FLOW_RATE, ErdDataType.FLOAT),
    ErdConfigurationEntry(ErdCode.WH_FILTER_VALVE_STATE, ErdFilterValveStateConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_MODE, ErdFilterModeConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_DAY_USAGE, ErdReadOnlyIntConverter(), ErdCodeClass.LIQUID_VOLUME, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_ALERT, ErdFilterAlertStateConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_FLOW_ALERT_SETTINGS, ErdWaterFilterAlertSettingsConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_LEAK_VALIDITY, ErdFilterLeakValidityConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_MANUAL_MODE, ErdFilterManualModeConverter(), ErdCodeClass.WATERFILTER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_FILTER_LIFE_REMAINING, ErdWaterFilterLifeRemainingConverter(), ErdCodeClass.PERCENTAGE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.WH_FILTER_POSITION, ErdFilterPositionConverter(), ErdCodeClass.WATERFILTER_SENSOR),

    # Water Softener
    ErdConfigurationEntry(ErdCode.WH_SOFTENER_ERROR_CODE, ErdWaterSoftenerErrorCodeConverter(), ErdCodeClass.WATERSOFTENER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_SOFTENER_LOW_SALT, ErdWaterSoftenerSaltLevelConverter(), ErdCodeClass.WATERSOFTENER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_SOFTENER_SALT_LIFE_REMAINING, ErdIntConverter(), ErdCodeClass.WATERSOFTENER_SENSOR, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.WH_SOFTENER_SHUTOFF_VALVE_STATE, ErdWaterSoftenerShutoffValveStateConverter(), ErdCodeClass.WATERSOFTENER_SENSOR),
    ErdConfigurationEntry(ErdCode.WH_SOFTENER_SHUTOFF_VALVE_CONTROL, ErdWaterSoftenerShutoffValveStateConverter(), ErdCodeClass.WATERSOFTENER_SENSOR),

    #AC
    ErdConfigurationEntry(ErdCode.AC_TARGET_TEMPERATURE, ErdAcTargetTemperatureConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.AC_FAN_SETTING, ErdAcFanSettingConverter(), ErdCodeClass.FAN),
    ErdConfigurationEntry(ErdCode.AC_OPERATION_MODE, ErdAcOperationModeConverter(), ErdCodeClass.AC_SENSOR),
    ErdConfigurationEntry(ErdCode.AC_AMBIENT_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.AC_FILTER_STATUS, ErdAcFilterStatusConverter(), ErdCodeClass.AC_SENSOR),
    ErdConfigurationEntry(ErdCode.AC_POWER_STATUS, ErdOnOffConverter(), ErdCodeClass.AC_SENSOR),
    
    #Window AC
    ErdConfigurationEntry(ErdCode.WAC_DEMAND_RESPONSE_POWER, ErdWacDemandResponsePowerConverter(), ErdCodeClass.POWER, ErdDataType.FLOAT),
    ErdConfigurationEntry(ErdCode.WAC_DEMAND_RESPONSE_STATE, ErdWacDemandResponseStateConverter(), ErdCodeClass.AC_SENSOR),

    #Split AC
    ErdConfigurationEntry(ErdCode.SAC_AVAILABLE_MODES, ErdSacAvailableModesConverter(), ErdCodeClass.AC_SENSOR),
    ErdConfigurationEntry(ErdCode.SAC_SLEEP_MODE, ErdOnOffConverter(), ErdCodeClass.AC_SENSOR),
    ErdConfigurationEntry(ErdCode.SAC_TARGET_TEMPERATURE_RANGE, ErdSacTargetTemperatureRangeConverter(), ErdCodeClass.AC_SENSOR),
    ErdConfigurationEntry(ErdCode.SAC_AUTO_SWING_MODE, ErdOnOffConverter(), ErdCodeClass.AC_SENSOR),

    #Hood
    ErdConfigurationEntry(ErdCode.HOOD_LIGHT_LEVEL, ErdHoodLightLevelConverter(), ErdCodeClass.LIGHT),
    ErdConfigurationEntry(ErdCode.HOOD_LIGHT_LEVEL_AVAILABILITY, ErdHoodLightLevelAvailabilityConverter(), ErdCodeClass.HOOD_SENSOR),
    ErdConfigurationEntry(ErdCode.HOOD_FAN_SPEED, ErdHoodFanSpeedConverter(), ErdCodeClass.FAN),
    ErdConfigurationEntry(ErdCode.HOOD_FAN_SPEED_AVAILABILITY, ErdHoodFanSpeedAvailabilityConverter(), ErdCodeClass.HOOD_SENSOR),
    ErdConfigurationEntry(ErdCode.HOOD_DELAY_OFF, ErdOnOffConverter(), ErdCodeClass.HOOD_SENSOR),
    ErdConfigurationEntry(ErdCode.HOOD_TIMER, ErdTimeSpanConverter(uom="seconds"), ErdCodeClass.TIMER, ErdDataType.TIMESPAN),
    ErdConfigurationEntry(ErdCode.HOOD_TIMER_AVAILABILITY, ErdOnOffConverter(), ErdCodeClass.HOOD_SENSOR),

    #Opal Ice Maker
    ErdConfigurationEntry(ErdCode.OIM_STATUS, ErdOimStatusConverter(), ErdCodeClass.OIM_SENSOR),
    ErdConfigurationEntry(ErdCode.OIM_POWER, ErdOnOffConverter(), ErdCodeClass.OIM_SENSOR),
    ErdConfigurationEntry(ErdCode.OIM_FILTER_STATUS, ErdOimFilterStatusConverter(), ErdCodeClass.OIM_SENSOR),
    ErdConfigurationEntry(ErdCode.OIM_LIGHT_LEVEL, ErdOimLightLevelConverter(), ErdCodeClass.LIGHT),

    #Cafe Coffee Maker
    ErdConfigurationEntry(ErdCode.CCM_IS_BREWING, ErdReadOnlyBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_BREW_STRENGTH, ErdCcmBrewStrengthConverter(), ErdCodeClass.CCM_SENSOR),
    ErdConfigurationEntry(ErdCode.CCM_BREW_CUPS, ErdReadOnlyIntConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.CCM_BREW_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.CCM_BREW_TEMPERATURE_RANGE, ErdCcmBrewTemperatureRangeConverter(), ErdCodeClass.CCM_SENSOR),
    ErdConfigurationEntry(ErdCode.CCM_BREW_SETTINGS, ErdCcmBrewSettingsConverter(), ErdCodeClass.CCM_SENSOR),
    ErdConfigurationEntry(ErdCode.CCM_CANCEL_BREWING, ErdBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_POT_PRESENT, ErdReadOnlyBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_OUT_OF_WATER, ErdReadOnlyBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_CURRENT_WATER_TEMPERATURE, ErdReadOnlyIntConverter(), ErdCodeClass.NON_ZERO_TEMPERATURE, ErdDataType.INT),
    ErdConfigurationEntry(ErdCode.CCM_IS_DESCALING, ErdReadOnlyBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_START_DESCALING, ErdBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
    ErdConfigurationEntry(ErdCode.CCM_CANCEL_DESCALING, ErdBoolConverter(), ErdCodeClass.CCM_SENSOR, ErdDataType.BOOL),
]
