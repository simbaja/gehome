import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdWashStainRemovalGuideOption

_LOGGER = logging.getLogger(__name__)

class LaundryWashStainRemovalGuideOptionConverter(ErdReadOnlyConverter[ErdWashStainRemovalGuideOption]):
    def erd_decode(self, value: str) -> ErdWashStainRemovalGuideOption:
        try:
            return ErdWashStainRemovalGuideOption(erd_decode_int(value))
        except (KeyError, ValueError):
            return ErdWashStainRemovalGuideOption.OFF
