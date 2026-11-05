# Fictitious-but-valid example identifiers — mainland China, Hong Kong, Taiwan

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation or person, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with Simplified Chinese (mainland), Traditional Chinese
(Hong Kong, Taiwan) and English queries. Checks marked ✅ were run during research:
check characters for the Unified Social Credit Code (GB 32100), the organisation code
(GB 11714), the resident identity number (GB 11643), the HKID, the Taiwan Unified
Business Number (old and 2023 rule) and the Taiwan national ID; lookups of Taiwan
UBNs in three official open registers (Ministry of Finance tax registration dataset
`BGMOPEN1`, 1,715,523 rows, dated 2026-11-05; MOEA company register API; MOEA business
register API); DNS lookups of candidate placeholder domains.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**

- **No region formally reserves identifiers, telephone numbers or postcodes for
  fiction or tests.** Nothing like ARCEP's or Ofcom's drama numbers exists in the
  mainland (MIIT), Hong Kong (OFCA) or Taiwan (NCC / now MODA).
- The standards themselves publish **valid worked examples**: GB 32100-2015's USCC
  `91350100M000100Y43` and GB 11643-1999's ID numbers; the Taiwan Ministry of
  Finance's UBN worked examples `10458575` / `19312376`.
- Official **specimen ID cards deliberately fail the check digit**: all eight Hong
  Kong Immigration Department specimens and the Taiwan Ministry of the Interior
  specimen `A234567890`. Useful as "obviously fake" values, not as valid ones.
- Hong Kong's tax authority masks BR numbers in its specimens (`5XXXXXXX-000-04-17-A`).

---

## 1. Mainland China (中国大陆)

### 1.1 Unified Social Credit Code (统一社会信用代码, USCC)

Defined by **GB 32100-2015** *法人和其他组织统一社会信用代码编码规则* (mandatory, in
force since 2015-10-01, amendment No. 1 from 2016-04-18; a revision, plan
20260042-Q-469, is being drafted). 18 characters from the set
`0123456789ABCDEFGHJKLMNPQRTUWXY` (no `I O S V Z`).

| Position | Meaning |
|---|---|
| 1 | Registration authority (登记管理部门): `1` 机构编制 · `5` 民政 · `9` 工商 (market regulation, i.e. companies) · `Y` other … |
| 2 | Entity category (机构类别): with `9`: `1` 企业 enterprise, `2` 个体工商户 sole trader, `3` 农民专业合作社 cooperative |
| 3–8 | Administrative division code of the registering authority (GB/T 2260) |
| 9–17 | Subject identifier = 9-character organisation code (GB 11714: 8 characters + check) |
| 18 | Check character: `C18 = 31 − MOD(Σ Ci·Wi, 31)`, `Wi = 3^(i−1) mod 31` (weights 1 3 9 27 19 26 16 17 20 29 25 13 8 24 10 30 28); result 31 → `0` |

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| USCC (enterprise, Fuzhou `350100`) | `91350100M000100Y43` | Published example | GB 32100-2015 Appendix B worked example; ✅ check character `3`; ✅ embedded organisation code `M000100Y-4` passes the GB 11714 check (weights 3 7 9 10 5 8 4 2, mod 11). ⚠️ Existence **not verified**: the national register (gsxt.gov.cn) needs a captcha. Widely reused as a test value in validator libraries and in Alibaba Cloud API docs |
| VAT / taxpayer ID (纳税人识别号) | Same as USCC | Rule | Since the 2015 "three certificates in one" reform the taxpayer identification number of an organisation is its USCC; the e-invoice form labels the field 统一社会信用代码/纳税人识别号 |
| Peppol / ISO 6523 | — | — | No China-specific ICD found for USCC; use `cbc:CompanyID` without `schemeID` |

Only one official valid example exists. Deriving more USCCs is easy (compute the
check character), but without a register lookup any derived value may be a real
entity. Recommendation: use `91350100M000100Y43` for one Chinese party at most; for
others, consider category `Y1` (other) + an obviously synthetic subject identifier and
mark them Derived/unverified.

### 1.2 Fully digitalised e-invoice (全面数字化的电子发票, 数电发票, formerly 全电发票)

