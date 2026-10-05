# Enterprise Risk Register Report: Cris Santos Company | Energy | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company: PS-1, PS-2, PS-3, and operated JV-1 to JV-3; 9 states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Energy (natural gas pipeline) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Risk input to the TSA Cybersecurity Implementation Plan and Cybersecurity Assessment Plan (SD Pipeline-2021-02G Sections II.B and III.G); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |
| Handling | Risk entries for Critical Cyber Systems are SSI when shared with TSA (49 CFR 1520.5(b)(5)); this sample contains no SSI |

## 1. Scope and risk framing
**Scope.** All IT and OT systems across the three owned pipeline systems, the three operated JV pipelines, the three control rooms, 96 compressor stations, the two clouds and two colocation data centers, and about 1,100 suppliers (about 140 with OT access or data). Business processes and impact values come from the enterprise BIA (P05). The PSGCS is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, IT, and OT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit, co-sourced with an independent OT assessment firm (third line), tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Public and worker safety:** very low appetite for cyber events that could affect safe pipeline operation.
- **Security directive and safety compliance:** very low appetite for noncompliance with TSA security directives, PHMSA rules, or SEC disclosure rules.
- **Reliable deliveries:** low appetite for curtailment of firm service caused by cyber or technology events.
- **Sensitive information:** low appetite for disclosure of SSI, CEII, shipper data, or employee data.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Loss of safe pipeline operations from cyber events | Low |
| ER-02 Disruption of gas deliveries and commercial services | Moderate |
| ER-03 Third-party and supply chain risk | Moderate |
| ER-04 Integration of the PS-3 acquisition | Moderate |
| ER-05 Security directive and pipeline safety compliance (TSA, PHMSA, FERC) | Low |
| ER-06 Disclosure, financial reporting, and fraud | Low |
| ER-07 Compromise of sensitive information (SSI, CEII, shipper data, employee data) | Moderate |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

ER-01 safety risks at Moderate or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the pipeline threat picture in CISA and TSA advisories (ransomware on business IT, nation-state pre-positioning in OT, edge device exploitation, supply chain); the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Safety consequences set impact to Very High where loss of control or false data could contribute to an overpressure or a missed rupture.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 33 |
| Low | 20 |
| **Total** | **65** |

