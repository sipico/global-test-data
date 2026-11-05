# Fictitious-but-valid example identifiers — France

**Purpose:** collect identifiers, addresses and contact data that (a) pass format and
checksum validation, (b) are published or reserved by an official or authoritative
body for examples/tests, and (c) cannot be confused with a real organisation. These
feed the canonical 26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05. Checks marked ✅ were run during research (Luhn, VAT key,
IBAN mod-97, lookup in the national company register via
`recherche-entreprises.api.gouv.fr`, lookup in La Poste's official postcode file).

Legend for the **Status** column:

| Status | Meaning |
|---|---|
| **Reserved** | An authority formally reserves the value/range for fiction, examples or tests |
| **Published example** | An authority uses the value in its own official examples, not formally reserved |
| **Derived** | Not published anywhere; computed by us from the format rules and checked to be unused |
| **Avoid** | Seen as an "example" somewhere but belongs to a real entity or fails validation |

---

## 1. Company identifiers (SIREN / SIRET / VAT / routing)

### 1.1 Primary source: FNFE-MPE official example invoices

FNFE-MPE (Forum National de la Facture Électronique et des Marchés Publics
Électroniques) publishes the validation artefacts of the French e-invoicing standard
(AFNOR XP Z12-012 / Z12-014) in
[`fnfempe/France_RFE`](https://github.com/fnfempe/France_RFE) (Apache 2.0, last
commit 2026-09-05). Folder `FNFE_RFE_INVOICE/Z.example/TEST/` contains ~100 example
files: 13 **UBL 2.1** invoices (EN16931 and EXTENDED-CTC-FR profiles), CII invoices,
and CDAR lifecycle status messages.

| Element | Value | Status | Checks |
|---|---|---|---|
| SIREN (seller) | `100000009` | Published example | ✅ Luhn · ✅ not in register |
| SIREN (buyer) | `200000008` | Published example | ✅ Luhn · ✅ not in register |
| SIREN (3rd party, multi-vendor case) | `111111118` | Published example | ✅ Luhn · ✅ not in register |
| SIRET | `11111111800019` | Published example | ✅ Luhn |
| VAT | `FR88100000009`, `FR37200000008`, `FR44111111118` | Published example | ✅ VAT key correct |
| Electronic address, scheme `0225` | `100000009`, `100000009_STATUTS`, `100000009_AUTOFACT`, `200000008` | Published example | — |
| SIREN in UBL | `cbc:CompanyID schemeID="0002"`, `cbc:EndpointID schemeID="0225"` | Published example | — |
| IBAN | `FR20 1254 2547 2569 8542 5874 698` | Published example | ✅ mod-97 |
| BIC | `BIC_MONCOMPTE` | Placeholder | ❌ not a valid BIC format |
| GLN (`schemeID="0088"`) | `3654789851`, `587451236587` | Placeholder | ❌ not 13 digits |
| Names | `LE VENDEUR`, `LE CLIENT`, `VENDEUR XXX`, `AGRI1`, `COOP1` | Published example | — |

Defects in the FNFE-MPE set (do not copy): VAT `FR37288100000008` (typo, wrong
length), the phone numbers `01 02 03 54 87` / `01 01 25 45 87` (not in the reserved
ARCEP range, see §3), and the email domains `vendeur.fr` / `acheteur.fr` (registered
by private parties, see §4).

### 1.2 Other sources checked

| Source | What it uses | Notes |
|---|---|---|
| DGFiP *Dossier de spécifications externes* v3.2 (2026-04-30) | "SIRET 123 456 789 000001" in prose | ❌ fails Luhn — deliberately invalid |
| DGFiP v2.4 examples (directory flows F12–F14) | SIREN `000000001`, SIRET `00000000100001`, "Unité Légale 1" | ❌ fails Luhn; address `10 Rue du Centre 93160 Noisy-le-Grand` is a real public-sector address |
| DGFiP v3.1 / v3.2 packages | — | No example XML files any more |
| Chorus Pro qualification portal | Test SIRETs (seen starting `882…`) | Generated per user account ("matelas de données"); not stable or reusable |
| [Cabinet Digital](https://www.cabinetdigital.fr/facture-electronique/exemples-de-factures/) (private, CC BY 4.0) | Same SIRENs as FNFE-MPE, `ATELIER EXEMPLE SAS`, `CLIENT EXEMPLE SARL`, `.test` emails, `DE811234567` / `BEISPIEL GMBH`, `EXEMPLE SA` (Geneva) | Secondary source; 22 UBL/CII files incl. credit note, reverse charge, intra-EU, export, currency, SEPA direct debit |

### 1.3 Derivation rules (to build more identifiers)

| Identifier | Rule |
|---|---|
| SIREN | 9 digits, Luhn check on all 9 |
| SIRET | SIREN + 5-digit establishment number (NIC), Luhn check on all 14 |
| VAT (TVA intracommunautaire) | `FR` + key + SIREN, key = `(12 + 3 × (SIREN mod 97)) mod 97`, 2 digits |
| EORI | `FR` + SIRET (or SIREN) |
| RCS mention | `RCS <town of registry court> <SIREN>`, e.g. `RCS Paris 100 000 009` |
| Peppol / EN16931 schemes | `0002` = SIREN, `0009` = SIRET, `0225` = French CTC electronic address |

The FNFE-MPE convention "leading digit + zeros + Luhn digit" (`d00000000c`, check
digit `c = (10 − d) mod 10`) gives only nine numbers (`100000009` … `900000001`).
The 26 + C party set needs a wider pattern, and **every candidate must be checked
against the register** before use. A made-up SIREN gives a VAT number that passes
syntax validation but fails a live VIES lookup, which is the desired behaviour.

---

## 2. Bank identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| IBAN | `FR14 2004 1010 0505 0001 3M02 606` | Published example | SWIFT IBAN Registry (ISO 13616 Registration Authority), France entry; ✅ mod-97 |
| BIC | 8th character `0` (e.g. `XXXXFRP0`) | Reserved (convention) | ISO 9362: second character of the location code = `0` marks a test BIC |

Caveat: French bank codes cannot be fictitious and still pass national validation.
`20041` (registry example) is La Banque Postale; `30006` in the widely copied
`FR76 3000 6000 0112 3456 7890 189` is Crédit Agricole. The account part is what
makes these examples fictitious.

---

## 3. Telephone numbers

| Range | Region | Status |
|---|---|---|
| `01 99 00 xx xx` | Île-de-France | Reserved |
| `02 61 91 xx xx` | North-West, La Réunion, Mayotte | Reserved |
| `03 53 01 xx xx` | North-East | Reserved |
| `04 65 71 xx xx` | South-East | Reserved |
| `05 36 49 xx xx` | South-West | Reserved |
| `06 39 98 xx xx` | Mobile | Reserved |

Source: ARCEP national numbering plan, art. 2.5.12 "Numéros pour œuvres
audiovisuelles" (decision 2018-0881, amended by 2021-0532). Never assigned to an end
user and cannot be called; no authorisation needed. International format:
`+33 1 99 00 xx xx`. Note: libphonenumber 9.0.37 reportedly rejects the `06 39 98`
mobile range.

---

## 4. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com`, `example.net`, `example.org` | Reserved | RFC 2606 / RFC 6761 |
| `vendeur.fr`, `acheteur.fr`, `exemple.fr`, `example.fr` | **Avoid** | All registered by private parties (DNS NS records checked) |

Recommendation: `facturation@<party-alias>.test` or `<role>@example.com`.

---

## 5. Postal addresses

### 5.1 What La Poste and the UPU publish

**There is no official fictitious town name or postcode in France.** Nothing was found
in La Poste, AFNOR or UPU material that reserves one (searched in French and
English). The official pattern is **fictitious people and companies at real
communes**:

| Source | Example address |
|---|---|
| La Poste SP 8855 vol. 2 v1.11 *Adressage des plis* (applies NF Z10-011), private person | `Monsieur Jean DELORME` / `Appartement 2` / `ENTREE A BATIMENT JONQUILLE` / `25 RUE DE L'EGLISE` / `CAUDOS` / `33380 MIOS` |
| La Poste SP 8855, company | `Société DUPONT` / `Monsieur Martin Service Achats` / `ZONE INDUSTRIELLE OUEST` / `35 IMPASSE DES GABARRES` / `BP 18 ARVEYRES` / `33506 LIBOURNE CEDEX` |
| UPU *Postal addressing systems — France* (09/2011) | `Société DUPONT` / `Mademoiselle Lucie MARTIN` / `Résidence les Capucines` / `56 RUE EMILE ZOLA` / `BP 90432 MONTFERRIER SUR LEZ` / `34092 MONTPELLIER CEDEX 5`; also `Monsieur Jean DURAND` at `33380 MIOS`, `DURAND SA` |
| Colissimo shipping web service spec (2021-12) | Placeholder strings (`companyName`, `lastName`, `line0`…`line3`, `mon adresse`) with real postcodes/cities (`75007 Paris`, `35000`, Rome `00121`); also `test@email.com` |
| FNFE-MPE (§1.1) | `35 rue d'ici`, `55 avenue de là-bas`, `12 impasse plus loin`, `ligne 2 vendeur`; town `MA VILLE` with real postcode `06000`; `PARIS 75018` |

The Colissimo spec also contains a real La Poste employee email address — do not copy.

### 5.2 Formatting rules (NF Z10-011 / SP 8855 / UPU)

- At most 6 lines (7 with country for international), 38 characters per line, left-aligned, no blank lines.
- Lines 4–6 (street, special mention/lieu-dit, postcode + locality): no punctuation, capitals recommended for the last 3 lines.
- Line 6: 5-digit postcode, space, locality name (never abbreviated); `CEDEX` / `CEDEX nn` must never be removed.
- Private-person structure: 1 name · 2 inside building (apartment, floor) · 3 outside building (entrance, building, residence) · 4 number + street · 5 special mention (BP, lieu-dit) · 6 postcode + locality.

### 5.3 Checked against La Poste's official postcode file

Base officielle des codes postaux (`laposte-hexasmal`, Licence Ouverte 2.0), downloaded
2026-11-05: 39,192 rows, 6,328 distinct postcodes, range `01000`–`98890`. This file
holds geographic postcodes only; CEDEX codes are in a separate reference (CEDEXA),
which was not checked.

| Finding | Detail | Status |
|---|---|---|
| Unused first two digits | `00`, `96`, `99`, so `00xxx`, `96xxx`, `99xxx` appear in no geographic postcode | Derived (would fail a postcode-existence check) |
| Overseas prefixes in use | `971`–`976`, `980` (Monaco), `986`–`988` | — |
| `75000`, `75999` | Not in the file | Derived; `75000` is a common but non-existent "Paris" placeholder |
| `MA VILLE`, `EXEMPLE`, `EXEMPLEVILLE`, `TEST` | Not commune names | Derived |
| `VILLE` | **Is a real commune** (Villé, Bas-Rhin) | **Avoid** as a placeholder |
| `TRIFOUILLIS LES OIES`, `PERPETTE LES OIES` | Not communes; recognisable French joke placeholder town names | Derived (not official) |

### 5.4 Address strategy options

| Option | Passes format check | Passes postcode/town lookup | Risk of real match |
|---|---|---|---|
| A. Real postcode + real commune + invented street (official La Poste / UPU pattern) | ✅ | ✅ | Low if the street is checked not to exist in that commune (BAN) |
| B. Real postcode + invented town (FNFE-MPE `MA VILLE 06000`) | ✅ | ❌ (pair mismatch) | None |
| C. Unused postcode prefix (`00xxx`/`96xxx`) + invented town | ✅ (5 digits) | ❌ | None |

Option A is the only one that passes full validation; street names should be checked
against the Base Adresse Nationale (adresse.data.gouv.fr).

---

## 6. Other identifiers useful for UBL elements

| Element | Value / range | Status | Source |
|---|---|---|---|
| GLN / GTIN (`schemeID="0088"`) | GS1 prefix `952` (e.g. GLN `952xxxxxxxxxC`) | Reserved | GS1 General Specifications; GS1 Style Guide §2.18 |
| GTIN-12 (UPC) | `012345000058` | Published example | GS1 US, via GS1 Style Guide |
| Parcel tracking (La Poste Suivi sandbox) | e.g. `EP111111110FR` | Published example (unverified, forum source) | developpez.net thread |

---

## 7. Avoid list

| Value | Seen as | Why |
|---|---|---|
| `552100554` | "Example SIREN" on a third-party e-invoicing site | Real company: PEUGEOT SA ✅ register lookup |
| `123456789`, `000000001` | DGFiP prose/examples | Fail Luhn (deliberately) |
| `FR37288100000008` | FNFE-MPE file | Malformed VAT |
| `vendeur.fr`, `acheteur.fr`, `exemple.fr`, `example.fr` | Example email domains | Registered domains |
| `FR76 3000 6000 0112 3456 7890 189` | Widely copied example IBAN | Not from an authority; real bank code `30006` |
| `VILLE` | Placeholder town | Real commune |
| `10 Rue du Centre 93160 Noisy-le-Grand` | DGFiP example | Real public-sector address |

---

## 8. Sources

- FNFE-MPE: [fnfempe/France_RFE](https://github.com/fnfempe/France_RFE) · [Ressources](https://fnfe-mpe.org/ressources/)
- DGFiP: [Spécifications externes B2B](https://www.impots.gouv.fr/specifications-externes-b2b) · direct downloads: [v3.2 ZIP](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/specification_externes_b2b/specifications-externes-v3.2.zip) · [v3.1 ZIP](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/specification_externes_b2b/specifications-externes-v3.1.zip) · [v2.4 ZIP, last version with example XML files](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/specification_externes_b2b/version_2-4_du_19_06_2024/specifications-externes-facturation-electronique-v2.4.zip) · [Norme AFNOR XP Z12-012](https://www.impots.gouv.fr/factures-norme-afnor)
- AIFE: [Chorus Pro qualification portal](https://communaute.chorus-pro.gouv.fr/portail-de-qualification/?lang=en)
- ARCEP: [Décision 2018-0881](https://www.arcep.fr/uploads/tx_gsavis/18-0881.pdf) · [Légifrance, décision 2021-0532](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043910280)
- SWIFT: [IBAN Registry](https://www.swift.com/resource/iban-registry-pdf) · [ISO 9362 (Wikipedia)](https://en.wikipedia.org/wiki/ISO_9362)
- GS1: [Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix) · [Style Guide](https://www.gs1.org/standards/gs1-style-guide/current-standard) · [General Specifications](https://ref.gs1.org/standards/genspecs/)
- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- La Poste: [SP 8855 vol. 2 *Adressage des plis*](https://lastation.laposte.fr/sites/p8_u1/files/2023-03/SP8855-Volume%202_V1.11%20-%20Adressage%20des%20plis.pdf) · [Colissimo web service spec](https://www.colissimo.entreprise.laposte.fr/sites/default/files/2021-12/DT_Flexibilite_Expedition_Web-Service-Affranchissement_202112_FR.pdf) · [Base officielle des codes postaux](https://www.data.gouv.fr/datasets/base-officielle-des-codes-postaux) ([raw CSV, laposte-hexasmal](https://data.laposte.fr/data-fair/api/v1/datasets/laposte-hexasmal/raw)) · [Abréviations](https://www.laposte.fr/envoyer/abreviation-adresses-postales)
- UPU: [Postal addressing systems — France (EN)](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/fraEn.pdf) · [(FR)](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/FraFr.pdf)
- Register lookups: [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr)
- Secondary: [Cabinet Digital example invoices](https://www.cabinetdigital.fr/facture-electronique/exemples-de-factures/) ([ZIP, 32 files](https://www.cabinetdigital.fr/facture-electronique/exemples-de-factures/exemples-factures-electroniques.zip))
