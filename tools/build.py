#!/usr/bin/env python3
"""Build the static site into _site/ from data/*.yaml.

Usage: python tools/build.py [--out _site]
Pages: index (directory), one page per country, contribute page,
plus machine-readable exports in data/ (JSON per country, all.json, all.csv).
"""

import argparse
import csv
import html
import io
import json
import os
import pathlib
import shutil
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from checks import CHECKS  # noqa: E402
from validate import load, validate  # noqa: E402

REPO = os.environ.get("GITHUB_REPOSITORY", "sipico/global-test-data")
BRANCH = os.environ.get("TESTDATA_BRANCH", "main")
REPO_URL = f"https://github.com/{REPO}"
BLOB = f"{REPO_URL}/blob/{BRANCH}"
TITLE = "Global Test Data"
TAGLINE = "Country-specific example data that passes validation but belongs to no one."

REGIONS = ["Global", "Europe", "Africa", "Asia", "North America", "Latin America", "Oceania"]
CATEGORIES = [
    ("organisation", "Organisation", "Company and tax identifiers, names, e-invoicing addresses"),
    ("address", "Address", "Postal addresses, postcodes, towns"),
    ("contact", "Contact", "Telephone numbers, email addresses, domains"),
    ("banking", "Banking", "IBAN, account numbers, bank codes, BIC"),
    ("trade", "Trade & logistics", "Location numbers, customs, transport codes"),
    ("person", "Person", "Personal identifiers for consumer examples"),
    ("document", "Documents", "Specimen documents, document numbers, test texts"),
    ("other", "Other", "Everything else"),
]
STATUS = {
    "reserved": ("Reserved", "An authority formally reserves this value or range for fiction, examples or tests."),
    "published-example": ("Official example", "Published by an authority in its own examples. The Checks column shows whether it passes validation."),
    "derived": ("Derived", "Built from the official format rules and checked to be unassigned."),
    "avoid": ("Avoid", "Circulates as an example but belongs to a real entity or fails validation."),
}

e = html.escape




def issue_url(country=""):
    q = {"template": "suggest-data.yml", "title": f"[{country or 'XX'}] "}
    if country:
        q["country"] = country
    return f"{REPO_URL}/issues/new?" + urllib.parse.urlencode(q)


def flag(code):
    if code == "GLOBAL":
        return "🌐"
    return "".join(chr(0x1F1E6 + ord(c) - 65) for c in code)


def slug(code):
    return code.lower()


def page(title, body, depth, active=""):
    up = "../" * depth
    nav = [("Directory", f"{up}index.html", "home"),
           ("Contribute", f"{up}contribute/index.html", "contribute"),
           ("Download", f"{up}index.html#download", "download"),
           ("GitHub", f"{REPO_URL}/tree/{BRANCH}", "gh")]
    links = "".join(
        f'<a href="{href}"{" aria-current=page" if key == active else ""}>{e(label)}</a>'
        for label, href, key in nav)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(TAGLINE)}">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="site-head"><div class="wrap">
