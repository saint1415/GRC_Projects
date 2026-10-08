# Regulatory Gap Analysis: Cris Santos Company Holdings | Critical Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Critical Manufacturing (focus division: Transformer Manufacturing, NAICS 335311) |
| Primary benchmark (focus division) | NIST Cybersecurity Framework 2.0 (CSWP 29, 2024-02-26) with NIST SP 800-82 Rev. 3 (OT, 2023-09). Voluntary: no binding sector-wide cyber rule exists for critical manufacturing |
| Binding duties (focus division) | FAR 52.204-21, -23, -25, and -30 in 14 federal contracts; the Utility Supplier Cyber Security Addendum in 140 utility contracts (flow-down of NERC CIP-013-2 R1 Part 1.2 topics); EAR recordkeeping |
| Division regulations | Electric Utility: NERC CIP (medium and low impact), EOP-004-4, Form DOE-417. Grid Engineering: NERC CIP terms flowed down by 41 client contracts, FERC CEII procedures, FAR 52.204-21, SOC 2 commitments |
| Group-wide | SEC Form 8-K Item 1.05 and Regulation S-K Item 106; state breach notification laws; OFAC (P08) |
| Gap tables | `gap-analysis.csv` (Transformer Manufacturing and group-wide, 103 rows); `gap-analysis-electric-utility.csv` (53 rows); `gap-analysis-engineering.csv` (28 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28). Regulatory text re-checked 2026-10-05 |
| Assessors | Division security and compliance leads, the Electric Utility NERC compliance director, and the Grid Engineering contracts director, coordinated by the Group CISO; reviewed by group internal audit |

## 1. Applicability
### 1.1 Who is what
| Entity | Status | Basis |
|---|---|---|
| Transformer Manufacturing | **Not NERC-registered.** A supplier to about 700 utilities. NERC CIP-013-2 applies to the Responsible Entities in its section 4.1, not to their vendors, so CIP terms reach the division only through contracts: the 140 utility addenda and the 2019 intercompany supply agreement with the Electric Utility | CIP-013-2 section 4.1; contract register |
| Electric Utility | **NERC-registered** Distribution Provider, Transmission Owner, and Transmission Operator in the SERC region. Medium impact BES Cyber Systems at the TCC and backup TCC (CIP-002-5.1a Attachment 1 criterion 2.12); low impact at 58 transmission substations (criterion 3.2) | CIP-002-5.1a categorization approved 2025-11-18 |
| Grid Engineering | **Not NERC-registered.** A vendor to 41 client utilities whose contracts flow down CIP-004-7, CIP-011-3, CIP-013-2, and Transient Cyber Asset terms, and a vendor to the Electric Utility under its CIP-013-2 plan | Contract review 2026-07 |
| Corporate shared services | Common control provider for all three divisions (P02). Not inside any Electronic Security Perimeter | P02 common control catalog |
| Holding company | SEC registrant (not a smaller reporting company) | Form 8-K Item 1.05; 17 CFR 229.106 |

**Why the focus division uses a voluntary benchmark.** The vertical's registry (`02_industry-rules/manufacturing_critical-manufacturing/requirements.csv`) lists four requirements. None is a binding cyber rule for a transformer maker of this kind: CIRCIA is proposed only (C-CRITICAL-MFG-R01), the connected vehicles rule does not reach transformers (R02), EAR applies to exports but is not a cyber program rule (R03), and DFARS 252.204-7012 needs a DoD contract, which the group does not hold (R04). The group therefore measures Manufacturing against CSF 2.0 with SP 800-82 Rev. 3, and assesses the binding contract and FAR duties line by line beside it. There is no size exemption to think about: the benchmark is the group's choice, and the contract and FAR duties have no size threshold.

