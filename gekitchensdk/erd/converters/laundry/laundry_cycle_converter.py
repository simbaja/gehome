import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdLaundryCycle, LaundryCycle, LAUNDRY_CYCLE_MAP

_LOGGER = logging.getLogger(__name__)

class LaundryCycleConverter(ErdReadOnlyConverter[LaundryCycle]):
    def erd_decode(self, value: str) -> LaundryCycle:
        try:
            om = ErdLaundryCycle(erd_decode_int(value))
            return LAUNDRY_CYCLE_MAP[om].value
        except (KeyError, ValueError):
            return ErdLaundryCycle.NA
