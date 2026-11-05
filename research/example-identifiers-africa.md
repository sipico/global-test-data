# Fictitious-but-valid example identifiers — South Africa, Kenya, Nigeria, Egypt

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with English queries plus Afrikaans (South Africa),
Swahili (Kenya) and Arabic (Egypt) queries. Checks marked ✅ were run during research:
SARS modulus-10 (= Luhn) on tax/VAT/PAYE numbers, Luhn on SA ID numbers, CBN NUBAN
check digit, IBAN mod-97, phone number validation with libphonenumber 9.0.42, and DNS
NS lookups for domains. Official files (SARS BRS, ICASA and CA Kenya numbering plans,
CBN NUBAN circulars, KRA OSCU/VSCU specs, ETA Postman collection, NRS e-invoicing
portal bundle, UPU addressing sheets) were downloaded and read.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**

- **None of the four countries has a UBL e-invoicing system with official UBL XML
  examples.** Nigeria's NRS (formerly FIRS) system is officially "UBL"/"Peppol-based",
  but its API takes a snake_case JSON derived from UBL, not UBL XML. Egypt (ETA) and
  Kenya (KRA eTIMS) use their own JSON/XML formats. South Africa (SARS) is still
  consulting (Aug 2026 paper names Peppol PINT, EN 16931 and CII as options).
- Best official finds: SARS publishes **worked examples that pass its own check digit**
  (tax reference `0001339050`, PAYE `7230767891`, ID number `8001015009087`); ICASA
  **reserves geographic test ranges** `0XX 114/115/116/117`; CA Kenya reserves NDC
  **`199`** for network testing; KRA uses the obviously fictitious PIN
  **`A123456789Z`** / `P123456789Z` in its specs; SWIFT/CBE publish an Egyptian example IBAN.

---

## 1. South Africa

### 1.1 Tax identifiers (SARS)

Primary source: SARS *PAYE Employer Reconciliation BRS* (v15.0.0 2016, Appendix B
"Number validations"; the same examples are still in v23.0.0, 2024). The algorithm is
the same as Luhn on 10 digits: double digits 1, 3, 5, 7, 9 (sum the digits of the
product), add digits 2, 4, 6, 8; check digit = `(10 − total mod 10) mod 10`.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Income tax reference number | `0001339050` | Published example | ✅ SARS modulus 10 · BRS §9.1 worked example. Existence not checked (no open lookup) |
| PAYE / SDL / UIF reference | `7230767891` / `L230767891` / `U230767891` | Published example | ✅ modulus 10 with the first character replaced by `4` (BRS §9.2) |
| VAT registration number | — | — | No official example found. SARS: "10 digits and starts with the number 4" (VAT vendor search help). The check digit is the same modulus 10 rule (unverified for VAT in a SARS document; the PAYE rule of replacing the first digit with `4` suggests it) |
| VAT number (derived) | `4000000002`, `4111111110`, `4999999990` | Derived | ✅ modulus 10. **Not checked against the register**: the SARS VAT vendor search (`secure.sarsefiling.co.za/vatvendorsearch`) is interactive only |
| Income tax ref (derived, non-individual) | `9000000001`, `9111111119` | Derived | ✅ modulus 10. Starts with `9` = Nature of Person E/G/H (trusts, etc.) per BRS; `0`–`3` = individuals/companies |

Rules (BRS): income tax number is 10 digits, starts with `0`, `1`, `2`, `3` or `9`;
PAYE starts with `7`, SDL with `L`, UIF with `U` (same last 9 digits).

E-invoicing: SARS *VAT Modernisation Consultation Paper* (Aug 2026, comments closed
16 Oct 2026) proposes a decentralised CTC model with accredited service providers and
names EN 16931 CIUS, UN/CEFACT CII and Peppol PINT BIS as candidate standards. No
schema, CIUS or test environment exists yet. No Peppol Authority appointed.

### 1.2 Company registration (CIPC)

