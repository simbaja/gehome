import struct
from typing import Any
from ..abstract import ErdReadWriteConverter, ErdReadOnlyConverter
from ...erd_codes import ErdCodeType

def erd_decode_int(value: str, multibyte_endian: bool = False) -> int:
    """Decode an integer value sent as a hex encoded string."""
    value_length = len(value)
    if ((not multibyte_endian) or (value_length <= 2)):
        return int(value, 16)
    elif (value_length == 4):
        return struct.unpack("<H", bytes.fromhex(value))[0]
    elif (value_length == 8):
        return struct.unpack(">I", bytes.fromhex(value))[0]
    elif (value_length == 16):
        return struct.unpack(">Q", bytes.fromhex(value))[0]
    else:
        return -1

def erd_encode_int(value: Any, length: int = 2) -> str:
    """Encode an integer value as a hex string."""
    iv = int(value)
    return iv.to_bytes(length, 'big').hex()

class ErdIntConverter(ErdReadWriteConverter[int]):
    def __init__(self, erd_code: ErdCodeType = "Unknown", length: int = 2):
        super().__init__(erd_code)
        self.length = length
    def erd_decode(self, value: str) -> int:
        """Decode an integer value sent as a hex encoded string."""
        return erd_decode_int(value)
    def erd_encode(self, value) -> str:
        """Encode an integer value as a hex string."""
        return erd_encode_int(value, self.length)

class ErdReadOnlyIntConverter(ErdReadOnlyConverter[int]):
    def erd_decode(self, value: str) -> int:
        """Decode an integer value sent as a hex encoded string."""
        return erd_decode_int(value, False)

class ErdIntMultibyteConverter(ErdReadWriteConverter[int]):
    def __init__(self, erd_code: ErdCodeType = "Unknown", length: int = 2):
        super().__init__(erd_code)
        self.length = length
    def erd_decode(self, value: str) -> int:
        """Decode an integer value sent as a hex encoded string."""
        return erd_decode_int(value, True)
    def erd_encode(self, value) -> str:
        """Encode an integer value as a hex string."""
        return erd_encode_int(value, self.length)

class ErdReadOnlyIntMultibyteConverter(ErdReadOnlyConverter[int]):
    def erd_decode(self, value: str) -> int:
        """Decode an integer value sent as a hex encoded string."""
        return erd_decode_int(value, True)
