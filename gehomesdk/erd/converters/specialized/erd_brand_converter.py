import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from ...values import ErdBrand

_LOGGER = logging.getLogger(__name__)

class ErdBrandConverter(ErdReadOnlyConverter[ErdBrand]):
    def erd_decode(self, value: str) -> ErdBrand:
        try:
            return ErdBrand(value)
        except ValueError:
            _LOGGER.info(f"Unknown brand found, value = {value}")
            return ErdBrand.UNKNOWN
