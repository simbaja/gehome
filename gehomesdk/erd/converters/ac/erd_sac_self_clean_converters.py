from ..abstract import ErdReadOnlyConverter, ErdReadWriteConverter
from ..primitives import erd_decode_int, erd_encode_int
from ...values.ac import (
    ErdSacAlerts,
    ErdSacSelfCleanReminderDuration,
    ErdSacSelfCleanSupport,
)


class ErdSacSelfCleanSupportConverter(ErdReadOnlyConverter[ErdSacSelfCleanSupport]):
    def erd_decode(self, value: str) -> ErdSacSelfCleanSupport:
        try:
            return ErdSacSelfCleanSupport(erd_decode_int(value))
        except ValueError:
            return ErdSacSelfCleanSupport.UNKNOWN


class ErdSacSelfCleanReminderDurationConverter(
    ErdReadWriteConverter[ErdSacSelfCleanReminderDuration]
):
    def erd_decode(self, value: str) -> ErdSacSelfCleanReminderDuration:
        try:
            return ErdSacSelfCleanReminderDuration(erd_decode_int(value))
        except ValueError:
            return ErdSacSelfCleanReminderDuration.UNKNOWN

    def erd_encode(self, value: ErdSacSelfCleanReminderDuration) -> str:
        return erd_encode_int(ErdSacSelfCleanReminderDuration(value).value, 1)


class ErdSacAlertsConverter(ErdReadOnlyConverter[ErdSacAlerts]):
    def erd_decode(self, value: str) -> ErdSacAlerts:
        if not value:
            return ErdSacAlerts()
        try:
            i = erd_decode_int(value)
            return ErdSacAlerts(
                self_clean_first_alert=bool((i >> 8) & 1),
                self_clean_second_alert=bool((i >> 9) & 1),
                self_clean_third_alert=bool((i >> 10) & 1),
                self_clean_in_app_banner_alert=bool((i >> 11) & 1),
                raw_value=value,
            )
        except ValueError:
            return ErdSacAlerts(raw_value=value)
