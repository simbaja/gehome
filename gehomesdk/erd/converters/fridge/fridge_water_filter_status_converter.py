from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.fridge import ErdFilterStatus, FridgeWaterFilterStatus

class FridgeWaterFilterStatusConverter(ErdReadOnlyConverter[FridgeWaterFilterStatus]):
    def erd_decode(self, value: str) -> FridgeWaterFilterStatus:
        """Decode the 9 byte water filter status payload.

        Byte 0 is the filter status, byte 1 is the order status. When the filter
        status is "good" (00), the order status is used instead so that
        replace/expired states surface even though the filter itself hasn't
        faulted yet.
        """
        status_byte = value[:2]
        if status_byte == "00":
            status_byte = value[2:4]
        try:
            status = ErdFilterStatus(status_byte)
        except ValueError:
            status = ErdFilterStatus.NA

        return FridgeWaterFilterStatus(
            status=status,
            percent_remaining=erd_decode_int(value[4:6]),
            days_remaining=erd_decode_int(value[6:10]),
            days_since_expired=erd_decode_int(value[10:14]),
            dispenses_since_expired=erd_decode_int(value[14:18]),
        )
