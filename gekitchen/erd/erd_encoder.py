import logging
from typing import Any

from ..exception import GeUnsupportedOperationError

from .erd_configuration import ErdConfigurationEntry, _configuration
from .erd_codes import ErdCode, ErdCodeType
from .converters import *

_LOGGER = logging.getLogger(__name__)

class ErdEncoder:
    # Create the converter registry for all known types
    def __init__(self) -> None:
        super().__init__()
        self._registry = dict((k.erd_code, k) for k in _configuration)

    def translate_code(self, erd_code: ErdCodeType) -> ErdCodeType:
        """
        Try to resolve an ERD codes from string to ErdCode if possible.  If an ErdCode
        object is passed in, it will be returned.
        :param erd_code: ErdCode or str
        :return: Either an ErdCode object matching the `erd_code` string, or, if resolution fails,
        the `erd_code` string itself.
        """
        if isinstance(erd_code, ErdCode):
            return erd_code

        try:
            return ErdCode[erd_code]
        except KeyError:
            pass

        try:
            return ErdCode(erd_code.lower())
        except ValueError:
            return erd_code

    def decode_value(self, erd_code: ErdCodeType, erd_value: str) -> Any:
        """
        Decode and ERD Code raw value into something useful.  If the erd_code is a string that
        cannot be resolved to a known ERD Code, the value will be treated as raw byte string.
        Unregistered ERD Codes will be translated as ints.

        :param erd_code: ErdCode or str, the ERD Code the value of which we want to decode
        :param erd_value: The raw ERD code value, usually a hex string without leading "0x"
        :return: The decoded value.
        """
        if erd_value == '':
            return None

        erd_code = self.translate_code(erd_code)

        if isinstance(erd_code, str):
            return erd_decode_bytes(erd_value)

        try:
            return self._registry[erd_code].erd_decode(erd_value)
        except KeyError:
            return erd_decode_int(erd_value)

    def encode_value(self, erd_code: ErdCodeType, value: Any) -> str:
        """
        Encode an ERD Code value as a hex string.
        Only ERD Codes registered with self.erd_encoders will processed.  Otherwise an error will be returned.

        :param erd_code: ErdCode or str, the ERD Code the value of which we want to decode
        :param value: The value to re-encode
        :return: The encoded value as a hex string
        """
        if value is None:
            return ''

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].erd_encode(value)
        except KeyError:
            _LOGGER.error(f'Attempt to encode unregistered ERD code {erd_code}')
            raise

    def boolify_value(self, erd_code: ErdCodeType) -> bool:
        """
        Boolifies a code if possible
        """

        erd_code = self.translate_code(erd_code)

        if not self.can_boolify(erd_code):
            raise GeUnsupportedOperationError

        try:
            value = self.decode_value(erd_code)
            if isinstance(value, bool):
                return value
            else:
                value.boolify()
        except:
            raise GeUnsupportedOperationError

    def can_decode(self, erd_code: ErdCodeType) -> bool:
        """ 
        Indicates whether an ERD Code can be decoded. If the code
        is not registered, defaults to true
        """

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].can_decode
        except KeyError:
            return True

    def can_encode(self, erd_code: ErdCodeType) -> bool:
        """ 
        Indicates whether an ERD Code can be encoded. If the code
        is not registered, defaults to false
        """

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].can_encode
        except KeyError:
            return False

    def can_boolify(self, erd_code: ErdCodeType) -> bool:
        """
        Indicates whether an ERD Code can boolified.  If the code
        is not registered, defaults to false
        """

        erd_code = self.translate_code(erd_code)

        try:
            return self._registry[erd_code].can_boolify
        except KeyError:
            return False
        