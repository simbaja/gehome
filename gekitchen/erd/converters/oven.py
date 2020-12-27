""" ERD Converters for oven """

__all__ = (
    "ErdOvenStateConverter",
    "ErdAvailableCookModeConverter",
    "OvenCookModeConverter",
    "OvenConfigurationConverter",
    "OvenRangesConverter",
    "ErdOvenCooktopConfigConverter",
    "CooktopStatusConverter",
    "ErdPrecisionCookingAppProbeControlModeConverter",
    "ErdPrecisionCookingProbeBatteryStatusConverter",
    "ErdPrecisionCookingProbeTargetTimeReachedConverter",
    "ErdPrecisionCookingStartSousVideTimerActiveStatusConverter"
)

from .abstract import ErdReadOnlyConverter, ErdValueConverter
from .primitives import *
from gekitchen.erd.values.oven import *

class ErdOvenStateConverter(ErdReadOnlyConverter[ErdOvenState]):
    def erd_decode(self, value: str) -> ErdOvenState:
        """
        See erdCurrentState.smali
        """
        state_code = erd_decode_int(value)
        if 44 <= state_code <= 59:
            return ErdOvenState.OVEN_STATE_SPECIAL_X
        if 42 <= state_code <= 43:
            return ErdOvenState.OVEN_STATE_BAKED_GOODS
        if 40 <= state_code <= 41:
            return ErdOvenState.OVEN_STATE_FROZEN_PIZZA_MULTI
        if 38 <= state_code <= 39:
            return ErdOvenState.OVEN_STATE_FROZEN_SNACKS_MULTI
        if 36 <= state_code <= 37:
            return ErdOvenState.OVEN_STATE_FROZEN_PIZZA
        if 33 <= state_code <= 35:
            return ErdOvenState.OVEN_STATE_FROZEN_SNACKS
        if 1 <= state_code <= 27:
            # These 27 were nicely enumerated in v1.0.3 of the app, though the display logic is more similar to
            # to those above, grouping similar things. See ErdCurrentState.smali for more details.
            return ErdOvenState(state_code)
        return ErdOvenState.STATUS_DASH

class ErdAvailableCookModeConverter(ErdReadOnlyConverter[ErdAvailableCookMode]):
    def erd_decode(self, value: str) -> ErdAvailableCookMode:
        if not value:
            return {ErdAvailableCookMode.OVEN_BAKE.value.cook_mode}
        mode_bytes = [int(i) for i in erd_decode_bytes(value)]
        available_modes = {
            mode.value.cook_mode
            for mode in ErdAvailableCookMode
            if mode_bytes[mode.value.byte] & mode.value.mask
        }
        return available_modes

class OvenCookModeConverter(ErdValueConverter[OvenCookSetting]):
    def erd_decode(self, value: str) -> OvenCookSetting:
        """
        Get the cook mode and temperature.
        TODO: Figure out what the other 10 bytes are for.
            I'm guessing they have to do with two-temp cooking, probes, delayed starts, timers, etc.
        """
        byte_string = erd_decode_bytes(value)
        cook_mode_code = byte_string[0]
        temperature = int.from_bytes(byte_string[1:3], 'big')
        cook_mode = ErdOvenCookMode(cook_mode_code)
        return OvenCookSetting(cook_mode=OVEN_COOK_MODE_MAP[cook_mode], temperature=temperature, raw_bytes=byte_string)
    def erd_encode(self, value: OvenCookSetting) -> str:
        """Re-encode a cook mode and temperature
        TODO: Other ten bytes"""
        cook_mode = value.cook_mode
        cook_mode_code = OVEN_COOK_MODE_MAP.inverse[cook_mode].value
        cook_mode_hex = cook_mode_code.to_bytes(1, 'big').hex()
        temperature_hex = int(value.temperature).to_bytes(2, 'big').hex()
        return cook_mode_hex + temperature_hex + ('00' * 10)

