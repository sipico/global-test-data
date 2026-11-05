# Fictitious-but-valid example identifiers — India and Singapore

**Purpose:** same as `example-identifiers-fr.md`. This file collects identifiers,
addresses and contact data that pass format and checksum validation, come from an
official or authoritative source, and cannot be confused with a real organisation.
They feed the canonical 26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05. Queries were run in English, Hindi (India), and Chinese,
Malay and Tamil (Singapore). The non-English queries found nothing beyond the English
sources. Checks marked ✅ were run during research:

- GSTIN Luhn mod-36 check character and Aadhaar Verhoeff digit.
- UEN check letters (all three formats) and NRIC/FIN check letters.
- GS1 check digits.
- Lookup in ACRA's full open register (data.gov.sg *Entities Registered with ACRA*,
  2,127,089 rows, downloaded 2026-11-05).
- Lookup in the OneMap (SLA) address search for Singapore postcodes.
- DNS lookups for example email domains.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headlines**

- **Singapore** has the richer official material. OpenPeppol/IMDA publish 16 PINT-SG
  **UBL 2.1** example files, and GovTech publishes 19 Myinfo sandbox NRIC/FINs. However,
  **every UEN in IMDA's examples fails its check letter**, and one of them
  (`201012456C`) is a real company (Singtel Mobile).
- **India** has official **sandbox** GSTINs: six on NIC's e-invoice API portal, which
  pass the checksum, and five UIDAI test Aadhaar numbers, which pass Verhoeff. India
  has no UBL. Its e-invoice is a GSTN JSON schema, so only the identifiers carry over.

---

# Part A — India

## A1. GSTIN (GST identification number)

### A1.1 Structure and check character

| Pos. | Content | Rule |
|---|---|---|
| 1–2 | State code | GST state code, e.g. `27` Maharashtra, `29` Karnataka, `33` Tamil Nadu, `07` Delhi, `37` Andhra Pradesh (new) |
| 3–12 | PAN of the holder | See A2 |
| 13 | Entity number | `1`–`9`, then `A`–`Z`: nth registration of the same PAN in that state. `0` is rejected by python-stdnum |
| 14 | `Z` | Default. Other letters are used for special registrations |
| 15 | Check character | Luhn mod-36 over chars 1–14 (alphabet `0-9A-Z`, weights 1,2,1,2… from the left, add `p div 36 + p mod 36`, check = `(36 − sum mod 36) mod 36`) |

GSTN has **not published** the algorithm officially. The rule above is the one used by
python-stdnum 2.2 (`stdnum/in_/gstin.py`) and by validator tools. ✅ It accepts all six
NIC sandbox GSTINs below.

### A1.2 Official sandbox GSTINs — NIC e-Invoice API sandbox (IRP 1)

Source: the NIC e-Invoice API Developer's Portal `einv-apisandbox.nic.in`, page *Sync
GSTIN Details from CP* (API v1.03). The page tells developers to test with these
GSTINs. The NIC site was unreachable from the research environment (HTTP 503 or
connection reset), so the list was confirmed via search-engine extracts of the NIC
page and Masters India's API documentation. Masters India returns
`"LegalName": "GSTN2 MH TaxPayer 1 Ltd"` for `27GSPMH1881G1ZH`, with an empty address
and `AddrPncd` = 0.

| Element | Value | Status | Checks / notes |
|---|---|---|---|
| GSTIN (Tamil Nadu) | `33GSPTN1882G1Z3` | Published example (sandbox test GSTIN) | ✅ check char · ✅ PAN shape valid (4th char `T` = trust) |
| GSTIN (Tamil Nadu) | `33GSPTN3381G1Z5` | Published example (sandbox) | ✅ check char · ✅ PAN shape |
| GSTIN (Tamil Nadu) | `33GSPTN3382G1Z4` | Published example (sandbox) | ✅ check char · ✅ PAN shape |
| GSTIN (Maharashtra) | `27GSPMH1881G1ZH` | Published example (sandbox) | ✅ check char · ⚠️ 4th PAN char `M` is not a PAN holder type, so strict validators (python-stdnum) reject it |
| GSTIN (Maharashtra) | `27GSPMH1882G1ZG` | Published example (sandbox) | ✅ check char · ⚠️ same PAN-type issue |
| GSTIN (Maharashtra) | `27GSPMH3381G1ZI` | Published example (sandbox) | ✅ check char · ⚠️ same PAN-type issue |
| Legal name (sandbox) | `GSTN2 MH TaxPayer 1 Ltd` | Published example | Obviously fictitious |