By threat source type: Adversarial 26, Structural 22, Accidental 14, Environmental 3.
By treatment: Mitigate 56, Accept 7, Avoid 2.
By status: In progress 51, Open 5, Closed (accepted) 7, Closed (avoided) 2.
**24 risks are outside tolerance**, and each has a dated treatment plan. All 24 are board-reported.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Loss of safe pipeline operations from cyber events | Operational and safety | 16 | 0 | 6 | 6 | 4 | **High** | Low | 12 |
| ER-02 | Disruption of gas deliveries and commercial services | Operational | 11 | 1 | 1 | 4 | 5 | **Very High** | Moderate | 2 |
| ER-03 | Third-party and supply chain risk | Operational | 4 | 0 | 2 | 2 | 0 | **High** | Moderate | 2 |
| ER-04 | Integration of the PS-3 acquisition | Strategic | 7 | 0 | 1 | 6 | 0 | **High** | Moderate | 1 |
| ER-05 | Security directive and pipeline safety compliance | Compliance | 7 | 0 | 0 | 5 | 2 | **Moderate** | Low | 5 |
| ER-06 | Disclosure, financial reporting, and fraud | Compliance and financial | 7 | 0 | 1 | 1 | 5 | **High** | Low | 2 |
| ER-07 | Compromise of sensitive information | Compliance and reputational | 7 | 0 | 0 | 5 | 2 | **Moderate** | Moderate | 0 |
| ER-08 | Responsible use of AI | Strategic and operational | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-02 (deliveries)** carries the only Very High risk: ransomware on business IT that forces a precautionary shutdown (R-001). The business IT itself is not needed to move gas safely (P05), so the treatment focuses on fast, trusted isolation and a clear operate-or-shut-down decision.
- **ER-01 (safety)** has the lowest tolerance and six High risks, mostly OT conditions: the shared SCADA platform (R-002), pre-positioning in OT (R-003), legacy station controls (R-004), unpatched OT (R-006), false data (R-011), and untested isolation (R-012). 12 of its 16 risks are outside tolerance.
- **ER-04 (PS-3)** is within its Moderate tolerance except for R-005, the PS-3 network and SCADA conditions, which drive several other ratings.
- **ER-05 (compliance)** has no High risk but 5 risks outside its Low tolerance, mostly record and schedule items TSA or PHMSA could cite (R-015, R-035, R-036, R-054, R-056).
- **ER-06 (disclosure)** is outside tolerance mainly because the materiality process has not been exercised for an operational shutdown (R-013).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware on business IT forces a precautionary shutdown of a pipeline system | Very High | ER-02 | Isolation exercises at GCC-2 and PS3-CR (POAM-012); curtailment factors and disclosure tabletop (POAM-013); annual enterprise ransomware exercise with gas control | CISO | 2027-03-31 |
| R-002 | Fault or compromise of the common SCADA platform affects both control centers | High | ER-01 | Platform-wide scenario in the contingency plan; offline golden images; drill (POAM-011) | Vice President, Gas Control | 2027-03-31 |
| R-003 | Nation-state pre-positioning in OT | High | ER-01 | OT monitoring at the remaining 22 stations (POAM-005); quarterly hunts | Director of Security Operations | 2027-03-31 |
| R-004 | Unauthorized commands through a compromised legacy station HMI | High | ER-01 | Mitigations at the last 7 stations; replacement program (POAM-003) | Director of Compression Engineering | 2027-06-30 |
| R-005 | Attacker enters PS-3 OT through flat networks or the legacy SCADA | High | ER-04 | Segmentation, encryption, migration (POAM-016) | Vice President, Integration Management Office | 2027-06-30 |
| R-006 | Exploitation of a Known Exploited Vulnerabilities entry on unpatched OT | High | ER-01 | Clear overdue items (POAM-002); credentialed scanning (POAM-020) | Director of SCADA Engineering | 2027-01-31 |
| R-008 | Always-on vendor modem used as entry to a station network | High | ER-03 | Remove the 7 modems (POAM-004) | Director of OT Security | 2026-12-15 |
| R-011 | False field data misleads controllers | High | ER-01 | Authenticated protocols in new RTUs; anomaly rules | Director of SCADA Engineering | 2027-12-31 |
| R-012 | IT/OT isolation slow or fails at GCC-2 or PS3-CR | High | ER-01 | Isolation exercises; PS-3 manual operation drill (POAM-012) | Director of OT Security | 2027-03-31 |
| R-013 | Late or inaccurate SEC disclosure of an operational shutdown | High | ER-06 | Playbook update; tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| R-030 | Malicious code in a trusted SCADA or station software update | High | ER-03 | Signed updates and vendor attestation; soak testing (POAM-014) | Director of SCADA Engineering | 2027-06-30 |
| R-048 | Zero-day in an internet-facing edge device | High | ER-02 | Retire VPN concentrators; 72-hour emergency patch service level | Director of Network Engineering | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Business IT is the likely entry point; OT trust is the decision point (ER-02, ER-01).** A ransomware event on business IT (R-001) does not by itself make the pipelines unsafe, but the company must be able to show quickly that OT is clean. Isolation has been exercised at GCC-1 only (R-012), and OT monitoring has gaps at 22 stations (R-003, R-010).
2. **PS-3 integration (ER-04).** Flat networks, local accounts, unencrypted polling, no hot standby, and an incomplete inventory (R-005, R-058, R-059, R-060, R-064). The amended Cybersecurity Implementation Plan schedule ends 2027-06-30.
3. **Legacy station controls (ER-01).** 22 stations with end-of-support components (R-004, R-006) and shared accounts on legacy HMIs (R-007).
4. **Vendors with OT reach (ER-03).** Always-on modems (R-008), no software bills of materials (R-031), and the SCADA update path (R-030).
5. **Disclosure readiness (ER-06).** The materiality process has not been exercised for a curtailment or shutdown (R-013).
6. **AI (ER-08).** The leak model's coverage gaps and vendor change control (R-039, R-040, R-042); 4 unreviewed use cases (R-043).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $14.8 million:** station HMI and PLC replacement first phase ($6.9M), OT monitoring sensors at 22 stations ($1.6M), PS-3 segmentation and encryption ($2.2M, part of the PS-3 integration budget), second PS-3 carrier and cellular path diversity ($1.3M), vendor modem replacement ($0.4M), SCADA platform resilience drill and golden images ($0.5M), OT staff ($1.6M), and outside counsel for the disclosure tabletop ($0.3M). Items map to the POA&M in P07.
- **Accepted (7):** R-022, R-044, R-045, R-050, R-052, R-057, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 (unapproved generative AI domains blocked) and R-065 (no ransom payment without the POL-03 conditions).
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances, and the status of TSA plan schedules. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and disclosure control topics (R-013, R-062). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, at PS-3 cutover, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
