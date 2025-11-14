from datetime import timedelta
from typing import NamedTuple, Optional
import humanize

class ErdWaterFilterLifeRemaining(NamedTuple):
    life_remaining: int
    

    def stringify(self, **kwargs) -> Optional[str]:
        return str(self.life_remaining)
