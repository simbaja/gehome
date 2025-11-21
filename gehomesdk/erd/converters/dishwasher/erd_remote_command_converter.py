from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values.dishwasher import *

class ErdRemoteCommandConverter(ErdReadWriteConverter[ErdRemoteCommand]):
    def erd_decode(self, value: str) -> ErdRemoteCommand:
        try:
            return ErdRemoteCommand(erd_decode_int(value))
        except:
            return ErdRemoteCommand.UNKNOWN

    def erd_encode(self, value: ErdRemoteCommand) -> str:
        return erd_encode_int(value.value, length = 1)