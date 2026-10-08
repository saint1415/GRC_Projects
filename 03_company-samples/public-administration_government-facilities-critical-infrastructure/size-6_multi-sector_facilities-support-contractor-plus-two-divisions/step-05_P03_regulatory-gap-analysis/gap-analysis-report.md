# Regulatory Gap Analysis: Cris Santos Company Holdings | Government Services and Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Government Services and Facilities (focus division: Government Facilities Support) |
| Primary standard | NIST SP 800-53 Rev. 5, Release 5.2.0 (Aug 27, 2025), **Moderate baseline** from SP 800-53B (177 base controls). **Binding by contract** for state agency scope; **benchmark** for county, municipal, and education scope. OT tailoring from NIST SP 800-82 Rev. 3 |
| Division regulations | Construction: DFARS 252.204-7012, -7019, -7020, -7021, NIST SP 800-171 Rev. 2, and 32 CFR Part 170 (CMMC). Janitorial and Security: NIST CSF 2.0 as benchmark, plus FCRA, the Disposal Rule, Form I-9 retention, E-Verify, and agency requirements flowed down by customer contracts. All divisions: FAR 52.204-21, -23, -25, -30, 52.204-9 |
| Gap tables | `gap-analysis.csv` (Facilities Support and the IBOP: 177 control rows and 20 FAR rows); `gap-analysis-construction.csv` (46 rows); `gap-analysis-janitorial-security.csv` (38 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31 (customer site walkthroughs 2026-06-08 to 2026-06-19), with evidence updated from the P07 assessment (to 2026-08-28). Clause and regulation text read from eCFR (point-in-time 2026-09-23) |
| Assessors | Division security and compliance leads, the Construction CUI program manager, and the Group contracts compliance director, coordinated by the Group CISO; reviewed by group internal audit |

## 1. Applicability
### 1.1 How rules reach a contractor group
The vertical profile names SP 800-53 Rev. 5 as the primary control set because FISMA, IRS Pub. 1075, CJIS, and GovRAMP are all built on it. **SP 800-53 is a catalog, not a law.** It binds a private contractor only through a contract or a federal system authorization. The same is true of most agency rules in this vertical: they bind the agency, and the agency flows them down. So applicability was decided per division and per legal entity, because each division is a separate subsidiary that signs its own contracts and FAR representations.

There is no size exemption anywhere in this analysis. The group is not small under the SBA standard ($47.0 million for NAICS 561210), but none of the clauses or contract terms below depends on size.

### 1.2 Vertical requirements, decided requirement by requirement
| ID | Requirement | Applies to the group? | Reason |
|---|---|---|---|
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558) | **Indirectly, Facilities Support only** | Agencies are responsible for systems "used or operated by an agency or by a contractor of an agency" (44 U.S.C. 3554(a)(1)(A)(ii)). Federal building automation stays on agency networks under agency authorizations; staff reach it only through agency virtual desktops with PIV cards (SYS-F2) and follow agency IT policy (BTTRG v3.0 section 1.1 for GSA buildings). No group system operates on an agency's behalf |
| C-GOVERNMENT-R02 | IRS Pub. 1075 | **By customer contract, at one building** | No group system receives FTI. At the state revenue department building, Pub. 1075 section 2.B.2 lets guards and custodial staff hold keys only where FTI has a second barrier, and section 2.B.3.3 requires cleaning and maintenance in restricted areas with unsecured FTI to happen in the presence of an authorized employee. These are agency duties the contract flows down to Facilities Support and Janitorial and Security |
| C-GOVERNMENT-R03 | CJIS Security Policy v6.1 | **By customer contract** | No group system holds CJI. CJISSECPOL v6.1 AT-3 requires role-based training for all individuals with unescorted access to a physically secure location; its own example is custodial staff at a police department. Customer contracts at buildings housing sheriff's offices and courts flow this down |
| C-GOVERNMENT-R04 | VVSG 2.0 | No | No election systems |
| C-GOVERNMENT-R05 | FERPA | **Yes, Facilities Support, by contract** | The state university designated the company a school official under 34 CFR 99.31(a)(1)(i)(B) for about 38,000 students' cardholder records, which the university treats as education records. The company is bound by the 99.33(a) redisclosure limits, and the university must use reasonable methods to limit access (99.31(a)(1)(ii)) |
| C-GOVERNMENT-R06 | CIRCIA | Not in force | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. As proposed, it would reach an entity in a critical infrastructure sector that exceeds its SBA size standard; counsel will decide whether a facilities contractor group is in the sector when a final rule appears. Tracked in section 6 |
| C-GOVERNMENT-R07 | SLCGP (6 U.S.C. 665g) | No | A grant condition for governments. Customers' grant-funded projects may add contract terms, which are handled as contract terms |
| C-GOVERNMENT-R08 | GovRAMP | **Yes for the IBOP, by contract from 2027** | One state customer's 2027 renewal requires GovRAMP verification of the IBOP by 2027-07-01. GovRAMP is a nonprofit verification program, not law |

