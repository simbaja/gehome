import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdLaundryDoorStatus, LaundryDoorStatus, LAUNDRY_DOOR_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class LaundryDoorStatusConverter(ErdReadOnlyConverter[LaundryDoorStatus]):
    def erd_decode(self, value: str) -> LaundryDoorStatus:
        try:
            om = ErdLaundryDoorStatus(erd_decode_int(value))
            return LAUNDRY_DOOR_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdLaundryDoorStatus.CLOSED
