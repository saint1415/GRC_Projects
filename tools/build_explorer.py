#!/usr/bin/env python3
"""Build the sample company explorer site in docs/ from the finished samples.

It reads the finished sample folders in 03_company-samples/ and writes:
  docs/assets/grc-data.js  every company's data, shared by all pages
  docs/index.html          landing page: choose a look (from tools/landing_template.html)
  docs/app.html            the explorer in two looks, Case Files and Threat Board (tools/app_template.html)
  docs/explorer.html       the plain reading mode (tools/explorer_template.html)
Every page has a switch to move between the three modes without losing your place.
Only Google Fonts and the data file are fetched; fonts fall back to system fonts when offline.

Each company is retold as a plain-English story: who it is, what it runs on, where it
stands, which rules apply and why, what could go wrong, what the checks found, what it
does in an incident, and what it decided about AI. Every section links to the full
deliverable on GitHub.

Usage: python3 tools/build_explorer.py
Run it after any change to a sample, then python3 tools/validate.py.
"""
import csv, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
S = ROOT / "03_company-samples"
DATA = ROOT / "docs" / "assets" / "grc-data.js"
# (template in tools/, page in docs/): the landing page, the two-look app, and the plain reading mode.
PAGES = [("landing_template.html", "index.html"), ("app_template.html", "app.html"), ("explorer_template.html", "explorer.html")]
REPO = "https://github.com/saint1415/GRC_Projects/blob/main/"

TIERS = {1: "Sole proprietor", 2: "Micro", 3: "Small", 4: "Mid-market", 5: "Enterprise", 6: "Multi-sector"}
LEVELS = ["Very High", "High", "Moderate", "Low", "Very Low"]

# Plain-English names for the rules a company is actually tested against or must report under.
# Tags come from P03 rows that apply and P08 notification rows that apply, never from the
# vertical's full requirement list (that list is the same at every size).
TAGS = [
    ("HIPAA", r"HIPAA"),
    ("PCI DSS", r"PCI DSS"),
    ("CMMC and DFARS", r"CMMC|DFARS|800-171"),
    ("Federal contract clauses (FAR)", r"FAR 52\.204-21|FAR clause|FAR Basic|52\.204-21"),
    ("Section 889", r"\b889\b|52\.204-25"),
    ("FedRAMP or GovRAMP", r"FedRAMP|GovRAMP|StateRAMP"),
    ("SEC cyber disclosure", r"\bSEC\b|S-K Item 106|8-K Item 1\.05|Regulation S-P|Regulation SCI"),
    ("SOX", r"\bSOX\b|Sarbanes"),
    ("FTC Safeguards Rule (GLBA)", r"Safeguards Rule|GLBA|Gramm|16 CFR Part 314|16 CFR 314"),
    ("Bank regulators", r"Interagency Guidelines|\bOCC\b|Computer-Security Incident Notification|NCUA|Federal Reserve|Bank service provider"),
    ("NYDFS", r"NYDFS|23 NYCRR"),
    ("NERC CIP", r"NERC CIP|CIP-0\d\d"),
    ("TSA security directives", r"\bTSA\b"),
    ("Coast Guard maritime cyber", r"USCG|Maritime Cyber|MTSA|33 CFR Part 101|33 CFR 101"),
    ("CJIS", r"CJIS"),
    ("IRS tax data rules", r"Publication 1075|IRC 7216|Publication 4557|26 CFR 301\.7216"),
    ("FERPA", r"FERPA"),
    ("COPPA", r"COPPA"),
    ("CCPA", r"CCPA|CPPA|CPRA"),
    ("FTC Act Section 5", r"FTC Act"),
    ("State breach laws", r"[Ss]tate breach|501\.171|Information Protection Act"),
    ("NRC nuclear", r"\bNRC\b|10 CFR 73|10 CFR Part 37|RG 5\.71"),
    ("Drinking water (SDWA)", r"SDWA|AWIA"),
    ("FDA medical device", r"FDA premarket|FDA postmarket|524B|QMSR"),
    ("Food safety", r"FSMA|FSIS|HACCP|Food Traceability|Produce Safety"),
    ("CIRCIA (proposed)", r"CIRCIA"),
    ("FCC telecom", r"\bFCC\b|CPNI|CALEA"),
    ("Export controls", r"ITAR|\bEAR\b|Export Administration"),
    ("Chemical safety", r"CFATS|RBPS|\bRMP\b|1910\.119|40 CFR Part 68"),
    ("Pipeline and hazmat", r"PHMSA|[Hh]azmat|49 CFR Part 172|49 CFR 172"),
    ("Dam safety (FERC)", r"FERC|18 CFR Part 12"),
    ("Gaming", r"Gaming|NIGC|[Cc]asino"),
    ("Employment records", r"Form I-9|E-Verify|FCRA|Local Law 144"),
    ("DOJ bulk data rule", r"DOJ Data Security|bulk sensitive|PADFA"),
]

