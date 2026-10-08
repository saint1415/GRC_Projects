# Risk Register Report: Cris Santos Company Holdings | Healthcare and Public Health | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Healthcare and Public Health, Finance and Insurance, Educational Services) |
| Focus division | Hospital System (NAICS 622110), 9 acute-care hospitals, a HIPAA covered entity |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), for each covered entity (Hospital System and Health Plan); an input to the College's new written risk assessment under the GLBA Safeguards Rule, 16 CFR 314.4(b)(1) (POAM-019); an input to the all-hazards risk assessment input to the hospitals' emergency plan, 42 CFR 482.15(a)(1) |
| Registers | `risk-register.csv` (group), `risk-register-hospital-system.csv`, `risk-register-health-plan.csv`, `risk-register-college.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that creates, receives, maintains, or transmits ePHI, member information, or student customer information in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 data centers, network, file service, cloud, and backup vault, and SYS-G4 ERP and HR. Division systems are SYS-H1 to SYS-H3, SYS-P1, and SYS-E1 and SYS-E2 ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. The Hospital System, the focus division, has the most detailed register (30 risks).
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (group risk management strategy, EV-025):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Patient-safety risks rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the intake evidence, the HHS 405(d) HICP threat list for large organizations, interviews with each division's leadership, clinical engineering, and the system emergency management director (EV-092 group, EV-093 Hospital System, EV-094 Health Plan, EV-095 College), the gap analyses (P03), and the first results of the common control assessment (P07), which began on 2026-07-06 inside the fieldwork window. The gap analyses ran in the same window, as is usual for a HIPAA risk analysis, and the two shared findings.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column of all four registers: configuration exports, inventories, contracts, plans, and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Patient-safety consequences (delayed treatment, medication errors, missed results) rate Very High; group impact reflects several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence, including the P07 results available by then. P07 testing continued to 2026-08-28; it confirmed existing risks and added none, so every risk in the four registers is Pass 1 (`assessment_pass`). The plain-text interface passwords found in P07 testing on 2026-07-09 (EV-C1-IA-5) were folded into HS-019 in Pass 1. Later test findings were tracked in the POA&M and linked to the risks they affect (`related_risk_ids`).

## 3. Results
| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 12 | 2 | 0 | 18 | n/a |
| Hospital System | 0 | 5 | 15 | 10 | 0 | 30 | 21 |
| Health Plan | 0 | 0 | 9 | 7 | 0 | 16 | 10 |
| College | 0 | 1 | 9 | 6 | 0 | 16 | 10 |
| **All registers** | **0** | **10** | **45** | **25** | **0** | **80** | **41** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware spreads through the shared directory and data centers, forcing EHR downtime at all 9 hospitals and stopping the claims core | HS-001, HS-002, HS-011, HS-029, HP-001, HP-003, ED-004 | Clean recovery environment and EHR restore test; separate directory tier and data center zones; cross-division exercise | Group CISO | 2027-06-30 |
| GR-02 | Medical device and clinical OT compromise across hospitals | HS-004, HS-005, HS-006, HS-025, HS-030 | Segmentation at 4 hospitals; vendor access through PAM; device network monitoring | Hospital System security and compliance lead | 2027-06-30 |
| GR-04 | AI in clinical, coverage, or academic decisions without adequate governance | HS-009, HS-010, HP-005, ED-010 | Group AI program (P10): sepsis model validation at every hospital, UM committee approval, proctoring review | Group Chief Risk Officer | 2027-03-31 |
| GR-07 | Third-party remote access used to enter group networks | HS-005, HS-012, HP-010 | All vendor access through PAM with per-session approval | Group CISO | 2027-03-31 |

### Hospital System (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| HS-001 | Ransomware encrypts EHR and ancillary servers in both data centers | Clean recovery environment and restore test (POAM-012); zone separation (POAM-007) | Hospital System security and compliance lead | 2027-03-31 |
| HS-002 | EHR downtime beyond the MTD causes medication errors, missed results, or delayed treatment | Multi-day downtime drills; procedures for outages over 24 hours (POAM-009) | System CNO | 2027-03-31 |
| HS-005 | Device vendor remote support connection used to reach device networks | 37 connections into PAM (POAM-013) | Clinical engineering director | 2026-12-31 |
| HS-009 | Sepsis model under-detects sepsis in some patient groups or hospitals | Validation at all 9 hospitals; universal screening; 92.210 documentation (POAM-024) | System CMIO | 2026-12-31 |
| HS-011 | System-wide IT outage overwhelms incident command; diversion and transfers uncoordinated | Cyber and IT outage annex with diversion criteria in the unified emergency plan (POAM-023) | System emergency management director | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ED-001 | College | Staff accounts on the student information and financial aid system taken over without MFA (16 CFR 314.4(c)(5)) | College IT director | 2026-11-30 |

The Health Plan has no High risks. Its program inherits documented common controls (2025 inheritance matrix), and its largest exposure, the claims core in DC1, is rated through group risk GR-01.

### What the results say
There are no Very High risks, and most control families are in place: a 24x7 SOC, PAM, quarterly access certification, immutable backups, and a tested failover to DC2. The High risks cluster in three places:
1. **What the divisions share** (GR-01, GR-07). One directory forest and unseparated server zones in two data centers mean one ransomware compromise can stop all 9 hospitals, the claims core, and the College's administrative files at once, and the restore path from the vault has never been proven (group gap 1).
2. **Patient safety during and around IT failures** (HS-002, HS-011, GR-02). The hospitals' paper downtime is built for hours, the unified emergency plan has no system-wide IT outage scenario (group gap 2), and the device estate has unsupported and unsegmented parts (group gap 3).
3. **Governance that has not caught up** (GR-04, ED-001). The sepsis model went live at 9 hospitals with validation at one (group gap 6), and the College is still outside group identity controls (group gap 5).

Group gaps 4, 7, and 8 (student access, minimum necessary between covered entities, multi-regulator notification) are Moderate at group level (GR-05, GR-09, GR-03). They matter because each involves two or more divisions and none can be fixed by one division alone.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** clean recovery environment and directory tier separation (GR-01); device network segmentation and vendor PAM (GR-02, GR-07); group AI program (GR-04); College migration to SYS-G1 (GR-06); SIEM coverage of device networks and the College (GR-12).
- **Accepted (all Low):** HS-024 (encrypted workstation theft), HS-026 (telehealth vendor breach), HP-012 (hurricane at the claims center, covered by remote work), ED-016 (simulation lab misuse, synthetic data only).
- **Contract and agreement actions:** affiliation agreements with 22 outside schools (POAM-014); minimum-necessary protocols in the intercompany data sharing addendum (GR-09); proctoring vendor terms (ED-010).
- **Treatment status:** 72 risks are In progress, 4 are Open (treatment approved, work not started: GR-16, HS-013, ED-009, ED-014), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line). The College's Qualified Individual will present the College part of this register in the first written annual report under 16 CFR 314.4(i) (POAM-025).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the six High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
