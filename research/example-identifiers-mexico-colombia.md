# Fictitious-but-valid example identifiers — Mexico and Colombia

**Purpose:** same as `example-identifiers-fr.md`: identifiers, addresses and contact
data that pass format/checksum validation, come from an official or authoritative
source, and cannot be confused with a real organisation, for the canonical
26 + Consumer party set (`session-decisions.md` §5.3).

**Researched:** 2026-11-05, with Spanish- and English-language queries. Checks marked ✅
were run during research:

- **Mexico:** RFC check digit and CURP check digit (own implementation of the SAT/RENAPO
  algorithms); the SAT test-certificate package was downloaded and every `.cer` file
  decoded with OpenSSL; postcodes were looked up in the SAT CFDI 4.0 catalogue
  `c_CodigoPostal` (95,749 codes, catalogue dated 2026-10-29) and in the Correos de
  México (SEPOMEX) national catalogue (31,869 postcodes, file dated 2026-11-03); CLABE
  check digit.
- **Colombia:** NIT check digit (DV, modulus 11); lookup in the RUES chamber-of-commerce
  register via the open-data API on datos.gov.co (dataset `c82u-588k`); postcodes looked
  up in the DIAN table (3,681 codes, from 4-72 / codigopostal.gov.co); CUFE (SHA-384)
  example recomputed.

Status legend (same as the France file): **Reserved** · **Published example** ·
**Derived** · **Avoid**.

**Headline:**

- **Mexico is the best case so far.** The SAT publishes an official set of **30 test
  taxpayers** (15 companies, 15 individuals) with test certificates. They have invented
  names, valid RFC check digits, CURPs, and postcodes from the SAT catalogue. Most
  company postcodes have no real settlement.
- **Colombia's e-invoice is UBL 2.1** (`cbc:UBLVersionID` = `UBL 2.1`). The DIAN toolkit
  ships 44 signed example XMLs. They are an excellent structural reference, but **most
  party NITs in them are real companies**, including DIAN's own NIT. Only a handful of
  DIAN example NITs pass the DV check and are not in RUES.

---

# Part A — Mexico

## A1. SAT test taxpayers (CFDI 4.0 test certificates)

**Source:** SAT, *Certificados de sello digital*,
[`Certificados_de_Prueba.zip`](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Certificados_de_Prueba.zip)
(447 KB, linked from the SAT page below). It contains FIEL and CSD certificates
plus private keys for each test RFC, the password file (`12345678a` for all), an LCO
(certificate list) file, and `Caracteristicas fiscales de RFC.xlsx` (tax regime,
economic activity and obligations for each RFC). The certificates were issued in
January–May 2023 and **expire in January–May 2027**. CSD serial numbers start
`300010000005000…`, e.g. EKU9003173C9 = `30001000000500003416`. The SAT test
environment and PAC sandboxes (CFDI stamping providers) only accept these RFCs as
issuers.

These are the strongest "Reserved" values in this research: the SAT itself created them
as test taxpayers. They pass offline validation. In production they fail, because they
are not in the SAT's list of registered RFCs (LRFC).

### A1.1 Personas morales (companies) — 15 RFCs

Name as in the certificate subject (CN). In CFDI 4.0, `Nombre` must be sent **without**
the company-type suffix (e.g. `ESCUELA KEMPER URGATE`). Postcode comes from PAC
documentation (Facturama), not from the SAT package; see A1.3.

| RFC | Name (certificate) | Regime (SAT xlsx) | Postcode | Checks |
|---|---|---|---|---|
| `EKU9003173C9` | ESCUELA KEMPER URGATE SA DE CV | 601 General de Ley PM | `42501` | ✅ DV · ✅ CP in SAT, not in SEPOMEX |
| `EWE1709045U0` | ESCUELA WILSON ESQUIVEL S DE CV | 603 Fines no lucrativos | — | ✅ DV |
| `H&E951128469` | HERRERIA & ELECTRICOS S DE CV | 601 | `06002` | ✅ DV · ✅ CP in SAT only |
| `HAÑ930228SM9` | HERMANOS ANZURES ÑARVAEZ SA | 603 | — | ✅ DV |
| `IIA040805DZ4` | INDISTRIA ILUMINADORA DE ALMACENES SA DE CV | 626 RESICO | `62661` | ✅ DV · ✅ CP in SAT only |
| `IVD920810GU2` | INNOVACION VALOR Y DESARROLLO SA | 601 | `63901` | ✅ DV · ✅ CP in SAT only |
| `IXS7607092R5` | INTERNACIONAL XIMBO Y SABORES SA DE CV | 603 | `23004` | ✅ DV · ✅ CP in SAT only |
| `JES900109Q90` | JIMENEZ ESTRADA SALAS A A | 622 Agrícolas… | `37161` | ✅ DV · ✅ CP in SAT only |
| `KIJ0906199R1` | KERNEL INDUSTIA JUGUETERA SA DE CV | 622 | `28971` | ✅ DV · ✅ CP in SAT only |
| `L&O950913MSA` | LUCES & OBRAS SA DE CV | 626 | `60922` | ✅ DV (`A`) · ✅ CP in SAT only |
| `OÑO120726RX3` | ORGANICOS ÑAVEZ OSORIO S.A DE C.V SA DE CV | 601 | `40501` | ✅ DV · ✅ CP in SAT only |
| `S&S051221SE2` | S & SOFTWARE SA DE CV | 624 Coordinados | — | ✅ DV |
| `URE180429TM6` | UNIVERSIDAD ROBOTICA ESPAÑOLA SA DE CV | 601 | `86991` | ✅ DV · ✅ CP in SAT only |
| `XIA190128J61` | XENON INDUSTRIAL ARTICLES S DE CV | 622 | `76343` | ✅ DV · ✅ CP in SAT only |
| `ZUÑ920208KL4` | ZAPATERIA URTADO ÑERI SA DE CV | 626 | `34541` | ✅ DV · ✅ CP in SAT only |

