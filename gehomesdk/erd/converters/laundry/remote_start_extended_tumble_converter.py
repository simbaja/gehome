import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdRemoteStartExtendedTumble

_LOGGER = logging.getLogger(__name__)

class ErdRemoteStartExtendedTumbleConverter(ErdReadOnlyConverter[ErdRemoteStartExtendedTumble]):
    def erd_decode(self, value: str) -> ErdRemoteStartExtendedTumble:
        try:
            return ErdRemoteStartExtendedTumble(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Remote start extended tumble unknown {value}, using default")
            return ErdRemoteStartExtendedTumble.REQUEST_PROCESSED
