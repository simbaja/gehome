import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdDryerExtendedTumbleOptionRequest

_LOGGER = logging.getLogger(__name__)

class ErdDryerExtendedTumbleOptionRequestConverter(ErdReadOnlyConverter[ErdDryerExtendedTumbleOptionRequest]):
    def erd_decode(self, value: str) -> ErdDryerExtendedTumbleOptionRequest:
        try:
            return ErdDryerExtendedTumbleOptionRequest(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Dryer extended tumble option request unknown {value}, using default")
            return ErdDryerExtendedTumbleOptionRequest.REQUEST_PROCESSED
