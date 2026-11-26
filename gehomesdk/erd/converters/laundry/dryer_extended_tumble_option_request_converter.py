import logging
from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.laundry import ErdDryerExtendedTumbleOptionRequest

_LOGGER = logging.getLogger(__name__)

class ErdDryerExtendedTumbleOptionRequestConverter(ErdReadWriteConverter[ErdDryerExtendedTumbleOptionRequest]):
    def erd_decode(self, value: str) -> ErdDryerExtendedTumbleOptionRequest:
        try:
            return ErdDryerExtendedTumbleOptionRequest(erd_decode_int(value))
        except (KeyError, ValueError):
            _LOGGER.debug("Dryer extended tumble option request unknown {value}, using default")
            return ErdDryerExtendedTumbleOptionRequest.REQUEST_PROCESSED

    def erd_encode(self, value: ErdDryerExtendedTumbleOptionRequest | bool | int) -> str:
        if isinstance(value, bool):
            enum_val = (
                ErdDryerExtendedTumbleOptionRequest.ENABLED
                if value
                else ErdDryerExtendedTumbleOptionRequest.DISABLED
            )
        else:
            enum_val = ErdDryerExtendedTumbleOptionRequest(value)
        return erd_encode_int(enum_val.value, 1)