Source: 国家税务总局公告2024年第11号 *关于推广应用全面数字化电子发票的公告* (in force
2024-12-01).

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Invoice number (发票号码) | 20 digits: 1–2 year (last 2 digits), 3–4 provincial tax bureau area code, 5 issuing channel, 6–20 sequence | Rule | Art. 4 of the announcement. No example number is published |
| Invoice types | 电子发票（增值税专用发票）, 电子发票（普通发票）, 航空运输电子客票行程单, 铁路电子客票, 机动车销售统一发票, 二手车销售统一发票 … | Rule | |
| Official sample (票样) | Attachment 1 *数电发票样式* (`.doc`, 20 pages) | Published example | ✅ Downloaded and inspected: **blank layouts only**, no example data (no names, codes or amounts) |
| Mandatory face fields | 发票名称, 发票号码, 开票日期, 购买方信息, 销售方信息, 项目名称, 规格型号, 单位, 数量, 单价, 金额, 税率/征收率, 税额, 合计, 价税合计, 备注, 开票人 | Rule | Useful mapping checklist for a Chinese UBL invoice example |

The XML format that the national e-invoice service platform delivers to taxpayers was
not found as a public specification with sample files (not verified either way).

### 1.3 Resident identity number (公民身份号码)

Defined by **GB 11643-1999**: 6-digit address code (GB/T 2260) + 8-digit birth date +
3-digit sequence (odd = male, even = female) + check character (ISO 7064 MOD 11-2;
weights `2^(i−1) mod 11`, remainder 0–10 → `1 0 X 9 8 7 6 5 4 3 2`).

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| ID (female, Beijing Chaoyang, born 1949-12-31) | `11010519491231002X` | Published example | GB 11643-1999 Appendix A; ✅ MOD 11-2. ⚠️ Plausibly a real person: address code `110105` is current and the date is realistic |
| ID (male, Shantou Chaoyang county, born 1880-01-01) | `440524188001010014` | Published example | GB 11643-1999 Appendix A; ✅ MOD 11-2. Safer: born 1880, and `440524` (潮阳县) is no longer a current division code |

Recommendation: personal ID numbers are rarely needed in UBL; if one is needed for the
Consumer party, use `440524188001010014`.

### 1.4 Telephone numbers

**No reserved fictional range found.** MIIT's *电信网编号计划（2017年版）* (the newest edition found) and the *电信网码号资源管理办法* contain no range for films,
drama or documentation; searches in Chinese and English found none. The newest
dedicated range found is `700` for number-protection ("privacy number") services
(工信部信管函〔2025〕130号), which is a real service. Recommendation: do not invent
mainland numbers (`+86 1xx xxxx xxxx` mobile, `+86 10 xxxx xxxx` Beijing landline are
all potentially real).

### 1.5 Postal codes (邮政编码)

6 digits, four-level structure (digits 1–2 province, 3 postal area, 4 county,
5–6 delivery office; GB/T 7156; secondary sources only, chinapost.com.cn not
checked). China Post assigns `999077` (Hong Kong), `999078` (Macao), `999079`
(Taiwan) for its own sorting; these places do not use them. No official fictitious
code found. A real code + real district + invented street is the only pattern that
passes a postcode check.

### 1.6 Other identifiers

| Element | Rule / value | Status | Notes |
|---|---|---|---|
| Vehicle plate (机动车号牌) | Province abbreviation + issuing-authority letter + 5 (6 for new-energy) serial characters; **serial never uses `I` or `O`** | Rule | GA 36-2018. An example such as `闽A·12345` is format-valid but may be real; a serial with `O` (e.g. `闽A·1O345`) can never be real but fails strict validation |
| Bank account / CNAPS bank code (联行号, 12 digits) | — | Not found | China has no IBAN. No official fictitious CNAPS code or account found (not researched in depth) |
| Customs codes (海关编码) | Party: USCC (the 10-digit customs registration code still exists alongside); goods: 10-digit HS-based commodity code | Rule | Commodity codes are a public classification and can be used as-is. No example party customs code found |
| GLN/GTIN | GS1 China prefixes `690`–`699` are real; use GS1 prefix `952` (reserved for demos) | Reserved | See France file §6 |

