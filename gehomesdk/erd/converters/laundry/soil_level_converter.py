import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdSoilLevel

_LOGGER = logging.getLogger(__name__)

class SoilLevelConverter(ErdReadOnlyConverter[ErdSoilLevel]):
    def erd_decode(self, value: str) -> ErdSoilLevel:
        try:
            return ErdSoilLevel(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSoilLevel.INVALID
