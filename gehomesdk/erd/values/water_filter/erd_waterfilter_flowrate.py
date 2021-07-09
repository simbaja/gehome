from typing import NamedTuple, Optional

class ErdWaterFilterFlowRate(NamedTuple):
    flow_rate: float

    def stringify(self, **kwargs) -> Optional[str]:
        return "{:.2f}".format(self.flow_rate)
