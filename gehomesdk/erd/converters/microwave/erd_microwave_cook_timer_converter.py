from datetime import timedelta
from typing import Optional

from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.advantium import ErdAdvantiumCookTimeMinMax

class ErdMicrowaveCookTimerConverter(ErdReadOnlyConverter[Optional[timedelta]]):
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes the cook time as a time span"""
        try:
            m = value[0:2]
            s = value[2:4]
            return timedelta(seconds=m * 60 + s)
        except:
            return None
