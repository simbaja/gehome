from typing import NamedTuple, Optional

class ErdSheetUsageConfiguration (NamedTuple):
    extraLargeLoadSize: int = 0
    LargeLoadSize: int = 0
    mediumLoadSize: int = 0
    smallLoadSize: int = 0
    timedDryerSheetsLoadSize: int = 0
    raw_value: Optional[str] = None
