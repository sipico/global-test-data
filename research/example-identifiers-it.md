# Fictitious-but-valid example identifiers — Italy

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with Italian- and English-language queries. Checks marked ✅
were run during research: Partita IVA check digit (Luhn), lookup in the EU VAT
service VIES (REST API), lookup in the IndicePA e-invoicing office list (open data,
56,383 office codes), and lookup in the ISTAT list of municipalities (7,889 names).

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:** unlike France, Italy has **no official source of fictitious identifiers
that also pass validation**. The tax agency's own examples use deliberately invalid
VAT numbers, and the Treasury's UBL order examples use real public bodies.

---

## 1. Official example files

### 1.1 Agenzia delle Entrate — FatturaPA examples (national XML format, not UBL)

Six files on [fatturapa.gov.it](https://www.fatturapa.gov.it/it/norme-e-regole/documentazione-fattura-elettronica/formato-fatturapa/)
(`IT01234567890_FPA01..03.xml`, `IT01234567890_FPR01..03.xml`).

| Element | Value | Status | Checks |
|---|---|---|---|
| Partita IVA (supplier) | `01234567890` | Published example | ❌ check digit wrong · ❌ not in VIES |
| Partita IVA (other party) | `24681012141` | Published example | ❌ check digit wrong · ❌ not in VIES |
| Codice fiscale (customer) | `09876543210` | Published example | ❌ check digit wrong · ❌ not in VIES |
| Names | `SOCIETA' ALPHA SRL`, `ALPHA SRL`, `AMMINISTRAZIONE BETA`, `BETA GAMMA`, `DITTA BETA`, `Trasporto spa` | Published example | — |
| Addresses | `VIALE ROMA 543` 07100 SASSARI SS; `VIA TORINO 38-B` 00145 ROMA RM | Published example | Real CAP/town/province combinations |
| CodiceDestinatario | `AAAAAA` (PA office), `ABC1234` (private) | Published example | ✅ `AAAAAA` not in IndicePA |
| PEC | `betagamma@pec.it` | **Avoid** | `pec.it` is a real commercial PEC provider domain |

`IT01234567890` is the most-copied Italian "example VAT number", but it fails the check
digit and the SDI exchange system (which checks the tax registry) would reject it.

Reserved CodiceDestinatario values, defined in the FatturaPA technical specification
v1.4 (these have a real meaning, they are not test values):

| Value | Meaning |
|---|---|
| `0000000` | Recipient receives via PEC, or has no registered channel (consumers, flat-rate taxpayers) |
| `XXXXXXX` | Recipient not resident in Italy (cross-border invoice) |

### 1.2 MEF / RGS — NSO (Nodo di Smistamento degli Ordini) UBL examples

The national hub for public-sector purchase orders accepts only **UBL 2.1 Peppol BIS
Ordering 3** messages. The Ragioneria Generale dello Stato publishes
[*NSO – File di esempio*](https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/acquisti_pubblici_in_rete_apir/nodo_di_smistamento_degli_ordini_di_acquisto_delle_amministrazioni_pubbliche_nso/)
(ZIP, 19 files): Order, OrderResponse, OrderAgreement, SBDH envelopes and an invoice,
for three flows (simple, complete, pre-agreed ordering).

**These examples use real organisations — Avoid as party data**:

| Element | Value | Reality |
|---|---|---|
| Buyer | `Ministero dell'economia e delle finanze`, VAT `IT80415740580` | Real (MEF tax code 80415740580) |
| Supplier | `Sogei - Società Generale d'Informatica S.p.A.`, `IT01043931003` | Real; ✅ valid check digit |
| Other party | `Consip`, `IT05359681003` | Real; ✅ valid check digit |
| IPA office code (`schemeID="0201"`) | `M0E2RI` | ✅ Real MEF office in IndicePA (Largo Santa Susanna 13, 00187 Roma) |
| IPA office code | `B9BGAQ` | Not in the current IndicePA e-invoicing list |
| People / emails | `Paolo Trimarchi`, `paolo.trimarchi@mef.gov.it`, `francesco@sogei.it`, `hd@consip.it` | Real-looking personal data |

Still useful as a **structural** reference for Italian UBL (NSO order ID convention
`<ID>#<IssueDate>#<EndpointID>[#Revised|#Cancelled]`, SBDH usage, the scheme IDs below,
and placeholder GLNs `7400000001235` / `7560000012345`, `schemeID="0160"`).

---

## 2. Company and person identifiers

| Identifier | Rule | Notes |
|---|---|---|
| Partita IVA | 11 digits: 7-digit serial + 3-digit office code + Luhn check digit | Office code `001`–`100` (province, ≈ ISTAT province code, e.g. `058` Rome, `015` Milan, `001` Turin) or special codes `120`, `121`, `888`, `999` |
| VAT number (EN16931 / UBL) | `IT` + Partita IVA | |
| Codice fiscale (company) | Same 11 digits as the Partita IVA | |
| Codice fiscale (person) | 16 characters: surname + name + birth date/sex + birthplace code + check letter (D.M. 23/12/1976) | |
| Peppol schemes | `0201` = IPA office code (Codice Univoco Ufficio), `0210` = codice fiscale, `0211` = Partita IVA | `0201` and `0211` seen in the NSO examples |
| IPA office code | 6 alphanumeric characters | Public bodies only |
| REA number | `<province>-<number>`, e.g. `RM-1234567` | Chamber of Commerce economic and administrative register |

### 2.1 Derived Partita IVA candidates

Built with a valid office code and check digit, then checked in VIES:

| Candidate | Office code | Check digit | VIES |
|---|---|---|---|
| `00000010587` | 058 Rome | ✅ | ✅ not registered |
| `00000020586` | 058 Rome | ✅ | ✅ not registered |
| `00000010157` | 015 Milan | ✅ | ✅ not registered |
| `00000010017` | 001 Turin | ✅ | ✅ not registered |
| `11111110588` | 058 Rome | ✅ | ✅ not registered |

Limitation: VIES only lists numbers enabled for intra-EU trade. A number missing from
VIES could still be a purely domestic Partita IVA. Before use, check each candidate with
the Agenzia delle Entrate's
[*Verifica partita IVA*](https://telematici.agenziaentrate.gov.it/VerificaPIVA/Scegli.do?parameter=verificaPiva)
service (manual, with captcha; not done in this session).

### 2.2 Personal codice fiscale — Avoid the textbook example

`RSSMRA80A01H501U` (Mario Rossi, born in Rome on 1 January 1980) is the standard worked
example on calculator sites, but Mario Rossi is the most common name in Italy, so this
code may well belong to a real person. No official fictitious codice fiscale was found.
For the Consumer party, prefer a company or omit the personal tax code. Building
fictitious codes (e.g. from an unused birthplace code) is an open question.

---

## 3. Bank identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| IBAN | `IT60 X054 2811 1010 0000 0123 456` | Published example | SWIFT IBAN Registry, Italy entry; ✅ mod-97. Bank code (ABI) `05428` is a real bank code |
| BIC | 8th character `0` (e.g. `XXXXITM0`) | Reserved (convention) | ISO 9362 test BIC |

---

## 4. Telephone numbers

**No reserved fictional range found.** Searches in Italian and English of AGCOM
material (national numbering plan, delibera 8/15/CIR and later updates incl. 21/26/CIR)
found no equivalent of France's ARCEP or the UK's Ofcom drama numbers.

Recommendation: do not invent Italian numbers. Either leave telephone elements out,
use an obvious placeholder that fails validation, or point to a reserved number in
another country for a foreign contact (e.g. France `+33 1 99 00 xx xx`).

---

## 5. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com/.net/.org` | Reserved | RFC 2606 / RFC 6761 |
| `pec.it`, `legalmail.it`, `pec.sogei.it`, etc. | **Avoid** | Real PEC (certified email) provider domains |

No reserved PEC test domain was found. PEC addresses (`EndpointID` / `ElectronicMail`)
should use a `.test` domain, e.g. `fatture@<alias>.pec.test`.

---

## 6. Postal addresses

### 6.1 What Poste Italiane publishes

**No fictitious town or postcode (CAP) found.** Like La Poste, Poste Italiane's
material uses real places:

| Source | Example |
|---|---|
| [poste.it/cap](https://www.poste.it/cap) (merged municipalities) | `SIG. MARIO ROSSI` / `VIA ROMA CAMAIRAGO 8` / `26844 CASTELGERUNDO`; `SIG. GIUSEPPE BIANCHI` / `VIA ROMA CAVACURTA 8` / `26844 CASTELGERUNDO` |
| Poste Italiane [CAP FAQ](https://business.poste.it/business/files/1473808238165/banchedati-faq-cap.pdf) | Street-specific CAP: via Velia 84, Salerno → `84135` (not the general `84122`) |
| [it.wikipedia *Indirizzo*](https://it.wikipedia.org/wiki/Indirizzo) | `PAOLO VERDI` / `DITTA FLEX S.R.L.` / `SCALA A INTERNO 4` / `VIA GIOACCHINO ROSSINI 40` / `84011 AMALFI SA` |
| FatturaPA examples (§1.1) | `VIALE ROMA 543` 07100 SASSARI SS; `VIA TORINO 38-B` 00145 ROMA RM |

Rules (Poste Italiane): 3–5 lines; last line = `CAP TOWN PROVINCE` (province as a
2-letter code without brackets); capitals recommended; no punctuation, no comma or "N."
before the house number (exception `10/B`); street-specific CAP in cities with several
postal zones.

### 6.2 Postcode (CAP) coverage

There is **no official open CAP dataset**: Poste Italiane sells it, and the ISTAT list
of municipalities has no CAP. Checked against the community dataset
[matteocontrini/comuni-json](https://github.com/matteocontrini/comuni-json) (2020,
4,678 CAPs, `00010`–`98168`, completeness not guaranteed):

| Finding | Status |
|---|---|
| First two digits `49`, `68`, `69`, `77`, `78`, `79`, `99` not used | Derived, unofficial dataset |
| `00000`, `00100`, `12345`, `99999` not used | Derived; `00100` is the old pre-1999 general Rome CAP, still often seen |
| `00120` = Vatican City, `47890`–`47899` = San Marino | Inside the Italian CAP system but **not Italy**, so avoid |

### 6.3 Town names checked against ISTAT

Official ISTAT *Elenco comuni italiani* (updated 2026-02-21), 7,889 names:

| Name | Real municipality? | Status |
|---|---|---|
| `PAESE` ("village") | **Yes** (Paese, province of Treviso) | **Avoid** as a placeholder, like `VILLE` in France |
| `CANICATTÌ`, `ROCCASECCA`, `CAPRACOTTA`, `PIZZO`, `FORTEZZA` | **Yes** | Avoid. Canicattì is used jokingly as "the middle of nowhere" but is real |
| `ROCCACANNUCCIA`, `VATTELAPESCA` | No | Derived; recognisable Italian joke placeholder names |
| `ESEMPIO`, `CITTÀ`, `MOLTO LONTANO` | No | Derived |
| `PAPEROPOLI`, `TOPOLINIA` | No | **Avoid** anyway: Disney's Duckburg and Mouseton (trademark) |

### 6.4 Address strategy

Same options as France (`example-identifiers-fr.md` §5.4). Only a real CAP + real
municipality + invented street passes full validation; check street names against
OpenStreetMap or the national street register (ANNCSU), since the street directory
from Poste Italiane is not open.

---

## 7. Other identifiers

| Element | Value / range | Status | Source |
|---|---|---|---|
| GLN / GTIN (`schemeID="0088"`) | GS1 prefix `952` | Reserved | GS1 General Specifications (see France file §6) |
| GLN (`schemeID="0160"`) | `7400000001235`, `7560000012345` | Published example (NSO) | Unverified ownership; prefer `952` |

---

## 8. Avoid list

| Value | Seen as | Why |
|---|---|---|
| `01234567890`, `09876543210`, `24681012141` | Agenzia delle Entrate examples | Fail the Partita IVA check digit |
| `IT80415740580`, `IT01043931003`, `IT05359681003` | NSO examples | Real: MEF, Sogei, Consip |
| `M0E2RI` | NSO example IPA office code | Real MEF office |
| `paolo.trimarchi@mef.gov.it`, `francesco@sogei.it`, `hd@consip.it` | NSO examples | Real-looking personal/organisational emails |
| `betagamma@pec.it` | FatturaPA example | Real PEC provider domain |
| `RSSMRA80A01H501U` | "Example codice fiscale" | Probably belongs to a real person |
| `PAESE`, `CANICATTÌ` | Placeholder town names | Real municipalities |
| `PAPEROPOLI`, `TOPOLINIA` | Placeholder town names | Disney trademark |
| `00120`, `4789x` | CAP | Vatican City / San Marino |

---

## 9. Sources

- Agenzia delle Entrate / SdI: [Formato FatturaPA (examples, XSD, specs)](https://www.fatturapa.gov.it/it/norme-e-regole/documentazione-fattura-elettronica/formato-fatturapa/) · [Specifiche tecniche v1.4](https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.4/Specifiche_tecniche_del_formato_FatturaPA_V1.4.pdf) · [Verifica partita IVA](https://telematici.agenziaentrate.gov.it/VerificaPIVA/Scegli.do?parameter=verificaPiva)
- MEF / RGS: [NSO page](https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/acquisti_pubblici_in_rete_apir/nodo_di_smistamento_degli_ordini_di_acquisto_delle_amministrazioni_pubbliche_nso/) · [NSO – File di esempio (ZIP)](https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/e-GOVERNME1/apir/NSO-File-di-esempio.zip)
- AgID: [IndicePA open data — servizi di fatturazione elettronica](https://indicepa.gov.it/ipa-dati/dataset/servizi-fatturazione-elettronica)
- EU: [VIES](https://ec.europa.eu/taxation_customs/vies/)
- ISTAT: [Codici dei comuni](https://www.istat.it/classificazione/codici-dei-comuni-delle-province-e-delle-regioni/) · [Elenco comuni italiani (xlsx)](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.xlsx)
- Poste Italiane: [CAP](https://www.poste.it/cap) · [FAQ banche dati CAP](https://business.poste.it/business/files/1473808238165/banchedati-faq-cap.pdf)
- AGCOM: [Piano di numerazione](https://www.agcom.it/competenze/comunicazioni-elettroniche/reti/numerazione/piano-di-numerazione) · [Delibera 21/26/CIR](https://www.agcom.it/sites/default/files/provvedimenti/delibera/2026/Delibera%2021-26-CIR.pdf)
- SWIFT: [IBAN Registry](https://www.swift.com/resource/iban-registry-pdf)
- Partita IVA structure (secondary): [Fiscozen](https://www.fiscozen.it/guide/composizione-partita-iva/) · [Morfoedro](https://morfoedro.art/it/articolo/221)
- Community CAP dataset: [matteocontrini/comuni-json](https://github.com/matteocontrini/comuni-json)
