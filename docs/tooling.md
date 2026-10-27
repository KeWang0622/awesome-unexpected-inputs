# Search, rebuild and fork

[Collection](../README.md) · [Data](../data/projects.json) · [Schema](../data/schema.json)

The catalog works as plain Markdown. Optional tools require **Python 3.10+**, use only its standard library, and need no API key, package installation or network access.

```sh
python3 scripts/catalog.py search
python3 scripts/catalog.py search "camera"
python3 scripts/catalog.py search "声音" --json
python3 scripts/catalog.py search --status source-build
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 -m unittest discover -s tests -v
```

Search terms are case-insensitive AND matches across names, English/Chinese summaries and outcomes, devices, and requirements. Use quotes for a multiword query. `--category` accepts an exact English category name from `data/config.json`; combine it with `--status` and `--json` for filtered machine-readable results.

## Where to edit

| File | Role |
| --- | --- |
| `data/projects.json` | Reviewed entries and their evidence |
| `data/config.json` | Category order, six spotlights, titles and editorial descriptions |
| `scripts/catalog.py` | Validation, search, page generation and original SVG diagrams |
| `docs/choose.md` | Human-authored decisions and starting points |
| `docs/landscape.md` | Related work and the scope of novelty claims |

The builder writes both READMEs, setup notes, six SVG cards, the summary and schema. Edit their inputs instead of generated output. `check` regenerates in memory and fails on drift without changing files. `make verify` runs the checker and regression suite. A plain Python command is equivalent if Make is unavailable.

The JSON Schema documents the structural format. The Python validator additionally enforces cross-record uniqueness, category order, spotlight references, non-future dates and URL rules. Dates mean source inspection, not device testing. The URL check validates syntax and public-style HTTPS destinations; it does not fetch pages or prove a host's DNS/security properties.

## Forking

Update the account/repository links in the generator and workflow documentation, change the catalog/config, and regenerate. Preserve provenance for any retained records. Re-review sources before updating review dates. The original prose/diagrams are CC0; scripts/tests are MIT. Linked projects and media retain their own terms.
