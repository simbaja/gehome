import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdRemoteStatus, RemoteStatus, REMOTE_STATUS_MAP

_LOGGER = logging.getLogger(__name__)

class RemoteStatusConverter(ErdReadOnlyConverter[RemoteStatus]):
    def erd_decode(self, value: str) -> RemoteStatus:
        try:
            om = ErdRemoteStatus(erd_decode_int(value))
            return REMOTE_STATUS_MAP[om].value
        except (KeyError, ValueError):
            return ErdRemoteStatus.NA
