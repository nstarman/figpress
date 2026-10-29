"""scripts/version.py: a tag maps to the PyPI and npm versions it publishes."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("version", ROOT / "scripts" / "version.py")
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)


class VersionTest(unittest.TestCase):
    def test_first_release_of_a_day(self):
        self.assertEqual(version.versions("v2026.10.28"), {"pypi": "2026.10.28", "npm": "20261028.0.0"})

    def test_same_day_release(self):
        self.assertEqual(version.versions("v2026.10.28.2"), {"pypi": "2026.10.28.2", "npm": "20261028.0.2"})

    def test_rejects_other_tags(self):
        for bad in ("2026.10.28", "v2026.1.28", "v0.2.0", "v2026.10.28.1"):
            with self.subTest(bad), self.assertRaises(ValueError):
                version.versions(bad)

    def test_repository_versions_agree(self):
        have = version.current()
        self.assertEqual(have, version.versions(f"v{have['pypi']}"))


if __name__ == "__main__":
    unittest.main()
