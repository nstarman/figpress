"""scripts/build_site.py: the website lists every member of family.json."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_site", ROOT / "scripts" / "build_site.py")
build_site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_site)
FAMILY = json.loads((ROOT / "family.json").read_text(encoding="utf-8"))


class SiteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.html = build_site.build(Path(self.tmp.name)).read_text(encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_every_member_with_its_purpose_and_links(self):
        for m in FAMILY["members"]:
            with self.subTest(m["name"]):
                self.assertIn(f'id="{m["name"]}"', self.html)
                self.assertIn(m["purpose"].replace("'", "&#x27;"), self.html)
                self.assertIn(m["repository"], self.html)

    def test_unreleased_members_have_no_install_commands(self):
        for m in FAMILY["members"]:
            if not m["released"]:
                self.assertNotIn(f"pip install {m['name']}", self.html)

    def test_no_javascript(self):
        self.assertNotIn("<script", self.html)

    def test_released_member_shows_install_commands(self):
        f = dict(FAMILY, members=[dict(FAMILY["members"][0], released=True)])
        html = build_site.page(f)
        self.assertIn(f"pip install {f['members'][0]['name']}", html)
        self.assertIn(f"npm install {f['members'][0]['name']}", html)


if __name__ == "__main__":
    unittest.main()
