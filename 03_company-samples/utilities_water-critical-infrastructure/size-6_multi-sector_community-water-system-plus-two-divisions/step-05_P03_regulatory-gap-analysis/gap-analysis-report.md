# Regulatory Gap Analysis: Cris Santos Company Holdings | Water and Wastewater Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Water and Wastewater Systems (focus division: Water Utility) |
| Primary regulation | SDWA section 1433, community water system risk and resilience, 42 U.S.C. 300i-2 (as amended by AWIA 2018 section 2013), with the RRA's cyber element benchmarked against NIST CSF 2.0 and NIST SP 800-82 Rev. 3 (September 2023) |
| Division regulations | Water Utility: also the SDWA public notification rule (40 CFR 141 Subpart Q) and 40 CFR 141.31. Construction: DFARS 252.204-7012 with NIST SP 800-171 Rev. 2, the CMMC Program (32 CFR Part 170), and FAR 52.204-21, -23, and -25. Environmental Services: NIST CSF 2.0 as the voluntary baseline, plus FAR 52.204-21, PHMSA hazardous materials security plans (49 CFR 172.800-172.804), and the FTC Disposal Rule (16 CFR 682.3) |
| Gap tables | `gap-analysis.csv` (Water Utility, 52 rows); `gap-analysis-construction.csv` (38 rows); `gap-analysis-environmental-services.csv` (34 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Water Utility Emergency Management Director, and the Construction CMMC program owner, coordinated by the Group Chief Risk Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Water Utility: SDWA section 1433 applies system by system
Section 1433 applies to each **community water system** serving a population **greater than 3,300 persons** (42 U.S.C. 300i-2(a)(1); community water system defined in 42 U.S.C. 300f(15)). It applies to each system, not to the company: the Water Utility holds 58 systems, so it has 42 separate RRA and ERP obligations, each certified to EPA. There is no business-size exemption, and being a large public company changes nothing; population served is the only threshold.

| Size category (population served) | Systems | People served (about) | RRA review deadline (second cycle) | RRA certified | ERP |
|---|---|---|---|---|---|
| 100,000 or more | 6 (including RS-1) | 1,960,000 | 2025-03-31 | 2025-03-26 | Certified 2025-09-22 |
| 50,000 to 99,999 | 9 | 630,000 | 2025-12-31 | 2025-12-17 | Certified 2026-06-15 |
| 3,301 to 49,999 | 27 | 756,000 | 2026-06-30 | 2026-06-24 | **Due by 2026-12-24** (internal target 2026-12-11) |
| 3,300 or fewer | 16 | 26,000 | Not covered by 1433 | n/a | n/a (group standard applies voluntarily) |

Sources: statute text at uscode.house.gov (42 U.S.C. 300i-2(a)(3)(A)-(B) and (b)); EPA "AWIA Section 2013" page, which lists the second-cycle dates and states that ERP certifications are due six months from the date of the RRA certification.

**What the statute does and does not require.** The RRA must assess the resilience of "electronic, computer, or other automated systems (including the security of such systems)" (300i-2(a)(1)(A)(ii)), and the ERP must include strategies to improve "the physical security and cybersecurity of the system" (300i-2(b)(1)). The statute does not prescribe controls, and EPA does not require a particular standard. This analysis uses **NIST CSF 2.0** outcomes, applied to OT through **NIST SP 800-82 Rev. 3**, as the yardstick for whether the cyber element was actually assessed. The 25 benchmark rows (G-020 to G-044) are voluntary outcomes, not separate legal requirements.

**Public notification rule.** All 58 systems are public water systems under 40 CFR Part 141. A cyber-caused failure or significant interruption in key treatment processes is a "waterborne emergency" that requires a **Tier 1 notice no later than 24 hours** after the system learns of it and **primacy agency consultation within 24 hours** (40 CFR 141.202(a) Table 1 item (7), (b)). That is the binding clock the ERPs' cyber procedures must support.

**Excluded, with reasons:** 300i-2(f) (alternative path through EPA-recognized standards; the group certifies under (a) and (b) directly); 300i-2(e) and (g) (EPA duties and grants); wastewater (POTW) rules, because the Water Utility runs no wastewater systems.

### 1.2 Construction: DFARS and CMMC through contracts
- **DFARS 252.204-7012** applies through 14 DoD contracts whose performance involves **covered defense information** (controlled technical information in installation facility drawings). It requires NIST SP 800-171 on every covered contractor information system, FedRAMP Moderate equivalency for any external cloud service holding the information, 72-hour incident reporting ("rapidly report"), malware submission, 90-day image preservation, and flowdown.
- **CMMC (32 CFR Part 170)** applies to DoD contracts involving FCI or CUI. Level 2 uses the 110 requirements of **NIST SP 800-171 Rev. 2** (32 CFR 170.14(c)). The division holds a Final Level 2 (Self) status (2025-12-12) and must affirm continuing compliance annually after the Final status date (170.22(a)(3)(iii)). **Phase 2 (planned for 2026-11-10, 170.3(e)(2)) is suspended** by the DoD (Department of War) CIO memorandum of 2026-07-13. Until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). The 2027-02 C3PAO assessment is now a voluntary choice.
- **FAR 52.204-21** applies to 22 other federal contracts with FCI. **FAR 52.204-25** (covered telecommunications and video surveillance equipment; report within 1 business day, then 10 business days) and **FAR 52.204-23** (Kaspersky covered articles; report within 3 business days, then 10 business days) apply to federal contracts.
- No size exemption applies to any of these clauses. Construction is not a CISA critical infrastructure sector, so CIRCIA would reach it only through another criterion (for example as a DFARS 7012 contractor), and CIRCIA is not in effect anyway.

