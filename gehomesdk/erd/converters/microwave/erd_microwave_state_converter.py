from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values import (
    ErdMicrowaveState, 
    ErdDoorStatus,
    ErdMicrowaveCookStatus,
    ErdMicrowaveCookMode
)

class ErdMicrowaveStateConverter(ErdReadOnlyConverter[ErdMicrowaveState]):
    def erd_decode(self, value: str) -> ErdMicrowaveState:
        try:
            try:
                status = ErdMicrowaveCookStatus(value[0:2])
            except Exception:
                status = ErdMicrowaveCookStatus.UNKNOWN
            mode = ErdMicrowaveCookMode(value[2:4])
            try:
                door = ErdDoorStatus(value[4:6])
            except Exception:
                door = ErdDoorStatus.NA
                
            pl = erd_decode_int(value[6:8])
            pl = max(min(pl, 10), 0)

            if len(value) >= 12:
                temp = int(value[8:12])
            else:
                temp = 0

            return ErdMicrowaveState(
                status,
                mode,
                door,
                pl,
                temp,
                value
            )
        except Exception:
            return ErdMicrowaveState(
                ErdMicrowaveCookStatus.UNKNOWN, 
                ErdMicrowaveCookMode.DASH, 
                ErdDoorStatus.NA,
                0,
                0,
                value)
