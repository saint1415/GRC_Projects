# Regulatory Gap Analysis: Cris Santos Company | Transportation Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad, 16 route miles, north Florida) |
| Tier / Vertical | Micro / Transportation Systems |
| Primary regulation named for this vertical | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (C-TRANSPORTATION-R01): **not applicable**, kept as a readiness reference together with SD 1580-21-01E |
| Binding rules analyzed | TSA: 49 CFR 1570.105, 1570.201, 1570.203 (C-TRANSPORTATION-S01); 49 CFR 1520.9 (S03); part 1580 subparts B and C applicability (S02). PHMSA hazmat security: 49 CFR 172.800, 172.802, 172.704(a)(4)-(5), 174.9 (S06). FRA PTC applicability: 49 CFR 236.1005(b)(1), 236.1006(b)(4) (S04). Text read on eCFR, point in time 2026-09-23 |
| Cyber benchmark analyzed | NIST CSF 2.0, 25 subcategories (C-TRANSPORTATION-BM) |
| Assessment dates | 2026-07-13 to 2026-07-24 (applicability confirmed 2026-07-14) |
| Assessor | Office Manager (Security Lead) with the Owner and General Manager and the MSP lead technician |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Applicability

### 1.1 TSA rail cybersecurity directives: do not apply
SD 1580-21-01E and SD 1580/82-2022-01E apply to freight railroads identified in 49 CFR 1580.101 and to other railroads that TSA designates and notifies. 49 CFR 1580.101 lists three kinds of freight railroad: (a) a Class I railroad; (b) a railroad that transports RSSM in an HTUA; and (c) a railroad that serves as a host railroad to a covered freight or passenger operation.

**Finding.** None of the three criteria is met, and TSA has never designated the company:
- **Class:** Class III. Revenue of about $1.1 million is far below any Class I or Class II threshold.
- **RSSM in an HTUA:** the company carries no RSSM. Its only hazmat that matters for security is propane (Division 2.1), which is not in the RSSM definition in 49 CFR 1580.3 (explosives over 2,268 kg, PIH tank cars, highway route-controlled radioactive material). The line is also outside every Florida HTUA in Appendix A to part 1580 (map check 2026-07-14).
- **Host railroad:** the Class I does not operate on company track. The company is a guest on the Class I's line for 2.5 miles, not a host.
- **Designation:** the General Manager confirmed on 2026-07-14 that no TSA notice has been received, and the correspondence file holds none.

The 7 SD rows in `gap-analysis.csv` (G-052 to G-058) are marked Not applicable. Each carries a readiness note pointing to the benchmark row that would close it if TSA designated the railroad.

### 1.2 TSA rules that do apply
Part 1580 reaches every freight railroad on the general system: 49 CFR 1580.1(a)(1) covers "each freight railroad carrier that operates rolling equipment on track that is part of the general railroad system of transportation," with no size test. Through that section:
- **49 CFR 1570.201** requires a primary and alternate Security Coordinator at the corporate level, reported to TSA within 37 calendar days of any change, with at least one reachable 24/7.
- **49 CFR 1570.203** requires reports to TSA "within 24 hours of initial discovery" of potential threats and significant security concerns, by the methods TSA prescribes (reports go to the Transportation Security Operations Center, TSOC). Appendix A to part 1570 lists "Cyber Attack": "Compromising, or attempting to compromise or disrupt the information/technology infrastructure of an owner/operator subject to this part." **This is the only binding cyber reporting duty the railroad has today**, and the company was not meeting it (G-007, G-008).
- **49 CFR 1520.9** applies because 1520.7(n) makes every surface owner/operator subject to subchapter D a covered person for SSI.
- **Part 1580 subpart C does not apply** today: it covers carriers that transport RSSM (1580.201(1)). It would apply the day a customer ships PIH (for example anhydrous ammonia), which is why G-002 adds a check to the new-customer process.
- **Part 1580 subpart B does not apply**, because it uses the same 1580.101 criteria (G-011).

### 1.3 Hazmat transportation security: applies
The railroad transports propane in tank cars, a large bulk quantity of Division 2.1 material, so 49 CFR 172.800(b)(3) requires a written hazmat transportation security plan with the components in 172.802, and 172.704(a)(4)-(5) requires security awareness and in-depth security training. 174.9 requires a ground-level security inspection of placarded cars. These are security rules, not cyber rules, but they set who is responsible for protecting hazmat shipment information, and the plan is the natural place to say how that information is protected (G-016).

