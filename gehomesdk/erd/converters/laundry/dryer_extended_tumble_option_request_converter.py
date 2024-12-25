import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdDryerExtendedTumbleOptionRequest

_LOGGER = logging.getLogger(__name__)

class ErdDryerExtendedTumbleOptionRequestConverter(ErdReadOnlyConverter[ErdDryerExtendedTumbleOptionRequest]):
    def erd_decode(self, value: str) -> ErdDryerExtendedTumbleOptionRequest:
        try:
            return ErdDryerExtendedTumbleOptionRequest(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Dryer extended tumble option request unknown {value}, using default")
            return ErdDryerExtendedTumbleOptionRequest.REQUEST_PROCESSED
