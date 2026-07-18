import enum
from typing import Optional


@enum.unique
class ErdToasterOvenSize(enum.Enum):
    """Size selection packed into the toaster oven cook setting ERDs (0x9207/0x9208)."""
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

    def stringify(self, **kwargs) -> Optional[str]:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        return self.stringify() or ""
