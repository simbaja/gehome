import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdSmartDispenseTankStatus

_LOGGER = logging.getLogger(__name__)

class SmartDispenseTankStatusConverter(ErdReadOnlyConverter[ErdSmartDispenseTankStatus]):
    def erd_decode(self, value: str) -> ErdSmartDispenseTankStatus:
        try:
            return ErdSmartDispenseTankStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSmartDispenseTankStatus.INVALID