The company certificates name a legal representative RFC/CURP `VADA800927DJ3` /
`VADA800927HSRSRL05` (✅ both check digits). `ZUÑ920208KL4` names `KAHO641101B39`
instead. These are useful as an example **contact person**.

The `&` and `Ñ` RFCs are deliberate edge cases: XML-escape `&` as `&amp;`, and keep
the files in UTF-8. `INDISTRIA` and `INDUSTIA` are typos in the SAT originals. Copy
them exactly, because the test environment matches the name to the RFC.

**Best picks for UBL samples:** `EKU9003173C9` (most widely used, regime 601, plain ASCII)
and `IVD920810GU2` / `URE180429TM6` (regime 601). Use `L&O950913MSA` /
`HAÑ930228SM9` only to show escaping and non-ASCII characters on purpose.

### A1.2 Personas físicas (individuals) — 15 RFCs with CURP

The CURP is taken from the certificate `serialNumber` attribute.

| RFC | Name | CURP (certificate) | CURP DV | Regime | Postcode |
|---|---|---|---|---|---|
| `CACX7605101P8` | XOCHILT CASAS CHAVEZ | `CACX760510MGTSHC04` | ✅ | (not in xlsx) | `36257` |
| `CAÑF770131PA3` | FERNANDO CASTILLO ÑABARRO | `CANF770131HBCSBR08` | ❌ | 616 Sin obligaciones | — |
| `FUNK671228PH6` | KARLA FUENTE NOLASCO | `FUNK671228MCLNLR05` | ✅ | 621 / 625 | `01160` |
| `IAÑL750210963` | LUIS IAN ÑUZCO | `IANL750210HSRNZS09` | ❌ | 608 | `82525` |
| `JUFA7608212V6` | ADRIANA JUAREZ FERNANDEZ | `JUFA760821MDGRRD04` | ✅ | 614 Intereses | `01160` |
| `KAHO641101B39` | OSCAR KALA HAAK | `KAHO641101HNTLKS06` | ✅ | 626 RESICO | `76074` |
| `KICR630120NX3` | RODRIGO KITIA CASTRO | `KICR630120HGTTSD05` | ✅ | 626 | `36246` |
| `LIÑI920228KS8` | IRIS LIANEZ ÑAKI | `LINI920228MOCNKR04` | ❌ | 605 Sueldos | — |
| `MISC491214B86` | CECILIA MIRANDA SANCHEZ | `MISC491214MCCRNC01` | ✅ | 612 | `01010` |
| `RAQÑ7701212M3` | ÑEVES RAMIREZ QUEZADA | `RAQN770121HDFMZV08` | ❌ | 605 | `78905` |
| `WATM640917J45` | MARIA WATEMBER TORRES | `WATM640917MHGTRR01` | ✅ | 612 | `43543` |
| `WERX631016S30` | XAIME WEIR ROJO | `WERX631016HJCRJM08` | ✅ | 625 Plataformas | `01279` |
| `XAMA620210DQ5` | ALBA XKARAJAM MENDEZ | `XAMA620210MSLKNL04` | ✅ | 612 / 606 | `01219` |
| `XIQB891116QE4` | BERENICE XIMO QUEZADA | `XIQB891116MGRMZR05` | ✅ | (not in xlsx) | `40968` |
| `XOJI740919U48` | INGRID XODAR JIMENEZ | `XOJI740919MQTDMN02` | ✅ | 612 / 605 | `76028` |

✅ All 15 RFC check digits are correct. The 4 CURPs that fail their check digit all
belong to holders with `Ñ` in the name. Our check uses the RENAPO character set
(`Ñ` between N and O); RENAPO's exact rule for Ñ was not verified.

Most individuals' postcodes are **real settlements** in SEPOMEX: `01160`, `01010`,
`01219`, `01279` are colonias of Álvaro Obregón, Ciudad de México; `76028` is Col.
Universidad, Querétaro. `82525` (Sinaloa) is in the SAT catalogue only.

The FIEL certificates carry emails `pruebas.sat@pruebas.gob.mx`, `pruebas@pruebas.gob.mx`
and `prueba@prueba.gob.mx`. ✅ `pruebas.gob.mx` does not exist in DNS (NXDOMAIN), but
✅ `prueba.gob.mx` **is a registered domain**. Do not use either: they are government
second-level names.

Best pick for the **Consumer** party: `XOJI740919U48` / INGRID XODAR JIMENEZ (CURP
✅, postcode `76028`), or `KAHO641101B39` (also used as a legal representative in the
SAT set).

