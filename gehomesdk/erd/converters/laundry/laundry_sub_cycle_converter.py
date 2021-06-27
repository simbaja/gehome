import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdLaundrySubCycle, LaundrySubCycle, LAUNDRY_SUB_CYCLE_MAP

_LOGGER = logging.getLogger(__name__)

class LaundrySubCycleConverter(ErdReadOnlyConverter[LaundrySubCycle]):
    def erd_decode(self, value: str) -> LaundrySubCycle:
        try:
            om = ErdLaundrySubCycle(erd_decode_int(value))
            return LAUNDRY_SUB_CYCLE_MAP[om].value
        except (KeyError, ValueError):
            return ErdLaundrySubCycle.CYCLE_NONE
