import logging

from ..abstract import ErdReadOnlyConverter
from ...erd_codes import ErdCodeType
from ...values.common import ErdPersonality

_LOGGER = logging.getLogger(__name__)

class ErdPersonalityConverter(ErdReadOnlyConverter[ErdPersonality]):
    def __init__(self, erd_code: ErdCodeType = "Unknown"):
        super().__init__(erd_code)
        self._unknowns = set()

    def erd_decode(self, value) -> ErdPersonality:
        try:
            return ErdPersonality(value)
        except Exception:
            if not self._have_already_seen_unknown_appliance(value):
                _LOGGER.debug("Unknown personality found: %s, using default", value)
            return ErdPersonality.UNKNOWN

    def _have_already_seen_unknown_appliance(self, value):
        is_duplicate = value in self._unknowns
        if not is_duplicate:
            self._unknowns.add(value)
        return is_duplicate
