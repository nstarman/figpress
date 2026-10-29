# figpress Constitution

figpress is the home of a family of packages for the figures of scientific papers: figures that go
to press as print figures and to the web as interactive ones. This repository hosts the family's
website and the `figpress` package itself; each `figpress-*` package lives in its own repository.

## Core Principles

### I. One home for the family

- The website lists every `figpress-*` package: what it is for, how to install it, and where its
  code, documentation and releases are.
- The family's members are recorded once, in `family.json`; the site is built from it. Adding a
  package to the family is a pull request that changes `family.json`.
- Rationale: one list cannot disagree with itself; a site and a README edited separately can.

### II. A real package, not a squat

- `figpress` on PyPI and npm is a small, working package: it describes the family, lists its
  members (from `family.json`) and points to the website. It MUST NOT claim functionality it does
  not have, and MUST NOT depend on the other `figpress-*` packages until a member is useful to
  install by itself through it.
- Rationale: the name is claimed so the family owns it; a placeholder that pretends to do more
  misleads people who install it.

### III. Static and dependency-free site

- The website is plain HTML and CSS served by GitHub Pages, generated from `family.json` by a
  standard-library Python script. No framework, bundler or runtime dependency.
- Rationale: the family's pages must keep working as long as the papers that use it; the web
  platform is backward compatible, toolchains are not.

### IV. Releases from tags, without stored secrets

- Versions are dates: tags `vYYYY.MM.DD`, and `vYYYY.MM.DD.N` (N = 2, 3, …) for another release the
  same day. The PyPI version is the tag's (`YYYY.MM.DD[.N]`); npm, which needs three-part semver,
  gets `YYYYMMDD.0.N` (N = 0 for the day's first release), as the nstarkman.space packages do. One
  script maps a tag to both, and a release whose versions do not match its tag MUST fail.
- A pushed tag publishes to PyPI and npm from `.github/workflows/release.yml` with trusted
  publishing (OIDC), from the GitHub environments `pypi` and `npm`. No API token is stored in the
  repository. (An npm package's first release is published by hand, because npm trusted
  publishing can be configured only for a package that exists.)
- Rationale: date versions say how current a release is at a glance, as in the family's other
  repositories; tokens in secrets leak and expire.

## Repository Rules

- Squash merges only. Agent guidance lives in `AGENTS.md`; this constitution overrides it where
  they differ.
- Features go through Spec Kit: specify, plan, tasks, implement, under `specs/`.

## Governance

- This constitution overrides other practices here. Specs and plans include a constitution check;
  deviations are justified in the plan's complexity tracking.
- Amendments are made by pull request with a version bump: MAJOR for removing or redefining a
  principle, MINOR for adding or materially expanding one, PATCH for wording.

**Version**: 1.0.0 | **Ratified**: 2026-10-28 | **Last Amended**: 2026-10-28
