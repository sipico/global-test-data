# Fictitious-but-valid example identifiers — Global / international

**Purpose:** same as `example-identifiers-fr.md`: identifiers that (a) pass format and
checksum validation, (b) are published or reserved by an official or authoritative
body (standards body, registration authority, scheme owner, regulator) for examples
or tests, and (c) cannot be confused with a real organisation. This file covers
**identifiers that are not tied to one country**. National identifiers (VAT, company
numbers, phone ranges, postcodes) are in the per-country files. All of this feeds the
canonical 26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05. Checks marked ✅ were run during research: Luhn (payment
cards), ICAO 9303 MRZ check digits (weights 7-3-1), GS1 mod-10, ISO 6346 check digit,
IMO check digit, ISO 7064 mod 97-10 (IBAN, LEI), ISSN mod-11, ISBN-10/13, VIN
(49 CFR 565 weights), a lookup in the GLEIF LEI API, and a lookup in Open Library for
the ISBNs.

Status legend (same as the France file):

| Status | Meaning |
|---|---|
| **Reserved** | An authority formally reserves the value/range for fiction, examples or tests |
| **Published example** | An authority uses the value in its own official examples, not formally reserved |
| **Derived** | Not published anywhere; computed by us from the format rules and checked to be unused |
| **Avoid** | Seen as an "example" somewhere but belongs to a real entity, has another real meaning, or fails validation |

**Headline:** truly *reserved* global values exist for: ISO 3166 user-assigned codes,
ISO 4217 `XTS`, ICAO "Utopia" (`UTO`), GS1 prefix `952`, SWIFT test-and-training BICs,
and the IETF/IANA documentation ranges (domains, IPv4/IPv6, ASN, MAC). **No reserved
range was found** for LEI, ISBN, ISSN, DOI (any more), IMO numbers, ISO 6346 owner
codes, VIN, IATA codes, ISO 6523 ICDs or E.164 country codes. Payment-card test PANs
are published by the schemes' own acquiring/gateway businesses (Visa Acceptance,
Mastercard Gateway), not by ISO or EMVCo.

---

## 1. Country, currency and location codes

### 1.1 ISO 3166-1 user-assigned codes

ISO 3166-1 (clause 8.1.3 in the 2006 edition; quoted on the ISO 3166 glossary page)
makes these available to users who need codes for names not in the standard. ISO will
never assign them to a country.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Alpha-2 | `AA`, `QM`–`QZ`, `XA`–`XZ`, `ZZ` | Reserved | User-assigned. ISO asks users to inform the ISO 3166/MA of such use |
| Alpha-3 | `AAA`–`AAZ`, `QMA`–`QZZ`, `XAA`–`XZZ`, `ZZA`–`ZZZ` | Reserved | Same |
| Numeric | `900`–`999` | Reserved | Same |
| **Recommended fictitious country** | `AA` / `AAA` / `900` | Derived | No conflicting real-world use found (see list below) |

Many user-assigned codes **already have a de-facto meaning** in systems a UBL document
may meet. Do not use these as a fictitious country:

| Code | Real-world meaning | Source |
|---|---|---|
| `XI` | United Kingdom (Northern Ireland) — EU VAT/EORI prefix; **in the Peppol/EN 16931 country list** | Peppol ISO 3166 code list |
| `XK` / `XKX` | Kosovo (EU, many registries); Peppol uses `1A` instead | Wikipedia (XK) |
| `XZ` | UN/LOCODE: installations in international waters (offshore platforms) | UNECE Rec. 16 |
| `ZZ` / `ZZZ` / `999` | Unicode CLDR "Unknown or Invalid Territory" | UTS #35 |
| `XX` | WIPO ST.3 "unknown states, other entities or organizations" | WIPO ST.3 |
| `QZ`, `XN`, `XU`, `XV` | WIPO ST.3: CPVO (EU plant varieties), Nordic Patent Institute, UPOV, Visegrad Patent Institute | WIPO ST.3 |
| `XBA`, `XCC`, `XCE`, `XEC`, `XOM`, `XPO`, `XXA`–`XXC`, `XXX` … | ICAO Doc 9303 Part 3 codes for organisations and for stateless persons / refugees | ICAO Doc 9303-3 Parts D–E |