### A1.3 Postcodes of the test taxpayers

The SAT package does **not** contain postcodes. They are distributed by PACs: Facturama
lists them for 25 of the 30 RFCs; Sovos/Reachcore gives `26015` for EKU9003173C9
(older value). In the test environment, PACs check that `DomicilioFiscalReceptor` and
`LugarExpedicion` match the test taxpayer's data. Treat the postcodes as **Published
example (secondary source)**.

✅ Every postcode listed exists in the SAT `c_CodigoPostal` catalogue, so CFDI validation
accepts it. Of the 12 company postcodes, **none** exists in the SEPOMEX catalogue. They
are SAT-only codes, with a state but no municipality or settlement, so they cannot be
confused with a real address.

---

## A2. Generic RFCs (real meaning — not test values)

Defined in the SAT *Anexo 20 — Guía de llenado de los CFDI* (CFDI 4.0, PDF dated
2026-01-16) and the *Guía de llenado del CFDI global*:

| Value | Meaning | Mandatory companions | Checks |
|---|---|---|---|
| `XAXX010101000` | Receiver = *público en general* (anonymous domestic buyer; also used in the global CFDI that summarises retail sales) | `Nombre` = `PUBLICO EN GENERAL`; `DomicilioFiscalReceptor` = issuer's `LugarExpedicion`; `RegimenFiscalReceptor` = `616`; `UsoCFDI` = `S01` | ❌ DV does not compute (fixed value; validators special-case it) |
| `XEXX010101000` | Receiver = foreign resident without Mexican RFC | `RegimenFiscalReceptor` = `616`, `UsoCFDI` = `S01`, `ResidenciaFiscal` + `NumRegIdTrib` | ✅ DV happens to compute |

Use them only in their real meaning, e.g. a consumer-sale invoice to an anonymous buyer
(`XAXX010101000`) or an export invoice (`XEXX010101000`). Never use them as a party's
own tax ID.

## A3. Example values in SAT's own guides

The Anexo 20 guide uses invented companies, but almost all of their RFCs **fail the
check digit**:

| RFC | Name in guide | DV | Status |
|---|---|---|---|
| `LIN820625PU5` | La Linterna S.A. de C.V. | ❌ | Published example, invalid |
| `NUF150930AAA` | Nueva Factura, S.A. de C.V. | ❌ | Published example, invalid |
| `LOAV890607PY7` | VICTORIOSS LOPEZ AVILA (CP 14600) | ❌ | Published example, invalid |
| `MKIZ910508JUM` | MARKUZ KURI (CP 33147) | ❌ | Published example, invalid |
| `CABL840215RF4`, `FIMA420127R44` | (individual, field examples) | ❌ | Published example, invalid |
| `ENT010101000` | EENNTT (CP 75450) | ❌ | Published example, invalid |
| `FME170920PW1`, `FJP831022PW1` | FIDEICOMISO MÉXICO TE NECESITA / FUNDACIÓN DAMNIFICADOS 0917 | ❌ | Published example, invalid |
| `PAL7202161U0`, `COR391215F4A` | (company, field examples) | ✅ | **Avoid**: valid DV, ownership not checked (no open RFC lookup) |

Other examples in the guide: `LugarExpedicion="01000"` (✅ real: San Ángel, CDMX);
global-CFDI address *Av. Estrella No. 236; Col. Miraluz C.P. 33146*. ✅ 33146 is real
(Santa Rosalía de Cuevas, Chihuahua), but **Miraluz is not a settlement at that
postcode**. `NumRegIdTrib="121585958"` with `ResidenciaFiscal="USA"`.
`CuentaPredial` `15956011002`.

## A4. Derivation rules

| Identifier | Rule | Notes |
|---|---|---|
| RFC persona moral | 12 chars: 3 letters (name) + `YYMMDD` (incorporation) + 2-char homoclave + check digit | Letters may include `&` and `Ñ` |
| RFC persona física | 13 chars: 4 letters + `YYMMDD` (birth) + homoclave + check digit | |
| RFC check digit | Alphabet `0-9 A-N & O-Z (space) Ñ` → values 0–38; pad a 12-char RFC with a leading space; sum value × weight (13…2) over first 12 positions; `11 − (sum mod 11)`, 11→`0`, 10→`A` | ✅ verified on all 30 SAT test RFCs |
| CURP | 18 chars: 4 letters + `YYMMDD` + sex (`H`/`M`) + 2-letter state + 3 internal consonants + differentiator (digit before 2000, letter from 2000) + check digit | Check: alphabet `0-9 A-N Ñ O-Z`, weights 18…2, `10 − (sum mod 10)`, 10→`0` |
| Homoclave | Computed by the SAT from the full name | Not reproducible without SAT's tables; do not try to derive |

**Recommendation:** do not derive new RFCs. 30 SAT test taxpayers cover the 26 + C
party set. In production, a derived RFC with a valid check digit could belong to a
real taxpayer, and there is no open RFC lookup. The SAT's *Validación de RFC* service
needs a captcha or e.firma.

## A5. Bank identifiers (CLABE)