The `GSP` + state-abbreviation pattern (`GSPTN`, `GSPMH`) makes these unmistakably
test values. **Recommendation:** use the three `33GSPTN…` values. They pass checksum,
PAN shape and state-code validation. A live GST lookup (GST portal "Search Taxpayer",
captcha-protected, not run) should not find them in production.

### A1.3 Other GSTINs seen in official or semi-official samples

| Value | Where | Status | Checks |
|---|---|---|---|
| `37ARZPT4384Q1MT` | Seller in the NIC *Generate IRN* sample JSON (`NIC company pvt ltd` / `NIC Industries`) | **Avoid** | ❌ 14th char `M` not `Z` · ❌ check char (would be `X`) |
| `29AWGPV7107B1Z1` | Buyer / ship-to in the same NIC sample; also *Get GSTIN* sample | **Avoid** | ❌ check char (correct would be `F`). A ClearTax IRP document links this PAN to "VIKAS EXPORTS", so it may be a real taxpayer |
| `12AWGPV7107B1Z1` | Transporter ID (`TransId`) in the NIC sample | **Avoid** | ❌ check char |
| `05AAACG2140A1ZL` | e-Way Bill sandbox transporter GSTIN, per India Compliance (ERPNext) docs and a reproduced EWB API guide | Published example (secondary source, unverified) | ✅ check char · PAN `AAACG2140A` looks like a real-company PAN; owner not verified |
| `05AAACG2115R1ZN` | Same EWB API guide | Unverified | Not checked against NIC |
| `29AAFCD5862R000`, `27AAFCD5862R013`, … | ClearTax GSP sandbox list (private) | **Avoid** | ❌ not GSTINs (13th char `0`, 14th char not `Z`) |

### A1.4 Derivation rule (for more Indian parties)

Take a PAN-shaped string that is clearly fictitious. Prefix a state code, add entity
`1` and `Z`, then compute the check character. Example: `29` + `AAFCD5862R` + `1Z`
gives `29AAFCD5862R1ZR` (Derived). **There is no open API for checking that a PAN or
GSTIN is unused.** The GST portal search is captcha-protected, so derived GSTINs
remain *unverified for collision*. Prefer the NIC sandbox values.

## A2. PAN (Permanent Account Number)

| Element | Value / rule | Status | Notes |
|---|---|---|---|
| Format | `AAAAA9999A`: 3 letters, holder-type letter, initial of name/surname, 4-digit serial `0001`–`9999`, check letter | — | The check-letter algorithm is **undocumented**. Validators check shape and holder type only |
| Holder types (4th char) | `A` AOP · `B` BOI · `C` company · `F` firm/LLP · `G` government · `H` HUF · `L` local authority · `J` artificial juridical person · `P` individual · `T` trust | — | Per python-stdnum, citing the Income Tax Department |
| `ABCDE1234F` | Common textbook placeholder | **Avoid** | ❌ 4th char `D` is not a holder type |
| IEC (importer-exporter code) | = PAN since DGFT Trade Notice 09/2017 (12 June 2017) | — | No separate example values exist. Reuse the party's PAN |

## A3. Aadhaar (UIDAI) — official test numbers

UIDAI's *Data and Downloads → Testing Data and License Keys* section (uidai.gov.in)
publishes test UIDs for the **staging/pre-production** authentication environment
(`developer.uidai.gov.in`, test AUA code `public`). UIDAI notes that all these UIDs
share the same biometric record.

| Aadhaar (UID) | Test resident (as published) | Status | Checks |
|---|---|---|---|
| `999941057058` | Shivshankar Choudhury, 12 Maulana Azad Marg, New Delhi 110002 | Published example (staging test UID) | ✅ Verhoeff |
| `999971658847` | Kumar Agarwal, 5A Madhuban, Veera Desai Road, Udaipur, Rajasthan 313001 | Published example | ✅ Verhoeff |
| `999933119405` | Fatima Bedi, K-3A Rampur Garden, Bareilly, Uttar Pradesh 243001 | Published example | ✅ Verhoeff |
| `999955183433` | Rohit Pandey, 603/4 Vindyachal, 7th Road Raja Wadi, Ghatkopar (East), Mumbai, **pincode 243001** | Published example | ✅ Verhoeff · ⚠️ PIN `243001` is Bareilly, not Mumbai (UIDAI data error) |
| `999990501894` | Anisha Jay Kapoor, 2B 203, 14 Main Road, Jayanagar, Bangalore 560036 | Published example | ✅ Verhoeff |
| `999999990019` | "Shivshankar Choudhury" per a third-party sandbox guide (dpdpindia.in) | Unverified | ✅ Verhoeff, but not on the UIDAI page |

