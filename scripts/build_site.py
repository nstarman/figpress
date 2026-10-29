"""Build the family's website from family.json: _site/index.html and _site/style.css.

    python scripts/build_site.py [OUT]     (OUT defaults to _site)
"""

import json
import shutil
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALL = {"pypi": "pip install {name}", "npm": "npm install {name}"}  # {name}: the member's name on that index


def member_html(m: dict) -> str:
    name = escape(m["name"])
    status = "" if m["released"] else '<span class="status">not released yet</span>'
    note = f" {escape(m['note'])}" if m.get("note") else ""
    # A member not released yet gets no install commands: they would fail.
    install = "".join(f"<pre>{escape(INSTALL[i].format(name=n))}</pre>" for i, n in m["indexes"].items()) if m["released"] else ""
    return (f'<section class="member" id="{name}"><h2>{name}{status}</h2>'
            f"<p>{escape(m['purpose'])}{note}</p>{install}"
            f'<p><a href="{escape(m["repository"])}">Code</a> · <a href="{escape(m["docs"])}">Documentation</a></p></section>')


def page(f: dict) -> str:
    members = "\n".join(member_html(m) for m in f["members"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>figpress</title>
<meta name="description" content="{escape(f['about'])}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<h1>figpress</h1>
<p class="lede">{escape(f['about'])}</p>
{members}
<footer>The figpress family · <a href="{escape(f['repository'])}">{escape(f['repository'].removeprefix('https://'))}</a></footer>
</main>
</body>
</html>
"""


def build(out: Path) -> Path:
    f = json.loads((ROOT / "family.json").read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page(f), encoding="utf-8")
    shutil.copyfile(ROOT / "site" / "style.css", out / "style.css")
    return out / "index.html"


if __name__ == "__main__":
    print(build(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"))