| Element | Value | Status | Notes |
|---|---|---|---|
| CLABE | `002180032240946700` | Published example | Banxico Circular 12/2018, annex with the official check-digit procedure; ✅ DV |
| CLABE (structure) | 3 bank + 3 plaza + 11 account + 1 DV; weights `3 7 1` repeating over 17 digits, each product mod 10, DV = `(10 − sum mod 10) mod 10` | — | Circular 12/2018 (DOF 2018-09-10) |
| CLABE | `032180000118359719` | Secondary (Wikipedia) | ✅ DV |

As with French bank codes, the bank code cannot be fictitious. `002` in the Banxico example
is Banamex. The account part is what makes it fictitious. Mexico has no IBAN. Use
the CLABE in `cac:PayeeFinancialAccount/cbc:ID`. For a test BIC, use the ISO 9362 test
convention: 8th character `0`, e.g. `XXXXMXM0`.

## A6. Postcodes and addresses

| Finding | Detail | Status |
|---|---|---|
| SEPOMEX catalogue | 31,869 postcodes (`01000`–`99998`), 159,446 settlements | ✅ downloaded |
| SAT `c_CodigoPostal` | 95,749 codes; **62,940 have no municipality**, and 61,693 of those are not in SEPOMEX | ✅ |
| Unused first two digits | `17`, `18`, `19` are in neither catalogue; `00xxx` only `00004` in SAT | Derived; fails CFDI validation |
| `00000` | Not in either catalogue | Derived |
| `99999` | In SAT (Zacatecas), not in SEPOMEX | — |
| Best option | A **SAT-only postcode** (in `c_CodigoPostal`, not in SEPOMEX), e.g. the test-taxpayer codes `42501` (Hidalgo), `63901` (Nayarit), `86991` (Tabasco) | Published example (via test taxpayers) |

A SAT-only postcode passes CFDI validation but points to no real colonia, so it is the
Mexican equivalent of a reserved postcode. A full address should still look normal:
`Calle`, `Número exterior`, `Colonia`, `Municipio`, `Estado`. No official fictitious
street name was found.

## A7. Telephone

**No reserved fictional range found** (searched IFT material in Spanish and English;
IFT was replaced as regulator by the CRT in 2025). Mexico has used uniform 10-digit
national numbers since 2019-08-03 (`+52 55 xxxx xxxx` for Mexico City). Recommendation: as for Italy, omit
the telephone number or use a reserved foreign range. IFT's public number-lookup tool
(`sns.ift.org.mx`) could be used to find an unassigned block (not done).

## A8. Customs (pedimento) and other

| Element | Value | Status | Notes |
|---|---|---|---|
| Pedimento number | `10  47  3807  8003832` (two spaces between groups) | Published example (Anexo 20 guide, `InformacionAduanera/NumeroPedimento`) | Structure: year (2) · customs office (2) · broker licence (4) · last digit of year + 6-digit sequence. ✅ `47` = Aeropuerto Internacional de la Ciudad de México, ✅ patente `3807` in `c_PatenteAduanal` and `c_NumPedimentoAduana`. **Inconsistent:** year `10` but 7th group starts with `8` |
| `ResidenciaFiscal` / `NumRegIdTrib` | `USA` / `121585958` | Published example | Anexo 20 |
| GTIN / GLN | GS1 prefix `952` | Reserved | See France file §6; Mexico's own GS1 prefix is `750` |
| Vehicle plates | — | Not researched in depth | State-issued; no reserved series found |

---

## A9. Avoid list (Mexico)

| Value | Seen as | Why |
|---|---|---|
| `XAXX010101000`, `XEXX010101000` | "Test RFC" in blogs | Real generic RFCs with legal meaning |
| `LAN7008173R5`, `TME960709LR2`, `AAA010101AAA` | CFDI 3.3-era test RFCs, common placeholders | Old test certificates revoked; `AAA010101AAA` fails DV |
| `LIN820625PU5`, `NUF150930AAA`, etc. | SAT Anexo 20 examples | Fail RFC check digit |
| `PAL7202161U0`, `COR391215F4A` | SAT Anexo 20 examples | Valid DV; ownership unknown |
| `CANF770131HBCSBR08`, `IANL750210HSRNZS09`, `LINI920228MOCNKR04`, `RAQN770121HDFMZV08` | SAT test CURPs | Fail our CURP check |
| `prueba.gob.mx`, `pruebas.gob.mx` | SAT test certificate emails | Government domains (one registered) |
| `01000`, `01160`, `76028` etc. | Example / test postcodes | Real settlements; fine for format, but not "fictitious" |
| Test-certificate validity | — | Certificates expire January–May 2027; recheck the SAT package after that |

---

# Part B — Colombia

## B1. DIAN e-invoicing toolkit (UBL 2.1)

**Source:** DIAN,
[*Caja de herramientas FE V1.9 (v2026)*](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-herramientas-FE_V19_v2026.zip)
(26 MB), linked from the
[Documentación técnica](https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica/)
page. It contains: the *Anexo Técnico de Factura Electrónica de Venta v1.9*
(Resolución 000165 of 2023-11-01, 753 pages), 37 code tables (xlsx), genericode value
lists, the DIAN Schematron, and **44 example XMLs**. The examples include Invoice,
CreditNote, DebitNote, export, foreign currency, consumer, multiple buyers, mandates,
transport, fuel, health taxes, and 5 RADIAN ApplicationResponse events. Of the 44
files, 39 carry `UBLVersionID` = `UBL 2.1` and `ProfileExecutionID` = `2` (test
environment).

