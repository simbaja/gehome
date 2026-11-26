import logging
from ..abstract import ErdReadOnlyConverter

from ...values import ErdBrand

_LOGGER = logging.getLogger(__name__)

class ErdBrandConverter(ErdReadOnlyConverter[ErdBrand]):
    def erd_decode(self, value: str) -> ErdBrand:
        try:
            return ErdBrand(value)
        except ValueError:
            _LOGGER.info("Unknown brand found, value = %s", value)
            return ErdBrand.UNKNOWN
