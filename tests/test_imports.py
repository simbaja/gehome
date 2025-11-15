import importlib
import pytest

MODULES = [
    "gehomesdk",
    "gehomesdk.ge_appliance",
    "gehomesdk.gather_data",
    "gehomesdk.entry_points",
    "gehomesdk.erd",
    "gehomesdk.erd.converters",
]


def test_modules_importable():
    """
    Ensure key package modules import without requiring network access.
    If modules perform heavy side effects at import-time, they should be refactored.
    """
    failures = []
    for mod in MODULES:
        try:
            importlib.import_module(mod)
        except Exception as exc:
            failures.append(f"{mod}: {exc!r}")

    if failures:
        pytest.fail("Import failures:\n" + "\n".join(failures))