# Fictitious-but-valid example identifiers — Australia and New Zealand

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, English-language queries (no Māori-language official
material was found for these identifiers). Checks marked ✅ were run during research:
ABN mod-89, ACN mod-10, TFN mod-11, IRD mod-11 (primary/secondary weights), GS1 mod-10
(NZBN/GLN), NZ bank account algorithms A/B/D/E/F/G, Medicare and old-format NHI check
digits; lookups in **ABN Lookup** (`abr.business.gov.au`, public HTML search), the
**NZ Companies Register** search, the **AusPayNet BSB directory** (full CSV, 17,306
rows, Nov 2026) and a community Australian postcode dataset.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**
- **Australia:** the joint A-NZ Peppol authorities (ATO + MBIE) publish UBL examples
  whose ABNs `47 555 222 000`, `91 888 222 000`, `65 631 636 556` and
  `46 610 678 455` pass the ABN check and are **not in ABN Lookup**. These are the best
  official fictitious company identifiers found in any country so far. ACMA formally
  reserves telephone numbers for fiction.
- **New Zealand:** **no official fictitious NZBN exists**. The two NZBNs in the PINT A-NZ
  examples belong to real (removed) companies. There is no reserved telephone range.
  The IRD and bank-account algorithms are officially published, with worked examples.

---

# Part A — Australia

## A1. Official example files: Peppol PINT A-NZ (UBL 2.1)