---

## 2. Hong Kong (香港)

### 2.1 Business Registration number (商業登記號碼, BR / BRN)

8 digits = first 8 characters of the certificate number
`99999999-&&&-&&-&&-&` (branch, month, year, check character). Since 2023-12-27 the
BRN is also the Unique Business Identifier replacing the company registration number,
and it is Hong Kong's entity TIN (OECD TIN sheet). **No check-digit algorithm is
published** for the 8-digit BRN; validation can only be `^\d{8}$`.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Certificate No. | `5XXXXXXX-000-04-17-A` | Published example (masked) | IRD specimen certificates (`new_main_brc.pdf`, `onestop_spec.pdf`); `7XXXXXXX-000-02-24-A` in the limited partnership fund specimen. Masked, so **not** a valid number |
| Certified extract BRN | `3XXXXXXX-000` | Published example (masked) | IRD `br_ctc_sample.pdf` |
| Name | `ＸＸ貨櫃運輸公司` / `KXX DXX TRANSPORTATION COMPANY` (`… LIMITED`), `KXX DXX LIMITED PARTNERSHIP FUND` | Published example | IRD specimens |
| Address | `X/F XXX GLOUCESTER ROAD WANCHAI HK`; `X/F XXX CONCORDE RD KAI TAK KL` | Published example | Masked house numbers on real streets |

Recommendation: there is no official valid BRN. Any 8-digit number is format-valid,
but cannot be checked for non-existence without the paid IRD/Companies Registry
search; mark derived BRNs as such.

### 2.2 HKID (香港身份證號碼)

Format: 1–2 letters + 6 digits + check character (0–9 or `A`) printed in brackets.
The check character is "not part of the identity card number" (ImmD ROP133). The
check algorithm (letters A=10…Z=35, a single letter padded with value 36, weights
9…2, `11 − (sum mod 11)`, 10 → `A`, 11 → `0`) is **not published by ImmD**; it is the
widely used algorithm, confirmed by the well-known example `A123456(3)` ✅, and the
OECD TIN sheet confirms the 11 possible values 0–9 and A.

All official specimens **fail** this check (deliberately, it appears):

| Card (ImmD source) | Name on specimen | Printed number | Status | Check |
|---|---|---|---|---|
| Permanent ID, labelled diagram (ROP133, 10/2025) | 齊煥正 CHAI, Wun Ching | `D899336(6)` | Published example | ❌ correct would be `(0)` |
| Adult permanent (press release 2025-04-28, Annex II) | 樂永晴 LOK, Wing Ching | `Z683365(5)` | Published example | ❌ correct `(A)` |
| Juvenile permanent | 林日朗 LAM, Yat Long | `Z691338(2)` | Published example | ❌ correct `(6)` |
| Minor permanent | 余樂芯 YU, Lok Sum | `Z982600(5)` | Published example | ❌ correct `(A)` |
| Adult non-permanent | WILLIAMS, Peter | `G908833(1)` | Published example | ❌ correct `(3)` |
| Juvenile non-permanent | 林日朗 LAM, Yat Long | `Z988132(8)` | Published example | ❌ correct `(9)` |
| Overseas-issued adult | LOK, Wing Ching | `Z690266(6)` | Published example | ❌ correct `(A)` |
| Overseas-issued minor | CHEUK, Chi Yin | `Z988300(8)` | Published example | ❌ correct `(3)` |

The specimens also carry Chinese commercial codes (e.g. `7871 3562 2973`) and the
symbols `***AZ`. Recommendation: personal IDs are rarely needed; if one is, use a
specimen number as printed (official and obviously fake) and accept that it fails
validation, rather than a check-valid number that may belong to a real person.

### 2.3 Telephone numbers

**No range reserved for fiction or examples.** OFCA's *Numbering Plan for
Telecommunications Services in Hong Kong* (issue 2026-11-02) has no drama/fiction
category; searches in English and Traditional Chinese found none.