Rules: 12 digits, Verhoeff check digit, first digit not `0`/`1`. The `9999` prefix
marks the test series. The UIDAI test records' **emails and phones must not be
copied**: `dummyemail.com` and `mailserver.com` are registered domains (✅ DNS), and
the 10-digit phone values (`2810806979` …) look like landline numbers. UBL rarely
carries Aadhaar. Use these only for a consumer party's national ID, if at all.

## A4. Company, bank and payment identifiers

| Identifier | Rule / value | Status | Notes |
|---|---|---|---|
| CIN (MCA) | 21 chars: `L`/`U` + 5-digit NIC 2008 activity code + 2-letter state + 4-digit year + 3-letter class (`PTC`, `PLC`, `OPC`, `NPL`, `GOI`, `SGC`, `FTC`, `ULL`, `ULT`) + 6-digit ROC number | — | No checksum. No MCA-published example was found; examples on the web (`U74999MH2020PTC345678` etc.) come from consultancies, not MCA. MCA's free CIN lookup was not tested |
| LLPIN | `AAA-9999` | — | No official example found |
| IFSC (RBI) | 11 chars: 4-letter bank code + `0` + 6-char branch | — | 5th char `0` is "reserved for future use" (RBI NEFT FAQ, via Wikipedia). **No official test IFSC exists.** `TEST0001234` is a Cashfree sandbox value (private) |
| IFSC in NIC sample | `SBIN11000` | **Avoid** | ❌ 9 chars. `SBIN` is State Bank of India |
| Bank account in NIC sample | `5697389713210` | Published example | No checksum on Indian account numbers |
| UPI VPA | `name@handle` | — | **NPCI publishes no test VPAs.** `success@upi` / `failure@upi` (Juspay, Cashfree), `testsuccess@gocash` (Cashfree) and `customer@upi` (PayU) are private gateway sandbox values |
| HSN code | e.g. `1006` rice, `1001` wheat and meslin (HS 2022 chapter 10) | Published example | The NIC sample pairs `"PrdDesc": "Rice"` with `"HsnCd": "1001"`, which is semantically wrong. Use `1006` for rice |
| Vehicle number (e-way bill) | State + RTO + series + 4 digits, e.g. `KA01AB1234` | — | No official fictitious plates found. The NIC sample `ka123456` is malformed |

## A5. PIN codes and addresses

| Finding | Detail | Status |
|---|---|---|
| Structure | 6 digits. 1st digit = region (`1`–`8` geographic), 1st–2nd = postal circle, 1st–3rd = sorting district, last 3 = delivery office | India Post via the UPU and Wikipedia (citing *Post Office Guide Part I*) |
| First digit `9` | Army Postal Service / Field Post Offices | **Avoid** for civilian parties (real military routing) |
| First digit `0` | Not used by any region | Derived: `0xxxxx` fails any PIN-existence check |
| UPU *Postal addressing systems — India* (01/2013) | `Mr. Rajiv Rattan, 4, Amrita Shergill Road, New Delhi 110003`; `Mr. N Gopalarathnam, 32/1, 2nd Main Road, 8th Block, Jayanagar, Bangalore, Karnataka 560082`; `Popular Electronics, Astro High Complex, Near Old Taxi Stand, Main Road, Ranchi, Jharkhand 834001-34`; P.O. box: `Post Box No. 4380, Kalkaji Post Office, New Delhi 110019` | Published example (real streets and PINs, fictitious-looking names). Amrita Shergill Road is a real New Delhi street |
| NIC e-invoice sample | `5th block, kuvempu layout`, `GANDHINAGAR`, PIN `518001` (state 37); `7th block, kuvempu layout`, PIN `562160` (state 29) | Published example. PIN/state pairs are plausible; not checked against the India Post directory |

No official PIN-directory API was used. data.gov.in requires an API key, and the
"IndiaPost/pin" GitHub repository (2015) is incomplete and not demonstrably official.
**PIN existence was therefore not verified.**

## A6. Telephone numbers

**No reserved fictional range was found.** Neither TRAI nor DoT reserves one: National
Numbering Plan 2003, TRAI recommendations of 2020 and 2025, searched in English and
Hindi. Mobile numbers are 10 digits starting `6`–`9`. The NIC sample's `9000000000`
is a valid-looking mobile number. Its `91111111111` has 11 digits and is malformed.
Recommendation: same approach as for Italy. Use a clearly patterned number and accept
that it is Derived, or omit the telephone.

