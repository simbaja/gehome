from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

from gehomesdk.erd.erd_codes import ErdCodeType
from gehomesdk.exception import GeSetErdNotAllowedError

T = TypeVar('T')

class ErdValueConverter(Generic[T], ABC):
    def __init__(self, erd_code: ErdCodeType = "Unknown", can_decode: bool = True, can_encode: bool = True):
        self.erd_code = erd_code
        self._can_decode = can_decode
        self._can_encode = can_encode

    @abstractmethod
    def erd_encode(self, value: T) -> str:
        pass
    @abstractmethod
    def erd_decode(self, value: str) -> T:
        pass
    @property
    def can_decode(self) -> bool:
        return self._can_decode
    @property
    def can_encode(self) -> bool:
        return self._can_encode

class ErdReadWriteConverter(Generic[T], ABC):
    def __init__(self, erd_code: ErdCodeType = "Unknown"):
        ErdValueConverter.__init__(self, erd_code, True, True)

class ErdReadOnlyConverter(ErdValueConverter[T]):
    def __init__(self, erd_code: ErdCodeType = "Unknown"):
        ErdValueConverter.__init__(self, erd_code, True, False)
    def erd_encode(self, value: T) -> str:
        raise GeSetErdNotAllowedError(self.erd_code)
