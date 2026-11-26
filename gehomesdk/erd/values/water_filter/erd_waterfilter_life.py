from typing import NamedTuple

class ErdWaterFilterLifeRemaining(NamedTuple):
    life_remaining: int
    

    def stringify(self, **kwargs) -> str | None:
        return str(self.life_remaining)
