import enum
from typing import Optional, NamedTuple

from .common_enums import ErdAcAvailableModes as ErdSacAvailableModes ### deprecated, use ErdAcAvailableModes


class ErdSacTargetTemperatureRange(NamedTuple):
    min: int
    max: int
    raw_value: str

    def stringify(self, **kwargs) -> Optional[str]:
        return f"min: {self.min}, max: {self.max}"


@enum.unique
class ErdSacSelfCleanSupport(enum.Enum):
    NOT_SUPPORTED = 0
    SUPPORTED = 1
    UNKNOWN = 255

    def stringify(self, **kwargs) -> str:
        return self.name.replace("_", " ").title()


@enum.unique
class ErdSacSelfCleanReminderDuration(enum.Enum):
    HOURS_250 = 0
    HOURS_500 = 1
    HOURS_1000 = 2
    HOURS_1500 = 3
    NEVER = 4
    UNKNOWN = 255

    def stringify(self, **kwargs) -> str:
        labels = {
            ErdSacSelfCleanReminderDuration.HOURS_250: "250 Hours",
            ErdSacSelfCleanReminderDuration.HOURS_500: "500 Hours",
            ErdSacSelfCleanReminderDuration.HOURS_1000: "1000 Hours",
            ErdSacSelfCleanReminderDuration.HOURS_1500: "1500 Hours",
            ErdSacSelfCleanReminderDuration.NEVER: "Never",
            ErdSacSelfCleanReminderDuration.UNKNOWN: "Unknown",
        }
        return labels[self]


class ErdSacAlerts(NamedTuple):
    self_clean_first_alert: bool = False
    self_clean_second_alert: bool = False
    self_clean_third_alert: bool = False
    self_clean_in_app_banner_alert: bool = False
    raw_value: Optional[str] = None

    def boolify(self) -> bool:
        return any(
            (
                self.self_clean_first_alert,
                self.self_clean_second_alert,
                self.self_clean_third_alert,
                self.self_clean_in_app_banner_alert,
            )
        )

    def stringify(self, **kwargs) -> str:
        active = [
            name
            for flag, name in (
                (self.self_clean_first_alert, "Self Clean First Alert"),
                (self.self_clean_second_alert, "Self Clean Second Alert"),
                (self.self_clean_third_alert, "Self Clean Third Alert"),
                (self.self_clean_in_app_banner_alert, "Self Clean In-App Banner Alert"),
            )
            if flag
        ]
        return ", ".join(active) if active else "None"
