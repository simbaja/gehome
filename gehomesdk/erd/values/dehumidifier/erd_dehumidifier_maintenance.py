from typing import NamedTuple

class ErdDehumidifierMaintenance (NamedTuple):
    empty_bucket: bool = False
    clean_filter: bool = False
    raw_value: str | None = None

