import enum
from typing import NamedTuple


@enum.unique
class ErdOvenEstimatedTimeStatus(enum.Enum):
    INVALID = 0
    PENDING = 1
    ACTIVE = 2
    COMPLETE = 3
    UNKNOWN = 255

    def stringify(self, **kwargs) -> str:
        return self.name.replace("_", " ").title()


class ErdOvenEstimatedMinutesRemaining(NamedTuple):
    minutes_remaining: int = 0
    status: ErdOvenEstimatedTimeStatus = ErdOvenEstimatedTimeStatus.INVALID
    raw_value: str | None = None

    def stringify(self, **kwargs) -> str:
        if self.status in (
            ErdOvenEstimatedTimeStatus.INVALID,
            ErdOvenEstimatedTimeStatus.UNKNOWN,
        ):
            return self.status.stringify()
        return f"{self.minutes_remaining} min ({self.status.stringify()})"
