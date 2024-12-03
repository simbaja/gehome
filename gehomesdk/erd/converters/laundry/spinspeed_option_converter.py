import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSpinSpeedOption, SpinSpeedOption, SPINSPEED_OPTION_MAP

_LOGGER = logging.getLogger(__name__)

class SpinSpeedOptionConverter(ErdReadOnlyConverter[SpinSpeedOption]):
    def erd_decode(self, value: str) -> SpinSpeedOption:
        try:
            om = ErdSpinSpeedOption(erd_decode_int(value))
            return SPINSPEED_OPTION_MAP[om].value
        except (KeyError, ValueError):
            return ErdSpinSpeedOption.DASH
