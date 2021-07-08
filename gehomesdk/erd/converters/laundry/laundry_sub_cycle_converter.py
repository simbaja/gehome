import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdLaundrySubCycle

_LOGGER = logging.getLogger(__name__)

class LaundrySubCycleConverter(ErdReadOnlyConverter[ErdLaundrySubCycle]):
    def erd_decode(self, value: str) -> ErdLaundrySubCycle:
        try:
            return ErdLaundrySubCycle(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdLaundrySubCycle.CYCLE_NONE
