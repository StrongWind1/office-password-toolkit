# Installation

The toolkit is a pure-Python package built and run with [uv](https://docs.astral.sh/uv/). Pick one of the two paths below depending on whether you want the released tool or a working copy of the source.

## As a tool (recommended)

```bash
uv tool install office-password-toolkit
```

That installs the package into an isolated, always-on-PATH environment and exposes two console scripts that point at the same CLI: the full name `office-password-toolkit` and the short alias `opt`. Everything in the rest of the docs is written against `opt`.

```bash
opt --version          # office-password-toolkit 0.1.0
opt --help             # list the three commands
```

To upgrade to the latest release later, run `uv tool upgrade office-password-toolkit`.

## From source

Clone the repository and install it into a virtual environment:

```bash
git clone https://github.com/StrongWind1/office-password-toolkit
cd office-password-toolkit
uv venv
uv pip install .
uv run opt --help
```

If you intend to hack on the code, use the project workflow instead of a plain install — `uv sync` resolves the full lockfile (runtime plus the `dev` group) so `make check` and `uv run opt` work out of the box:

```bash
uv sync
make check             # ruff + ty + pytest + mkdocs --strict
uv run opt --help
```

Source and lockfile installs track `olefile` from its upstream Git HEAD (pinned via `[tool.uv.sources]` in `pyproject.toml`) rather than the last PyPI release, because HEAD carries the OLE write-path fixes the `bypass` code depends on for editing containers in place.

## Requirements

Python 3.11 or newer (`requires-python = ">=3.11"`; the package is tested on 3.11 through 3.14). uv will download a suitable interpreter for you if the host does not already have one.

The six runtime dependencies are pulled in automatically and need no extra flags:

| Dependency | Role |
|---|---|
| `typer` | the subcommand CLI (`info` / `unlock` / `advanced`) |
| `rich` | the coloured status and per-gate breakdown written to stderr |
| `olefile` (Git HEAD) | reading and rewriting OLE/CFB containers (`.doc` / `.xls` / `.ppt`, and the OLE wrapper around encrypted OOXML) |
| `cryptography` | AES / Blowfish / 3DES / RC2 cipher primitives behind `decrypt` and hash extraction (RC4 is pure-Python; hashes use stdlib `hashlib`) |
| `argon2-cffi` | Argon2id key derivation for ODF 1.3 document-open encryption |
| `typing-extensions` | `@override` backport so the format handlers keep strict typing under the 3.11 floor |

There are no optional extras to enable.

## Next step

**Next steps:**

- [Quick start](quick-start.md) — end-to-end walkthrough
- [Command reference](../usage/commands.md) — every flag and exit code
