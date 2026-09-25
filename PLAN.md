# Plan: Completing the GRC Project List for Cris Santos Company

**Status as of 2026-09-25:** Phase 0 (foundation) is complete. The universal framework, tiers, verticals, generator, and all 216 scenario scaffolds exist. Phases 1-5 fill in the deliverables.

---

## 1. Decisions this plan is built on

| Topic | Decision | Authority |
|---|---|---|
| Company | One fictitious company, **Cris Santos Company** | Your choice |
| Projects | The 10 projects on the GRC Project List, framed universally (for example, "HIPAA Gap Analysis" becomes "Regulatory Gap Analysis", with HIPAA as the Health Care instance) | [Notion list](https://nicoleenesse.notion.site/GRC-Project-List-3bf8eef497be8080afc3ee1cbd34bf68) |
| Universal anchor | NIST CSF 2.0 (macro) and NIST SP 800-53 Rev. 5, Release 5.2.0 (granular) | NIST |
| Verticals | All 20 NAICS 2022 sectors as parents. All 16 CISA critical infrastructure sectors nested under their primary NAICS parent. 36 in total | Census (NAICS 2022); CISA (NSM-22) |
| Industry per vertical | One primary 6-digit NAICS industry per vertical, chosen for GRC relevance, stored in one editable CSV. Tier-specific substitutions where the primary industry is implausible at that size | `02_verticals/verticals.csv`, `scenario-industry-overrides.csv` |
| Size tiers | Six parallel, independent tiers: Sole Proprietorship, Micro, Small, Mid-Market, Enterprise, Multi-Sector | IRS; Census Nonemployer and SUSB; SBA 13 CFR 121.201 |
| Jurisdiction | United States only | Your choice |
| Formats | Markdown and CSV. Word and PDF exports can be generated later for meetings | Your choice |
| Matrix | All 216 scenario folders physically created, but generated from the layers so a regulation change updates every one | Your choice |

---

## 2. Architecture: macro to granular

| Level | What it is | Where | Example |
|---|---|---|---|
| L0 Universal | Frameworks, crosswalks, sources, cross-sector law, 10 methods and templates | `00_universal/` | P01 method uses NIST SP 800-30 Tables G-5 and I-2 |
| L1 Tier | Size definition plus how deep each project goes at that size | `01_tiers/` | Small: 25-40 risks, semi-quantitative scoring |
| L2 Vertical | Sector regulators, requirements, notification rules, data, systems | `02_verticals/<NAICS>/<CISA>/` | Health Care: HIPAA Security Rule, 60-day breach notice |
| L3 Scenario | One tier x one vertical: meeting brief plus 10 project folders | `03_scenarios/<NAICS>/[<CISA>/]<tier>/` | Health Care, Small: 60-employee physician practice |
| L4 Project | What the deliverable means in that scenario (`_context.md`) | `.../P01_risk-register/` | Scope, regulatory drivers, pre-filled notification duties |
| L5 Artifact | The working files you complete | `.../risk-register.csv` | Individual risks, controls, evidence |

Every artifact traces upward. Each row cites a `regulatory_driver` ID (L2), CSF 2.0 and SP 800-53 IDs (L0), and follows the depth set for its tier (L1).

---

## 3. Order of work inside any scenario

The Notion list orders projects by career value. Building them in **dependency order** lets each deliverable reuse the last:

| Step | Project | Why here | Feeds |
|---|---|---|---|
| 1 | P05 Business Impact Analysis | Establishes what matters and how long it can be down | P01 impact, P02 availability, P08 recovery order |
| 2 | P02 System Security Plan | Fixes the system, boundary, and FIPS 199 category | P04, P07 |
| 3 | P04 Cloud Control Mapping | Places controls on the SSP boundary | P02 control table, P07 |
| 4 | P01 Risk Register | Scores threats against the system using BIA impact | P03, P06, P07 |
| 5 | P03 Regulatory Gap Analysis | Tests current state against the vertical's primary regulation | P01 (new risks), P06 |
| 6 | P06 Security Policy Set | Closes governance gaps found in P03 | P07 (criteria to test) |
| 7 | P07 Control Assessment | Tests controls against SSP statements and policies | POA&M, P01 |
| 8 | P08 Incident Response Runbook | Uses BIA recovery order and the pre-filled notification matrix | P01 |
| 9 | P09 SOC 2 Readiness | Reuses evidence from P02, P06, and P07 | Customer assurance |
| 10 | P10 AI Governance | Applies policies (P06) and the risk method (P01) to AI | P01 |

**Definition of done for a deliverable:**
- every `[FILL]` is replaced
- the quality checklist in the universal README passes
- every row cites its `regulatory_driver`
- `tools/validate.py` passes

---

## 4. Phases

| Phase | Scope | Deliverables | Outcome |
|---|---|---|---|
| **0. Foundation** (done) | Universal layer, tiers, 36 verticals, generator, validator, 216 scaffolds | Repository structure | Any scenario is ready to fill in |
| **1. Flagship** | **Health Care (NAICS 62), Small** | 10 completed deliverables | One end-to-end sample for meetings. It mirrors the Notion HIPAA project |
| **2. Scalability ladder** | Health Care across all 6 tiers | 50 more (5 tiers x 10) | Shows the same method scaling from a sole practitioner to a multi-sector enterprise |
| **3. Named verticals** | Small tier for Manufacturing (31-33), Wholesale (42), Retail (44-45), Transportation and Warehousing (48-49), Information/SaaS (51), Finance (52), Education (61), Defense Industrial Base (CISA) | 80 (8 x 10) | Covers the industries you named, including supply chain and federal/defense |
| **4. Full sector coverage** | Small tier for every remaining vertical (27) | 270 | Every NAICS and CISA sector has at least one complete sample |
| **5. Full matrix** (optional) | Remaining tier x vertical combinations | Up to 1,750 more (2,160 total) | Complete library. Prioritize by meeting demand |

**Recommended sample for your first meeting:** `03_scenarios/n62_health-care/t3_small/`. Read its `README.md` first; [docs/meeting-guide.md](docs/meeting-guide.md) explains how to run the meeting from it.

---

## 5. Keeping it current (the isolated universal layer)

**Routine:** review quarterly. Run the refresh tools, re-check every row marked `verified=false`, and update `last_verified` in the source register. See [docs/how-to-update.md](docs/how-to-update.md).

**Watch list** (verified 2026-09-25). Each item would change the layers:

| Item | Status | Affects |
|---|---|---|
| HIPAA Security Rule NPRM (90 FR 898) | Proposed Jan 2025; still pending | Health Care P03, P06, P07 |
| CIRCIA final rule (6 CFR 226) | Targeted Sept 2026; not published | Cross-sector P08 notification baseline |
| FedRAMP Consolidated Rules 2026 | Mandatory 2027-01-01; no new Rev 5 certifications after 2027-06-11 | P02, P04 for federal-facing scenarios |
| CMMC phase-in | Phase 2 starts 2026-11-10 | Defense Industrial Base, Manufacturing, Construction |
| NIST AI RMF revision | In progress (AI Action Plan) | P10 |
| Colorado SB26-189 (ADMT) and CPPA ADMT rules | Both effective or compliance-due 2027-01-01 | P10, cross-sector |
| SBA size standards proposed rule | Proposed Aug 2026; comments to 2026-11-20 | Tier sizing (rerun `refresh_sba_standards.py` when final) |
| NAICS 2027 | Proposed by OMB July 2026 | Vertical codes |
| FAR overhaul (proposed Part 40, NIST SP 800-171 Rev. 3, 72-hour CUI reporting) | Proposed June 2026 | Federal contractor scenarios |
| NERC CIP future versions | Effective 2028-2029 | Utilities and Energy |
| TSA pipeline directives 01G and 02G | Expire 2027-01-15 and 2027-05-02 | Energy |
| NIST SP 800-60 Rev. 2 | Working draft | P02 categorization |
| New state privacy laws | Oklahoma, Louisiana (2027-01-01), Alabama (2027-05-01), Vermont (2028-01-01) | Cross-sector |
| NSM-22 review (EO 14239) | Under review; still in effect | CISA sector list |

---

## 6. Open items

1. **Unverified research rows.** A small number of vertical rows are marked `verified=false`. `tools/validate.py` counts them. Confirm each against its source before using it in a deliverable.
2. **Industry picks.** The 36 primary industries and 22 tier substitutions are proposals in two CSVs. Change any pick and rebuild.
3. **Office formats.** If you want Word or PDF versions of a finished sample for a meeting, that is a later export step.
