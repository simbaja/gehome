from datetime import time, timedelta
from typing import Optional

from ..abstract import ErdReadWriteConverter
from ..primitives import *

class ErdMicrowaveCookTimerConverter(ErdReadWriteConverter[Optional[timedelta]]):
    def erd_decode(self, value: str) -> Optional[timedelta]:
        """ Decodes the cook time as a time span"""
        try:
            m = value[0:2]
            s = value[2:4]
            return timedelta(seconds=m * 60 + s)
        except:
            return None
    def erd_encode(self, value: Optional[timedelta]) -> str:
        try:
            minutes = (value.seconds % 3600) // 60 
            seconds = (value.seconds % 60)

            return erd_encode_int(minutes) + erd_encode_int(seconds)
        except:
            return "0000"    
