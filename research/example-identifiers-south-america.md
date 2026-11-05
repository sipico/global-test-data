# Fictitious-but-valid example identifiers — Brazil, Argentina, Chile

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with Portuguese, Spanish and English queries. Checks marked ✅
were run during research:

- check digits: CNPJ (mod 11, including the alphanumeric ASCII − 48 rule), CPF (mod 11),
  CUIT (mod 11), RUT (mod 11), CBU (mod 10, weights 9-7-1-3), Pix BR Code CRC16-CCITT
- CNPJ lookups in BrasilAPI (`brasilapi.com.br/api/cnpj/v1/…`). BrasilAPI is not an
  official service, but it serves the Receita Federal open CNPJ data and already
  handles alphanumeric CNPJs.

Argentina and Chile have **no open registry lookup** (ARCA's old public
`soa.afip.gob.ar/sr-padron` API returns 404; the SII lookup needs a captcha), so
CUITs and RUTs below are checked for check digits only.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**

- None of the three countries uses UBL or Peppol for domestic e-invoicing. Each has
  its own national XML format and a tax-authority clearance model (§1.1, §2.1, §3.1).
- **Brazil** has the strongest official material:
  - Receita Federal's worked example for the new alphanumeric CNPJ, `12.ABC.345/01DE-35`
    (✅ valid · ✅ not registered)
  - Serpro's list of official "CPF fictícios" (22 numbers, ✅ all valid)
  - a reserved homologation CNPJ, `99.999.999/0001-91` (✅ valid · ✅ not registered)
  - mandatory test-environment text literals

  But Serpro's *numeric* "fictitious" CNPJs belong to real companies.
- **Chile** has SII-defined generic RUTs with a real meaning:
  - `66.666.666-6`: anonymous boleta customer
  - `55.555.555-5`: foreign receiver without a RUT

  The SII certification manual also has a "fictitious company" RUT, `97975000-5`.
- **Argentina** has only ARCA web-service examples (`20111111112`, `30000000007`) and
  the meaningful `23000000000` ("No Categorizado").
- No regulator in the three countries reserves telephone numbers for fiction.

---

## 1. Brazil

### 1.1 E-invoicing landscape (not UBL)

| Document | Format | Test environment |
|---|---|---|
| NF-e (model 55, goods B2B) / NFC-e (model 65, retail) | National XML, layout 4.00, namespace `http://www.portalfiscal.inf.br/nfe` (MOC 7.0) | **Homologação**, `tpAmb = 2`; endpoints per state SEFAZ / SVRS; schemas on `hom.nfe.fazenda.gov.br` |
| CT-e (transport) | National XML 4.00 | Homologação, `tpAmb = 2` |
| NFS-e Nacional (services) | National DPS/NFS-e XML (ADN) | **Produção restrita**: `sefin.producaorestrita.nfse.gov.br`, `adn.producaorestrita.nfse.gov.br`, `www.producaorestrita.nfse.gov.br/EmissorNacional/`. Documents issued there have no legal value. |

Not UBL, and there is no Peppol Authority. From 2026 the tax reform adds IBS/CBS fields
(NT 2025.002-RTC) to the existing national formats.

### 1.2 Mandatory test texts and reserved test values (homologação)

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| NF-e `dest/xNome` (E04) when `tpAmb=2` | `NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL` | Reserved | Rejection **598** if different. Capitals, no accents (no `Ç`/`Ã`), ASCII hyphen. NT 2011/002; SEFAZ-PE guide confirms the literal. |
| NF-e `dest/CNPJ` (E02) when `tpAmb=2` | `99999999000191` (`99.999.999/0001-91`) | Reserved | ✅ CNPJ check digits · ✅ not registered (BrasilAPI). Rejection **597** in NT 2011/002. Since layout 3.10 (NT 2015.003) states may require a *valid* destinatário; with `99999999000191` use `indIEDest = 9` (non-contributor). Enforcement varies by state (forum reports, not verified per state). |
| NFC-e first item `det/prod/xProd` when `tpAmb=2` | `NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL` | Reserved | Rejection **373**. Note the different wording from NF-e (`NOTA FISCAL`, not `NF-E`). Attributed to NT 2015/002; only vendor knowledge-base pages were read. |
| CT-e `xNome` of remetente / expedidor / recebedor / destinatário when `tpAmb=2` | `CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL` | Reserved | Rejections **646 / 647 / 648 / 649**. Only vendor knowledge bases were read (Oobj, TecnoSpeed, NDD). Some states reportedly want `CTE` without the hyphen. |

