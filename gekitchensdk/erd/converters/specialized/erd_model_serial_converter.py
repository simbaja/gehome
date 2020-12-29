
from ..abstract import ErdReadOnlyConverter
from ..primitives import *

class ErdModelSerialConverter(ErdReadOnlyConverter[str]):
    def erd_decode(self, value) -> str:
        """
        Decode a serial/model number string value sent as a hex encoded string.

        TODO: I think the first byte is a checksum.  I need to confirm this so we can have an encoder as well.
        """
        raw_bytes = bytes.fromhex(value)
        raw_bytes = raw_bytes.rstrip(b'\x00')

        return raw_bytes[1:].decode('ascii')
