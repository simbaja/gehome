from ..abstract import ErdReadOnlyConverter
from ..primitives import *

class ErdModelSerialConverter(ErdReadOnlyConverter[str]):
    def erd_decode(self, value) -> str:
        """
        Decode a serial/model number string value sent as a hex encoded string.
        
        The first byte is a length field indicating the data length (including padding).
        We extract based on length, then strip any 0x00 or 0xFF padding bytes
        that some firmware versions incorrectly use.
        """
        raw_bytes = bytes.fromhex(value)

        if len(raw_bytes) < 2:
            return ""

        length = raw_bytes[0]

        data_end = min(1 + length, len(raw_bytes))
        data_bytes = raw_bytes[1:data_end]
        data_bytes = data_bytes.rstrip(b'\xff\x00')

        try:
            result = data_bytes.decode('ascii')
        except UnicodeDecodeError:
            return ""

        # Some firmware versions send PEM certificate data on this ERD code.
        # Those payloads contain control characters (e.g. \n); a valid model
        # or serial number is always printable ASCII.
        if not result.isprintable():
            return ""

        return result