### 1.3 Environmental Services: a voluntary baseline plus specific binding duties
NAICS 56 has no sector-specific federal cyber mandate, and Environmental Services is not part of the Water and Wastewater Systems Sector (which covers drinking water and wastewater utilities, not NAICS 562 firms). The division therefore uses **NIST CSF 2.0** as its baseline and maps the binding pieces onto it:
- **FAR 52.204-21** for FCI from 31 federal remediation sites held on SYS-E1;
- **49 CFR 172.800-172.804** for the hazardous materials transportation security plan (about 160 trucks haul covered quantities, such as large bulk Class 3 Packing Group I or II materials, 172.800(b)(6));
- **16 CFR 682.3** for disposal of background check reports;
- client contracts and expected SOC 2 commitments for the monitoring service (P09).
FCRA employment procedures (15 U.S.C. 1681b(b)) and Form I-9 retention (8 CFR 274a.2(b)(2)) also apply to the division as an employer, but they are HR process duties handled by group HR and are not analyzed row by row here.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Water Utility | Construction | Environmental Services | Group (corporate) |
|---|---|---|---|---|
| C-WATER-R01 SDWA section 1433 (42 U.S.C. 300i-2) | **Primary.** 42 covered systems | Not applicable (builds for the Water Utility; its work feeds the RRAs as a supplier risk) | Not applicable | Funds and coordinates the RRA program |
| SDWA public notification and reporting (40 CFR 141 Subpart Q; 141.31) | **Applies** to all 58 systems | Not applicable | Not applicable (runs no public water system) | Supports through the notification matrix |
| C-WATER-R02 CIRCIA (proposed 6 CFR Part 226) | Tracked only; would be covered through the water-sector criterion (community water system serving more than 3,300) | Tracked only; possible coverage through another proposed criterion | Tracked only | Tracked only; no obligation until a final rule takes effect |
| N23-R03 DFARS 252.204-7012 with NIST SP 800-171 | Not applicable (no federal contracts) | **Primary.** 14 DoD contracts | Not applicable (no covered defense information) | Group SOC supports 72-hour reporting |
| N23-R04 CMMC (32 CFR Part 170) | Not applicable | **Applies** (Level 2) | Applies at Level 1 if DoD remediation contracts with FCI require it (none currently do) | Not applicable |
| N23-R01 / N56-R07 FAR 52.204-21 | Not applicable | Applies (22 contracts) | **Applies** (31 federal sites) | Common controls support both |
| N23-R02 FAR 52.204-25 and FAR 52.204-23 | Not applicable | Applies | Applies | Group procurement screening |
| N56-R09 PHMSA security plans (49 CFR 172.800-172.804) | Not applicable (receives treatment chemicals; does not offer or transport them) | Not applicable | **Applies** | Not applicable |
| N56-R01 FTC Disposal Rule (16 CFR 682.3) | Applies to background reports (handled by group HR) | Same | **Applies** (driver and technician screening) | Group HR |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Customer personal information in SYS-W2 (each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171) | Employee and certified payroll data | Employee and client contact data | Coordinates |
| State utility commission rules | Applies in each of 6 states (rate regulation; any commission incident rules handled generically and **not verified** here) | Not applicable | Not applicable | Not applicable |
| SOC 2 (contractual) | Not in scope (P09) | Not in scope (P09) | **In scope:** monitoring service (P09) | Group services carved in |

