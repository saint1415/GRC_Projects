# Plan: Completing the GRC Project List for Cris Santos Company

**Status as of 2026-10-07:** All phases are complete. All 216 sample companies (36 industries x 6 sizes) are finished, 2,160 deliverables, and `tools/validate.py` reports 0 errors. Folder names are plain English (see the README).

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
| **5. Full matrix** (done) | Remaining size x industry combinations | 1,750 (175 x 10) | Complete library: every industry at every size |

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

### Phase 5 record (completed 2026-10-07)
Phase 5 filled every remaining cell of the matrix: the Sole Proprietorship, Micro, Mid-Market, Enterprise and Multi-Sector samples for the 35 industries other than Health Care (175 samples, 1,750 deliverables). With Phases 1 to 4, all **216 of 216** sample companies are finished.

**How it was built.** Batch 1 (2026-09-27) did the Manufacturing and Finance size ladders by hand review. The other 165 samples were built one company at a time by separate builders, up to 4 at once, each from a written brief and the shared rules below. Every sample passed `tools/check_sample.py` (P01 ratings recomputed from SP 800-30 Tables G-5 and I-2, every P07 statement matched word for word to the SP 800-53A catalog, no em dashes) and `tools/validate.py` before it got its own commit. Builders that stopped at a usage limit were restarted with a resume note: re-check the work already in the folder, keep what is correct, finish the rest. Facts a builder added while working are recorded in section 7 of each sample's `00_company-facts.md`.

**Final check (2026-10-07):** `tools/validate.py` reports 0 errors across 216 scenarios and 5,833 markdown files. The one warning is the 19 vertical rows still marked `verified=false` (see Open items). Across all 216 samples: 9,645 risks, of which 1,696 are High or Very High.

**Corrections made during Phase 5.** Each was found by a builder or a review, checked against the primary source, fixed in every affected file, and, where it could recur, added to the validator.

| Topic | What was wrong | Correct position (source) | Commits |
|---|---|---|---|
| FAR 52.204-23 (Kaspersky) report | Given a 1-business-day clock; source links pointed to the 52.204-25 page | 3 business days, then 10 business days (52.204-23(c)(2), eCFR 2026-09-23). Validator now flags both errors, in samples and in the shared layers | 03e9843, b367e21, 888df87, 68bfd08 |
| TSA security directives (rail, pipeline) | CISA report given as 24 hours | 72 hours, supplemental information within 24 hours of it becoming available (SD 1580-21-01E and SD Pipeline-2021-01G, Sec. II.C) | c5a6ea8 |
| DOE-417 | Attempted cyber compromise clock misstated in one sample | End of the next calendar day after determination (form OMB 1901-0288 instructions) | 3311aea |
| Florida 501.171 | 15-day extension described as covering all notices | It extends only the notice to individuals (501.171(4)(a)) | 833d5b0 |
| FAR overhaul | Described as creating "a new FAR part 40" | Proposed rule moves clauses into FAR Part 40; still proposed | 3263388 |
| Florida biometric data (501.702) | Face templates from camera video stated flatly as biometric data | The definition excludes "data generated from video or audio recordings", so this is unsettled; samples treat templates as biometric and send the question to counsel | 9881731 |
| E-Verify MOU | 3-business-day case rule cited as Art. II.A.7-8 | Art. II.A.9 (MOU for Employers, rev. 06/01/13). Validator now flags II.A.7-8 | 36f352b, 24e81b7, 38ec101 |
| README generator | Every Enterprise sample described as publicly traded; README showed registry defaults instead of each sample's own incident and AI use case | A sample's facts file now controls ownership wording, incident and AI use case | 5515e32, a50ccd2 |
| Completion test | A folder counted as done once its facts file existed | Done only when no template markers remain | 3de5e44 |

**Verified facts added to the shared builder rules** (so later samples stated them consistently): Florida Digital Bill of Rights controller test (over $1 billion revenue plus one of three activity tests, 501.702); the FTC fee rule citation (90 FR 2066, rule text at 2166); the FCC 2023 CPNI breach amendments are not yet in effect; the NIST SP 800-82 Rev. 4 initial public draft (2026-09-21); the 2026-06-09 DOJ Office of Legal Counsel opinion on Title VII disparate impact.

**Multi-Sector division pairings.** All 36 Multi-Sector samples are built. 33 of their pairings were proposals made for this project; they are marked "built (Phase 5), pairing open for review" in [`02_industry-rules/multi-sector-divisions.csv`](02_industry-rules/multi-sector-divisions.csv). Changing a pairing means rebuilding that one sample.

**Phase 5 samples.** Industry, size, business, the system documented in P02, risks in the P01 register(s) with the High or Very High count, and P07 determination statements. Each name links to the sample's README.

