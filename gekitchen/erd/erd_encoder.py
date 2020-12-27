import logging
from typing import Any

from .erd_codes import ErdCode, ErdCodeType
from .converters import *

_LOGGER = logging.getLogger(__name__)

class ErdEncoder:
    # Create the converter registry for all known types
    _registry = {
        #Universal
        ErdCode.APPLIANCE_TYPE: ErdApplianceTypeConverter(ErdCode.APPLIANCE_TYPE),
        ErdCode.MODEL_NUMBER: ErdModelSerialConverter(ErdCode.MODEL_NUMBER),
        ErdCode.SERIAL_NUMBER: ErdModelSerialConverter(ErdCode.SERIAL_NUMBER),
        ErdCode.SABBATH_MODE: ErdBoolConverter(ErdCode.SABBATH_MODE),
        ErdCode.ACM_UPDATING: ErdReadOnlyBoolConverter(ErdCode.ACM_UPDATING),
        ErdCode.APPLIANCE_UPDATING: ErdReadOnlyBoolConverter(ErdCode.APPLIANCE_UPDATING),
        ErdCode.LCD_UPDATING: ErdReadOnlyBoolConverter(ErdCode.LCD_UPDATING),
        ErdCode.CLOCK_FORMAT: ErdClockFormatConverter(ErdCode.CLOCK_FORMAT),
        ErdCode.END_TONE: ErdEndToneConverter(ErdCode.END_TONE),
        ErdCode.SOUND_LEVEL: ErdSoundLevelConverter(ErdCode.SOUND_LEVEL),
        ErdCode.TEMPERATURE_UNIT: ErdMeasurementUnitsConverter(ErdCode.TEMPERATURE_UNIT),
        ErdCode.APPLIANCE_SW_VERSION: ErdSoftwareVersionConverter(ErdCode.APPLIANCE_SW_VERSION),
        ErdCode.APPLIANCE_SW_VERSION_AVAILABLE: ErdSoftwareVersionConverter(ErdCode.APPLIANCE_SW_VERSION_AVAILABLE),
        ErdCode.LCD_SW_VERSION: ErdSoftwareVersionConverter(ErdCode.LCD_SW_VERSION),
        ErdCode.LCD_SW_VERSION_AVAILABLE: ErdSoftwareVersionConverter(ErdCode.LCD_SW_VERSION_AVAILABLE),
        ErdCode.WIFI_MODULE_SW_VERSION: ErdSoftwareVersionConverter(ErdCode.WIFI_MODULE_SW_VERSION),
        ErdCode.WIFI_MODULE_SW_VERSION_AVAILABLE: ErdSoftwareVersionConverter(ErdCode.WIFI_MODULE_SW_VERSION_AVAILABLE),

        #Fridge
        ErdCode.HOT_WATER_SET_TEMP: ErdIntConverter(ErdCode.HOT_WATER_SET_TEMP),
        ErdCode.HOT_WATER_IN_USE: ErdReadOnlyBoolConverter(ErdCode.HOT_WATER_IN_USE),
        ErdCode.TURBO_FREEZE_STATUS: ErdBoolConverter(ErdCode.TURBO_FREEZE_STATUS),
        ErdCode.TURBO_COOL_STATUS: ErdBoolConverter(ErdCode.TURBO_COOL_STATUS),
        ErdCode.DOOR_STATUS: FridgeDoorStatusConverter(ErdCode.DOOR_STATUS),
        ErdCode.HOT_WATER_STATUS: HotWaterStatusConverter(ErdCode.HOT_WATER_STATUS),
        ErdCode.ICE_MAKER_BUCKET_STATUS: FridgeIceBucketStatusConverter(ErdCode.ICE_MAKER_BUCKET_STATUS),
        ErdCode.ICE_MAKER_CONTROL: IceMakerControlStatusConverter(ErdCode.ICE_MAKER_CONTROL),
        ErdCode.WATER_FILTER_STATUS: ErdFilterStatusConverter(ErdCode.WATER_FILTER_STATUS),
        ErdCode.SETPOINT_LIMITS: FridgeSetPointLimitsConverter(ErdCode.SETPOINT_LIMITS),
        ErdCode.CURRENT_TEMPERATURE: FridgeSetPointsConverter(ErdCode.CURRENT_TEMPERATURE),
        ErdCode.TEMPERATURE_SETTING: FridgeSetPointsConverter(ErdCode.TEMPERATURE_SETTING),

        #Oven
        ErdCode.LOWER_OVEN_PROBE_PRESENT: ErdReadOnlyBoolConverter(ErdCode.LOWER_OVEN_PROBE_PRESENT),
        ErdCode.LOWER_OVEN_REMOTE_ENABLED: ErdReadOnlyBoolConverter(ErdCode.LOWER_OVEN_REMOTE_ENABLED),
        ErdCode.LOWER_OVEN_DISPLAY_TEMPERATURE: ErdReadOnlyIntConverter(ErdCode.LOWER_OVEN_DISPLAY_TEMPERATURE),
        ErdCode.LOWER_OVEN_PROBE_DISPLAY_TEMP: ErdReadOnlyIntConverter(ErdCode.LOWER_OVEN_PROBE_DISPLAY_TEMP),
        ErdCode.LOWER_OVEN_RAW_TEMPERATURE: ErdReadOnlyIntConverter(ErdCode.LOWER_OVEN_RAW_TEMPERATURE),
        ErdCode.LOWER_OVEN_USER_TEMP_OFFSET: ErdIntConverter(ErdCode.LOWER_OVEN_USER_TEMP_OFFSET),
        ErdCode.LOWER_OVEN_COOK_TIME_REMAINING: ErdReadOnlyTimeSpanConverter(ErdCode.LOWER_OVEN_COOK_TIME_REMAINING),
        ErdCode.LOWER_OVEN_DELAY_TIME_REMAINING: ErdReadOnlyTimeSpanConverter(ErdCode.LOWER_OVEN_DELAY_TIME_REMAINING),
        ErdCode.LOWER_OVEN_ELAPSED_COOK_TIME: ErdReadOnlyTimeSpanConverter(ErdCode.LOWER_OVEN_ELAPSED_COOK_TIME),
        ErdCode.LOWER_OVEN_KITCHEN_TIMER: ErdTimeSpanConverter(ErdCode.LOWER_OVEN_KITCHEN_TIMER),
        ErdCode.LOWER_OVEN_CURRENT_STATE: ErdOvenStateConverter(ErdCode.LOWER_OVEN_CURRENT_STATE),
        ErdCode.LOWER_OVEN_AVAILABLE_COOK_MODES: ErdAvailableCookModeConverter(ErdCode.LOWER_OVEN_AVAILABLE_COOK_MODES),
        ErdCode.LOWER_OVEN_COOK_MODE: OvenCookModeConverter(ErdCode.LOWER_OVEN_COOK_MODE),

        ErdCode.UPPER_OVEN_PROBE_PRESENT: ErdReadOnlyBoolConverter(ErdCode.UPPER_OVEN_PROBE_PRESENT),
        ErdCode.UPPER_OVEN_REMOTE_ENABLED: ErdReadOnlyBoolConverter(ErdCode.UPPER_OVEN_REMOTE_ENABLED),
        ErdCode.UPPER_OVEN_DISPLAY_TEMPERATURE: ErdReadOnlyIntConverter(ErdCode.UPPER_OVEN_DISPLAY_TEMPERATURE),
        ErdCode.UPPER_OVEN_PROBE_DISPLAY_TEMP: ErdReadOnlyIntConverter(ErdCode.UPPER_OVEN_PROBE_DISPLAY_TEMP),
        ErdCode.UPPER_OVEN_RAW_TEMPERATURE: ErdReadOnlyIntConverter(ErdCode.UPPER_OVEN_RAW_TEMPERATURE),
        ErdCode.UPPER_OVEN_USER_TEMP_OFFSET: ErdIntConverter(ErdCode.UPPER_OVEN_USER_TEMP_OFFSET),
        ErdCode.UPPER_OVEN_COOK_TIME_REMAINING: ErdReadOnlyTimeSpanConverter(ErdCode.UPPER_OVEN_COOK_TIME_REMAINING),
        ErdCode.UPPER_OVEN_DELAY_TIME_REMAINING: ErdReadOnlyTimeSpanConverter(ErdCode.UPPER_OVEN_DELAY_TIME_REMAINING),
        ErdCode.UPPER_OVEN_ELAPSED_COOK_TIME: ErdReadOnlyTimeSpanConverter(ErdCode.UPPER_OVEN_ELAPSED_COOK_TIME),
        ErdCode.UPPER_OVEN_KITCHEN_TIMER: ErdTimeSpanConverter(ErdCode.UPPER_OVEN_KITCHEN_TIMER),
        ErdCode.UPPER_OVEN_CURRENT_STATE: ErdOvenStateConverter(ErdCode.UPPER_OVEN_CURRENT_STATE),
        ErdCode.UPPER_OVEN_AVAILABLE_COOK_MODES: ErdAvailableCookModeConverter(ErdCode.UPPER_OVEN_AVAILABLE_COOK_MODES),
        ErdCode.UPPER_OVEN_COOK_MODE: OvenCookModeConverter(ErdCode.UPPER_OVEN_COOK_MODE),

        ErdCode.CONVECTION_CONVERSION: ErdBoolConverter(ErdCode.CONVECTION_CONVERSION),
        ErdCode.HOUR_12_SHUTOFF_ENABLED: ErdBoolConverter(ErdCode.HOUR_12_SHUTOFF_ENABLED),
        ErdCode.OVEN_CONFIGURATION: OvenConfigurationConverter(ErdCode.OVEN_CONFIGURATION),
        ErdCode.OVEN_MODE_MIN_MAX_TEMP: OvenRangesConverter(ErdCode.OVEN_MODE_MIN_MAX_TEMP),

        ErdCode.COOKTOP_CONFIG: ErdCooktopConfigConverter(ErdCode.COOKTOP_CONFIG),
        ErdCode.COOKTOP_STATUS: CooktopStatusConverter(ErdCode.COOKTOP_STATUS),

        ErdCode.PRECISION_COOKING_PROBE_CONTROL_MODE: ErdPrecisionCookingAppProbeControlModeConverter(ErdCode.PRECISION_COOKING_PROBE_CONTROL_MODE),
        ErdCode.PRECISION_COOKING_PROBE_STATUS: ErdReadOnlyIntConverter(ErdCode.PRECISION_COOKING_PROBE_STATUS), #TODO: Figure out the two variables here
        ErdCode.PRECISION_COOKING_PROBE_TEMP_TARGET: ErdIntConverter(ErdCode.PRECISION_COOKING_PROBE_TEMP_TARGET, 4),
        ErdCode.PRECISION_COOKING_PROBE_TEMP_CURRENT: ErdReadOnlyIntConverter(ErdCode.PRECISION_COOKING_PROBE_TEMP_CURRENT),
        ErdCode.PRECISION_COOKING_PROBE_TIME_TARGET: ErdTimeSpanConverter(ErdCode.PRECISION_COOKING_PROBE_TIME_TARGET),
        ErdCode.PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS: ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(ErdCode.PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS),
        ErdCode.PRECISION_COOKING_PROBE_TIME_CURRENT: ErdReadOnlyTimeSpanConverter(ErdCode.PRECISION_COOKING_PROBE_TIME_CURRENT),
        ErdCode.PRECISION_COOKING_PROBE_TARGET_TIME_REACHED: ErdPrecisionCookingProbeTargetTimeReachedConverter(ErdCode.PRECISION_COOKING_PROBE_TARGET_TIME_REACHED),
        ErdCode.PRECISION_COOKING_PROBE_BATTERY_STATUS: ErdPrecisionCookingProbeBatteryStatusConverter(ErdCode.PRECISION_COOKING_PROBE_BATTERY_STATUS),

        # Dishwasher
        ErdCode.CYCLE_NAME: ErdReadOnlyStringConverter(ErdCode.CYCLE_NAME),
        ErdCode.PODS_REMAINING_VALUE: ErdIntConverter(ErdCode.PODS_REMAINING_VALUE),
        ErdCode.TIME_REMAINING: ErdReadOnlyTimeSpanConverter(ErdCode.TIME_REMAINING),
        ErdCode.CYCLE_STATE: ErdCycleStateConverter(ErdCode.CYCLE_STATE),
        ErdCode.OPERATING_MODE: OperatingModeConverter(ErdCode.OPERATING_MODE),
        ErdCode.RINSE_AGENT: ErdRinseAgentConverter(ErdCode.RINSE_AGENT),
    }

    def translate_code(self, erd_code: ErdCodeType) -> ErdCodeType:
        """
        Try to resolve an ERD codes from string to ErdCode if possible.  If an ErdCode
        object is passed in, it will be returned.
        :param erd_code: ErdCode or str
        :return: Either an ErdCode object matching the `erd_code` string, or, if resolution fails,
        the `erd_code` string itself.
        """
        if isinstance(erd_code, ErdCode):
            return erd_code

        try:
            return ErdCode[erd_code]
        except KeyError:
            pass

        try:
            return ErdCode(erd_code.lower())
        except ValueError:
            return erd_code

    def decode_value(self, erd_code: ErdCodeType, erd_value: str) -> Any:
        """
        Decode and ERD Code raw value into something useful.  If the erd_code is a string that
        cannot be resolved to a known ERD Code, the value will be treated as raw byte string.
        Unregistered ERD Codes will be translated as ints.

        :param erd_code: ErdCode or str, the ERD Code the value of which we want to decode
        :param erd_value: The raw ERD code value, usually a hex string without leading "0x"
        :return: The decoded value.
        """
        if erd_value == '':
            return None

        erd_code = self.translate_code(erd_code)

        if isinstance(erd_code, str):
            return erd_decode_bytes(erd_value)

        try:
            return self._registry[erd_code].erd_decode(erd_value)
        except KeyError:
            return erd_decode_int(erd_value)

    def encode_value(self, erd_code: ErdCodeType, value: Any) -> str:
        """
        Encode an ERD Code value as a hex string.
        Only ERD Codes registered with self.erd_encoders will processed.  Otherwise an error will be returned.

        :param erd_code: ErdCode or str, the ERD Code the value of which we want to decode
        :param value: The value to re-encode
        :return: The encoded value as a hex string
        """
        if value is None:
            return ''

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].erd_encode(value)
        except KeyError:
            _LOGGER.error(f'Attempt to encode unregistered ERD code {erd_code}')
            raise

    def can_decode(self, erd_code: ErdCodeType) -> bool:
        """ 
        Indicates whether an ERD Code can be decoded. If the code
        is not registered, defaults to true
        """

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].can_decode()
        except KeyError:
            return True

    def can_encode(self, erd_code: ErdCodeType) -> bool:
        """ 
        Indicates whether an ERD Code can be encoded. If the code
        is not registered, defaults to false
        """

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].can_encode()
        except KeyError:
            return False
