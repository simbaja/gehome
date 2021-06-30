from datetime import timedelta
from typing import NamedTuple, Optional


class ErdWaterFilterLifeRemaining(NamedTuple):
    life_remaining: int

    def stringify(self, **kwargs) -> Optional[str]:
        return f"{self.life_remaining} %"
