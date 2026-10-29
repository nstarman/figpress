# figpress

Packages for the figures of scientific papers: figures that go to press as print figures and to
the web as interactive ones.

The family's website, **<https://nstarkman.space/figpress/>**, lists every member with what it is
for and how to install it. The members today:

- **[figpress-plotly](https://github.com/nstarman/figpress-plotly)**: a paper's figures in Plotly.
  One definition gives the print figure the paper publishes and a matching interactive web figure
  that can do more. *Not released yet.*
- **[figpress-apps](https://github.com/nstarman/figpress-apps)**: interactive apps that are the
  counterparts of a paper's figures, built from the paper's own data and published next to the
  PDF. Formerly figkit. *Not released yet.*

This repository hosts the website and the small `figpress` package on
[PyPI](https://pypi.org/project/figpress/) and [npm](https://www.npmjs.com/package/figpress), which
prints the same list:

```bash
pipx run figpress        # or: uvx figpress
npx figpress
```

## Developing

```bash
python -m unittest discover -s tests     # site, CLI, versions
node --test "tests/*.test.mjs"                  # npm CLI
python scripts/build_site.py              # → _site/index.html
```

The members are listed once, in [`family.json`](family.json); the website and both packages read
it. Releases are dated: see [AGENTS.md](AGENTS.md).

## Licence

MIT.
