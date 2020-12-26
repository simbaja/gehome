from typing import NamedTuple
from ..common import ErdOnOff

class IceMakerControlStatus(NamedTuple):
    status_fridge: ErdOnOff
    status_freezer: ErdOnOff