## 3. Method
1. **Requirements.** SDWA rows follow the structure of 42 U.S.C. 300i-2 at paragraph level, quoting the text briefly. Public notification rows follow 40 CFR 141.202, 141.205, 141.31, and 141.33 as read on the eCFR (current through 2026-09-23). DFARS, FAR, CMMC, and PHMSA rows follow the clause or section paragraphs read on the eCFR for the same date. SP 800-171 rows cite the Rev. 2 requirement numbers with short summaries.
2. **Crosswalk.** Benchmark rows (Water Utility G-020 to G-044; Environmental Services CSF rows) use a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); controls added beyond it are named in the `crosswalk_source` column. All other rows carry an **author mapping**, labeled as such, because no official mapping exists for statutory, clause, or regulation text.
3. **Evidence.** Interviews (division leaders, RS-1 operators, the Emergency Management Director, the CMMC program owner, the hazmat compliance manager), document review (RRAs, ERPs, public notice SOPs, the CUI enclave SSP and SPRS record, the hazmat security plan, contracts), configuration exports, and the P07 tests (including a CUI discovery scan and a client gateway audit).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 4. Results
### 4.1 Water Utility (`gap-analysis.csv`)
| Group | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| 300i-2(a) Risk and resilience assessment | 11 | 8 | 3 | 0 | 0 |
| 300i-2(b)-(d), (f) ERP, coordination, records, alternative path | 8 | 2 | 5 | 0 | 1 |
| Cyber element benchmark (CSF 2.0 with SP 800-82r3) | 25 | 6 | 19 | 0 | 0 |
| 40 CFR 141 Subpart Q and 141.31 public notification and reporting | 8 | 6 | 2 | 0 | 0 |
| **Total** | **52** | **22** | **29** | **0** | **1** |

Of the 29 partially met rows, 8 are rated High, 18 Moderate, and 3 Low.

**The main finding.** Every deadline in both cycles was met, and the certifications are correct on their face (G-010, G-011). The weakness is uneven substance. For the 15 largest systems, the cyber element rests on inventories, diagrams, vulnerability data, and this year's risk register. For the 27 mid-size systems certified on 2026-06-24, it was a generic checklist (G-004), and their ERPs, due by 2026-12-24, have no real cyber strategies or OT procedures yet (G-013, G-014). Nine of those 27 are acquired systems, which carry the group's weakest OT: no MFA on remote access (G-028), shared and default credentials (G-027), flat networks (G-037), and no offline controller backups (G-033). The ERP must incorporate the RRA's findings (300i-2(b)), so the cyber addenda must come first.

**A finding inside the strongest system.** RS-1, the best-run system, fails G-029 because of the commissioning exception: Construction engineers have standing, unapproved access into RS-1 through the group gateway. That is a supplier risk the RS-1 RRA did not consider (G-021).

### 4.2 Construction (`gap-analysis-construction.csv`)
| Regulation | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| DFARS 252.204-7012 | 12 | 6 | 6 | 0 | 0 |
| NIST SP 800-171 Rev. 2 (selected requirements) | 19 | 11 | 1 | 7 | 0 |
| CMMC (32 CFR Part 170) | 3 | 0 | 2 | 1 | 0 |
| FAR 52.204-21, -23, -25 | 4 | 3 | 1 | 0 | 0 |
| **Total** | **38** | **20** | **10** | **8** | **0** |

Of the 18 unmet or partially met rows, 9 are rated High and 9 Moderate. The 19 SP 800-171 rows were selected from the 110 requirements: the 7 that P07 found not met, the related assessment requirement (3.12.1), and 11 that were tested and met.

**The main finding: the boundary moved.** The CUI enclave itself is well built. But engineers copied covered defense information to 11 commissioning laptops and into 3 project workspaces on SYS-C1. Under DFARS 7012, any system holding covered defense information is a covered contractor information system, so those laptops and workspaces now fall short of 3.1.3, 3.1.20, 3.5.3, 3.8.7, and 3.12.4, and SYS-C1 fails the cloud requirement in (b)(2)(ii)(D). Separately, a file transfer tool that is not FIPS-validated (3.13.11) and a lapsed weekly log review (3.3.5) were found.

**Why the date matters.** The 2025 Level 2 (Self) assessment recorded all 110 requirements as MET. The Affirming Official must affirm continuing compliance by 2026-12-12 (170.22). A Conditional status with a POA&M is not an option for two of the failures: 3.1.20 and 3.12.4 may not be placed on a CMMC POA&M (170.21(a)(2)(iii)). The fastest path is to purge CUI from the laptops and SYS-C1, which returns them out of scope, then fix 3.3.5 and 3.13.11, and only then affirm. Counsel is reviewing how to correct the SPRS record if remediation is not complete by the date.

### 4.3 Environmental Services (`gap-analysis-environmental-services.csv`)
| Regulation | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FAR 52.204-21 (15 requirements and flowdown) | 16 | 13 | 3 | 0 | 0 |
| PHMSA hazmat security plan (49 CFR 172.800-172.802) | 7 | 4 | 3 | 0 | 0 |
| FTC Disposal Rule (16 CFR 682.3) | 1 | 0 | 1 | 0 | 0 |
| NIST CSF 2.0 baseline for the monitoring service | 10 | 4 | 6 | 0 | 0 |
| **Total** | **34** | **21** | **13** | **0** | **0** |

