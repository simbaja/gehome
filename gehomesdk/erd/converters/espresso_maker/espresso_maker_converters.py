import logging
import struct
from typing import Type

from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...erd_codes import ErdCodeType
from ...values.espresso_maker import *

_LOGGER = logging.getLogger(__name__)

def _clean(value: str) -> str:
    return value.replace(" ", "")

def _u8(value: str, offset: int) -> int:
    return erd_decode_int(value[offset * 2:offset * 2 + 2])

def _u16(value: str, offset: int) -> int:
    return erd_decode_int(value[offset * 2:offset * 2 + 4])

def _tenths(raw: int) -> float:
    return raw / 10.0

def _from_tenths(value: float) -> int:
    return int(round(float(value) * 10))

class ErdEspressoBrewParametersConverter(ErdReadWriteConverter[ErdEspressoBrewParameters]):
    """temperature (C*10, u16), brew type (u8), volume (mL, u8), grind time (s*10, u16)"""
    def erd_decode(self, value: str) -> ErdEspressoBrewParameters:
        value = _clean(value)
        try:
            try:
                brew_type = ErdEspressoBrewType(_u8(value, 2))
            except ValueError:
                brew_type = ErdEspressoBrewType.UNKNOWN
            return ErdEspressoBrewParameters(
                temperature=_tenths(_u16(value, 0)),
                brew_type=brew_type,
                volume=_u8(value, 3),
                grind_time=_tenths(_u16(value, 4)),
                raw_value=value
            )
        except Exception:
            _LOGGER.exception("Could not decode espresso brew parameters, using default.")
            return ErdEspressoBrewParameters(raw_value=value)

    def erd_encode(self, value: ErdEspressoBrewParameters) -> str:
        return (
            erd_encode_int(_from_tenths(value.temperature), 2) +
            erd_encode_int(value.brew_type.value, 1) +
            erd_encode_int(value.volume, 1) +
            erd_encode_int(_from_tenths(value.grind_time), 2)
        )

class ErdEspressoDrinkParametersConverter(ErdReadWriteConverter[ErdEspressoDrinkParameters]):
    """
    Current values are 16 bytes: temperature (C*10, u16), grind time (s*10, u16), volume (mL, u8),
    button type (u8), then min/max temperature, min/max grind time, min/max volume.
    Requested values are the first 6 bytes, with the button type byte as padding.
    """
    def erd_decode(self, value: str) -> ErdEspressoDrinkParameters:
        value = _clean(value)
        try:
            has_limits = len(value) >= 32
            return ErdEspressoDrinkParameters(
                temperature=_tenths(_u16(value, 0)),
                grind_time=_tenths(_u16(value, 2)),
                volume=_u8(value, 4),
                my_cup_button=_u8(value, 5) == 1,
                min_temperature=_tenths(_u16(value, 6)) if has_limits else 0,
                max_temperature=_tenths(_u16(value, 8)) if has_limits else 0,
                min_grind_time=_tenths(_u16(value, 10)) if has_limits else 0,
                max_grind_time=_tenths(_u16(value, 12)) if has_limits else 0,
                min_volume=_u8(value, 14) if has_limits else 0,
                max_volume=_u8(value, 15) if has_limits else 0,
                raw_value=value
            )
        except Exception:
            _LOGGER.exception("Could not decode espresso drink parameters, using default.")
            return ErdEspressoDrinkParameters(raw_value=value)

    def erd_encode(self, value: ErdEspressoDrinkParameters) -> str:
        return (
            erd_encode_int(_from_tenths(value.temperature), 2) +
            erd_encode_int(_from_tenths(value.grind_time), 2) +
            erd_encode_int(value.volume, 1) +
            "00"
        )

class ErdEspressoRangeConverter(ErdReadOnlyConverter[ErdEspressoRange]):
    """value, min, max; each field is `size` bytes"""
    def __init__(self, erd_code: ErdCodeType = "Unknown", size: int = 2):
        super().__init__(erd_code)
        self.size = size

    def erd_decode(self, value: str) -> ErdEspressoRange:
        value = _clean(value)
        w = self.size * 2
        try:
            return ErdEspressoRange(
                value=erd_decode_int(value[0:w]),
                min=erd_decode_int(value[w:2 * w]),
                max=erd_decode_int(value[2 * w:3 * w]),
                raw_value=value
            )
        except Exception:
            _LOGGER.exception("Could not decode espresso range, using default.")
            return ErdEspressoRange(raw_value=value)

class ErdEspressoSupportedBrewTypesConverter(ErdReadOnlyConverter[ErdEspressoSupportedBrewTypes]):
    # bit positions in the big-endian u32
    _BITS = {
        24: ErdEspressoBrewType.ESPRESSO,
        25: ErdEspressoBrewType.AMERICANO,
        26: ErdEspressoBrewType.LUNGO,
        27: ErdEspressoBrewType.HOT_WATER,
        28: ErdEspressoBrewType.STEAM,
        29: ErdEspressoBrewType.RISTRETTO,
        30: ErdEspressoBrewType.DOPPIO,
        31: ErdEspressoBrewType.TRIPLE_SHOT,
        16: ErdEspressoBrewType.RED_EYE,
        17: ErdEspressoBrewType.MY_CUP,
    }

    def erd_decode(self, value: str) -> ErdEspressoSupportedBrewTypes:
        value = _clean(value)
        try:
            bits = int(value, 16)
            return ErdEspressoSupportedBrewTypes(
                frozenset(t for b, t in self._BITS.items() if bits & (1 << b)),
                value
            )
        except Exception:
            _LOGGER.exception("Could not decode espresso supported brew types, using default.")
            return ErdEspressoSupportedBrewTypes(raw_value=value)

class ErdEspressoSupportedFeaturesConverter(ErdReadOnlyConverter[ErdEspressoSupportedFeatures]):
    def erd_decode(self, value: str) -> ErdEspressoSupportedFeatures:
        value = _clean(value)
        try:
            bits = int(value, 16)
            return ErdEspressoSupportedFeatures(
                my_cup=bool(bits & (1 << 24)),
                my_brew=bool(bits & (1 << 25)),
                steam=bool(bits & (1 << 26)),
                raw_value=value
            )
        except Exception:
            _LOGGER.exception("Could not decode espresso supported features, using default.")
            return ErdEspressoSupportedFeatures(raw_value=value)

class ErdEspressoLittleEndianU32Converter(ErdReadOnlyConverter[int]):
    """Some espresso counters (e.g. lifetime coffee ground) are reported little-endian"""
    def erd_decode(self, value: str) -> int:
        return struct.unpack("<I", bytes.fromhex(_clean(value)))[0]

class ErdEspressoEnumConverter(ErdReadWriteConverter):
    """Single byte enum; unknown values decode to the enum's UNKNOWN member"""
    def __init__(self, enum_type: Type, erd_code: ErdCodeType = "Unknown"):
        super().__init__(erd_code)
        self.enum_type = enum_type

    def erd_decode(self, value: str):
        try:
            return self.enum_type(erd_decode_int(_clean(value)))
        except ValueError:
            return self.enum_type.UNKNOWN

    def erd_encode(self, value) -> str:
        return erd_encode_int(value.value, 1)
