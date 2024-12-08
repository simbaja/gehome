import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdRemoteStartExtendedTumble

_LOGGER = logging.getLogger(__name__)

class ErdRemoteStartExtendedTumbleConverter(ErdReadOnlyConverter[ErdRemoteStartExtendedTumble]):
    def erd_decode(self, value: str) -> ErdRemoteStartExtendedTumble:
        try:
            return ErdRemoteStartExtendedTumble(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Remote start extended tumble unknown {value}, using default")
            return ErdRemoteStartExtendedTumble.REQUEST_PROCESSED