Of the 13 partially met rows, 2 are rated High, 8 Moderate, and 3 Low.

**The main findings.** The monitoring platform is sound; its edge is not. Twenty-three of about 210 client site gateways had default local web credentials, four of them at federal sites whose data is FCI (52.204-21(b)(1)(vi); CSF PR.AA-01). The service has no written commitments to clients (GV.OC-03), which blocks a SOC 2 report (P09) and leaves client incident notices undefined (RS.CO-02). The hazmat security plan is current, but its risk assessment does not consider that route, load, and schedule data in SYS-E2 could be stolen or altered (172.802(a)).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Commissioning access into RS-1 without per-session approval or contract terms (1) | WU, CN | CSF PR.AA-05, GV.SC-05 (G-021, G-029); 252.204-7012 does not apply to this path | High | Revoke the exception; security schedule in the intercompany contract; laptop standard | Group OT Security Director | 2026-12-31 |
| 2 | Cyber element of 27 RRAs and their ERPs (3) | WU | 300i-2(a)(1)(A)(ii); (b)(1)-(2) (G-004, G-013, G-014) | High | Cyber addenda by 2026-11-20; revised ERPs certified by 2026-12-11 | Water Utility Emergency Management Director | 2026-12-24 |
| 3 | Acquired systems' remote access, credentials, segmentation, backups (2) | WU | CSF PR.AA-01, PR.AA-03, PR.DS-11, PR.IR-01 (G-027, G-028, G-033, G-037) | High | Integration program | Water Utility security and compliance lead | 2027-06-30 |
| 4 | CUI outside the enclave and an inaccurate CMMC record (4) | CN | 252.204-7012(b)(2); SP 800-171 3.1.3, 3.1.20, 3.12.4; 32 CFR 170.16, 170.22 | High | Purge and block; correct the self-assessment; then affirm | Construction president | 2026-12-12 |
| 5 | Client gateway credentials and service commitments (5) | ES | 52.204-21(b)(1)(vi); CSF PR.AA-01, GV.OC-03 | High | Reset and harden gateways; write commitments | Environmental Services remote monitoring general manager | 2026-12-31 |
| 6 | Multi-regulator notification not exercised (6) | All | 141.202(b); 252.204-7012(c); Form 8-K Item 1.05 (G-041, G-042, G-045) | Moderate | Cyber trigger in all PN SOPs; cross-division tabletop | Group General Counsel with the VP of Water Quality and Compliance | 2026-12-15 |
| 7 | Inheritance undocumented for Construction and Environmental Services (7) | CN, ES | SP 800-171 3.12.4 (system description); CSF GV.RR | Moderate | Inheritance matrices | Group CISO | 2026-12-31 |
| 8 | Hazmat security plan lacks cyber risks | ES | 49 CFR 172.802(a) | Moderate | Cyber section in the risk assessment | Environmental Services hazmat compliance manager | 2026-12-31 |
| 9 | Local purchases not screened for covered equipment | CN | 52.204-25(b) | Moderate | Screening at job sites | Construction procurement director | 2026-12-31 |

**Key milestones:** 2026-10-31 commissioning exception revoked; 2026-11-20 RRA cyber addenda; 2026-11-30 CUI purge verified and gateways hardened; 2026-12-11 revised ERPs certified (latest allowed 2026-12-24); 2026-12-12 CMMC affirmation decision; 2026-12-15 cross-division tabletop.

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-024 to POAM-027 trace directly to this analysis).

## 6. Pending regulatory changes
- **CIRCIA** (6 U.S.C. 681-681g; proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024) is **still proposed**. No final rule had been published as of 2026-09-25. If finalized as proposed, the group would be a covered entity (it exceeds the SBA size standard and operates community water systems serving more than 3,300 people). It would then need to report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours, and preserve related data. Rows G-036, G-041, and G-042 are flagged. None of this is treated as a current obligation.
- **CMMC phases:** Phase 2 (planned for 2026-11-10) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. 32 CFR 170.3(e) still lists Phase 3 (2027-11-10) and Phase 4 (2028-11-10), but clause inclusion follows DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5): until 2028-11-09 only where a program office requires a specific CMMC level.
- **NIST SP 800-171 Rev. 3** is final, but CMMC Level 2 assesses **Rev. 2** (32 CFR 170.14(c)). The division tracks Rev. 3 but implements and assesses Rev. 2.
- **FAR overhaul:** proposed FAR rules published in 2026 may renumber clauses such as 52.204-21; the substance of current contracts is unchanged until clauses are modified.
- **EPA sanitary survey cybersecurity memorandum** (2023): withdrawn in October 2023 according to the vertical profile. Not relied on here.