### 1.4 FRA positive train control: no duty
- **Own track:** 49 CFR 236.1005(b)(1) requires PTC from "each Class I railroad and each railroad providing or hosting intercity or commuter passenger service." The company is neither (G-025).
- **Interchange move:** the daily turn uses 2.5 miles of the Class I's PTC-equipped, freight-only main line. 236.1006(b)(4) lets a Class II or III train run there with an unequipped locomotive because the segment has no regularly scheduled passenger traffic, the company runs no more than 4 unequipped trains a day on it (its turn counts as two), and each movement is under 20 miles (G-026). If the company ever added more than one more daily turn, or a longer move, it would need an operative onboard PTC apparatus on the controlling locomotive (236.1006(a)) and would take on tenant duties.

### 1.5 NIST CSF 2.0 as the cyber benchmark
The binding rules set roles and reporting, not cyber controls. With no binding cyber control rule, the company chose CSF 2.0 because it is sector-neutral, it is the structure TSA's vulnerability assessment form uses for covered railroads, and it is the framework the P08 runbook (SP 800-61 Rev. 3) uses. The 25 subcategories (G-027 to G-051) were chosen for a 7-person railroad that depends on SaaS and one dispatch desk. This is not a full CSF profile.

### 1.6 Other rules that touch this work (used in P08, not decomposed here)
- **FRA accident/incident reporting, 49 CFR part 225** (C-TRANSPORTATION-S05): applies to all railroads on the general system (225.3). A cyber event is reportable only if it leads to a reportable accident/incident (immediate telephone reports to the National Response Center under 225.9; monthly reports under 225.11).
- **Hazmat incident notice, 49 CFR 171.15:** only if a reportable hazmat incident occurs.
- **Fla. Stat. 501.171** (S07): employee personal information.

**Not applicable, with reasons:** pipeline, aviation, and maritime rules (C-TRANSPORTATION-R02 to R05). CIRCIA (R07) and the TSA surface cyber NPRM (R06) are proposed only (section 6).