| Range | Status in the plan | Usable as example? |
|---|---|---|
| `74xx xxxx`–`79xx xxxx` (the `7(4-9)X` levels) | "Reserved" for future migration to a longer numbering plan (CA statement 2016-06-24) | Derived: unassigned, so it cannot reach a real subscriber today; not a formal example range |
| Repeating blocks such as `2020 xxxx`, `2222 xxxx`, `3456 xxxx`, `4567 xxxx` | "Reserved" pending "special number arrangement" (auction of golden numbers) | Avoid: may be assigned later |

International format: `+852 7400 0000` (Derived, unassigned level).

### 2.4 Addresses

Hong Kong has **no postcodes**. Hongkong Post's addressing pages
(`hongkongpost.hk/.../correct_address/`, `.../postcode/`) returned HTTP 403 and could
not be read; according to secondary sources (Wikipedia, citing them), Hongkong Post
advises leaving the field blank or entering `000`, `0000`, `000000` or `HKG` where a
form requires one, and the order is name · flat/floor · building · number + street ·
district · region (`HONG KONG` / `KOWLOON` / `NEW TERRITORIES`). In UBL, omit
`cbc:PostalZone`; country code `HK`. The IRD specimen pattern (masked number on a
real street) is the closest official example: `X/F XXX GLOUCESTER ROAD, WANCHAI, HK`.

### 2.5 Bank identifiers

No IBAN. Accounts are 3-digit bank (clearing) code + 3-digit branch code + account
number; codes are assigned by HKICL (official list *Clearing Code and Branch Code*,
version 2026/042, 3 Oct 2026). All listed codes are real banks (e.g. `003` Standard
Chartered, `004` HSBC, `012` Bank of China (HK)). No fictitious bank code and no
published FPS test proxy ID found (FPS proxy IDs are a phone number, email or FPS ID).
BIC: use the ISO 9362 test convention (8th character `0`, e.g. `XXXXHKH0`).

---

## 3. Taiwan (臺灣)

### 3.1 Unified Business Number (營利事業統一編號, UBN, 統編)

8 digits; weights `1 2 1 2 1 2 4 1`; add the two digits of each product and sum. Since
**2023-04-01 (民國112年4月1日)** the sum must be divisible by **5** (previously 10),
to extend the number space; if the 7th digit is `7`, the sum or sum + 1 may be used.
The old rule is a subset of the new one, so validators only need `% 5`.

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| UBN (7th digit `7`, sum 20) | `10458575` | Published example | MOF *營利事業統一編號檢查碼邏輯修正說明（附件）*; ✅ old and new rule; ✅ not in MOF tax dataset, MOEA company or business register |
| UBN (7th digit `7`, sum 30) | `19312376` | Published example | Same MOF attachment; ✅ old and new rule; ✅ not in the three registers |
| UBN | `04595257` | **Avoid** | MOF's first worked example, but ✅ a real (revoked) company: 擎天金屬股份有限公司 in the MOEA register |
| UBN (new rule only) | `04595252`, `10458570` | Derived (secondary) | Third-party "test numbers" (toolmaple.com), not in the MOF attachment; ✅ valid only under the 5-rule; ✅ not in the three registers. Useful for testing new-rule support |
| UBN | `12345675` | Derived | ✅ both rules; ✅ not in the three registers |
| UBN | `00000000`, `99999997`, `88888880` | **Avoid** | ✅ checksum-valid but real (closed) sole proprietorships in the MOEA business register |
| UBN | `00000016`, `00000022`, `00000005` | **Avoid** | Real companies (active or dissolved) in the MOEA company register, although `00000016` is missing from the MOF tax dataset |

Limitation: UBNs are also assigned to withholding units (扣繳單位: schools, government
bodies, associations) that are not in these registers, so "not found" is strong but
not conclusive evidence. The MOF dataset alone misses some registered companies.

### 3.2 E-invoice (電子發票) — MOF e-invoice platform

