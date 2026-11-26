from datetime import timedelta

from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_timespan

class ErdAdvantiumCookTimeRemainingConverter(ErdReadOnlyConverter[timedelta | None]):
    def erd_decode(self, value: str) -> timedelta | None:
        """ Decodes the cook time as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value[2:6], uom="seconds")