## A7. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `example.com`, `*.example`, `*.test` | Reserved | RFC 2606 / RFC 6761 |
| `example.in` | Derived | ✅ NXDOMAIN (unregistered), but **not reserved**: anyone could register it |
| `example.co.in` | **Avoid** | Registered (DNS NS records present) |
| `abc@gmail.com`, `xyz@yahoo.com` (NIC sample) | **Avoid** | Real mail providers |
| `dummyemail.com`, `mailserver.com` (UIDAI test data) | **Avoid** | Registered domains (parked) |

---

# Part B — Singapore

## B1. Official UBL examples: PINT-SG (InvoiceNow)

InvoiceNow is Peppol. Its mandatory profile is **PINT-SG**
(`urn:peppol:pint:billing-1@sg-1`), syntax OASIS UBL 2.1 Invoice and CreditNote.
OpenPeppol and IMDA publish the specification at
[docs.peppol.eu/poac/sg/pint-sg](https://docs.peppol.eu/poac/sg/pint-sg/). Its
`resources.zip` (downloaded 2026-11-05) contains **15 Invoice examples and 1 Credit
Note example**. They cover:

- standard rated, zero rated and non-GST registered invoices;
- allowances and charges;
- foreign currency and foreign buyer;
- factored invoices and prepayment;
- decimals;
- AGD (government) invoices with PO reference;
- payment by SG bank transfer, GIRO, PayNow and credit card;
- GST in SGD.

It also contains schematrons, code lists and a stylesheet. IMDA's *InvoiceNow
Enterprise Best Practice Guide* v1.1 and the *TX2 Annex — Data specifications* reuse
the same party data.

### B1.1 Party data in the official examples

| Element | Value | Status | Checks |
|---|---|---|---|
| Seller name | `Gallery Photo Supplier` | Published example | ✅ no ACRA entity name contains it |
| Seller UEN / EndpointID | `200212345Z` / `0195:SGUEN200212345Z` | Published example | ❌ **check letter wrong** (correct: `E`) · ✅ neither form is in the ACRA register |
| Buyer UEN / EndpointID | `200254321Z` / `0195:SGUEN200254321Z` | Published example | ❌ check letter wrong (correct: `C`) · ✅ not in the register |
| Buyer name | `IMDA`, `Buyer trade name`, `AGD` | **Avoid** (`IMDA`, `AGD`) | Real government bodies |
| Seller UEN (ex. 07 foreign buyer) | `SGUEN201012456C` | **Avoid** | ✅ valid check letter, but **real**: SINGTEL MOBILE SINGAPORE PTE. LTD. (ACRA, registered 2010-06-10) |
| AGD buyer | `T08GA0028A`, `0195:SGUENT08GA0028A` | **Avoid** (unless a real government buyer is intended) | ✅ valid check letter. Real UEN of the Accountant-General's Department, the government's central e-invoice receiving point |
| Payee ID (Enterprise guide) | `200212345Y` | Published example | ❌ check letter |
| Payee legal ID | `5507983699` | Published example | Not a Singapore format |
| GST reg. no. | `M2-1234567-K` (= `M21234567K`), `M2-7654321-K`, `MR85004322` | Published example | `M21234567K` is also IRAS's own example (see B2). No public check algorithm |
| GST reg. no. (AGD example) | `SGTSTIMDADEMO01` | Published example | Explicit IMDA test/demo value. Not a valid GST-number format |
| Other legal ID | `C19002826A` | Published example | Not a valid UEN format |
| Buyer party ID | `345KS5324` (schemes `0035`, `0195`, `0199`) | Published example | Placeholder |
| GLN (`0035`/`0088`) | `5790000436071` | **Avoid** | ✅ GS1 check digit valid, but prefix 579 is GS1 Denmark. Copied from EU Peppol examples; owner unknown |
| GLN | `1234567890121`, `6754238987648` | **Avoid** | ❌ GS1 check digit |
| Addresses | `Mainstreet 112, Building 3, Singapore 1000`; `Central road 56, Second floor, 101`; `888 Jalan Ang Teng 560009`; `Central road 56, 321156`; `111 Somerset Road 238164` | Published example | ✅ `1000`, `101` not 6-digit SG postcodes · ✅ `560009`, `321156` not found in OneMap · `111 Somerset Road 238164` is a **real** building (OneMap) |
| Telephone | `4621230`, `5121230`; annex `887 654 321`, `876 654 321` | Published example | ❌ not 8-digit SG numbers |
| Email | `john@salescompany.sg`, `Buyer@buyer.sg` | Published example | ✅ both domains NXDOMAIN (unregistered, not reserved) |
| Email | `peter@seller.org`, `bill@imda.sg`, `einvoice@imda.gov.sg`, `test_vendor@gmail.com` | **Avoid** | Registered domains / real IMDA mailbox / real provider |
| Account / branch | `000166000001`, `17173211234567890`, `93274234`; branch/BIC `ICDLOG` | Published example | `ICDLOG` is not a valid BIC (6 chars) |
| PayNow proxy | `UEN123456879` (`PaymentMeansCode Z02`) | Published example | Not a valid UEN |
| TX2 annex UENs | `202012345M`, `SGUEN202345678A` | Published example | ❌ check letters wrong. **The corrected forms `202012345H` (VMG TECH PTE. LTD.) and `202345678W` are real ACRA entities: do not "fix" these** |

The PINT-SG schematrons check that identifiers are present but **not** UEN check
letters, so the official examples validate despite the wrong letters. A stricter
validator (python-stdnum `sg.uen`) rejects them.

### B1.2 Recommended corrected / derived UENs (pass the check letter, permanently unused)

The safest Singapore pattern is the ROC (local company) format `yyyynnnnnX`. Pick a
**past year whose serial range is closed** and a serial above that year's maximum.
Such a number can never be issued. The maximum serial was computed from the full ACRA
register: for example, 2002 has 11,162 companies with a maximum serial of 11246. For
2018 and later, serials up to 99999 exist, so avoid those years.

| UEN | Basis | Status | Checks |
|---|---|---|---|
| `200212345E` | PINT-SG seller `200212345Z` with correct check letter | Derived | ✅ check letter · ✅ not in ACRA register · serial 12345 > 2002 max 11246 |
| `200254321C` | PINT-SG buyer `200254321Z` with correct check letter | Derived | ✅ · ✅ not in register · serial > 2002 max |
| `201054321Z` | 2010, serial 54321 (2010 max 27553) | Derived | ✅ · ✅ not in register |
| `200599999K` | 2005, serial 99999 | Derived | ✅ · ✅ not in register |
| `201799990E` | 2017, serial 99990 (2017 max 37283) | Derived | ✅ · ✅ not in register |
| `99000001W`, `99000002L`, `99000003J` | ROB (business) format. Highest issued prefix is `53`; `54`–`99` unused | Derived | ✅ · ✅ not in register. Will remain free for decades, but not formally closed |
| `T99LL0001J` | "Others" format, LLP, year 2099 | Derived | ✅ check letter · ✅ not in register |

GST number: for most entities the **GST registration number is the UEN**, so a
derived UEN also serves as `cac:PartyTaxScheme/cbc:CompanyID`. The Peppol endpoint is
`<cbc:EndpointID schemeID="0195">SGUEN200212345E</cbc:EndpointID>`.

### B1.3 UEN check-letter algorithms (verified against the register)

ACRA does not publish these algorithms. The ones below come from python-stdnum and
community sources. ✅ They were verified against all 2.1 M ACRA records.

| Format | Rule | Register result |
|---|---|---|
| ROB `nnnnnnnnX` | weights `10,4,9,3,8,2,7,1`; letter = `XMKECAWLJDB`[sum mod 11] | 1,046,235 pass / 11 fail (1990s legacy numbers) |
| ROC `yyyynnnnnX` | weights `10,8,6,4,9,7,5,3,1`; letter = `ZKCMDNERGWH`[sum mod 11] | 1,026,719 pass / 0 fail |
| Others `[TSR]yyPQnnnnX` | alphabet `ABCDEFGHJKLMNPQRSTUVWX0123456789`; weights `4,3,5,3,10,2,2,5,7` on the 9 chars (alphabet index); letter = alphabet[(sum − 5) mod 11] | 54,124 pass / 0 fail |

Limit: the open dataset contains **ACRA-issued UENs only** (2,127,089 rows).
"Others" UENs from other agencies (government `GA`, societies, schools…) are not in
it, so `T…` candidates are checked against ACRA only.

## B2. GST registration numbers (IRAS)

| Element | Value | Status | Notes |
|---|---|---|---|
| UEN used as GST number | `123456789A` (IRAS "UEN: 123456789A GST Reg No.: 123456789A") | Published example | ❌ not a valid UEN (year `1234`, wrong letter) |
| Separate GST number | `M21234567K`, written also `M2-1234567-K` | Published example | IRAS *Invoicing customers* page. Format `M` + check char + 7 digits + check letter (10 chars). **No public check algorithm**, not verified |
| IRAS *Check GST Register* API sandbox | Test data in "Section 4.4" of the API spec | Not obtained | apisandbox.iras.gov.sg was "temporarily unavailable". Spec zip not downloadable |

## B3. NRIC / FIN — official sandbox personas (GovTech / Singpass Myinfo)

The Myinfo v3/v4 *person-sample* API
(`https://sandbox.api.myinfo.gov.sg/com/v4/person-sample/{uinfin}`, no auth) supports
these test NRIC/FINs, as listed in the Singpass developer docs, Myinfo v4 Tutorial 1:

| Values | Status | Checks |
|---|---|---|
| `S9812381D`, `S9812382B`, `S9812385G`, `S9812387C`, `S9812379B`, `S9912363Z`, `S9912366D`, `S9912369I`, `S9912370B`, `S9912372I`, `S9912374E`, `S6005053H`, `S6005055D` | Published example (sandbox personas) | ✅ check letter (all 13) |
| `F1612347K`, `G1612348Q`, `G1612349N`, `G1612350T`, `G1612352N`, `G1612353L` | Published example (sandbox personas) | ✅ check letter (all 6) |

Check-letter rule (S/T/F/G): weights `2,7,6,5,4,3,2` on the 7 digits, `+4` for T/G,
then index `sum mod 11` into `JZIHGFEDCBA` (S/T) or `XWUTRQPNMLK` (F/G). ICA does not
publish the rule. ✅ It matched all 19 sandbox values. The `M` series (FINs from 2022)
uses a different table and was not verified.

The persona data must not be copied wholesale. ✅ The API returned `S9812381D` =
`TAN XIAO HUI` with:

- a **real** residential address: 102 Bedok North Avenue 4, #09-128, Pearl Garden,
  460102 (✅ OneMap);
- mobile `+65 97399245`, which is in the live mobile range;
- email `myinfotesting@gmail.com`.

Use the NRIC numbers only. Note that sandbox NRIC/FINs are not formally reserved and
could coincide with real people's numbers. NRICs are not treated as secret (since the
2024 policy change), but avoid putting them in party data unless a consumer ID is
needed.

