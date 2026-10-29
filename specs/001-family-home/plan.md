# Implementation Plan: The figpress family home

**Branch**: `001-family-home` | **Date**: 2026-10-28 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-family-home/spec.md`

## Summary

One list of the family's members (`family.json`) feeds three things: the website (static HTML built
by a standard-library Python script and deployed to GitHub Pages), the `figpress` Python package and
the `figpress` npm package (both small command-line programs that print the list and the website
address). A tag `vYYYY.MM.DD[.N]` publishes both packages with trusted publishing.

## Technical Context

**Language/Version**: Python ≥ 3.10 (package, site builder, version script; standard library only);
JavaScript for Node ≥ 18 (npm package; no dependencies)

**Primary Dependencies**: none at runtime. Build: hatchling (Python wheel/sdist). CI: GitHub Actions
(`actions/configure-pages`, `upload-pages-artifact`, `deploy-pages`, `pypa/gh-action-pypi-publish`,
`actions/setup-node` with Node 24 for npm trusted publishing)

**Storage**: `family.json` in the repository

**Testing**: `python -m unittest` (site builds, members rendered, CLI output, tag→version mapping);
`node --test` (npm CLI output)

**Target Platform**: GitHub Pages (static); PyPI; npm

**Project Type**: website + two tiny CLI packages

**Performance Goals**: N/A

**Constraints**: no JavaScript on the website; no runtime dependencies; no stored secrets

**Scale/Scope**: a handful of members

## Constitution Check

| Principle | How this plan meets it |
|---|---|
| I. One home for the family | `family.json` is the only list; the site and both packages read it. |
| II. A real package, not a squat | Both packages print the real member list and the website; no dependencies on members. |
| III. Static, dependency-free site | `scripts/build_site.py` (standard library) writes plain HTML + CSS; Pages serves it. |
| IV. Releases from tags | `release.yml` on `v*` tags; `scripts/version.py` maps tag → PyPI and npm versions and fails on mismatch; OIDC to PyPI (`pypi` environment) and npm (`npm` environment). |

No violations.

## Project Structure

### Documentation (this feature)

```text
specs/001-family-home/
├── spec.md
├── plan.md
├── research.md
├── quickstart.md
├── checklists/requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
family.json                 the family's members (one source)
pyproject.toml              figpress (PyPI): hatchling; family.json shipped inside the package
src/figpress/__init__.py    __version__, members(), WEBSITE
src/figpress/__main__.py    `figpress` / `python -m figpress`: print the members and the website
package.json                figpress (npm): bin/figpress.js; files: bin/, family.json, README, LICENSE
bin/figpress.js             the npm CLI
scripts/build_site.py       family.json → _site/index.html, _site/style.css
scripts/version.py          tag → {pypi, npm}; `check` compares with pyproject/package.json
site/style.css              the site's stylesheet (copied into _site/)
tests/                      unittest: site, CLI, version mapping
tests/cli.test.mjs          node --test: npm CLI
.github/workflows/ci.yml       PRs/pushes: tests, build site, build both packages, versions agree
.github/workflows/pages.yml    pushes to main: build and deploy the site
.github/workflows/release.yml  tags v*: check versions, build, publish PyPI then npm
AGENTS.md, README.md, LICENSE, CHANGELOG.md
```

**Structure Decision**: single repository, both packages at the root sharing `family.json`, so the
list exists once (Principle I).

## Complexity Tracking

None.
