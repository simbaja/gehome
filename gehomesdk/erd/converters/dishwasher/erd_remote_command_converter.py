from ..abstract import ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.dishwasher import ErdRemoteCommand

class ErdRemoteCommandConverter(ErdReadWriteConverter[ErdRemoteCommand]):
    def erd_decode(self, value: str) -> ErdRemoteCommand:
        try:
            return ErdRemoteCommand(erd_decode_int(value))
        except Exception:
            return ErdRemoteCommand.UNKNOWN

    def erd_encode(self, value: ErdRemoteCommand) -> str:
        return erd_encode_int(value.value, length = 1)