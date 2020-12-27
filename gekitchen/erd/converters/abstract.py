from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

from gekitchen.erd.erd_codes import ErdCodeType
from gekitchen.exception import GeSetErdNotAllowedError

T = TypeVar('T')

class ErdValueConverter(Generic[T], ABC):
    def __init__(self, can_read: bool = True, can_write: bool = True, erd_code: ErdCodeType = "Unknown"):
        self.erd_code = erd_code
        self.can_read = can_read
        self.can_write = can_write

    @abstractmethod
    def erd_encode(self, value: T) -> str:
        pass
    @abstractmethod
    def erd_decode(self, value: str) -> T:
        pass

class ErdReadWriteConverter(Generic[T], ABC):
    def __init__(self, erd_code: ErdCodeType = "Unknown"):
        super().__init__(True, True, erd_code)

class ErdReadOnlyConverter(ErdValueConverter[T]):
    def __init__(self, erd_code: ErdCodeType):
        super().__init__(True, False, erd_code=erd_code)
    def erd_encode(self, value: T) -> str:
        raise GeSetErdNotAllowedError(self.erd_code)