These literals are useful as test-environment markers in a Brazilian sample. They have
no UBL counterpart.

### 1.3 Company identifiers — CNPJ

**Rule.** 14 characters: 8-character root, 4-character branch number (`0001` is
usually the head office) and 2 numeric check digits.

- Check digits: mod 11. First DV weights `5 4 3 2 9 8 7 6 5 4 3 2`, second DV weights
  `6 5 4 3 2 9 8 7 6 5 4 3 2`. Remainder < 2 → DV 0, else DV = 11 − remainder.
- **Alphanumeric CNPJ** (IN RFB 2.229/2024; new registrations from **July 2026**):
  - the first 12 positions may be `A–Z` or `0–9`; the DVs stay numeric
  - each character's value is its ASCII code − 48 (`A`=17 … `Z`=42); the rest of the
    algorithm is unchanged
  - existing numeric CNPJs stay valid

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| CNPJ (alphanumeric) | `12.ABC.345/01DE-35` (`12ABC34501DE35`) | Published example | Worked example in the RFB *Perguntas e Respostas* (question 14), the Serpro DV paper and the RFB normative annex. The BCB Pix manual also uses it as a CNPJ Pix key. ✅ DV · ✅ not registered. **Best choice for a Brazilian party.** |
| CNPJ (alphanumeric branch) | `AA.345.678/000A-29` | Published example | RFB FAQ question 23, Ex2. ✅ DV · ✅ not registered |
| CNPJ | `AA.345.678/0003-29` | **Avoid** | RFB FAQ Ex1. ❌ DV wrong (BrasilAPI: "inválido") |
| CNPJ | `12.345.678/000A-08` | **Avoid** | RFB FAQ Ex3. ✅ DV and this branch is not registered, but root `12345678` belongs to a real (closed) taxpayer |
| CNPJ (alphanumeric, Serpro trial API) | `L9J5BYRT000101` (active), `L9J5BYRTD90R79` (active), `10Y7G69E000163` (closed) | Published example | Serpro *Consulta CNPJ* trial data, labelled "CNPJ fictícios". ✅ DV · ✅ not registered |
| CNPJ (homologação) | `99.999.999/0001-91` | Reserved | See §1.2 |
| RFB **Simulador Nacional de CNPJ** | `https://servicos.receitafederal.gov.br/servico/cnpj-alfa/simular` | Official generator | Generates up to 1,000 fictitious CNPJs per user and validates them, for "testes com dados fictícios" (RFB FAQ questions 47–51). Output is random, so check each number against the register before use. |

The first alphanumeric CNPJ issued, `00.000.000/E08G-12`, is a real Banco do Brasil
branch; see the avoid list.

**Inscrição Estadual (IE, state ICMS registration).**

- Each state has its own length and check-digit routine, published on SINTEGRA
  (`sintegra.gov.br/Cad_Estados/cad_XX.html`).
- Official worked examples:
  - SP `110.042.490.114`, rural producer `P-01100424.3/002`
  - GO `10.987.654-7`
  - RS `224/3658792`
- These are not checked against state registers (no open API), so treat them as
  **Published example, unverified**.
- For non-contributors (`indIEDest = 9`) the IE is left empty. The literal `ISENTO` is
  used for IE-exempt contributors.

### 1.4 Personal identifiers — CPF

**Rule.** 11 digits: 9 base digits and 2 mod-11 check digits (weights 10…2, then
11…2; remainder < 2 → 0). The 9th digit is the fiscal region.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| CPF, "Regular" | `404.428.201-35` (birth date 14/11/1970), `630.172.859-95` (26/12/1964), `917.086.352-03` (03/01/1943), `581.360.533-91` (20/11/1972) | Published example | Serpro *Consulta CPF* trial data, explicitly "CPF fictícios". ✅ DV for all 22 numbers in the list. **Not checkable against the CPF register** (no open lookup). |
| CPF, other statuses (Serpro list) | Suspensa `40532176871`, `47123586964` · Pendente `07691852312`, `10975384600` · Cancelada por multiplicidade `01648527949`, `47893062592` · Nula `98302514705`, `18025346790` · Cancelada de ofício `64913872591`, `52389071686` · Titular falecido `05137518743`, `08849979878` · minor `30272095079`, `14898746071`, `20803407009`, `78411139000` · partial `88373571094`, `47460609080` | Published example | ✅ DV. Useful for negative tests. |
| CPF | `123.456.789-00` | **Avoid** | BCB Pix manual example key; ❌ fails DV (correct DV would be `-09`) |

