#!/usr/bin/env python3
"""Refresh 02_industry-rules/sba-size-standards.csv from the live eCFR text of 13 CFR 121.201.

Only NAICS codes referenced by verticals.csv or scenario-industry-overrides.csv are exported.
Usage: python3 tools/refresh_sba_standards.py
"""
import csv, datetime, gzip, html, pathlib, re, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "02_industry-rules"


def fetch_table():
    date = datetime.date.today().isoformat()
    url = f"https://www.ecfr.gov/api/versioner/v1/full/{date}/title-13.xml?part=121&section=121.201"
    req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
    except urllib.error.HTTPError:  # today's issue may not be published yet
        date = (datetime.date.today() - datetime.timedelta(days=3)).isoformat()
        with urllib.request.urlopen(urllib.request.Request(url.replace(url.split("/full/")[1].split("/")[0], date), headers={"Accept-Encoding": "gzip"}), timeout=120) as r:
            raw = r.read()
    xml = gzip.decompress(raw).decode() if raw[:2] == b"\x1f\x8b" else raw.decode()
    table = {}
    for row in re.findall(r"<TR>(.*?)</TR>", xml, re.S):
        cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<T[DH][^>]*>(.*?)</T[DH]>", row, re.S)]
        if cells and re.match(r"^\d{6}$", cells[0]):
            table[cells[0]] = cells[1:] + [""] * (3 - len(cells[1:]))
    return table, date


def parse(title, receipts, employees):
    """Split footnote markers from values; return (title, basis, value, footnotes)."""
    notes = set(re.findall(r"(?<=[a-z\)])\s?(\d{1,2})$", title))
    title = re.sub(r"\s?\d{1,2}$", "", title).strip()
    if employees:
        m = re.match(r"(?:(\d{1,2})\s)?([\d,]+)(?:\s(\d{1,2}))?$", employees)
        notes |= {n for n in (m.group(1), m.group(3)) if n}
        return title, "employees", int(m.group(2).replace(",", "")), notes
    m = re.match(r"\$([\d.]+)( million in assets)?(?:\s(\d{1,2}))?$", receipts)
    if m.group(3):
        notes.add(m.group(3))
    basis = "assets_musd" if m.group(2) else "receipts_musd"
    return title, basis, float(m.group(1)), notes


def main():
    codes = {r["primary_naics"] for r in csv.DictReader(open(V / "verticals.csv"))}
    codes |= {r["naics6"] for r in csv.DictReader(open(V / "scenario-industry-overrides.csv"))}
    table, date = fetch_table()
    with open(V / "sba-size-standards.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["naics6", "industry_title", "basis", "size_standard", "footnotes", "source", "ecfr_date"])
        for c in sorted(codes):
            if c not in table:
                w.writerow([c, "", "none", "", "", "No SBA size standard for this code", date])
                continue
            title, basis, value, notes = parse(*table[c])
            w.writerow([c, title, basis, value, ";".join(sorted(notes)), "13 CFR 121.201", date])
    print(f"wrote {len(codes)} codes from eCFR {date}")


if __name__ == "__main__":
    main()
