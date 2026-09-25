#!/usr/bin/env python3
"""Rebuild SP 800-53 Rev. 5 control catalog, baselines, and SP 800-53A objectives from NIST OSCAL content.

Outputs (00_universal/frameworks/):
  sp800-53r5_controls.csv     every control and enhancement with family, title, withdrawn flag, and baselines
  sp800-53a_objectives.csv    every leaf assessment objective (determination statement) with its label
Usage: python3 tools/refresh_sp800_53.py [--cache DIR]
"""
import csv, json, pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "00_universal" / "frameworks"
BASE = "https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/"
FILES = {
    "catalog": "NIST_SP-800-53_rev5_catalog.json",
    "low": "NIST_SP-800-53_rev5_LOW-baseline_profile.json",
    "moderate": "NIST_SP-800-53_rev5_MODERATE-baseline_profile.json",
    "high": "NIST_SP-800-53_rev5_HIGH-baseline_profile.json",
    "privacy": "NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json",
}


def load(name, cache):
    if cache and (cache / FILES[name]).exists():
        return json.load(open(cache / FILES[name]))
    with urllib.request.urlopen(BASE + FILES[name], timeout=180) as r:
        return json.load(r)


def label(ctrl):
    for p in ctrl.get("props", []):
        if p["name"] == "label" and "class" not in p:
            return p["value"]
    return ctrl["id"].upper()


def prose(s):
    s = re.sub(r"\{\{\s*insert: param, [^}]+\}\}", "[organization-defined value]", s or "")
    return " ".join(s.split())


def main():
    cache = pathlib.Path(sys.argv[sys.argv.index("--cache") + 1]) if "--cache" in sys.argv else None
    cat = load("catalog", cache)["catalog"]
    version = cat["metadata"]["version"]
    baselines = {}
    for b in ("low", "moderate", "high", "privacy"):
        prof = load(b, cache)["profile"]
        ids = set()
        for imp in prof["imports"]:
            for inc in imp.get("include-controls", []):
                ids.update(inc.get("with-ids", []))
        baselines[b] = ids
    controls, objectives = [], []

    def walk_obj(parts, cid):
        for p in parts:
            if p.get("name") != "assessment-objective":
                continue
            kids = [k for k in p.get("parts", []) if k.get("name") == "assessment-objective"]
            if kids:
                walk_obj(kids, cid)
            else:
                lab = next((x["value"] for x in p.get("props", []) if x["name"] == "label"), p["id"])
                objectives.append([cid, lab, prose(p.get("prose"))])

    def walk(ctrl, fam_id, fam):
        withdrawn = any(p["name"] == "status" and p["value"] == "withdrawn" for p in ctrl.get("props", []))
        cid = label(ctrl)
        controls.append([cid, fam_id.upper(), fam, ctrl["title"], "yes" if withdrawn else "no"]
                        + ["x" if ctrl["id"] in baselines[b] else "" for b in ("low", "moderate", "high", "privacy")])
        walk_obj(ctrl.get("parts", []), cid)
        for sub in ctrl.get("controls", []):
            walk(sub, fam_id, fam)

    for g in cat["groups"]:
        for c in g.get("controls", []):
            walk(c, g["id"], g["title"])
    with open(OUT / "sp800-53r5_controls.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["control_id", "family_id", "family", "title", "withdrawn", "baseline_low", "baseline_moderate", "baseline_high", "baseline_privacy"])
        w.writerows(controls)
    with open(OUT / "sp800-53a_objectives.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["control_id", "objective_label", "determination_statement"])
        w.writerows(objectives)
    print(f"SP 800-53 {version}: {len(controls)} controls/enhancements, {len(objectives)} assessment objectives")


if __name__ == "__main__":
    main()
