"""Values captured from a Cafe Affetto (C7CEBBS4RW3)"""
from gehomesdk import ErdCode
from gehomesdk.erd.erd_configuration import _configuration
from gehomesdk.erd.converters.espresso_maker import (
    ErdEspressoBrewParametersConverter,
    ErdEspressoDrinkParametersConverter,
    ErdEspressoEnumConverter,
    ErdEspressoLittleEndianU32Converter,
    ErdEspressoRangeConverter,
    ErdEspressoSupportedBrewTypesConverter,
    ErdEspressoSupportedFeaturesConverter,
)
from gehomesdk.erd.values.espresso_maker import (
    ErdEspressoBrewParameters,
    ErdEspressoBrewType,
    ErdEspressoDrinkParameters,
    ErdEspressoWaterHardness,
)


def test_current_brew_parameters() -> None:
    decoded = ErdEspressoBrewParametersConverter().erd_decode("0398012C0037")

    assert decoded.temperature == 92.0
    assert decoded.brew_type == ErdEspressoBrewType.AMERICANO
    assert decoded.volume == 44
    assert decoded.grind_time == 5.5


def test_brew_parameters_round_trip() -> None:
    converter = ErdEspressoBrewParametersConverter()
    value = ErdEspressoBrewParameters(92.0, ErdEspressoBrewType.AMERICANO, 44, 5.5)

    assert converter.erd_encode(value).upper() == "0398012C0037"


def test_drink_parameters_with_limits() -> None:
    decoded = ErdEspressoDrinkParametersConverter().erd_decode("039800374A0003840398002D003C1E4A")

    assert decoded.temperature == 92.0
    assert decoded.grind_time == 5.5
    assert decoded.volume == 74
    assert decoded.my_cup_button is False
    assert (decoded.min_temperature, decoded.max_temperature) == (90.0, 92.0)
    assert (decoded.min_grind_time, decoded.max_grind_time) == (4.5, 6.0)
    assert (decoded.min_volume, decoded.max_volume) == (30, 74)


def test_hot_water_has_no_grind_range() -> None:
    decoded = ErdEspressoDrinkParametersConverter().erd_decode("02BC00009400025803200000000076ED")

    assert decoded.temperature == 70.0
    assert decoded.volume == 148
    assert (decoded.min_grind_time, decoded.max_grind_time) == (0, 0)
    assert (decoded.min_volume, decoded.max_volume) == (118, 237)


def test_drink_parameters_encode_is_request_layout() -> None:
    value = ErdEspressoDrinkParameters(temperature=91.0, grind_time=5.0, volume=40)

    assert ErdEspressoDrinkParametersConverter().erd_encode(value).upper() == "038E00322800"


def test_ranges() -> None:
    standby = ErdEspressoRangeConverter(size=2).erd_decode("0A8C03840A8C")
    steam = ErdEspressoRangeConverter(size=2).erd_decode("005A001E0078")
    rinse = ErdEspressoRangeConverter(size=1).erd_decode("000000")

    assert (standby.value, standby.min, standby.max) == (2700, 900, 2700)
    assert (steam.value, steam.min, steam.max) == (90, 30, 120)
    assert (rinse.value, rinse.min, rinse.max) == (0, 0, 0)


def test_supported_brew_types() -> None:
    decoded = ErdEspressoSupportedBrewTypesConverter().erd_decode("FF030000")

    assert decoded.brew_types == frozenset(t for t in ErdEspressoBrewType if t != ErdEspressoBrewType.UNKNOWN)


def test_supported_features() -> None:
    decoded = ErdEspressoSupportedFeaturesConverter().erd_decode("05000000")

    assert (decoded.my_cup, decoded.my_brew, decoded.steam) == (True, False, True)


def test_lifetime_coffee_ground_is_little_endian() -> None:
    assert ErdEspressoLittleEndianU32Converter().erd_decode("741E0000") == 7796


def test_water_hardness() -> None:
    converter = ErdEspressoEnumConverter(ErdEspressoWaterHardness)

    assert converter.erd_decode("00") == ErdEspressoWaterHardness.VERY_SOFT
    assert converter.erd_decode("09") == ErdEspressoWaterHardness.UNKNOWN
    assert converter.erd_encode(ErdEspressoWaterHardness.HARD) == "02"


def test_all_espresso_codes_are_configured() -> None:
    configured = {entry.erd_code for entry in _configuration}
    for code in ErdCode:
        if code.name.startswith("ESPRESSO_"):
            assert code in configured, code
