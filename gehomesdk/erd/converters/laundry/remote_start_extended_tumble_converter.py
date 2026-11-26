import logging
from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.laundry import ErdRemoteStartExtendedTumble

_LOGGER = logging.getLogger(__name__)

class ErdRemoteStartExtendedTumbleConverter(ErdReadWriteConverter[ErdRemoteStartExtendedTumble]):
    def erd_decode(self, value: str) -> ErdRemoteStartExtendedTumble:
        try:
            return ErdRemoteStartExtendedTumble(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Remote start extended tumble unknown {value}, using default")
            return ErdRemoteStartExtendedTumble.REQUEST_PROCESSED

    def erd_encode(self, value: ErdRemoteStartExtendedTumble | bool | int) -> str:
        if isinstance(value, bool):
            enum_val = (
                ErdRemoteStartExtendedTumble.START_EXTENDED_TUMBLE
                if value
                else ErdRemoteStartExtendedTumble.REQUEST_PROCESSED
            )
        else:
            enum_val = ErdRemoteStartExtendedTumble(value)
        return erd_encode_int(enum_val.value, 1)
