import logging
from typing import Union
from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values.laundry import ErdTumbleStatus

_LOGGER = logging.getLogger(__name__)

class TumbleStatusConverter(ErdReadWriteConverter[ErdTumbleStatus]):
    def erd_decode(self, value: str) -> ErdTumbleStatus:
        try:
            return ErdTumbleStatus(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdTumbleStatus.NOT_AVAILABLE

    def erd_encode(self, value: Union[ErdTumbleStatus, bool, int]) -> str:
        if isinstance(value, bool):
            enum_val = ErdTumbleStatus.ENABLE if value else ErdTumbleStatus.DISABLE
        else:
            enum_val = ErdTumbleStatus(value)
        return erd_encode_int(enum_val.value, 1)