## B4. Postal codes and addresses

| Finding | Detail | Status |
|---|---|---|
| Format | 6 digits. First two = postal sector (`01`–`82`). Last four = delivery point (one code per building) | UPU / SingPost |
| Sector `74` | Missing from the URA district-sector list; ✅ `740000`, `741234` not found in OneMap | Derived (not exhaustively verified) |
| `83`–`99`, `00` | Beyond the sector range; ✅ `830000`, `990000`, `000000` not found in OneMap | Derived (fails existence check) |
| UPU *Postal addressing systems — Singapore* (07/2009) | `Ms. Tan Bee Soo` / `16 Sandilands Road` / `SINGAPORE 546080`; `Mr. M. Rajendran` / `Blk 35 Mandalay Road` / `# 13–37 Mandalay Towers` / `SINGAPORE 308215` | Published example. ✅ **both are real addresses** (OneMap). Fictitious person at a real address, the same pattern as La Poste in France |
| Unit format | `#13-37` = floor 13, unit 37 | UPU |

Address strategy: (A) a real postcode and street with an invented unit, as in the UPU
pattern, passes OneMap; (B) the PINT-SG style, an invented street with a non-existent
6-digit code such as `560009`, passes format checks only.

## B5. Telephone numbers

IMDA *National Numbering Plan* (Issue 2, February 2026) §2.2.1: numbers whose first
digit has no assigned service type "are reserved for future requirements and cannot
be used". The leading digits **`2`, `4` and `5`** are such digits (`3` VoIP, `6`
fixed, `8`/`9` mobile, `0`/`1`/`7` special).

