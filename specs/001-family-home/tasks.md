# Tasks: The figpress family home

**Input**: [spec.md](spec.md), [plan.md](plan.md), [research.md](research.md)

## Phase 1: Setup

- [ ] T001 Add `LICENSE` (MIT), `.gitignore`, `README.md`, `AGENTS.md`, `CHANGELOG.md`
- [ ] T002 Add `family.json` with figpress-apps and figpress-plotly (not yet released)

## Phase 2: Foundational

- [ ] T003 [P] `scripts/version.py`: tag → {pypi, npm}; `check` and `set` against `pyproject.toml`
      and `package.json`; tests in `tests/test_version.py`

## Phase 3: User Story 1 — find the family (P1)

- [ ] T004 [US1] `scripts/build_site.py` and `site/style.css`: `family.json` → `_site/`; no JS;
      readable on a phone; members not yet released say so instead of showing install commands
- [ ] T005 [US1] `tests/test_site.py`: every member appears with its purpose, links and status
- [ ] T006 [US1] `.github/workflows/pages.yml`: build and deploy to GitHub Pages on pushes to main

## Phase 4: User Story 2 — the name belongs to the family (P1)

- [ ] T007 [P] [US2] Python package: `pyproject.toml`, `src/figpress/{__init__,__main__}.py`
      (members from the bundled `family.json`, website), console script `figpress`
- [ ] T008 [P] [US2] npm package: `package.json`, `bin/figpress.js` (same output)
- [ ] T009 [US2] `tests/test_cli.py` and `tests/cli.test.mjs`: both print every member and the website

## Phase 5: User Story 3 — release by tagging (P2)

- [ ] T010 [US3] `.github/workflows/release.yml`: on `v*` tags check versions, build, publish to
      PyPI (`pypi` environment, skip existing) then npm (`npm` environment, skip existing)
- [ ] T011 [US3] `.github/workflows/ci.yml`: tests, site build, both packages build, versions agree

## Phase 6: Polish

- [ ] T012 Set the first version (`v2026.10.28`) with `scripts/version.py set`; run every check
      locally; show the maintainer before the repository is created and the tag pushed