| Element | Value | Status | Notes |
|---|---|---|---|
| Enterprise (registration) number | `YYYY/NNNNNN/TT` | — | **No check digit**, so nothing to validate beyond format. Type codes (secondary sources, not verified on cipc.co.za): `06` public, `07` private (Pty) Ltd, `08` non-profit, `21` personal liability (Inc), `23` close corporation |
| No official fictitious enterprise number found | — | — | A derived value such as `2099/000001/07` (future year) cannot exist, but fails any "year ≤ today" check |

### 1.3 Personal identity number

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| ID number | `8001015009087` | Published example | ✅ Luhn. Worked example in SARS PAYE BRS §9.3 ("Modulus 13 check on ID number"; it is actually Luhn). Structure `YYMMDD SSSS C A Z`: born 1980-01-01, male (`5009`), SA citizen (`0`), `8`, check `7`. **Caveat:** a real person could hold it — it is also the most-copied SA "example ID" on third-party sites |
| ID number (derived) | — | — | Every Luhn-valid number with a plausible date could be real. No Home Affairs specimen number found. Prefer `8001015009087` (the SARS one) or leave the personal ID out |

### 1.4 Telephone numbers (ICASA)

| Range | Status | Notes |
|---|---|---|
| `0XX 114 xxxx`, `0XX 115 xxxx`, `0XX 116 xxxx`, `0XX 117 xxxx` (any geographic area code `0XX`) | **Reserved** (for network testing) | ICASA Numbering Plan Regulations 2016, reg. 15(4): "reserved for testing purposes … licensees … may utilize these numbers and need not apply". Not changed by the 2023 amendment (Gazette 48328) or the 2026 amendments. E.g. `021 114 0000` → `+27 21 114 0000` (Cape Town), `011 115 0000` (Johannesburg). ✅ libphonenumber: valid fixed-line |

Not a "drama" range: test numbers may be used by operators for network tests, so a
call could reach test equipment. No fiction/drama range found (English and Afrikaans
searches). No reserved mobile range.

### 1.5 Postal addresses (SAPO / UPU)

4-digit postcode on the last line (below the locality); no punctuation; locality / PO
name in upper case. Examples from UPU *Postal addressing systems — South Africa*
(02/2010):

| Example | Status |
|---|---|
| `Mr P. Rossouw` / `442 Thirteenth Avenue` / `FISH HOEK` / `7975` | Published example (real town + postcode) |
| `Mr. Jimmy Jones` / `1023 Collet Heights` / `449 Collet Drive` / `LYNDHURST` / `1852` | Published example |
| `TV Matemala` / `9285 Block E` / `KHAYELITSHA` / `1982` | Published example (informal area) |
| `Mr. Joko Oxo` / `c/o Bamba Zonke primary school` / `960401 Kwatsita Village` / `NTABANKULU` / `5170` | Published example (rural) |
| `Accounts` / `Development Bank of SA Limited` / `PO Box 92214` / `PROTEA PARK` / `0305` | **Avoid** — real organisation |

No fictitious town or unused postcode range was verified: SAPO's postcode list is not
available as open data (not checked).

### 1.6 Banking

| Element | Value | Status | Notes |
|---|---|---|---|
| IBAN | — | — | South Africa does not use IBAN |
| Branch code | 6-digit universal branch codes | — | All real (one per bank). No test code found |
| Account check digit (CDV) | — | — | BankservAfrica's CDV algorithm is not published openly (not verified) |
| BIC | 8th character `0` (e.g. `XXXXZAJ0`) | Reserved (convention) | ISO 9362 test BIC |

### 1.7 South Africa avoid list

| Value | Seen as | Why |
|---|---|---|
| `4734567892` | "Example VAT" (taxid.pro) | ❌ fails modulus 10 |
| `Development Bank of SA Limited, PO Box 92214` | UPU example | Real organisation |
| `example.co.za` | Placeholder domain | Not registered on 2026-11-05 (NXDOMAIN), but **not reserved**; use `.test` |

---

## 2. Kenya

