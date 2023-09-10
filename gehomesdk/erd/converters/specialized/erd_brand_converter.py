from ..abstract import ErdReadWriteConverter
from ..primitives import *

from gehomesdk.erd.values import ErdBrand

class ErdBrandConverter(ErdReadWriteConverter[ErdBrand]):
    def erd_decode(self, value: str) -> ErdBrand:
        try:
            return ErdBrand(value)
        except ValueError:
            return ErdBrand.UNKNOWN