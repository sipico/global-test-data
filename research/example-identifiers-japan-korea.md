# Fictitious-but-valid example identifiers — Japan and South Korea

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with Japanese, Korean and English queries. Checks marked ✅
were run during research:

- Japan: Corporate Number check digit (NTA algorithm) and My Number check digit (MIC ordinance).
- Japan: lookups on the NTA Corporate Number publication site (`houjin-bangou.nta.go.jp`) and the NTA Qualified Invoice Issuer publication site (`invoice-kohyo.nta.go.jp`). Positive control: Toyota `1180301018771` was found on both.
- Japan: postcodes checked against Japan Post's KEN_ALL (UTF-8 edition, 124,527 rows, 120,721 area postcodes) and JIGYOSYO (22,196 business postcodes).
- Japan: telephone blocks checked against MIC allocation spreadsheets.
- Korea: business registration number (BRN) check digit.
- Both: telephone validity in libphonenumber (Python `phonenumbers` 9.0.42), and DNS lookups for domains.

Korean government sites (hometax, nts, epost, juso, law.go.kr) reset direct
connections from the research environment. They could be read page by page through a
fetch tool, but **no existence lookup of Korean numbers was possible.**

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**

- **Japan** has an official UBL source: the JP PINT example invoices published by the Digital Agency through OpenPeppol. But their corporate numbers and registration numbers **fail the NTA check digit**, apparently on purpose. The NTA's own `T1234567890123` fails it too.
- Japan's checksum-valid substitutes were derived from these official values and **confirmed absent from both NTA registers**.
- **JPRS reserves `example.jp`/`example.co.jp`**, a stronger reservation than France or Italy have.
- **Korea has no official reserved values** of any kind found. Its e-tax invoice format is not UBL, and its common "example" BRN `123-45-67890` fails the check digit.

---

## 1. Japan (日本)

### 1.1 Primary source: JP PINT example invoices (Digital Agency / デジタル庁, via OpenPeppol)

The Digital Agency is the Japanese Peppol Authority. The three Japanese Peppol
specifications are published on docs.peppol.eu, version 1.1.3 (2026-05-18); each has a
`resources.zip` with UBL 2.1 examples:

