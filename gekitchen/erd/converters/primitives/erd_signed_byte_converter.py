from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter

def erd_decode_signed_byte(value: any) -> int:
    """
    Convert a hex byte to a signed int.  Copied from GE's hextodec method.
    """
    val = int(value, 16)
    if val > 128:
        return val - 256
    return val
def erd_encode_signed_byte(value: int) -> str:
    """
    Convert a hex byte to a signed int.  Copied from GE's hextodec method.
    """
    value = int(value)
    if value < 0:
        value = value + 256
    return value.to_bytes(1, "big").hex()

class ErdSignedByteConverter(ErdReadWriteConverter[int]):
    def erd_decode(self, value: str) -> int:
        """
        Convert a hex byte to a signed int.  Copied from GE's hextodec method.
        """
        return erd_decode_signed_byte(value)
    def erd_encode(self, value: int) -> str:
        """
        Convert a hex byte to a signed int.  Copied from GE's hextodec method.
        """
        return erd_encode_signed_byte(value)

class ErdReadOnlySignedByteConverter(ErdReadOnlyConverter[int]):
    def erd_decode(self, value: str) -> int:
        """
        Convert a hex byte to a signed int.  Copied from GE's hextodec method.
        """
        return erd_decode_signed_byte(value)
