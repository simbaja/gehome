from ..abstract import ErdValueConverter
from ..primitives import *
from gekitchen.erd.values.oven import OvenCookSetting, ErdOvenCookMode, OVEN_COOK_MODE_MAP

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
