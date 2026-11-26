from ..abstract import ErdReadWriteConverter


class ErdCcmGrinderSettingConverter(ErdReadWriteConverter[bool | None]):
    """Converter for Cafe Speciality Grind & Brew grinder switch (ERD 0x9053).

    Raw byte polarity is inverted relative to standard bools:
      0x00 = Grind On (True)
      0x01 = Grind Off (False)
      0xFF = Unavailable (None)
    """

    def erd_decode(self, value: str) -> bool | None:
        if value.upper() == "FF":
            return None
        return int(value, 16) == 0

    def erd_encode(self, value: bool | None) -> str:
        if value is None:
            return "FF"
        return "00" if value else "01"
