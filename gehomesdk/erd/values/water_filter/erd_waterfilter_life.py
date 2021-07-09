from datetime import timedelta
from typing import NamedTuple, Optional
import humanize

class ErdWaterFilterLifeRemaining(NamedTuple):
    life_remaining: timedelta = timedelta(seconds=0)

    def stringify(self, **kwargs) -> Optional[str]:
        return humanize.naturaldelta(self.life_remaining, months=True, minimum_unit="days")
