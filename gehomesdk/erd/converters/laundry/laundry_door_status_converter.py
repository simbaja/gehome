import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdLaundryDoorStatus

_LOGGER = logging.getLogger(__name__)

class LaundryDoorStatusConverter(ErdReadOnlyConverter[ErdLaundryDoorStatus]):
    def erd_decode(self, value: str) -> ErdLaundryDoorStatus:
        try:
            return ErdLaundryDoorStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdLaundryDoorStatus.UNKNOWN
