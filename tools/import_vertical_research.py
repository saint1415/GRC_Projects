#!/usr/bin/env python3
"""One-time bootstrap: convert vertical research JSON into 02_industry-rules/<sector>/ CSV files.

After the bootstrap, the CSV files are the source of truth and are edited directly.
Re-running overwrites profile.csv, requirements.csv, and incident-notification.csv for the units in the JSON.

JSON schema (list of units):
  id, name, regulators[], regulations[{short, citation, summary, applies_to, size_thresholds, status, url, verified}],
  gap_analysis_primary{short, citation, url, rationale}, incident_notification[{requirement, citation, deadline, notify, url, verified}],
  ai_specific[], sensitive_data[], critical_systems[], notes

Usage: python3 tools/import_vertical_research.py research.json [research2.json ...] --verified-on YYYY-MM-DD
"""
import csv, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "02_industry-rules"

# Assurance mechanisms customers or regulators commonly expect instead of, or in addition to, SOC 2.
ASSURANCE = {
    "c-dib": "CMMC assessment (32 CFR Part 170) for DoD contracts; SOC 2 is secondary",
    "n44-45": "PCI DSS validation for card payments (PCI SSC standard, enforced through card-brand contracts)",
    "c-financial": "PCI DSS validation as a service provider; SOC 1 for financial reporting controls",
    "n71": "PCI DSS validation for card payments",
    "n72": "PCI DSS validation for card payments",
    "n52": "Federal and state bank examinations (FFIEC); SOC 1 from service providers",
    "n51": "ISO/IEC 27001 certification; FedRAMP authorization for federal customers",
    "c-it": "FedRAMP authorization for federal customers; ISO/IEC 27001 certification",
    "n92": "StateRAMP/GovRAMP (nonprofit program) for state and local customers; CJIS and IRS Publication 1075 audits",
    "n22": "NERC CIP compliance audits by regional entities (mandatory for applicable entities)",
    "c-energy": "TSA pipeline security directive compliance reviews (for designated pipelines)",
    "n54": "SOC 1 and SOC 2 reports are core services of CPA firms; client assurance via engagement letters",
}


def text(item, *keys):
    if isinstance(item, str):
        return item
    parts = [str(item.get(k, "")).strip() for k in keys if item.get(k)]
    return " ".join(parts)


def unit_dirs():
    units = list(csv.DictReader(open(V / "verticals.csv")))
    by_id = {u["unit_id"]: u for u in units}
    out = {}
    for u in units:
        out[u["unit_id"]] = V / u["slug"]
    return out


def write_csv(path, header, data):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(data)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verified_on = sys.argv[sys.argv.index("--verified-on") + 1] if "--verified-on" in sys.argv else ""
    args = [a for a in args if a != verified_on]
    dirs = unit_dirs()
    for path in args:
        for unit in json.load(open(path)):
            uid = unit["id"]
            if uid not in dirs:
                print(f"skip unknown unit {uid}")
                continue
            d = dirs[uid]
            d.mkdir(parents=True, exist_ok=True)
            prefix = uid.upper()
            gap = unit.get("gap_analysis_primary") or {}
            regs = unit.get("regulations", [])
            write_csv(d / "requirements.csv",
                      ["req_id", "short_name", "citation", "summary", "applies_to", "size_thresholds", "status", "source_url", "verified", "last_verified"],
                      [[f"{prefix}-R{i:02d}", r.get("short", ""), r.get("citation", ""), r.get("summary", ""), r.get("applies_to", ""),
                        r.get("size_thresholds", "") or "None identified", r.get("status", ""), r.get("url", ""),
                        str(r.get("verified", False)).lower(), verified_on] for i, r in enumerate(regs, 1)])
            write_csv(d / "incident-notification.csv",
                      ["obligation", "citation", "trigger", "deadline", "notify", "source_url", "verified"],
                      [[n.get("requirement", ""), n.get("citation", ""), n.get("trigger", ""), n.get("deadline", ""), n.get("notify", ""),
                        n.get("url", ""), str(n.get("verified", False)).lower()] for n in unit.get("incident_notification", [])])
            profile = {
                "regulators": "; ".join(text(r, "name", "role") for r in unit.get("regulators", [])),
                "primary_regulation": gap.get("short", ""),
                "primary_regulation_citation": gap.get("citation", ""),
                "primary_regulation_url": gap.get("url", ""),
                "primary_regulation_rationale": gap.get("rationale", ""),
                "sensitive_data": "; ".join(text(s, "name") for s in unit.get("sensitive_data", [])),
                "critical_systems": "; ".join(text(s, "name") for s in unit.get("critical_systems", [])),
                "ai_specific": "; ".join(text(a, "short", "name", "citation", "summary") for a in unit.get("ai_specific", [])),
                "assurance_alternatives": ASSURANCE.get(uid, ""),
                "notes": unit.get("notes", "") if isinstance(unit.get("notes", ""), str) else "; ".join(unit["notes"]),
                "last_verified": verified_on,
            }
            write_csv(d / "profile.csv", ["field", "value"], profile.items())
            print(f"{uid}: {len(regs)} requirements, {len(unit.get('incident_notification', []))} notifications")


if __name__ == "__main__":
    main()