### 2.1 Tax identifiers (KRA)

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| KRA PIN (individual) | `A123456789Z` | Published example | Used throughout KRA *OSCU Specification v2.0* and *VSCU Specification v2.0* JSON samples. Format `[AP]` + 9 digits + letter ✅. The check letter algorithm is not published, so it cannot be validated offline |
| KRA PIN (non-individual) | `P123456789Z` | Published example | VSCU spec (seller PIN). Also `A987654321Z`, `P123456789A` in the VSCU spec |
| Taxpayer / branch names | `TEST VSCU`, `TAXPAYER1`, `TAXPAYER2`, `Taxpayer1130`, `Headquater`, `MTEJA LIMITED` ("mteja" = customer) | Published example | `MTEJA LIMITED` not checked against the Business Registration Service |
| Branch ID (`bhfId`) | `00` (HQ), `01` | Published example | |
| Device serial | `dvcv1130` | Published example | OSCU spec |
| Item code | `KE1NTXU0000001` | Published example | KRA item code structure (country + type + origin + unit + serial) |
| Location | `NAIROBI CITY` / `WESTLANDS` / `Westlands Towers`, `NYUMBA TOWERS`, `KASARANI TOWERS` | Published example | Real county/sub-county names, invented buildings (not verified) |

Unverified claim (secondary source lookuptax.com): issued PINs start `A0…` / `P0…`. If
true, `A123456789Z` can never be issued; the leading `1` makes it a safe fictitious value.

eTIMS is not UBL: OSCU/VSCU are KRA-specific JSON APIs. Test server
`https://etims-api-sbx.kra.go.ke/etims-api/`; taxpayer sandbox portal
`https://etims-sbx.kra.go.ke` (sign-up uses your own real PIN; no shared test PIN).

### 2.2 Personal and company IDs

| Element | Notes |
|---|---|
| National ID | 7–8 digits (unverified), no published check digit. No official specimen found |
| Company number (BRS) | E.g. `PVT-…` format (unverified); no known check digit; not researched further |

### 2.3 Telephone numbers (Communications Authority of Kenya)

| Range | Status | Notes |
|---|---|---|
| `+254 199 xxx xxx` (NDC `199`, 9-digit NSN) | **Reserved** (network testing) | CA *Telecommunication Numbering Plan for Kenya* (Oct 2025): "Shared resource for internal use for purposes network testing, experimentations, and research". ⚠ libphonenumber 9.0.42 rejects it (`is_valid_number` = false) |

No fiction/drama range found (English and Swahili searches). `021`–`029`,
`031`–`039`, `047`–`049` are "reserved for future growth" — not safe, they may be assigned later.

### 2.4 M-Pesa (Safaricom Daraja sandbox)

| Element | Value | Status | Notes |
|---|---|---|---|
| Test MSISDN | `254708374149` | Published example | Shown as the example number in the Daraja portal simulator (portal JS bundle, checked). ✅ libphonenumber valid mobile — **a real Safaricom number format**, use only in payment-means test data, not as a contact phone |
| Test shortcode (M-Pesa Express) | `174379` | Published example (unverified at source) | Issued as per-app test credentials in the portal (not in the public page); widely documented by third parties |
| Other portal defaults | `600978` (reversal receiver), Till `1743791`, `300584` | Published example | Portal simulator defaults |

### 2.5 Postal addresses (Posta Kenya / UPU)

5-digit postcode of the delivery post office; P.O. Box addressing dominates. UPU
*Postal addressing systems — Kenya* (09/2004): `MR. JOHN BWANA` / `P O BOX 2784 – NAKURU GPO`
/ `20100` / `NAKURU` / `KENYA` — Published example (real postcode `20100` Nakuru,
`00100` Nairobi GPO). No fictitious town/postcode found.

### 2.6 Banking

Kenya does not use IBAN. No CBK-published account check digit or test account found.
Test BIC convention: `XXXXKEN0`.

### 2.7 Kenya avoid list

