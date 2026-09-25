#!/usr/bin/env python3
"""Consistency checks for the GRC library. Exit code 1 on errors; warnings are informational.

Checks:
  - CSF 2.0 subcategory/category IDs and SP 800-53 control IDs cited in layers 00-02 exist in the official catalogs
  - source IDs cited in registries exist in the source register
  - every vertical has profile, requirements, and notification files with required fields
  - every NAICS code used has an SBA size-standard row
  - every relative markdown link resolves
  - scenario folder count matches verticals x tiers
Usage: python3 tools/validate.py
"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
U, T, V, S = (ROOT / d for d in ("00_universal", "01_tiers", "02_verticals", "03_scenarios"))
errors, warnings = [], []


def rows(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f))


# ---- catalogs
csf = rows(U / "frameworks" / "csf2_core.csv")
csf_ids = {r["subcategory_id"] for r in csf} | {r["category_id"] for r in csf}
ctrl_ids = {r["control_id"] for r in rows(U / "frameworks" / "sp800-53r5_controls.csv")}
families = {c.split("-")[0] for c in ctrl_ids}
CSF_RE = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}(?:-\d{2})?\b")
CTRL_RE = re.compile(r"\b(" + "|".join(sorted(families)) + r")-(\d{1,2})(\((\d{1,2})\))?(?![\d.])")

layer_files = [p for d in (U / "projects", U / "cross-sector", T, V) for p in d.rglob("*") if p.suffix in (".md", ".csv")]
for p in layer_files:
    text = p.read_text()
    for m in CSF_RE.findall(text):
        if m not in csf_ids:
            errors.append(f"{p.relative_to(ROOT)}: unknown CSF 2.0 ID {m}")
    if p.parent.name.startswith("P") or p.parent == U / "projects":
        for fam, num, _, enh in CTRL_RE.findall(text):
            cid = f"{fam}-{int(num)}" + (f"({int(enh)})" if enh else "")
            if cid not in ctrl_ids:
                errors.append(f"{p.relative_to(ROOT)}: unknown SP 800-53 control {cid}")

# ---- sources
src_ids = {r["source_id"] for r in rows(U / "sources" / "source-register.csv")}
for r in rows(U / "projects" / "projects.csv"):
    for s in r["primary_sources"].split(";"):
        if s not in src_ids:
            errors.append(f"projects.csv {r['project_id']}: unknown source {s}")
for r in rows(T / "tiers.csv"):
    for s in r["sources"].split(";"):
        if s not in src_ids:
            errors.append(f"tiers.csv {r['tier_id']}: unknown source {s}")

# ---- verticals
units = rows(V / "verticals.csv")
by_id = {u["unit_id"]: u for u in units}
sba = {r["naics6"] for r in rows(V / "sba-size-standards.csv")}
codes = {u["primary_naics"] for u in units} | {o["naics6"] for o in rows(V / "scenario-industry-overrides.csv")}
for c in sorted(codes - sba):
    errors.append(f"NAICS {c} has no row in sba-size-standards.csv (run tools/refresh_sba_standards.py)")
unverified = 0
for u in units:
    d = V / u["slug"] if u["level"] == "naics_sector" else V / by_id[u["parent_id"]]["slug"] / u["slug"]
    for fname in ("profile.csv", "requirements.csv", "incident-notification.csv"):
        if not (d / fname).exists():
            errors.append(f"{u['unit_id']}: missing {d.relative_to(ROOT)}/{fname}")
    if (d / "profile.csv").exists():
        prof = {r["field"]: r["value"] for r in rows(d / "profile.csv")}
        for k in ("regulators", "primary_regulation", "primary_regulation_citation", "primary_regulation_url"):
            if not prof.get(k):
                errors.append(f"{u['unit_id']}: profile.csv missing {k}")
    if (d / "requirements.csv").exists():
        reqs = rows(d / "requirements.csv")
        if not reqs:
            warnings.append(f"{u['unit_id']}: no requirements listed")
        for r in reqs:
            if not r["source_url"].startswith("http"):
                errors.append(f"{u['unit_id']} {r['req_id']}: missing source URL")
            unverified += r["verified"] != "true"
    if (d / "incident-notification.csv").exists():
        unverified += sum(r["verified"] != "true" for r in rows(d / "incident-notification.csv"))
if unverified:
    warnings.append(f"{unverified} vertical requirement/notification rows are marked verified=false; review before relying on them")

# ---- links (skip generated scenario tree except a sample for speed)
md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and S not in p.parents]
md_files += list((S / "n62_health-care" / "t3_small").rglob("*.md")) + [S / "INDEX.md"]
LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
for p in md_files:
    if not p.exists():
        continue
    for target in LINK_RE.findall(p.read_text()):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (p.parent / target).resolve().exists():
            errors.append(f"{p.relative_to(ROOT)}: broken link {target}")

# ---- scenario count
tiers = rows(T / "tiers.csv")
readmes = list(S.rglob("t*_*/README.md"))
if len(readmes) != len(units) * len(tiers):
    errors.append(f"expected {len(units) * len(tiers)} scenarios, found {len(readmes)} (run tools/build_scenarios.py)")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"\n{len(errors)} errors, {len(warnings)} warnings. Checked {len(layer_files)} layer files, {len(md_files)} markdown files, {len(readmes)} scenarios.")
sys.exit(1 if errors else 0)
