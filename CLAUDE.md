# Claude Code instructions for global-test-data

This repository is a catalogue of **country-specific example data that passes
validation but belongs to no one**: company and tax identifiers, addresses,
postcodes, phone numbers, email domains, bank details, trade codes. Anyone can use
it in documentation, tests and sample documents (for example UBL invoices) without
colliding with a real organisation or person.

## Branches

- **`main`**: data, validators, site generator, research notes, docs. All work
  happens here (via pull requests or feature branches).
- **`gh-pages`**: generated website only. Written by the GitHub Actions workflow on
  every push to `main`. **Never edit or commit to `gh-pages` by hand.**

## Layout

| Path | Purpose |
|---|---|
| `data/<cc>.yaml` | One file per country (ISO 3166-1 alpha-2, lower case) plus `global.yaml` |
| `schema/country.schema.json` | JSON Schema for the data files |
| `tools/checks.py` | Check-digit / format validators, registered in `CHECKS` |
| `tools/validate.py` | Schema, unique ids, `checks` / `fails_checks` |
| `tools/build.py` | Builds the site and JSON/CSV exports into `_site/` |
| `research/` | Research notes: the evidence behind the data |
| `.github/workflows/pages.yml` | Validate on PRs; validate, build and publish to `gh-pages` on push to `main` |

## Rules for data

1. **Every entry needs at least one source URL**, preferably the authority's own
   page or document (regulator, tax authority, registry, standards body). Blogs,
   vendor pages and generators are secondary at best.
2. **Status only from evidence:**
   - `reserved`: an authority formally reserves the value or range
   - `published-example`: an authority uses it in its own examples (list the
     `checks` it passes, or `fails_checks` if deliberately invalid)
   - `derived`: built from the official rules **and** checked to be unassigned;
     `verified:` lines must name the register and the date
   - `avoid`: circulates as an example but is real or invalid; needs a `reason`
3. **Unverified findings stay in `research/`**, never as usable entries in `data/`.
   A passing checksum does not prove a value is unassigned.
4. Email addresses in usable entries must use a reserved domain
   (`reserved-domain` check: RFC 2606/6761, JPRS example.jp etc.).
5. Never put real personal data (names, emails, phone numbers of real people) in
   the data, not even in `avoid` entries; describe them instead.
6. When researching a country, also search in its official language(s), and prefer
   primary sources.

## Before committing

```bash
pip install pyyaml jsonschema
python tools/validate.py      # must report 0 errors
python tools/build.py         # optional local preview in _site/
```

New identifier type: add a validator to `tools/checks.py` with a docstring citing
the algorithm's source, register it in `CHECKS`, and use it in the entries.

## Open work

Tracked as GitHub issues: missing validators and values awaiting verification.

## Licence

CC0 1.0. Contributions are published under the same licence.