| Value | Seen as | Why |
|---|---|---|
| `0789001130`, `0789011130` | KRA OSCU/VSCU spec manager phones | ✅ valid Kenyan mobile numbers (real range) |
| `manage113000@test.com` | KRA OSCU spec | `test.com` is a registered domain |
| `test@gaoin.ke` | KRA VSCU spec | Not registered today (NXDOMAIN) but not reserved |
| `ODERICH CONSERVA QUALIDADE BRASIL` | VSCU import-item sample | Real Brazilian company |
| `254722001231`, `254726304245`, `254705912645` | Daraja portal defaults | Valid Kenyan mobiles, possibly real people |
| `P000591096X` | "Example KRA PIN" on third-party sites | Real company (Kenya Power) per secondary source |
| `https://mydomain.com/...` | Daraja callback URLs | Registered domain |

---

## 3. Nigeria

### 3.1 E-invoicing (NRS, formerly FIRS — Merchant-Buyer Solution)

NRS *Technical Overview on the National e-Invoicing System* (Apr 2025) says
"Peppol-Based e-Invoicing Network", "Structured (UBL Format)", and lists UBL, ISO 20022,
WCO HS and LEI as the standards adopted. The API docs at `einvoice.nrs.gov.ng/docs`
(single-page app; examples extracted from its JS bundle) show a **UBL-derived JSON**
(`accounting_supplier_party`, `invoice_type_code` `380`/`381`/`396`, `legal_monetary_total`
…) and an "XML" view with non-namespaced, non-UBL element names (`<Tin>`, `<Email>`).
**Not UBL 2.x XML; not usable as XSD-valid UBL examples.**

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| IRN (Invoice Reference Number) | `ITW001-E9E0C0D3-20240619`, `INV001-E9E0C0D3-20240619` | Published example | Structure `<invoice no>-<8-char service ID>-<YYYYMMDD>` |
| Supplier/customer TIN (API sample) | `TIN-0099990001`, `TIN-000001` | Published example | Placeholders; ❌ not Nigerian TIN format |
| TIN in field docs | `89487982-0001`, `33467982-0001`, `11223393-0001`, `29039239-0001`, `29334238-0001` | Published example | ✅ format `8 digits-4 digits`. No check digit known. **Not checked** (JTB TIN verification is interactive). Unknown whether real |
| Supplier TIN in field docs | `RN-847789` | Published example | RC-number-style ID (format invented) |
| Party names | `ABC Cement Ltd`, `XYZ Construction Ltd`, `ABC Holdings Ltd`, `ABC Tax Consultants Ltd` | Published example | Generic, not verified against CAC |
| Address | `32, Owonikoko Street`, `Ikeja`, `023401`; `45 Marina Road`, `Ikeja`, `101233`; `12 Tax Avenue`; state `NG-AB`, LGA `NG-AB-ANO` | Published example | ISO 3166-2:NG state codes; Marina is in Lagos Island, not Ikeja — internally inconsistent |
| Sandbox | `{{TEST_BUSINESS_ID}}` placeholders | — | Per-taxpayer API keys from the NRS portal; no shared test taxpayer |

### 3.2 Tax and company IDs

| Element | Notes |
|---|---|
| FIRS/JTB TIN | `NNNNNNNN-NNNN` (8 + 4 digits); no published check digit |
| Tax ID from Jan 2026 (Nigeria Tax Administration Act 2025) | NIN for individuals, CAC RC number for companies (FIRS statements, Dec 2025). Secondary sources disagree on a separate 13-digit NRS Tax ID (unverified) |
| CAC registration | `RC` + digits (companies), `BN` + digits (business names), `IT` (incorporated trustees); no check digit |
| NIN (NIMC) | 11 digits; no published check digit; no official test value. Third-party KYC sandboxes use their own (Dojah `70123456789`, Youverify `12345678901`) — provider-specific, not official |
| BVN (NIBSS) | 11 digits; no official NIBSS test value found. Dojah sandbox `22222222222` — provider-specific |

### 3.3 Banking — NUBAN (CBN)