# One plain-English line per project, shown in the guided tour.
PROJECT_PLAIN = {
    "P05": "Before protecting anything, list what the business does and how long each activity can stop before real harm. Those downtime limits decide what gets fixed first.",
    "P02": "Pick the one system the business cannot live without, draw a line around it, and write down how each security control works there today.",
    "P04": "Show which parts of that system run in the cloud or in vendor services, and who is responsible for each control: the company or the provider.",
    "P01": "List what could realistically go wrong, rate how likely and how harmful each event is with NIST tables, and assign an owner and a fix date.",
    "P03": "Take the main law or standard that applies, check every requirement line by line, and mark it Met, Partially met, or Not met with evidence.",
    "P06": "Turn the gaps into five short written policies people can follow: security program, access, incidents, data handling, and acceptable use.",
    "P07": "Test whether controls actually work by examining documents, interviewing staff, and testing systems. Failures go on a plan of action (POA&M).",
    "P08": "Write the playbook for the most likely bad day, with the legal deadlines for telling regulators, customers, and the public.",
    "P09": "Check readiness for a SOC 2 audit, the report customers and partners ask for to prove controls work.",
    "P10": "List where AI is used, rate the risk of each use with the NIST AI Risk Management Framework, and decide: approve, restrict, or stop.",
}


def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def all_rows(folder, stem):
    """The main CSV plus any division files (Multi-Sector samples split some registers)."""
    out = []
    for p in sorted(folder.glob(f"{stem}*.csv")):
        if p.stem == stem or p.stem.startswith(stem + "-"):
            out += rows(p)
    return out


