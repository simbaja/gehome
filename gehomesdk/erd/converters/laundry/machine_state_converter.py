import logging
from ..abstract import ErdReadOnlyConverter
from ..primitives import *
from ...values.laundry import ErdMachineState, MachineState, MACHINE_STATE_MAP

_LOGGER = logging.getLogger(__name__)

class MachineStateConverter(ErdReadOnlyConverter[MachineState]):
    def erd_decode(self, value: str) -> MachineState:
        try:
            om = ErdMachineState(erd_decode_int(value))
            return MACHINE_STATE_MAP[om]
        except (KeyError, ValueError):
            return MachineState.STATUS_OFF