### B1.1 Environment / test-set values (habilitación)

| Element | Value | Status | Notes |
|---|---|---|---|
| `cbc:ProfileExecutionID`, `cbc:UUID/@schemeID` | `1` = Producción, `2` = Pruebas | Reserved (code list 13.1.1) | Use `2` in samples |
| `sts:InvoiceAuthorization` | `18760000001` | Published example (test set) | Test-set numbering resolution, 33 example files |
| `sts:Prefix` / `From`–`To` | `SETP` `990000000`–`995000000`; `SETG` `980000000`–`985000000` | Published example | Invoice IDs e.g. `SETP990000002` |
| `sts:AuthorizationPeriod` | `2019-01-19` – `2030-01-19` | Published example | |
| `sts:SoftwareID` | `56f2ae4e-9812-4fad-9255-08fcfcd5ccb0`, `fa326ca7-c1f8-40d3-a6fc-24d7c1040607` | Published example | `ProviderID` = 800197268 (DIAN); `SoftwareSecurityCode` is derived from SoftwareID + PIN, and the PIN is not published |
| Technical key (`ClTec`) | `FC8EAC422EBA16E22FFD8C6F94B3F40A6E38162C` | Published example | Annex, *NumberRangeResponse* example (`AccountCode` 10182201486, prefix `F002`); widely used by PACs as the habilitación key (unverified that DIAN still issues it) |
| CUFE example | `NumFac 323200000129` … `ClTec 693ff6f2…1471`, `TipoAmbiente 1` → `8bb918b1…d9b4` | Published example | ✅ SHA-384 recomputed and matches |
| QR / validation URL (test) | `https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey=<CUFE>…` | Published example | `-hab` = habilitación host |
| Web service for test sets | `SendTestSetAsync` with the issuer's `TestSetId` | — | Annex §7.9; the TestSetId is issued per taxpayer in the habilitación portal, not reusable |
| Signing certificate in examples | Andes SCD test cert, CN `Usuario de Pruebas Persona Juridica`, `street=Calle Falsa No 12 34`, serialNumber `11111111`, valid 2017-09-16 to 2020-09-15 | Published example | ✅ decoded; expired; issuer `CA ANDES SCD S.A. Clase II` |

### B1.2 Parties in the DIAN examples

DV ✅/❌ = our modulus-11 computation vs the `schemeID` given. RUES = lookup in the
open-data copy of the chamber-of-commerce register (public bodies, non-registered
persons and RUT-only taxpayers are **not** in RUES, so "not in RUES" ≠ unassigned).

| Name in example | NIT / ID (type) | DV | RUES | Status |
|---|---|---|---|---|
| `FACTURADOR DE EJEMPLO` (supplier) | `800197268` (31) | ✅ 4 (some files give 9 ❌) | — | **Avoid**: this is **DIAN's own NIT** |
| `ADQUIRIENTE DE EJEMPLO` / `OPTICAS GMO COLOMBIA S A S` (customer) | `900108281` (31) | ✅ 3 | ✅ **LUXOTTICA OF COLOMBIA SAS**, active | **Avoid** |
| `Empresa de transporte` (DeliveryParty) | `981223983` (31) | ✅ 1 | ✅ not found | **Published example**: usable |
| TaxRepresentativeParty | `989123123` (31) | ✅ 4 | ✅ not found | **Published example**: usable |
| AgentParty (multiple buyers) | `995201603` (31) | ✅ 4 | ✅ not found | **Published example**: usable |
| `A & M INTERNACIONAL DE COMERCIO SAS` / `FACTURADOR DE EJEMPLO` (Medellín) | `99998888` (31) | ✅ 6 | ✅ not found | Published example; 8-digit, looks like a cédula-derived NIT |
| `CLIENTEFACTURAPRUE1` | `791098888` (31) | ✅ 4 | ✅ not found | Published example |
| `ADQUIRIENTE DE EJEMPLO 1` | `1832` (31) | ✅ 6 | 4 hits (records with no ID type) | Avoid (too short, ambiguous) |
| `Nombre del Tercero` | `2222222222222` (31) | ✅ 1 | not found | Avoid (placeholder) |
| `PRUEBAS PILOTO III-2021` | `900374636` (31) | ✅ 3 | not found | Avoid: inside the actively assigned `9003…` block; neighbours are real |
| `Empresa1`, `PRUEBAS PILOTO II-2021`, `FACTURA ELECTRONICA USUARIO PRUEBAS MIGRACION`, `Pruebas2`, `PRUEBAS2` | `900373981`, `900374635`, `900374637`, `900373991`, `900374634` | ✅ | ✅ **real companies** (e.g. DISTRIBUIDORA DE CARNICOS RM S A S; FUNDACION COLECTIVA MEDITERRANEO) | **Avoid** |
| `EmisorAutoretenedor`, `Exportacion` supplier | `900508908` | ✅ 9 | ✅ SIGNATURE SOUTH CONSULTING COLOMBIA S.A.S. | **Avoid** |
| AgentParty | `800242106` | ✅ 2 | ✅ SODIMAC COLOMBIA S A | **Avoid** |
| SoftwareProvider | `860028580` | ✅ 2 | ✅ DISPAPELES S.A.S | **Avoid** |
| RADIAN sender/receiver | `800197279`, `800197213`, `900373972`, `900373979`, `901781456`, `900508918`, `72659841521` | ❌ (all wrong DV) | some real (DENTI FORM, URBIJAMA, JO CLOUD…) | **Avoid** |
| `Prueba` supplier | `860003456` | ❌ (DV is 9, given 2) | not found | Avoid |
| `EHB` (customer, cédula) | `79907759` (13) | — | ✅ **real person** (HERNANDEZ BALANTA EDISON) with real-looking gmail address | **Avoid** |
| `PRUEBAS FACTURA`, `PRUEBAS FACTURA USUARIO6 PN` (supplier, cédula) | `2022516219`, `2024100706` (13) | ✅ | not found | Published example; Registraduría not checked |
| `Cliente Nuevo` (cédula) | `154698949` (13) | — | not found | Published example |
| Consumer | `222222222222` (13) | — | — | **Reserved** (see B2) |