Caveat: Serpro's *numeric* "fictitious" CNPJs in the same documentation turned out to
be real registrations (§1.9). The fictitious CPFs may have the same problem, and this
cannot be checked. Prefer them only where a CPF is unavoidable, such as a consumer
`AccountingCustomerParty`.

### 1.5 Banking and Pix

Source: BCB *Manual de Padrões para Iniciação do Pix* v2.10.0, §2.5.1 (key formats) and
§2.6 (example BR Codes).

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| Pix random key (EVP) | `123e4567-e12b-12d1-a456-426655440000` | Published example | Used in all static BR Code examples |
| Pix e-mail key | `fulano_da_silva.recebedor@example.com` | Published example | RFC 2606 domain, so safe |
| Pix CNPJ key | `12ABC34501DE35` | Published example | Same as the RFB example (§1.3) |
| Pix CNPJ key | `00038166000105` | **Avoid** as party data | ✅ DV, but it is Banco Central do Brasil itself (BrasilAPI) |
| Pix phone key | `+5561912345678` | **Avoid** (unverified) | Format example; a plausible real Brasília mobile number, and no reserved range exists (§1.6) |
| Static BR Code (EMV QR) | `00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913Fulano de Tal6008BRASILIA62070503***63041D3D` | Published example | ✅ CRC16 `1D3D` recomputed. Merchant name `Fulano de Tal` ("John Doe"). |
| Dynamic BR Code URL | `pix.example.com/…` | Published example | RFC 2606 domain |
| Bank account | Bank code (COMPE, 3 digits, e.g. `001`) + agência + conta | — | No national account checksum (bank-specific). Brazil does not use IBAN domestically. |

### 1.6 Telephone

**No Anatel range reserved for fiction or tests was found** (Portuguese and English
searches; Anatel numbering regulations not read in full).

Format: `+55` + 2-digit DDD + 8-digit fixed or 9-digit mobile (mobile starts with `9`).
Options:

- leave telephone out
- use a clearly invalid value in prose only
- accept the residual risk of a format-valid number

### 1.7 Postal addresses (CEP)

| Item | Value | Status | Notes |
|---|---|---|---|
| CEP format | `NNNNN-NNN`, alone on the last line; never write "CEP" before it, never use dots | — | Correios *Guia Técnico de Endereçamento* v1.4 (2021), UPU sheet |
| Correios official example | `João da Silva` / `Avenida Paulista 123, Loja B` / `Paraíso` / `01311-000 São Paulo/SP` | Published example | Fictitious person, real street and CEP. The Correios lookup gives bairro *Bela Vista* for `01311-000` (odd numbers up to 609), so the official example's bairro is inconsistent. |
| UPU examples | `Marina Costa e Silva` / `Rua Afonso Camargo, 805` / `Santana` / `GUARAPUAVA – PR` / `85070-200`; PO box `Caixa Postal 443`, `85100-970`; Brasília `SBN – Quadra 13 – Bloco B`, `70002-900` | Published example | `70002-900` is the Correios head office (real) |
| Unused CEPs | `00000-000` … `00999-999` | Derived | ✅ `00000000` and `00999999` rejected as "CEP INVÁLIDO" by the Correios service (via BrasilAPI). The lowest assigned range starts at `01000-000` (São Paulo). |
| CEP suffix conventions | `-900`…`-959` large users, `-960`… PO boxes / community boxes (e.g. `-970`, `-994`) | Published example | From the UPU examples; the full Correios suffix table was not read |
| Correios barcode check digit | Digit sum of the CEP, up to the next multiple of 10 (example `71010050` → `6`) | — | Correios guide, item 5 |

Recommendation: use the official pattern of a fictitious person or company at a real
CEP and a real street, as in the Correios and UPU examples. Alternatively, use
`00xxx-xxx` where failing a lookup is acceptable.

### 1.8 Other identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| Vehicle plate (Mercosur, `LLLNLNN`) | `ABC1C34` (converted from old `ABC1234`) | Published example | CONTRAN Res. 780/2019, Anexo II (revoked and replaced by Res. 969/2022, same format). Combinations are random and assigned by DENATRAN/SENATRAN, so the example may exist on a real vehicle. |
| Product classification | NCM (8 digits, Mercosur) | — | Real codes; not identifiers of parties |
| E-mail / web | `example.com`, `*.test` (RFC 2606/6761) | Reserved | `exemplo.com.br` registration status could not be checked (registro.br RDAP returned 403) |

### 1.9 Brazil avoid list

