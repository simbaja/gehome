from pathlib import Path


def test_readme_contains_usage():
    readme = Path("README.md")
    assert readme.exists(), "README.md must exist"
    text = readme.read_text(encoding="utf-8").lower()
    # Basic heuristic: README should include usage, example, or install instructions
    assert ("usage" in text) or ("example" in text) or ("install" in text), "README.md should contain usage/install/example text"


def test_setup_declares_entry_points_or_metadata():
    """
    Lightweight check to ensure setup.py contains package metadata or entry points text.
    """
    setup = Path("setup.py")
    assert setup.exists(), "setup.py must exist"
    text = setup.read_text(encoding="utf-8").lower()
    assert ("entry_points" in text) or ("install_requires" in text) or ("packages=" in text) or ("setup(" in text), "setup.py seems to be missing packaging metadata"