### 1.2 Excluded or screened requirements
- **DFARS 252.204-7012 and CMMC (C-CRITICAL-MFG-R04; N54-R05):** no DoD contracts in any division; the bid review gate stops any bid that would flow them down (G-101, ES-G25).
- **Connected vehicles rule (C-CRITICAL-MFG-R02):** no vehicles or vehicle connectivity systems (G-099).
- **CIRCIA (C-CRITICAL-MFG-R01; N54-R09):** not in effect; the Federal Register shows no final rule as of 2026-10-05 (G-098, EU-G53, ES-G28).
- **CIP-014-3:** no Electric Utility transmission station meets Applicability 4.1.1 (EU-G42). **CIP-015-1:** not yet effective (EU-G43).
- **Other utility registry rows** (TSA pipeline directives N22-R02, NRC 10 CFR 73.54 N22-R03, SDWA section 1433 N22-R04): no pipeline, no generation or NRC license, no water system (EU-G50 to EU-G52).
- **Professional services registry rows** for Grid Engineering (FTC Safeguards Rule N54-R01, tax preparer rules N54-R02 and R03, HIPAA N54-R06): the division is not a financial institution, prepares no tax returns, and holds no PHI (ES-G23, ES-G24, ES-G26). N54-R07 and N54-R08 (professional conduct rules for lawyers and CPAs, both unverified in the registry) were not relied on; they do not fit an engineering firm.

**Holding company and affiliate rules (context, not cyber rules).** FERC's holding company rules (18 CFR 366.2 to 366.4), its rule on affiliate purchases by a transmission-owning utility (18 CFR 35.44(b)(2)), and the Florida PSC affiliate transaction rule (Fla. Admin. Code R. 25-6.1351) govern how the Electric Utility prices and records what it buys from its sister divisions. They are not security requirements, so they are not scored here. They matter here because the intercompany agreements behind those purchases are also where the group's security terms for its sister divisions belong (see `00_company-facts.md`).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Transformer Manufacturing | Electric Utility | Grid Engineering | Group (corporate) |
|---|---|---|---|---|
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | **Primary benchmark** (G-001 to G-070) | Benchmark for systems outside CIP scope (DCC, ADMS, AMI, CIS, distribution substations) | Benchmark through group policy | Basis of group policy v2026 (P06) |
| N22-R01 NERC CIP (CIP-002 to CIP-013) | Not registered. Reaches the division through 140 utility addenda (G-091 to G-096) and the affiliate supply agreement (G-002) | **Primary.** Medium impact (TCC) and low impact (58 substations) (EU-G01 to EU-G41) | Not registered. Reaches the division through 41 client contracts (ES-G01 to ES-G12) and the Electric Utility's CIP-004-7 and CIP-013-2 programs | Not a BES Cyber System, EACMS, or PACS provider. Group SOC supports CIP-008-6 detection; group identity is not used inside ESPs |
| NERC EOP-004-4; Form DOE-417 | Not applicable | **Applies** (EU-G44 to EU-G49) | Not applicable | Group SOC feeds facts to the utility's reporting desk (P08) |
| FERC CEII procedures (18 CFR 388.113) | Not applicable (no CEII requests) | Applies as owner and operator of its own facilities | **Applies** to CEII requests made as a client's agent (ES-G13) | Not applicable |
| Utility addenda and client CIP flow-down terms | **Applies** (140 utilities; 24- and 48-hour incident notice) | Buyer side: imposes these terms on its vendors, including both affiliates (EU-G39) | **Applies** (41 clients; 24- to 72-hour incident notice) | Group SOC findings must reach both divisions' notice teams (P08) |
| N54-R04 FAR 52.204-21; 52.204-23; 52.204-25 | **Applies** (14 contracts; G-071 to G-089). 52.204-30 in 9 contracts (G-090) | Not applicable (no federal contracts) | **Applies** (federal civilian contracts; ES-G14 to ES-G19) | Common controls carry most of the 15 requirements |
| C-CRITICAL-MFG-R03 EAR | **Applies** (EAR99 exports; records 15 CFR 762.6(a)) (G-100) | Not applicable (no exports) | Not applicable (no exports of controlled technology) | GEPS export screening |
| C-CRITICAL-MFG-R01 CIRCIA (proposed) | Tracked only; would be covered by the manufacturing sector criterion if finalized as proposed | Tracked only | Tracked only | Tracked only; one group report if it comes into force |
| C-CRITICAL-MFG-R02 connected vehicles; C-CRITICAL-MFG-R04 DFARS | Not applicable | Not applicable | Not applicable | Bid review gate |
| SOC 2 (contractual) | FMS: first Type 2 readiness (P09) | Not in scope (P09) | Client project platform: existing Type 2 (ES-G20 to ES-G22) | Group services carved in |
| SEC Form 8-K Item 1.05; Reg S-K Item 106 | Via group | Via group | Via group | **Applies** (G-103) |
| State breach notification laws | Employee and applicant data | Customer data for 1.4 million meters (names, Social Security numbers for credit decisions, bank account numbers) | Employee data | Coordinates; Florida is the worked example (Fla. Stat. 501.171) (G-102) |
| OFAC sanctions check before any ransom payment | Via group | Via group | Via group | **Applies** (P08) |