## 2. Regulation-by-division matrix
| Requirement | Facilities Support (focus) | Construction | Janitorial and Security | Group (corporate) |
|---|---|---|---|---|
| SP 800-53 Rev. 5 Moderate (state contract exhibits; Florida worked example: Fla. Stat. 282.318(4)(h)) | **Primary.** Binding for state agency scope; benchmark for local and education scope | Not applicable (no such contracts) | Applies to state agency guard contracts only for incident notice terms | Provides 139 common controls (P02) |
| County and municipal security addenda (Florida worked example: Fla. Stat. 282.3185(4)) | Applies (customer standards; 24-hour or 12-hour notice) | Rare; owner specifications only | Applies to county guard and monitoring contracts | Notification matrix |
| C-GOVERNMENT-R01 FISMA | Indirect (agency systems at 46 federal buildings) | Not applicable | Not applicable (officers do not operate agency systems) | No system on behalf of an agency |
| C-GOVERNMENT-R02 IRS Pub. 1075 | By contract (maintenance in FTI areas, 2.B.3.3) | Not applicable | By contract (2.B.2 keys and second barrier; 2.B.3.3 escort) | No FTI systems |
| C-GOVERNMENT-R03 CJIS Security Policy | By contract (AT-3 training for staff at sheriff's office buildings) | Not applicable | By contract (AT-3 training for officers and custodial staff) | No CJI systems |
| C-GOVERNMENT-R05 FERPA | **Applies** (university cardholder records) | Not applicable | Not applicable | IBOP hosts the records |
| C-GOVERNMENT-R08 GovRAMP | Applies to the IBOP from the 2027 renewal | Not applicable | Not applicable | IBOP owner prepares |
| C-GOVERNMENT-R04 VVSG; R07 SLCGP | Not applicable | Not applicable | Not applicable | Not applicable |
| C-GOVERNMENT-R06 CIRCIA | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |
| FAR 52.204-21 (N23-R01; N56-R07) | Applies (FCI in CMMS, email, IBOP workspace) | Applies (CMMC Level 1 for DoD) | Applies (FPS and other federal contracts) | Common controls meet most of it |
| FAR 52.204-23, -25, -30 (N23-R02) | Applies | Applies (subcontractor camera installs) | **Applies, highest exposure** (installation business; monitoring NVRs) | Group screening and quarterly SAM checks |
| FAR 52.204-9 (PIV) | Applies (410 PIV holders) | Where agencies badge jobsite staff | Applies (officers at 22 federal buildings) | HR return process |
| FAR 52.222-54 and state E-Verify laws (Fla. Stat. 448.095 worked example) | Applies | Applies | Applies (about 70,000 applications a year) | Group HR |
| DFARS 252.204-7012, -7019, -7020 (N23-R03) | Not applicable to the division; the IBOP commissioning workspace held Construction CUI | **Primary** (6 DoD contracts) | Not applicable | SOC reporting support |
| DFARS 252.204-7021 and 32 CFR Part 170, CMMC (N23-R04) | Not applicable | **Primary** (Level 1 now; Level 2 (Self) or voluntary C3PAO for DoD bids; Phase 2 suspended 2026-07-13) | Not applicable | Inherited controls must be documented |
| FCRA, Disposal Rule, Form I-9 (N56-R01 to N56-R03) | Applies (group HR) | Applies (group HR) | **Primary** (volume and branch access) | Group HR policies |
| State breach laws (Florida worked example: Fla. Stat. 501.171) | Third-party agent for customer cardholder data; covered entity for own employees | Covered entity for own data | Covered entity for own data; third-party agent for monitoring customers | Coordinates |
| Public records (Florida worked example: Fla. Stat. 119.0701; 119.071(3)(a)) | Applies | Applies (public projects) | Applies (body camera footage, reports) | Group General Counsel |
| Colorado SB26-189 (effective 2027-01-01) | Under counsel review for AI-001 | Not applicable | **Applies** to AI applicant screening for Colorado applicants | Group AI program (P10) |
| NYC Local Law 144 (N56-R08) | Not applicable | Not applicable | Not applicable (no NYC hiring) | Not applicable |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |

## 3. Method
1. **Requirements.**
   - Facilities Support: one row per Moderate base control (G-001 to G-177), with its Moderate enhancements listed in the citation column, plus 20 FAR rows (G-178 to G-197) cited to clause paragraph.
   - Construction: DFARS 252.204-7012 by paragraph, 252.204-7019 and -7020, 252.204-7021 and 32 CFR 170.21, the 25 SP 800-171 Rev. 2 requirements where the division's evidence differs from group common controls or that cannot be placed on a CMMC POA&M, and 4 FAR rows.
   - Janitorial and Security: 20 CSF 2.0 subcategories (benchmark) and 18 binding or contract-driven rows.
2. **Crosswalk.**
   - 134 Facilities Support control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). The other 43 control rows and all FAR rows are author mappings, labeled as such.
   - Construction SP 800-171 rows take CSF subcategories from NIST's official CSF 2.0 to SP 800-171 Rev. 3 references for the same requirement number (author alignment to Rev. 2); SP 800-53 links follow the SP 800-171 Rev. 2 lineage (author mapping).
   - Janitorial and Security CSF rows use selected controls from the official crosswalk; statute and contract rows are author mappings.