<a class="brand" href="{up}index.html"><span class="mark" aria-hidden="true">◇</span> {e(TITLE)}</a>
<nav>{links}</nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-foot"><div class="wrap">
<p>Data: <a href="{BLOB}/LICENSE">CC0 1.0</a> — free to copy into tests and documentation.
Every value cites its source. Values are believed not to belong to any real person or
organisation; check before relying on one, and <a href="{REPO_URL}/issues">report problems</a>.</p>
</div></footer>
<script src="{up}assets/app.js"></script>
</body>
</html>
"""


def badge(status):
    label = STATUS[status][0]
    return f'<span class="badge s-{status}" title="{e(STATUS[status][1])}">{e(label)}</span>'


def counts(entries):
    c = {k: 0 for k in STATUS}
    for x in entries:
        c[x["status"]] += 1
    return c


def sources_html(sources):
    items = []
    for s in sources:
        pub = f' <span class="muted">— {e(s["publisher"])}</span>' if s.get("publisher") else ""
        items.append(f'<li><a href="{e(s["url"])}" rel="noopener">{e(s["title"])}</a>{pub}</li>')
    return f'<ul class="src">{"".join(items)}</ul>'


def checks_html(x):
    out = []
    for c in x.get("checks", []) or []:
        desc = CHECKS[c][1] if c in CHECKS else c
        out.append(f'<span class="chk ok" title="{e(desc)}">✓ {e(c)}</span>')
    for c in x.get("fails_checks", []) or []:
        desc = CHECKS[c][1] if c in CHECKS else c
        out.append(f'<span class="chk bad" title="{e(desc)}">✗ {e(c)}</span>')
    for v in x.get("verified", []) or []:
        out.append(f'<span class="chk ver">✓ {e(v)}</span>')
    return "".join(out) or '<span class="muted">—</span>'


def entry_row(x):
    kind = x.get("kind", "value")
    copy = "" if kind != "value" or x["status"] == "avoid" else (
        f'<button class="copy" type="button" data-copy="{e(x["value"])}" '
        f'aria-label="Copy {e(x["value"])}">Copy</button>')
    notes = f'<p class="note">{e(x["notes"])}</p>' if x.get("notes") else ""
    reason = f'<p class="note warn">{e(x["reason"])}</p>' if x.get("reason") else ""
    ubl = "".join(f"<code>{e(u)}</code>" for u in x.get("ubl", []) or [])
    kind_tag = f' <span class="kind">{e(kind)}</span>' if kind != "value" else ""
    return f"""<tr id="{e(x['id'])}" data-status="{e(x['status'])}">
<td class="val"><div class="v"><code>{e(x['value'])}</code>{copy}</div><div class="type">{e(x['type'])}{kind_tag}</div></td>
<td class="what"><p>{e(x['label'])}</p>{reason}{notes}</td>
<td>{badge(x['status'])}</td>
<td class="checks">{checks_html(x)}</td>
<td>{sources_html(x['sources'])}</td>
<td class="ubl">{ubl or '<span class="muted">—</span>'}</td>
</tr>"""


def table(entries):
    rows = "\n".join(entry_row(x) for x in entries)
    return f"""<div class="tbl"><table>
<thead><tr><th>Value</th><th>What it is</th><th>Status</th><th>Checks</th><th>Source</th><th>UBL</th></tr></thead>
<tbody>
{rows}
</tbody></table></div>"""


def country_page(doc):
    code = doc["code"]
    entries = doc["entries"]
    usable = [x for x in entries if x["status"] != "avoid"]
    avoid = [x for x in entries if x["status"] == "avoid"]
    c = counts(entries)
    parts = []
    native = doc.get("native_name")
    native_html = f' <span class="native">{e(native)}</span>' if native and native != doc["name"] else ""
    research = ""
    if doc.get("research"):
        research = f'<a href="{BLOB}/{e(doc["research"])}">Research notes</a> · '
    langs = ", ".join(doc.get("languages", []) or [])
    parts.append(f"""<nav class="crumbs"><a href="../index.html">Directory</a> › {e(doc['region'])}</nav>
<section class="hero country">
<h1><span class="flag" aria-hidden="true">{flag(code)}</span> {e(doc['name'])}{native_html}</h1>
<p class="lede">{e(doc['summary'].strip())}</p>
<p class="meta">Updated {e(doc['updated'])}{' · searched in ' + e(langs) if langs else ''} ·
{research}<a href="{BLOB}/data/{slug(code)}.yaml">Data file</a> ·
<a href="../data/{slug(code)}.json">JSON</a></p>
<div class="stats">{''.join(f'<span class="stat s-{k}"><b>{v}</b> {e(STATUS[k][0])}</span>' for k, v in c.items() if v)}</div>
</section>""")
    parts.append("""<div class="filters" role="group" aria-label="Filter by status">