Algorithm (CBN *Exposure circular on NUBAN*, 2018; *NUBAN proposals* v0.4, 2010):
16 digits `ABCDEF-GHIJKLMNO-P` = 6-digit institution code (bank `011` → `000011`;
OFI = `9` + 5-digit code) + 9-digit serial + check digit; weights
`3,7,3,3,7,3,3,7,3,3,7,3,3,7,3`; check = `(10 − sum mod 10) mod 10`. The account
number used in practice is the last 10 digits (serial + check).

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| NUBAN (DMB) | bank `011` + `0000014579` | Published example | ✅ CBN worked example (sum 81 → 9). `011` = First Bank, a real bank |
| NUBAN (OFI) | institution `950547` + `0000214579` | Published example | ✅ CBN worked example (sum 211 → 9) |
| NUBAN (2010 doc) | bank `011` + `0000000220` | Published example | ✅ check digit 0 |

Same caveat as France: bank codes are real; only the account serial makes these
fictitious, and a real account could exist. No IBAN in Nigeria. Test BIC: `XXXXNGL0`.

### 3.4 Telephone numbers (NCC)

**No reserved fictional or test subscriber range found.** NCC's draft numbering plan
report mentions short codes `15100`–`151XX` for operator "internal supervisory and test
signal codes" (short codes, not subscriber numbers). Do not invent Nigerian numbers.

### 3.5 Postal addresses (NIPOST / UPU)

6-digit postcode on the locality line ("Garki 900001"). UPU *Postal addressing systems
— Nigeria* (10/2022) examples: `Mr. Bukwa Okoro` / `Okukwo Nigeria Ltd` / `34 Alayande Cl` /
`Mokola 200212` / `Ibadan` / `OYO STATE`; `Mr Bukwa Okoro Kola` / `Adelboden Ltd` /
`P.O.Box. 125` / `Garki 900001` / `ABUJA` — Published example (real localities and
postcodes; company names not verified). No fictitious postcode found.

### 3.6 Nigeria avoid list

| Value | Seen as | Why |
|---|---|---|
| `Dangote Group` | Party name in the official NRS API samples | Real conglomerate |
| `supplier_business@email.com`, `business@email.com`, `paytest@email.com` | NRS samples | `email.com` is a real mail provider |
| `+23480254099000`, `+23480254000000` | NRS sample phones | ❌ wrong length (libphonenumber invalid) |
| `Gwarikpa`, `023401` | NRS sample city/postcode | Misspelling of Gwarinpa (Abuja); postcode not a known NIPOST code (not verified) |
| `NICON Insurance Corp. Plc`, `PMB 246 Garki` | UPU example | Real company |
| `22222222222`, `70123456789` | "Test BVN/NIN" | Third-party sandbox values only, not NIBSS/NIMC |

---

## 4. Egypt

### 4.1 E-invoicing (ETA — Egyptian Tax Authority)

Format: ETA-specific JSON or XML (not UBL), signed with CAdES-BES. Official SDK
`sdk.invoicing.eta.gov.eg`; preprod SDK `sdk.preprod.invoicing.eta.gov.eg`; preprod
portals `preprod.invoicing.eta.gov.eg`, `api.preprod.invoicing.eta.gov.eg`,
`id.preprod.eta.gov.eg`, `profile.preprod.eta.gov.eg`. Values below come from the
official Postman collection (*Egyptian eInvoicing SDK R3.0*) and the *Invoice v1.0* page.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Issuer registration number (RIN) | `674859545` | Published example | 9 digits ✅ format. Probably a preprod test taxpayer; **not verified** (no open lookup). No published check digit |
| Receiver RIN | `313717919`, `200000640` | Published example | Same caveat |
| RIN in EGS item codes | `113317713` (`EG-113317713-123456`), `100000053` | Published example | EGS code = `EG-<RIN>-<internal code>` |
| Registration number in field docs | `10201020102` | Published example | ❌ 11 digits, does not match the 9-digit RIN |
| Names | `Issuer Company`, `Receiver`, `الشركة المصدرة` ("the issuing company"), `receiver`, `taxpayer 1`, `My company` | Published example | Generic |
| Branch ID | `0` | Published example | |
| Activity code | `4620` | Published example | ISIC-based activity code |
| Address (docs) | `Giza Governorate` / `Dokki` / `17 Nabil Al Wakad` / building `17` | Published example | Real street in Dokki |
| Address (Postman) | `580 Clementina Key`, `7660 Melody Trail`, postcode `68030` | Published example | Faker-generated US-style strings; not Egyptian |
| Receiver types | `B` business (RIN), `P` person (national ID), `F` foreign (VAT ID) | — | |