| Industry | Size | Business | Primary system (P02) | Risks (High or above) | P07 statements |
|---|---|---|---|---|---|
| Accommodation and Food Services | Sole Proprietor | [Bed-and-breakfast inn](03_company-samples/hotels-restaurants/size-1_sole-proprietor_bed-and-breakfast-inn/README.md) | Inn Business Systems Profile (IBSP) | 15 (3) | 47 |
| Accommodation and Food Services | Micro | [Small motel](03_company-samples/hotels-restaurants/size-2_micro_small-motel/README.md) | Motel Property Management and Point-of-Sale System (MPPS) | 23 (4) | 93 |
| Accommodation and Food Services | Mid-Market | [Hotel operator](03_company-samples/hotels-restaurants/size-4_mid-market_hotel-operator/README.md) | Property Management and Point-of-Sale Platform (PMPS) | 52 (13) | 206 |
| Accommodation and Food Services | Enterprise | [Hotel operator](03_company-samples/hotels-restaurants/size-5_enterprise_hotel-operator/README.md) | Property and Payment Platform (PPP) | 64 (15) | 256 |
| Accommodation and Food Services | Multi-Sector | [Hotel operator plus two divisions](03_company-samples/hotels-restaurants/size-6_multi-sector_hotel-operator-plus-two-divisions/README.md) | Hotel Property Management and Point-of-Sale Platform (PMPS) | 78 (13) | 270 |
| Administrative and Support and Waste Management and Remediation Services | Sole Proprietor | [Independent recruiter](03_company-samples/admin-support-services/size-1_sole-proprietor_independent-recruiter/README.md) | Recruiting and Placement Systems Profile (RPSP) | 15 (3) | 48 |
| Administrative and Support and Waste Management and Remediation Services | Micro | [Staffing firm](03_company-samples/admin-support-services/size-2_micro_staffing-firm/README.md) | Payroll and Applicant Tracking System (PATS) | 22 (3) | 81 |
| Administrative and Support and Waste Management and Remediation Services | Mid-Market | [Staffing firm](03_company-samples/admin-support-services/size-4_mid-market_staffing-firm/README.md) | Associate Payroll and Applicant Tracking Platform (APATP) | 52 (7) | 247 |
| Administrative and Support and Waste Management and Remediation Services | Enterprise | [Staffing firm](03_company-samples/admin-support-services/size-5_enterprise_staffing-firm/README.md) | Associate Lifecycle and Payroll Platform (ALPP) | 64 (12) | 280 |
| Administrative and Support and Waste Management and Remediation Services | Multi-Sector | [Staffing firm plus two divisions](03_company-samples/admin-support-services/size-6_multi-sector_staffing-firm-plus-two-divisions/README.md) | Group Workforce Platform (GWP) | 78 (12) | 266 |
| Agriculture, Forestry, Fishing and Hunting | Sole Proprietor | [Crop farm](03_company-samples/agriculture/size-1_sole-proprietor_crop-farm/README.md) | Farm Management and Irrigation Control Platform (FMICP) | 15 (3) | 51 |
| Agriculture, Forestry, Fishing and Hunting | Micro | [Crop farm](03_company-samples/agriculture/size-2_micro_crop-farm/README.md) | Farm Management and Irrigation Control Platform (FMICP) | 23 (3) | 102 |
| Agriculture, Forestry, Fishing and Hunting | Mid-Market | [Crop farm](03_company-samples/agriculture/size-4_mid-market_crop-farm/README.md) | Farm Management and Irrigation Control Platform (FMICP) | 50 (10) | 265 |
| Agriculture, Forestry, Fishing and Hunting | Enterprise | [Crop farm](03_company-samples/agriculture/size-5_enterprise_crop-farm/README.md) | Farm Management and Irrigation Control Platform (FMICP) | 65 (11) | 287 |
| Agriculture, Forestry, Fishing and Hunting | Multi-Sector | [Crop farm plus two divisions](03_company-samples/agriculture/size-6_multi-sector_crop-farm-plus-two-divisions/README.md) | Farm Management and Irrigation Control Platform (FMICP) | 86 (11) | 237 |
| Arts, Entertainment, and Recreation | Sole Proprietor | [Independent event promoter](03_company-samples/arts-entertainment-recreation/size-1_sole-proprietor_independent-event-promoter/README.md) | Ticketing and Venue Operations Platform (TVOP) | 15 (3) | 46 |
| Arts, Entertainment, and Recreation | Micro | [Live event venue](03_company-samples/arts-entertainment-recreation/size-2_micro_live-event-venue/README.md) | Ticketing and Venue Operations Platform (TVOP) | 23 (4) | 91 |
| Arts, Entertainment, and Recreation | Mid-Market | [Live event venue](03_company-samples/arts-entertainment-recreation/size-4_mid-market_live-event-venue/README.md) | Ticketing and Venue Operations Platform (TVOP) | 52 (10) | 238 |
| Arts, Entertainment, and Recreation | Enterprise | [Live event venue](03_company-samples/arts-entertainment-recreation/size-5_enterprise_live-event-venue/README.md) | Ticketing and Venue Operations Platform (TVOP) | 65 (14) | 256 |
| Arts, Entertainment, and Recreation | Multi-Sector | [Live event venue plus two divisions](03_company-samples/arts-entertainment-recreation/size-6_multi-sector_live-event-venue-plus-two-divisions/README.md) | Ticketing and Venue Operations Platform (TVOP) | 88 (13) | 275 |
| Chemical | Sole Proprietor | [Chemical distributor broker](03_company-samples/manufacturing_chemical-critical-infrastructure/size-1_sole-proprietor_chemical-distributor-broker/README.md) | Brokerage Core SaaS Stack | 15 (3) | 41 |
| Chemical | Micro | [Specialty chemical maker](03_company-samples/manufacturing_chemical-critical-infrastructure/size-2_micro_specialty-chemical-maker/README.md) | Blending and Business Platform (BBP) | 23 (3) | 99 |
| Chemical | Mid-Market | [Specialty chemical maker](03_company-samples/manufacturing_chemical-critical-infrastructure/size-4_mid-market_specialty-chemical-maker/README.md) | Process Control and Batch Management System (PCBMS) | 52 (10) | 260 |
| Chemical | Enterprise | [Specialty chemical maker](03_company-samples/manufacturing_chemical-critical-infrastructure/size-5_enterprise_specialty-chemical-maker/README.md) | Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS) | 64 (15) | 334 |
| Chemical | Multi-Sector | [Specialty chemical maker plus two divisions](03_company-samples/manufacturing_chemical-critical-infrastructure/size-6_multi-sector_specialty-chemical-maker-plus-two-divisions/README.md) | Plant C1 Process Control and Batch Management System (PCBMS) | 80 (16) | 281 |
| Commercial Facilities | Sole Proprietor | [Commercial property owner](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-1_sole-proprietor_commercial-property-owner/README.md) | Property Systems Profile (PSP) | 15 (3) | 52 |
| Commercial Facilities | Micro | [Commercial property owner](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-2_micro_commercial-property-owner/README.md) | Building Automation and Access Control System (BAACS) | 24 (4) | 103 |
| Commercial Facilities | Mid-Market | [Commercial property owner](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-4_mid-market_commercial-property-owner/README.md) | Building Automation and Access Control System (BAACS) | 50 (10) | 252 |
| Commercial Facilities | Enterprise | [Commercial property owner](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-5_enterprise_commercial-property-owner/README.md) | Building Automation and Access Control System (BAACS) | 65 (10) | 317 |
| Commercial Facilities | Multi-Sector | [Commercial property owner plus two divisions](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-6_multi-sector_commercial-property-owner-plus-two-divisions/README.md) | Group Building Automation and Access Control System (BAACS) | 78 (14) | 258 |
| Communications | Sole Proprietor | [Wireless internet provider](03_company-samples/information-software-media_communications-critical-infrastructure/size-1_sole-proprietor_wireless-internet-provider/README.md) | ISP Operations Systems Profile | 15 (3) | 45 |
| Communications | Micro | [Telecom carrier](03_company-samples/information-software-media_communications-critical-infrastructure/size-2_micro_telecom-carrier/README.md) | Network Operations and Customer Billing Platform (OSS/BSS) | 24 (4) | 93 |
| Communications | Mid-Market | [Telecom carrier](03_company-samples/information-software-media_communications-critical-infrastructure/size-4_mid-market_telecom-carrier/README.md) | Network Operations and Customer Billing Platform (OSS/BSS) | 51 (10) | 234 |
| Communications | Enterprise | [Telecom carrier](03_company-samples/information-software-media_communications-critical-infrastructure/size-5_enterprise_telecom-carrier/README.md) | Customer Billing and Network Operations Platform (OSS/BSS) | 64 (12) | 250 |
| Communications | Multi-Sector | [Telecom carrier plus two divisions](03_company-samples/information-software-media_communications-critical-infrastructure/size-6_multi-sector_telecom-carrier-plus-two-divisions/README.md) | Network Operations and Customer Billing Platform (OSS/BSS) | 74 (14) | 297 |
| Construction | Sole Proprietor | [Commercial general contractor](03_company-samples/construction/size-1_sole-proprietor_commercial-general-contractor/README.md) | Project Management and Payment Application System (PMPAS) | 15 (4) | 41 |
| Construction | Micro | [Commercial general contractor](03_company-samples/construction/size-2_micro_commercial-general-contractor/README.md) | Project and Payment System (PPS) | 24 (3) | 97 |
| Construction | Mid-Market | [Commercial general contractor](03_company-samples/construction/size-4_mid-market_commercial-general-contractor/README.md) | Project Delivery and Payment Platform (PDPP) | 52 (9) | 214 |
| Construction | Enterprise | [Commercial general contractor](03_company-samples/construction/size-5_enterprise_commercial-general-contractor/README.md) | Project Delivery and Payment Platform (PDPP) | 65 (14) | 263 |
| Construction | Multi-Sector | [Commercial general contractor plus two divisions](03_company-samples/construction/size-6_multi-sector_commercial-general-contractor-plus-two-divisions/README.md) | Project Delivery and Payment Platform (PDPP) | 86 (14) | 305 |
| Critical Manufacturing | Sole Proprietor | [Industrial equipment repair technician](03_company-samples/manufacturing_critical-manufacturing/size-1_sole-proprietor_industrial-equipment-repair-technician/README.md) | Field Service Business Systems (FSBS) | 15 (3) | 51 |
| Critical Manufacturing | Micro | [Transformer repair shop](03_company-samples/manufacturing_critical-manufacturing/size-2_micro_transformer-repair-shop/README.md) | ERP and Job Scheduling Platform (EJSP) | 24 (4) | 98 |
| Critical Manufacturing | Mid-Market | [Power transformer manufacturer](03_company-samples/manufacturing_critical-manufacturing/size-4_mid-market_power-transformer-manufacturer/README.md) | ERP and Production Scheduling Platform (EPSP) | 52 (11) | 253 |
| Critical Manufacturing | Enterprise | [Power transformer manufacturer](03_company-samples/manufacturing_critical-manufacturing/size-5_enterprise_power-transformer-manufacturer/README.md) | Enterprise ERP and Production Scheduling Platform (EPSP) | 66 (13) | 282 |
| Critical Manufacturing | Multi-Sector | [Power transformer manufacturer plus two divisions](03_company-samples/manufacturing_critical-manufacturing/size-6_multi-sector_power-transformer-manufacturer-plus-two-divisions/README.md) | Group ERP and Production Scheduling Platform (GEPS) | 70 (11) | 225 |
| Dams | Sole Proprietor | [Dam safety consultant](03_company-samples/utilities_dams-critical-infrastructure/size-1_sole-proprietor_dam-safety-consultant/README.md) | Core Business SaaS Stack (CBSS) | 15 (2) | 37 |
| Dams | Micro | [Hydroelectric dam operator](03_company-samples/utilities_dams-critical-infrastructure/size-2_micro_hydroelectric-dam-operator/README.md) | Hydro Plant Control and Dam Monitoring System (HPCDMS) | 23 (4) | 100 |
| Dams | Mid-Market | [Hydroelectric dam operator](03_company-samples/utilities_dams-critical-infrastructure/size-4_mid-market_hydroelectric-dam-operator/README.md) | Hydro Control and Dam Monitoring System (HCDMS) | 51 (11) | 240 |
| Dams | Enterprise | [Hydroelectric dam operator](03_company-samples/utilities_dams-critical-infrastructure/size-5_enterprise_hydroelectric-dam-operator/README.md) | Hydro Fleet Control and Dam Monitoring System (HFCDMS) | 65 (18) | 297 |
| Dams | Multi-Sector | [Hydroelectric dam operator plus two divisions](03_company-samples/utilities_dams-critical-infrastructure/size-6_multi-sector_hydroelectric-dam-operator-plus-two-divisions/README.md) | Hydro Plant Control and Dam Monitoring System (HPCDMS) | 82 (17) | 256 |
| Defense Industrial Base | Sole Proprietor | [Engineering subcontractor with CUI](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-1_sole-proprietor_engineering-subcontractor-with-cui/README.md) | Engineering Office Systems (EOS) | 15 (5) | 41 |
| Defense Industrial Base | Micro | [Aircraft parts manufacturer](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-2_micro_aircraft-parts-manufacturer/README.md) | CUI Machining Enclave (CME) | 25 (6) | 77 |
| Defense Industrial Base | Mid-Market | [Aircraft parts manufacturer](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-4_mid-market_aircraft-parts-manufacturer/README.md) | CUI Engineering Enclave (CEE) | 50 (12) | 240 |
| Defense Industrial Base | Enterprise | [Aircraft parts manufacturer](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-5_enterprise_aircraft-parts-manufacturer/README.md) | CUI Engineering Enclave (CEE) | 64 (13) | 259 |
| Defense Industrial Base | Multi-Sector | [Aircraft parts manufacturer plus two divisions](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-6_multi-sector_aircraft-parts-manufacturer-plus-two-divisions/README.md) | Group CUI Engineering Enclave (GCEE) | 88 (15) | 266 |
| Educational Services | Sole Proprietor | [Tutoring service](03_company-samples/education/size-1_sole-proprietor_tutoring-service/README.md) | Core Business SaaS Stack | 15 (4) | 42 |
| Educational Services | Micro | [Tutoring company](03_company-samples/education/size-2_micro_tutoring-company/README.md) | Tutoring Operations Platform (TOP) | 24 (3) | 87 |
| Educational Services | Mid-Market | [Private college](03_company-samples/education/size-4_mid-market_private-college/README.md) | Student Information and Learning Platform (SILP) | 52 (9) | 233 |
| Educational Services | Enterprise | [Private college](03_company-samples/education/size-5_enterprise_private-college/README.md) | Student Records and Learning Platform (SRLP) | 66 (15) | 268 |
| Educational Services | Multi-Sector | [Private college plus two divisions](03_company-samples/education/size-6_multi-sector_private-college-plus-two-divisions/README.md) | Student Records and Learning Platform (SRLP) | 86 (12) | 236 |
| Emergency Services | Sole Proprietor | [Private security patrol](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-1_sole-proprietor_private-security-patrol/README.md) | Patrol Business SaaS Stack | 15 (3) | 46 |
| Emergency Services | Micro | [Non-emergency ambulance service](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-2_micro_non-emergency-ambulance-service/README.md) | Transport Operations Platform (TOP) | 24 (3) | 87 |
| Emergency Services | Mid-Market | [Ambulance service](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-4_mid-market_ambulance-service/README.md) | Dispatch and Patient Care Platform (DPCP) | 50 (9) | 255 |
| Emergency Services | Enterprise | [Ambulance service](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-5_enterprise_ambulance-service/README.md) | Enterprise Dispatch and Patient Care Platform (EDPCP) | 66 (12) | 271 |
| Emergency Services | Multi-Sector | [Ambulance service plus two divisions](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-6_multi-sector_ambulance-service-plus-two-divisions/README.md) | Dispatch and Patient Care Platform (DPCP) | 79 (12) | 271 |
| Energy | Sole Proprietor | [Pipeline integrity consultant](03_company-samples/utilities_energy-critical-infrastructure/size-1_sole-proprietor_pipeline-integrity-consultant/README.md) | Core Business SaaS Stack | 15 (4) | 43 |
| Energy | Micro | [Small intrastate pipeline](03_company-samples/utilities_energy-critical-infrastructure/size-2_micro_small-intrastate-pipeline/README.md) | Pipeline SCADA and Gas Control System (PSGCS) | 23 (4) | 108 |
| Energy | Mid-Market | [Gas transmission pipeline](03_company-samples/utilities_energy-critical-infrastructure/size-4_mid-market_gas-transmission-pipeline/README.md) | Pipeline SCADA and Gas Control System (PSGCS) | 51 (7) | 253 |
| Energy | Enterprise | [Gas transmission pipeline](03_company-samples/utilities_energy-critical-infrastructure/size-5_enterprise_gas-transmission-pipeline/README.md) | Pipeline SCADA and Gas Control System (PSGCS) | 65 (12) | 278 |
| Energy | Multi-Sector | [Gas transmission pipeline plus two divisions](03_company-samples/utilities_energy-critical-infrastructure/size-6_multi-sector_gas-transmission-pipeline-plus-two-divisions/README.md) | Pipeline SCADA and Gas Control System (PSGCS) | 80 (15) | 262 |
| Finance and Insurance | Sole Proprietor | [Registered investment adviser](03_company-samples/finance-insurance/size-1_sole-proprietor_registered-investment-adviser/README.md) | Advisory Practice Systems Profile | 15 (3) | 33 |
| Finance and Insurance | Micro | [Community credit union](03_company-samples/finance-insurance/size-2_micro_community-credit-union/README.md) | Core and Digital Banking Platform (CDBP) | 23 (4) | 86 |
| Finance and Insurance | Mid-Market | [Regional bank](03_company-samples/finance-insurance/size-4_mid-market_regional-bank/README.md) | Core and Online Banking Platform (COBP) | 50 (8) | 244 |
| Finance and Insurance | Enterprise | [Super-regional bank](03_company-samples/finance-insurance/size-5_enterprise_super-regional-bank/README.md) | Core Banking and Digital Channels Platform (CBDC) | 66 (11) | 269 |
| Finance and Insurance | Multi-Sector | [Diversified financial group](03_company-samples/finance-insurance/size-6_multi-sector_diversified-financial-group/README.md) | Core and Digital Banking Platform (CDBP) | 80 (11) | 269 |
| Financial Services | Sole Proprietor | [Independent insurance agency](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-1_sole-proprietor_independent-insurance-agency/README.md) | Agency Systems Profile | 15 (3) | 41 |
| Financial Services | Micro | [Merchant services provider](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-2_micro_merchant-services-provider/README.md) | Merchant Payments Platform (MPP) | 22 (4) | 102 |
| Financial Services | Mid-Market | [Payment processor](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-4_mid-market_payment-processor/README.md) | Payment Processing Platform (PPP) | 52 (13) | 207 |
| Financial Services | Enterprise | [Payment processor](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-5_enterprise_payment-processor/README.md) | Core Payment Processing Platform (CPPP) | 65 (14) | 277 |
| Financial Services | Multi-Sector | [Payment processor plus two divisions](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-6_multi-sector_payment-processor-plus-two-divisions/README.md) | Payment Processing Platform (PPP) | 80 (10) | 260 |
| Food and Agriculture | Sole Proprietor | [Custom-exempt meat processor](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-1_sole-proprietor_custom-exempt-meat-processor/README.md) | Shop Production and Cold-Chain Monitoring System (SPCM) | 15 (4) | 50 |
| Food and Agriculture | Micro | [Meat processor](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-2_micro_meat-processor/README.md) | Plant Production and Cold-Chain Monitoring System (PPCM) | 23 (4) | 106 |
| Food and Agriculture | Mid-Market | [Meat processor](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-4_mid-market_meat-processor/README.md) | Plant Production and Cold-Chain Monitoring System (PPCM) | 52 (15) | 244 |
| Food and Agriculture | Enterprise | [Meat processor](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-5_enterprise_meat-processor/README.md) | Plant Production and Cold-Chain Monitoring System (PPCM) | 65 (13) | 293 |
| Food and Agriculture | Multi-Sector | [Meat processor plus two divisions](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-6_multi-sector_meat-processor-plus-two-divisions/README.md) | Plant Production and Cold-Chain Monitoring System (PPCM) | 86 (15) | 290 |
| Government Services and Facilities | Sole Proprietor | [Facilities support contractor](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-1_sole-proprietor_facilities-support-contractor/README.md) | Building Systems Support Environment | 15 (3) | 37 |
| Government Services and Facilities | Micro | [Facilities support contractor](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-2_micro_facilities-support-contractor/README.md) | Building Systems Operations Platform | 23 (4) | 88 |
| Government Services and Facilities | Mid-Market | [Facilities support contractor](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-4_mid-market_facilities-support-contractor/README.md) | Integrated Facility Operations Platform (IFOP) | 52 (13) | 253 |
| Government Services and Facilities | Enterprise | [Facilities support contractor](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-5_enterprise_facilities-support-contractor/README.md) | Integrated Building Operations Platform (IBOP) | 64 (12) | 307 |
| Government Services and Facilities | Multi-Sector | [Facilities support contractor plus two divisions](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-6_multi-sector_facilities-support-contractor-plus-two-divisions/README.md) | Integrated Building Operations Platform (IBOP) | 86 (12) | 265 |
| Healthcare and Public Health | Sole Proprietor | [Independent pharmacy](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-1_sole-proprietor_independent-pharmacy/README.md) | Pharmacy Core SaaS Stack | 15 (3) | 39 |
| Healthcare and Public Health | Micro | [Independent pharmacy](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-2_micro_independent-pharmacy/README.md) | Pharmacy Core SaaS Stack | 23 (4) | 102 |
| Healthcare and Public Health | Mid-Market | [Hospital](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-4_mid-market_hospital/README.md) | Hospital EHR and Clinical Systems (HECS) | 55 (14) | 243 |
| Healthcare and Public Health | Enterprise | [Hospital system](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-5_enterprise_hospital-system/README.md) | Enterprise Clinical Information System (ECIS) | 66 (12) | 289 |
| Healthcare and Public Health | Multi-Sector | [Hospital plus two divisions](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-6_multi-sector_hospital-plus-two-divisions/README.md) | Hospital Clinical Information System (HCIS) | 80 (10) | 259 |
| Information | Sole Proprietor | [Independent SaaS developer](03_company-samples/information-software-media/size-1_sole-proprietor_independent-saas-developer/README.md) | Multi-tenant Booking Platform (MBP) | 15 (3) | 35 |
| Information | Micro | [B2B SaaS publisher](03_company-samples/information-software-media/size-2_micro_b2b-saas-publisher/README.md) | Vendor Compliance Platform (VCP) | 25 (3) | 85 |
| Information | Mid-Market | [B2B SaaS publisher](03_company-samples/information-software-media/size-4_mid-market_b2b-saas-publisher/README.md) | Customer Engagement Platform (CEP) | 52 (9) | 224 |
| Information | Enterprise | [B2B SaaS publisher](03_company-samples/information-software-media/size-5_enterprise_b2b-saas-publisher/README.md) | Operations Cloud Production Platform (OCP) | 64 (13) | 270 |
| Information | Multi-Sector | [B2B SaaS publisher plus two divisions](03_company-samples/information-software-media/size-6_multi-sector_b2b-saas-publisher-plus-two-divisions/README.md) | Workforce Cloud Platform (WCP) | 86 (11) | 274 |
| Information Technology | Sole Proprietor | [Web hosting reseller](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-1_sole-proprietor_web-hosting-reseller/README.md) | Hosting Control Plane and Customer Portal (HCP) | 15 (4) | 43 |
| Information Technology | Micro | [Cloud hosting provider](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-2_micro_cloud-hosting-provider/README.md) | Hosting Control Plane and Customer Portal (HCP) | 25 (5) | 83 |
| Information Technology | Mid-Market | [Cloud hosting provider](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-4_mid-market_cloud-hosting-provider/README.md) | Hosting Control Plane and Customer Portal (HCP) | 52 (14) | 185 |
| Information Technology | Enterprise | [Cloud hosting provider](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-5_enterprise_cloud-hosting-provider/README.md) | Hosting Control Plane and Customer Portal, Government Region (HCP-G) | 65 (11) | 306 |
| Information Technology | Multi-Sector | [Cloud hosting provider plus two divisions](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-6_multi-sector_cloud-hosting-provider-plus-two-divisions/README.md) | Hosting Control Plane and Customer Portal (HCP) | 84 (9) | 257 |
| Management of Companies and Enterprises | Sole Proprietor | [Owner of several small businesses](03_company-samples/holding-companies/size-1_sole-proprietor_owner-of-several-small-businesses/README.md) | Shared Back-Office Platform | 15 (3) | 56 |
| Management of Companies and Enterprises | Micro | [Family holding office](03_company-samples/holding-companies/size-2_micro_family-holding-office/README.md) | Family Office Shared Services Platform | 23 (4) | 89 |
| Management of Companies and Enterprises | Mid-Market | [Holding company](03_company-samples/holding-companies/size-4_mid-market_holding-company/README.md) | Shared Corporate Services Platform (SCSP) | 52 (10) | 254 |
| Management of Companies and Enterprises | Enterprise | [Holding company](03_company-samples/holding-companies/size-5_enterprise_holding-company/README.md) | Shared Corporate Services Platform (SCSP) | 65 (14) | 275 |
| Management of Companies and Enterprises | Multi-Sector | [Holding company plus two divisions](03_company-samples/holding-companies/size-6_multi-sector_holding-company-plus-two-divisions/README.md) | Shared Corporate Services Platform (SCSP) | 60 (9) | 243 |
| Manufacturing | Sole Proprietor | [CNC machine shop](03_company-samples/manufacturing/size-1_sole-proprietor_cnc-machine-shop/README.md) | Shop Business Systems (SBS) | 15 (3) | 46 |
| Manufacturing | Micro | [Medical device startup](03_company-samples/manufacturing/size-2_micro_medical-device-startup/README.md) | Product Development and Release Platform (PDRP) | 24 (4) | 111 |
| Manufacturing | Mid-Market | [Medical device manufacturer](03_company-samples/manufacturing/size-4_mid-market_medical-device-manufacturer/README.md) | Device Lifecycle Platform (DLP) | 50 (9) | 212 |
| Manufacturing | Enterprise | [Global medical device maker](03_company-samples/manufacturing/size-5_enterprise_global-medical-device-maker/README.md) | Device Software Factory and Manufacturing Execution System (DSF-MES) | 65 (11) | 270 |
| Manufacturing | Multi-Sector | [Diversified industrial group](03_company-samples/manufacturing/size-6_multi-sector_diversified-industrial-group/README.md) | Device Engineering and Manufacturing System (DEMS) | 78 (12) | 227 |
| Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietor | [Oilfield services contractor](03_company-samples/mining-oil-gas/size-1_sole-proprietor_oilfield-services-contractor/README.md) | Field Service Business Systems (FSBS) | 15 (4) | 49 |
| Mining, Quarrying, and Oil and Gas Extraction | Micro | [Crude oil producer](03_company-samples/mining-oil-gas/size-2_micro_crude-oil-producer/README.md) | Field SCADA and Production Accounting System (FSPA) | 25 (4) | 110 |
| Mining, Quarrying, and Oil and Gas Extraction | Mid-Market | [Crude oil producer](03_company-samples/mining-oil-gas/size-4_mid-market_crude-oil-producer/README.md) | Field SCADA and Production Accounting System (FSPA) | 52 (7) | 251 |
| Mining, Quarrying, and Oil and Gas Extraction | Enterprise | [Crude oil producer](03_company-samples/mining-oil-gas/size-5_enterprise_crude-oil-producer/README.md) | Field SCADA and Production Accounting System (FSPA) | 64 (12) | 300 |
| Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector | [Crude oil producer plus two divisions](03_company-samples/mining-oil-gas/size-6_multi-sector_crude-oil-producer-plus-two-divisions/README.md) | Field SCADA and Production Accounting System (FSPA) | 66 (14) | 242 |
| Nuclear Reactors, Materials, and Waste | Sole Proprietor | [Radiation safety consultant](03_company-samples/utilities_nuclear-critical-infrastructure/size-1_sole-proprietor_radiation-safety-consultant/README.md) | Core Business SaaS Stack (CBSS) | 15 (2) | 34 |
| Nuclear Reactors, Materials, and Waste | Micro | [Radiation safety consulting practice](03_company-samples/utilities_nuclear-critical-infrastructure/size-2_micro_radiation-safety-consulting-practice/README.md) | Practice Business Platform | 23 (3) | 85 |
| Nuclear Reactors, Materials, and Waste | Mid-Market | [Nuclear power plant](03_company-samples/utilities_nuclear-critical-infrastructure/size-4_mid-market_nuclear-power-plant/README.md) | Plant Business Network and Work Management System (PBN-WMS) | 52 (9) | 245 |
| Nuclear Reactors, Materials, and Waste | Enterprise | [Nuclear power plant](03_company-samples/utilities_nuclear-critical-infrastructure/size-5_enterprise_nuclear-power-plant/README.md) | Fleet Work Management System and Plant Business Networks (WMS-PBN) | 64 (9) | 283 |
| Nuclear Reactors, Materials, and Waste | Multi-Sector | [Nuclear power plant plus two divisions](03_company-samples/utilities_nuclear-critical-infrastructure/size-6_multi-sector_nuclear-power-plant-plus-two-divisions/README.md) | Plant Business Network and Work Management System (PBN-WMS) | 82 (13) | 246 |
| Other Services (except Public Administration) | Sole Proprietor | [Device repair service](03_company-samples/repair-personal-services/size-1_sole-proprietor_device-repair-service/README.md) | Service Ticketing and Point-of-Sale System (STPS) | 15 (2) | 41 |
| Other Services (except Public Administration) | Micro | [Device repair service](03_company-samples/repair-personal-services/size-2_micro_device-repair-service/README.md) | Service Ticketing and Point-of-Sale System (STPS) | 24 (3) | 80 |
| Other Services (except Public Administration) | Mid-Market | [Device repair service](03_company-samples/repair-personal-services/size-4_mid-market_device-repair-service/README.md) | Service Ticketing and Point-of-Sale Platform (STPP) | 50 (8) | 255 |
| Other Services (except Public Administration) | Enterprise | [Device repair service](03_company-samples/repair-personal-services/size-5_enterprise_device-repair-service/README.md) | Service Ticketing and Point-of-Sale Platform (STPP) | 64 (12) | 251 |
| Other Services (except Public Administration) | Multi-Sector | [Device repair service plus two divisions](03_company-samples/repair-personal-services/size-6_multi-sector_device-repair-service-plus-two-divisions/README.md) | Service Ticketing and Point-of-Sale Platform (STPP) | 86 (14) | 252 |
| Professional, Scientific, and Technical Services | Sole Proprietor | [CPA tax firm](03_company-samples/professional-services/size-1_sole-proprietor_cpa-tax-firm/README.md) | Tax Practice Systems Profile | 15 (2) | 44 |
| Professional, Scientific, and Technical Services | Micro | [CPA tax firm](03_company-samples/professional-services/size-2_micro_cpa-tax-firm/README.md) | Client Tax Platform (CTP) | 25 (3) | 80 |
| Professional, Scientific, and Technical Services | Mid-Market | [CPA tax firm](03_company-samples/professional-services/size-4_mid-market_cpa-tax-firm/README.md) | Tax and Client Data Platform (TCDP) | 52 (11) | 203 |
| Professional, Scientific, and Technical Services | Enterprise | [CPA tax firm](03_company-samples/professional-services/size-5_enterprise_cpa-tax-firm/README.md) | Tax Engagement Platform (TEP) | 64 (13) | 263 |
| Professional, Scientific, and Technical Services | Multi-Sector | [CPA tax firm plus two divisions](03_company-samples/professional-services/size-6_multi-sector_cpa-tax-firm-plus-two-divisions/README.md) | Tax Preparation and Client Portal Platform (TPCP) | 86 (11) | 270 |
| Public Administration | Sole Proprietor | [Independent GovTech consultant](03_company-samples/public-administration/size-1_sole-proprietor_independent-govtech-consultant/README.md) | Consulting Delivery Environment (CDE) | 15 (3) | 39 |
| Public Administration | Micro | [GovTech integrator](03_company-samples/public-administration/size-2_micro_govtech-integrator/README.md) | Hosted Case Management Service (HCMS) | 25 (7) | 85 |
| Public Administration | Mid-Market | [GovTech integrator](03_company-samples/public-administration/size-4_mid-market_govtech-integrator/README.md) | Agency Case Management Cloud (ACMC) | 52 (8) | 224 |
| Public Administration | Enterprise | [GovTech integrator](03_company-samples/public-administration/size-5_enterprise_govtech-integrator/README.md) | Agency Case Management Cloud (ACMC) | 66 (14) | 283 |
| Public Administration | Multi-Sector | [GovTech integrator plus two divisions](03_company-samples/public-administration/size-6_multi-sector_govtech-integrator-plus-two-divisions/README.md) | Agency Case Management Platform (ACMP) | 86 (18) | 257 |
| Real Estate and Rental and Leasing | Sole Proprietor | [Real estate brokerage](03_company-samples/real-estate/size-1_sole-proprietor_real-estate-brokerage/README.md) | Transaction Management and Closing Communications System (TMCC) | 15 (3) | 33 |
| Real Estate and Rental and Leasing | Micro | [Real estate brokerage](03_company-samples/real-estate/size-2_micro_real-estate-brokerage/README.md) | Transaction Management and Closing Communications System (TMCC) | 25 (3) | 80 |
| Real Estate and Rental and Leasing | Mid-Market | [Real estate brokerage](03_company-samples/real-estate/size-4_mid-market_real-estate-brokerage/README.md) | Transaction Management and Closing Communications System (TMCC) | 52 (9) | 223 |
| Real Estate and Rental and Leasing | Enterprise | [Real estate brokerage](03_company-samples/real-estate/size-5_enterprise_real-estate-brokerage/README.md) | Transaction Management and Closing Communications System (TMCC) | 64 (14) | 294 |
| Real Estate and Rental and Leasing | Multi-Sector | [Real estate brokerage plus two divisions](03_company-samples/real-estate/size-6_multi-sector_real-estate-brokerage-plus-two-divisions/README.md) | Transaction Management and Closing Communications System (TMCC) | 79 (13) | 279 |
| Retail Trade | Sole Proprietor | [Corner grocery](03_company-samples/retail-trade/size-1_sole-proprietor_corner-grocery/README.md) | Store Sales Platform | 15 (3) | 49 |
| Retail Trade | Micro | [Grocery retailer](03_company-samples/retail-trade/size-2_micro_grocery-retailer/README.md) | Store Commerce Platform (SCP) | 25 (2) | 100 |
| Retail Trade | Mid-Market | [Grocery retailer](03_company-samples/retail-trade/size-4_mid-market_grocery-retailer/README.md) | E-commerce and Point-of-Sale Platform (EPP) | 50 (10) | 256 |
| Retail Trade | Enterprise | [Grocery retailer](03_company-samples/retail-trade/size-5_enterprise_grocery-retailer/README.md) | Omnichannel Commerce and Payments Platform (OCPP) | 64 (9) | 279 |
| Retail Trade | Multi-Sector | [Grocery retailer plus two divisions](03_company-samples/retail-trade/size-6_multi-sector_grocery-retailer-plus-two-divisions/README.md) | E-commerce and Point-of-Sale Platform (EPP) | 76 (10) | 275 |
| Transportation Systems | Sole Proprietor | [Rail and truck freight broker](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-1_sole-proprietor_rail-and-truck-freight-broker/README.md) | Freight Brokerage SaaS Stack | 15 (4) | 35 |
| Transportation Systems | Micro | [Freight railroad](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-2_micro_freight-railroad/README.md) | Train Dispatch and Operations Back Office (TDOB) | 22 (3) | 84 |
| Transportation Systems | Mid-Market | [Freight railroad](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-4_mid-market_freight-railroad/README.md) | Train Dispatch and PTC Operations Platform (TDPO) | 52 (10) | 252 |
| Transportation Systems | Enterprise | [Freight railroad](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-5_enterprise_freight-railroad/README.md) | Train Dispatching and PTC Back Office Platform (TDPB) | 63 (12) | 297 |
| Transportation Systems | Multi-Sector | [Freight railroad plus two divisions](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-6_multi-sector_freight-railroad-plus-two-divisions/README.md) | Train Dispatching and PTC Back Office Platform (TDPB) | 74 (9) | 276 |
| Transportation and Warehousing | Sole Proprietor | [Freight forwarder customs broker](03_company-samples/transportation-warehousing/size-1_sole-proprietor_freight-forwarder-customs-broker/README.md) | Core Brokerage SaaS Stack | 15 (3) | 37 |
| Transportation and Warehousing | Micro | [Freight forwarding office](03_company-samples/transportation-warehousing/size-2_micro_freight-forwarding-office/README.md) | Core Brokerage SaaS Stack | 23 (3) | 83 |
| Transportation and Warehousing | Mid-Market | [Marine cargo terminal](03_company-samples/transportation-warehousing/size-4_mid-market_marine-cargo-terminal/README.md) | Terminal Operations and Gate Platform (TOGP) | 51 (8) | 246 |
| Transportation and Warehousing | Enterprise | [Marine cargo terminal](03_company-samples/transportation-warehousing/size-5_enterprise_marine-cargo-terminal/README.md) | Enterprise Terminal Operating and Gate Platform (ETOP) | 65 (13) | 289 |
| Transportation and Warehousing | Multi-Sector | [Marine cargo terminal plus two divisions](03_company-samples/transportation-warehousing/size-6_multi-sector_marine-cargo-terminal-plus-two-divisions/README.md) | Terminal Operations Platform (TOP) | 80 (22) | 269 |
| Utilities | Sole Proprietor | [Utility engineering consultant](03_company-samples/utilities/size-1_sole-proprietor_utility-engineering-consultant/README.md) | Core Business Systems (CBS) | 15 (3) | 30 |
| Utilities | Micro | [Small electric cooperative](03_company-samples/utilities/size-2_micro_small-electric-cooperative/README.md) | Distribution SCADA and Outage Management System (DSOMS) | 23 (3) | 118 |
| Utilities | Mid-Market | [Electric distribution utility](03_company-samples/utilities/size-4_mid-market_electric-distribution-utility/README.md) | Distribution Operations Platform (DOP) | 52 (8) | 236 |
| Utilities | Enterprise | [Electric distribution utility](03_company-samples/utilities/size-5_enterprise_electric-distribution-utility/README.md) | Distribution Operations Platform (DOP) | 66 (11) | 300 |
| Utilities | Multi-Sector | [Electric distribution utility plus two divisions](03_company-samples/utilities/size-6_multi-sector_electric-distribution-utility-plus-two-divisions/README.md) | Distribution Operations Platform (DOP) | 86 (16) | 254 |
| Water and Wastewater Systems | Sole Proprietor | [Small water system](03_company-samples/utilities_water-critical-infrastructure/size-1_sole-proprietor_small-water-system/README.md) | Water System Operations Profile (WSOP) | 15 (2) | 51 |
| Water and Wastewater Systems | Micro | [Community water system](03_company-samples/utilities_water-critical-infrastructure/size-2_micro_community-water-system/README.md) | Water Treatment SCADA System (WTSS) | 23 (4) | 117 |
| Water and Wastewater Systems | Mid-Market | [Community water system](03_company-samples/utilities_water-critical-infrastructure/size-4_mid-market_community-water-system/README.md) | Integrated Water Operations SCADA (IWOS) | 53 (10) | 247 |
| Water and Wastewater Systems | Enterprise | [Community water system](03_company-samples/utilities_water-critical-infrastructure/size-5_enterprise_community-water-system/README.md) | Gulf Coast Regional Water Treatment SCADA System (GCR-WTSS) | 65 (14) | 313 |
| Water and Wastewater Systems | Multi-Sector | [Community water system plus two divisions](03_company-samples/utilities_water-critical-infrastructure/size-6_multi-sector_community-water-system-plus-two-divisions/README.md) | Regional System 1 Water Treatment SCADA (RS1-SCADA) | 78 (10) | 243 |
| Wholesale Trade | Sole Proprietor | [IT hardware reseller](03_company-samples/wholesale-trade/size-1_sole-proprietor_it-hardware-reseller/README.md) | Reseller Order Desk (ROD) | 15 (3) | 52 |
| Wholesale Trade | Micro | [IT hardware reseller](03_company-samples/wholesale-trade/size-2_micro_it-hardware-reseller/README.md) | Reseller Operations Platform (ROP) | 25 (6) | 85 |
| Wholesale Trade | Mid-Market | [IT hardware distributor](03_company-samples/wholesale-trade/size-4_mid-market_it-hardware-distributor/README.md) | Distribution Operations Platform (DOP) | 52 (11) | 194 |
| Wholesale Trade | Enterprise | [IT hardware distributor](03_company-samples/wholesale-trade/size-5_enterprise_it-hardware-distributor/README.md) | Order-to-Cash and Fulfillment Platform (OCFP) | 65 (14) | 270 |
| Wholesale Trade | Multi-Sector | [IT hardware distributor plus two divisions](03_company-samples/wholesale-trade/size-6_multi-sector_it-hardware-distributor-plus-two-divisions/README.md) | Order-to-Fulfillment Platform (OFP) | 75 (12) | 247 |

**Batch 1 detail (completed 2026-09-27): Manufacturing and Finance size ladders**, with the primary-rule finding of each P03. With Health Care, three industries now show the same method at all six sizes.

| Industry | Size | Business | P03 finding (primary rule) | Risks (High+) | P07 statements |
|---|---|---|---|---|---|
| Manufacturing | Sole Proprietor | CNC machine shop | FAR 52.204-21 and CMMC Level 1 by contract flow-down; FDA 524B and QMSR do not reach a component maker directly | 15 (3) | 46 |
| Manufacturing | Micro | Medical device startup | FD&C Act 524B premarket duties; QMSR (effective 2026-02-02) as manufacturer of record | 24 (4) | 111 |
| Manufacturing | Mid-Market | Medical device manufacturer | 524B postmarket, QMSR, 21 CFR 803 and 806, HIPAA business associate; SP 800-82r3 for the plant | 50 (9) | 212 |
| Manufacturing | Enterprise | Global medical device maker | Same, plus the FTC Health Breach Notification Rule for its consumer app and SEC Item 1.05 and 106 | 65 (11) | 270 |
| Manufacturing | Multi-Sector | Diversified industrial group | Devices (524B), distribution (FAR 52.204-21, CMMC Level 1), testing (CSF 2.0 benchmark); group SEC rules | 78 (12) | 227 |
| Finance | Sole Proprietor | Registered investment adviser | State-registered, so the FTC Safeguards Rule (16 CFR 314.1(b)), not SEC Regulation S-P | 15 (3) | 33 |
| Finance | Micro | Community credit union | NCUA 12 CFR Part 748 and its 72-hour notice; bank and FTC rules do not apply | 23 (4) | 86 |
| Finance | Mid-Market | Regional bank | 12 CFR 30 App. B and 12 CFR 53; App. D and SEC rules do not apply at this size | 50 (8) | 244 |
| Finance | Enterprise | Super-regional bank | App. D heightened standards, 12 CFR 252.22, 53.3 and 225.302, SEC rules, Reg S-P for its broker-dealer | 66 (11) | 269 |
| Finance | Multi-Sector | Diversified financial group | Bank (App. D), bank service provider software division (12 CFR 53.4), real estate under the holding company's GLBA program | 80 (11) | 269 |

**Added to the industry rules during batch 1:** N52-R09 (NCUA Part 748) and N52-R10 (OCC heightened standards).

---

## 5. Keeping it current (the isolated universal layer)

**Routine:** review quarterly. Run the refresh tools, re-check every row marked `verified=false`, and update `last_verified` in the source register. See [docs/how-to-update.md](docs/how-to-update.md).

**Watch list** (verified 2026-09-25). Each item would change the layers:

| Item | Status | Affects |
|---|---|---|
| HIPAA Security Rule NPRM (90 FR 898) | Proposed Jan 2025; regulatory agenda projects a final rule July 2027 | Health Care P03, P06, P07 |
| CIRCIA final rule (6 CFR 226) | Targeted Sept 2026; not published | Cross-sector P08 notification baseline |
| FedRAMP Consolidated Rules 2026 | Mandatory 2027-01-01; no new Rev 5 certifications after 2027-06-11 | P02, P04 for federal-facing scenarios |
| CMMC phase-in | **Phase 2 suspended (verified 2026-10-08).** The DoD (Department of War) CIO memorandum of 2026-07-13 suspended the 2026-11-10 Phase 2 transition. DoD Class Deviation 2026-O0025, Revision 3 (SRC-DFARS-DEV-2026-O0025; DFARS 240.371-5) uses clause 252.204-7021 until 2028-11-09 only when a program office requires a CMMC level, and from 2028-11-10 whenever FCI or CUI is handled. Requiring activities may require Level 1 (Self) or Level 2 (Self); SP 800-171 Rev. 2 under 252.204-7012 still applies. The industry layers and the affected samples were updated on 2026-10-08, each judged as of its own assessment date. Watch for the deviation being rescinded or codified | Defense Industrial Base, Manufacturing, Construction, and federal contractors in other industries |
| NIST AI RMF revision | In progress (AI Action Plan) | P10 |
| Colorado SB26-189 (ADMT) and CPPA ADMT rules | Both effective or compliance-due 2027-01-01 | P10, cross-sector |
| SBA size standards proposed rule | Proposed Aug 2026; comments to 2026-11-20 | Tier sizing (rerun `refresh_sba_standards.py` when final) |
| NAICS 2027 | Proposed by OMB July 2026 | Vertical codes |
| FAR overhaul (proposed Part 40, NIST SP 800-171 Rev. 3, 72-hour CUI reporting) | Proposed June 2026 | Federal contractor scenarios |
| Revolutionary FAR Overhaul Part 40 and DFARS Part 240 (in use by class deviation) | **Applied 2026-10-08, dual-track.** Agencies that issued a FAR Part 40 class deviation (DoD, GSA, DHS, DOE, VA and most others) put FAR 52.240-90 to 52.240-93 in new awards; contracts awarded earlier keep FAR 52.204-21, -23, -25 and DFARS 252.204-7019/-7020 until modified. 52.240-93 has the same 15 requirements as 52.204-21; 52.240-91 has one prohibited-product report within 72 hours; DFARS 252.240-7997 covers DoD-led Medium and High assessments. Layers, all 200 notification matrices that cite the old clauses, 85 facts files and 61 gap analysis reports now state both. Watch for the formal RFO final rule, whose proposed numbers differ (for example 52.240-5) | All federal contractor scenarios |
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
| OCC heightened standards threshold (12 CFR 30 App. D) | Proposal to raise the $50 billion threshold (90 FR 61084, 2025-12-30); not final | Finance Enterprise and Multi-Sector |
| Model risk management guidance | Federal Reserve SR 26-2 (2026-04-17) supersedes SR 11-7; generative AI outside its scope | Finance P10 |
| NCUA Part 748 Appendices A and B | Proposed for removal from the CFR; not final | Finance Micro (credit union) |
| NSM-22 review (EO 14239) | Under review; still in effect | CISA sector list |