<span>Show:</span>
""" + "".join(
        f'<label class="chip s-{k}"><input type="checkbox" data-filter="{k}" checked> {e(v[0])}</label>'
        for k, v in STATUS.items() if k != "avoid" and c[k]) + "</div>")
    for key, label, desc in CATEGORIES:
        rows = [x for x in usable if x["category"] == key]
        if not rows:
            continue
        parts.append(f'<section class="cat" id="{key}"><h2>{e(label)} <span class="count">{len(rows)}</span></h2>'
                     f'<p class="muted">{e(desc)}</p>{table(rows)}</section>')
    idents = doc.get("identifiers") or []
    if idents:
        rows = []
        for i in idents:
            chk = i.get("check")
            chk_html = f'<code title="{e(CHECKS[chk][1])}">{e(chk)}</code>' if chk in CHECKS else '<span class="muted">—</span>'
            notes = f'<p class="note">{e(i["notes"])}</p>' if i.get("notes") else ""
            ubl = "".join(f"<code>{e(u)}</code>" for u in i.get("ubl", []) or [])
            rows.append(f"<tr><td><b>{e(i['name'])}</b>{notes}</td><td>{e(i['format'])}</td>"
                        f"<td>{chk_html}</td><td>{e(i.get('authority', ''))}</td>"
                        f"<td class='ubl'>{ubl or '<span class=muted>—</span>'}</td></tr>")
        parts.append(f"""<section class="cat" id="identifiers"><h2>Identifier rules</h2>
<p class="muted">Formats and check algorithms. Validators live in <a href="{BLOB}/tools/checks.py">tools/checks.py</a>.</p>
<div class="tbl"><table><thead><tr><th>Identifier</th><th>Format</th><th>Validator</th><th>Authority</th><th>UBL</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div></section>""")
    if avoid:
        parts.append(f"""<section class="cat avoid" id="avoid"><h2>Do not use <span class="count">{len(avoid)}</span></h2>
<p class="muted">These values circulate as "examples" but belong to real organisations or people, or fail validation.</p>
{table(avoid)}</section>""")
    parts.append(f"""<section class="suggest"><h2>Know a better source?</h2>
<p>Suggest a value for {e(doc['name'])} with its official source:
<a href="{e(issue_url(code))}">open an issue</a> or
<a href="{BLOB}/CONTRIBUTING.md">send a pull request</a>.</p></section>""")
    return page(f"{doc['name']} — {TITLE}", "\n".join(parts), 1)


def index_page(docs):
    total = sum(len(d["entries"]) for d in docs)
    usable = sum(1 for d in docs for x in d["entries"] if x["status"] != "avoid")
    avoid = total - usable
    countries = sum(1 for d in docs if d["code"] != "GLOBAL")
    groups = []
    for region in REGIONS:
        ds = sorted([d for d in docs if d["region"] == region], key=lambda d: d["name"])
        if not ds:
            continue
        cards = []
        for d in ds:
            c = counts(d["entries"])
            n_use = len(d["entries"]) - c["avoid"]
            cats = sorted({x["category"] for x in d["entries"] if x["status"] != "avoid"},
                          key=[k for k, _, _ in CATEGORIES].index)
            cat_labels = " · ".join(dict((k, l) for k, l, _ in CATEGORIES)[k] for k in cats)
            cards.append(f"""<a class="card" href="{slug(d['code'])}/index.html">
<span class="flag" aria-hidden="true">{flag(d['code'])}</span>
<span class="cname">{e(d['name'])}</span>
<span class="cnum"><b>{n_use}</b> usable · {c['avoid']} to avoid</span>
<span class="ccats">{e(cat_labels)}</span>
</a>""")
        groups.append(f'<section class="region"><h2>{e(region)}</h2><div class="cards">{"".join(cards)}</div></section>')
    legend = "".join(f"<li>{badge(k)} {e(v[1])}</li>" for k, v in STATUS.items())
    body = f"""<section class="hero">
<h1>{e(TITLE)}</h1>
<p class="lede">{e(TAGLINE)} Company and tax numbers, addresses, phone numbers, bank details
and more — for documentation, tests and sample documents, without the risk of hitting a real
company or person. Every value cites an official source.</p>
<div class="stats"><span class="stat"><b>{countries}</b> countries</span>
<span class="stat"><b>{usable}</b> usable values</span>
<span class="stat s-avoid"><b>{avoid}</b> traps to avoid</span></div>
</section>
<section class="search-box">
<label for="q">Search all values</label>
<input id="q" type="search" placeholder="e.g. VAT, IBAN, phone, postcode, 952…" autocomplete="off">
<div id="results" class="results" hidden></div>
</section>
{''.join(groups)}
<section class="legend"><h2>What the statuses mean</h2><ul>{legend}</ul>
<p class="muted">Only values that are reserved, official examples or derived-and-checked are offered for use.
Unverified findings stay in the research notes.</p></section>
<section id="download" class="legend"><h2>Download</h2>
<p><a href="data/all.json">all.json</a> · <a href="data/all.csv">all.csv</a> · one JSON file per country
(linked on each country page). Source data: <a href="{REPO_URL}/tree/{BRANCH}/data">YAML files on GitHub</a>.</p></section>"""
    return page(TITLE, body, 0, "home")


def contribute_page():
    body = f"""<section class="hero"><h1>Contribute</h1>
