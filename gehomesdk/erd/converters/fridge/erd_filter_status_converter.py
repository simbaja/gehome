from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import ErdFilterStatus

class ErdFilterStatusConverter(ErdReadOnlyConverter[ErdFilterStatus]):
    def erd_decode(self, value: str) -> ErdFilterStatus:
        """Decode water filter status.

        This appears to be 9 bytes, of which only the first two are obviously used. I suspect that the others
        relate to how much time remains on the filter.  Leaving as a TODO.
        """
        status_byte = value[:2]
        if status_byte == "00":
            status_byte = value[2:4]
        try:
            return ErdFilterStatus(status_byte)
        except ValueError:
            return ErdFilterStatus.NA