## 3. Method
1. **Requirements.** CSF 2.0 rows use the official CSF 2.0 subcategory text; SP 800-82 Rev. 3 section numbers show where the OT guidance applies. FAR rows were read from the eCFR (current through 2026-09-23). NERC rows were read from the standard PDFs published by NERC; the FERC CEII row from 18 CFR 388.113 on the eCFR. Form DOE-417 rows use the OMB-approved form and instructions. Contract rows follow the six CIP-013-2 R1 Part 1.2 topics, because the addenda and client terms are built on them.
2. **Crosswalk.** CSF rows use NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/`), as a subset. Every other row carries an **author mapping**, labeled as such in the `crosswalk_source` column. SOC 2 rows list Trust Services Criteria IDs with short topic labels in our own words; no criteria text is reproduced.
3. **Evidence.** Interviews, document review, configuration exports, plant walkthroughs at P2, P5, and P8 (2026-06-09 to 2026-06-12), the TCC walkthrough (2026-06-17), contract reviews, and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale (Very Low to Very High).

## 4. Results
### 4.1 Transformer Manufacturing and group-wide rows (`gap-analysis.csv`)
| Group of rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (20) | 12 | 8 | 0 | 0 |
| CSF 2.0 Identify (16) | 7 | 9 | 0 | 0 |
| CSF 2.0 Protect (18) | 7 | 11 | 0 | 0 |
| CSF 2.0 Detect (6) | 3 | 3 | 0 | 0 |
| CSF 2.0 Respond (5) | 2 | 2 | 1 | 0 |
| CSF 2.0 Recover (5) | 0 | 5 | 0 | 0 |
| FAR 52.204-21, -25, -23, -30 (20) | 17 | 3 | 0 | 0 |
| Utility addenda (6) | 2 | 4 | 0 | 0 |
| EAR, state breach laws, SEC (3) | 1 | 2 | 0 | 0 |
| Screens: CIP-013-2 direct, CIRCIA, connected vehicles, DFARS (4) | 0 | 0 | 0 | 4 |
| **Total (103)** | **51** | **47** | **1** | **4** |

14 gaps are rated High. They sit in four places:
- **The acquired plant P8** (scenario gap 2): asset inventory (G-018), identity and the legacy domain trust (G-033), OEM cellular routers (G-034), backups (G-041), and network segmentation (G-046).
- **GEPS recovery** (gap 1): recovery plans and restore tests for APS and the integration hub (G-059, G-060).
- **TMU product security** (gap 3): vulnerability disclosure (G-028, G-094), the firmware signing key (G-029, G-095), and SBOMs and the build environment (G-068).
- **Notification** (gap 7): the one **Not met** row, RS.CO-02 (G-057), because the group notification matrix was drafted in 2026-06 and never adopted or exercised; and the 24- and 48-hour addendum incident notice (G-091).

The Recover function has no Met rows. All five rows are partially met, because the plant recovery design, built for P1 to P7, has never been tested against a GEPS scheduling outage and does not yet cover P8.

The FAR clauses are mostly met through group common controls. The three gaps are FCI folders open to all office users for 5 contracts (G-072), two freight forwarder subcontracts without the 52.204-21(c) flow-down (G-087), and the 9 covered video cameras found at P8 during integration (G-088). The cameras were reported to the 14 contracting officers within 1 business day, as 52.204-25(d) requires, and are disconnected pending replacement.

### 4.2 Electric Utility (`gap-analysis-electric-utility.csv`)
| Standard or rule | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CIP-002-5.1a (4) | 4 | 0 | 0 | 0 |
| CIP-003-9 (7) | 4 | 3 | 0 | 0 |
| CIP-004-7 (5) | 3 | 2 | 0 | 0 |
| CIP-005-7 (4) | 4 | 0 | 0 | 0 |
| CIP-006-6, CIP-007-6, CIP-009-6, CIP-010-4 (8) | 8 | 0 | 0 | 0 |
| CIP-008-6 (3) | 2 | 1 | 0 | 0 |
| CIP-011-3 (2) | 1 | 1 | 0 | 0 |
| CIP-012-2 (4) | 1 | 1 | 2 | 0 |
| CIP-013-2 (4) | 2 | 2 | 0 | 0 |
| CIP-014-3, CIP-015-1 (2) | 0 | 0 | 0 | 2 |
| EOP-004-4 (2) | 2 | 0 | 0 | 0 |
| Form DOE-417 (4) | 2 | 2 | 0 | 0 |
| Registry screens: TSA, NRC, SDWA, CIRCIA (4) | 0 | 0 | 0 | 4 |
| **Total (53)** | **33** | **12** | **2** | **6** |

The medium impact program at the TCC is mature. The 2024 audit findings (CIP-007-6 R2 and CIP-010-4 R1) stayed closed. The gaps come from two newer requirements and from the affiliates:
- **CIP-003-9 Attachment 1 Section 6** (effective 2026-04-01): a method to detect known or suspected malicious communications on vendor electronic remote access is in place at only 22 of 58 transmission substations (EU-G10, High; POAM-015).
- **CIP-012-2** (effective 2026-07-01): the plan does not cover availability (Part 1.2) or recovery (Part 1.3) of the data links (EU-G35, EU-G36, Not met; POAM-016).
- **The affiliates as vendors:** TCC BCSI on Grid Engineering's platform, outside the utility's access and handling program (EU-G16, EU-G33, High); affiliate engineers' personnel risk assessments accepted on a weak attestation (EU-G14); no CIP-013-2 terms or vendor risk assessment for either affiliate (EU-G39, EU-G41).
- **DOE-417 at the DCC:** the distribution control center procedure lacks the cyber criteria, so a cyber event that interrupts distribution operations could miss the 1-hour Emergency Alert clock (EU-G46, High).

**Self-reports.** On 2026-09-30 the Electric Utility self-reported to SERC the potential noncompliances found here: CIP-003-9 R2 Attachment 1 Sections 3.1 and 6.3 (EU-G07, EU-G10), CIP-004-7 R6 Part 6.1 and CIP-011-3 R1 Part 1.2 for the TCC BCSI on the affiliate platform (EU-G16, EU-G33), and CIP-012-2 R1 Parts 1.2 and 1.3 (EU-G35, EU-G36). Mitigation plans follow the POA&M dates (P07).

### 4.3 Grid Engineering (`gap-analysis-engineering.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Client NERC CIP flow-down terms (12) | 3 | 8 | 1 | 0 |
| FERC CEII procedures and client CEII terms (1) | 1 | 0 | 0 | 0 |
| FAR 52.204-21, -25, -23 (6) | 5 | 1 | 0 | 0 |
| SOC 2 commitments for the client project platform (3) | 0 | 3 | 0 | 0 |
| Screens: N54-R01 to R03, R05, R06, NERC registration, CIRCIA (6) | 0 | 0 | 0 | 6 |
| **Total (28)** | **9** | **12** | **1** | **6** |

