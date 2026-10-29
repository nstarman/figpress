# AGENTS.md

figpress is the home of the figpress family (packages for the figures of scientific papers, in
print and on the web): its website and the small `figpress` package on PyPI and npm. Read
`.specify/memory/constitution.md` first; it overrides this file.

## Layout

```
family.json                 the family's members — the one list; the site and both packages read it
scripts/build_site.py       family.json → _site/ (GitHub Pages, deployed by pages.yml)
scripts/version.py          tag → PyPI and npm versions; check / set
src/figpress/               the PyPI package (`figpress`, `python -m figpress`)
bin/figpress.js             the npm package's CLI
tests/                      python -m unittest discover -s tests; node --test "tests/*.test.mjs"
.specify/, specs/           Spec Kit (v1.1.3): specify → plan → tasks → implement
```

## Adding a member

Add an entry to `family.json` (name, purpose, repository, docs, indexes, released) and open a pull
request. Set `released` to true once the member's first release is on its indexes.

## Releasing

Versions are dates. A tag `vYYYY.MM.DD` (or `vYYYY.MM.DD.N`, N = 2, 3, … for another release the
same day) publishes PyPI `YYYY.MM.DD[.N]` and npm `YYYYMMDD.0.N` (N = 0 for the day's first):

```bash
python scripts/version.py set v2026.10.29     # writes src/figpress/__init__.py and package.json
git commit -am "Release v2026.10.29" && git tag v2026.10.29 && git push --follow-tags
```

`release.yml` checks the versions against the tag, builds, and publishes with trusted publishing
from the `pypi` and `npm` environments; a version already on an index is skipped. No token is
stored. npm's first release was published by hand (trusted publishing needs an existing package).
