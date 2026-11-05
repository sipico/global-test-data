# Global Test Data

Test data from across the world that can be used in testing and example data sets:
country-specific example data that passes validation but belongs to no one.

Company and tax numbers, VAT numbers, addresses, postcodes, phone numbers, email
domains, bank details and trade codes for documentation, tests and sample
documents (such as UBL invoices), without the risk of colliding with a real
company or person. Every value cites its source.

**Site:** https://sipico.github.io/global-test-data/

The data and tools live on `main`. On every push to `main`, GitHub Actions validates
the data, builds the site and commits the generated files to the `gh-pages` branch,
which GitHub Pages serves. Do not edit `gh-pages` by hand.

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

See [CONTRIBUTING.md](CONTRIBUTING.md). No code? Open an issue with the
"Suggest a value" form.

## Licence

Data and code: [CC0 1.0](LICENSE). Sources remain the property of their
publishers; only facts (identifier values and rules) are reproduced.
