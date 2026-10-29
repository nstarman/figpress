# Quickstart: The figpress family home

```bash
python -m unittest discover tests          # site, CLI, version mapping
node --test "tests/*.test.mjs"                     # npm CLI
python scripts/build_site.py                # → _site/index.html
python -m figpress                          # prints the family and the website
node bin/figpress.js                        # the same, from the npm package
python scripts/version.py v2026.10.28       # → {"pypi": "2026.10.28", "npm": "20261028.0.0"}
python scripts/version.py check v2026.10.28 # fails unless pyproject and package.json match
```

Add a member: edit `family.json`, open a pull request; the site updates on merge.

Release: set the versions (`python scripts/version.py set v2026.10.29`), commit, tag `v2026.10.29`,
push the tag.