**Validation caveat:** the UBL XSD accepts any token in `cbc:IdentificationCode`, but
the **Peppol / EN 16931 country code list contains none of the user-assigned codes
except `XI`**, so an `AA` country fails Peppol BIS / CEN Schematron. Use a real ISO
3166 country where the document must pass those rules.

### 1.2 ISO 4217 currency codes

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Test currency | `XTS` (numeric `963`) | Reserved | Official name "Codes specifically reserved for testing purposes"; minor units N.A. ✅ in the Peppol ISO 4217 code list |
| No currency | `XXX` (numeric `999`) | Reserved (different purpose) | "Transactions where no currency is involved" — not a test code. Also in the Peppol list |

`XTS` passes the UBL XSD and the Peppol currency code list. Because it has no minor
units defined, amounts with 2 decimals are not "wrong" for any rule found, but a
real-looking currency (EUR, USD) is still needed when the example must be realistic.

### 1.3 UN/LOCODE

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Fictitious location | none | — | UNECE Rec. 16 and the UN/LOCODE Manual define no fictitious or test location |
| `XZ` + 3 characters | Offshore installations | **Avoid** | Real entries for international waters |
| `AA` + 3 characters (e.g. `AAXMP`) | — | Derived | Correct format (2 + 3), not in UN/LOCODE because `AA` is no country; fails a code-list lookup |

### 1.4 Geographic coordinates

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| `0, 0` ("Null Island") | — | **Avoid** | Not reserved. Natural Earth (v1.3, 2011) added a 1 m² "island" with scalerank 100 so that geocoding errors can be found. Systems treat 0,0 as an error marker |

---

## 2. Travel and identity documents

### 2.1 ICAO Doc 9303 specimen (8th edition, 2021)

Doc 9303 Part 3, Section 5 Part G "Codes Used in Specimen Documents": *"In order to
establish a standardized way to identify specimen documents, it is recommended to set
the nationality of the document holder to 'Utopia' for sample documents."* Code
**`UT` / `UTO`**.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Issuing state / nationality | `UTO` ("UTOPIA", "UTOPIAN/UTOPIENNE") | Reserved (ICAO) | ICAO only; `UT`/`UTO` are **not** ISO 3166 user-assigned codes, so ISO could in theory assign them |
| Passport (TD3) holder | `ERIKSSON, ANNA MARIA`, F, born 12 AUG 74 in `ZENITH` | Published example | Part 3 Figure 1 and Part 4 |
| Passport number | `L898902C3` | Published example | ✅ check digit `6` |
| Personal number | `ZE184226B` | Published example | ✅ check digit `1` |
| Dates | issue 16 APR 07, expiry 15 APR 12 (`120415`) | Published example | ✅ check digits; **expired**, so a "valid document" check fails |
| TD3 MRZ | `P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<` / `L898902C36UTO7408122F1204159ZE184226B<<<<<10` | Published example | ✅ all 5 check digits incl. composite `0` |
| ID card (TD1) number | `D23145890` | Published example | Part 5; ✅ check digit `7` |
| TD1 MRZ | `I<UTOD231458907<<<<<<<<<<<<<<<` / `7408122F1204159UTO<<<<<<<<<<<6` / `ERIKSSON<<ANNA<MARIA<<<<<<<<<<` | Published example | ✅ composite `6` |
| TD2 MRZ | `I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<` / `D231458907UTO7408122F1204159<<<<<<<6` | Published example | Part 6; ✅ composite `6` |

Note: icao.int returned HTTP 403 to automated download. The text above was checked
against a copy of Parts 3–6 (8th ed.) hosted at smartid.com.vn; the canonical URLs are
in §11.

