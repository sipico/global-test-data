"""Check-digit and format validators for the global test data set.

Each validator takes the value as a string and returns True/False.
Spaces, dots, hyphens and slashes are stripped before checking unless the
validator says otherwise. Add a new validator by writing a function and
registering it in CHECKS with a short description.
"""

import re

_STRIP = re.compile(r"[\s.\-/]")


def _clean(v):
    return _STRIP.sub("", str(v)).upper()


def _luhn_digits(s):
    total = 0
    for i, c in enumerate(reversed(s)):
        d = int(c)
        if i % 2:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def luhn(v):
    s = _clean(v)
    return s.isdigit() and _luhn_digits(s)


def mod97_iso7064(s):
    """ISO 7064 MOD 97-10 on an alphanumeric string (letters A=10..Z=35)."""
    return int("".join(str(int(c, 36)) for c in s)) % 97 == 1


def iban(v):
    s = _clean(v)
    if not re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]{10,30}", s):
        return False
    return mod97_iso7064(s[4:] + s[:4])


def bic(v):
    return bool(re.fullmatch(r"[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?", _clean(v)))


def bic_test(v):
    """ISO 9362 convention: '0' as 2nd character of the location code = test BIC."""
    s = _clean(v)
    return bic(s) and s[7] == "0"


def gs1(v):
    """GS1 mod-10 check digit (GTIN-8/12/13/14, GLN, SSCC)."""
    s = _clean(v)
    if not s.isdigit() or len(s) not in (8, 12, 13, 14, 17, 18):
        return False
    body, check = s[:-1], int(s[-1])
    total = sum(int(c) * (3 if i % 2 == 0 else 1) for i, c in enumerate(reversed(body)))
    return (10 - total % 10) % 10 == check


def gs1_952(v):
    s = _clean(v)
    return gs1(s) and s.lstrip("0").startswith("952")


def lei(v):
    s = _clean(v)
    return bool(re.fullmatch(r"[A-Z0-9]{18}\d{2}", s)) and mod97_iso7064(s)


# --- Europe -----------------------------------------------------------------

def fr_siren(v):
    s = _clean(v)
    return len(s) == 9 and luhn(s)


def fr_siret(v):
    s = _clean(v)
    return len(s) == 14 and luhn(s)


def fr_vat(v):
    s = _clean(v)
    m = re.fullmatch(r"FR(\d{2})(\d{9})", s)
    if not m:
        return False
    key, siren = int(m.group(1)), int(m.group(2))
    return key == (12 + 3 * (siren % 97)) % 97


def it_piva(v):
    s = _clean(v)
    if s.startswith("IT"):
        s = s[2:]
    return len(s) == 11 and s.isdigit() and _luhn_digits(s)


# --- Oceania ------------------------------------------------------------------

def au_abn(v):
    s = _clean(v)
    if len(s) != 11 or not s.isdigit():
        return False
    d = [int(c) for c in s]
    d[0] -= 1
    w = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    return sum(a * b for a, b in zip(d, w)) % 89 == 0


def au_acn(v):
    s = _clean(v)
    if len(s) != 9 or not s.isdigit():
        return False
    t = sum(int(c) * w for c, w in zip(s[:8], [8, 7, 6, 5, 4, 3, 2, 1]))
    return (10 - t % 10) % 10 == int(s[8])


def nz_ird(v):
    s = _clean(v)
    if not s.isdigit() or len(s) not in (8, 9):
        return False
    if not (10_000_000 < int(s) < 200_000_000):  # Inland Revenue range, 2026-27 spec
        return False
    s = s.zfill(9)
    body, check = [int(c) for c in s[:8]], int(s[8])
    for w in ([3, 2, 7, 6, 5, 4, 3, 2], [7, 4, 3, 2, 5, 2, 7, 6]):
        r = sum(a * b for a, b in zip(body, w)) % 11
        c = 0 if r == 0 else 11 - r
        if c != 10:
            return c == check
    return False


