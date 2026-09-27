#!/usr/bin/env python3
"""Consistency checks for the GRC library. Exit code 1 on errors; warnings are informational.

Checks:
  - CSF 2.0 subcategory/category IDs and SP 800-53 control IDs cited in layers 00-02 exist in the official catalogs
  - source IDs cited in registries exist in the source register
  - every vertical has profile, requirements, and notification files with required fields
  - every NAICS code used has an SBA size-standard row
  - every relative markdown link resolves (layers, docs, index, and every completed sample)
  - completed samples: no template markers, no em dashes, even CSV rows, valid CSF and SP 800-53 IDs
  - every sample folder matches 02_industry-rules/sample-folder-labels.csv (216 = 36 industries x 6 sizes)
Usage: python3 tools/validate.py
"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
U, T, V, S = (ROOT / d for d in ("00_universal-framework", "01_company-sizes", "02_industry-rules", "03_company-samples"))
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

CSF_V1_FILES = {"hipaa-nist-official-mapping.csv"}
layer_files = [p for d in (U / "projects", U / "cross-sector", T, V) for p in d.rglob("*") if p.suffix in (".md", ".csv")]
for p in layer_files:
    text = p.read_text()
    csf_check = p.name not in CSF_V1_FILES  # official NIST files that cite CSF 1.1 on purpose
    for m in CSF_RE.findall(text) if csf_check else []:
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
    d = V / u["slug"]
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

# ---- links (all layers, every completed sample, and the index; blank planned samples are skipped for speed)
md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and S not in p.parents]
md_files += [p for f in S.rglob("00_company-facts.md") for p in f.parent.rglob("*.md")] + [S / "INDEX.md"]
LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
for p in md_files:
    if not p.exists():
        continue
    for target in LINK_RE.findall(p.read_text()):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (p.parent / target).resolve().exists():
            errors.append(f"{p.relative_to(ROOT)}: broken link {target}")

# ---- completed samples (00_company-facts.md present): definition of done
for facts in S.rglob("00_company-facts.md"):
    sd = facts.parent
    for p in [x for x in sd.rglob("*") if x.suffix in (".md", ".csv") and x.name not in ("README.md", "_context.md")]:
        text = p.read_text()
        where = p.relative_to(ROOT)
        if "[FILL" in text or "{{" in text:
            errors.append(f"{where}: unfinished template marker in a completed sample")
        if "\u2014" in text:
            errors.append(f"{where}: em dash (house style uses a period or comma)")
        if p.suffix == ".csv":
            with open(p, newline="") as fh:
                widths = {len(r) for r in csv.reader(fh) if r}
            if len(widths) > 1:
                errors.append(f"{where}: rows have different column counts {sorted(widths)}")
        for m in CSF_RE.findall(text):
            if m not in csf_ids:
                errors.append(f"{where}: unknown CSF 2.0 ID {m}")
        for fam, num, _, enh in CTRL_RE.findall(text):
            cid = f"{fam}-{int(num)}" + (f"({int(enh)})" if enh else "")
            if cid not in ctrl_ids:
                errors.append(f"{where}: unknown SP 800-53 control {cid}")
    print(f"Completed sample checked: {sd.relative_to(S)}")

# ---- sample count and folder names (each folder must match sample-folder-labels.csv)
tiers = rows(T / "tiers.csv")
tier_slug = {r["tier_id"]: r["slug"] for r in tiers}
expected = {S / by_id[r["unit_id"]]["slug"] / f"{tier_slug[r['tier_id']]}_{r['business_label']}"
            for r in rows(V / "sample-folder-labels.csv")}
actual = {p for p in S.glob("*/size-*") if p.is_dir()}
for p in sorted(actual - expected):
    errors.append(f"{p.relative_to(ROOT)}: folder is not in sample-folder-labels.csv (label changed? move it with git mv)")
for p in sorted(expected - actual):
    errors.append(f"{p.relative_to(ROOT)}: expected sample folder is missing (run tools/build_scenarios.py)")
if len(expected) != len(units) * len(tiers):
    errors.append(f"sample-folder-labels.csv has {len(expected)} rows; expected {len(units) * len(tiers)}")
readmes = list(S.glob("*/size-*/README.md"))

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"\n{len(errors)} errors, {len(warnings)} warnings. Checked {len(layer_files)} layer files, {len(md_files)} markdown files, {len(readmes)} scenarios.")
sys.exit(1 if errors else 0)
