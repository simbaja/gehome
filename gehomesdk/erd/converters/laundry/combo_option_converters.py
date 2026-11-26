from typing import Any

from ..abstract import ErdReadOnlyConverter
from ..primitives import erd_decode_int
from ...values.laundry import (
    ErdDeepFillIncrementalOption,
    ErdLaundryControlLockOption,
    ErdSoilLevelOption,
    ErdWashTempOption,
)


class _EnumOptionConverter(ErdReadOnlyConverter):
    _enum_cls: type[Any]
    _default: Any = None

    def erd_decode(self, value: str):
        try:
            return self._enum_cls(erd_decode_int(value))
        except ValueError:
            return self._default


class ErdLaundryControlLockOptionConverter(_EnumOptionConverter):
    _enum_cls = ErdLaundryControlLockOption
    _default = ErdLaundryControlLockOption.UNKNOWN


class ErdDeepFillIncrementalOptionConverter(_EnumOptionConverter):
    _enum_cls = ErdDeepFillIncrementalOption
    _default = ErdDeepFillIncrementalOption.UNKNOWN


class ErdWashTempOptionConverter(_EnumOptionConverter):
    _enum_cls = ErdWashTempOption
    _default = ErdWashTempOption.UNKNOWN


class ErdSoilLevelOptionConverter(_EnumOptionConverter):
    _enum_cls = ErdSoilLevelOption
    _default = ErdSoilLevelOption.UNKNOWN
