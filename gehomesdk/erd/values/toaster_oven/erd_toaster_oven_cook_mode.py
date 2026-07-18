import enum
from typing import Optional


@enum.unique
class ErdToasterOvenCookMode(enum.Enum):
    """
    Cook modes for toaster oven appliances (e.g. Cafe/Couture countertop ovens),
    as packed into the "Cook Mode" field of the cook setting ERDs (0x9207/0x9208).
    """
    AIR_FRY = 0
    BAKE = 1
    BROIL = 2
    ROAST = 3
    REHEAT = 4
    WARM = 5
    SLOW_COOK = 6
    DEHYDRATE = 7
    PROOF = 8
    COOKIE = 9
    PIZZA = 10
    BAGEL = 11
    TOAST = 12
    CRISP_FINISH = 13
    CAKE = 14
    COOKIE_WITH_PREFERENCES = 15
    PIZZA_WITH_PREFERENCES = 16
    CONVECTION_BAKE = 17

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        return self.stringify() or ""
