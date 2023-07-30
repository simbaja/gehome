from ..abstract import ErdReadWriteConverter, ErdReadOnlyConverter

def erd_decode_bytes(value: any) -> bytes:
    """Decode a raw bytes ERD value sent as a hex encoded string."""
    return bytes.fromhex(value)
def erd_encode_bytes(value: bytes) -> str:
    """Encode a raw bytes ERD value."""
    return value.hex()

class ErdBytesConverter(ErdReadWriteConverter[bytes]):
    def erd_decode(self, value: str) -> bytes:
        """Decode a raw bytes ERD value sent as a hex encoded string."""
        return erd_decode_bytes(value)
    def erd_encode(self, value: bytes) -> str:
        """Encode a raw bytes ERD value."""
        return erd_encode_bytes(value)

class ErdReadOnlyBytesConverter(ErdReadOnlyConverter[bytes]):
    def erd_decode(self, value: str) -> bytes:
        """Decode a raw bytes ERD value sent as a hex encoded string."""
        return erd_decode_bytes(value)
