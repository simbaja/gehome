import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdEcoDryStatus, EcoDryStatus, ECODRY_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class EcoDryStatusConverter(ErdReadOnlyConverter[EcoDryStatus]):
    def erd_decode(self, value: str) -> EcoDryStatus:
        try:
            om = ErdEcoDryStatus(erd_decode_int(value))
            return ECODRY_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return EcoDryStatus.STATUS_UNKNOWN
