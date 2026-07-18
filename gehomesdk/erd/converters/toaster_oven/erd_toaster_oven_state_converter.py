from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.toaster_oven import ErdToasterOvenState


class ErdToasterOvenStateConverter(ErdReadOnlyConverter[ErdToasterOvenState]):
    def erd_decode(self, value: str) -> ErdToasterOvenState:
        """Decode the toaster oven's current state (a single byte enum)."""
        try:
            return ErdToasterOvenState(erd_decode_int(value))
        except ValueError:
            return ErdToasterOvenState.UNKNOWN
