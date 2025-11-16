import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdSpinTimeLevel

_LOGGER = logging.getLogger(__name__)

class SpinTimeLevelConverter(ErdReadOnlyConverter[ErdSpinTimeLevel]):
    def erd_decode(self, value: str) -> ErdSpinTimeLevel:
        try:
            return ErdSpinTimeLevel(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSpinTimeLevel.NO_SPIN