| Element | Value / rule | Status | Notes |
|---|---|---|---|
| Test platform | `https://wwwtest.einvoice.nat.gov.tw` (separate registration from production) | Official | Per MOF's *Turnkey 上線前自行檢測作業* v4.7.1 (2024-03-21), as quoted in search snippets (PDF not reachable): "測試資料請勿填寫真實個人及營業資料" — test data must not contain real personal or business data |
| Invoice track/number (字軌號碼) | 2 capital letters + 8 digits, e.g. pattern `AB12345678` | Rule | Test track numbers are issued on the test platform per business (limit 50 booklets) |
| Message format | MIG 4.0 (`F0401` platform-registered invoice, `F0501` void …; from 2025-01-01) | Rule | National XML, not UBL |
| Mobile barcode carrier | `CarrierType=3J0002`, `CarrierId` 8 characters starting with `/` | Rule | From the Turnkey self-test document (via search snippets) |
| Official test UBNs | — | Not verified | The Turnkey and MIG PDFs on einvoice.nat.gov.tw returned **HTTP 403** to both curl and WebFetch; search snippets show a "測試統編" column but no values. Not resolved |

### 3.3 National ID (國民身分證統一編號)

Letter (household registration city/county, A = Taipei …) + sex digit (`1` male,
`2` female) + 7 digits + check digit. Letter value (A=10 … with I=34, O=35, W=32, X=30,
Y=31, Z=33) split into two digits, weights `1 9 8 7 6 5 4 3 2 1 1`, total divisible by
10 (regulation *國民身分證及戶口名簿格式內容製發相片影像檔建置管理辦法* art. 3 defines the
structure; the check rule is from secondary sources).

| Element | Value | Status | Checks/Notes |
|---|---|---|---|
| Specimen card (樣本), 陳筱玲, born 民國57年6月5日 | `A234567890` | Published example | MOI Department of Household Registration, *國民身分證真偽辨識資料*; ❌ fails the check (correct would be `A234567893`), apparently deliberately |
| Textbook example | `A123456789` | **Avoid** | ✅ passes the check, and therefore widely misused; press reports say it belongs to a real person |

### 3.4 Telephone numbers

**No fictional range found.** Number administration moved from NCC to the Ministry of
Digital Affairs (MODA) in 2022. The *電信網路編碼計畫* lists reserved prefixes (e.g.
`011`–`019`, local numbers starting with `9`) for future use and lets the regulator
lend unassigned blocks for tests to operators or research bodies, but nothing for
fiction or documentation. Recommendation: do not invent Taiwanese numbers.

### 3.5 Postal codes (郵遞區號)

3+3 digits since 2020-03-03 (3-digit district + 3-digit delivery section; 3+2 still
seen). Written on line 1 above the address, no separator (Chunghwa Post). Chunghwa
Post's own page uses its real headquarters address `106409 臺北市大安區金山南路2段55號`
(real: Avoid as party data). The full 3+3 file is only available after registration
on `fpp.post.gov.tw`, so unused codes could not be checked. The 3-digit list is open
(data.gov.tw dataset 25489).

### 3.6 Bank identifiers

No IBAN. Bank code = 3-digit financial institution code (+ 4-digit branch), real
institutions only; no fictitious code found (not researched in depth). BIC: ISO 9362
test convention (e.g. `XXXXTWT0`).

---

