"""figpress: the home of a family of packages for the figures of scientific papers.

This package lists the family's members and points to its website; the members are separate
packages (``figpress-plotly``, ``figpress-apps``). ``python -m figpress`` prints the list.
"""

import json
from importlib.resources import files
from pathlib import Path

__all__ = ("__version__", "family")

__version__ = "2026.10.28"


def family() -> dict:
    """The family: what it is for, its website and its members (``family.json``)."""
    bundled = files(__package__).joinpath("family.json")
    if bundled.is_file():  # installed: shipped inside the package
        return json.loads(bundled.read_text(encoding="utf-8"))
    # Run from a checkout: the repository's own list.
    return json.loads((Path(__file__).resolve().parents[2] / "family.json").read_text(encoding="utf-8"))