| Value | Seen as | Why |
|---|---|---|
| `11.222.333/0001-81` | Ubiquitous "valid example CNPJ" in validator docs | Real: a school fund in São Sebastião do Caí/RS, active ✅ |
| `12.345.678/0001-95` | RFB FAQ prose example | Real taxpayer (closed) ✅ |
| `00.000.000/0001-91`, `00.000.000/E08G-12` | "First" CNPJs | Banco do Brasil ✅ |
| `00.038.166/0001-05` | BCB Pix manual | Banco Central do Brasil ✅ |
| `34238864000168`, `54447820000155`, `46768703000165`, `31151791000184`, `34428654000132`, `06115832000130`, `52293473000128`, `07781066000105`, `60367129000164` | Serpro trial "CNPJ fictícios" | All ✅ registered to real businesses (several are MEIs named after real people). Only `78078291000128` was not found. |
| `AA.345.678/0003-29` | RFB FAQ | ❌ DV wrong |
| `123.456.789-00` | BCB Pix manual | ❌ DV wrong |
| `+5561912345678` | BCB Pix manual | Possibly a real number |

---

## 2. Argentina

### 2.1 E-invoicing landscape (not UBL)

- Electronic invoices are authorised online by **ARCA** (formerly AFIP) through SOAP web
  services: **WSFEv1** (domestic), WSFEXv1 (export), WSMTXCA, and FCE MiPyMEs
  (factura de crédito electrónica, which requires a CBU).
- The invoice itself is a WS request/response, not a document XML standard. There is
  no UBL and no Peppol.
- **Homologación** (test):
  - WSFEv1 at `https://wswhomo.afip.gov.ar/wsfev1/service.asmx`; production at
    `https://servicios1.afip.gov.ar/wsfev1/service.asmx`
  - WSAA at `https://wsaahomo.afip.gov.ar/ws/services/LoginCms`
- ARCA publishes **no shared test CUIT**. Developers use their own CUIT with a test
  certificate from *WSASS – Autogestión Certificados Homologación*.

### 2.2 Company and personal identifiers — CUIT / CUIL / DNI

**Rule.** 11 digits: 2-digit type prefix, 8-digit DNI or serial, and a check digit.

- Prefixes: `20`/`23`/`24`/`27` = persons (CUIL/CUIT); `30`/`33`/`34` = legal entities.
- Check digit: weights `5 4 3 2 7 6 5 4 3 2`; DV = 11 − (sum mod 11); 11 → 0. A result
  of 10 is not allowed, so the prefix switches to 23/33, which is why `23`/`33`
  numbers exist.
- The algorithm is widely documented, but **no ARCA primary source for it was
  found**.

Source of the values below: ARCA *Manual para el desarrollador – Facturación
Electrónica RG 4291*, Proyecto FE v4.0 (revision of 15 January 2025).

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| Receiver CUIT in example requests (`DocTipo 80`) | `20111111112` | Published example | ✅ DV. Prefix `20` + DNI `11111111`: a person-type number that **could belong to a real person**; not checkable (no open padrón API). |
| Receiver CUIT in examples | `30000000007` | Published example | ✅ DV. Legal-entity prefix with serial `00000000`; very unlikely to be assigned (not verifiable). **Best Argentine party ID.** |
| "No Categorizado" receiver | `23000000000` | Reserved (has a meaning) | ✅ DV. When `DocTipo 80` + `DocNro 23000000000`, ARCA skips the padrón check (errors 10015, 1425 etc.). It means "not categorised", so it is not a party identifier. |
| Consumidor final | `DocTipo 99`, `DocNro 0` | Reserved (has a meaning) | Anonymous final consumer on B/C invoices below the RG 4444 threshold (errors 1415–1419) |
| Issuer CUIT in examples | `23000000004` | **Avoid** | ❌ DV (correct would be `23000000000`) |
| Other example CUITs | `33333333333`, `33000000007` | **Avoid** | ❌ DV wrong |
| `Auth/Cuit` in examples | `33693450239` | **Avoid** as party | ✅ DV; this is AFIP/ARCA's own CUIT (also in the WSAA homologation certificate DN `SERIALNUMBER=CUIT 33693450239`) |
| DNI | 7–8 digits, no check digit | — | **No official test DNI found.** RENAPER publishes none. |

### 2.3 Banking — CBU / CVU

**Rule** (BCRA Comunicación "A" 2622, 14/11/1997; now in the *Sistema Nacional de
Pagos* consolidated text). 22 digits in two blocks, each check digit computed "con la
clave 10 con el ponderador 9713":

