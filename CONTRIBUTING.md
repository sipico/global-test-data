# Contributing to Global Test Data

Thank you for helping. This data set only grows through values that come with
evidence. A value without a source will not be merged.

Pull requests go to the **`gh-pages`** branch of this repository, not to `main`
(`main` holds the UBL examples).

## What qualifies

| Status | Use when | Evidence required |
|---|---|---|
| `reserved` | A regulator, registry or standard formally reserves the value or range for fiction, examples or tests (e.g. phone numbers for drama, GS1 prefix 952, RFC 2606 domains) | Link to the reservation (law, plan, standard, registry page) |
| `published-example` | An authority uses the value in its own published examples, specimens or test environments | Link to the authority's document or file; list the `checks` it passes, or `fails_checks` if it is deliberately invalid |
| `derived` | You built the value from the official format rules and checked that it is unassigned | `verified:` lines naming the register searched and the date |
| `avoid` | A value that circulates as an "example" but belongs to a real entity or fails validation | `reason:` plus a source showing the problem |

Prefer the authority's own page or document over blogs, vendor pages or
generators. Search in the country's official language(s) as well as English.
Values that you could not verify belong in the research notes
(`research/`), not in `data/`.

## Adding or changing data

1. Edit `data/<country>.yaml`, or create one named after the ISO 3166-1 alpha-2
   code in lower case (e.g. `data/de.yaml`). Copy the structure of
   [`data/fr.yaml`](data/fr.yaml). The schema is
   [`schema/country.schema.json`](schema/country.schema.json).
2. Each entry needs: `id` (starts with the country code, e.g. `de-`), `category`,
   `type`, `value`, `label`, `status` and at least one source with a URL.
3. Use `kind: range` for ranges or patterns (`01 99 00 xx xx`) and
   `kind: placeholder` for text such as a formatted example address.
4. List validators the value must pass under `checks` (see
   [`tools/checks.py`](tools/checks.py)). Email addresses in usable entries must
   use a reserved domain and list `reserved-domain`.
5. New identifier type? Add a validator function to `tools/checks.py`, register it
   in `CHECKS` with a one-line description, and cite the algorithm's source in a
   comment.
6. Optional: add `ubl:` hints (e.g. `cac:PartyTaxScheme/cbc:CompanyID`) and
   longer evidence in a research note under `research/`.

## Check locally

```bash
pip install pyyaml jsonschema
python tools/validate.py
python tools/build.py   # writes the site to _site/
```

`validate.py` must report 0 errors. The same checks run on every pull request.

## No code?

Open an issue with the value, what it is, the source URL and the checks you did.

## Licence

By contributing you agree that your contribution is published under
[CC0 1.0](LICENSE) (public domain dedication).
