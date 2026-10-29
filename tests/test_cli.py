"""`python -m figpress` prints every member and the website."""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY = json.loads((ROOT / "family.json").read_text(encoding="utf-8"))


class CliTest(unittest.TestCase):
    def test_prints_members_and_website(self):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"))
        out = subprocess.run([sys.executable, "-m", "figpress"], env=env, capture_output=True, text=True, check=True).stdout
        for m in FAMILY["members"]:
            self.assertIn(m["name"], out)
        self.assertIn(FAMILY["website"], out)


if __name__ == "__main__":
    unittest.main()
