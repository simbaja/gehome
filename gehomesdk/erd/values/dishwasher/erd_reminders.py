from typing import NamedTuple, Optional

class ErdReminders (NamedTuple):
    clean_filter: bool = False
    add_rinse_aid: bool = False
    sanitized: bool = False
    raw_value: Optional[str] = None