- **Block 1:** entity (3) + branch (4) + DV.
- **Block 2:** account (13) + DV.
- **CVU** (Com. "A" 6510, payment-service providers): same structure, prefix `000` +
  4-digit PSP code.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| CBU | `2850590940090418135201` | **Avoid** | Wikipedia (es) / blog example; ✅ both DVs. Entity `285` is Banco Macro (real bank, possibly a real account) and the example is not from the BCRA. |
| CBU | `0110599520000012345676` | **Avoid** | Third-party "example"; ❌ block-2 DV (should end `…8`); entity `011` is Banco Nación |
| BCRA example CBU | — | Not found | Com. "A" 2622 gives the rule only, with no example number |
| Alias CBU | 6–20 characters, letters, digits, `.` and `-` | — | Free text chosen by the account holder |

Argentina does not use IBAN; there is no fictitious bank code that would also pass a
bank-code lookup. Recommendation: **Derived** CBU with a real entity code, an obviously
synthetic account part and correct DVs, documented as fictitious.

### 2.4 Telephone

**No ENACOM range reserved for fiction or tests was found.** The national numbering
plan is Res. SC 46/97 (PFNN): 10-digit national numbers, and first digits 4, 5, 7, 9
are reserved for future use, not for fiction. The full PFNN Tabla 5.1 was not read.
Format: `+54` + area code + subscriber; mobiles are `+54 9` + area + number.

### 2.5 Postal addresses (CPA)

| Item | Value | Status | Notes |
|---|---|---|---|
| CPA format | `A9999AAA`: province letter (ISO 3166-2:AR letter, `C` = CABA, `X` = Córdoba, `B` = Buenos Aires province) + old 4-digit postcode + 3-letter block-face code, left of the locality | — | UPU sheet (07/2002), Correo Argentino |
| Line rules | ≤ 40 characters per line; avoid `.`, `-`, accents; `CALLE` only when the street name is a number/letter; `No` before the house number when the street name ends in a number (`17 DE OCTUBRE DE 1945 No 1340`) | — | UPU sheet |
| UPU examples | `SIGNUM SRL` / `JUAN LOPEZ` / `SAN MARTIN 230` / `PISO 4 DPTO. A` / `Y5900FNF VILLA MARIA`; `SR. JUAN LOPEZ` / `CASILLA DE CORREOS 432` / `CORREO CENTRAL` / `C1000WAE CAPITAL FEDERAL`; `X5187YAB SAN CLEMENTE` | Published example | Villa María is in Córdoba, so the CPA should start with **`X`**; `Y` is Jujuy. The UPU example is internally inconsistent. Do not copy it unchanged. |

Unused-range analysis: not done, because Correo Argentino has no open CPA file.

### 2.6 Other identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| Vehicle plate (Mercosur, since 2016) | Cars `LL NNN LL` (e.g. `AA 000 AA` pattern); motorcycles `L NNN LLL` | Derived | Format only; no official example verified |
| E-mail / web | `example.com`, `*.test` | Reserved | `ejemplo.com.ar` resolves (registered) → **Avoid** |

### 2.7 Argentina avoid list

| Value | Seen as | Why |
|---|---|---|
| `33693450239` | ARCA examples, WSAA DN | ARCA's own CUIT |
| `23000000004`, `33333333333`, `33000000007` | ARCA manual examples | ❌ DV wrong |
| `20267565393` | PyAfipWs homologation examples | ✅ DV; a developer's own CUIT (personal) |
| `2850590940090418135201`, `0110599520000012345676` | "Example CBU" on Wikipedia / blogs | Real bank codes; the second fails its DV |
| `Y5900FNF VILLA MARIA` | UPU example | Wrong province letter |

---

## 3. Chile

### 3.1 E-invoicing landscape (not UBL)

- **DTE** (Documento Tributario Electrónico): SII national XML, namespace
  `http://www.sii.cl/SiiDte`, envelope `EnvioDTE_v10.xsd`.
- Document types: factura 33/34, boleta 39/41, export 110/111/112, guía de despacho
  52, notas 56/61.
- Format specifications:
  - *Formato Documentos Tributarios Electrónicos* v2.5 (2026-02)
  - *Formato Boletas Electrónicas* v4.2 (2025-09-08)
- No UBL and no Peppol.
- **Certificación** environment: `maullin.sii.cl` (e.g. `/DTEWS/CrSeed.jws`,
  `/cgi_dte/UPL/DTEUpload`); production: `palena.sii.cl`.
- Certification uses an SII-issued **Set de Pruebas**:
  - the first reference line must be `TpoDocRef = SET` and `RazonRef = CASO nnnn-n`
  - `NroResol = 0` is fixed in certification