**Usable DIAN-published NITs:** `981223983-1`, `989123123-4`, `995201603-4` (and,
less clean, `99998888-6`, `791098888-4`). Before use, check them in the DIAN RUT
(*Consulta estado RUT*, MUISCA, captcha; not done).

Names: the DIAN examples use `FACTURADOR DE EJEMPLO`, `ADQUIRIENTE DE EJEMPLO`
(`… 1/2/3` for multiple buyers), `Empresa de transporte`, `Nombre del Tercero`,
`Nombre Tienda`, `Establecimiento Principal`. These are generic and safe, **but not
with the NITs they come with**.

Addresses: `Av. #97 - 13`, `CARRERA 8 No 20-14/40`, `Av. Jiménez #7 - 13`,
`CR 9 A N0 99 - 07 OF 802`, `AV 123 # 45 - 67`, `Calle 000` (consumer).
`Av. Jiménez #7 - 13` and `Carrera 8 Nº 6C-38` are real DIAN/Bogotá-centre addresses.
Prefer `AV 123 # 45 - 67` or `Calle 000`. City code `11001` / department `11`
(Bogotá) dominate.

### B1.3 People and emails in the examples — Avoid

The examples contain real DIAN staff and vendor addresses: `lcanono@dian.gov.co`,
`jnavarretech@dian.gov.co`, `sd_fistrib_facturaelectronica@dian.gov.co`,
`eric.vanboxsom@gosocket.net`, `eric.valencia@ket.co`. They also contain apparently
personal gmail addresses: `jeimyperezfilop@gmail.com`, `petopower@gmail.com`,
`empresa1@gmail.com`. Placeholder domains that are **registered** (DNS checked):
`empresa.org`, `empresa.net`, `empresa.co`, `servicios.com`, `sistemas.net`,
`mail.co`, `mail.com`, `soluciones.com.co`, `prue.com`, `pruebas.com`,
`sincorreo.com` (the last two are parked for sale). `dian.go.co` (typo) does not exist.

## B2. Reserved / generic identifiers (real meaning)

| Value | Meaning | Source | Status |
|---|---|---|---|
| `222222222222` (12 × 2), type `13` | **Consumidor final** (anonymous consumer) in e-invoices; `AdditionalAccountID` = `2`, name `consumidor final`, email optional | Anexo Técnico v1.9, rules FAK61/FAK62 (and CreditNote/DebitNote equivalents) | Reserved |
| `222222222` (9 × 2), document type `43`, name `CUANTÍAS MENORES` | Aggregated small amounts in *información exógena* (annual third-party reporting) | DIAN exógena resolutions (secondary sources: gerencie.com, actualicese.com) | Reserved, not for e-invoices |
| `444444001`, `444444002`, … type `43` | Foreign third parties without tax ID, in exógena | Secondary sources; exact article of Res. 000227/2025 not found | Reserved (unverified) |
| Type `50` *NIT de otro país*, `42` foreign ID, `41` passport, `91` NUIP | Code list 13.2.1 | Toolkit | — |

The DIAN examples also use `22222222222` (11 × 2) and `2222222222` (10 × 2) for the
consumer. These are **not** the annex value. ✅ `2222222222` is in RUES (a cancelled
individual). Use `222222222222`.

## B3. Derivation rules

| Identifier | Rule | Notes |
|---|---|---|
| NIT | 9 digits for legal entities (blocks `800…`, `830…`, `860…`, `890…`, `900…`, `901…`); individuals use their cédula as NIT | |
| DV (check digit) | Weights from the right `3 7 13 17 19 23 29 37 41 43 47 53 59 67 71`; `r = sum mod 11`; DV = `r` if `r` ∈ {0,1}, else `11 − r` | ✅ verified on 20+ real/example NITs. In UBL: `cbc:CompanyID schemeName="31" schemeID="<DV>" schemeAgencyID="195"` |
| Cédula de ciudadanía | 6–10 digits, **no check digit** | Cannot be validated offline; avoid inventing |
| Derived NITs | e.g. `990000001-1`, `990000002-7`, `990000003-4`: ✅ DV, ✅ not in RUES | Derived. `999999999` is **in RUES** many times (placeholder) — avoid |

