import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdTumbleStatus, TumbleStatus, TUMBLE_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class TumbleStatusConverter(ErdReadOnlyConverter[TumbleStatus]):
    def erd_decode(self, value: str) -> TumbleStatus:
        try:
            om = ErdTumbleStatus(erd_decode_int(value))
            return TUMBLE_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdTumbleStatus.NOT_AVAILABLE