# --- Asia ---------------------------------------------------------------------

def jp_corporate(v):
    s = _clean(v)
    if s.startswith("T"):
        s = s[1:]
    if len(s) != 13 or not s.isdigit():
        return False
    d = [int(c) for c in s[1:]][::-1]
    t = sum(x * (1 if i % 2 == 0 else 2) for i, x in enumerate(d))
    return 9 - t % 9 == int(s[0])


def kr_brn(v):
    s = _clean(v)
    if len(s) != 10 or not s.isdigit():
        return False
    d = [int(c) for c in s]
    w = [1, 3, 7, 1, 3, 7, 1, 3, 5]
    t = sum(a * b for a, b in zip(d[:9], w)) + (d[8] * 5) // 10
    return (10 - t % 10) % 10 == d[9]


_VERHOEFF_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
_VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 8, 7, 6, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]


def in_aadhaar(v):
    s = _clean(v)
    if len(s) != 12 or not s.isdigit():
        return False
    c = 0
    for i, ch in enumerate(reversed(s)):
        c = _VERHOEFF_D[c][_VERHOEFF_P[i % 8][int(ch)]]
    return c == 0


def in_gstin(v):
    s = _clean(v)
    if not re.fullmatch(r"\d{2}[A-Z0-9]{10}[A-Z0-9]Z[A-Z0-9]", s):
        return False
    cs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = 0
    for i, ch in enumerate(s[:14]):
        p = cs.index(ch) * (2 if i % 2 else 1)
        t += p // 36 + p % 36
    return cs[(36 - t % 36) % 36] == s[14]


def sg_uen(v):
    """Singapore UEN: business (8+1), local company (9+1), others (T/S/R yy + PQ + 4 + 1)."""
    s = _clean(v)
    if re.fullmatch(r"\d{8}[A-Z]", s):
        w = [10, 4, 9, 3, 8, 2, 7, 1]
        t = sum(int(c) * x for c, x in zip(s[:8], w))
        return "XMKECAWLJDB"[t % 11] == s[8]
    if re.fullmatch(r"\d{9}[A-Z]", s):
        w = [10, 8, 6, 4, 9, 7, 5, 3, 1]
        t = sum(int(c) * x for c, x in zip(s[:9], w))
        return "ZKCMDNERGWH"[t % 11] == s[9]
    if re.fullmatch(r"[TSR]\d{2}[A-Z]{2}\d{4}[A-Z]", s):
        al = "ABCDEFGHJKLMNPQRSTUVWX0123456789"
        w = [4, 3, 5, 3, 10, 2, 2, 5, 7]
        t = sum(al.index(c) * x for c, x in zip(s[:9], w))
        return al[(t - 5) % 11] == s[9]
    return False


def sg_nric(v):
    s = _clean(v)
    if not re.fullmatch(r"[STFGM]\d{7}[A-Z]", s):
        return False
    w = [2, 7, 6, 5, 4, 3, 2]
    t = sum(int(c) * x for c, x in zip(s[1:8], w))
    p = s[0]
    if p in "TG":
        t += 4
    elif p == "M":
        t += 3
    r = t % 11
    if p in "ST":
        table = "JZIHGFEDCBA"
    elif p in "FG":
        table = "XWUTRQPNMLK"
    else:
        table = "KLJNPQRTUWX"
    return table[r] == s[8]


def cn_uscc(v):
    s = _clean(v)
    cs = "0123456789ABCDEFGHJKLMNPQRTUWXY"
    if len(s) != 18 or any(c not in cs for c in s):
        return False
    w = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
    t = sum(cs.index(c) * x for c, x in zip(s, w))
    return cs[(31 - t % 31) % 31] == s[17]


def cn_resident_id(v):
    s = _clean(v)
    if not re.fullmatch(r"\d{17}[\dX]", s):
        return False
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    t = sum(int(c) * x for c, x in zip(s[:17], w))
    return "10X98765432"[t % 11] == s[17]


