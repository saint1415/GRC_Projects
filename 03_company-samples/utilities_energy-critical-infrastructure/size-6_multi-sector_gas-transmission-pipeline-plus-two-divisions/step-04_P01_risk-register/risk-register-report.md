# Risk Register Report: Cris Santos Company Holdings | Energy | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Energy, Mining and Oil and Gas Extraction, Professional Services) |
| Focus division | Gas Transmission (NAICS 486210), a TSA-designated interstate natural gas pipeline |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also supports | The Critical Cyber System identification and risk-based patch methodology in the TSA implementation plan (SD Pipeline-2021-02G Sections III.A and III.E.2.a) |
| Registers | `risk-register.csv` (group), `risk-register-gas-transmission.csv`, `risk-register-gathering-production.csv`, `risk-register-integrity-services.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-22 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that monitors or controls pipeline and field operations, every business service the pipeline depends on, and every system that holds SSI, CEII, client data, or personal information, in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity and the OT remote access gateway, SYS-G2 SOC, SYS-G3 network, data centers, and cloud, and SYS-G6 data platform (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Gas Transmission, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Pipeline safety and environmental risks rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, CISA and TSA advisories on pipeline threats, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's operations and compliance leaders.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). For OT risks, impact includes physical consequences: loss of supply to homes and power plants, a release, or injury. Hardwired station shutdowns cap some worst cases, which is reflected in impact ratings.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 7 | 3 | 0 | 16 | n/a |
| Gas Transmission | 0 | 5 | 17 | 6 | 0 | 28 | 13 |
| Gathering and Production | 0 | 1 | 11 | 6 | 0 | 18 | 11 |
| Integrity Services | 0 | 3 | 7 | 8 | 0 | 18 | 7 |
| **All registers** | **0** | **15** | **42** | **23** | **0** | **80** | **31** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware on corporate IT disables gas measurement and nominations, forcing a precautionary transmission shutdown | ES-004; GP-003; TX-001; TX-002 | Move SYS-T4 into a dedicated enclave with its own identity store | Group CISO with the Gas Transmission president | 2027-06-30 |
| GR-02 | An IT compromise reaches the OT DMZs of two divisions through the shared OT remote access gateway | ES-002; GP-002; TX-003 | Split the gateway by division | Group OT Security Director | 2026-12-31 |
| GR-03 | TSA finds the Gas Transmission division out of compliance with its approved implementation plan and assessment plan | TX-004; TX-005 | Notify TSA and request a plan amendment | Director of Pipeline Cybersecurity | 2026-12-31 |
| GR-04 | Client and group SSI held by Integrity Services is disclosed | ES-001; ES-003; TX-012 | SSI program: labeling, need-to-know groups, separate SSI store, enforced deletion of engagement evidence | Integrity Services Client Security Officer | 2026-12-31 |
| GR-06 | AI used in safety-relevant pipeline and integrity decisions without governance | ES-006; GP-009; TX-009 | Group AI program (P10): validation, change control linked to the control room, council approval before any automation | Group Chief Risk Officer | 2027-03-31 |
| GR-15 | A nation-state actor pre-positions in OT networks across divisions using legitimate tools | TX-018; TX-025 | Close sensor gaps | Group SOC director | 2027-03-31 |

### Gas Transmission (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| TX-001 | Ransomware spreads from the corporate directory to the gas measurement servers and encrypts them | Block directory administrator logons by 2026-10-31; dedicated measurement enclave by 2027-06-30 (POAM-007) | Vice President of Commercial Operations | 2027-06-30 |
| TX-002 | Prolonged loss of measurement and nominations leads to a precautionary curtailment or segment shutdown | Write and exercise a 72-hour manual scheduling and measurement procedure (POAM-006) | Vice President of Commercial Operations | 2027-03-31 |
| TX-003 | Attacker uses the shared OT remote access gateway to reach the central or regional OT DMZ | Dedicated Transmission gateway tier; account clean-up (POAM-001, POAM-002) | Group OT Security Director | 2026-12-31 |
| TX-005 | TSA inspection finds the approved plan not implemented on schedule and the architecture design review lapsed | Architecture design review starts 2026-10-05; assessment schedule resourced (POAM-009) | Director of Pipeline Cybersecurity | 2026-12-15 |
| TX-025 | A nation-state actor pre-positions in the Transmission OT DMZs using legitimate tools | Baseline-deviation alerts; twice-yearly hunts (POAM-003) | Group SOC director | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| GP-001 | Gathering and Production | The Arkoma legacy SCADA is compromised through the always-on vendor connection | Vice President of Field Operations Technology | 2026-12-31 |
| ES-001 | Integrity Services | SSI from designated clients and Gas Transmission is disclosed from the IDP or engineering shares | Integrity Services Client Security Officer | 2026-12-31 |
| ES-003 | Integrity Services | An OT assessment toolkit holding client network captures is lost or stolen | OT Assessment Practice Leader | 2026-11-30 |
| ES-006 | Integrity Services | The ILI anomaly classification model misclassifies a severe anomaly and a client delays a repair | Vice President of Integrity Engineering | 2027-03-31 |

### What the results say
The program is mature where the TSA directives have pushed it: zone-based segmentation, MFA and PAM, an OT desk in the SOC, offline SCADA backups, and an exercised incident response plan. There are no Very High risks. The High risks cluster around **the seams between what the group shares and what the pipeline needs**:
1. **Business services on corporate IT** (GR-01, TX-001, TX-002). The pipeline can run safely without business IT, but it cannot run commercially for long without measurement and nominations, and those depend on the corporate directory (scenario gap 1). This is the path by which a business IT ransomware incident becomes a pipeline shutdown.
2. **Shared access paths into OT** (GR-02, TX-003) and **nation-state pre-positioning** (GR-15, TX-025). One gateway serves three divisions (gap 3), and sensor gaps limit what the SOC can prove about OT during an incident.
3. **Compliance with the TSA-approved plans** (GR-03, TX-005). The measures are largely in place; the schedule and the assessment cycle slipped without the amendment request the directive requires (gap 5).
4. **Data the group holds for others** (GR-04, ES-001, ES-003). Integrity Services holds SSI for Gas Transmission and 9 designated clients without SSI controls (gap 2).
5. **AI in safety-relevant work** (GR-06, ES-006) has run ahead of the Group AI Standard (gap 9).

Gathering and Production's one High risk is the acquired Arkoma SCADA (GP-001, gap 4). Its governance gaps (inheritance and supplement drift, gaps 7 and 10) are Moderate and Low at group level (GR-10, GR-11), but they hide whether its controls actually operate, which is why P07 sampled Gathering on CA-2 and PL-1.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** measurement enclave and 72-hour manual fallback (GR-01); division-split OT remote access gateway (GR-02); Integrity Services SSI program (GR-04); group AI program (GR-06); Arkoma migration (GR-07); OT sensor coverage and threat hunting (GR-15).
- **TSA actions:** notify TSA and request an implementation plan amendment for the station panel schedule; complete the architecture design review (GR-03).
- **Accepted (4, all Low):** TX-015, TX-016, GP-016, GP-018. **Avoided (2):** GP-009, ES-017.
- **Treatment status:** 41 risks are In progress, 34 are Open (treatment approved, work not started), and 5 are Closed (accepted or avoided by policy).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The 6 High group risks were presented on 2026-09-22. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here: the board risk committee's oversight, the Group CISO's reporting line, and the TSA directives as a source of regulatory risk. Risk details that would reveal security vulnerabilities of the Gas Transmission system are SSI and are presented to the board in a restricted annex, not in the public disclosure.

## 6. Approval
- Board risk committee: approved the group register, the 6 High group treatment plans, and the funding request, 2026-09-22.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the 9 High division risks, 2026-09-22.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-15 to 2026-09-22.
- Next full review: May to July 2027, or sooner after a major change, acquisition, TSA directive revision, or incident.
