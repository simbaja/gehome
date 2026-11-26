from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int


class ErdReadOnlyWaterHeaterTemperatureConverter(ErdReadOnlyConverter[float]):
    def erd_decode(self, value) -> float:
        try:
            return erd_decode_int(value) / 10
        except ValueError:
            return 0


class ErdWaterHeaterTemperatureConverter(
    ErdReadWriteConverter[float]
):
    def erd_decode(self, value) -> float:
        try:
            return erd_decode_int(value) / 10
        except ValueError:
            return 0

    def erd_encode(self, value: float) -> str:
        return erd_encode_int(int(value * 10))
