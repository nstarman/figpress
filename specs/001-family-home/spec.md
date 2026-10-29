# Feature Specification: The figpress family home

**Feature Branch**: `001-family-home`

**Created**: 2026-10-28

**Status**: Draft

**Input**: User description: "The figpress repository should start by hosting the website of all the
figpress-* packages, and take the name figpress on npm and PyPI. Publish on whatever package index
makes sense. Releases from tags with trusted publishing; the first npm release is published by hand."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Find the family and pick a package (Priority: P1)

A researcher who heard of figpress opens the family's website and, on one page, learns what the
family is for, which packages it has (today figpress-apps and figpress-plotly), what each one is
for, and how to install it, with links to each package's code, documentation and releases.

**Why this priority**: it is the reason the repository exists; without it the family has no home.

**Independent Test**: open the published website and, for each package, find its purpose, its
install commands and working links, without reading any other page.

**Acceptance Scenarios**:

1. **Given** the website is published, **When** a reader opens it, **Then** they see what the
   family is for and one entry per member, each with its purpose, install commands and links.
2. **Given** a new member is added to the family's list, **When** the change is merged, **Then**
   the website shows it with no other edit.
3. **Given** a reader on a phone, **When** they open the website, **Then** it is readable without
   horizontal scrolling.

---

### User Story 2 - The name `figpress` belongs to the family (Priority: P1)

Someone who runs `pip install figpress` or `npm install @nstarkman/figpress` gets a genuine, small package
from the family that tells them what figpress is, lists its members and points to the website,
rather than nothing or someone else's package.

**Why this priority**: until a first release exists, the names can be taken by anyone; claiming
them is time-critical.

**Independent Test**: install `figpress` from each index in a clean environment and run its
entry point; it prints the family's members and the website address.

**Acceptance Scenarios**:

1. **Given** the first release is published, **When** someone installs `figpress` from PyPI and
   runs it, **Then** it prints the family's members (from the same list as the website) and the
   website address.
2. **Given** the first release is published, **When** someone installs `@nstarkman/figpress` from npm and
   runs it, **Then** it prints the same.
3. **Given** either package page on an index, **When** a reader opens it, **Then** it describes
   the family and links to the website and repository.

---

### User Story 3 - Release by tagging (Priority: P2)

The maintainer releases a new version by pushing a date tag; the package is built, checked and
published to both indexes without any stored token.

**Why this priority**: every later release depends on it, but the first npm release is by hand
anyway, so it can follow the first PyPI release.

**Independent Test**: push a tag `vYYYY.MM.DD` and confirm the matching versions appear on both
indexes, built from that commit.

**Acceptance Scenarios**:

1. **Given** a tag `vYYYY.MM.DD` is pushed, **When** the release workflow runs, **Then** PyPI gets
   `YYYY.MM.DD` and npm `YYYYMMDD.0.0`, both built from the tagged commit.
2. **Given** a tag whose version does not match the package's version, **When** the workflow runs,
   **Then** it fails before publishing anything.
3. **Given** the version already exists on an index, **When** the workflow runs, **Then** that
   index is skipped with a notice rather than failing the release.

### Edge Cases

- A same-day second release: `vYYYY.MM.DD.2` publishes as `YYYY.MM.DD.2` on PyPI and
  `YYYYMMDD.0.2` on npm (npm needs three-part semver), each sorting after the day's first release.
- npm's first release cannot come from the workflow (trusted publishing needs the package to
  exist): the maintainer publishes it by hand, and the workflow then skips that version.
- A member listed without a released package yet: the website still lists it and says it is not
  released yet, instead of showing broken install commands.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The family's members MUST be recorded once, in one machine-readable list, with each
  member's name, one-sentence purpose, repository, documentation link, indexes it is published to
  and release status.
- **FR-002**: The website MUST be generated from that list and published from the repository's
  default branch; a change to the list MUST update the website with no other edit.
- **FR-003**: The website MUST work without JavaScript, from any static host, and on a phone.
- **FR-004**: The `figpress` package MUST be published to PyPI as `figpress` and to npm as
  `@nstarkman/figpress` (npm refuses the unscoped name as too similar to `figures`), with a description, the website and repository links, and the MIT licence.
- **FR-005**: Running the package's entry point (`figpress` on the command line from either index)
  MUST print the family's members and the website address, from the same list as the website.
- **FR-006**: The package MUST NOT depend on the other family packages.
- **FR-007**: Pushing a tag `vYYYY.MM.DD` or `vYYYY.MM.DD.N` MUST publish that version to both
  indexes from the tagged commit with trusted publishing, and MUST fail before publishing if the
  tag and the package version differ.
- **FR-008**: CI MUST check on every pull request that the website builds from the list and that
  both packages build and run.

### Key Entities

- **Family member**: name, purpose, repository, documentation link, its name on each index (PyPI,
  npm), status
  (released or not yet).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pip install figpress` and `npm install @nstarkman/figpress` both succeed and print the family
  list, from the first release on.
- **SC-002**: A reader finds a member's install command on the website in under 30 seconds.
- **SC-003**: Adding a member is a change to one file, and the website shows it after merge.
- **SC-004**: A release needs only a pushed tag after the first npm release; no stored secret
  exists in the repository.

## Assumptions

- The repository is public, `nstarman/figpress`, with GitHub Pages serving the website at
  `https://nstarkman.space/figpress/` (the account's Pages domain).
- PyPI's pending trusted publisher for `figpress` is already registered (repository
  `nstarman/figpress`, workflow `release.yml`, environment `pypi`).
- The npm package is plain JavaScript with no dependencies; the PyPI package is pure Python.
- npm names are scoped `@nstarkman/<name>`: npm refused the unscoped `figpress` as too similar to
  `figures`, and the family is mostly for the maintainer's own use.
- Members at first: figpress-apps (the renamed figkit) and figpress-plotly, both not yet released.
