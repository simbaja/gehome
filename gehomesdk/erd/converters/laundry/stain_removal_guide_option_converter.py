import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdWashStainRemovalGuideOption

_LOGGER = logging.getLogger(__name__)

class LaundryWashStainRemovalGuideOptionConverter(ErdReadOnlyConverter[ErdWashStainRemovalGuideOption]):
    def erd_decode(self, value: str) -> ErdWashStainRemovalGuideOption:
        try:
            return ErdWashStainRemovalGuideOption(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdWashStainRemovalGuideOption.OFF
