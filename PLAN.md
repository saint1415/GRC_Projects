# Plan: Completing the GRC Project List for Cris Santos Company

**Status as of 2026-09-26:** Phases 0 to 4 are complete: 41 finished samples (410 deliverables), each validated. Health Care is finished at all six sizes, and every one of the 36 verticals (NAICS sectors and CISA sectors) is finished at Small. Phase 5 (remaining tier and vertical combinations) is optional.

---

## 1. Decisions this plan is built on

| Topic | Decision | Authority |
|---|---|---|
| Company | One fictitious company, **Cris Santos Company** | Your choice |
| Projects | The 10 projects on the GRC Project List, framed universally (for example, "HIPAA Gap Analysis" becomes "Regulatory Gap Analysis", with HIPAA as the Health Care instance) | [Notion list](https://nicoleenesse.notion.site/GRC-Project-List-3bf8eef497be8080afc3ee1cbd34bf68) |
| Universal anchor | NIST CSF 2.0 (macro) and NIST SP 800-53 Rev. 5, Release 5.2.0 (granular) | NIST |
| Verticals | All 20 NAICS 2022 sectors as parents. All 16 CISA critical infrastructure sectors nested under their primary NAICS parent. 36 in total | Census (NAICS 2022); CISA (NSM-22) |
| Industry per vertical | One primary 6-digit NAICS industry per vertical, chosen for GRC relevance, stored in one editable CSV. Tier-specific substitutions where the primary industry is implausible at that size | `02_industry-rules/verticals.csv`, `scenario-industry-overrides.csv` |
| Size tiers | Six parallel, independent tiers: Sole Proprietorship, Micro, Small, Mid-Market, Enterprise, Multi-Sector | IRS; Census Nonemployer and SUSB; SBA 13 CFR 121.201 |
| Jurisdiction | United States only | Your choice |
| Formats | Markdown and CSV. Word and PDF exports can be generated later for meetings | Your choice |
| Matrix | All 216 scenario folders physically created, but generated from the layers so a regulation change updates every one | Your choice |

---

## 2. Architecture: macro to granular

| Level | What it is | Where | Example |
|---|---|---|---|
| L0 Universal | Frameworks, crosswalks, sources, cross-sector law, 10 methods and templates | `00_universal-framework/` | P01 method uses NIST SP 800-30 Tables G-5 and I-2 |
| L1 Company size | Size definition plus how deep each project goes at that size | `01_company-sizes/` | Small: 25-40 risks, semi-quantitative scoring |
| L2 Industry | Sector regulators, requirements, notification rules, data, systems | `02_industry-rules/<industry>/` (critical infrastructure sectors are named `<industry>_<sector>-critical-infrastructure`) | Health Care: HIPAA Security Rule, 60-day breach notice |
| L3 Sample company | One size x one industry: meeting brief, company facts, and 10 project folders | `03_company-samples/<industry>/size-<n>_<size>_<business>/` | `health-care/size-3_small_multi-specialty-practice/` |
| L4 Project | One of the 10 projects, numbered by build step and Notion project number (`_context.md` explains it) | `.../step-04_P01_risk-register/` | Scope, regulatory drivers, pre-filled notification duties |
| L5 Artifact | The working files you complete | `.../risk-register.csv` | Individual risks, controls, evidence |

Every artifact traces upward. Each row cites a `regulatory_driver` ID (L2), CSF 2.0 and SP 800-53 IDs (L0), and follows the depth set for its tier (L1).

---

## 3. Order of work inside any sample company

The Notion list orders projects by career value. Building them in **dependency order** lets each deliverable reuse the last, so project folders are named `step-NN_PNN_<project>`. The full teaching guide, including where company size changes the work, is [docs/how-to-build-the-10-projects.md](docs/how-to-build-the-10-projects.md).

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
| **1. Flagship** (done) | **Health Care (NAICS 62), Small** | 10 completed deliverables | One end-to-end sample for meetings. It mirrors the Notion HIPAA project |
| **2. Scalability ladder** (done) | Health Care across all 6 tiers | 50 more (5 tiers x 10) | Shows the same method scaling from a sole practitioner to a multi-sector enterprise |
| **3. Named verticals** (done) | Small tier for Manufacturing (31-33), Wholesale (42), Retail (44-45), Transportation and Warehousing (48-49), Information/SaaS (51), Finance (52), Education (61), Defense Industrial Base (CISA) | 80 (8 x 10) | Covers the industries you named, including supply chain and federal/defense |
| **4. Full sector coverage** (done) | Small tier for every remaining vertical (27) | 270 | Every NAICS and CISA sector has at least one complete sample |
| **5. Full matrix** (optional) | Remaining tier x vertical combinations | Up to 1,750 more (2,160 total) | Complete library. Prioritize by meeting demand |

**Recommended sample for your first meeting:** `03_company-samples/health-care/size-3_small_multi-specialty-practice/`. Read its `README.md` first; [docs/meeting-guide.md](docs/meeting-guide.md) explains how to run the meeting from it.

### Phase 1 record (completed 2026-09-26)
| Item | Result |
|---|---|
| Sample | [`03_company-samples/health-care/size-3_small_multi-specialty-practice/`](03_company-samples/health-care/size-3_small_multi-specialty-practice/README.md), with shared facts in `00_company-facts.md` |
| Decisions confirmed with you | Florida location, with state law cited only where unavoidable; vendor-agnostic cloud; partially compliant posture; generic vendor names; role titles only; 2 clinics, 12 providers, ~18,000 patients; 42 CFR Part 2 excluded; SOC 2 as both a customer-assurance self-assessment and an EHR vendor report review |
| Reusable output for Phase 2 | `02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`: 69 HIPAA requirements from NIST SP 800-66r2 data, with an author mapping to CSF 2.0 and SP 800-53 |
| Headline results | 31 risks (3 High); 69 HIPAA requirements (10 met, 41 partially met, 11 not met, 7 N/A); 70 SSP controls; 164 SP 800-53A determination statements (57 satisfied); 21 POA&M items |
| Validation | `tools/validate.py` checks completed samples for unfinished markers and invalid CSF or SP 800-53 IDs |

### Phase 2 record (completed 2026-09-26)
| Size | Folder | Risks | HIPAA rows (met / partial / not met / N/A) | Controls assessed (statements) |
|---|---|---|---|---|
| Sole Proprietorship | [`size-1_sole-proprietor_solo-physician-practice`](03_company-samples/health-care/size-1_sole-proprietor_solo-physician-practice/README.md) | 15 | 14 / 33 / 15 / 7 | 10 (38) |
| Micro | [`size-2_micro_two-physician-primary-care-office`](03_company-samples/health-care/size-2_micro_two-physician-primary-care-office/README.md) | 23 | 10 / 34 / 18 / 7 | 13 (91) |
| Small (Phase 1) | [`size-3_small_multi-specialty-practice`](03_company-samples/health-care/size-3_small_multi-specialty-practice/README.md) | 31 | 10 / 41 / 11 / 7 | 22 (164) |
| Mid-Market | [`size-4_mid-market_physician-group-with-surgery-center`](03_company-samples/health-care/size-4_mid-market_physician-group-with-surgery-center/README.md) | 50 | 24 / 57 / 2 / 7 (90 rows incl. breach and ASC) | 34 (242) |
| Enterprise | [`size-5_enterprise_large-medical-group`](03_company-samples/health-care/size-5_enterprise_large-medical-group/README.md) | 65 | 63 / 41 / 0 / 9 (113 rows, all regimes) | 44 (263) |
| Multi-Sector | [`size-6_multi-sector_care-delivery-health-plan-and-saas`](03_company-samples/health-care/size-6_multi-sector_care-delivery-health-plan-and-saas/README.md) | 87 (group + 3 divisions) | Care Delivery 44 / 18 / 0 / 7, plus Health Plan and SaaS tables | 39 (261) |

**Decisions confirmed with you:**
- Maturity realistic by size.
- Florida headquarters with multi-state operations for Enterprise and Multi-Sector (state law handled generically).
- Multi-Sector divisions: a health plan and a health-tech SaaS.
- Specialty mix scaled from the Phase 1 practice.

**Official NIST HIPAA mapping obtained:** OLIR 110 and 109 were added to the Health Care vertical and shown in every P03 gap analysis (see `02_industry-rules/health-care/hipaa-crosswalk-README.md`).

### Phase 3 record (completed 2026-09-26)
All Small tier, Florida, partially compliant.

| Vertical | Business | P03 regulation | Risks (High+) | P07 controls (statements) |
|---|---|---|---|---|
| Manufacturing (31-33) | Connected medical device maker | FD&C Act 524B and FDA guidance (Feb. 3, 2026) | 32 (5) | 22 (129) |
| Defense Industrial Base (CISA) | Aircraft parts maker with CUI | NIST SP 800-171 Rev. 2 (110 requirements), CMMC Level 2 | 32 (7) | 20 (131) |
| Wholesale (42) | IT distributor, supply chain focus | SP 800-171 Rev. 2 for the CUI stream, FAR 52.204-21, C-SCRM | 35 (9) | 25 (130) |
| Retail (44-45) | One-store grocery with online ordering | PCI DSS v4.0.1 | 32 (3) | 22 (149) |
| Transportation (48-49) | Marine cargo terminal | USCG 33 CFR 101 Subpart F | 33 (4) | 24 (155) |
| Information (51) | Workforce scheduling SaaS | SOC 2 TSC with FTC Act Section 5 | 34 (4) | 23 (164) |
| Finance (52) | Cris Santos Bank, N.A. (OCC) | 12 CFR 30 App. B and 12 CFR 53 | 32 (5) | 21 (153) |
| Education (61) | Private career college (Title IV) | FTC Safeguards Rule 16 CFR 314 and FERPA | 33 (4) | 24 (164) |

**Decisions confirmed with you:**
- SaaS gap target is SOC 2 plus the FTC Act, with the CCPA as an applicability check only.
- All eight companies are in Florida.
- The bank has a national (OCC) charter.
- The grocery has no pharmacy.

**Regulatory changes found and verified:**
- FDA reissued its premarket cybersecurity guidance on 2026-02-03.
- CFPB amended Regulation B, effective 2026-07-21, so the "effects test" no longer applies (12 CFR 1002.6(a)).

### Phase 4 record (completed 2026-09-26)
All Small tier, Florida, partially compliant. Each P03 starts with an applicability check: does the sector rule actually bind a company of this size? Where it does not, the sample says so with the citation and uses the closest binding rule or a voluntary benchmark.

| Vertical | Business | P03 finding (primary rule) | Risks (High+) | P07 controls (statements) |
|---|---|---|---|---|
| Agriculture (11) | Diversified crop farm | FSMA 21 CFR 121 does not apply (farms exempt); NIST CSF 2.0 benchmark with SP 800-82r3 for irrigation OT; Produce Safety Rule records secondary | 32 (4) | 21 (179) |
| Food and Agriculture (CISA) | Meat processor | FSMA Intentional Adulteration rule applies (21 CFR 121) | 32 (7) | 22 (182) |
| Mining, oil and gas (21) | Onshore crude producer | TSA pipeline directives, USCG MTS rule and PHMSA Part 195 do not apply; CSF 2.0 with SP 800-82r3 | 32 (3) | 21 (191) |
| Utilities (22) | Electric distribution utility | NERC CIP-003-9 low impact applies to 8 relays; DOE-417 reporting | 31 (4) | 22 (154) |
| Energy (CISA) | Intrastate gas transmission pipeline | TSA SD 02G not applicable (not designated); 49 CFR 192.631 applies | 31 (5) | 21 (195) |
| Water (CISA) | Community water system | SDWA section 1433 (AWIA) applies | 32 (5) | 20 (175) |
| Dams (CISA) | Small hydroelectric project | FERC Security Program, Security Group 2, Section 9 at Critical level | 33 (5) | 22 (176) |
| Nuclear (CISA) | Radioactive waste processor | 10 CFR 73.54 does not apply (not a reactor); 10 CFR Part 37 via Florida license | 32 (5) | 20 (141) |
| Construction (23) | Federal general contractor | FAR 52.204-21 applies now; CMMC Level 1 on next DoD award | 34 (4) | 23 (153) |
| Chemical (CISA) | Specialty chemical formulator | CFATS lapsed (voluntary benchmark); EPA RMP Program 2 applies; OSHA PSM does not | 33 (4) | 22 (181) |
| Critical Manufacturing (CISA) | Transformer manufacturer | No binding sector rule; NERC CIP-013 by utility contract; FAR clauses on one federal contract | 34 (8) | 22 (164) |
| Transportation Systems (CISA) | Class III short line railroad | TSA rail directives not applicable; 49 CFR 1570 and 1580 subpart C apply | 32 (4) | 22 (184) |
| Communications (CISA) | Regional broadband and voice carrier | FCC CPNI rules reach voice only (broadband is an information service after Ohio Telecom, 6th Cir. 2025) | 34 (6) | 20 (140) |
| Information Technology (CISA) | Cloud hosting provider | FedRAMP not yet applicable (readiness); bank service provider rule applies | 32 (7) | 22 (185) |
| Financial Services (CISA) | Payment processor | PCI DSS v4.0.1 service provider (Visa Level 1); FTC Safeguards Rule; 12 CFR 53.4 via sponsor bank | 31 (5) | 21 (130) |
| Real estate (53) | Residential brokerage with closing services | FTC Safeguards Rule applies through settlement work only | 34 (3) | 22 (141) |
| Commercial Facilities (CISA) | Office and retail property owner | CISA CPGs voluntary; PCI by contract (SAQ P2PE); FTC Act and Fla. Stat. 501.171 binding | 34 (3) | 22 (167) |
| Professional services (54) | CPA and tax firm | FTC Safeguards Rule applies (no 314.6 exemption); IRC 7216 | 33 (5) | 22 (125) |
| Management of companies (55) | Holding company | NIST CSF 2.0 group profile; SEC Item 106 not applicable (private) | 32 (4) | 22 (155) |
| Admin and support (56) | Staffing firm | CSF 2.0 benchmark; Form I-9, FCRA, Fla. Stat. 448.095 binding | 35 (3) | 22 (156) |
| Healthcare and Public Health (CISA) | 12-bed critical access hospital | HIPAA Security Rule; CMS 42 CFR 485.625 | 33 (5) | 22 (186) |
| Arts and entertainment (71) | Live event venue | PCI DSS v4.0.1 merchant; BOTS Act and FTC fee rule for P10 | 34 (5) | 21 (140) |
| Accommodation (72) | Independent hotel | PCI DSS v4.0.1 (SAQ D rooms, SAQ P2PE restaurant) | 31 (5) | 23 (156) |
| Other services (81) | Device repair | CSF 2.0 benchmark; FTC Act and Fla. Stat. 501.171 binding | 31 (4) | 23 (158) |
| Public administration (92) | GovTech integrator | SP 800-53 Moderate by contract; CJIS and IRS Pub. 1075 flow-down | 32 (6) | 20 (132) |
| Government Services and Facilities (CISA) | Facilities support contractor | SP 800-53 Moderate by state contract; FAR clauses; GSA building technologies guide | 33 (4) | 22 (163) |
| Emergency Services (CISA) | Private ambulance | HIPAA applies; CJIS does not | 33 (5) | 22 (163) |

**Decisions confirmed with you:**
- Payment processor gap target is PCI DSS as a service provider, kept national rather than state-specific.
- Holding company uses a NIST CSF 2.0 group profile.
- All 27 companies are in Florida.

**Corrections made during the phase:**
- Fla. Stat. 501.171(3)(a): the 15-day good-cause extension applies to notice to individuals, not to the Department of Legal Affairs notice. Fixed in 10 earlier sample files after checking the statute text.
- Utilities and Energy vertical notification rows: DOE Form OE-417 renamed DOE-417 and verified against OMB ICR 202402-1901-002.

**Regulatory status verified during the phase:**
- FinCEN residential real estate rule (31 CFR 1031.320) vacated 2026-03-19 (E.D. Tex.); FinCEN has appealed.
- FCC 2023 breach amendments to 47 CFR 64.2011 upheld by the Sixth Circuit (2025-08-13) but still without an effective date.
- CFATS authority still lapsed since 2023-07-28.
- TSA surface cyber NPRM (89 FR 88488) and CIRCIA still proposed.

---

## 5. Keeping it current (the isolated universal layer)

**Routine:** review quarterly. Run the refresh tools, re-check every row marked `verified=false`, and update `last_verified` in the source register. See [docs/how-to-update.md](docs/how-to-update.md).

**Watch list** (verified 2026-09-25). Each item would change the layers:

| Item | Status | Affects |
|---|---|---|
| HIPAA Security Rule NPRM (90 FR 898) | Proposed Jan 2025; regulatory agenda projects a final rule July 2027 | Health Care P03, P06, P07 |
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
| NIST SP 800-82 Rev. 4 (OT security guide) | Initial public draft published 2026-09-21; Rev. 3 remains final | OT samples (utilities, water, dams, energy, manufacturing, transportation) |
| NIST SP 800-60 Rev. 2 | Working draft | P02 categorization |
| New state privacy laws | Oklahoma, Louisiana (2027-01-01), Alabama (2027-05-01), Vermont (2028-01-01) | Cross-sector |
| FBI CJIS Security Policy | v6.1 (2026-06-25) is current; 1-hour incident reporting | Public Administration, Emergency Services |
| FinCEN residential real estate rule (31 CFR 1031.320) | Vacated 2026-03-19; government appeal to the Fifth Circuit pending | Real estate P03, P08 |
| FCC CPNI breach amendments (47 CFR 64.2011) | Upheld 2025-08-13; effective date not yet announced | Communications P03, P08 |
| CFATS reauthorization | Lapsed since 2023-07-28 | Chemical P03 |
| TSA surface cyber NPRM (89 FR 88488) | Proposed Nov 2024; not final | Transportation, Energy |
| NSM-22 review (EO 14239) | Under review; still in effect | CISA sector list |

---

## 6. Open items

1. **Unverified research rows.** A small number of vertical rows are marked `verified=false`. `tools/validate.py` counts them. Confirm each against its source before using it in a deliverable.
2. **Industry picks.** The 36 primary industries and 22 tier substitutions are proposals in two CSVs. Change any pick and rebuild.
3. **Office formats.** If you want Word or PDF versions of a finished sample for a meeting, that is a later export step.