| Spec | CustomizationID | Example files |
|---|---|---|
| [JP PINT](https://docs.peppol.eu/poac/jp/pint-jp/) (適格請求書, Standard Invoice) | `urn:peppol:pint:billing-1@jp-1` | 9 (full, minimum, tax-currency, summary ×3, allowance/charge, corrective, return) |
| [JP BIS Self-Billing](https://docs.peppol.eu/poac/jp/pint-jp-sb/) (仕入明細書) | `urn:peppol:pint:selfbilling-1@jp-1` | 1 |
| [JP BIS Non-tax Registered Businesses](https://docs.peppol.eu/poac/jp/pint-jp-ntr/) (免税事業者向け請求書) | `urn:peppol:pint:nontaxinvoice-1@jp-1` | 7 |

All 17 files use the same two parties:

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| Supplier name | `株式会社 〇〇商事` (Kabushiki Kaisha Marumaru Shōji; `〇〇` is the Japanese "blank" placeholder) | Published example | — |
| Customer name | `株式会社 〇〇物産` (… Marumaru Bussan); delivery party `株式会社 〇〇物産 札幌支社` (Sapporo branch) | Published example | — |
| Foreign supplier (Example2) | `XYZ Digital Learning Services, Inc.` (GB), customer `〇〇 Bussan Co., Ltd.` | Published example | — |
| Corporate Number, `EndpointID`/`CompanyID schemeID="0188"` | `1234567890123` (supplier), `3210987654321` (customer) | Published example | ❌ check digit wrong (would be `9…`, `2…`) · ✅ absent from NTA register |
| Registration number (`PartyTaxScheme/CompanyID`, `TaxScheme/ID=VAT`) | `T1234567890123`, `T3210987654321`, tax representative `T7654321098765` | Published example | ❌ check digit wrong · ✅ absent from NTA invoice register |
| Standard Company Code (ICD `0147`, JIPDEC 標準企業コード) | `123456:000123:0147:1`, `654321:000321:0147:1`, payee `123456:000124:0147:1` | Published example | Not checked (no open register) |
| GLN endpoint (Example2) | `9482348239847239874` (schemeID `0088`) | Placeholder | ❌ 19 digits, not a GLN |
| Supplier address | `四谷4-29-X` / `〇〇商事ビル` / `新宿区` / `東京都` / `1600044` | Published example | ❌ **`160-0044` does not exist** (Yotsuya is `160-0004`) ✅ KEN_ALL |
| Customer address | `北区` / `北十二条西76-X` / `札幌市` / `北海道` / `0010012` | Published example | ✅ `001-0012` = 札幌市北区北十二条西 (1〜4丁目); "76" is outside the real 1–4 chōme |
| Contact | `青木 志郎` (Aoki Shirō), `03-3xxx-0001`, `011-757-1xxx` | Published example | ❌ phone numbers masked with `x`, fail any parser |
| Email | `shirou_aoki@〇〇co.jp`, `purchaser@oobussan.co.jp` | Published example | ❌ first is malformed · `oobussan.co.jp` unregistered (DNS NXDOMAIN) but not reserved, so anyone could register it |
| Bank account (`PayeeFinancialAccount/ID`) | `1234:567:1:3242394` (bank:branch:type:account), holder `ｶ)ﾏﾙﾏﾙｼﾖｳｼﾞ` | Published example | Bank code `1234` not in the community Zengin dataset (see §1.8) |

Defects in the JP PINT set (do not copy):

- Five files (Example, Example3–7) and the Self-Billing example have `CompanyID` `>T3210987654321`, with a stray `>`.
- `CompanyLegalForm` is `Private Limited Company`, an English label rather than the Japanese legal form.

### 1.2 Corporate Number (法人番号, *hōjin bangō*)

- 13 digits: a check digit, then a 12-digit base. For registered companies, the base is the 会社法人等番号 (company/legal-entity number) from the Ministry of Justice.
- Check digit (NTA, ✅ implemented): `9 − (Σ Pₙ × Qₙ mod 9)`.
  - Pₙ is the n-th digit of the base, counted from the right.
  - Qₙ = 1 for odd n and 2 for even n.
- The NTA's worked example is `8700110005901`. ✅ It passes the check and ✅ is absent from the register.
- Government bodies use bases starting `0000` (e.g. NTA itself is `7000012050002`). Keep derived values out of that range.

| Element | Value | Status | Checks |
|---|---|---|---|
| NTA algorithm example | `8700110005901` | Published example | ✅ check digit · ✅ not in register · ✅ not in invoice register |
| JP PINT values with corrected check digit | `9234567890123` (supplier), `2210987654321` (customer), `8654321098765` (tax rep.) | Derived | ✅ check digit · ✅ not in register · ✅ not in invoice register |
| Party-set series `CD + 999900 + nnnnnn` (n = 1…27) | `8999900000001`, `7999900000002`, `6999900000003`, `5999900000004`, `4999900000005`, `3999900000006`, `2999900000007`, `1999900000008`, `9999900000009`, `7999900000010`, `6999900000011`, `5999900000012`, `4999900000013`, `3999900000014`, `2999900000015`, `1999900000016`, `9999900000017`, `8999900000018`, `7999900000019`, `5999900000020`, `4999900000021`, `3999900000022`, `2999900000023`, `1999900000024`, `9999900000025`, `8999900000026`, `7999900000027` | Derived | ✅ all 27 check digits · ✅ all 27 absent from both NTA registers (2026-11-05) |

The NTA publication site lists every corporate number ever assigned, closed entities
included. "対象の法人番号は存在しません" ("this corporate number does not exist") is
therefore a strong negative.

The open **Web-API** (`houjin-bangou.nta.go.jp/webapi/`) needs a registered
application ID. The per-number HTML detail page (`henkorireki-johoto.html?selHouzinNo=`)
was used instead. Full-dataset CSV downloads (基本3情報ダウンロード) also exist.

### 1.3 Qualified Invoice registration number (適格請求書発行事業者登録番号)

| Element | Value | Status | Notes |
|---|---|---|---|
| Format | `T` + 13 digits | — | NTA Q&A 問18 ([qa/18.pdf](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/qa/18.pdf)) |
| Corporations | `T` + Corporate Number | — | So `T9234567890123` etc. from §1.2 are consistent |
| Sole traders / unincorporated bodies | `T` + 13 digits, not the My Number and not overlapping corporate numbers | — | Check digit for these: **unverified**; the same mod-9 rule is widely assumed, but no NTA primary source was found |
| NTA's own example | `T1234567890123`, also written `T-1234567890123`; half- or full-width allowed | Published example | ❌ check digit · ✅ not in invoice register. Used throughout NTA Q&A and leaflets (`△△商事㈱`, `B株式会社`, `スーパー○○`) |
| UBL / Peppol scheme | EAS/ICD `0221` = registered number of the qualified invoice issuer; `0188` = Corporate Number | — | JP PINT code lists |

Party names in NTA material are placeholders, not names: `A株式会社`, `B株式会社`,
`△△商事㈱`, `▲▲㈱`, `■■建設`, `スーパー○○`, `○○旅館`. These are good for
Japanese-language samples.

### 1.4 My Number (個人番号) — do not use in UBL samples

| Element | Value | Status | Notes |
|---|---|---|---|
| Check digit | Last digit; `11 − (Σ Pₙ × Qₙ mod 11)`, or 0 if the remainder ≤ 1. Pₙ is the n-th digit from the right of the first 11; Qₙ = n+1 for n ≤ 6 and n−5 for n ≥ 7 | — | MIC ordinance No. 85 of 2014, art. 5 ([e-Gov](https://laws.e-gov.go.jp/law/426M60000008085)); ✅ implemented |
| Official card specimen | `1234 5678 9012`, name `番号 花子` (Bangō Hanako), born 平成元年3月31日 (31 March 1989) | Published example | ❌ check digit (valid would be `123456789018`). Seen in MIC [001039529.pdf](https://www.soumu.go.jp/main_content/001039529.pdf); also Digital Agency and MOJ leaflets |

The My Number Act strictly limits collecting and storing these numbers, and no UBL
business document needs one. **Leave it out.** If a demo needs a person ID, the
specimen name `番号 花子` is the official placeholder.

### 1.5 Postal addresses and postcodes (Japan Post / 日本郵便)

Format: 7 digits written `NNN-NNNN`. UBL `PostalZone` takes `1600004` or
`160-0004` (JP PINT uses no hyphen). Address order: 都道府県 (prefecture) → 市区町村
(city/ward/town) → 町域 (district) → 丁目-番-号 (chōme-block-house) → building.

| Finding | Detail | Status |
|---|---|---|
| Unused 3-digit prefixes | `000`, `008`, `009`, `032`, `908`, `909`, `977`, `978`: in neither KEN_ALL nor JIGYOSYO | Derived (fails a postcode-existence check) |
| `000-0000`, `999-9999` | Not assigned | Derived |
| Lowest / highest code in use | `001-0000` / `999-8531` | ✅ |
| JP PINT `160-0044` | Not assigned | ✅ (an accidental "fictitious" postcode) |
| Business postcodes (個別番号) | e.g. `100-8792` = Japan Post Co., Ltd. HQ | **Avoid** for fictional parties |

Official example addresses:

| Source | Example | Notes |
|---|---|---|
| UPU *Postal addressing systems — Japan* (06/2019) | `Mr Taro Tanaka` (田中 太郎) / `10–23, Kotobukicho` / `Chuo-ku, NIIGATA` / `951-8073 JAPAN`; `2–17–10, Aioicho, Naka-ku, YOKOHAMA 231-0012`; `2338 Magatake, Zaou-machi, Katta-gun, MIYAGI 989-0851`; `4-3-2, Hakusan, Bunkyo-ku, TOKYO 112-0001` | ✅ all postcode/town pairs real. Defect: the UPU also prints `Musashi-Murayama-shi, TOKYO 231-0012` (that postcode is Yokohama) |
| JP PINT (§1.1) | Real ward + out-of-range chōme (`北十二条西76-X`) + building `〇〇商事ビル` | Pattern: real municipality, impossible block number |

Address strategy:

| Option | Passes format | Passes postcode/town lookup | Risk of real match |
|---|---|---|---|
| A. Real postcode + real 町域 + chōme beyond the real range (JP PINT pattern, e.g. `札幌市北区北十二条西76丁目`) | ✅ | ✅ postcode/town; ❌ chōme in a full geocoder | None |
| B. Real postcode + real 町域 + plausible 番地 + `〇〇ビル` | ✅ | ✅ | Low-medium (most 番地 exist) |
| C. Unused prefix (`000`/`008`/`009`/`032`/`908`/`909`/`977`/`978`) + any town | ✅ | ❌ | None |

### 1.6 Telephone numbers (MIC / 総務省)

**Japan reserves no numbers for fiction or examples.** Nothing was found in MIC's
numbering plan (電気通信番号計画, 令和元年総務省告示第6号, MIC Notice No. 6 of 2019)
or anywhere else. Secondary sources agree: Japanese productions mask digits, as JP
PINT does with `03-3xxx-0001`. MIC publishes allocation status
([電気通信番号指定状況](https://www.soumu.go.jp/main_sosiki/joho_tsusin/top/tel_number/number_shitei.html),
page status 2026-10-01), so unallocated blocks can be derived:

| Range | Allocation status per MIC file | libphonenumber 9.0.42 | Status |
|---|---|---|---|
| `03-3102-xxxx` … `03-3199-xxxx` (Tokyo) | 未使用 (unassigned) in the "3から始まる市外局番" file dated 2024-03-01; 1,146 of 3,200 Tokyo local codes unassigned | ✅ valid fixed line | Derived (could be allocated later) |
| `03-1xxx`, `03-2xxx`, `03-7xxx`–`03-9xxx` | Not in MIC's list at all (Tokyo local codes defined only from 3100 to 6999) | ✅ valid (e.g. `03-1234-5678`) | Derived — probably never assignable, but the rule was not confirmed in the notice text |
| `070-98xx-xxxx`, `070-99xx-xxxx` (mobile) | Unassigned in the 070 file dated 2026-09-01 | ✅ valid mobile | Derived |
| `060-15xx-xxxx` … `060-99xx-xxxx` (mobile) | Unassigned in the 060 file dated 2025-07-01 (060 was only recently opened) | ✅ valid mobile | Derived |
| `090-…`, `080-…` | Fully allocated (files dated 2024-09-01) | — | **Avoid** |
| `03-0xxx`, `090-0000-0000` | Structurally invalid | ❌ | Avoid (fails validation) |

Recommendation: `03-3150-00nn` for fixed lines and `070-9800-00nn` for mobile
(`+81 3 3150 00nn`, `+81 70 9800 00nn`). Re-check against MIC before freezing.

### 1.7 Email and web domains

| Value | Status | Notes |
|---|---|---|
| `example.jp`, `example.co.jp`, `example.ne.jp`, `example0`–`example9` under these, `ドメイン名例.jp` (`xn--eckwd4c7cu47r2wf.jp`) | **Reserved** | JPRS FAQ "例示に使用可能なドメイン名" ([jprs.jp/faq/use/](https://jprs.jp/faq/use/)); ✅ all NXDOMAIN |
| `oobussan.co.jp` (JP PINT) | Avoid | Not registered but not reserved |
| RFC 2606/6761 names (`*.example`, `*.test`, `example.com`) | Reserved | As in the France file |

Recommendation: `seikyu@marumaru-shoji.example.co.jp`, or the party alias as
`<alias>.example.co.jp` / `<alias>1.example.jp`.

### 1.8 Bank, product, customs and other identifiers

| Element | Value / range | Status | Source / Notes |
|---|---|---|---|
| Zengin bank code (金融機関コード, 4 digits) + branch (3 digits) + type (`1` 普通 ordinary, `2` 当座 current) + account (7 digits) | JP PINT `1234:567:1:3242394` | Published example | No reserved test bank code found (Zengin-kyō publishes none). Banks' own file specs use their real codes. `1234` is absent from the community [zengin-code/source-data](https://github.com/zengin-code/source-data) list (1,146 codes; not official). `0001` is Mizuho, `9900` Japan Post Bank (ゆうちょ) — **Avoid** |
| IBAN | — | n/a | Japan does not use IBAN; use `cac:PayeeFinancialAccount/cbc:ID` as JP PINT does |
| GTIN-13 / JAN | `4512345000035`, ITF/GTIN-14 `14512345000032` | Published example | GS1 Japan slide deck (2019, hosted by MLIT, [001347058.pdf](https://www.mlit.go.jp/common/001347058.pdf)); ✅ check digits; ❌ **not** checked against GEPIR — `4512345` may be a real company prefix. Japan's prefixes are `450`–`459` and `490`–`499`. GS1 prefix `952` (demo) remains the safer choice |
| NACCS importer/exporter code (輸出入者符号) | Corporate Number + 4-digit branch, e.g. `1234567890123-0000`; customs code `10000ABC0000`; JASTPRO `P06543210000` | Published example | Japan Customs ([naccsriyou.pdf](https://www.customs.go.jp/zeikan/seido/zeikancode/upload/naccsriyou.pdf)); its corporate numbers `5001234567890`, `2345678901234` ❌ fail the check digit. Use `9234567890123-0000` (Derived) |
| Vehicle registration plates | — | Not researched | No official specimen found in the time available |

---

## 2. South Korea (대한민국)

### 2.1 E-invoicing context

The NTS e-tax invoice (전자세금계산서) uses the KEC XML standard (KEC XML
표준전자세금계산서 v3.0), namespace
`urn:kr:or:kec:standard:Tax:ReusableAggregateBusinessInformationEntitySchemaModule:1:0`.
It is UN/CEFACT-based, **not UBL**, and Korea has no Peppol authority.

- No official example XML or test identifiers were found on nts.go.kr or hometax.go.kr.
- Conformance testing runs on the NIPA certification site `taxcerti.org`, which was unreachable from the research environment.
- A widely copied unsigned sample (GitHub `ruseel/kr-etax-sample`, secondary) contains BRNs `2048631263` and `6028131841`. Both pass the checksum, so they are probably real. It also contains real-looking email addresses at `klnet.co.kr` and `freechal.com`, and the name `(주)샘플사업자` ("Sample Business Co."). **Avoid** (see §2.8).

### 2.2 Business registration number (사업자등록번호)

- Format: `XXX-XX-XXXXX`.
  - First 3 digits: historically the tax office code.
  - Next 2 digits: type (e.g. `81` = for-profit corporation HQ, `85` = branch; `01`–`79` = individuals).
  - Next 4 digits: serial number.
  - Last digit: check digit.
- Check digit (✅ implemented; algorithm from consistent secondary sources, **no NTS primary document found**):
  1. Weights `1,3,7,1,3,7,1,3,5` on digits 1–9.
  2. Add `floor(d₉ × 5 / 10)`.
  3. Check digit = `(10 − sum mod 10) mod 10`.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| Common "example" `123-45-67890` | Used by KEPCO, KIPS and many blogs; no NTS source | Avoid | ❌ check digit (would be `…891`) |
| `987-65-43210` | Blog examples | Avoid | ❌ check digit |
| Party-set series `000-81-0nnnC` | `000-81-00014`, `000-81-00028`, `000-81-00033`, `000-81-00047`, `000-81-00052`, `000-81-00066`, `000-81-00071`, `000-81-00085`, `000-81-00090`, `000-81-00106`, `000-81-00111`, `000-81-00125`, `000-81-00130`, `000-81-00144`, `000-81-00159`, `000-81-00163`, `000-81-00178`, `000-81-00182`, `000-81-00197`, `000-81-00203`, `000-81-00218`, `000-81-00222`, `000-81-00237`, `000-81-00241`, `000-81-00256`, `000-81-00260`, `000-81-00275` | Derived | ✅ check digits. Office code `000` is not a tax office (secondary). ⚠️ **existence not verified**: the NTS status API (data.go.kr 사업자등록정보 진위확인 및 상태조회) needs a service key, and Hometax was unreachable |

### 2.3 Corporate registration number (법인등록번호)

13 digits, written `XXXXXX-XXXXXXX`, issued by the court registry (등기소). The check
digit is commonly described as weights `1,2,1,2,…` on the first 12 digits, then
`(10 − sum mod 10) mod 10`. This is **unverified**: only secondary sources, and no
official example was found. Not needed for Peppol/UBL party identification; omit it or
mark it clearly fictitious.

### 2.4 Resident registration number (주민등록번호) — Avoid entirely

- Format `YYMMDD-GNNNNNN`.
- Until September 2020, digits 8–11 encoded the region and the last digit was a mod-11 check digit.
- Since 5 October 2020 (주민등록법 시행규칙 amendment, MOIS), the six digits after the gender digit are assigned at random ([korea.kr](https://www.korea.kr/news/policyNewsView.do?newsId=148872723)). So a checksum test no longer proves anything.
- Collecting these numbers is restricted by the Personal Information Protection Act.
- No official specimen *number* was verified: the MOIS ID-card specimen exists only as an image.
- The official placeholder **name** is `홍길동` (Hong Gil-dong). It appears in MOIS specimens, the UPU Korea sheet and many government forms.

### 2.5 Postal codes and addresses (Korea Post / 우정사업본부, MOIS)

- Since 1 August 2015, postcodes are the 5-digit State Basic District number (국가기초구역번호).
  - Digits 1–2 = province; digits 1–3 = city/county/district; digits 4–5 = serial number.
  - About 34,000 numbers are in use.
- Korea Post states that numbers were assigned **"from Seoul (01XXX) to Jeju (63XXX), excluding reserve numbers kept for future unification and urban development"** (국가기초구역번호는 향후 통일과 도시개발을 대비하여 예비번호를 제외하고 서울(01XXX)부터 제주(63XXX)까지 부여) ([epost](https://www.epost.go.kr/search/zipcode/cmzcd004k01.jsp)).

| Province prefixes (Korea Post) | |
|---|---|
| Seoul 서울 `01`–`09` · Gyeonggi 경기 `10`–`20` · Incheon 인천 `21`–`23` · Gangwon 강원 `24`–`26` · Chungbuk 충북 `27`–`29` · Sejong 세종 `30` · Chungnam 충남 `31`–`33` · Daejeon 대전 `34`–`35` · Gyeongbuk 경북 `36`–`40` · Daegu 대구 `41`–`43` · Ulsan 울산 `44`–`45` · Busan 부산 `46`–`49` · Gyeongnam 경남 `50`–`53` · Jeonbuk 전북 `54`–`56` · Jeonnam 전남 `57`–`60` · Gwangju 광주 `61`–`62` · Jeju 제주 `63` | |

| Finding | Detail | Status |
|---|---|---|
| `00xxx`, `64xxx`–`99xxx` | Outside the assigned range per Korea Post; within ranges, Korea Post also names reserve numbers (e.g. Jongno-gu `03199`–`03299`) | Derived (would fail an existence check). The 70000–99998 "North Korea" reserve is secondary (Namuwiki) |
| Database check | Korea Post's postcode DB and juso.go.kr could not be downloaded | ⚠️ not verified |

Official example addresses (UPU *Postal addressing systems — Korea (Rep.)*, 03/2016):

| Example | Notes |
|---|---|
| `Mr. Hong, Gil Dong` / `101-dong 103-ho` / `2275-12, Dalgubeol-daero, Suseong-gu` / `DAEGU 42007` / `REP. OF KOREA` | Building complex (`-dong` building, `-ho` unit) |
| `Dr. Hong, Gil Dong` / `24, Songnim-ro, Dong-gu` / `INCHEON 22554` | Urban |
| `Mr. Hong, Gil Dong` / `6, Jong-ro, Changnyeong-eup, Changnyeong-gun` / `GYEONGSANGNAM-DO 50329` | Rural |
| `Mr. Hong, Gil Dong` / `P.O. Box 00` / `51, Oncheon-ro, Yuseong-gu` / `DAEJEON 34186` | P.O. box (`00` is a placeholder) |
| `Samsung Card Bldg.` / `194, Yulgok-ro, Jongno-gu` / `SEOUL 03127` | **Avoid**: a real company building |

Korean-script order is the reverse of the English: `대구광역시 수성구 달구벌대로 2275-12 101동 103호`.
Strategy: as in Japan, use a real road + district + postcode with a building number
checked not to exist on juso.go.kr. That check could not be done here.

### 2.6 Telephone numbers (MSIT / 과학기술정보통신부)

**No range is reserved for fiction or examples** (searched in Korean and English).

- The Korean Film Council (KOFIC, 영화진흥위원회) lends film producers 4 landlines and 2 mobile lines "for screen exposure".
- These are real, unpublished numbers. OTT dramas are not covered: the 2021 *Squid Game* incident ([HuffPost Korea](https://www.huffingtonpost.kr/article/113673)).

| Range | Notes | libphonenumber 9.0.42 | Status |
|---|---|---|---|
| `010-0xxx-xxxx`, `010-1xxx-xxxx` | Exchange codes 0000–1999 reportedly not assignable to subscribers (secondary: Namuwiki); `0100` is used for satellite phones | ✅ valid mobile | Derived, ⚠️ not confirmed in the MSIT 전기통신번호관리세칙 (Telecommunications Numbering Management Rules) |
| `02-0xxx-xxxx`, `02-1xxx-xxxx` (Seoul) | Local exchanges start with 2–9 (Korean Wikipedia, secondary) | ❌ `02-0123-4567` invalid | Avoid (fails validation) |
| `010-1234-5678`, `010-0000-0000` | Valid format; `010-1234-…` falls in the 1xxx range above | ✅ | Derived; do not use `010-xxxx` with exchange ≥ 2000 |

Recommendation: `010-1000-00nn` (`+82 10 1000 00nn`) as Derived, with the caveat
above. For landlines no unassigned range was verified, so mask the number or omit it.

### 2.7 Email and web domains

| Value | Status | Notes |
|---|---|---|
| `example.kr`, `example.co.kr` | **Avoid** | Registered (NS `comn.com`) ✅ DNS |
| `test.co.kr`, `sample.co.kr` | **Avoid** | Registered ✅ DNS |
| `example.or.kr` | Not registered (NXDOMAIN) | Not reserved by KISA as far as found; Derived at best |
| RFC 2606/6761 names | Reserved | Use `<alias>.example` or `example.com` for Korean parties |

KISA's 도메인이름 관리준칙 (Domain Name Management Rules) allows reserving publicly
listed names, but no example-domain reservation like JPRS's was found.

### 2.8 Banks and other identifiers

| Element | Notes | Status |
|---|---|---|
| Bank codes (금융기관 공동코드, 3 digits, KFTC 금융결제원) | e.g. `004` KB Kookmin, `088` Shinhan, `020` Woori; no test code found | Not researched in depth |
| IBAN | Korea does not use IBAN | n/a |
| GTIN | Korea prefix `880` (GS1 Korea); no official example checked; use GS1 `952` | — |
| Placeholder person name | `홍길동` (Hong Gil-dong); also seen: `김철수`, `이영희` (common textbook names) | Published example (`홍길동`) |

---

## 3. Avoid list

| Value | Seen as | Why |
|---|---|---|
| `1234567890123`, `3210987654321`, `7654321098765` (and `T`-prefixed forms) | JP PINT / NTA examples | Fail Corporate Number check digit (deliberate); use the §1.2 corrected forms |
| `>T3210987654321` | JP PINT files | Typo |
| `160-0044` | JP PINT supplier postcode | Non-existent postcode |
| `03-3xxx-0001`, `011-757-1xxx`, `shirou_aoki@〇〇co.jp` | JP PINT contacts | Masked/malformed |
| `oobussan.co.jp` | JP PINT email domain | Unreserved, registrable by anyone |
| `5001234567890`, `2345678901234` | Japan Customs NACCS examples | Fail check digit |
| `123456789012` | My Number card specimen | Fails check digit, and My Number must not be used |
| `7000012050002` | Seen in check-digit tutorials | Real: National Tax Agency (国税庁) |
| `1180301018771` | — | Real: Toyota Motor Corporation (positive control) |
| `0001`, `0005`, `9900` bank codes | Common examples | Real banks (Mizuho, MUFG, Japan Post Bank) |
| `100-8792` | UPU contact | Real Japan Post HQ business postcode |
| `123-45-67890`, `987-65-43210` | Korean "example" BRNs | Fail check digit |
| `204-86-31263`, `602-81-31841` | Korean e-tax sample on GitHub | Pass checksum, probably real businesses |
| `124-81-00998`, `220-81-62517` | Seen in validator tutorials | Pass checksum; widely cited as Samsung Electronics and Naver (not verified on Hometax) |
| `example.kr`, `example.co.kr`, `test.co.kr`, `sample.co.kr` | Example domains | Registered |
| `Samsung Card Bldg., 194 Yulgok-ro` | UPU Korea example | Real company building |
| `서울특별시 강남구 테헤란로 123` | Blog invoice examples | Real road; the building number very likely exists |

---

## 4. Sources

**Japan**

- Peppol/Digital Agency: [JP PINT](https://docs.peppol.eu/poac/jp/pint-jp/) ([resources.zip](https://docs.peppol.eu/poac/jp/pint-jp/resources.zip)) · [JP BIS Self-Billing](https://docs.peppol.eu/poac/jp/pint-jp-sb/) · [JP BIS Non-tax Registered](https://docs.peppol.eu/poac/jp/pint-jp-ntr/)
- NTA Corporate Number: [Check-digit method (checkdigit.pdf)](https://www.houjin-bangou.nta.go.jp/documents/checkdigit.pdf) · [Publication site](https://www.houjin-bangou.nta.go.jp/) · [Web-API](https://www.houjin-bangou.nta.go.jp/webapi/)
- NTA invoice system: [Q&A 問18 registration number structure](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/qa/18.pdf) · [Q&A 01-09 invoice items](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/qa/01-09.pdf) · [Invoice leaflet 0024002-057_a](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0024002-057_a.pdf) · [Qualified Invoice Issuer publication site](https://www.invoice-kohyo.nta.go.jp/)
- My Number: [MIC ordinance No. 85 (e-Gov)](https://laws.e-gov.go.jp/law/426M60000008085) · [MIC card leaflet with specimen](https://www.soumu.go.jp/main_content/001039529.pdf)
- Japan Post: [Postcode data download](https://www.post.japanpost.jp/zipcode/download.html) (utf_ken_all.zip, jigyosyo.zip)
- UPU: [Postal addressing systems — Japan](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/jpnEn.pdf)
- MIC numbering: [電気通信番号指定状況](https://www.soumu.go.jp/main_sosiki/joho_tsusin/top/tel_number/number_shitei.html) · [03 area file (xls)](https://www.soumu.go.jp/main_content/000697545.xls) · [070 file](https://www.soumu.go.jp/main_content/001090878.xlsx) · [060 file](https://www.soumu.go.jp/main_content/001019693.xlsx) · [090 file](https://www.soumu.go.jp/main_content/000697567.xlsx)
- JPRS: [FAQ — domain names usable for examples](https://jprs.jp/faq/use/)
- GS1 Japan: [GS1の仕組み (MLIT-hosted, 2019)](https://www.mlit.go.jp/common/001347058.pdf) · [Code overview](https://www.gs1jp.org/code/)
- Japan Customs: [NACCS importer/exporter codes with Corporate Number](https://www.customs.go.jp/zeikan/seido/zeikancode/upload/naccsriyou.pdf)
- Secondary: [zengin-code/source-data](https://github.com/zengin-code/source-data) · [Blog: no fictional phone numbers in Japan](https://shinkufencer.hateblo.jp/entry/2021/03/27/000000)

**South Korea**

- Korea Post: [Postcode structure (cmzcd003k01)](https://www.epost.go.kr/search/zipcode/cmzcd003k01.jsp) · [Province ranges (cmzcd004k01)](https://www.epost.go.kr/search/zipcode/cmzcd004k01.jsp) · [korea.kr 2015-07-30 announcement](https://www.korea.kr/news/policyNewsView.do?newsId=148798638)
- UPU: [Postal addressing systems — Korea (Rep.)](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/korEn.pdf)
- MOIS resident number reform: [korea.kr policy news](https://www.korea.kr/news/policyNewsView.do?newsId=148872723) · [MOIS ID card page](https://www.mois.go.kr/frt/sub/a06/b06/IDCard/screen.do)
- NTS: [National Tax Service](https://www.nts.go.kr/) · [data.go.kr: 전자(세금)계산서 제도의 이해](https://www.data.go.kr/data/15050750/fileData.do)
- KCC research (numbering, 2009): [010번호통합 및 중장기 번호자원관리 방안 연구](https://www.kmcc.go.kr/download.do?fileSeq=28044)
- KISA: [도메인이름 관리준칙](https://krnic.kisa.or.kr/jsp/infoboard/law/domManRule.jsp)
- Secondary: [HuffPost Korea — KOFIC screen phone numbers](https://www.huffingtonpost.kr/article/113673) · [ruseel/kr-etax-sample](https://github.com/ruseel/kr-etax-sample) · [Korean Wikipedia — telephone numbering](https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8_%EC%B2%B4%EA%B3%84) · [BRN checksum explanation (hongpage.kr)](https://hongpage.kr/96)

**Both**

- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- libphonenumber: Python port [`phonenumbers`](https://pypi.org/project/phonenumbers/) 9.0.42