RUES has scattered records even in the `903…` range, so a whole range cannot be
declared "unused". Each value must be checked individually. Prefer the three DIAN-published
NITs in B1.2.

## B4. Postcodes and addresses

| Finding | Detail | Status |
|---|---|---|
| Structure | 6 digits: DANE department (2) + routing zone (2; `00` = department capital) + postal district (2) | Anexo §13.2.9.4; official source codigopostal.gov.co (4-72) |
| DIAN table | 3,681 codes; department prefixes in use: `05 08 11 13 15 17 18 19 20 23 25 27 41 44 47 50 52 54 63 66 68 70 73 76 81 85 86 88 91 94 95 97 99` | ✅ toolkit table 13.4.4 |
| Unused prefixes | e.g. `00`, `01`–`04`, `06`, `07`, `09`, `10`, `12` | Derived. An unknown `PostalZone` is only a **notification** (warning), not a rejection (rule FAJ73) |
| `000000` | Used in a DIAN example; not in the table | Derived (warning only) |
| Example postcodes | `110111` (Usaquén, Bogotá) ×53, `050031` (Medellín), `111821`, `110521`, `111221` | ✅ all real |
| Address format | `CR 9 A N0 99 - 07 OF 802` style: street type + number + `#` / `No` + cross-street number − house number | No official fictitious address; none found at 4-72 |

## B5. Telephone

**No reserved fictional range found** (CRC; searched in Spanish). Since 2021-09-01
(Resolución CRC 5826/2019) all numbers are 10 digits: fixed `60` + 1-digit area code
+ 7 digits (`601` Bogotá, `604` Medellín, `602` Cali); mobile `3xx xxx xxxx`. DIAN
examples use invalid short numbers (`9712311`, `6111111`, `7777777`, `0000000`).
Recommendation: omit the telephone number, or use an obvious invalid placeholder.

## B6. Bank, payroll and other

| Element | Finding | Status |
|---|---|---|
| Bank account | No IBAN and no national account check digit; formats are bank-specific | Nothing official found; not researched in depth |
| Payment means | DIAN list `MediosPago` (UN/ECE 4461 codes) | Toolkit |
| PILA (social security payroll form) | Not researched | — |
| GTIN / GLN | GS1 prefix `952` (reserved); Colombia's own GS1 prefix is `770`/`771` | See France file §6. DIAN examples use non-GTIN values (`6543542313534` under `EAN13`, `COCA3.5LTS`); do not copy |

---

## B7. Avoid list (Colombia)

| Value | Seen as | Why |
|---|---|---|
| `800197268` | `FACTURADOR DE EJEMPLO` | DIAN's own NIT |
| `900108281` | `ADQUIRIENTE DE EJEMPLO` / OPTICAS GMO | Real: Luxottica of Colombia SAS |
| `900373981`, `900374634`, `900374635`, `900374637`, `900373991`, `900508908`, `800242106`, `860028580` | DIAN example parties / software providers | Real companies (RUES) |
| `800197279`, `800197213`, `900373972`, `900373979`, `901781456`, `900508918`, `860003456` | DIAN example NITs | Wrong DV and/or real companies |
| `79907759` + `petopower@gmail.com` | DIAN consumer example | Real person |
| `2222222222`, `22222222222` | Consumer ID in DIAN examples | Not the annex value; one is in RUES |
| `999999999`, `123456789` | Placeholder NITs | Present in RUES (`123456789` = MATRICULA PRUEBA SAS and a real person) |
| `lcanono@dian.gov.co` and other DIAN/vendor emails | DIAN examples | Real people |
| `pruebas.com`, `sincorreo.com`, `empresa.co`, `mail.com` … | Placeholder email domains | Registered domains |
| `Av. Jiménez #7 - 13`, `Carrera 8 Nº 6C-38` | Example addresses | Real DIAN/central Bogotá addresses |
| `FC8EAC42…162C`, `18760000001` | Test technical key / resolution | Fine in samples **only** with `ProfileExecutionID` = `2` |

---

# Part C — Email and web domains (both countries)

| Value | Status | Notes |
|---|---|---|
| `*.test`, `*.example`, `example.com/.net/.org` | Reserved | RFC 2606 / RFC 6761 — **use these** |
| `example.com.mx`, `ejemplo.com.mx`, `ejemplo.mx`, `example.co`, `prueba.gob.mx` | **Avoid** | Registered (resolve in DNS) |
| `ejemplo.co`, `ejemplo.com.co`, `example.mx`, `prueba.mx`, `pruebas.gob.mx` | Avoid anyway | Currently NXDOMAIN, but anyone could register them; NIC México / .CO reserve nothing for examples (none found) |

Recommendation: `facturacion@<alias>.test` (e.g. `facturacion@escuela-kemper.test`), as
in the France file.

---

# Part D — Recommended picks for the 26 + C party set

