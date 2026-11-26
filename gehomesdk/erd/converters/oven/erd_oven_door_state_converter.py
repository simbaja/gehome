from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.oven import ErdOvenDoorState


class ErdOvenDoorStateConverter(ErdReadOnlyConverter[ErdOvenDoorState]):
    def erd_decode(self, value: str) -> ErdOvenDoorState:
        try:
            return ErdOvenDoorState(erd_decode_int(value))
        except ValueError:
            return ErdOvenDoorState.UNKNOWN