| Range | Status | Notes |
|---|---|---|
| `+65 4xxx xxxx`, `+65 5xxx xxxx`, `+65 2xxx xxxx` | Derived | Cannot be assigned under the current plan. **No range is reserved for fiction** (searched IMDA and Wikipedia). libphonenumber will flag them as invalid |

## B6. Bank and payment identifiers

| Element | Value / rule | Status | Notes |
|---|---|---|---|
| Bank code | 4 digits (e.g. `7171` DBS), branch 3 digits; no IBAN in Singapore | — | No official test bank code found |
| BIC | 8th char `0` marks a test BIC (ISO 9362), e.g. `XXXXSGS0` | Reserved (convention) | Same as the France file |
| PayNow proxy | UEN (type 2) or `+65` mobile (type 0), plus optional 3-char suffix | — | **No public PayNow test environment or test proxy** (ABS/MAS SGQR spec; bank FAQs) |
| PINT-SG payment means codes | `30` bank transfer, `54` credit card, `Z01` GIRO, `Z02` PayNow | Published example | From the PINT-SG examples |

## B7. Email and web domains

| Value | Status | Notes |
|---|---|---|
| `example.com`, `*.example`, `*.test` | Reserved | RFC 2606 / RFC 6761 |
| `example.sg`, `buyer.sg`, `salescompany.sg` | Derived | ✅ NXDOMAIN, but not reserved |
| `test.sg`, `seller.org`, `imda.sg` | **Avoid** | Registered |