class OvenConfigurationConverter(ErdReadOnlyConverter[OvenConfiguration]):
    def erd_decode(self, value: str) -> OvenConfiguration:
        if not value:
            n = 0
        else:
            n = erd_decode_int(value)

        config = OvenConfiguration(
            has_knob=bool(n & ErdOvenConfiguration.HAS_KNOB.value),
            has_warming_drawer=bool(n & ErdOvenConfiguration.HAS_WARMING_DRAWER.value),
            has_light_bar=bool(n & ErdOvenConfiguration.HAS_LIGHT_BAR.value),
            has_lower_oven=bool(n & ErdOvenConfiguration.HAS_LOWER_OVEN.value),
            has_lower_oven_kitchen_timer=bool(n & ErdOvenConfiguration.HAS_LOWER_OVEN_KITCHEN_TIMER.value),
            raw_value=value,
        )
        return config

class OvenRangesConverter(ErdReadOnlyConverter[OvenRanges]):  
    def erd_decode(self, value: str) -> OvenRanges:
        raw_bytes = bytes.fromhex(value)
        upper_temp = int.from_bytes(raw_bytes[:2], 'big')
        lower_temp = int.from_bytes(raw_bytes[-2:], 'big')
        return OvenRanges(
            lower=lower_temp, 
            upper=upper_temp
        )

class ErdOvenCooktopConfigConverter(ErdReadOnlyConverter[ErdCooktopConfig]):
    def erd_decode(self, value: str):       
        if value:
            try:
                present = erd_decode_int(value[:2])
                return ErdCooktopConfig.NONE if present == 0 else ErdCooktopConfig.PRESENT 
            except ValueError:
                return ErdCooktopConfig.NONE
        else:
            return ErdCooktopConfig.NONE

class CooktopStatusConverter(ErdReadOnlyConverter[CooktopStatus]):
    def erd_decode(self, value: str) -> CooktopStatus:
        if not value:
            return ErdCooktopStatus.DEFAULT()
        
        try:
            # break the string into two character segments and parse as ints
            vals = [erd_decode_int(value[i:i + 2]) for i in range(0, len(value), 2)]
            status = ErdCooktopStatus(vals[0])
            burners = {}

            burners["leftFront"] = Burner(vals[1], vals[2])
            burners["leftRear"] = Burner(vals[3], vals[4])
            burners["centerFront"] = Burner(vals[5], vals[6])
            burners["centerRear"] = Burner(vals[7], vals[8])
            burners["rightFront"] = Burner(vals[9], vals[10])
            burners["rightRear"] = Burner(vals[11], vals[12])

            return CooktopStatus(status, burners, value)
        except:
            return CooktopStatus.DEFAULT()

class ErdPrecisionCookingProbeBatteryStatusConverter(ErdReadOnlyConverter[ErdPrecisionCookingProbeBatteryStatus]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingProbeBatteryStatus:
        if value:
            try:
                return ErdPrecisionCookingProbeBatteryStatus(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingProbeBatteryStatus.NA
        else:
            return ErdPrecisionCookingProbeBatteryStatus.NA
        

class ErdPrecisionCookingAppProbeControlModeConverter(ErdReadOnlyConverter[ErdPrecisionCookingAppProbeControlMode]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingAppProbeControlMode:
        if value:
            try:
                return ErdPrecisionCookingAppProbeControlMode(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingAppProbeControlMode.NA
        else:
            return ErdPrecisionCookingAppProbeControlMode.NA
        
class ErdPrecisionCookingProbeTargetTimeReachedConverter(ErdReadOnlyConverter[ErdPrecisionCookingProbeTargetTimeReached]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingProbeTargetTimeReached:
        if value:
            try:
                return ErdPrecisionCookingProbeTargetTimeReached(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingProbeTargetTimeReached.NA
        else:
            return ErdPrecisionCookingProbeTargetTimeReached.NA
        
class ErdPrecisionCookingStartSousVideTimerActiveStatusConverter(ErdReadOnlyConverter[ErdPrecisionCookingStartSousVideTimerActiveStatus]):
    def erd_decode(self, value: str) -> ErdPrecisionCookingStartSousVideTimerActiveStatus:
        if value:
            try:
                return ErdPrecisionCookingStartSousVideTimerActiveStatus(erd_decode_int(value[:2]))  
            except ValueError:
                return ErdPrecisionCookingStartSousVideTimerActiveStatus.NA
        else:
            return ErdPrecisionCookingStartSousVideTimerActiveStatus.NA
