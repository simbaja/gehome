from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.common import ErdDsmPowerUsage


class ErdDsmPowerUsageConverter(ErdReadOnlyConverter[ErdDsmPowerUsage]):
    def erd_decode(self, value: str) -> ErdDsmPowerUsage:
        # Byte layout (from appliance API spec, ERD 0xd005):
        #   [0+2]  u16  Instantaneous Power (W)
        #   [2+4]  u32  Watt Seconds Since Clear
        #   [6+2]  u16  Seconds Since Cleared
        #   [8+1]  u8   Referenced To Line
        #   [9+2]  u16  Water Usage
        # Each byte is 2 hex chars, so offsets in hex string are 2×.
        return ErdDsmPowerUsage(
            instantaneous_power_w=erd_decode_int(value[0:4]),
            watt_seconds_since_clear=erd_decode_int(value[4:12]),
            seconds_since_cleared=erd_decode_int(value[12:16]),
            referenced_to_line=erd_decode_int(value[16:18]),
            water_usage=erd_decode_int(value[18:22]),
        )