def tw_ubn(v):
    s = _clean(v)
    if len(s) != 8 or not s.isdigit():
        return False
    w = [1, 2, 1, 2, 1, 2, 4, 1]
    t = 0
    for c, x in zip(s, w):
        p = int(c) * x
        t += p // 10 + p % 10
    return t % 5 == 0 or (s[6] == "7" and (t + 1) % 5 == 0)


def hk_hkid(v):
    """HKID: 1-2 letters + 6 digits + check (0-9 or A). Widely used algorithm; ImmD does not publish it."""
    s = _clean(v).replace("(", "").replace(")", "")
    m = re.fullmatch(r"([A-Z]{1,2})(\d{6})([0-9A])", s)
    if not m:
        return False
    letters, digits, check = m.groups()
    vals = [ord(c) - 55 for c in letters]
    if len(vals) == 1:
        vals = [36] + vals
    t = vals[0] * 9 + vals[1] * 8 + sum(int(d) * w for d, w in zip(digits, range(7, 1, -1)))
    r = 11 - t % 11
    exp = "0" if r == 11 else "A" if r == 10 else str(r)
    return exp == check


def tw_national_id(v):
    """Taiwan national ID: letter + 9 digits, total divisible by 10 (letter split into two digits)."""
    s = _clean(v)
    if not re.fullmatch(r"[A-Z][12]\d{8}", s):
        return False
    codes = dict(zip("ABCDEFGHJKLMNPQRSTUVXYWZIO", range(10, 36)))
    n = codes[s[0]]
    digits = [n // 10, n % 10] + [int(c) for c in s[1:]]
    w = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    return sum(a * b for a, b in zip(digits, w)) % 10 == 0


# --- Americas -----------------------------------------------------------------

def _mod11_cnpj(vals, n):
    w = list(range(2, 10)) * 2
    t = sum(vals[i] * w[n - 1 - i] for i in range(n))
    r = t % 11
    return 0 if r < 2 else 11 - r


def br_cnpj(v):
    """Numeric and 2026 alphanumeric CNPJ (char value = ASCII - 48)."""
    s = _clean(v)
    if not re.fullmatch(r"[0-9A-Z]{12}\d{2}", s):
        return False
    vals = [ord(c) - 48 for c in s]
    return _mod11_cnpj(vals, 12) == vals[12] and _mod11_cnpj(vals, 13) == vals[13]


def br_cpf(v):
    s = _clean(v)
    if len(s) != 11 or not s.isdigit() or len(set(s)) == 1:
        return False
    d = [int(c) for c in s]
    for n in (9, 10):
        t = sum(d[i] * (n + 1 - i) for i in range(n))
        if (t * 10 % 11) % 10 != d[n]:
            return False
    return True


def cl_rut(v):
    s = _clean(v)
    if not re.fullmatch(r"\d{7,8}[\dK]", s):
        return False
    body, dv = s[:-1], s[-1]
    t, m = 0, 2
    for c in reversed(body):
        t += int(c) * m
        m = 2 if m == 7 else m + 1
    r = 11 - t % 11
    exp = "0" if r == 11 else "K" if r == 10 else str(r)
    return exp == dv


def ar_cuit(v):
    s = _clean(v)
    if len(s) != 11 or not s.isdigit():
        return False
    w = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    r = 11 - sum(int(c) * x for c, x in zip(s[:10], w)) % 11
    exp = 0 if r == 11 else 9 if r == 10 else r
    return exp == int(s[10])


def ar_cbu(v):
    """CBU: 22 digits in two blocks, each with a weighted mod-10 check digit (BCRA Com. A 2622)."""
    s = _clean(v)
    if len(s) != 22 or not s.isdigit():
        return False

    b1, b2 = s[:8], s[8:]
    w1 = [7, 1, 3, 9, 7, 1, 3]
    c1 = (10 - sum(int(c) * x for c, x in zip(b1[:7], w1)) % 10) % 10
    w2 = [3, 9, 7, 1, 3, 9, 7, 1, 3, 9, 7, 1, 3]
    c2 = (10 - sum(int(c) * x for c, x in zip(b2[:13], w2)) % 10) % 10
    return c1 == int(b1[7]) and c2 == int(b2[13])


def co_nit(v):
    """Colombian NIT with check digit as last character (e.g. 981223983-1)."""
    s = _clean(v)
    if not s.isdigit() or len(s) < 2:
        return False
    body, dv = s[:-1], int(s[-1])
    w = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
    t = sum(int(c) * x for c, x in zip(reversed(body), w))
    r = t % 11
    return (r if r < 2 else 11 - r) == dv


def mx_clabe(v):
    s = _clean(v)
    if len(s) != 18 or not s.isdigit():
        return False
    w = [3, 7, 1] * 6
    t = sum((int(c) * x) % 10 for c, x in zip(s[:17], w))
    return (10 - t % 10) % 10 == int(s[17])


def mx_rfc(v):
    """RFC homoclave check digit (12 chars companies, 13 chars persons)."""
    s = _clean(v).replace("Ñ", "#")
    if not re.fullmatch(r"[A-Z&#]{3,4}\d{6}[A-Z0-9]{3}", s):
        return False
    al = "0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ #"
    if len(s) == 12:
        s2 = " " + s
    else:
        s2 = s
    t = sum(al.index(c) * (13 - i) for i, c in enumerate(s2[:12]))
    r = t % 11
    exp = "0" if r == 0 else "A" if 11 - r == 10 else str(11 - r)
    return exp == s2[12]


def mx_curp(v):
    """CURP: 18 chars; check digit (10 - sum(value*weight 18..2) mod 10) mod 10 (RENAPO). Ñ handling unverified."""
    s = str(v).strip().upper()
    if not re.fullmatch(r"[A-ZÑ]{4}\d{6}[HMX][A-ZÑ]{5}[0-9A-Z]\d", s):
        return False
    al = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    t = sum(al.index(c) * w for c, w in zip(s[:17], range(18, 1, -1)))
    return (10 - t % 10) % 10 == int(s[17])


# --- Africa -------------------------------------------------------------------

def za_id(v):
    s = _clean(v)
    return len(s) == 13 and luhn(s)


def ng_nuban(v):
    """NUBAN: pass as '<3-digit bank code>:<10-digit account>' (CBN algorithm)."""
    m = re.fullmatch(r"(\d{3}):(\d{10})", str(v).replace(" ", ""))
    if not m:
        return False
    s = m.group(1) + m.group(2)[:9]
    w = [3, 7, 3, 3, 7, 3, 3, 7, 3, 3, 7, 3]
    t = sum(int(c) * x for c, x in zip(s, w))
    c = 10 - t % 10
    return (0 if c == 10 else c) == int(m.group(2)[9])


def za_paye(v):
    """SARS PAYE/SDL/UIF reference: 7/L/U + 9 digits; Luhn after replacing the first character by 4 (SARS BRS 9.2)."""
    s = _clean(v)
    return bool(re.fullmatch(r"[7LU]\d{9}", s)) and _luhn_digits("4" + s[1:])


def ke_kra_pin(v):
    """KRA PIN format only (no public check-letter algorithm): A/P + 9 digits + letter."""
    return bool(re.fullmatch(r"[AP]\d{9}[A-Z]", _clean(v)))


# --- Internet -----------------------------------------------------------------

_RESERVED_TLDS = ("test", "example", "invalid", "localhost")
_RESERVED_DOMAINS = (
    "example.com", "example.net", "example.org",  # RFC 2606
    "example.jp", "example.co.jp", "example.ne.jp",  # reserved by JPRS (.jp registry)
)
_RESERVED_PATTERNS = (re.compile(r"(^|\.)example\d\.(co\.|ne\.)?jp$"),)  # JPRS example0-9


def reserved_domain(v):
    host = str(v).split("@")[-1].lower().rstrip(".")
    if host.split(".")[-1] in _RESERVED_TLDS:
        return True
    if any(p.search(host) for p in _RESERVED_PATTERNS):
        return True
    return any(host == d or host.endswith("." + d) for d in _RESERVED_DOMAINS)


CHECKS = {
    "luhn": (luhn, "Luhn mod-10"),
    "iban": (iban, "ISO 13616 IBAN mod-97"),
    "bic": (bic, "ISO 9362 BIC format"),
    "bic-test": (bic_test, "ISO 9362 test BIC (8th character '0')"),
    "gs1": (gs1, "GS1 mod-10 check digit"),
    "gs1-952": (gs1_952, "GS1 key with prefix 952 (examples) and valid check digit"),
    "lei": (lei, "ISO 17442 LEI mod-97"),
    "fr-siren": (fr_siren, "SIREN: 9 digits, Luhn"),
    "fr-siret": (fr_siret, "SIRET: 14 digits, Luhn"),
    "fr-vat": (fr_vat, "French VAT key (12 + 3 × (SIREN mod 97)) mod 97"),
    "it-piva": (it_piva, "Partita IVA: 11 digits, Luhn"),
    "au-abn": (au_abn, "ABN mod-89"),
    "au-acn": (au_acn, "ACN mod-10"),
    "nz-ird": (nz_ird, "IRD number mod-11 (Inland Revenue)"),
    "jp-corporate": (jp_corporate, "Japanese Corporate Number check digit (optional T prefix)"),
    "kr-brn": (kr_brn, "Korean business registration number check digit"),
    "in-aadhaar": (in_aadhaar, "Aadhaar Verhoeff check digit"),
    "in-gstin": (in_gstin, "GSTIN mod-36 check character"),
    "sg-uen": (sg_uen, "Singapore UEN check letter"),
    "sg-nric": (sg_nric, "Singapore NRIC/FIN check letter"),
    "cn-uscc": (cn_uscc, "Unified Social Credit Code (GB 32100) check character"),
    "cn-resident-id": (cn_resident_id, "Resident ID (GB 11643) ISO 7064 MOD 11-2"),
    "tw-ubn": (tw_ubn, "Taiwan Unified Business Number (2023 rule)"),
    "hk-hkid": (hk_hkid, "Hong Kong ID check character (unofficial algorithm)"),
    "tw-national-id": (tw_national_id, "Taiwan national ID check digit"),
    "br-cnpj": (br_cnpj, "CNPJ mod-11 (numeric and alphanumeric)"),
    "br-cpf": (br_cpf, "CPF mod-11"),
    "cl-rut": (cl_rut, "Chilean RUT mod-11"),
    "ar-cuit": (ar_cuit, "Argentine CUIT/CUIL mod-11"),
    "co-nit": (co_nit, "Colombian NIT check digit (DIAN)"),
    "mx-clabe": (mx_clabe, "CLABE weighted mod-10"),
    "mx-rfc": (mx_rfc, "RFC homoclave check digit"),
    "mx-curp": (mx_curp, "CURP check digit (RENAPO; Ñ handling unverified)"),
    "za-id": (za_id, "South African ID number, Luhn"),
    "za-paye": (za_paye, "SARS PAYE/SDL/UIF reference (Luhn with leading 4)"),
    "ke-kra-pin": (ke_kra_pin, "KRA PIN format (no public check algorithm)"),
    "ar-cbu": (ar_cbu, "Argentine CBU, two weighted mod-10 check digits"),
    "ng-nuban": (ng_nuban, "NUBAN check digit, value as 'bank:account'"),
    "reserved-domain": (reserved_domain, "Reserved example domain (RFC 2606/6761, JPRS)"),
}
