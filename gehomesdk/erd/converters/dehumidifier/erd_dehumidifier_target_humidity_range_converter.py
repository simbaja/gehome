from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.dehumidifier import DehumidifierTargetRange

class DehumidifierTargetRangeConverter(ErdReadOnlyConverter[DehumidifierTargetRange]):
    def erd_decode(self, value: str) -> DehumidifierTargetRange:
        return DehumidifierTargetRange(
            min_humidity=erd_decode_int(value[0:2]),
            max_humidity=erd_decode_int(value[2:4]),
        )

