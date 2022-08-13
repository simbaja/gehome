
import logging

from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.erd_codes import ErdCodeType
from gehomesdk.erd.values import ErdApplianceType

_LOGGER = logging.getLogger(__name__)
class ErdApplianceTypeConverter(ErdReadOnlyConverter[ErdApplianceType]):
    def __init__(self, erd_code: ErdCodeType = "Unknown"):
        super().__init__(erd_code)
        self._unknowns = set()

    def erd_decode(self, value) -> ErdApplianceType:
        try:
            return ErdApplianceType(value)
        except ValueError:
            if not self._have_already_seen_unknown_appliance(value):
                _LOGGER.info(f"Unknown appliance type found, value = {value}")
            return ErdApplianceType.UNKNOWN

    def _have_already_seen_unknown_appliance(self, value):
        is_duplicate = value in self._unknowns
        if not is_duplicate:
            self._unknowns.add(value)
        return not is_duplicate