3. **Evidence.** Interviews, configuration exports, contract and subcontract samples, SPRS records, the 12 customer site walkthroughs, and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

The Facilities Support statements are the same ones in the SSP control table (P02), so the two documents do not drift apart.

## 4. Results
### 4.1 Facilities Support and the IBOP: SP 800-53 Rev. 5 Moderate baseline (177 base controls)
| Family | Met | Partially met | Not met |
|---|---|---|---|
| AC Access Control | 12 | 5 | 0 |
| AT Awareness and Training | 3 | 1 | 0 |
| AU Audit and Accountability | 7 | 4 | 0 |
| CA Assessment, Authorization, and Monitoring | 5 | 2 | 0 |
| CM Configuration Management | 7 | 5 | 0 |
| CP Contingency Planning | 6 | 3 | 0 |
| IA Identification and Authentication | 6 | 4 | 0 |
| IR Incident Response | 4 | 4 | 0 |
| MA Maintenance | 5 | 1 | 0 |
| MP Media Protection | 5 | 2 | 0 |
| PE Physical and Environmental Protection | 16 | 0 | 0 |
| PL Planning | 5 | 1 | 0 |
| PS Personnel Security | 8 | 1 | 0 |
| RA Risk Assessment | 5 | 1 | 0 |
| SA System and Services Acquisition | 8 | 3 | 0 |
| SC System and Communications Protection | 16 | 2 | 0 |
| SI System and Information Integrity | 8 | 3 | 0 |
| SR Supply Chain Risk Management | 4 | 3 | 2 |
| **Total (177)** | **130** | **45** | **2** |