- The SII *Instrucciones* tell the developer to use "un Rut receptor de un **cliente
  existente**", so the official test process uses real receiver RUTs. Do not copy
  them.

### 3.2 Company and personal identifiers — RUT / RUN

**Rule.** Body (up to 8 digits) + `-` + check digit.

- Check digit: mod 11 with weights 2…7 repeating from the right; 11 → `0`, 10 → `K`.
- Written `12.345.678-5` or `12345678-5` in DTE XML (hyphen and DV, no dots).
- Natural persons (RUN) currently occupy roughly ≤ 30 million; legal entities
  ≈ 50–99 million, e.g. `76…`/`77…` for recent companies. Range boundaries are
  approximate and not officially verified.

| Element | Value | Status | Checks / Notes |
|---|---|---|---|
| Generic boleta customer `RUTRecep` | `66.666.666-6` | Reserved (has a meaning) | ✅ DV. *Formato Boletas* v4.2: "se debe utilizar el RUT genérico 66.666.666-6" when the buyer has no RUT/internal code; not printed. For a consumer, not a business party. |
| Foreign receiver without RUT | `55.555.555-5` | Reserved (has a meaning) | ✅ DV. *Formato DTE* v2.5, field 50: "En doctos. Exportac. 55.555.555-5"; also for the tourist invoice (`TipoFactEsp = 1`) and in SII Res. Ex. 66/2022 (foreign ID then goes in `CdgIntRecep` + `Nacionalidad`). **Correct value for a non-Chilean buyer in a Chilean export DTE.** |
| `RutReceptor` in the `EnvioDTE` carátula | `60803000-K` | Reserved (has a meaning) | ✅ DV. "corresponde al RUT del SII" (SII *Instrucciones set de pruebas*). The SII itself, so **not** a party. |
| Issuer in the SII certification manual | `97975000-5`, name `RUT DE PRUEBA` | Published example | ✅ DV. *Manual para empresas usuarias – ambiente de certificación* (2009) §5.1, "datos de una Empresa ficticia". **Best Chilean party ID**, but not checkable against the register. That manual also uses SII's own address `Teatinos 120, Piso 4` (real). |
| Authorised sender (person) | `7880442-4` | Published example | ✅ DV; RUN-range number, so possibly a real person → use with caution |
| Receiver in the same manual | `8414240-9`, `JORGE GONZALEZ LTDA`, `SAN DIEGO 2222` | **Avoid** (unverified) | ✅ DV; RUN-range number with a person-like company name |
| SII *Instructivo técnico* (2021-10-28) examples | `11.111.111-1` "Ejemplo S.A.", `22.222.222-2`, `12.345.678-5` "Comprador S.A.", `77777777-7` | Published example → **Avoid** | ✅ all DVs. The first three fall in the natural-person RUN range and `77777777-7` in the active company range; all are likely assigned to real taxpayers (not checkable). |

### 3.3 Banking

| Item | Notes |
|---|---|
| Account numbers | No national check digit or IBAN. A transfer needs bank code (CMF list, e.g. `001` Banco de Chile, `012` BancoEstado) + account type + account number + holder RUT. |
| Official example account | Not found |

### 3.4 Telephone

**No Subtel range reserved for fiction or tests was found.** The numbering plan is
DS 747/1999 (*Plan Técnico Fundamental de Numeración*) and its amendments.
Format: `+56` + 9 digits; mobiles are `+56 9 XXXX XXXX`; Santiago landlines are
`+56 2 2XXX XXXX`.

### 3.5 Postal addresses (código postal)

| Item | Value | Status | Notes |
|---|---|---|---|
| Format | 7 digits (3-digit sector, usually a commune, + 4-digit block-face serial), left of the commune name; commune-wide codes end in `0000` | — | UPU sheet (03/2017) |
| UPU / Correos Chile examples | `Juan Pérez` / `Moneda 1152` / `8340648 SANTIAGO`; `Ester Avila` / `Avenida Palena 1084, Depto. 505, Piso 5` / `9180794 ESTACION CENTRAL`; `Pedro López` / `Empresa Automotriz` / `Avenida Arturo Prat 567` / `3930000 BULNES`; rural `Panamericana Norte S/N Km. 15` / `8700000 QUILICURA` | Published example | Fictitious people at real streets and communes. `El Juncal 050`, `8720019 QUILICURA` is Correos Chile's own address. |
| Line structure | Name / street + number + "resto de dirección" / postcode + COMUNA / REGION / CHILE | — | UPU sheet |