## 4. Email and web domains (all three regions)

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com`, `example.net`, `example.org` | Reserved | RFC 2606 / RFC 6761 |
| `example.com.cn`, `test.cn`, `ceshi.cn` (测试 "test"), `shili.cn` (示例 "example") | **Avoid** | ✅ registered (NS records present) |
| `example.tw`, `example.com.tw` | **Avoid** | ✅ registered (NS records present) |
| `example.cn` | Avoid (unclear) | DNS lookup returns SERVFAIL, so probably registered |
| `example.hk`, `example.com.hk` | Not registered today | ✅ NXDOMAIN, but not reserved by HKIRC; can be registered at any time, so prefer `.test` |

No registry (CNNIC, HKIRC, TWNIC) reserved example domain was found. Recommendation:
`fapiao@<party-alias>.test` (China), `accounts@<alias>.test` (HK), `invoice@<alias>.test`
(Taiwan).

---

## 5. Avoid list

| Value | Seen as | Why |
|---|---|---|
| `11010519491231002X` | GB 11643 example ID | Valid and realistic; may belong to a real person |
| `+86` / `+852` / `+886` invented numbers | Placeholder phone numbers | No reserved ranges; all may be real |
| HK repeating blocks `2020 xxxx`, `2222 xxxx`, `3456 xxxx` … | "Reserved" in OFCA plan | Special numbers held for later allocation |
| `04595257` | MOF UBN worked example | Real (revoked) company 擎天金屬股份有限公司 |
| `00000000`, `99999997`, `88888880`, `00000005`, `00000016`, `00000022` | Obvious placeholder UBNs | Real (closed or active) businesses |
| `A123456789` | "Example" Taiwan ID | Reportedly a real person's number |
| `106409 臺北市大安區金山南路2段55號` | Chunghwa Post page | Real Chunghwa Post headquarters |
| `example.com.cn`, `test.cn`, `ceshi.cn`, `shili.cn`, `example.tw`, `example.com.tw` | Example domains | Registered |
| HKICL bank codes `003`, `004`, `012` … | Example bank codes | Real banks |

---

## 6. Not verified / open

- Existence of USCC `91350100M000100Y43` (gsxt.gov.cn needs a captcha).
- Taiwan MOF e-invoice test UBNs and MIG 4.0 sample XML (einvoice.nat.gov.tw PDFs
  returned HTTP 403).
- Hongkong Post addressing guidance (pages returned HTTP 403; secondary sources used).
- Mainland postcode unused ranges and China Post primary sources (not reached).
- CNAPS, HK FPS, Taiwan bank codes, mainland customs party codes: no fictitious
  values found; not researched in depth.
- HKID check algorithm: not published by ImmD; widely used algorithm only.

---

## 7. Sources

**Mainland China**
- GB 32100-2015: [openstd.samr.gov.cn record](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=24691C25985C1073D3A7C85629378AC0) · [std.samr.gov.cn (revision status)](https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D808D6D3A7E05397BE0A0AB82A) · [CODS (full text)](https://www.cods.org.cn/cods/2020-10/29/article_2020102914512312575.html) · [Wikisource full text](https://zh.wikisource.org/wiki/GB_32100-2015_%E6%B3%95%E4%BA%BA%E5%92%8C%E5%85%B6%E4%BB%96%E7%BB%84%E7%BB%87%E7%BB%9F%E4%B8%80%E7%A4%BE%E4%BC%9A%E4%BF%A1%E7%94%A8%E4%BB%A3%E7%A0%81%E7%BC%96%E7%A0%81%E8%A7%84%E5%88%99)
- GB 11643-1999: [Wikisource full text](https://zh.wikisource.org/wiki/GB_11643-1999_%E5%85%AC%E6%B0%91%E8%BA%AB%E4%BB%BD%E5%8F%B7%E7%A0%81)
- State Taxation Administration: [公告2024年第11号 (with 数电发票样式 attachment)](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5236067/content.html) · [Fujian 12366: 数电发票号码编码规则](https://fujian.chinatax.gov.cn/bsfw/nsfwrx/12366wtj_201/202501/t20250108_589332.htm)
- MIIT: [电信网编号计划（2017年版）](https://www.miit.gov.cn/jgsj/xgj/wjfb/art/2020/art_eb0adf5b6e7148cbb70802b264878b1e.html)
- GA 36-2018 vehicle plates: [PDF on Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/0/00/GA_36-2018.pdf)
- Postcodes (secondary): [Baidu Baike 邮政编码](https://baike.baidu.com/item/%E9%82%AE%E6%94%BF%E7%BC%96%E7%A0%81) · [Zhihu on 999077](https://www.zhihu.com/question/624779280)

**Hong Kong**
- Immigration Department: [ROP133 Information on the front of the HKID card](https://www.immd.gov.hk/pdforms/rop133.pdf) · [Sample of New Smart Identity Card (Annex II)](https://gia.info.gov.hk/general/202504/28/P2025042500653_493099_1_1745572608931.pdf) · [Smart Identity Card](https://www.immd.gov.hk/eng/services/hkid/smartid.html)
- Inland Revenue Department: [Valid business registration certificate (specimens)](https://www.ird.gov.hk/eng/tax/bre_vbr.htm) · [Specimen certificate](https://www.ird.gov.hk/eng/pdf/new_main_brc.pdf) · [One-stop specimen](https://www.ird.gov.hk/eng/pdf/onestop_spec.pdf) · [LPF specimen](https://www.ird.gov.hk/eng/pdf/onestop_lpf_spec.pdf) · [Certified extract specimen](https://www.ird.gov.hk/eng/pdf/br_ctc_sample.pdf)
- OECD: [Hong Kong TIN information sheet](https://www.oecd.org/content/dam/oecd/en/topics/policy-issue-focus/aeoi/hong-kong-tin.pdf)
- OFCA: [Numbering Plan for Telecommunications Services in Hong Kong](https://www.ofca.gov.hk/filemanager/ofca/en/content_311/no_plan.pdf)
- Hongkong Post (HTTP 403 during research): [Correct address](https://www.hongkongpost.hk/en/about_us/tips/correct_address/index.html) · [Postcode](https://www.hongkongpost.hk/en/about_us/tips/postcode/index.html) · secondary: [Wikipedia, Postal codes in Hong Kong](https://en.wikipedia.org/wiki/Postal_codes_in_Hong_Kong)
- HKICL: [Clearing Code and Branch Code (3 Oct 2026)](https://www.hkicl.com.hk/files/page_file/118/12916/Clearing%20Code%20and%20Branch%20Code%20(3%20Oct%202026)%20with%20Tel%20No.pdf)

**Taiwan**
- Ministry of Finance: [統一編號檢查碼邏輯修正 (news)](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=8d164b10f20042b9ab9864b51b20f0c2) · [檢查碼邏輯修正說明（附件）, copy hosted by trust.org.tw](https://www.trust.org.tw/upload/1100002250002.pdf) · [全國營業(稅籍)登記資料集 BGMOPEN1](https://eip.fia.gov.tw/data/BGMOPEN1.zip)
- MOF e-invoice platform (HTTP 403 during research): [Turnkey 上線前自行檢測作業 v4.7.1](https://www.einvoice.nat.gov.tw/static/ptl/ein_upload/download/9.pdf) · [MIG v4.1](https://www.einvoice.nat.gov.tw/static/ptl/ein_upload/download/5340.pdf) · test platform `https://wwwtest.einvoice.nat.gov.tw`
- MOEA open data: [Company register API](https://data.gcis.nat.gov.tw/od/demo_cond/5F64D864-61CB-4D0D-8AD9-492047CC1EA6) · [Business register API (應用三)](https://data.gcis.nat.gov.tw/od/demo_cond/426D5542-5F05-43EB-83F9-F1300F14E1F1)
- Ministry of the Interior: [國民身分證真偽辨識資料 (specimen image)](https://www.ris.gov.tw/documents/html/apply-idCard/189.html) · [ID card format regulation](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0030030) · [Wikipedia 中華民國國民身分證 (A123456789 misuse)](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%B0%91%E8%BA%AB%E5%88%86%E8%AD%89)
- Numbering: [電信網路編碼計畫 (MOTC)](https://www.motc.gov.tw/uploaddowndoc?file=mlaw%2F201611221609390.pdf&filedisplay=%E9%9B%BB%E4%BF%A1%E7%B6%B2%E8%B7%AF%E7%B7%A8%E7%A2%BC%E8%A8%88%E7%95%AB.pdf&flag=doc) · [NCC telecom page](https://www.ncc.gov.tw/chncc/app/folder/65)
- Chunghwa Post: [國內郵件橫式信封書寫方式](https://www.post.gov.tw/post/internet/Postal/index.jsp?ID=21002) · [3+3 dataset entry](https://data.gov.tw/dataset/150689) · [3-digit postcode dataset](https://data.gov.tw/dataset/25489)
- Secondary: [toolmaple UBN tool (new-rule test numbers)](https://toolmaple.com/tools/tax-id)

**General**
- RFC 2606 / RFC 6761 (reserved domain names); GS1 prefix `952` and ISO 9362 test BIC: see `example-identifiers-fr.md`.