**FAR clauses (20 rows):** 14 Met and 6 Partially met (52.204-21(b)(1)(i), (ii), (iii), (vi), 52.204-21(c), and 52.204-25).

**Gap risk** (Partially met and Not met rows): of the 47 control gaps, 10 High, 32 Moderate, and 5 Low; of the 6 FAR gaps, 2 High and 4 Moderate.

The focus division is mostly compliant. Most Met rows are group common controls (identity, SOC, cloud, HR, facilities). The gaps sit where the IBOP meets customer sites and integrators (scenario gaps 1 to 4), in incident notification (gap 10), and in supply chain controls, where SR-8 and SR-10 are the only Not met rows.

### 4.2 Construction (`gap-analysis-construction.csv`)
| Requirement group | Met | Partially met | Not met |
|---|---|---|---|
| DFARS 252.204-7012 (11 rows) | 2 | 5 | 4 |
| DFARS 252.204-7019 and -7020 (1 row) | 0 | 1 | 0 |
| DFARS 252.204-7021 and 32 CFR 170 (5 rows) | 0 | 2 | 3 |
| NIST SP 800-171 Rev. 2 (25 rows) | 12 | 12 | 1 |
| FAR 52.204-21, -23, -25, -30 (4 rows) | 3 | 1 | 0 |
| **Total (46)** | **17** | **21** | **8** |

Gap risk: 13 High, 15 Moderate, 1 Low.

**The CMMC problem is placement and score, not missing technology.** The enclave (SYS-C2) meets most requirements, mostly through inherited group controls. But CUI also sits in a commercial SaaS, the IBOP commissioning workspace, an AI estimating service, and jobsite plan rooms, none of which was in the assessed boundary (7012(b)(2)(ii)(D); 7021(d)(2); SP 800-171 3.1.3). The SPRS score is 71 of 110. A conditional Level 2 status needs a score of at least 0.8 of the requirements, 88 of 110 (32 CFR 170.21(a)(2)(i)), and four of the requirements that may never be on a POA&M are open: 3.1.20 (external systems, through subcontractor downloads), 3.12.4 (SSP), 3.10.3 (escort visitors), and 3.10.4 (physical access logs) (170.21(a)(2)(iii)). Phase 2 of the CMMC rollout (planned for 2026-11-10) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. Until 2028-11-09 DoD includes DFARS 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). The 3 planned DoD bids may still require Level 2 (Self), so the score gap matters either way, and SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies. The division keeps the C3PAO assessment as a voluntary choice.

### 4.3 Janitorial and Security (`gap-analysis-janitorial-security.csv`)
| Requirement group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| NIST CSF 2.0 benchmark (20 subcategories) | 4 | 16 | 0 | 0 |
| FCRA, Disposal Rule, Form I-9, E-Verify (8 rows) | 2 | 4 | 2 | 0 |
| FAR clauses (3 rows) | 1 | 1 | 1 | 0 |
| Agency requirements by contract (Pub. 1075, CJIS) (2 rows) | 0 | 2 | 0 | 0 |
| State law, public records, AI and local laws, HIPAA (5 rows) | 1 | 1 | 1 | 2 |
| **Total (38)** | **8** | **24** | **4** | **2** |

Gap risk: 6 High, 13 Moderate, 9 Low.

