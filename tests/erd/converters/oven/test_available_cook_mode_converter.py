from gehomesdk.erd.converters.oven.erd_available_cook_mode_converter import (
    ErdAvailableCookModeConverter,
)
from gehomesdk.erd.values.oven import ErdOvenCookMode


def test_available_cook_mode_converter_decodes_warm() -> None:
    converter = ErdAvailableCookModeConverter()

    # GE "Warm No Option" is bit 15 of ERD 0x510b/0x520b (byte 8, mask 0x80)
    assert converter.erd_decode("00000000000000008000") == {ErdOvenCookMode.WARM_NOOPTION}


def test_available_cook_mode_converter_decodes_snrm128408q() -> None:
    converter = ErdAvailableCookModeConverter()

    # Reported by a GE SNRM128408Q upper oven (bake, broil, proof, warm, clean)
    decoded = converter.erd_decode("0000000E00000000BC8B")

    assert decoded == {ErdOvenCookMode.BAKE_NOOPTION, ErdOvenCookMode.WARM_NOOPTION}


def test_available_cook_mode_converter_ignores_proof_and_broil_bits() -> None:
    converter = ErdAvailableCookModeConverter()

    # Proof (bit 13) and Broil Low/High (bits 11/12) are advertised but not decoded
    assert converter.erd_decode("00000000000000003800") == set()