### 2.2 Other specimen documents

| Source | Notes |
|---|---|
| EU PRADO (Council of the EU, *Public Register of Authentic travel and identity Documents Online*) | Shows images of genuine national specimens with fictitious holders (e.g. the German "Mustermann" convention). Number formats are national — see country files. Not checked in detail here (unverified) |

---

## 3. Payment cards

ISO/IEC 7812 defines the PAN structure and Luhn check but **reserves no test IIN** (the
ISO IIN register is not public; nothing found). EMVCo publishes no general test PANs.
PCI DSS requires test card numbers in test environments, and the schemes publish them
through their own acquiring/gateway businesses. These PANs are known to every gateway
and fraud filter as test cards; they never authorise in production.

| Brand | Value | Status | Checks/Notes |
|---|---|---|---|
| Visa | `4111 1111 1111 1111` | Published example | Visa Acceptance (Visa's Cybersource platform) testing guide; also Braintree, PayPal, Spreedly, Adyen. ✅ Luhn |
| Visa | `4622 9431 2701 3705` (CVV 838) … `…3747` | Published example | Visa Acceptance; ✅ Luhn (3705) |
| Visa (alt.) | `4012 8888 8888 1881` | Published example (PSPs only) | PayPal Payflow, Spreedly; ✅ Luhn |
| Mastercard | `5555 5555 5555 4444` | Published example | Visa Acceptance; Braintree, Adyen, Stripe. ✅ Luhn |
| Mastercard 2-series | `2222 4200 0000 1113`, `2222 6300 0000 1125` | Published example | Visa Acceptance; ✅ Luhn |
| Mastercard | `5123 4500 0000 0008`, `2223 0000 0000 0007`, `5111 1111 1111 1118` | Published example | Mastercard Gateway (MPGS) "standard test cards" on developer.mastercard.com (seen in search index; page itself not fetchable). ✅ Luhn |
| Mastercard 2-series | `2223 0000 4840 0011` | Published example (PSPs only) | Braintree, TabaPay; ✅ Luhn |
| American Express | `3782 822463 10005` | Published example | Visa Acceptance; Braintree, Stripe. No americanexpress.com page found. ✅ Luhn |
| American Express | `3714 496353 98431` | Published example (PSPs only) | Braintree, Stripe; **Spreedly uses it as the declined card**. ✅ Luhn |
| Discover | `6011 1111 1111 1117` | Published example | Visa Acceptance; ✅ Luhn |
| JCB | `3566 1111 1111 1113` | Published example | Visa Acceptance; ✅ Luhn |
| UATP | `1354 1234 5678 911` | Published example | Visa Acceptance; ✅ Luhn |
| Negative case | `4111 1111 1111 1112` | Published example | Cybersource: triggers "Invalid Luhn Mod 10"; ✅ fails Luhn |

UBL usage: `cac:CardAccount/cbc:PrimaryAccountNumberID` should be **masked** in
realistic invoices (Peppol BIS: only the last 4–6 digits), e.g. `************1111`,
with `cbc:NetworkID` `VISA`/`MC`.

---

## 4. Banking (ISO 9362 BIC, ISO 13616 IBAN, ISO 20022)

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Test-and-training BIC | 8th character (2nd char of location code) = `0`, e.g. `DEUTDES0` for `DEUTDESS` | Reserved (convention of the RA) | SWIFT white paper on ISO 9362:2014 §4.5 "Test & Training BIC" (title seen in search; swift.com blocked download). `1` in that position = passive (non-connected) participant |
| Fully fictitious BIC | `AAAA` + real country + `X0`, e.g. `AAAAFRX0` | Derived | Format-valid; institution code `AAAA` not checked against the BIC directory (unverified) |
| IBAN | SWIFT IBAN Registry examples, e.g. `DE89 3704 0044 0532 0130 00`, `GB29 NWBK 6016 1331 9268 19` | Published example | ✅ mod-97. **Bank codes are real** (`37040044` Commerzbank, `NWBK` NatWest); the account part makes them fictitious |
| IBAN for a fictitious country | — | — | Not possible: IBAN validators check the country against the registry |
| ISO 20022 example data | `AAAAGB2L`, `BBBBUS33`, "DEF Electronics" | Unverified | Seen only on a low-quality scrape attributed to the ISO 20022 MDR samples; not confirmed at iso20022.org |

---

## 5. GS1 identification keys

### 5.1 Prefix 952

GS1 General Specifications Release 24.0 (Jan 2024), Figure 1.4.2-1 and 1.4.3-1:
**`952` — "Used for demonstrations and examples of the GS1 system"** (both GS1 Prefix
and GS1-8 Prefix). GS1 Style Guide §2.18 (new in v5.1, May 2021): 952 is *"an official
GS1 prefix specifically allocated to demonstrations, examples, tests or any other
usage"* and *"will not be subject to any central or decentralised governance"*.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| GTIN-13 / GLN | `9520123456788` | Published example | GS1 Digital Link URI Syntax 1.7.0 (both GTIN and GLN); ✅ mod-10 |
| GTIN-14 | `09520123456788` | Published example | Same; ✅ |
| GTIN | `09524000059109` | Published example | GS1 General Specifications 24.0; ✅ |
| SSCC | `195201234567891232` | Published example | GS1 Digital Link; ✅ |
| GIAI | `9520614141234567` | Published example | GS1 Digital Link (no check digit in GIAI) |
| GTIN-12 (UPC) | `012345000058` | Published example | GS1 US via Style Guide §2.18.1; ✅ |
| GLN set for parties 1–27 | `9520000000011`, `9520000000028`, `9520000000035` … `9520000000264`, `9520000000271` | Derived | GCP `9520000` + 5-digit location ref (= party #) + check; ✅ mod-10 |
| GTIN-13 / GTIN-14 | `9520000100018` / `09520000100018` | Derived | ✅ |
| SSCC | `095200000000000011` | Derived | extension 0 + `9520000` + serial; ✅ |
| GRAI (AI 8003) base | `09520000200015` + optional serial | Derived | ✅ |
| GTIN-8 | `95200002` | Derived | GS1-8 prefix 952; ✅ |
| Peppol scheme | `schemeID="0088"` (GLN) for EndpointID / PartyIdentification; `0160` (GTIN) for item IDs | — | Peppol EAS / ICD lists |

### 5.2 Other GS1 example conventions

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Example web domains | `example.com`, `brand.example.com`, `retailer.example.com`, `example.org` | Reserved | GS1 Digital Link 1.7.0 cites RFC 2606 |
| Canonical resolver | `https://id.gs1.org/01/09520123456788` | Published example | `id.gs1.org` is GS1's **real** resolver, not a documentation domain |
| Demo brand | "Dal Giardino" (GTINs `09506000134352`, `9506000134369`, prefix 950) | **Avoid** for fiction | Fictitious brand, but GTINs are genuinely registered under GS1 Global Office prefix 950 and resolve live (Style Guide §2.18.4) |
| Example company names | Style Guide §2.17 "Name used for example companies" | Unverified | Names are in an image; page not fetchable. "GS1 Garden Company" appears in the GLN Allocation Rules (search snippet) |
| Classic GCP `0614141` | used in older GS1 examples (e.g. `9520614141…` above) | Unverified | Ownership not checked; prefer pure 952 values |

---

## 6. Legal entity, publication and object identifiers

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| LEI (ISO 17442) — reserved test value | none | — | No test LEI or reserved LOU prefix found at GLEIF or in the ISO 17442 preview |
| LEI `5493001KJTIIGC8Y1R12` | used in GLEIF API docs | **Avoid** | ✅ mod-97, but ✅ GLEIF lookup: **Bloomberg Finance L.P.** (US, ISSUED) |
| LEI `00000000EXAMPLE00A87`, `00000000EXAMPLE00B84`, `00000000EXAMPLE00C81` | — | Derived | ✅ mod 97-10; ✅ GLEIF API 404 (not issued) on 2026-11-05. Prefix `0000` is no known LOU prefix (not proven) |
| ISBN — reserved range | none | — | No reserved registrant range found (International ISBN Agency manual not reached) |
| ISBN `978-0-306-40615-7` / `0-306-40615-2` | Wikipedia's example | **Avoid** | ✅ checksums; ✅ Open Library: real book (*Error-correction coding for digital communications*, Clark, Plenum) |
| ISBN `978-3-16-148410-0` | Wikipedia's barcode example | **Avoid** | ✅ checksum; registrant `3-16` believed real (unverified) |
| ISSN `0317-8471`, `1050-124X` | ISSN International Centre portal examples | Published example (probably real serials) | ✅ mod-11; portal lookup blocked (unverified) |
| ISMN | — | — | Not investigated in detail; 979-0 under ISBN/ISMN agencies |
| DOI test prefix `10.5072` | historical DataCite test prefix | **Avoid** | Retired by DataCite 2019-06-01; DataCite: no DOI-wide example prefix exists |
| DOI `10.1000/182` | DOI Handbook | **Avoid** | Real DOI (IDF's own) |

---

## 7. Internet and telecom

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Domains | `example`, `example.com`, `example.net`, `example.org`, `test`, `invalid`, `localhost` (+ subdomains) | Reserved | RFC 2606 / RFC 6761; IANA Special-Use Domain Names registry ✅ |
| Email | `<role>@<party-alias>.example` or `@example.com` | Reserved | Same |
| IPv4 | `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` (TEST-NET-1/2/3) | Reserved | RFC 5737; IANA IPv4 special registry ✅ |
| IPv6 | `2001:db8::/32`; `3fff::/20` | Reserved | RFC 3849; RFC 9637 (updates 3849, adds the /20) |
| AS numbers | `64496`–`64511`, `65536`–`65551` | Reserved | RFC 5398 §4 |
| MAC (EUI-48) | `00-00-5E-00-53-00` … `00-00-5E-00-53-FF` (unicast), `01-00-5E-90-10-00` … `-FF` (multicast) | Reserved | RFC 7042 §2.1.2 |
| EUI-64 | `00-00-5E-EF-10-00-00-00` … `-FF` (unicast) | Reserved | RFC 7042 §2.2.3 |
| E.164 fictitious country code | none | — | ITU-T reserves no country code for fiction or documentation |
| E.164 `+991` | Shared trial code | **Avoid** | ITU-T E.164.2 (03/2024): assigned to real non-commercial trials |
| E.164 `+999` | "Reserved for future global service" | **Avoid** | ITU list of assigned country codes |
| Fictitious phone numbers | national drama ranges (e.g. NANP `555-0100`–`0199`, Ofcom, ARCEP) | Reserved (national) | See country files; not verified here |

---

## 8. Transport and trade

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| ISO 6346 owner code — reserved test code | none | — | Nothing in BIC material or ISO 6346 previews |
| `BICU 123456 5` | BIC's own "theoretical" container number on bic-code.org | Published example | ✅ check digit 5. `BICU` may be BIC's own registered code (register search is JS-only; unverified) |
| `CSQU 305438 3` | Wikipedia / ISO 6346 worked example | **Avoid** | ✅ check digit 3; `CSQU` is a registered owner code (real fleet) |
| `ABZU 001234 3` | ISO 6346:1984 worked example ("registered owner code") | **Avoid** (probably real) | ✅ check digit 3 |
| Derived owner codes | `ZZZU 123456 4`, `XXXU 123456 1`, `QQQU 123456 0` | Derived (unverified) | ✅ check digits; **not checked** against the BIC register |
| IMO ship number — reserved | none | — | IMO Res. A.1117(30) defines the scheme, no example or test range |
| IMO `9074729` | Wikipedia's check-digit example | **Avoid** | ✅ check digit; a real ship number |
| IMO `0000000` | — | Derived | ✅ check digit (0); obviously fictitious, but systems may reject a leading 0 |
| VIN — reserved WMI | none | — | No reserved or test WMI found |
| VIN `1M8GDM9AXKP042788` | Wikipedia / 49 CFR 565 check-digit example | **Avoid** | ✅ check digit `X`; WMI `1M8` = Motor Coach Industries (decodes to a 1989 bus) |
| VIN `11111111111111111` | — | Derived | ✅ check digit; WMI `111` ownership not checked |
| IATA airline / airport codes | none reserved for tests found | — | `ZZZ` = US DOT/BTS code for non-designated Alaska airports; ICAO `ZZZZ` = "no ICAO location indicator"; ICAO `YYY` = operator without designator (secondary sources) |
| Air waybill | 3-digit airline prefix + 7-digit serial + mod-7 check | — | No reserved airline prefix found |
| EORI (EU) | none | — | No EU (EOS) test EORI found |
| EORI (GB, HMRC sandbox only) | `GB` + 12 digits; last digit `0`–`7` valid, `8`/`9` invalid; e.g. `GB123456789133` | Published example (sandbox) | HMRC *Check an EORI Number* API, `test-api.service.hmrc.gov.uk` only |
| UN numbers, HS codes | real values (e.g. `UN1263` paint) | — | Classification codes, not entity identifiers: no fiction needed |

---

## 9. Peppol and ISO/IEC 6523

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Test participant | `iso6523-actorid-upis::9915:test` | Published example (live on test network) | Peppol Directory spec example; registered in the Peppol **test** SML (SMK), endpoint `test.erechnung.gv.at` (Austrian government test AP). `9915` = Austrian VKZ scheme. Not in production |
| ISO 6523 ICD for tests | none | — | ICD list (iso6523.info, 2026-07-26): no test ICD; `0001`, `0103`, `0181` "Not Assigned". ISO/IEC 6523-1:2023 Clause 5 lists "ICD values reserved for special use" (not seen) |
| Peppol EAS test code | none | — | Peppol EAS list has no test or reserved code |
| Recommended | `cbc:EndpointID schemeID="0088"` with a 952 GLN (§5.1) | Derived | Format-valid; never registered in any SML |

---

## 10. Avoid list

| Value | Seen as | Why |
|---|---|---|
| `XI`, `XK`, `XZ`, `ZZ`, `XX`, `QZ`, `XN`, `XU`, `XV`, ICAO `X..` codes | "Fictitious" country codes | Real meanings in EU VAT, Peppol, UN/LOCODE, CLDR, WIPO, ICAO |
| `UT` as an ISO country | ICAO specimen | Valid only inside ICAO 9303; not ISO-reserved |
| `0,0` coordinates | Placeholder location | Error marker ("Null Island") |
| `5493001KJTIIGC8Y1R12` | Example LEI | Bloomberg Finance L.P. |
| `978-0-306-40615-7`, `978-3-16-148410-0` | Example ISBNs | Real book / real registrant |
| `10.5072/…` | Test DOI | Retired 2019 |
| `CSQU3054383`, `ABZU0012343` | Example container numbers | Registered owner codes |
| `IMO 9074729` | Example IMO number | Real ship |
| `1M8GDM9AXKP042788` | Example VIN | Real manufacturer WMI |
| `+991…`, `+999…` | Fictitious phone numbers | ITU trial / reserved global service |
| Dal Giardino GTINs (`0950600013435x`) | GS1 demo barcodes | Genuine registered GTINs (prefix 950) |
| IBAN registry examples | "Fictitious IBANs" | Real bank codes (account part only is fictitious) |
| `3714 4963 5398 431` | "Good" Amex test card | Some PSPs treat it as a decline card |

---

## 11. Sources

- ISO 3166: [ISO Glossary for ISO 3166](https://www.iso.org/glossary-for-iso-3166.html) (403 to automated fetch; quoted via search) · [Wikipedia ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) · [XK (user assigned code)](https://en.wikipedia.org/wiki/XK_(user_assigned_code)) · [Unicode UTS #35](https://www.unicode.org/reports/tr35/) · [WIPO ST.3](https://www.wipo.int/documents/d/standards/docs-en-03-03-01.pdf)
- Peppol code lists: [ISO 3166](https://docs.peppol.eu/poacc/billing/3.0/codelist/ISO3166/) · [ISO 4217](https://docs.peppol.eu/poacc/billing/3.0/codelist/ISO4217/) · [EAS](https://docs.peppol.eu/poacc/billing/3.0/codelist/eas/) · [ICD](https://docs.peppol.eu/poacc/billing/3.0/codelist/ICD/)
- ISO 4217: [Wikipedia ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) · [SIX ISO 4217 maintenance agency](https://www.six-group.com/en/products-services/financial-information/data-standards.html)
- UN/LOCODE: [UNECE Recommendation 16](https://unlocode.unece.org/recommendation16/) · [UN/LOCODE Manual](https://unece.org/sites/default/files/2023-10/unlocode_manual.pdf)
- Null Island: [Library of Congress blog](https://blogs.loc.gov/maps/2016/04/the-geographical-oddity-of-null-island/) · [Wikipedia](https://en.wikipedia.org/wiki/Null_Island)
- ICAO: [Doc 9303 Part 3](https://www.icao.int/sites/default/files/publications/DocSeries/9303_p3_cons_en.pdf) · [Part 4](https://www.icao.int/sites/default/files/publications/DocSeries/9303_p4_cons_en.pdf) · [Part 5](https://www.icao.int/sites/default/files/publications/DocSeries/9303_p5_cons_en.pdf) · [Part 6](https://www.icao.int/sites/default/files/publications/DocSeries/9303_p6_cons_en.pdf) (checked via [mirror copy](https://smartid.com.vn/media/lib/30-03-2022/9303_p3_cons_en.pdf))
- PRADO: [Council of the EU — PRADO](https://www.consilium.europa.eu/prado/en/) (URL not reachable by automated fetch; unverified)
- Payment cards: [Visa Acceptance testing guide](https://developer.visaacceptance.com/hello-world/testing-guide.html) · [Visa Acceptance KB 000001655](https://support.visaacceptance.com/knowledgebase/knowledgearticle/?code=000001655) · [Mastercard Gateway test cards](https://developer.mastercard.com/mastercard-gateway/documentation/testing/test-cards/) · [Braintree testing](https://developer.paypal.com/braintree/docs/guides/credit-cards/testing-go-live/php/) · [Spreedly test data](https://developer.spreedly.com/docs/test-data) · [Adyen test cards](https://docs.adyen.com/development-resources/test-cards-and-credentials/test-card-numbers) · [Wikipedia ISO/IEC 7812](https://en.wikipedia.org/wiki/ISO/IEC_7812)
- SWIFT: [White paper ISO 9362:2014](https://www.swift.com/swift-resource/14256/download?language=en) · [IBAN Registry](https://www.swift.com/resource/iban-registry-pdf) · [Wikipedia ISO 9362](https://en.wikipedia.org/wiki/ISO_9362) · [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions)
- GS1: [General Specifications R24.0 (GS1 Switzerland copy)](https://www.gs1.ch/sites/default/files/2024-02/GS1%20General%20Specifications%2001_24.pdf) · [GS1 Style Guide](https://www.gs1.org/standards/gs1-style-guide/53) · [GS1 Digital Link URI Syntax](https://ref.gs1.org/standards/digital-link/uri-syntax/) · [GS1 Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix) · [GSCN 23-243](https://www.gs1.org/docs/barcodes/GSCN-23-243-clarifications.pdf) · [GLN Allocation Rules](https://www.gs1.org/standards/gs1-gln-allocation-rules-standard/30)
- LEI: [GLEIF API](https://api.gleif.org/api/v1/lei-records/5493001KJTIIGC8Y1R12) · [ISO 17442:2019 preview](https://cdn.standards.iteh.ai/samples/75998/2b77042cb3a346fda3b26dfd6bfd42ca/ISO-17442-2019.pdf) · [GLEIF supporting documents](https://www.gleif.org/en/lei-data/access-and-use-lei-data/supporting-documents)
- ISBN/ISSN/DOI: [Wikipedia ISBN](https://en.wikipedia.org/wiki/ISBN) · [Open Library API](https://openlibrary.org/api/books?bibkeys=ISBN:9780306406157&format=json&jscmd=data) · [ISSN portal](https://portal.issn.org/) · [DataCite: test prefix 10.5072 retiring](https://datacite.org/blog/test-prefix-10-5072-retiring-june-1/) · [PID Forum: example DOI prefix](https://pidforum.org/t/example-doi-prefix-best-practice-for-documentation-on-dois/1763)
- IETF/IANA: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761) · [Special-Use Domain Names](https://www.iana.org/assignments/special-use-domain-names/special-use-domain-names.xhtml) · [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737) · [IPv4 special registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) · [RFC 3849](https://www.rfc-editor.org/rfc/rfc3849) · [RFC 9637](https://www.rfc-editor.org/rfc/rfc9637.html) · [RFC 5398](https://www.rfc-editor.org/rfc/rfc5398.html) · [RFC 7042](https://www.rfc-editor.org/rfc/rfc7042.html)
- ITU: [ITU-T E.164.2 (03/2024)](https://www.itu.int/epublications/en/publication/itu-t-e-164-2-2024-03-itu-t-e-164-numbering-resources-for-trials/en) · [List of E.164 assigned country codes (2016)](https://www.itu.int/dms_pub/itu-t/opb/sp/t-sp-e.164d-2016-pdf-e.pdf)
- Containers: [BIC — BIC codes](https://www.bic-code.org/bic-codes/) · [Wikipedia ISO 6346](https://en.wikipedia.org/wiki/ISO_6346) · [ISO 6346:1984 preview](https://cdn.standards.iteh.ai/samples/12648/681ff881db114cce8e8054309a1dc438/ISO-6346-1984.pdf)
- Ships/vehicles/air: [IMO Res. A.1117(30)](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/AssemblyDocuments/A.1117(30).pdf) · [Wikipedia IMO number](https://en.wikipedia.org/wiki/IMO_number) · [Wikibooks VIN check digit](https://en.wikibooks.org/wiki/Vehicle_Identification_Numbers_(VIN_codes)/Check_digit) · [BTS: codes for non-designated Alaska airports](https://www.bts.gov/topics/airlines-and-airports/number-186-codes-nondesignated-alaska-airports) · [Wikipedia Airline codes](https://en.wikipedia.org/wiki/Airline_codes)
- Customs: [HMRC Check an EORI Number API](https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/check-eori-number-api/1.0/oas/resolved) · [HMRC test data](https://github.com/hmrc/check-eori-number-api/tree/master/public/api/conf/1.0/test-data)
- Peppol / ISO 6523: [Peppol Directory spec 1.1.1](https://docs.peppol.eu/edelivery/directory/PEPPOL-EDN-Directory-1.1.1-2020-10-15.pdf) · [Peppol Practical (helger)](https://peppol.helger.com/public/locale-en_US/menuitem-docs-doc-exchange) · [ICD list (iso6523.info)](http://iso6523.info/icd_list.pdf) · [ISO/IEC 6523-1:2023 preview](https://cdn.standards.iteh.ai/samples/82246/71444a0e45184dd089ebd0b5471da064/ISO-IEC-6523-1-2023.pdf)
