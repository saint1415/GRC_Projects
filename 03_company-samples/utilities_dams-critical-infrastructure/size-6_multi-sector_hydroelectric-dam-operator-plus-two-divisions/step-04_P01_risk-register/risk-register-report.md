# Risk Register Report: Cris Santos Company Holdings | Dams | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Utilities, Construction, and Professional Services) |
| Focus division | Cris Santos Hydro (NAICS 221111): FERC licensee and NERC-registered Generator Owner and Generator Operator |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | FERC Security Program Rev. 3A risk and threat assessment items (Form 3 Q23 and Q29 to Q32); the annual risk input to the CIP-013-2 plan; the risk assessment behind the FPE's NIST SP 800-171 Rev. 2 requirement 3.11.1 |
| Registers | `risk-register.csv` (group), `risk-register-hydro.csv`, `risk-register-constructors.csv`, `risk-register-engineering.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Chief Dam Safety Engineer |
| Approved | 2026-09-10 by the board safety, risk, and reliability committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system in `../00_company-facts.md` section 3: the corporate shared services (SYS-G1 to SYS-G6), Hydro's OT and supporting systems (SYS-H1 to SYS-H7), Constructors' systems (SYS-C1 to SYS-C5), Engineering's systems (SYS-E1 to SYS-E3), and third parties with access (SYS-T).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Hydro, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to it. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating. For example, GR-03 (the DSMS path into Hydro OT) is High at group level because one cloud compromise reaches both Engineering's clients and Hydro's plants, while Hydro's own view of the same path (HY-003) is Moderate because gates and units can run in local control.

**Risk tolerance and who can accept risk** (also in `../00_company-facts.md` section 7 and POL-01 4.4):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board safety, risk, and reliability committee; temporary only, with a dated plan |
| Very High | Board safety, risk, and reliability committee only |

High risks to public safety (uncontrolled release, missed dam safety anomalies) and potential NERC noncompliance may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the 2026-07-08 Section 9 determinations, and interviews with each division's leadership, the HOC Managers, and the Chief Dam Safety Engineer.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). A plausible uncontrolled release or loss of HOC control is Very High. Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 11 | 3 | 0 | 20 | n/a |
| Hydro | 0 | 6 | 16 | 8 | 0 | 30 | 12 |
| Constructors | 0 | 3 | 9 | 4 | 0 | 16 | 9 |
| Engineering | 0 | 2 | 7 | 7 | 0 | 16 | 10 |
| **All registers** | **0** | **17** | **43** | **22** | **0** | **82** | **31** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Unauthorized control of spillway gates or units through construction or vendor connections that bypass Hydro OT access controls | HY-001, HY-009, HY-018, CN-003 | Group commissioning standard at Hydro sites; EDR on all kits; affiliates treated as vendors in every OT control | Group CISO | 2026-12-31 |
| GR-02 | Ransomware spreads through shared IT across divisions | CN-005, EN-015, HY-025 | EDR on kits and jobsite devices; jobsite segmentation; quarterly DSMS and FPE restore tests | Group CISO | 2027-03-31 |
| GR-03 | DSMS compromise used to reach Hydro OT DMZs through two-way replication | HY-003, EN-006 | One-way transfer at 17 plants; intercompany interconnection agreement | Director, OT Security | 2027-03-31 |
| GR-05 | Dam safety anomalies missed because AI-001 replaced manual review and changes without control | HY-010, HY-026, EN-002, EN-003 | Weekly manual readings restored; change control for thresholds and models; quarterly back-tests | Chief Dam Safety Engineer | 2026-12-31 |
| GR-06 | CUI mishandled and CMMC status not achieved for USACE work | CN-001, CN-002, EN-008 | Purge CUI from SYS-C1 and shares; reach at least 88 with only POA&M-eligible items open; C3PAO assessment 2027-03-15 | Federal Programs Compliance Director | 2027-03-31 |
| GR-08 | Governor and excitation OEM compromise or failure affects 55% of Hydro units | HY-013 | CIP-013 contract terms; second qualified vendor; offline governor configurations | Chief Procurement Officer | 2027-06-30 |

### Hydro (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| HY-001 | Unauthorized gate commands through a Constructors commissioning kit at a rehabilitation site | Permanent commissioning design (GR-01); gate position alarms to the HOC during rehabilitation | Director, OT Security | 2026-12-31 |
| HY-004 | Exploitation of unsupported plant HMIs and gate control workstations | Replace gate workstations by 2027-03, HMIs by 2027-12; allow-listing | Director, OT Security | 2027-12-31 |
| HY-006 | Undetected intrusion at the 27 plants without OT monitoring | Sensors at all 41 plants, Group 1 and 2 dams first | Director, OT Security | 2027-06-30 |
| HY-013 | Malicious update from the governor and excitation OEM | Group plan GR-08 | Chief Procurement Officer | 2027-06-30 |
| HY-018 | Gate PLC logic changed by a construction project outside Hydro change control | Hydro change board approves every logic change at Hydro sites; Hydro witness at commissioning | Senior Vice President, Hydro Operations | 2026-11-30 |
| HY-026 | Missed anomaly at one of the 31 dams moved to monthly manual readings | Return to weekly manual readings (GR-05) | Chief Dam Safety Engineer | 2026-10-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| CN-001 | Constructors | CUI stored and shared outside the FPE | Federal Programs Compliance Director | 2026-12-31 |
| CN-002 | Constructors | No Conditional Level 2 (C3PAO) status when USACE requires it | Federal Programs Compliance Director | 2027-03-31 |
| CN-003 | Constructors | A compromised commissioning kit pivots into an owner's control system | Constructors security and compliance lead | 2026-11-30 |
| EN-002 | Engineering | AI-001 misses an anomaly at a client dam | Director of Data Science | 2026-12-31 |
| EN-006 | Engineering | An attacker in the DSMS uses the Hydro replication path toward OT | DSMS General Manager | 2027-03-31 |

### What the results say
The program is defined and largely works: no risk is Very High, the HOC Electronic Security Perimeters, Intermediate Systems, OT identity domain, and SOC are sound, and most Moderate risks are about coverage, not design. The High risks cluster around **where the divisions meet**:
1. **Constructors inside Hydro plants** (GR-01). Because Constructors is an affiliate, its commissioning kits were treated as internal and bypassed the vendor controls that every outside OEM must use (scenario gap 1). This is the group's top risk and the path used in the P08 scenario.
2. **Engineering's cloud service connected back to Hydro** (GR-03) and **Engineering's AI model on Hydro's dam safety critical path** (GR-05). Hydro relies on an intercompany service that has no interconnection agreement, no SOC 2 report yet, and no change control for alert thresholds (gaps 3, 6, and 10).
3. **CUI handling for federal work** (GR-06). The enclave is sound, but the self-assessment score of 74 is below the 88 needed for a Conditional Level 2 status, and Phase 2 of CMMC begins 2026-11-10 (gap 5).

Hydro's own High risks (HY-004, HY-006) are the scale problems expected at this size: legacy OT and monitoring that has not yet reached every plant below the HOCs (gaps 2 and 4).

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q4, $46 million approved 2026-09-10):** commissioning standard and kit EDR (GR-01); one-way DSMS transfer (GR-03); OT sensors at all HOC-operated plants (HY-006); HMI and gate workstation replacement (HY-004); CMMC remediation (GR-06); AI governance conditions (GR-05).
- **Accepted (all Low):** GR-16 (payroll provider outage), HY-027 (reservation vendor breach), HY-030 (GPS time spoofing), CN-007 (telematics account takeover), EN-014 (cloud provider A identity incident).
- **Regulatory actions:** self-report to SERC for the CIP-003-9 Attachment 1 Sections 5 and 6 gap at BES plants (HY-009, filed 2026-09-30); plan and schedule letters to the FERC Regional Engineers for negative Form 3 answers (HY-017).
- **Treatment status:** 46 risks are In progress, 31 are Open (treatment approved, work not started), and 5 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board safety, risk, and reliability committee each quarter. The six High group risks were presented on 2026-09-10. The Reg S-K Item 106 disclosure in the next annual report on Form 10-K draws on this governance: the committee's oversight, the Group CISO's reporting line, and the use of internal audit and outside assessors.

## 6. Approval
- Board safety, risk, and reliability committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eleven High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
