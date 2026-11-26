import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.laundry import ErdSmartDispenseTankStatus

_LOGGER = logging.getLogger(__name__)

class SmartDispenseTankStatusConverter(ErdReadOnlyConverter[ErdSmartDispenseTankStatus]):
    def erd_decode(self, value: str) -> ErdSmartDispenseTankStatus:
        try:
            return ErdSmartDispenseTankStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdSmartDispenseTankStatus.UNKNOWN
