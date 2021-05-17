
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values import ErdApplianceType

class ErdApplianceTypeConverter(ErdReadOnlyConverter[ErdApplianceType]):
    def erd_decode(self, value) -> ErdApplianceType:
        try:
            return ErdApplianceType(value)
        except ValueError:
            return ErdApplianceType.UNKNOWN