**Not met:** the Disposal Rule (16 CFR 682.3(a): no disposal process for consumer reports), FAR 52.204-25 (possible covered video equipment, gap 6), the E-Verify MOU breach notice duty (Article II.A.16, not in the matrix), and Colorado SB26-189 deployer duties for the AI screening tool (effective 2027-01-01). The division depends on group common controls for its technology, which are sound; its gaps are in HR data handling, customer-site credentials, and the acquired installation business.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Legacy OT remote access at 37 acquired sites (1) | FS (IBOP) | AC-17; MA-4; FAR 52.204-21(b)(1)(vi) | High | Jump service with MFA and approval everywhere | Group building technology director | 2026-12-15 |
| 2 | CUI outside the enclave; SPRS 71; CMMC Level 2 (5) | CN, FS (IBOP) | DFARS 252.204-7012(b)(2)(ii)(D), (m); 252.204-7021(d); 32 CFR 170.21 | High | Consolidate CUI in SYS-C2; fix no-POA&M requirements; voluntary C3PAO assessment | Construction division president | 2027-03-31 |
| 3 | Covered equipment screening and the 4 NVRs (6) | JS, FS (IBOP), CN | FAR 52.204-25(b)(2), (d) | High | Confirm by 2026-11-30; report within 1 business day if covered; extend screening | Group procurement director | 2026-11-30 |
| 4 | Standing cross-tenant administration (2) | FS (IBOP) | AC-5; AC-6; 34 CFR 99.31(a)(1)(ii) | High | Per-customer just-in-time administration | Facilities Support security systems director | 2027-03-31 |
| 5 | OT segmentation, inventory, and logging (3, 4) | FS (IBOP) | SC-7; CM-8; AU-6; SI-4 | High | Segment 19 sites; reconcile inventory; onboard all sites | Facilities Support controls engineering director | 2027-03-31 |
| 6 | Consumer report access and disposal (7) | JS | 15 U.S.C. 1681b(b); 16 CFR 682.3(a); 8 CFR 274a.2(b)(2) | High | Adjudicator-only access; disposal schedule | Janitorial and Security talent director | 2027-01-31 |
| 7 | Multi-party notification not exercised (10) | All | IR-6; IR-8; DFARS 252.204-7012(c)-(e); BTTRG 1.6.1; Form 8-K Item 1.05 | Moderate | Contract inventory; CUI steps; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 8 | Agency requirements flowed down at FTI and CJIS buildings | JS, FS | Pub. 1075 2.B.2, 2.B.3.3; CJISSECPOL v6.1 AT-3 | Moderate | Site training modules and supervisor checks | Janitorial and Security operations director | 2026-12-31 |
| 9 | Division supplement drift and inheritance (8, 9) | JS, CN | PL-1; PL-2; SP 800-171 3.12.4 | Moderate | Re-issue supplement; inheritance matrices | Group CISO | 2026-12-31 |
| 10 | AI deployer duties (11) | JS, FS | Colorado SB26-189 | Moderate | P10 conditions before 2027-01-01 | Group Chief Risk Officer | 2026-12-31 |
| 11 | GovRAMP verification of the IBOP | FS (IBOP) | C-GOVERNMENT-R08 | Low | Readiness plan using SSP and SOC 2 evidence | Group building technology director | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-011, POAM-013, and POAM-027 to POAM-030 trace directly to this analysis.

## 6. Pending regulatory changes (not current obligations)
- **FAR overhaul (RFO).** The proposed rule (FR Doc. 2026-12559, June 23, 2026) would move information security clauses into FAR part 40, renumber 52.204-21 as 52.240-5, and add CUI clauses requiring NIST SP 800-171 Rev. 3 and CUI incident reporting within 72 hours of discovery. **Proposed only**; comments closed 2026-07-23. Flagged on the FAR rows. If finalized, Facilities Support and Janitorial and Security would need a CUI program like Construction's for any civilian-agency CUI.
- **CMMC phase-in.** Phase 2 (planned for 2026-11-10) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. Until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). In existing contracts, contracting officers remove these CMMC requirements by modification before the next option period or at the next scheduled administrative modification. 32 CFR 170.3(e) itself is unchanged.
- **NIST SP 800-82 Rev. 4.** Initial public draft published 2026-09-21 (comments due 2026-11-30). **Draft only.** Rev. 3 remains the OT reference. Flagged on the OT rows.
- **CIRCIA.** No final rule as of 2026-09-25. Reporting is voluntary.
- **Colorado SB26-189** takes effect 2027-01-01; federal preemption efforts (EO 14365) continue, so counsel re-checks its status before that date.
