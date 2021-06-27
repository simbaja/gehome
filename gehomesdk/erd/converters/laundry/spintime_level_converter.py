import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSpinTimeLevel, SpinTimeLevel, SPINTIME_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class SpinTimeLevelConverter(ErdReadOnlyConverter[SpinTimeLevel]):
    def erd_decode(self, value: str) -> SpinTimeLevel:
        try:
            om = ErdSpinTimeLevel(erd_decode_int(value))
            return SPINTIME_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdSpinTimeLevel.NO_SPIN