---

## 6. Open items

1. **Unverified research rows: reviewed 2026-10-08.** 17 of 19 vertical rows were verified against primary sources (Florida breach and local government statutes, Visa rules, FedRAMP 2026 rules, 44 U.S.C. 3554 and CISA guidelines, Florida Bar rules). Two stay `verified=false` because their sources could not be reached: Illinois BIPA (N72-R05) and the AICPA Code (N54-R08). See `docs/reviews/2026-10-unverified-vertical-rows-review.md`. `tools/validate.py` still counts them.
2. **Industry picks.** The 36 primary industries and 22 tier substitutions are proposals in two CSVs. Change any pick and rebuild.
3. **Multi-Sector pairings: reviewed 2026-10-08.** All 36 pairings are kept; three samples gained missing facts (utility holding company and affiliate rules for Utilities and Critical Manufacturing, state lending licenses for Retail Trade). See `docs/reviews/2026-10-multi-sector-pairings-review.md`. Changing a pairing still means rebuilding that sample.
4. **Office formats.** If you want Word or PDF versions of a finished sample for a meeting, that is a later export step.
5. **External review backlog.** The October 2026 architecture review and our response are in `docs/reviews/2026-10-gemini-architecture-review-response.md`. Fixes A to G and backlog items 1 to 3 are applied (size-1 compensating-control rows, size-6 tenancy decisions, nuclear license-transfer rows). The DoD class deviation was read on 2026-10-08 and the CMMC Phase 2 suspension applied. Still open: the FAR Part 40 and DFARS Part 240 renumbering (see the watch list).
