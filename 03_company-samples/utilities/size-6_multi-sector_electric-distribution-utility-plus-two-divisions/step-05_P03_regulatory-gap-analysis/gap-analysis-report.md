# Regulatory Gap Analysis: Cris Santos Company Holdings | Utilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Utilities (focus division: Electric Utility) |
| Primary regulation | NERC CIP Reliability Standards under Federal Power Act section 215 (16 U.S.C. 824o), at **medium impact** (TCC and backup TCC) and **low impact** (74 transmission substations) |
| Secondary (Electric Utility) | Electric incident and event reporting: NERC **EOP-004-4** and Form **DOE-417** |
| Division regulations | Gas Production: no binding federal sector cyber rule; NIST CSF 2.0 with SP 800-82 Rev. 3 as a voluntary benchmark, plus applicability screens. Engineering Services: client contract flow-down of NERC CIP terms, CEII handling, and FAR 52.204-21 |
| Group-wide | SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach notification laws (Florida worked example); OFAC sanctions screening before any ransom payment |
| Versions checked | NERC CIP standards page (nerc.com), retrieved 2026-09-26: CIP-002-5.1a, CIP-003-9 (effective 2026-04-01), CIP-004-7, CIP-005-7, CIP-006-6, CIP-007-6, CIP-008-6, CIP-009-6, CIP-010-4, CIP-011-3, CIP-012-2 (effective 2026-07-01), CIP-013-2, CIP-014-3 mandatory and enforceable; standard texts read from the NERC PDFs. eCFR current through 2026-09-23 for 18 CFR 388.113, 49 CFR 192.1, 16 CFR 314, and 48 CFR 52.204-21 |
| Gap tables | `gap-analysis.csv` (Electric Utility, 85 rows); `gap-analysis-gas-production.csv` (38 rows); `gap-analysis-engineering-services.csv` (36 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31; Electric Utility rows updated with P07 test results to 2026-08-28 |
| Assessors | Division security and compliance leads with the Electric Utility NERC compliance director, coordinated by the Group CISO's GRC team; reviewed by group internal audit |

## 1. Applicability
### 1.1 Electric Utility: NERC CIP applies at medium and low impact
1. **Who must comply.** Section 215 of the Federal Power Act requires users, owners, and operators of the bulk-power system to comply with approved Reliability Standards (16 U.S.C. 824o(b)(1)). NERC enforces through the Regional Entities; for Florida that is SERC, which took over the former FRCC footprint in 2019.
2. **Registration.** The Electric Utility is registered as Distribution Provider, Transmission Owner, and Transmission Operator. As a TO and TOP, every CIP standard's applicability section reaches it; as a DP, the narrower DP applicability applies only to UFLS, UVLS, RAS, Protection Systems, and Cranking Paths, which add nothing here.
3. **Impact rating (CIP-002-5.1a Attachment 1).**

| Criterion | Test | Company fact | Result |
|---|---|---|---|
| 1.3 (high) | Control Center performing TOP functions for assets meeting 2.2, 2.4, 2.5, 2.7, 2.8, 2.9, or 2.10 | No such assets (below) | Not met |
| 2.4 | Transmission Facilities at 500 kV or higher | Highest voltage 230 kV | Not met |
| 2.5 | 200 kV to 499 kV station connected to 3 or more other stations with an aggregate weighted value above 3000 (230 kV lines weigh 700) | No 230 kV station connects to more than four other 230 kV stations; highest value 2,800 | Not met |
| 2.6, 2.9 | Facilities critical to IROLs; RAS that could cause IROL violations | None identified by the RC, PC, or TP | Not met |
| 2.8 | Transmission Facilities that interconnect a plant meeting 2.1 or 2.3 | No GO has notified a qualifying plant; the largest interconnected plant is 1,240 MW | Not met |
| 2.10 | UFLS or UVLS under a common control system shedding 300 MW or more | Feeder UFLS relays act independently at each substation | Not met |
| **2.12 (medium)** | **Control Center or backup Control Center performing TOP functions, not rated high** | **TCC and backup TCC** | **Medium impact** |
| 3.2 (low) | Transmission stations and substations | 74 transmission substations | Low impact |

4. **What is out of CIP scope.** The DCCs and the DOP are not Control Centers: the NERC Glossary limits "Control Center" to RC, BA, TOP, and GOP functions, and the DCCs perform only distribution operations on Facilities below 100 kV. The AMI, CIS, and distribution substations are also outside. These are held to the group's voluntary benchmark in the SSP (P02) and the P07 assessment. **The exception that matters:** at the 74 transmission substations, the DOP polls gateways that are part of the low impact BES Cyber Systems, so DOP traffic there must meet CIP-003-9 Attachment 1 Section 3.1, and vendor access to those substations through SYS-G4 must meet Section 6.
5. **Standards that do not apply.** CIP-014-3 applies only to TOs with stations meeting Applicability 4.1.1 (the same voltage and weighted-value tests as criteria 2.4 to 2.7); none qualifies. Parts that apply only to high impact systems are kept as Not applicable rows so the decision is visible. CIP-015-1 is approved but not yet effective.

**Secondary regulation (Electric Utility).**
- **EOP-004-4** lists the TO, TOP, and DP as responsible entities. It requires an event reporting Operating Plan (R1) and reports by the later of 24 hours or the end of the next business day (R2). Because the 2025 peak was above 3,000 MW, the uncontrolled firm load loss threshold is 300 MW for 15 minutes or more.
- **Form DOE-417** is mandatory under section 13(b) of the Federal Energy Administration Act of 1974 (Pub. L. 93-275). Criteria were read from the OMB-approved form and instructions (OMB 1901-0288; approval expires 2027-05-31): Emergency Alert within 1 hour (criteria 1-9, including 2, a Reportable Cyber Security Incident, and 3, a cyber event that interrupts electrical system operations); Normal Report within 6 hours (criteria 10-13, including 11, a cyber event that could affect reliability, and 12, loss of service to more than 50,000 customers for 1 hour or more); Attempted Cyber Compromise by the end of the next calendar day after determination (criterion 14); final report within 72 hours.

### 1.2 Gas Production: no binding federal sector cyber rule
| Candidate requirement | Applicability test | Decision |
|---|---|---|
| N21-R01 USCG Marine Transportation System cyber rule (33 CFR Part 101, Subpart F) | MTSA vessels and facilities and OCS facilities (101.605) | Not applicable: onshore only |
| N21-R02 TSA SD Pipeline-2021-02G | TSA-notified owners and operators of critical pipelines | Not applicable: no pipeline; no TSA notice (counsel confirmation 2026-06-30) |
| PHMSA gas pipeline safety (49 CFR Part 192) | Part 192 does not apply to onshore gathering through a pipeline that is not a regulated onshore gathering line as determined in 192.8 (192.1(b)(4)) | Not applicable to the division as an operator: custody passes at pad and central delivery point meters to third-party gatherers, who operate the downstream lines |
| N21-R03 CIRCIA (proposed 6 CFR Part 226) | Final rule required | Not in effect as of 2026-09-25 |

**Why a voluntary benchmark.** With no binding sector rule, Gas Production's obligations come from state breach laws (royalty owner and employee data), the group's SEC duties, and its contracts (firm supply contracts with generators, the SCADA integrator contract). The division uses NIST CSF 2.0 with SP 800-82 Rev. 3, the group's OT benchmark. In 2026 it assessed the 33 CSF 2.0 subcategories that the group OT standard marks as core for field SCADA; a full 106-subcategory profile is scheduled for 2027.

### 1.3 Engineering Services: obligations arrive by contract
NERC CIP standards apply to registered entities, not to their vendors. They reach Engineering Services through its **clients' contracts**: clients put their CIP-004-7 (training and personnel risk assessments), CIP-011-3 (BES Cyber System Information handling), CIP-013-2 Part 1.2 (vendor notices, access revocation, vulnerability disclosure, software integrity, remote access coordination), and CIP-010-4 R4 or CIP-003-9 Section 5.2 (Transient Cyber Assets) obligations into service agreements. 37 of its client contracts contain such terms.

| Candidate requirement | Decision |
|---|---|
| N54-R01 FTC Safeguards Rule (16 CFR Part 314) | **Not applicable.** The rule covers financial institutions under FTC jurisdiction (314.1(b)); an institution is one whose business is an activity that is financial in nature under 12 U.S.C. 1843(k) (314.2). Engineering is not |
| N54-R04 FAR 52.204-21 | **Applies** to federal civilian contracts that involve Federal Contract Information |
| FAR 52.204-25 and 52.204-23 | **Apply** to the same contracts (reporting clocks in P08) |
| N54-R05 DFARS 252.204-7012 and CMMC | Not applicable: no DoD contracts |
| N54-R06 HIPAA business associate | Not applicable: no PHI |
| CEII, 18 CFR 388.113 | Applies as a route: non-employee agents may obtain an owner's CEII from FERC only with the owner's written authorization (388.113(g)(1)); clients' CEII terms then govern handling |

**Holding company and affiliate rules (context, not cyber rules).** FERC's holding company rules (18 CFR 366.2 to 366.4), its rule on affiliate purchases by a transmission-owning utility (18 CFR 35.44(b)(2)), and the Florida PSC affiliate transaction rule (Fla. Admin. Code R. 25-6.1351) govern how the Electric Utility prices and records what it buys from its sister divisions. They are not security requirements, so they are not scored here. They matter here because the intercompany agreements behind those purchases are also where the group's security terms for its sister divisions belong (see `00_company-facts.md`).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Electric Utility | Gas Production | Engineering Services | Group (corporate) |
|---|---|---|---|---|
| N22-R01 NERC CIP | **Primary.** Medium impact (TCC) and low impact (74 substations) | Not applicable (not registered) | By contract only (37 client contracts; affiliate vendor to the Electric Utility) | SYS-G4 and group HR, training, and procurement support the Electric Utility's CIP program |
| NERC EOP-004-4; Form DOE-417 | Applies (TO, TOP, DP; electric utility) | Not applicable | Not applicable | Not applicable |
| N22-R02 TSA pipeline directives | Not applicable (no pipelines) | Not applicable (no pipeline; no TSA notice) | Not applicable | Not applicable |
| PHMSA 49 CFR Part 192 | Not applicable | Not applicable as operator (third-party gatherers) | Not applicable | Not applicable |
| N22-R03 NRC 10 CFR 73.54; N22-R04 SDWA 1433 | Not applicable (no reactors, no water systems) | Not applicable | Not applicable | Not applicable |
| N21-R01 USCG MTS cyber rule | Not applicable | Not applicable (onshore) | Not applicable | Not applicable |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | DOP, AMI, distribution substations (P02, P07) | **Primary benchmark** | Not used (SOC 2 instead) | Group policy framework |
| CEII (18 CFR 388.113) | Its own CEII; FERC filings | Not applicable | Handles client CEII under authorizations and NDAs | Not applicable |
| N54-R04 FAR 52.204-21; 52.204-25; 52.204-23 | Not applicable (no federal contracts) | Not applicable | **Applies** (federal civilian contracts) | Not applicable |
| N54-R01 FTC Safeguards Rule | Not applicable | Not applicable | Not applicable (not a financial institution) | Not applicable |
| SOC 2 (contractual assurance) | Out of scope (P09); vendor SOC 2 reviews | Out of scope | **In scope:** Type 1 issued; Type 2 period from 2027-01-01 (P09) | Group services carved in |
| SEC Form 8-K Item 1.05; Reg S-K Item 106 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Customer data in the CIS (Florida) | Royalty owners and employees in each state where they reside | Employees in 22 states | Coordinates; Florida worked example (Fla. Stat. 501.171) |
| N21-R03 / N54-R09 CIRCIA (proposed) | Tracked only | Tracked only | Tracked only | Tracked only |

## 3. Method
1. **Requirements.** NERC rows follow each standard's own structure (requirement, part, Attachment 1 section). Summaries are written in this repository's own words. The requirement type column records each requirement's Violation Risk Factor as stated in the standard. Gas Production rows quote CSF 2.0 subcategories. Engineering Services rows follow the clauses of the FAR and the contract terms that flow down from clients' CIP programs.
2. **Crosswalk.** NERC rows and contract rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5; NIST has not published a mapping for NERC CIP. Gas Production rows use NIST's official CSF 2.0 informative references (full list in `nist_official_sp800_53r5`), with the key-control selection and the SP 800-82 Rev. 3 section as author mappings.
3. **Evidence.** Interviews; CIP evidence binders; gateway and firewall rule exports; SYS-G4 and SYS-S1 permission reports; walkthroughs of the TCC, backup TCC, 6 transmission substations, the Gas Production POC, and 3 compressor stations; contract reviews; P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 4. Results
### 4.1 Electric Utility (`gap-analysis.csv`)
| Standard | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CIP-002-5.1a | 5 | 1 | 0 | 0 |
| CIP-003-9 | 12 | 3 | 0 | 0 |
| CIP-004-7 | 8 | 3 | 0 | 0 |
| CIP-005-7 | 7 | 0 | 0 | 1 |
| CIP-006-6 | 4 | 0 | 0 | 1 |
| CIP-007-6 | 5 | 0 | 0 | 1 |
| CIP-008-6 | 3 | 1 | 0 | 0 |
| CIP-009-6 | 3 | 0 | 0 | 1 |
| CIP-010-4 | 4 | 0 | 0 | 1 |
| CIP-011-3 | 2 | 1 | 0 | 0 |
| CIP-012-2 | 1 | 2 | 2 | 0 |
| CIP-013-2 | 4 | 1 | 0 | 0 |
| CIP-014-3; CIP-015-1 | 0 | 0 | 0 | 2 |
| EOP-004-4 | 2 | 0 | 0 | 0 |
| Form DOE-417 | 2 | 2 | 0 | 0 |
| **Total (85)** | **62** | **14** | **2** | **7** |

Of the 16 unmet or partially met rows, 6 are rated High, 8 Moderate, and 2 Low.

**The medium impact program is mature.** CIP-005 to CIP-010 for the TCC had no gaps; the three 2024 audit findings stayed fixed. **The gaps sit at the edges:** where the DOP and SYS-G4 reach into low impact substations, where the Electric Utility's BCSI sits on an affiliate's platform, and where a standard changed in 2026.

**Potential noncompliance to self-report.** Six rows (four issues) describe potential violations of an enforceable standard, not only weaknesses:
- CIP-003-9 Attachment 1 Section 3.1 (G-011): gateway rules allow any protocol from the DOP front-end processors at all 74 substations, since the 2024 ADMS cutover
- CIP-003-9 Attachment 1 Section 6.3 (G-019): no detection method for vendor remote access at 43 substations since 2026-04-01
- CIP-004-7 R6 Part 6.1 (G-031) and CIP-011-3 R1 Part 1.2 (G-066): TCC BCSI on the Engineering Services project platform outside the access and handling program
- CIP-012-2 R1 Parts 1.2 and 1.3 (G-069, G-070): availability and recovery methods missing from the plan since 2026-07-01

The CIP Senior Manager decided on 2026-09-15 to **self-report** them to SERC by 2026-09-30, with mitigation plans. A "Self-Report" is the Compliance Monitoring and Enforcement Program term (NERC Rules of Procedure Appendix 4C) for a registered entity reporting that it has, or may have, violated a standard.

### 4.2 Gas Production (`gap-analysis-gas-production.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| GOVERN (6 core subcategories) | 1 | 3 | 2 | 0 |
| IDENTIFY (7) | 1 | 6 | 0 | 0 |
| PROTECT (13) | 1 | 9 | 3 | 0 |
| DETECT (3) | 1 | 0 | 2 | 0 |
| RESPOND (2) | 0 | 2 | 0 | 0 |
| RECOVER (2) | 0 | 1 | 1 | 0 |
| **CSF 2.0 subtotal (33)** | **4** | **21** | **8** | **0** |
| Applicability screens (4) | 0 | 0 | 0 | 4 |
| State breach laws (1) | 0 | 1 | 0 | 0 |
| **Total (38)** | **4** | **22** | **8** | **4** |

Of the 30 unmet or partially met rows, 2 are rated High, 17 Moderate, and 11 Low. The two High gaps are internet-exposed well pad modems (PR.IR-01) and Engineering Services access to the POC through SYS-G4 (PR.AA-05). The pattern is a division that has physical and safety controls but almost no OT cyber controls, and a 2023 standard that predates the group's OT program.

### 4.3 Engineering Services (`gap-analysis-engineering-services.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Client contract flow-down (CIP-004, CIP-010, CIP-011, CIP-013 terms), CEII, intercompany agreement, SOC 2 description, AI confidentiality (15) | 2 | 10 | 3 | 0 |
| FAR 52.204-21 (15 requirements) and FAR 52.204-25 and 52.204-23 reporting (16) | 15 | 1 | 0 | 0 |
| Applicability screens: FTC Safeguards, DFARS and CMMC, HIPAA, CIRCIA (4) | 0 | 0 | 0 | 4 |
| State breach laws (1) | 0 | 1 | 0 | 0 |
| **Total (36)** | **17** | **12** | **3** | **4** |

Of the 15 unmet or partially met rows, 3 are rated High, 9 Moderate, and 3 Low. **Not met:** no process or register for client incident notices (CIP-013-2 Part 1.2.1 terms, scenario gap 4); no security schedule in the intercompany agreement with the Electric Utility; client documents sent to the AI design assistant pilot without client consent (gap 5). Federal contract safeguarding is in good shape because SYS-S1's SOC 2 controls already cover the 15 basic requirements.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Shared OT remote access with standing affiliate access and incomplete vendor-session detection (1) | EU, GP, ES | CIP-003-9 Att. 1 Sec. 6.3; client CIP-013-2 Part 1.2.6 terms; CSF PR.AA-05 | High | Per-session approval; no standing access; detection at all 74 substations | Group OT security director | 2026-12-31 (detection); 2027-03-31 (access) |
| 2 | Electric Utility BCSI and client CEII and BCSI on the project platform (5) | EU, ES | CIP-004-7 R6; CIP-011-3 R1; client CIP-011-3 terms; 18 CFR 388.113 | High | Restricted folders with authorized access lists; block personal storage; self-report | Electric Utility NERC compliance director; Engineering Services security and compliance lead | 2026-11-30 (EU BCSI); 2026-12-31 (clients) |
| 3 | DOP traffic into low impact substations broader than necessary (2) | EU | CIP-003-9 Att. 1 Sec. 3.1 | High | DNP3-only rules; change procedure check; self-report | Electric Utility substation engineering manager | 2026-11-30 |
| 4 | Gas well pad modems on public IP addresses (6) | GP | CSF PR.IR-01; SP 800-82r3 5.2.3 | High | Private APN for all modems | Gas Production SCADA and automation manager | 2026-12-31 |
| 5 | CIP-012-2 availability and recovery (3) | EU | CIP-012-2 R1 Parts 1.2-1.5 | Moderate | Update the plan and agreements with the RC and TOPs; self-report | Electric Utility system operations director | 2026-12-31 |
| 6 | Cross-division notification not exercised; DCC lacks DOE-417 cyber criteria; no client notice register (4, 9) | All | DOE-417 criteria 2, 3, 11; CIP-008-6 R1; client CIP-013-2 Part 1.2.1 terms; Form 8-K Item 1.05 | Moderate to High | Complete the matrix; DCC checklist; client notice register; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 7 | Gas Production supplement drift and undocumented inheritance (6, 7) | GP, ES | CSF GV.PO-01, GV.PO-02 | Moderate | Re-issue the supplement; inheritance matrices for GP and ES | Group CISO | 2026-12-31 |
| 8 | Affiliate vendor treated less rigorously (4) | EU, ES | CIP-013-2 R2; intercompany agreement | Moderate | OT security schedule in the intercompany agreement; full vendor assessment of Engineering Services | Group procurement director | 2027-03-31 |
| 9 | AI design assistant used with client documents (5) | ES | Client confidentiality terms | Moderate | Block CEII and BCSI uploads; client consent clause | Engineering Services chief operating officer | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-012 to POAM-015 trace directly to the Electric Utility rows above; POAM-011 traces to G-076 and ES-G13.

## 6. Pending regulatory changes
None of these is treated as a current obligation. Dates are from the NERC CIP standards page (retrieved 2026-09-26) and the vertical research files. The `pending_rule_change` column flags affected rows.
- **Virtualization revisions, 2028-07-01:** CIP-002-8 (and CIP-002-7), CIP-003-10, CIP-004-8, CIP-005-8, CIP-006-7.1, CIP-007-7.1, CIP-008-7.1, CIP-009-7.1, CIP-010-5, CIP-011-4.1, and CIP-013-3. The TCC runs virtualized EMS servers, so the definitions of Shared Cyber Infrastructure and the new ESP options will need a design review in 2027.
- **CIP-003-11, 2029-07-01:** rewrites low impact electronic access controls for all routable access, not only vendor access. The detection and access work in roadmap items 1 and 3 is designed to meet it early.
- **CIP-014-4, 2028-10-01**, and **CIP-015-1, 2028-10-01** (internal network security monitoring; CIP-015-2 on 2029-10-01). Recheck applicability for the TCC before the effective dates.
- **EOP-004-5, 2027-10-01:** update the event reporting Operating Plan.
- **DOE-417:** the current OMB approval expires 2027-05-31. Check for a revised form.
- **CIRCIA:** no final rule as of 2026-09-25. If finalized as proposed, the group would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours.
- **TSA surface cyber risk management rule** (NPRM 2024-11-07): not final; relevant to Gas Production only if it ever operates a pipeline TSA designates.
- **Watch item:** DOE issued a request for information (FR Doc. 2026-18370, 2026-09-09) implementing an executive order on bulk-power system security (foreign-adversary equipment and supply chain). It is not a requirement today; the Electric Utility's CIP-013-2 plan owner tracks it.
