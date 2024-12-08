import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdDownloadedCycleRequest

_LOGGER = logging.getLogger(__name__)

class ErdDownloadedCycleRequestConverter(ErdReadOnlyConverter[ErdDownloadedCycleRequest]):
    def erd_decode(self, value: str) -> ErdDownloadedCycleRequest:
        try:
            return ErdDownloadedCycleRequest(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdDownloadedCycleRequest.OFF
