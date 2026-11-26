from ..abstract import ErdReadOnlyConverter
from ...values.oven import (
    ErdOvenEstimatedMinutesRemaining,
    ErdOvenEstimatedTimeStatus,
)


class ErdOvenEstimatedMinutesRemainingConverter(
    ErdReadOnlyConverter[ErdOvenEstimatedMinutesRemaining]
):
    def erd_decode(self, value: str) -> ErdOvenEstimatedMinutesRemaining:
        if not value:
            return ErdOvenEstimatedMinutesRemaining()
        try:
            raw = bytes.fromhex(value)
            if len(raw) < 3:
                return ErdOvenEstimatedMinutesRemaining(raw_value=value)
            minutes = int.from_bytes(raw[0:2], "big")
            try:
                status = ErdOvenEstimatedTimeStatus(raw[2])
            except ValueError:
                status = ErdOvenEstimatedTimeStatus.UNKNOWN
            return ErdOvenEstimatedMinutesRemaining(
                minutes_remaining=minutes,
                status=status,
                raw_value=value,
            )
        except ValueError:
            return ErdOvenEstimatedMinutesRemaining(raw_value=value)
