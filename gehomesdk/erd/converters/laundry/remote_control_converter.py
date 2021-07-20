import logging

from gehomesdk.erd.converters.abstract import ErdReadWriteConverter
from gehomesdk.erd.converters.primitives import *

_LOGGER = logging.getLogger(__name__)

class LaundryRemotePowerControlConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        return erd_decode_int(value)

    def erd_encode(self, value: any) -> str:
        return erd_encode_int(value, 1)

class LaundryRemoteDelayControlConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        return erd_decode_int(value)

    def erd_encode(self, value: any) -> str:
        return erd_encode_int(value, 2)