### 4.2 Tax, company and personal IDs

| Element | Notes |
|---|---|
| Tax registration number (RIN) | 9 digits (`000-000-000` on the tax card); also the e-invoice issuer ID. No published check digit |
| National ID (الرقم القومي) | 14 digits: century (`2` = 1900s, `3` = 2000s) + `YYMMDD` + 2-digit governorate (`01` Cairo, `02` Alexandria, `21` Giza, `88` born abroad) + 4-digit serial (13th digit odd = male) + check digit. **Check digit algorithm not published** (Arabic and English searches) — cannot be validated. No official specimen found |

### 4.3 Banking

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| IBAN | `EG38 0019 0005 0000 0000 2631 8000 2` | Published example | SWIFT IBAN Registry (Egypt entry, contact Central Bank of Egypt), 29 characters; ✅ mod-97. Bank code `0019` and branch `0005` are probably real |
| Test BIC | `XXXXEGC0` | Reserved (convention) | ISO 9362 |

### 4.4 Telephone numbers (NTRA)

**No reserved fictional or test range found** (Arabic and English searches of NTRA
material). Do not invent Egyptian numbers.

### 4.5 Postal addresses (Egypt Post / UPU)

7-digit postcode below the province. UPU *Postal addressing systems — Egypt* (07/2023):
`Mohamed Ahmed Mahmoud` / `30 Moussa Galal street` / `Al-Mohandessine` / `GIZA` /
`3759914`; `4 El-Mehata street - El-Zohor Village` / `Ville El-kharga` / `NEW VALLEY` /
`1062261` — Published example (real places). Note the ETA samples use 5-/6-digit
postcodes (`68030`, `098607`), which do not match the 7-digit system.

### 4.6 Egypt avoid list

| Value | Seen as | Why |
|---|---|---|
| `+201020567462` | ETA e-receipt sample buyer mobile | ✅ valid Egyptian mobile, possibly a real person |
| `037000401629`, `Samsung A02 32GB…` | ETA e-receipt sample item | Real GTIN prefix / real product |
| `Alpha Bank` | ETA bank name example | Real bank |
| `10201020102` | ETA field docs | Wrong length for a RIN |
| `580 Clementina Key`, `68030` | ETA Postman address | Non-Egyptian placeholder text |

---

## 5. Cross-country identifiers

| Element | Value / range | Status | Notes |
|---|---|---|---|
| GLN / GTIN | GS1 prefix `952` | Reserved | GS1 General Specifications (see France file §6). National prefixes (600–601 ZA, 615 NG, 616 KE, 622 EG) are for real companies |
| Email / web | `*.test`, `*.example`, `example.com/.net/.org` | Reserved | RFC 2606 / 6761. `example.co.za`, `example.co.ke`, `example.com.ng`, `example.com.eg` are not registered today but not reserved |
| Vehicle plates, customs IDs | — | — | No officially reserved example values found in any of the four countries (not researched in depth) |

---

## 6. Sources

