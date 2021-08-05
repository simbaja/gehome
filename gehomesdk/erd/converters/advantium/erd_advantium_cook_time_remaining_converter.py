from datetime import timedelta
from typing import Optional

from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumCookTimeMinMax

class ErdAdvantiumCookTimeRemainingConverter(ErdReadOnlyConverter[Optional[timedelta]]):
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes the cook time as a time span, 65535 is treated as None. """
        return erd_decode_timespan(value[2:6], uom="seconds")