Grid Engineering's gaps are about **knowing what it promised**. It has no register of the CIP terms in its 41 client contracts and no route from group SOC findings to client notices, so the 24- to 72-hour incident notice term is **Not met** (ES-G07, High; POAM-012). The other High gaps are client BCSI open to whole project teams and personal cloud storage on engineering laptops (ES-G05; POAM-013) and uneven hardening of the 700 commissioning laptops used as Transient Cyber Assets at client substations (ES-G12). Its SOC 2 gaps (90-day log retention, undocumented inheritance, drifted 2023 standards) are the same problems seen from the auditor's side (scenario gap 6).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Multi-party notification matrix not adopted or exercised (7) | All | CSF RS.CO-02; addendum sec. 1; client CIP-013-2 R1 Part 1.2.1 terms; CIP-008-6 R4; Form DOE-417; Form 8-K Item 1.05 | High | Adopt the P08 matrix; client terms register; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 2 | P8 segmentation, OEM access, and domain trust (2) | MF, group | CSF PR.IR-01, PR.AA-01, PR.AA-03 | High | OT DMZ at P8; disconnect cellular routers; break the trust | Director of OT engineering; Group identity director | 2027-03-31 |
| 3 | TMU signing key, disclosure, and SBOMs (3) | MF (affects EU and 140 utilities) | Addendum secs. 4 and 5; CSF ID.RA-08, ID.RA-09, PR.PS-06 | High | HSM signing; 20-day disclosure workflow; SBOMs for all 7 lines | Chief product security officer | 2027-03-31 |
| 4 | GEPS scheduling recovery untested (1) | Group, MF, EU | CSF RC.RP-02, RC.RP-03 | High | Recovery runbook and full restore test in provider B | Group ERP platform director | 2027-03-31 |
| 5 | Affiliate vendor terms and TCC BCSI on the affiliate platform (4) | EU, MF, ES | CIP-013-2 R1, R2; CIP-004-7 R6; CIP-011-3 R1 | High | Security schedules in both intercompany agreements; move TCC BCSI; restricted BCSI folders | Group General Counsel; Electric Utility NERC compliance director | 2027-03-31 |
| 6 | Low impact vendor access detection and CIP-012-2 plan (5) | EU | CIP-003-9 Att. 1 Sec. 6.3; CIP-012-2 R1 Parts 1.2, 1.3 | High | Detection at 36 substations; plan update; self-reports filed 2026-09-30 | Group OT security director; Electric Utility system operations director | 2026-12-31 |
| 7 | Grid Engineering inheritance, standards drift, log retention (6) | ES | TSC CC2.3, CC5.3, CC7.2 | Moderate | Inheritance matrix; replace 2023 standards; 1-year log retention | Grid Engineering security and compliance lead | 2026-12-31 |
| 8 | Commissioning laptops as Transient Cyber Assets | ES (affects EU and 41 clients) | CIP-010-4 R4 Att. 1 Sec. 2; CIP-003-9 Att. 1 Sec. 5.2 (client terms) | High | One hardened image; patch exceptions under 35 days; pre-connection record | Grid Engineering chief operating officer | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). 23 of the 27 POA&M items name a row of this analysis in their `source` column; POAM-016 (CIP-012-2) comes from this analysis alone. Moderate gaps without a POA&M item are tracked through the division registers.

