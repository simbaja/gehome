import logging
from datetime import timedelta

from ..abstract import ErdReadWriteConverter
from ..primitives import *
from ...values.toaster_oven import ErdToasterOvenCookMode, ErdToasterOvenSize, ToasterOvenCookSetting

_LOGGER = logging.getLogger(__name__)


class ToasterOvenCookSettingConverter(ErdReadWriteConverter[ToasterOvenCookSetting]):
    """
    Decodes/encodes the toaster oven cook setting ERDs (current: 0x9207,
    requested: 0x9208). Not all cook modes use all fields; unused fields are
    zero. The raw 12-byte payload packs, in order:
      - shade (1 byte)
      - size (1 byte, enum: 0=Small, 1=Medium, 2=Large)
      - temperature (2 bytes, big endian, degrees Fahrenheit)
      - cook time (4 bytes, big endian, seconds)
      - count (1 byte)
      - cook mode (1 byte, enum)
      - preferences (1 byte)
      - padding (1 byte, always zero)
    """
    def erd_decode(self, value: str) -> ToasterOvenCookSetting:
        try:
            shade = erd_decode_int(value[0:2])
            size_code = erd_decode_int(value[2:4])
            temperature = erd_decode_int(value[4:8])
            cook_time = timedelta(seconds=erd_decode_int(value[8:16]))
            item_count = erd_decode_int(value[16:18])
            cook_mode = ErdToasterOvenCookMode(erd_decode_int(value[18:20]))
            preferences = erd_decode_int(value[20:22])

            try:
                size = ErdToasterOvenSize(size_code)
            except ValueError:
                size = None

            return ToasterOvenCookSetting(
                cook_mode=cook_mode,
                temperature=temperature,
                cook_time=cook_time,
                shade=shade,
                size=size,
                item_count=item_count,
                preferences=preferences,
                raw_string=value,
            )
        except (ValueError, IndexError):
            _LOGGER.warning(f"Could not decode toaster oven cook setting, raw value {value}")
            return ToasterOvenCookSetting(raw_string=value)

    def erd_encode(self, value: ToasterOvenCookSetting) -> str:
        cook_mode_code = value.cook_mode.value if value.cook_mode is not None else 0
        size_code = value.size.value if value.size is not None else 0

        return (
            erd_encode_int(value.shade, 1) +
            erd_encode_int(size_code, 1) +
            erd_encode_int(value.temperature, 2) +
            erd_encode_int(int(value.cook_time.total_seconds()), 4) +
            erd_encode_int(value.item_count, 1) +
            erd_encode_int(cook_mode_code, 1) +
            erd_encode_int(value.preferences, 1) +
            erd_encode_int(0, 1)
        )
