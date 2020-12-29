from ..abstract import ErdReadWriteConverter, ErdReadOnlyConverter

def erd_decode_string(value: str) -> str:
    """
    Decode an string value sent as a hex encoded string.
    """
    raw_bytes = bytes.fromhex(value)
    raw_bytes = raw_bytes.rstrip(b'\x00')

    return raw_bytes.decode('ascii')
def erd_encode_string(value: str) -> str:
    """
    Encode an string value to a hex encoded string.
    """
    raw_bytes = value.encode('ascii')
    return bytes.hex(raw_bytes)

class ErdStringConverter(ErdReadWriteConverter[str]):
    def erd_decode(self, value: str) -> str:
        """
        Decode an string value sent as a hex encoded string.
        """
        return erd_decode_string(value)
    def erd_encode(self, value: str) -> str:
        """
        Encode an string value to a hex encoded string.
        """
        return erd_encode_string(value)

class ErdReadOnlyStringConverter(ErdReadOnlyConverter[str]):
    def erd_decode(self, value: str) -> str:
        """
        Decode an string value sent as a hex encoded string.
        """
        return erd_decode_string(value)
        