## 6. Pending regulatory changes
None of the items below is treated as a current obligation. The `pending_rule_change` column flags affected rows.
- **CIRCIA** (6 U.S.C. 681-681g): proposed rule 89 FR 23644 (2024-04-04). No final rule had been published as of 2026-10-05 (Federal Register API); CISA held town hall meetings on the rulemaking in 2026. If finalized as proposed, Manufacturing would meet the sector criterion for electrical equipment manufacturing, and the group would report covered incidents within 72 hours and ransom payments within 24 hours.
- **NIST SP 800-82 Rev. 4**: initial public draft published 2026-09-21, comments due 2026-11-30. The group stays on Rev. 3 until the final is published.
- **NERC CIP revisions** (as listed on the NERC standards pages): CIP-013-3 and the virtualization revisions (CIP-002-7 and -8, CIP-003-10, CIP-004-8, CIP-005-8, CIP-006-7.1, CIP-007-7.1, CIP-008-7.1, CIP-009-7.1, CIP-010-5, CIP-011-4.1) effective 2028-07-01; CIP-015-1 internal network security monitoring effective 2028-10-01; CIP-003-11 (2029-07-01) rewrites low impact electronic access controls; EOP-004-5 effective 2027-10-01. Utilities may revise their supplier addenda and client terms when CIP-013-3 takes effect.
- **Form DOE-417**: the current OMB approval expires 2027-05-31; check for a revised form.
- **FAR overhaul**: the proposed rule at 91 FR 37550 (2026-06-23) would move the information security clauses into FAR part 40. Proposed only; the clauses in the current contracts still govern.