In DTE XML the address is free text (`DirRecep`, `CmnaRecep`, `CiudadRecep`) with no
postcode field.

### 3.6 Other identifiers

| Element | Value | Status | Notes |
|---|---|---|---|
| Vehicle plate (PPU) | `BB·BB·10` pattern: 4 letters from `BCDFGHJKLPRSTVWXYZ` + 2 digits (from 2007); motorcycles `BBB·10` | Derived | Not Mercosur. The plate check digit appears only on the registration document. A 5-letter + 1-digit scheme is expected once combinations run out (2026+; unverified). |
| E-mail / web | `example.com`, `*.test` | Reserved | `ejemplo.cl` registration could not be checked (NIC Chile RDAP unreachable) |

### 3.7 Chile avoid list

| Value | Seen as | Why |
|---|---|---|
| `60803000-K` | Carátula examples | SII's own RUT |
| `11.111.111-1`, `22.222.222-2`, `12.345.678-5`, `77777777-7` | SII *Instructivo* examples | Likely assigned to real persons/companies |
| `8414240-9` `JORGE GONZALEZ LTDA` | SII certification manual | Person-range RUN, person-like name |
| `76543210-K` | Library examples (dte-sii) | ❌ DV wrong (should be `-3`) |
| Real customer RUTs used in a certification set | SII instructions require existing customers | Real data |
| `Teatinos 120`, `El Juncal 050` | Official example addresses | SII and Correos Chile head offices |

---

## 4. Recommendations for the party set

| Country | Business party ID | Consumer | Address | Phone |
|---|---|---|---|---|
| Brazil | Alphanumeric CNPJ `12ABC34501DE35` (or `AA345678000A29`, the Serpro alphanumerics) | Serpro fictitious CPF (e.g. `40442820135`), with the §1.4 caveat | Fictitious name at a real CEP/street (Correios pattern) or `00xxx-xxx` | Omit |
| Argentina | CUIT `30000000007` | `DocTipo 99` / `DocNro 0` (consumidor final) | Fictitious name + valid CPA with consistent province letter | Omit |
| Chile | RUT `97975000-5` ("RUT DE PRUEBA"); foreign buyer `55555555-5` | `66666666-6` | Fictitious name at real street/commune + code | Omit |

In UBL, use `cbc:CompanyID` with `schemeName` naming the national scheme (`CNPJ`,
`CUIT`, `RUT`). No ISO 6523 ICD for these three schemes was confirmed during this
research.

---

## 5. Sources

