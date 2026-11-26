from typing import NamedTuple

class ErdReminders (NamedTuple):
    clean_filter: bool = False
    add_rinse_aid: bool = False
    sanitized: bool = False
    raw_value: str | None = None

