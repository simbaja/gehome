import logging

from gehomesdk.erd.converters.abstract import ErdReadOnlyConverter
from gehomesdk.erd.converters.primitives import *
from gehomesdk.erd.values.laundry import ErdMachineState, MachineState, MACHINE_STATE_MAP

_LOGGER = logging.getLogger(__name__)

class MachineStateConverter(ErdReadOnlyConverter[MachineState]):
    def erd_decode(self, value: str) -> MachineState:
        try:
            om = ErdMachineState(erd_decode_int(value))
            return MACHINE_STATE_MAP[om].value
        except (KeyError, ValueError):
            return MachineState.STATUS_OFF
