# Research: The figpress family home

## Versions on two indexes

- **Decision**: tags `vYYYY.MM.DD[.N]`; PyPI version `YYYY.MM.DD[.N]`; npm version `YYYYMMDD.0.N`
  (N = 0 for the day's first release).
- **Rationale**: PEP 440 accepts four-part date versions; npm requires three-part semver, so
  `2026.10.28.2` is invalid there. `YYYYMMDD.0.N` is what `@nstarkman/research-kit` already uses,
  sorts correctly and keeps the date readable.
- **Alternatives**: `YYYY.MMDD.N` (harder to read); npm prerelease suffix `-N` (sorts *before* the
  plain version, wrong).

## Publishing without secrets

- **Decision**: PyPI trusted publishing with `pypa/gh-action-pypi-publish` from environment `pypi`
  (pending publisher already registered); npm trusted publishing (`npm publish --provenance`, npm ≥
  11.5.1, i.e. Node 24) from environment `npm`, configured on npmjs.com after a hand-published
  first release.
- **Rationale**: no token to leak or rotate; provenance on both indexes.
- **Alternatives**: API tokens in repository secrets (rejected by Principle IV).

## Skipping versions already published

- **Decision**: PyPI step uses `skip-existing: true`; npm step checks `npm view figpress@<v>` first.
- **Rationale**: the first npm release is published by hand; the tag's workflow must not fail on it.

## Website hosting

- **Decision**: GitHub Pages deployed by Actions (`configure-pages`, `upload-pages-artifact`,
  `deploy-pages`) from `_site/` built in CI; served at `https://nstarkman.space/figpress/` through
  the account's Pages domain.
- **Rationale**: nothing generated is committed; the site rebuilds from `family.json` on every push.