| Use | Mexico | Colombia |
|---|---|---|
| Supplier | `EKU9003173C9` ESCUELA KEMPER URGATE, regime 601, CP `42501` | NIT `981223983-1` (DIAN example DeliveryParty NIT), name from party set |
| Customer | `IVD920810GU2` INNOVACION VALOR Y DESARROLLO, 601, CP `63901` | NIT `989123123-4` |
| Third party / agent / carrier | `URE180429TM6`, `XIA190128J61`, `KIJ0906199R1` … | NIT `995201603-4` |
| Consumer | `XOJI740919U48` INGRID XODAR JIMENEZ (CURP ✅) or generic `XAXX010101000` | `222222222222` (type 13, `AdditionalAccountID` 2) |
| Contact person | `VADA800927DJ3` (legal rep. in SAT certs) | — (no official fictitious person) |
| Bank | CLABE `002180032240946700` | — |
| Postcode | SAT-only code from test taxpayer | Real 4-72 code (`110111`) + invented street, or `000000` (warning only) |
| Email | `<role>@<alias>.test` | `<role>@<alias>.test` |
| Environment flags | — (CFDI is not UBL) | `ProfileExecutionID` `2`, `UUID/@schemeID` `2`, prefix `SETP`, resolution `18760000001` |

---

# Not verified

- RFC ownership: there is no open SAT RFC lookup. The SAT test RFCs are trusted as
  official test data. `PAL7202161U0` / `COR391215F4A` stay unverified.
- The SAT package does not contain the postcodes of the test taxpayers; they come from
  PAC documentation.
- The CURP check-digit rule for names with `Ñ` (4 SAT test CURPs fail our check).
- Colombian NITs against the DIAN RUT (MUISCA *Consulta estado RUT* needs a captcha);
  RUES only covers chamber-of-commerce registrations.
- Whether DIAN still issues test key `FC8EAC42…` / resolution `18760000001` to new
  test sets (TestSetIds are per taxpayer).
- The exact article of DIAN Res. 000227/2025 for `444444xxx`.
- Telephone: no reserved ranges found in either country. Unassigned blocks were not
  looked up.
- Vehicle plates, PILA, Colombian bank-account conventions: not researched in depth.

---

# Sources

**Mexico**
- SAT: [Certificados de sello digital (test certificates page)](http://omawww.sat.gob.mx/tramitesyservicios/paginas/certificado_sello_digital.htm) · [Certificados_de_Prueba.zip](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Certificados_de_Prueba.zip) · [Anexo 20 page](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm) · [catCFDI_V_4_20261029.xls](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_20261029.xls) · [Anexo 20 Guía de llenado CFDI 4.0](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo_20_Guia_de_llenado_CFDI.pdf) · [Guía de llenado del CFDI global](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Guia_llenado_CFDI_global.pdf)
- Banxico: [Circular 12/2018 (CLABE check digit annex)](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-12-2018/%7BA6023AE0-8135-44ED-04DA-2068117ED5FD%7D.pdf)
- Correos de México: [Catálogo Nacional de Códigos Postales (export)](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx)
- IFT: [Plan Técnico Fundamental de Numeración](https://www.ift.org.mx/sites/default/files/ptfn_1996_vlimpia.pdf) · [Comunicado 34/2019 (10-digit dialling)](https://www.ift.org.mx/sites/default/files/comunicado_34_ift.pdf) · [Number lookup](https://sns.ift.org.mx:8081/sns-frontend/)
- Secondary (PACs): [Facturama — CSD de pruebas (postcodes)](https://facturama.mx/docs/es/catalogos/csds-pruebas) · [SW Sapien — CSD de pruebas vigentes](https://developers.sw.com.mx/knowledge-base/donde-encuentro-csd-de-pruebas-vigentes/) · [Sovos/Reachcore](https://go.reachcore.com/docs/Articulos/CSDPruebas) · [Timbox](https://www.timbox.com.mx/rfcs-ambiente-de-pruebas-sat/)

**Colombia**
- DIAN: [Documentación técnica](https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica/) · [Caja de herramientas FE V1.9 (v2026)](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-herramientas-FE_V19_v2026.zip) · [Anexo Técnico FEV v1.9](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo-Tecnico-Factura-Electronica-de-Venta-vr-1-9.pdf) · [Anexo v1.8](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo-Tecnico-Resolucion-000012-09022021.pdf) · [Habilitación portal](https://catalogo-vpfe-hab.dian.gov.co/User/Login)
- RUES open data: [datos.gov.co dataset c82u-588k](https://www.datos.gov.co/resource/c82u-588k.json)
- 4-72: [codigopostal.gov.co](http://www.codigopostal.gov.co)
- CRC: [Resolución CRC 5826 de 2019 (normograma)](https://normograma.info/crc/docs/resolucion_crc_5826_2019.htm) · [ITU notification, Colombia +57](https://www.itu.int/dms_pub/itu-t/oth/02/02/T020200002C0002PDFS.pdf)
- Secondary: [gerencie.com — cuantías menores](https://gerencie.com/informacion-exogena-en-facturacion-en-ventas-masivas-al-detal.html) · [actualicese.com — seudo-NIT 222222222](https://actualicese.com/archivo/seudo-nit-222222222-en-los-formatos-de-informacion-exogena-ag-2020/) · [Aliaddo — test-set invoice](https://factura-electronica.aliaddo.dev/habilitacion/facturas/enviar-una-factura-para-set-de-pruebas)

**General**
- IETF: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) · [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761)
- GS1: [Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix)
