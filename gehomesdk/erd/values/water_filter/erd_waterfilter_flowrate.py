from typing import NamedTuple

class ErdWaterFilterFlowRate(NamedTuple):
    flow_rate: float

    def stringify(self, **kwargs) -> str | None:
        return "{:.2f}".format(self.flow_rate)
