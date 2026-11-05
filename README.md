# Global Test Data

Country-specific example data that passes validation but belongs to no one.

Company and tax numbers, VAT numbers, addresses, postcodes, phone numbers, email
domains, bank details and trade codes for documentation, tests and sample
documents (such as UBL invoices), without the risk of colliding with a real
company or person. Every value cites its source.

**Site:** published from this branch with GitHub Pages.

## What is in here

| Path | Contents |
|---|---|
| `data/*.yaml` | One file per country (plus `global.yaml`): usable values and values to avoid, each with sources |
| `schema/country.schema.json` | JSON Schema for the data files |
| `tools/checks.py` | Check-digit and format validators (SIREN, IBAN, ABN, GSTIN, CNPJ, …) |
| `tools/validate.py` | Validates schema, unique ids and check digits |
| `tools/build.py` | Builds the static site and JSON/CSV exports into `_site/` |
| `site/assets/` | Site stylesheet and script |
| `research/` | Research notes with the evidence behind the data |

## Status of a value

- **reserved**: an authority formally reserves it for fiction, examples or tests
- **published-example**: an authority uses it in its own examples
- **derived**: built from the official rules and checked to be unassigned
- **avoid**: circulates as an example but is real or invalid

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests target this `gh-pages`
branch.

## Licence

Data and code: [CC0 1.0](LICENSE). Sources remain the property of their
publishers; only facts (identifier values and rules) are reproduced.