def sections(text):
    """Split markdown into {heading text without number: body} for ## headings."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(?:\d+\.\s*)?(.+?)\s*$", line)
        if m and not line.startswith("###"):
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def find(secs, prefix):
    for k, v in secs.items():
        if k.lower().startswith(prefix.lower()):
            return k, v
    return None, ""


def strip_md(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"[*_`]", "", s).strip()


def first_table(md):
    lines = [l for l in md.splitlines() if l.startswith("|")]
    if len(lines) < 2:
        return [], []
    split = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
    head = split(lines[0])
    body = [split(l) for l in lines[2:]]
    return head, body


def git_link(base_dir, target):
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return target
    p = (base_dir / target.split("#")[0]).resolve()
    try:
        rel = p.relative_to(ROOT).as_posix()
    except ValueError:
        return target
    return REPO + rel


def inline(s, base_dir):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{html.escape(git_link(base_dir, html.unescape(m.group(2))))}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    return s


def md_to_html(md, base_dir):
    """Small markdown converter for the sections the explorer shows: paragraphs, lists, tables, h3/h4."""
    out, para, i = [], [], 0
    lines = md.splitlines()

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), base_dir) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            flush(); i += 1; continue
        if line.startswith("<!--"):
            i += 1; continue
        m = re.match(r"^(#{3,6})\s+(.*)", line)
        if m:
            flush(); out.append(f"<h4>{inline(m.group(2), base_dir)}</h4>"); i += 1; continue
        if line.startswith("|"):
            flush()
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            head, body = first_table("\n".join(block))
            t = ['<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c, base_dir)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c, base_dir)}</td>" for c in r) + "</tr>")
            out.append("".join(t) + "</tbody></table></div>")
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if m:
            flush()
            # collect the list block, nesting by indent (two levels is enough here)
            items = []
            while i < len(lines):
                m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", lines[i])
                if m:
                    items.append([len(m.group(1)), m.group(2)[0].isdigit(), m.group(3)])
                elif lines[i].startswith("  ") and lines[i].strip() and items:
                    items[-1][2] += " " + lines[i].strip()
                else:
                    break
                i += 1
            base = items[0][0]
            tag = "ol" if items[0][1] else "ul"
            buf, sub = [f"<{tag}>"], None
            for ind, num, text in items:
                if ind > base:
                    if sub is None:
                        sub = "ol" if num else "ul"
                        buf[-1] = buf[-1].removesuffix("</li>") + f"<{sub}>"
                    buf.append(f"<li>{inline(text, base_dir)}</li>")
                else:
                    if sub:
                        buf.append(f"</{sub}></li>"); sub = None
                    buf.append(f"<li>{inline(text, base_dir)}</li>")
            if sub:
                buf.append(f"</{sub}></li>")
            buf.append(f"</{tag}>")
            out.append("".join(buf))
            continue
        if line.startswith(">"):
            flush(); out.append(f"<blockquote>{inline(line.lstrip('> '), base_dir)}</blockquote>"); i += 1; continue
        para.append(line.strip()); i += 1
    flush()
    return "\n".join(out)


def count(items, key, order):
    c = {k: 0 for k in order}
    for r in items:
        v = (r.get(key) or "").strip()
        v = "Not applicable" if v in ("N/A", "Not applicable") else v
        if v in c:
            c[v] += 1
    return c


def applies(v):
    v = (v or "").strip().lower()
    return v.startswith("yes") or v.startswith("applies")


def tags_for(gap, notif):
    text = [r.get("regulation", "") for r in gap if applies(r.get("applies_at_this_tier")) and r.get("status") != "Not applicable"]
    text += [r.get("obligation", "") + " " + r.get("citation", "") for r in notif if applies(r.get("applies_at_this_tier"))]
    blob = "\n".join(text)
    return [name for name, rx in TAGS if re.search(rx, blob)]


def glance(readme):
    out = {}
    for line in readme.splitlines():
        m = re.match(r"^\| ([^|]+?) \| (.+?) \|$", line)
        if m and m.group(1) not in ("", "Requirement", "Step", "---"):
            out[m.group(1)] = strip_md(m.group(2))
        if line.startswith("## What the business handles"):
            break
    return out


def sample(folder):
    unit = folder.parent.name
    tier = int(folder.name.split("_")[0].split("-")[1])
    readme = (folder / "README.md").read_text(encoding="utf-8")
    title = readme.splitlines()[1]
    _, industry, rest = [x.strip() for x in title.lstrip("# ").split("|")]
    business = rest.split(":", 1)[1].strip()
    one = next((strip_md(l[1:]) for l in readme.splitlines() if l.startswith("> Cris")), "")
    g = glance(readme)
    rel = folder.relative_to(ROOT).as_posix()
    step = {p.name.split("_")[1]: p for p in folder.glob("step-*")}

    facts = (folder / "00_company-facts.md").read_text(encoding="utf-8")
    fs = sections(facts)
    _, org = find(fs, "The organization")
    _, sysmd = find(fs, "Systems")
    post_h, post = find(fs, "Current security posture")
    _, scen = find(fs, "Scenario choices")
    head, body = first_table(sysmd)
    ci = next((i for i, h in enumerate(head) if h.lower() == "system"), 1)
    systems = [[strip_md(r[0]), strip_md(r[ci])] for r in body if len(r) > ci]
    _, sbody = first_table(scen)
    scenario = [[strip_md(r[0]), strip_md(r[1])] for r in sbody if len(r) > 1]

    # P05 BIA
    bia = rows(step["P05"] / "bia.csv")
    def prio(r):
        try:
            return float(re.findall(r"[\d.]+", r.get("recovery_priority") or "99")[0])
        except IndexError:
            return 99
    bia_top = [[r["business_process"], r.get("rto_hours", ""), r.get("rpo_hours", ""), r.get("overall_criticality", "")]
               for r in sorted(bia, key=prio)[:5]]

    # P02 SSP
    ssp = rows(step["P02"] / "control-implementation.csv")
    ssp_status = {}
    for r in ssp:
        k = (r.get("implementation_status") or "").split("(")[0].split(";")[0].strip() or "Unstated"
        ssp_status[k] = ssp_status.get(k, 0) + 1

    # P04 cloud
    cloud = rows(step["P04"] / "cloud-control-map.csv")
    resp = {}
    for r in cloud:
        k = (r.get("responsibility") or "").split("(")[0].split(";")[0].strip() or "Unstated"
        resp[k] = resp.get(k, 0) + 1
    components = len({r.get("component") for r in cloud})

    # P01 risk
    risks = all_rows(step["P01"], "risk-register")
    rc = count(risks, "risk_level", LEVELS)
    top = [r for r in risks if r.get("risk_level") in ("Very High", "High")]
    top.sort(key=lambda r: LEVELS.index(r["risk_level"]))
    top_risks = [[r["risk_id"], r["threat_event"], r["risk_level"], r.get("treatment_plan") or r.get("treatment", ""),
                  r.get("owner", ""), r.get("due_date", "")] for r in top[:8]]
    if not top_risks:
        mods = [r for r in risks if r.get("risk_level") == "Moderate"][:5]
        top_risks = [[r["risk_id"], r["threat_event"], r["risk_level"], r.get("treatment_plan") or r.get("treatment", ""),
                      r.get("owner", ""), r.get("due_date", "")] for r in mods]

    # P03 gap
    gap = all_rows(step["P03"], "gap-analysis")
    gc = count(gap, "status", ["Met", "Partially met", "Not met", "Not applicable"])
    gr = (step["P03"] / "gap-analysis-report.md").read_text(encoding="utf-8")
    m = re.search(r"^\| Regulations? analyzed \| (.+?) \|$", gr, re.M)
    rule = strip_md(m.group(1)) if m else ""
    m = re.search(r"Regulation: ([^|]+?)\.? \|", readme)
    rule_short = strip_md(m.group(1)) if m else rule
    _, appl = find(sections(gr), "Applicability")

    # P06 policies
    pols = []
    for p in sorted(step["P06"].glob("POL-*.md")):
        t = next((l[2:].strip() for l in p.read_text(encoding="utf-8").splitlines() if l.startswith("# ")), p.stem)
        pols.append([t, f"{p.parent.name}/{p.name}"])

    # P07 assessment
    res = rows(step["P07"] / "assessment-results.csv")
    poam = rows(step["P07"] / "poam.csv")
    p07 = {
        "controls": len({r.get("control_id") for r in res}),
        "objectives": len(res),
        "sat": sum(r.get("finding") == "Satisfied" for r in res),
        "other": sum(r.get("finding") == "Other than satisfied" for r in res),
        "poam": len(poam),
        "poamHigh": [[r["poam_id"], r["weakness"], r.get("scheduled_completion", "")] for r in poam if r.get("risk_level") in ("High", "Very High")][:6],
    }

    # P08 incident
    rb = (step["P08"] / "ir-runbook.md").read_text(encoding="utf-8")
    incident = strip_md(rb.splitlines()[0].lstrip("# ").split(":", 1)[-1])
    notif = rows(step["P08"] / "notification-matrix.csv")
    clocks = [[r["obligation"], r.get("deadline", ""), r.get("notify", "")] for r in notif if applies(r.get("applies_at_this_tier"))]

    # P09 SOC 2
    soc = rows(step["P09"] / "soc2-readiness.csv")
    sc = count(soc, "readiness_status", ["Ready", "Partially ready", "Not ready", "Not applicable"])

    # P10 AI
    ai = rows(step["P10"] / "ai-use-case-inventory.csv")
    use_cases = [[r["use_case_id"], r["use_case"], r.get("risk_tier", ""), r.get("status", "")] for r in ai]
    ar = (step["P10"] / "ai-risk-assessment.md").read_text(encoding="utf-8")
    _, dec = find(sections(ar), "Decision")
    ai_title = strip_md(ar.splitlines()[0].lstrip("# ").split(":", 1)[-1])

    # Links are stored relative to the sample folder; the page adds the GitHub prefix.
    links = []
    for p in sorted(folder.glob("step-*")):
        files = [f.name for f in sorted(p.iterdir()) if f.suffix in (".md", ".csv") and f.name != "_context.md"]
        links.append([p.name, files])

    return {
        "id": f"{unit}/{folder.name}", "unit": unit, "tier": tier, "industry": industry, "business": business,
        "path": rel,
        "one": one, "glance": {k: g[k] for k in ("Legal name", "Legal form", "Ownership", "Employees", "Annual receipts (fictional)", "Total assets (fictional)",
                                                   "Primary industry", "Primary system", "IT footprint",
                                                   "Who owns security and compliance") if k in g},
        "org": md_to_html(org, folder), "systems": systems, "scenario": scenario,
        "postureTitle": strip_md(post_h.split(":", 1)[1]) if post_h and ":" in post_h else "",
        "posture": md_to_html(post, folder),
        "tags": tags_for(gap, notif), "rule": rule_short, "ruleFull": rule,
        "bia": {"count": len(bia), "top": bia_top},
        "ssp": {"system": g.get("Primary system", ""), "controls": len(ssp), "status": ssp_status},
        "cloud": {"rows": len(cloud), "components": components, "resp": resp},
        "risk": {"counts": rc, "total": len(risks), "top": top_risks},
        "gap": {"counts": gc, "total": len(gap), "appl": md_to_html(appl, step["P03"])},
        "policies": pols, "p07": p07,
        "p08": {"incident": incident, "clocks": clocks[:12], "clockCount": len(clocks)},
        "p09": sc, "ai": {"title": ai_title, "uses": use_cases, "decision": md_to_html(dec, step["P10"])},
        "links": links,
    }


def unit_label(unit, industry, parents):
    """Critical-infrastructure folders sit under their parent industry; show them that way."""
    if "_" in unit:
        return parents.get(unit.split("_")[0], ""), True
    return industry, False


def main():
    folders = sorted(p for p in S.glob("*/size-*") if (p / "00_company-facts.md").exists())
    data = [sample(p) for p in folders]
    parents = {d["unit"]: d["industry"] for d in data if "_" not in d["unit"]}
    units = []
    for unit in sorted({d["unit"] for d in data}, key=lambda u: (u.split("_")[0], "_" in u, u)):
        d0 = next(d for d in data if d["unit"] == unit)
        parent, is_ci = unit_label(unit, d0["industry"], parents)
        units.append({"unit": unit, "name": d0["industry"], "parent": parent, "ci": is_ci})
    projects = sorted(rows(ROOT / "00_universal-framework" / "projects" / "projects.csv"), key=lambda r: int(r["build_step"]))
    projects = [{"id": r["project_id"], "step": int(r["build_step"]), "name": r["name"], "buildsOn": r["builds_on"],
                 "plain": PROJECT_PLAIN[r["project_id"]]} for r in projects]
    payload = json.dumps({"units": units, "samples": data, "tiers": TIERS, "projects": projects,
                          "tagList": [t for t, _ in TAGS], "repo": REPO},
                         ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    # One shared data file feeds all three reading modes.
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text("window.GRC_DATA=" + payload + ";\n", encoding="utf-8")
    risks = sum(d["risk"]["total"] for d in data)
    stats = {"__COMPANIES__": f"{len(data)}", "__INDUSTRIES__": f"{len(units)}", "__RISKS__": f"{risks:,}",
             "__DELIVERABLES__": f"{len(data) * 10:,}"}
    for template, out in PAGES:
        text = (ROOT / "tools" / template).read_text(encoding="utf-8")
        for k, v in stats.items():
            text = text.replace(k, v)
        (ROOT / "docs" / out).write_text(text, encoding="utf-8")
    print(f"Wrote docs/assets/grc-data.js ({DATA.stat().st_size / 1e6:.2f} MB, {len(data)} companies) and "
          + ", ".join(f"docs/{o}" for _, o in PAGES))

if __name__ == "__main__":
    main()
