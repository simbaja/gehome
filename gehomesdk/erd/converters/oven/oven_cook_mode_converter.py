import logging
from datetime import timedelta
from gehomesdk.erd.values.advantium.advantium_enums import CookMode
from gehomesdk.erd.values.oven.oven_cook_mode import OvenCookMode
from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.oven import OvenCookSetting, ErdOvenCookMode, OVEN_COOK_MODE_MAP

_LOGGER = logging.getLogger(__name__)

class OvenCookModeConverter(ErdReadWriteConverter[OvenCookSetting]):
    def erd_decode(self, value: str) -> OvenCookSetting:
        """
        Decode the oven mode (cook mode, temperatures, times, etc)
        """
        try:
            cook_mode = ErdOvenCookMode(erd_decode_int(value[0:2]))
            return OvenCookSetting (
                cook_mode=OVEN_COOK_MODE_MAP[cook_mode], 
                temperature=erd_decode_int(value[2:6]), 
                cook_time=erd_decode_timespan(value[6:10]),
                probe_temperature=erd_decode_int(value[10:14]),
                delay_time=erd_decode_timespan(value[14:18]),
                two_temp_cook_temperature=erd_decode_int(value[18:22]),
                two_temp_cook_time=erd_decode_timespan(value[22:26]),
                raw_string=value)
        except:
            _LOGGER.error(f"Could not decode oven mode {erd_decode_int(value[0:2])}, raw value {value}")
            return OvenCookSetting(
                raw_string=value
            )
    def erd_encode(self, value: OvenCookSetting) -> str:
        """
        Encode the oven mode (cook mode, temperatures, times, etc)
        """
        cook_mode = value.cook_mode
        cook_mode_code = OVEN_COOK_MODE_MAP.inverse[cook_mode].value
        return (
            erd_encode_int(cook_mode_code,1) + 
            erd_encode_int(value.temperature) +
            erd_encode_timespan(value.cook_time) +
            erd_encode_int(value.probe_temperature) +
            erd_encode_timespan(value.delay_time) +
            erd_encode_int(value.two_temp_cook_temperature) +
            erd_encode_timespan(value.two_temp_cook_time)
        )