---

# Part C — Avoid lists

## C1. India

| Value | Seen as | Why |
|---|---|---|
| `37ARZPT4384Q1MT` | NIC sample seller GSTIN | 14th char `M`, check char wrong |
| `29AWGPV7107B1Z1`, `12AWGPV7107B1Z1` | NIC sample buyer / transporter | Check char wrong; PAN possibly real ("VIKAS EXPORTS") |
| `29AAFCD5862R000` etc. | ClearTax GSP sandbox | Not valid GSTINs |
| `ABCDE1234F` | Placeholder PAN | Invalid holder type |
| `SBIN11000` | NIC sample IFSC | Malformed; real bank prefix |
| `abc@gmail.com`, `xyz@yahoo.com`, `*@dummyemail.com`, `*@mailserver.com` | NIC / UIDAI samples | Real providers / registered domains |
| PIN `9xxxxx` | — | Army Postal Service |
| HSN `1001` for rice | NIC sample | Wrong code (`1001` = wheat) |
| `243001` with Mumbai | UIDAI test resident | Bareilly PIN |

## C2. Singapore

| Value | Seen as | Why |
|---|---|---|
| `201012456C` | PINT-SG example 07 seller UEN | Real: Singtel Mobile Singapore Pte. Ltd. |
| `T08GA0028A` | PINT-SG example 05 buyer | Real: Accountant-General's Department |
| `202012345H`, `202345678W` | "Corrected" IMDA annex UENs | Real ACRA entities |
| `200212345Z`, `200254321Z`, `202012345M`, `202345678A`, `200212345Y` | IMDA official examples | Wrong check letters (use B1.2 instead) |
| `IMDA`, `AGD` as party names | PINT-SG examples | Real government bodies |
| `111 Somerset Road 238164`, `102 Bedok North Ave 4 460102` | PINT-SG / Myinfo | Real buildings (fine for addresses only with fictitious names) |
| `+65 97399245`, `myinfotesting@gmail.com` | Myinfo persona | Live-range mobile; real mail provider |
| `5790000436071` | PINT-SG GLN | GS1 Denmark prefix, possibly a real GLN |
| `peter@seller.org`, `einvoice@imda.gov.sg`, `test_vendor@gmail.com` | PINT-SG / IMDA guide | Registered domains / real mailbox |
| `ICDLOG`, `UEN123456879`, `4621230` | PINT-SG examples | Invalid BIC / proxy / phone formats |

---

# Part D — Not verified / open points

- **NIC e-invoice sandbox pages** (`einv-apisandbox.nic.in`) and **einvoice1.gst.gov.in**
  could not be fetched (503 / connection reset). The six test GSTINs are confirmed via
  search-engine extracts and a GSP's documentation, not by direct download.
- The **e-Way Bill sandbox** test GSTIN `05AAACG2140A1ZL` comes from secondary sources
  only, and its PAN owner is unknown.
- No GSTIN/PAN existence check was possible (captcha), and no PIN-code existence check
  (no keyless official API).
- **IRAS Check GST Register** sandbox test data (spec §4.4) could not be obtained. The
  `M…` GST-number check algorithm is unknown.
- **Singpass Myinfo v5 test personas** are only in a downloadable file linked from the
  developer docs; not retrieved.
- No official India or Singapore source reserves telephone numbers, domains, postcodes
  or company numbers for fiction. Everything in those categories is Derived.

---

# Sources