Source: [PINT A-NZ Billing](https://docs.peppol.eu/poac/aunz/pint-aunz/),
`resources.zip` (60 files, version 1.1.3, released 2026-06-08, "Maintained by
Australian & New Zealand Peppol Authorities"). It contains 17 invoice examples and 2
credit note examples (`AU Invoice.xml`, `AU GST Only.xml`, `AU Freight - Line Item.xml`,
`AU Invoice Energy Bill Example_1..3`, `AU Invoice Annual Insurance.xml`, `NZ …`), plus
the BIS document (`bis.pdf`) with UBL snippets. `CustomizationID` =
`urn:peppol:pint:billing-1@aunz-1`.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| ABN, seller (`EndpointID`/`CompanyID schemeID="0151"`) | `47555222000` | Published example | ✅ mod-89 · ✅ ABN Lookup: no record |
| ABN, buyer | `91888222000` | Published example | ✅ mod-89 · ✅ no record |
| ABN, seller endpoint (BIS snippet) | `65631636556` | Published example | ✅ mod-89 · ✅ no record |
| ABN, buyer endpoint (BIS snippet) | `46610678455` | Published example | ✅ mod-89 · ✅ no record |
| ABN, buyer (5 freight/GST files) | `57946356658` | **Avoid** | ✅ mod-89, but **real: Mid North Coast Local Health District** (NSW) |
| GST branch number (`PartyTaxScheme/CompanyID`) | `47555222000001`, `91888222000001`, `65631636556001` | Published example | ABN + 3-digit GST branch; the BIS gives the rule with `51824753556001` (ATO's own ABN, see A8) |
| Names | `Supplier Trading Name Ltd`, `Supplier Official Name Ltd`, `Supplier ABC Pty Ltd`, `Buyer CDE Pty Ltd`, `Buyer Official Name`, `Grey Roo Energy`, `Elite Insurance`, `Trotters Trading Co Ltd` | Published example | Generic names are safe; `Elite Insurance`, `Grey Roo Energy` not checked against business-name registers |
| BSB (`FinancialInstitutionBranch/ID`) | `123-456`, BIS: `205536` | Published example | ✅ neither is in the AusPayNet directory (see A4) |
| Account number | `12345`, `324875423`, `56477787743` | Published example | No checksum exists for AU account numbers |
| Other payment means | `BPAY`, `NPP-EMAL` (PayID e-mail) | Published example | Pseudo-branch IDs used by the examples for BPAY/PayID |
| GLN (`schemeID="0088"`) | `1234567890128`, `1234567890135` | Placeholder | ✅ GS1 check digit, but prefix `123…` is a GS1 US range: use `952…` instead (A7) |

**Address and contact defects in the examples (do not copy):**

| Value in example | Problem |
|---|---|
| `Harrison` / `2912` / `NSW` | Harrison is in the **ACT** (postcode 2914); 2912 is Gungahlin ACT |
| `Eastmead` 2443 NSW | Not an Australian locality (good as a fictitious town, but fails a postcode/locality check) |
| `Sydney` 2310 NSW | 2310 = "Hunter Region MC" (mail centre, Newcastle) |
| `Sydney` 2758 NSW | 2758 = Kurrajong/Bilpin area, not Sydney |
| Phones `0261234567`, `0761234567`, `0430123456`, `0450000001` | In live ranges, not ACMA-reserved (A3) |
| E-mail domains `qualitygoods.com.au`, `buyer.com.au`, `business1.com.au`, `blackhouse.com` | Registered domains (DNS NS checked) |
| `eliteinsure.com.au`, `yourpaymentwebsite.com.au`, `yourwebsiteexample.com.au` | Not registered today (NXDOMAIN), but could be registered at any time; use `.test` |

## A2. Company and tax identifiers

| Identifier | Rule (official source) | Notes |
|---|---|---|
| ABN | 11 digits. Subtract 1 from the first digit, weights `10 1 3 5 7 9 11 13 15 17 19`, sum mod 89 = 0 ([ABR *ABN format*](https://abr.business.gov.au/Help/AbnFormat)) | Display `nn nnn nnn nnn`. Peppol EAS `0151` |
| ACN / ARBN | 9 digits; weights `8 7 6 5 4 3 2 1` on digits 1–8, check = `(10 − sum mod 10) mod 10` | Company ABN = 2 check digits + ACN. ASIC's current page no longer shows the algorithm (it now uses the invalid example `123 456 789`); the algorithm is in ASIC's *Message Implementation Guide* App. D (secondary sources) |
| GST registration | No separate number: GST is registered against the ABN; GST branches = ABN + 3 digits | PINT A-NZ BIS |
| TFN | 8 or 9 digits, mod-11 with weights `1 4 3 7 5 8 6 9 10` (9 digits) | **Not officially published** by the ATO; algorithm is from secondary sources. Do not use in UBL (see A8) |

### A2.1 Derived ABN candidates

Built on the same `555 222 nnn` / `888 222 nnn` pattern as the official examples, then
checked in ABN Lookup:

| Candidate | Check | ABN Lookup |
|---|---|---|
| `28 555 222 001` | ✅ | ✅ no record |
| `98 555 222 002` | ✅ | ✅ no record |
| `79 555 222 003` | ✅ | ✅ no record |
| `72 888 222 001` | ✅ | ✅ no record |
| `76 999 222 000` | ✅ | ✅ no record |
| `18 123 456 789` | ✅ | ✅ no record (ABN built on the invalid ASIC "ACN" `123456789`, so it has no valid ACN) |

For each 9-digit base there is at most one pair of leading check digits that makes a
valid ABN. Limitation: ABN Lookup shows ABNs once they are active (cancelled ABNs stay
listed). A "no record" result means the number is not issued now, not that it is
reserved. The ABN Lookup web services (SOAP/JSON) need a registered GUID. No public
test GUID or test dataset was found.

### A2.2 ACN examples — Avoid

The "valid ACN" list copied from an old ASIC page (`000 000 019`, `000 250 000`,
`000 500 005`, `000 750 005`, `001 000 004`, `001 250 004`, `001 500 009`,
`001 749 999`) and ASIC's worked example `004 085 616` are **real companies**:

| ACN | ABN Lookup result |
|---|---|
| `000 000 019` | MONAKA PTY LTD (ABN `89 000 000 019`) |
| `000 250 000` | WAM PTY LTD |
| `000 500 005` | A.C.N. 000 500 005 PTY LTD |
| `000 750 005` | ELECTROMEC INDUSTRIES PTY LTD |
| `004 085 616` | B P AUSTRALIA PTY LTD (ABN `53 004 085 616`) |
| `001 000 004` | No ABN record (it may still be a registered company with no ABN) |

**No official fictitious ACN was found.** If a party needs an ACN, use only an ABN
derived from it whose ACN part is checked as unused (ASIC Connect search, not done in
this session), or leave the ACN out.

## A3. Telephone numbers — ACMA reserved for creative works

The ACMA publishes numbers that "do not belong to people or businesses and you are free
to use them in works of fiction" (also recommended for documentation by secondary
sources).

| Type | Value / range | Status |
|---|---|---|
| Geographic, Central East (NSW, ACT) | `(02) 5550 xxxx`, `(02) 7010 xxxx` | Reserved |
| Geographic, South East (VIC, TAS) | `(03) 5550 xxxx`, `(03) 7010 xxxx` | Reserved |
| Geographic, North East (QLD) | `(07) 5550 xxxx`, `(07) 7010 xxxx` | Reserved |
| Geographic, Central West (SA, WA, NT) | `(08) 5550 xxxx`, `(08) 7010 xxxx` | Reserved |
| Mobile (30 single numbers, **not** a block) | `0491 570 006`, `0491 570 156`, `0491 570 157`, `0491 570 158`, `0491 570 159`, `0491 570 110`, `0491 570 313`, `0491 570 737`, `0491 571 266`, `0491 571 491`, `0491 571 804`, `0491 572 549`, `0491 572 665`, `0491 572 983`, `0491 573 770`, `0491 573 087`, `0491 574 118`, `0491 574 632`, `0491 575 254`, `0491 575 789`, `0491 576 398`, `0491 576 801`, `0491 577 426`, `0491 577 644`, `0491 578 957`, `0491 578 148`, `0491 578 888`, `0491 579 212`, `0491 579 760`, `0491 579 455` | Reserved |
| Freephone | `1800 160 401`, `1800 975 707` – `1800 975 711` | Reserved |
| Local rate | `1300 975 707` – `1300 975 711` | Reserved |
| Premium rate | `1900 654 321` | Reserved (listed on older ACMA versions and by Wikipedia; not confirmed on the current page) |

International format: `+61 2 5550 xxxx`, `+61 491 570 006`. The neighbours of the
reserved mobile numbers are ordinary numbers, so copy them exactly.

Verification note: the ACMA page returned HTTP 503 to every fetch from this session.
The geographic list and the first 23 mobile numbers were confirmed from
search-engine extracts of the live ACMA page. The other 7 mobile numbers and the
1300/1900 numbers come from Wikipedia, which cites the same page. **Re-check against
the ACMA page before use.**

## A4. Bank identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| BSB | `123-456` | Published example | PINT A-NZ and AusPayNet's own BSB file guide (`123-456 ABC XYZ Company 109 Test Street Sydney NSW 2000`). ✅ Not in the BSB directory, but prefix `12` is allocated to Bank of Queensland |
| BSB | `205-536` | Published example | PINT BIS. ✅ Not in directory; first two digits `20` not used by any BSB |
| BSB | `000-000` | Avoid | AusPayNet uses it as a format template and in "Merged — Refer to BSB 000-000" records |
| Unused BSB first digits | `00 05 07 13 16 17 20 27 28 38 44 50 54 60 62 66 69 71 74 75 78 79 86 87 97 99` | Derived | ✅ No row in the full directory (Nov 2026). Some may be allocated to an institution in the *Key to Abbreviations* without branches |

BSBs have **no check digit**; validity means "present in the AusPayNet directory". So a
fictitious BSB fails a directory check by design. **No reserved test BSB was found.**
Australia does not use IBAN. For BIC, use the ISO 9362 test convention (8th character
`0`), see the France file §2.

## A5. Postal addresses

### A5.1 What Australia Post publishes

**No fictitious locality or postcode is reserved.** Australia Post examples use
fictitious people/companies at real localities:

| Source | Example |
|---|---|
| [*Correct addressing*](https://auspost.com.au/content/dam/auspost_corp/media/documents/correct-addressing.pdf) | `Mr A Jones` / `54 Stockton Rd` / `BUNBURY WA 6230`; `Ms A Citizen` / `3 Example Street` / `PARKVILLE VIC 3052`; `Mr J Citizen` / `Sample Games Co` / `GPO Box 123` |
| [*Address Presentation Standards* (1999)](https://auspost.com.au/content/dam/auspost_corp/media/documents/australia-post-addressing-standards-1999.pdf) | `Mr C.R. MacDonald AO` / `Manager` / `Orbit Travel Co` / `Travel World House` / `Level 7 17 Jones St` / `NORTH SYDNEY NSW 2060` |
| same, floor of a building | `Ms C. Fitzgerald` / `William Jones Pty Ltd` / `Level 6 51 Jacobson St` / `BRISBANE QLD 4000` |
| same, unit | `MR JOHN SMYTHE` / `UNIT 4 28 PAXTON CT` / `MOORABIN VIC 3189` (sic: the locality is MOORABBIN) |
| same, PO Box / Locked Bag | `SILKHOUSE TRAVEL CO` / `ATTN: MR A. BROWN` / `PO BOX 37` / `SPRINGVALE VIC 3171`; `The Secretary` / `Broken Arrow Corporation` / `Locked Bag 801` / `FORTITUDE VALLEY QLD 4006` |
| same, rural | `Mr Ron James` / `4360 Dukes Rd` / `KALGOORLIE WA 6430` |
| [Address label template](https://auspost.com.au/content/dam/auspost_corp/media/documents/address-label-template.pdf) | `J. Smith`, customer number `12345678` |
| PreSort Letters guide (search extract) | `Mr A Sample` / `111 Bourke Street` / `MELBOURNE VIC 3000` |

Names to avoid from the 1999 standard: `Compass Airlines Pty Ltd` (a real former
airline); `AUSTRALIA POST` / `219-241 CLEVELAND ST` / `STRAWBERRY HILLS NSW 1427` (real).

Rules (Australia Post / AS 4590-1999): 3–4 lines, no blank lines, left-justified, max
40 characters per line, no punctuation in the address proper (`-` and `/` allowed
between elements); last line = `LOCALITY STATE POSTCODE` in capitals, with 1–2 spaces
between the parts; state abbreviations `NSW VIC QLD SA WA TAS NT ACT`; street types
abbreviated per AS 4590 (`ST`, `RD`, `DR` …); unit `U 2 17 Jones St` or `2/17 Jones St`;
no `/` between a level and the street number.

### A5.2 Postcode checks

Australia Post's postcode file is not open. Checked against the community dataset
[matthewproctor/australianpostcodes](https://github.com/matthewproctor/australianpostcodes)
(18,559 rows, 3,175 postcodes, `0200`–`9999`; not official):

| Finding | Status |
|---|---|
| First two digits `00 01 03 04 05 06 07 19 49 75–79 86 88 89 91–93 95 96 98` not used | Derived (unofficial dataset) |
| `0000`, `0100`, `1000`, `0999` not used | Derived |
| `9999` = **NORTH POLE VIC** (Australia Post's letters-to-Santa postcode) | **Avoid** as a "dummy" postcode |
| `EXAMPLE`, `SAMPLE`, `SAMPLEVILLE`, `ANYTOWN`, `EASTMEAD`, `BULLAMAKANKA`, `WOOP WOOP` | Not localities: Derived. `Bullamakanka` / `Woop Woop` are recognisable Australian joke "middle of nowhere" names (not official) |
| `SPRINGFIELD`, `HARRISON`, `PARKVILLE`, `BUNBURY` | Real localities |

Strategy: as in France, only a real postcode + matching locality + invented street
passes full validation. Check invented streets against the G-NAF (Geocoded National
Address File, open data on data.gov.au). This was not done in this session.

## A6. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com/.net/.org` | Reserved | RFC 2606 / RFC 6761 |
| `example.com.au` | **Avoid** | Registered and used by a private brand agency ("We Are Example") |
| `test.com.au` | **Avoid** | Registered |
| `example.net.au` | Unclear | DNS SERVFAIL. Do not use |

auDA has no reserved example name in `.au`. Use `accounts@<alias>.test`.

## A7. Other identifiers

| Element | Value / range | Status | Notes |
|---|---|---|---|
| GLN / GTIN (`0088`) | GS1 prefix `952` | Reserved | GS1 demo prefix (France file §6). GS1 Australia's own prefix is `93` (real companies) |
| Medicare card number | 10 digits (+IRN): first digit 2–6, weights `1 3 7 9 1 3 7 9`, digit 9 = sum mod 10, digit 10 = issue no. | — | Algorithm only from secondary sources. Services Australia test cards are only in the registered Health Systems Developer Portal. Not needed in UBL |
| TFN exemption codes | `000 000 000` (not quoted), `111 111 111` (declaration pending), `333 333 333` (under 18), `444 444 444` (pensioner) | Published (ATO) | Placeholders with a legal meaning, not test values; only `000000000` passes the TFN check |
| ATO test data (EVTE) | Service-specific test-data workbooks on softwaredevelopers.ato.gov.au | Not verified | The PDF download was refused by the server (HTTP/2 reset) |
| Driver licence, USI, vehicle plates | — | Not researched | No official reserved values found. No UBL use beyond `cac:IdentityDocumentReference` |

## A8. Avoid list — Australia

| Value | Seen as | Why |
|---|---|---|
| `51 824 753 556` | ABR worked example, PINT GST branch example `51824753556001` | Real: **Australian Taxation Office** |
| `57 946 356 658` | PINT A-NZ buyer ABN (5 files) | Real: Mid North Coast Local Health District |
| `53 004 085 616` / ACN `004 085 616` | ASIC worked example | Real: BP Australia Pty Ltd |
| ACNs `000 000 019`, `000 250 000`, `000 500 005`, `000 750 005` | "Valid ACN" test lists | Real companies |
| `83 914 571 673` | Sample ABN seen in third-party validator code (origin not traced) | Real: The Trustee for Carpenter Family Trust |
| ACN `123 456 789`, ABN `36 123 456 789` | ASIC ACN page | Fail the check digits |
| TFN `123 456 782`, `876 543 210` | Common "valid TFN" samples (pass the check) | Not official, and TFN use is restricted by the Privacy (Tax File Number) Rule 2015. Never put a TFN in a business document |
| GLN `1234567890128` / `…0135` | PINT A-NZ | GS1 US prefix range |
| Phones `02 6123 4567`, `07 6123 4567`, `0430 123 456`, `0450 000 001` | PINT A-NZ | Not ACMA-reserved |
| `9999` | Dummy postcode | North Pole VIC (real Australia Post postcode) |
| `example.com.au`, `test.com.au`, `qualitygoods.com.au`, `buyer.com.au`, `business1.com.au`, `blackhouse.com` | Example domains | Registered |
| `Harrison 2912 NSW` | PINT A-NZ | Wrong state/postcode pair |

---

# Part B — New Zealand

## B1. Official example files: Peppol PINT A-NZ (NZ examples)

The same `resources.zip` as A1 holds `NZ No Allowances.xml`, `NZ Prepaid Amount.xml`,
`NZ Invoice Level Allowance.xml`, `NZ Invoice Level Charge.xml`,
`NZ Allowance On Invoice Line.xml` and `NZ Credit note.xml`. MBIE (with the ATO) is the
NZ Peppol Authority. There is no separate NZ UBL format.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| NZBN, seller (`schemeID="0088"`) | `9429033821733` | **Avoid** | ✅ GS1 check · **real: Scarlet Software Services Limited** (company 1873404, removed) |
| NZBN, buyer | `9429033591476` | **Avoid** | ✅ GS1 check · **real: Scarlet Software Services NZ Limited** (company 1911796, removed; Levin address) |
| GST number (`PartyTaxScheme/CompanyID`) | `888-888-888`, `999-999-999`, `777-777-777` | Placeholder | ❌ All fail the IRD check (above 200,000,000) |
| Names | `SupplierTradingName Ltd.`, `SupplierOfficialName Ltd`, `Trotters Trading Co Ltd`, `Trotters Incorporated`, `Black House Trading` | Published example | Not checked against the Companies Register |
| People / emails | `Ronald MacDonald`, `ronald.macdonald@qualitygoods.co.nz`, `Malakai King`, `MalakaiKing@blackhouse.com`, `Mr Anderson`, `Mr Wilson` | Avoid emails | `blackhouse.com` registered; `qualitygoods.co.nz` NXDOMAIN today |
| Postcodes | `NZ 123 EW`, `A36577`, `21234`, `1111` | Placeholder | ❌ NZ postcodes are 4 digits; `1111` is not a Wellington postcode |
| Addresses | `16 Stout Street` Wellington (region `Kapiti Coast`); `100 Queen Street` Auckland; `Delivery street 2` Auckland (`Northland`) | Avoid | Real street names in central Wellington/Auckland. Region/town mismatches |
| Phone | `Mobile 021 1090666` | Avoid | Live mobile range |

**Conclusion: do not take NZ party data from PINT A-NZ.** Use it only as a structural
reference (EAS `0088` = NZBN for NZ endpoints and legal IDs).

## B2. Company and tax identifiers

| Identifier | Rule | Notes |
|---|---|---|
| NZBN | 13-digit GS1 GLN, GS1 mod-10 check; all NZBNs seen start `9429` (GS1 NZ prefix `94`; block bought by the government) | MBIE: "Each NZBN is a 13 digit Global Location Number (GLN) provided by GS1 New Zealand". Peppol EAS `0088` |
| IRD number | 8 or 9 digits; valid range **10,000,000 – 200,000,000** (raised from 150,000,000 on 1 April 2026); mod-11 with weights `3 2 7 6 5 4 3 2`, and if the result is 10, secondary weights `7 4 3 2 5 2 7 6` | IR *Payroll calculations and business rules specification* 2026-27, §6 |
| GST number | Same number as the IRD number, usually shown `123-456-789` | |
| Company number | Companies Office sequential number (e.g. `1873404`) | No check digit |

### B2.1 IRD numbers — official worked examples

| Value | Status | Check |
|---|---|---|
| `49-091-850` | Published example (IR spec Example 1) | ✅ valid |
| `35-901-981` | Published example (IR spec Example 2) | ✅ valid |
| `150-000-026` | Published example (IR spec Example 3, 9-digit) | ⚠ See note |
| `9-125-568` | Published example (IR spec Example 4) | ❌ invalid by design (below range) |

**Inconsistency in the IR spec:** step 3 says to use the secondary weights only when
the primary check digit computes to 10. For `150000026` the primary result is 5 (not 10,
and it does not match), yet Example 3 goes on to the secondary weights and declares
the number valid. A validator that follows the written steps rejects `150000026`.
Validators differ here, so avoid `150000026`.

IR states that the range check "ensures that the IRD number is in the already issued
range", so **every valid IRD number may belong to a real taxpayer**. Whether `49091850`
and `35901981` are issued is unknown. IR's test IRD numbers are available only through
the Gateway Services developer portal (login), not in public. Recommendation: use
`49-091-850` / `35-901-981` as GST numbers, marked as IR worked examples.

### B2.2 NZBN — no fictitious source

- MBIE's API docs use `9429000106078` (an ETag example). The Companies Register search
  returned nothing for it, but non-company NZBNs (sole traders, trusts, government)
  are not in that register, so it is not verified.
- The NZBN API sandbox (`api.business.govt.nz/sandbox/nzbn/v5`) holds "a mixture of
  test cases and old Companies Register data (prior to 2010)". Its NZBNs can be the
  same as production NZBNs that belong to other businesses, so they are not safe.
- Derived: `9429999990009`, `9429999990016`, `9429999990023` (✅ GS1 check). They are
  far above the issued range seen (`94290…`–`94290 5…`), and a Companies Register
  search found no match. They have **not** been checked in the full NZBN register
  (needs an API key). Status: Derived, partly verified.
- Alternative: use a GS1 `952` GLN (`9520000000011`, `9520000000028`) with
  `schemeID="0088"`. It passes the 0088 syntax rule, but it is not an NZBN and would
  fail an NZ-specific NZBN check.

## B3. Bank account numbers

Format `BB-bbbb-AAAAAAA(A)-SSS(S)` (bank 2, branch 4, base 7–8, suffix 2–4 digits).
The algorithm is published by IR (§7 of the same spec), which points to the Payments NZ
Bank Branch Register for branch validity:

| Bank ID | Algorithm |
|---|---|
| 01–06, 10–24, 27, 30, 38, 88 | A if base < 00990000, else B (mod 11) |
| 08 | D (mod 11) |
| 25 | F (mod 10) |
| 31 | X (always valid) |
| 09, 26, 28, 29 | Not in IR's table. Payments NZ uses E (09) and G (26/28/29); not verified from Payments NZ |

| Value | Status | Check |
|---|---|---|
| `01-902-0068389-00` | Published example (IR Example 1) | ✅ Algorithm A |
| `08-6523-1954512-001` | Published example (IR Example 2) | ✅ Algorithm D |
| `26-2600-0320871-032` | Published example (IR Example 3) | ✅ Algorithm G |
| `02-0500-0632487-000` | PINT A-NZ BIS | ❌ fails algorithm A |

The IR examples use real bank/branch codes (01 = ANZ, 08 = former National Australia
Bank NZ, 26 = a bank ID IR's table does not list). Whether the accounts exist is
unknown. **No reserved test account was found.** For an IBAN-style field, NZ has no
IBAN.

## B4. Telephone numbers

**No reserved fictional range.** No TCF (NZ Telecommunications Forum, the numbering
administrator), Commerce Commission or MBIE source was found. Secondary sources say
NZ productions use unassigned ranges. For example, *Shortland Street* uses
`(09) 4299 xxxx`, which is a convention, not a reservation. `*555` is a live NZ Police
traffic-report number. Recommendation (as for Italy): leave NZ telephone elements
out, or use an obvious placeholder that fails validation.

## B5. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com/.net/.org` | Reserved | RFC 2606 / 6761 |
| `example.nz`, `example.co.nz`, `test.nz` | **Avoid** | All registered (Cloudflare, dan.com, parking NS) |

## B6. Postal addresses

### B6.1 What NZ Post publishes

[*Address Standards* ADV 358](https://www.nzpost.co.nz/sites/nz/files/2021-10/adv358-address-standards.pdf)
(June 2011, based on AS/NZS 4819 *Rural and urban addressing*) and the
[address layout standards page](https://www.nzpost.co.nz/business/shipping-in-nz/bulk-mail/address-layout-standards).
They use fictitious people at real places:

| Type | Example |
|---|---|
| Urban, organisation + unit + floor | `Mrs Parker` / `McKay's Emporium` / `Shop 1 Level 2` / `320A Sydney Street West` / `Thorndon` / `Wellington 6011` |
| Urban | `John Smith` / `Smith's Books` / `Shop 2` / `1153A Great South Road` / `Epsom` / `Auckland 1050` |
| Urban (web page) | `Mr A B Sample` / `123 Sample St` / `Redwood` / `Christchurch 8051` (or consolidated: `Redwood Christchurch 8051`) |
| Rural | `John Smith` / `Apt 2` / `153A Farm Road` / `RD 1` / `Outram 9073`; `415 Midhurst Road` / `RD 1` / … |
| PO Box | `John Smith` / `PO Box 4099` / `Highfield` / `Timaru 7942` |
| Private Bag | `ABC Finance` / `Private Bag 92132` / `Auckland 1142` |
| Floor only | `Level 2` / `777 Hereford Street` / `Christchurch Central` / `Christchurch 8011` |

Rules: no blank lines, left-justified, **no punctuation**. Recipient, then
organisation, then unit/floor (`Shop 1 Level 2`, unit before floor), then street
(number + alpha + name, type in full where possible), then suburb (or box lobby / `RD n`),
then `Town Postcode`. The postcode is 4 digits. Since 1 July 2011, suburb, town and
postcode may share one line, separated by spaces only. Box numbers have no spaces
(`PO Box 23226`). Never combine a PO Box with a street address. Do not use the
region/province.

### B6.2 Postcode coverage

No open official NZ postcode file was found (NZ Post sells it; the LINZ address data
has no postcodes). **Not checked.** NZ postcodes run roughly `0110`–`9893`. Use real
postcode + town pairs from the NZ Post examples above (`Wellington 6011`,
`Auckland 1050`, `Christchurch 8011`, `Timaru 7942`, `Outram 9073`) with invented
streets, checked against LINZ NZ Addresses.

## B7. Other identifiers

| Element | Value / range | Status | Source |
|---|---|---|---|
| NHI number (health) | Any NHI **starting with `Z`** (old `AAANNNC` and new `AAANNAC` formats), e.g. `ZAA0105` | Reserved | HISO 10046:2023 §2.1.6 ("NHI numbers starting with the letter Z are reserved as test numbers"); `ZAA0105` ✅ passes the old-format mod-11 check. Not needed in UBL |
| GLN (`0088`) | GS1 prefix `952` | Reserved | GS1; GS1 NZ's own prefix `94` is real companies |

## B8. Avoid list — New Zealand

| Value | Seen as | Why |
|---|---|---|
| NZBN `9429033821733` | PINT A-NZ seller | Real: Scarlet Software Services Limited (removed) |
| NZBN `9429033591476` | PINT A-NZ buyer | Real: Scarlet Software Services NZ Limited (removed) |
| NZBN `9429041926024` | "Example NZBN" on third-party sites | Reported as Inland Revenue's NZBN (not verified) |
| NZBN `9429032389470` | SDK example | Reported as Burger Fuel Limited |
| GST `888-888-888`, `999-999-999`, `777-777-777` | PINT A-NZ | Fail the IRD check |
| IRD `150000026` | IR spec Example 3 | Contradicts the spec's own written algorithm |
| Account `02-0500-0632487-000` | PINT A-NZ BIS | Fails the bank checksum |
| `example.nz`, `example.co.nz`, `test.nz`, `blackhouse.com` | Example domains | Registered |
| Postcodes `NZ 123 EW`, `A36577`, `21234` | PINT A-NZ | Not NZ postcode format |
| `*555`, `(09) 4299 xxxx` | "Fake" NZ numbers | Live service / unofficial convention |

---

## Sources

**Peppol A-NZ**
- [PINT A-NZ Billing (docs.peppol.eu)](https://docs.peppol.eu/poac/aunz/pint-aunz/) · [resources.zip](https://docs.peppol.eu/poac/aunz/pint-aunz/resources.zip) · [Release notes](https://docs.peppol.eu/poac/aunz/pint-aunz/release-notes/)

**Australia**
- ABR: [ABN format / check digit](https://abr.business.gov.au/Help/AbnFormat) · [ABN Lookup](https://abr.business.gov.au/)
- ASIC: [Australian company numbers](https://asic.gov.au/for-business/registering-a-company/steps-to-register-a-company/australian-company-numbers/australian-company-number-digit-check/) · ACN algorithm quoted from the old ASIC page in [Drupal issue #1878530](https://www.drupal.org/project/abn/issues/1878530) (secondary)
- ATO: [PAYG payment summary — TFN codes](https://www.ato.gov.au/forms-and-instructions/payg-payment-summary-individual-non-business/section-a-payee-details) · [Contributions V2 testing guidance (EVTE)](https://softwaredevelopers.ato.gov.au/sites/default/files/resource-attachments/Contributions_V2_Testing_and_Cutover_Guidance_V0.6.pdf) (not downloadable from this session)
- ACMA: [Phone numbers for use in TV shows, films and creative works](https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works) (HTTP 503 during research) · [Wikipedia — Fictitious telephone number](https://en.wikipedia.org/wiki/Fictitious_telephone_number)
- AusPayNet: [BSB static download links](https://auspaynet.com.au/BSBLinks) · [BSBDirectoryFull.csv](https://auspaynetbsbpublic.blob.core.windows.net/bsb-reports/BSBDirectoryFull.csv) · [Downloading BSB files (example record 123-456)](https://auspaynet.com.au/sites/default/files/2023-10/Downloading_BSB_Files_from_AusPayNet_via_FTP.pdf)
- Australia Post: [Correct addressing](https://auspost.com.au/content/dam/auspost_corp/media/documents/correct-addressing.pdf) · [Address Presentation Standards 1999](https://auspost.com.au/content/dam/auspost_corp/media/documents/australia-post-addressing-standards-1999.pdf) · [Address label template](https://auspost.com.au/content/dam/auspost_corp/media/documents/address-label-template.pdf) · [PreSort Letters guide](https://auspost.com.au/content/dam/auspost_corp/media/documents/presort-letters-service-guide.pdf)
- Community postcode data: [matthewproctor/australianpostcodes](https://github.com/matthewproctor/australianpostcodes)
- Medicare algorithm (secondary): [AIR claiming docs](https://air.claiming.com.au/docs/validation-and-checks/) · [clearwater.com.au](https://clearwater.com.au/code/medicare/)

**New Zealand**
- Inland Revenue: [Payroll calculations and business rules specification 2026-27](https://www.ird.govt.nz/digital-service-providers/services-catalogue/returns-and-information/payday-filing/payroll-calculations-and-business-rules) ([PDF](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf), §6 IRD validation, §7 bank account validation) · [IRD number validation service](https://www.ird.govt.nz/digital-service-providers/services-catalogue/customer-and-account/ird-number-validation)
- MBIE / NZBN: [NZBN API](https://portal.api.business.govt.nz/api/nzbn) · [What's an NZBN](https://www.nzbn.govt.nz/whats-an-nzbn/) · [Companies Register search](https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/search)
- Payments NZ: [Bank Branch Register](https://www.paymentsnz.co.nz/resources/industry-registers/bank-branch-register/)
- NZ Post: [Address Standards ADV 358](https://www.nzpost.co.nz/sites/nz/files/2021-10/adv358-address-standards.pdf) · [Address layout standards](https://www.nzpost.co.nz/business/shipping-in-nz/bulk-mail/address-layout-standards) · [How to address mail](https://www.nzpost.co.nz/personal/sending-in-nz/how-to-address-mail)
- Health NZ / HISO: [HISO 10046:2023 Consumer Health Identity Standard (copy)](https://ehealthforum.nz/uploads/short-url/zdzy3oGbJ3KWMi2Q77EfMlgjzIq.pdf) · [NHI Number (Wikipedia)](https://en.wikipedia.org/wiki/NHI_Number)
- Telephone (secondary): [Telephone numbers in New Zealand (Wikipedia)](https://en.wikipedia.org/wiki/Telephone_numbers_in_New_Zealand)

**General**
- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- GS1: [Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix) · [General Specifications](https://ref.gs1.org/standards/genspecs/)
