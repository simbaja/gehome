import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdLaundryDoorStatus

_LOGGER = logging.getLogger(__name__)

class LaundryDoorStatusConverter(ErdReadOnlyConverter[ErdLaundryDoorStatus]):
    def erd_decode(self, value: str) -> ErdLaundryDoorStatus:
        try:
            return ErdLaundryDoorStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdLaundryDoorStatus.UNKNOWN
