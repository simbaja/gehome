from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from gehomesdk.erd.values.fridge import FridgeIceBucketStatus, ErdFullNotFull

class FridgeIceBucketStatusConverter(ErdReadOnlyConverter[FridgeIceBucketStatus]):
    def erd_decode(self, value: str) -> FridgeIceBucketStatus:
        """Decode Ice bucket status"""
        if not value:
            n = 0
        else:
            n = erd_decode_int(value)

        is_present_ff = bool(n & 1)
        is_present_fz = bool(n & 2)
        state_full_ff = ErdFullNotFull.FULL if n & 4 else ErdFullNotFull.NOT_FULL
        state_full_fz = ErdFullNotFull.FULL if n & 8 else ErdFullNotFull.NOT_FULL

        if not is_present_ff:
            state_full_ff = ErdFullNotFull.NA
        if not is_present_fz:
            state_full_fz = ErdFullNotFull.NA

        if not (is_present_ff or is_present_ff):
            # No ice buckets at all
            total_status = ErdFullNotFull.NA
        elif (state_full_ff == ErdFullNotFull.NOT_FULL) or (state_full_fz == ErdFullNotFull.NOT_FULL):
            # At least one bucket is not full
            total_status = ErdFullNotFull.NOT_FULL
        else:
            total_status = ErdFullNotFull.FULL

        ice_status = FridgeIceBucketStatus(
            state_full_fridge=state_full_ff,
            state_full_freezer=state_full_fz,
            is_present_fridge=is_present_ff,
            is_present_freezer=is_present_fz,
            total_status=total_status,
        )
        return ice_status
