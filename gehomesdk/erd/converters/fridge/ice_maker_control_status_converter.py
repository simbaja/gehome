from ..abstract import ErdReadWriteConverter
from ..primitives import *
from gehomesdk.erd.values.common import ErdOnOff
from gehomesdk.erd.values.fridge import IceMakerControlStatus

class IceMakerControlStatusConverter(ErdReadWriteConverter[IceMakerControlStatus]):
    def erd_decode(self, value: str) -> IceMakerControlStatus:
        def parse_status(val: str) -> ErdOnOff:
            try:
                return ErdOnOff(val)
            except ValueError:
                return ErdOnOff.NA

        status_fz = parse_status(value[:2])
        status_ff = parse_status(value[2:])

        return IceMakerControlStatus(status_fridge=status_ff, status_freezer=status_fz)
    def erd_encode(self, value: IceMakerControlStatus):
        return value.status_freezer.value + value.status_fridge.value