## 2. Method
1. **Requirements.** TSA, PHMSA, and FRA rows follow each regulation's own section and paragraph structure, at the most granular citation that imposes a separate duty. Brief quotes are used; this is public-domain federal text. CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`. SD rows follow the directives' own section numbers and are summarized in our own words.
2. **Crosswalk.** TSA, PHMSA, FRA, and SD rows use an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such; no official NIST mapping exists for these rules. CSF rows use a subset of the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`).
3. **Documentary evidence.** Each status rests on a named document or record: the company's 2021 applicability determination letter to TSA (1570.105(b)), the Security Coordinator designation memo and TSA confirmation, the TSA report log, the after-hours test call (2026-07-17), the hazmat security plan and training records, hazmat inspection checklists, the interchange agreement, the SYS-01 user and role lists, the shared-drive permission report (2026-07-20), the MSP device list, patch report, antivirus export, and backup job report, and a walkthrough of the office, enginehouse, and customer siding (2026-07-16). Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since then (for example, the Security Lead designation on 2026-08-31) are noted in the remediation column but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| **A. TSA regulations (binding)** | | | | |
| 49 CFR 1570.105, 1570.201, 1570.203 | 3 | 5 | 1 | 0 |
| 49 CFR part 1580 subparts B and C (applicability) | 0 | 0 | 0 | 2 |
| 49 CFR 1520.9 (SSI) | 0 | 1 | 2 | 0 |
| **Subtotal TSA (14)** | **3** | **6** | **3** | **2** |
| **B. Hazmat security, 49 CFR 172.800, 172.802, 172.704, 174.9 (binding) (10)** | **7** | **2** | **1** | **0** |
| **C. FRA PTC applicability, 49 CFR 236.1005, 236.1006 (2)** | **1** | **0** | **0** | **1** |
| **D. NIST CSF 2.0 (benchmark)** | | | | |
| Govern | 0 | 1 | 4 | 0 |
| Identify | 0 | 1 | 3 | 0 |
| Protect | 0 | 8 | 1 | 0 |
| Detect | 0 | 1 | 2 | 0 |
| Respond | 0 | 0 | 2 | 0 |
| Recover | 0 | 0 | 2 | 0 |
| **Subtotal CSF (25)** | **0** | **11** | **14** | **0** |
| **E. TSA SD 1580-21-01E and 1580/82-2022-01E (readiness only) (7)** | 0 | 0 | 0 | 7 |
| **Total (58)** | **11** | **19** | **18** | **10** |

Of the 37 unmet or partially met rows, 6 are rated High, 24 Moderate, and 7 Low.

**The pattern.** The hazmat security side is in good shape: the plan exists, training is current, and crews inspect propane cars at acceptance, because the General Manager has run these for years. The failures sit where security meets IT:
- **The one binding cyber duty is missed.** 1570.203 makes a cyber attack reportable to TSA within 24 hours, and the 2025 mailbox compromise was not reported (G-007, G-008).
- **SSI is treated like any other file.** Two TSA-marked documents sit where every account can open them, and nobody would tell TSA if they were stolen (G-012, G-014).
- **The benchmark shows an office built for convenience:** a shared crew login, no plan for losing the dispatch desk, backups never tested, no monitoring, and a dispatch computer past end of support.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Cyber attacks not reported to TSA; no 24-hour procedure | 1570.203(a)(1), (b); Appendix A | High | TSA report step in POL-03 and P08 (company target 12 hours); brief all staff | Owner and General Manager | 2026-10-15 |
| No incident response plan | CSF RS.MA-01 | High | POL-03 and P08 runbook (approved 2026-08-31); tabletop | Office Manager | 2026-11-30 |
| No written paper dispatch or recovery procedure | CSF RC.RP-01 | High | Contingency plan with paper dispatch and the BIA recovery order | Owner and General Manager | 2026-11-30 |
| Backups unprotected and untested; no copy of operations data | CSF PR.DS-11 | High | Immutable versions; restore tests; weekly SYS-01 export | Office Manager (MSP performs) | 2026-10-31 |
| No behavior-based detection or after-hours alerting | CSF DE.CM-09 | High | MSP-managed EDR with alert monitoring | Office Manager | 2026-12-31 |
| SSI open to every account | 1520.9(a)(1)-(3) | Moderate | Restricted folder for the Security Coordinators | Owner and General Manager | 2026-10-31 |
| No procedure to report an SSI release | 1520.9(c) | Moderate | SSI notice in the P08 matrix | Owner and General Manager | 2026-10-15 |
| Security Coordinator not reliably reachable 24/7 | 1570.201(f)(2) | Moderate | Number rings both coordinators; on-call rotation | Owner and General Manager | 2026-09-30 |
| Hazmat security plan review overdue; plan open to all | 172.802(c) | Moderate | Annual review; restricted folder | Owner and General Manager | 2026-10-31 |
| Shared crew login; MFA gaps | CSF PR.AA-01, PR.AA-03 | Moderate | Named crew accounts with MFA; MFA on MSP-held logins | Office Manager | 2026-11-30 |
| Unsupported dispatch desktop on a flat network | CSF PR.PS-02, PR.IR-01 | Moderate | Replace the desktop; separate segment | Office Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person railroad: most actions are one-page procedures, phone settings, or MSP work, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Duties and contacts | 2026-10-15 | TSA report step and cyber triggers in POL-03 and P08; report form cyber fields; contact card with MSP, FBI, and CISA; registered number rings both coordinators; SSI release notice | G-005, G-006, G-007, G-008, G-009, G-014, G-048 |
| 2. Access and records | 2026-10-31 | Security Lead designation and policies published (done 2026-08-31); obligations list; restricted SSI and security plan folder; SSI handling rules; hazmat security plan review; new-customer TSA check; inventory; desktop encryption; access review; log review starts; first restore test and backup upgrade | G-002, G-012, G-013, G-016, G-020, G-021, G-027, G-028, G-029, G-032, G-033, G-037, G-039, G-040, G-046, G-050 |
| 3. Resilience and identity | 2026-11-30 | Contingency plan with paper dispatch; tabletop and paper dispatch drill; named crew accounts with MFA; MFA on MSP-held logins; dispatch segment; failover router | G-035, G-036, G-042, G-043, G-047, G-049, G-051 |
| 4. Detection and suppliers | 2026-12-31 | EDR; vulnerability scanning; awareness training and phishing simulations; replacement dispatch desktop; MSP contract amendment; supplier reviews | G-030, G-031, G-034, G-038, G-041, G-044, G-045 |
| 5. Annual cycle | 2027-03 to 2027-08 | Hazmat security plan review (March); risk assessment update (July); independent assessment (August) | Keeps G-021 and the benchmark rows current |

**Progress check.** The Office Manager reports progress to the Owner and General Manager at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488, 2024-11-07; C-TRANSPORTATION-R06). **Still proposed:** no final rule in the Federal Register as of 2026-10-05. As proposed, it would reach this railroad in two ways:
  - Proposed 1580.311 would require **every** railroad in 1580.1(a)(1) to designate a Cybersecurity Coordinator.
  - Proposed 1580.325 would require **every** such railroad to report reportable cybersecurity incidents to CISA within 24 hours.
  - The full cyber risk management program in the proposal is aimed at higher-risk railroads. Its proposed criteria for short lines turn on factors such as RSSM in an HTUA and hosting covered railroads, which this railroad does not meet. Recheck against the final text.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR part 226, 89 FR 23644; C-TRANSPORTATION-R07). The final rule has not been published; CISA held further town halls in 2026. The proposed rule combined a size criterion (the railroad is SBA-small, so it would not be covered that way) with sector criteria that include certain freight railroads. If finalized as proposed, it would add 72-hour incident reports and 24-hour ransom payment reports to CISA.
- **TSA directives** are renewed periodically. Recheck applicability at each renewal and whenever the business changes (1570.105(b)).

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these proposals is treated as a current obligation.