- SARS: [PAYE Employer Reconciliation BRS v15.0.0](https://www.sars.gov.za/wp-content/uploads/Docs/PAYE/BRS/SARS_PAYE_BRS-PAYE-Employer-Reconciliation_V15-0-0.pdf) · [BRS v23.0.0](https://www.sars.gov.za/wp-content/uploads/Docs/PAYE/BRS/SARS_PAYE_BRS-PAYE-Employer-Reconciliation_V23-0-0.pdf) · [VAT Modernisation Consultation Paper (Aug 2026)](https://www.sars.gov.za/wp-content/uploads/VAT-Modernisation-Consultation-Paper-August-2026.pdf) · [VAT vendor search help](https://secure.sarsefiling.co.za/vatvendorsearch/application/HELP.html)
- ICASA: [Numbering Plan Regulations 2016](https://www.icasa.org.za/uploads/files/NumberingPlanReg.pdf) · [Amendment 2023 (Gazette 48328)](https://www.icasa.org.za/uploads/files/Amendment-of-the-Numbering-Plan-Regulations-2016.pdf) · [Numbering page](https://www.icasa.org.za/pages/numbering)
- KRA: [OSCU Specification v2.0](https://www.kra.go.ke/images/publications/OSCU_Specification_Document_v2.0.pdf) · [VSCU Specification v2.0](https://www.kra.go.ke/images/publications/VSCU_Specification_Document_v2.0.pdf) · [OSCU/VSCU sign-up guide](https://www.kra.go.ke/images/publications/OSCU_VSCU_Step-by-Step_Guide-on-how-to-sign-up.pdf) · [PIN without obligation guide](https://www.kra.go.ke/images/publications/Step-By-Step-Guide-for-Application-Of-PIN-Without-Obligation-PWO.pdf)
- CA Kenya: [Telecommunication Numbering Plan for Kenya, Oct 2025](https://www.ca.go.ke/sites/default/files/2025-10/Telecommunication%20Numbering%20Plan%20for%20Kenya%20October%202025[1].pdf)
- Safaricom: [Daraja developer portal](https://developer.safaricom.co.ke/)
- NRS (FIRS): [e-Invoicing developer docs](https://einvoice.nrs.gov.ng/docs/introduction) · [Technical Overview (Telcos), Apr 2025](https://einvoice.nrs.gov.ng/documents/Technical%20Overview%20on%20the%20National%20e-Invoicing%20System%20(Telcos).pdf)
- CBN: [Exposure circular on NUBAN (2018)](https://www.cbn.gov.ng/out/2018/psmd/exposure%20circular%20for%20nuban.pdf) · [NUBAN proposals v0.4 (2010)](https://www.cbn.gov.ng/OUT/2011/CIRCULARS/BSPD/NUBAN%20PROPOSALS%20V%200%204-%2003%2009%202010.PDF)
- NCC: [Development of a New Numbering Plan for Nigeria (draft report)](https://www.ncc.gov.ng/media/1066/view)
- Nigeria Tax ID change (secondary): [Guardian, Dec 2025](https://guardian.ng/business-services/nin-cac-numbers-to-serve-as-tin-from-2026-says-firs/)
- ETA: [eInvoicing SDK](https://sdk.invoicing.eta.gov.eg/) · [Invoice v1.0](https://sdk.invoicing.eta.gov.eg/documents/invoice-v1-0/) · [Postman collection](https://sdk.invoicing.eta.gov.eg/files/Egyptian%20eInvoicing%20SDK.postman_collection.json) · [FAQ (environments)](https://sdk.invoicing.eta.gov.eg/faq/) · [SDK links (preprod)](https://www.eta.gov.eg/sites/default/files/2021-09/SDK%20links_0.pdf)
- UPU addressing sheets: [South Africa](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/zafEn.pdf) · [Kenya](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/kenEn.pdf) · [Nigeria](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/ngaEn.pdf) · [Egypt](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/egyEn.pdf)
- SWIFT: [IBAN Registry](https://www.swift.com/resource/iban-registry-pdf)
- Secondary (format claims only): [lookuptax.com Kenya PIN](https://lookuptax.com/docs/tax-identification-number/kenya-tax-id-guide) · [Dojah sandbox data](https://guides.dojah.io/user-manual/identity-verification/sandbox-test-data) · [VLens Egyptian national ID decoder](https://vlenseg.com/en/egyptian-national-id-decoder/)