**Brazil**
- Receita Federal: [CNPJ alfanumérico – Perguntas e Respostas](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/cnpj/cnpj-alfanumerico.pdf) · [Projeto CNPJ alfanumérico](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/cnpj-alfanumerico) · [Simulador Nacional de CNPJ](https://servicos.receitafederal.gov.br/servico/cnpj-alfa/simular) · [Anexo normativo (cálculo DV)](https://normas.receita.fazenda.gov.br/sijut2consulta/anexoOutros.action?idArquivoBinario=76204)
- Serpro: [Cálculo dos DV do CNPJ alfanumérico](https://www.serpro.gov.br/menu/noticias/videos/calculodvcnpjalfanaumerico.pdf) · [API Consulta CPF – guia rápido / dados para testes](http://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf/pt/quick_start/) · [API Consulta CNPJ – guia rápido](http://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cnpj/pt/quick_start/) · [API Cartório Data – guia rápido](http://apicenter.estaleiro.serpro.gov.br/documentacao/cartorio-data/pt/quick_start/)
- NF-e: [NT 2011/002](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Ll7tbBdZPyE%3D) (not downloadable during research; quoted via secondary sources) · [NT 2011/004](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Z1ivX0aahCM%3D) · [SEFAZ-PE Guia de Procedimentos NF-e](https://www.sefaz.pe.gov.br/Servicos/nota-fiscal-eletronica/Guias%20e%20Procedimentos/NF-e%20%20Guia%20De%20Procedimentos%20(05-08-2015).pdf) · [MOC 7.0 Anexo I (Confaz)](https://www.confaz.fazenda.gov.br/legislacao/arquivo-manuais/moc7-anexo-i-leiaute-e-rv.pdf) · [Esquemas XML (homologação portal)](https://hom.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=BMPFMBoln3w%3D)
- Secondary (rejection codes): [FlexDocs 597](https://flexdocs.net/suporte/knowledgebase.php?article=97) · [TecnoSpeed 373](https://atendimento.tecnospeed.com.br/hc/pt-br/articles/360010301653) · [Oobj 649 (CT-e)](https://oobj.com.br/bc/rejeicao-649-como-resolver/)
- NFS-e Nacional: [Documentação técnica](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica)
- Banco Central do Brasil: [Manual de Padrões para Iniciação do Pix v2.10.0](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf) · [Manual do BR Code](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf)
- SINTEGRA: [Roteiro IE São Paulo](http://www.sintegra.gov.br/Cad_Estados/cad_SP.html) · [Goiás](https://www.sintegra.gov.br/Cad_Estados/cad_GO.html) · [Rio de Janeiro](http://www.sintegra.gov.br/Cad_Estados/cad_RJ.html)
- Correios: [Guia Técnico de Endereçamento de Correspondências v1.4](https://www.correios.com.br/enviar/correspondencia/arquivos/nacional/guia-tecnico-de-enderecamento-de-correspondencias.pdf) · UPU: [Postal addressing — Brazil](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/braEn.pdf)
- CONTRAN: [Resolução 780/2019 (LegisWeb)](https://www.legisweb.com.br/legislacao/?id=424984)
- Lookups: [BrasilAPI CNPJ/CEP](https://brasilapi.com.br/docs)

**Argentina**
- ARCA: [Manual para el desarrollador FE RG 4291 v4.0](https://www.afip.gov.ar/fe/documentos/manual-desarrollador-ARCA-COMPG-v4-0.pdf) · [Homologación externa – Web Services](https://www.afip.gob.ar/ws/documentacion/homologacion-externa.asp) · [Webservices de factura electrónica](https://www.afip.gob.ar/ws/documentacion/ws-factura-electronica.asp)
- BCRA: [Comunicación "A" 2622 (CBU)](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/a2622.pdf) · [Texto ordenado Sistema Nacional de Pagos – Servicios de pago](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-spd.pdf) · [Comunicación "A" 7533](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/a7533.pdf)
- ENACOM: [Plan Fundamental de Numeración Nacional (Res. 46/97)](https://www.enacom.gob.ar/multimedia/normativas/1997/Resolucion%2046_97.pdf) · [Numeración](https://www.enacom.gob.ar/numeracion_p136)
- UPU: [Postal addressing — Argentina](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/argEn.pdf)
- Secondary: [Clave Bancaria Uniforme (Wikipedia es)](https://es.wikipedia.org/wiki/Clave_Bancaria_Uniforme) · [PyAfipWs WSFEv1](https://www.sistemasagiles.com.ar/trac/wiki/ProyectoWSFEv1)

**Chile**
- SII: [Formato DTE v2.5 (2026-02)](https://www.sii.cl/factura_electronica/factura_mercado/formato_dte_202602.pdf) · [Formato Boletas Electrónicas v4.2](https://www.sii.cl/factura_electronica/factura_mercado/formato_boleta_electronica.pdf) · [Instrucciones set de pruebas](https://www.sii.cl/servicios_online/docs/inst_set_pruebas.pdf) · [Manual ambiente de certificación](https://www.sii.cl/servicios_online/docs/manual_certificacion.pdf) · [Instructivo técnico de emisión (2021)](https://www.sii.cl/factura_electronica/factura_mercado/instructivo_emision.pdf) · [Res. Ex. SII 66/2022](https://www.sii.cl/normativa_legislacion/resoluciones/2022/reso66.pdf) · [Sistema propio o de mercado – certificación](https://www.sii.cl/factura_electronica/factura_mercado/menu_certificacion.html)
- Subtel: [Decreto 747 Plan Técnico Fundamental de Numeración (LeyChile)](https://www.leychile.cl/leychile/Navegar?idNorma=173931) · [Normativa técnica](https://www.subtel.gob.cl/normativa-tecnica1/)
- UPU: [Postal addressing — Chile](https://www.upu.int/UPU/media/upu/PostalEntitiesFiles/addressingUnit/chlEn.pdf)
- Secondary: [rut.ts issue #44 (SII placeholder RUTs)](https://github.com/arrowsw/rut.ts/issues/44) · [niclabs/DTE endpoints](https://github.com/niclabs/DTE/blob/master/src/cl/nic/dte/resources/Net.properties) · [Matrículas de Chile (Wikipedia es)](https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Chile)

**General**
- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- Peppol status in Latin America: [OpenPeppol, *The global shift to eInvoicing* (2025)](https://peppol.org/wp-content/uploads/2025/10/The-global-shift-to-eInvoicing.pdf) · [Tickstar, Peppol around the world](https://www.tickstar.com/peppol-einvoicing-around-the-world/)