<p class="lede">The data set grows through pull requests. A value is accepted only with a source
that shows it is reserved or published for examples, or with a documented check that it is unassigned.</p></section>
<section class="prose">
<h2>What qualifies</h2>
<ul>
<li><b>Reserved</b> — a regulator, registry or standard formally reserves the value or range (e.g. phone numbers for drama, GS1 prefix 952).</li>
<li><b>Official example</b> — an authority uses the value in its own published examples, and it passes the official format and check rules.</li>
<li><b>Derived</b> — built from the official rules and checked against the official register to be unassigned. State which register and the date.</li>
<li><b>Avoid</b> — a value that circulates as an "example" but belongs to a real entity or fails validation. These warnings are just as valuable.</li>
</ul>
<h2>How</h2>
<ol>
<li>Edit or add <code>data/&lt;country&gt;.yaml</code> (copy the structure of <a href="{BLOB}/data/fr.yaml">fr.yaml</a>; schema in <a href="{BLOB}/schema/country.schema.json">schema/country.schema.json</a>).</li>
<li>Give every entry at least one source with a URL, preferably the authority's own page or document.</li>
<li>List the validators the value must pass under <code>checks</code>. Add a validator to <a href="{BLOB}/tools/checks.py">tools/checks.py</a> if the identifier type is new.</li>
<li>Run <code>pip install pyyaml jsonschema</code> and <code>python tools/validate.py</code> — it must report 0 errors. The pull request runs the same check.</li>
<li>Open a pull request. No code? <a href="{e(issue_url())}">Suggest a value in an issue</a> instead.</li>
</ol>
<p>Full guide: <a href="{BLOB}/CONTRIBUTING.md">CONTRIBUTING.md</a>. Contributions are published under CC0 1.0.</p>
</section>"""
    return page(f"Contribute — {TITLE}", body, 1, "contribute")


def build(out):
    paths = sorted((ROOT / "data").glob("*.yaml"))
    errors, _, _ = validate(paths)
    if errors:
        for err in errors:
            print("ERROR", err)
        sys.exit("Validation failed; site not built.")
    docs = [load(p) for p in paths]
    if out.exists():
        shutil.rmtree(out)
    (out / "data").mkdir(parents=True)
    shutil.copytree(ROOT / "site" / "assets", out / "assets")
    (out / "index.html").write_text(index_page(docs), encoding="utf-8")
    (out / "contribute").mkdir()
    (out / "contribute" / "index.html").write_text(contribute_page(), encoding="utf-8")
    flat = []
    for d in docs:
        dirp = out / slug(d["code"])
        dirp.mkdir()
        (dirp / "index.html").write_text(country_page(d), encoding="utf-8")
        (out / "data" / f"{slug(d['code'])}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        for x in d["entries"]:
            flat.append({"country": d["code"], "country_name": d["name"], **x})
    (out / "data" / "all.json").write_text(json.dumps(flat, ensure_ascii=False), encoding="utf-8")
    buf = io.StringIO()
    cols = ["country", "id", "category", "type", "value", "kind", "label", "status",
            "checks", "verified", "reason", "notes", "ubl", "source_urls"]
    w = csv.writer(buf)
    w.writerow(cols)
    for x in flat:
        w.writerow([x["country"], x["id"], x["category"], x["type"], x["value"], x.get("kind", "value"),
                    x["label"], x["status"], " ".join(x.get("checks", []) or []),
                    " | ".join(x.get("verified", []) or []), x.get("reason", ""), x.get("notes", ""),
                    " | ".join(x.get("ubl", []) or []), " ".join(s["url"] for s in x["sources"])])
    (out / "data" / "all.csv").write_text(buf.getvalue(), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(docs)} pages, {len(flat)} entries into {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    build(pathlib.Path(ap.parse_args().out).resolve())
