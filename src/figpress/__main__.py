"""``figpress`` / ``python -m figpress``: the family's members and its website."""

from figpress import __version__, family


def render(f: dict) -> str:
    lines = [f"figpress {__version__}: {f['about']}", ""]
    for m in f["members"]:
        status = "" if m["released"] else " (not released yet)"
        lines += [f"  {m['name']}{status}", f"    {m['purpose']}", f"    {m['repository']}", ""]
    lines.append(f"More: {f['website']}")
    return "\n".join(lines)


def main() -> None:
    print(render(family()))


if __name__ == "__main__":
    main()
