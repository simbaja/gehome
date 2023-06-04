from typing import NamedTuple, Optional

class ErdDehumidifierMaintenance (NamedTuple):
    empty_bucket: bool = False
    clean_filter: bool = False
    raw_value: Optional[str] = None

