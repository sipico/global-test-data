#!/usr/bin/env python3
"""Validate every data file: schema, unique ids, and check digits.

Usage: python tools/validate.py [data/xx.yaml ...]
Exit code 0 = all good, 1 = errors (printed).
"""

import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from checks import CHECKS  # noqa: E402


class _Loader(yaml.SafeLoader):
    """SafeLoader that keeps dates (and times) as plain strings."""


_Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, Loader=_Loader)  # noqa: S506 - SafeLoader subclass


def validate(paths):
    schema = json.loads((ROOT / "schema" / "country.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors, ids, codes = [], {}, {}
    total = 0
    for path in paths:
        rel = path.relative_to(ROOT) if path.is_absolute() else path
        try:
            doc = load(path)
        except yaml.YAMLError as e:
            errors.append(f"{rel}: YAML error: {e}")
            continue
        for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
            loc = "/".join(str(p) for p in err.path)
            errors.append(f"{rel}: schema: {loc}: {err.message}")
        if not isinstance(doc, dict):
            continue
        code = str(doc.get("code", ""))
        expected = path.stem.upper()
        if code != expected:
            errors.append(f"{rel}: code '{code}' must match file name ({expected})")
        if code in codes:
            errors.append(f"{rel}: duplicate country code {code} (also in {codes[code]})")
        codes[code] = rel
        prefix = "global-" if code == "GLOBAL" else code.lower() + "-"
        research = doc.get("research")
        if research and not (ROOT / research).exists():
            errors.append(f"{rel}: research file not found: {research}")
        for ident in doc.get("identifiers", []) or []:
            chk = ident.get("check")
            if chk and chk not in CHECKS:
                errors.append(f"{rel}: identifier '{ident.get('name')}': unknown check '{chk}'")
        for i, e in enumerate(doc.get("entries", []) or []):
            total += 1
            eid = e.get("id", f"#{i}")
            where = f"{rel}: {eid}"
            if not str(eid).startswith(prefix):
                errors.append(f"{where}: id must start with '{prefix}'")
            if eid in ids:
                errors.append(f"{where}: duplicate id (also in {ids[eid]})")
            ids[eid] = rel
            value = str(e.get("value", ""))
            for chk in e.get("checks", []) or []:
                if chk not in CHECKS:
                    errors.append(f"{where}: unknown check '{chk}'")
                elif not CHECKS[chk][0](value):
                    errors.append(f"{where}: value '{value}' FAILS check '{chk}'")
            for chk in e.get("fails_checks", []) or []:
                if chk not in CHECKS:
                    errors.append(f"{where}: unknown check '{chk}'")
                elif CHECKS[chk][0](value):
                    errors.append(f"{where}: value '{value}' unexpectedly PASSES '{chk}'")
            if e.get("status") != "avoid" and e.get("category") == "contact" \
                    and "@" in value and "reserved-domain" not in (e.get("checks") or []):
                errors.append(f"{where}: email addresses must list the 'reserved-domain' check")
    return errors, total, len(codes)


def main(argv):
    paths = [pathlib.Path(p).resolve() for p in argv] or sorted((ROOT / "data").glob("*.yaml"))
    errors, total, countries = validate(paths)
    for err in errors:
        print("ERROR", err)
    print(f"{countries} file(s), {total} entries, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
