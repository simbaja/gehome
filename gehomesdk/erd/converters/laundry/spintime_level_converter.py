import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSpinTimeLevel

_LOGGER = logging.getLogger(__name__)

class SpinTimeLevelConverter(ErdReadOnlyConverter[ErdSpinTimeLevel]):
    def erd_decode(self, value: str) -> ErdSpinTimeLevel:
        try:
            return ErdSpinTimeLevel(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSpinTimeLevel.NO_SPIN
