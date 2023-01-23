import logging
from typing import Any

from ..exception import GeUnsupportedOperationError

from .erd_configuration import ErdConfigurationEntry, _configuration
from .erd_codes import ErdCode, ErdCodeType
from .erd_code_class import ErdCodeClass
from .erd_data_type import ErdDataType
from .converters import *

_LOGGER = logging.getLogger(__name__)

class ErdEncoder:
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
        Unregistered ERD Codes will be translated as a byte string.

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
            return erd_decode_bytes(erd_value)
        except ValueError:
            _LOGGER.error(f'Got ValueError {erd_code} - {erd_value}')
            return erd_decode_bytes(erd_value)
            
    def get_code_class(self, erd_code: ErdCodeType) -> ErdCodeClass:
        """
        Gets the code class for a given ErdCode.  Returns GENERAL if not
        available.
        """
        erd_code = self.translate_code(erd_code)
        if isinstance(erd_code, str):
            return ErdCodeClass.GENERAL
        
        try:
            return self._registry[erd_code].code_class
        except KeyError:
            return ErdCodeClass.GENERAL


    def get_data_type(self, erd_code: ErdCodeType) -> ErdDataType:
        """
        Gets the data typefor a given ErdCode.  Returns STRING if not
        available.
        """
        erd_code = self.translate_code(erd_code)
        if isinstance(erd_code, str):
            return ErdDataType.STRING
        
        try:
            return self._registry[erd_code].data_type
        except KeyError:
            return ErdDataType.STRING            
    
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
        