**India**
- NIC e-Invoice API sandbox: [Home](https://einv-apisandbox.nic.in/) · [Sync GSTIN Details from CP](https://einv-apisandbox.nic.in/version1.03/Sync-GSTIN-Details-from-CP.html) · [Generate IRN](https://einv-apisandbox.nic.in/version1.03/generate-irn.html) · [FAQs on API](https://einv-apisandbox.nic.in/FaqsonAPI.html)
- GSTN: [e-Invoice bulk generation tools / schema](https://einvoice1.gst.gov.in/Others/BulkGenerationTools) · [API details of the 6 IRPs (PDF)](https://tutorial.gst.gov.in/downloads/news/e-invoice_api_integration_guide_irps.pdf) · [IRIS IRP sandbox access](https://einvoice6.gst.gov.in/content/kb/access-to-sandbox/)
- GSP documentation (secondary): [Masters India — Sync GSTIN](https://docs.mastersindia.co/e-invoicing-api/sync-gstin-details-from-cp) · [Vayana — Generate e-invoice sample](https://docs.gsp.vayana.com/E-Invoice/generate-einvoice-api/) · [ClearTax GSP sandbox GSTINs](https://docs.cleartax.in/cleartax-docs/e-invoicing-gsp-api/getting-started-with-einv-gsp-api/sandbox-gstin-for-einv-gsp) · [India Compliance sandbox](https://docs.indiacompliance.app/docs/developer-guide/sandbox)
- UIDAI: [Data and Downloads (test UIDs)](https://uidai.gov.in/en/data-and-download) · [Developer Section](https://uidai.gov.in/en/developer-section) · [PIB: Face Authentication SDK and Sandbox (2026-09)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2308398&reg=48&lang=2)
- DGFT IEC = PAN: [Trade Notice 09/2017 (reproduced)](http://worldtradescanner.com/09-TN-12.06.2017.htm)
- RBI IFSC format: [Wikipedia, citing RBI NEFT FAQ](https://en.wikipedia.org/wiki/Indian_Financial_System_Code) · [RBI IFSC lookup](https://www.rbi.org.in/Scripts/IFSCMICRDetails.aspx)
- PIN codes: [UPU — Postal addressing systems, India](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/indEn.pdf) · [Wikipedia — Postal Index Number](https://en.wikipedia.org/wiki/Postal_Index_Number)
- Telephone: [TRAI recommendations 2020 (PDF)](https://www.trai.gov.in/sites/default/files/2024-09/Recommendations_29052020.pdf)
- Payment gateway sandboxes (private, for contrast): [Juspay test resources](https://juspay.io/in/docs/resources/docs/common-resources/test-resources) · [Cashfree sandbox test data](https://www.cashfree.com/docs/api-reference/payments/data-to-test-integration)

**Singapore**
- OpenPeppol / IMDA PINT-SG: [Specification](https://docs.peppol.eu/poac/sg/pint-sg/) · [resources.zip (examples, schematron)](https://docs.peppol.eu/poac/sg/pint-sg/resources.zip)
- IMDA: [InvoiceNow Enterprise Best Practice Guide v1.1](https://file.go.gov.sg/invoicenow-enterprise-guide.pdf) · [TX2 Annex — Data specifications](https://www.imda.gov.sg/-/media/imda/files/programme/nationwide-e-invoicing-framework/invoicenow-technical-playbook/tx2---annex---data-specifications.pdf) · [TX3 Access Point services](https://www.imda.gov.sg/-/media/imda/files/programme/nationwide-e-invoicing-framework/invoicenow-technical-playbook/tx3---access-point-services-release.pdf) · [National Numbering Plan](https://www.imda.gov.sg/-/media/imda/files/regulation-licensing-and-consultations/frameworks-and-policies/numbering/national-numbering-plan-and-allocation-process/imda-national-numbering-plan.pdf)
- ACRA open data: [Entities Registered with ACRA (data.gov.sg)](https://data.gov.sg/datasets/d_3f960c10fed6145404ca7b821f263b87/view) · [ACRA Information on Corporate Entities](https://data.gov.sg/collections/2/view)
- IRAS: [Invoicing customers (GST number examples)](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/basics-of-gst/invoicing-price-display-and-record-keeping/invoicing-customers) · [Check GST Register API (sandbox)](https://apisandbox.iras.gov.sg/iras/devportal/sb/product/20287)
- Singpass / GovTech: [Myinfo v4 Tutorial 1 — person sample data](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v4/tutorials/tutorial-1-myinfo-person-sample-data) · [Myinfo test personas (v5)](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) · [Sample person API](https://sandbox.api.myinfo.gov.sg/com/v4/person-sample/S9812381D)
- SLA OneMap: [Search API](https://www.onemap.gov.sg/apidocs/)
- UPU: [Postal addressing systems — Singapore](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/sgpEn.pdf)
- Postal sectors: [Wikipedia — Postal codes in Singapore](https://en.wikipedia.org/wiki/Postal_codes_in_Singapore)
- PayNow / SGQR: [MAS — SGQR](https://www.mas.gov.sg/development/e-payments/sgqr) · [ABS PayNow business FAQ](https://abs.org.sg/docs/library/paynow-launch---business-faqs.pdf)

**Common**
- [python-stdnum 2.2](https://pypi.org/project/python-stdnum/) (`in_.gstin`, `in_.pan`, `in_.aadhaar`, `sg.uen`; used as reference, not executed)
- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- GS1: [Company Prefix (`952` reserved for demonstrations)](https://www.gs1.org/standards/id-keys/company-prefix)
