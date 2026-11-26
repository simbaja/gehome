from datetime import timedelta
from ..abstract import ErdReadWriteConverter
from ..primitives import erd_encode_int

class ErdMicrowaveCookTimerConverter(ErdReadWriteConverter[timedelta | None]):
    def erd_decode(self, value: str) -> timedelta | None:
        """ Decodes the cook time as a time span"""
        try:
            m = int(value[0:2])
            s = int(value[2:4])
            return timedelta(seconds=m * 60 + s)
        except Exception:
            return None
    def erd_encode(self, value: timedelta | None) -> str:
        if value is None:
            return "0000"
        
        try:
            minutes = (value.seconds % 3600) // 60 
            seconds = (value.seconds % 60)

            return erd_encode_int(minutes) + erd_encode_int(seconds)
        except Exception:
            return "0000"    
