# Enterprise Risk Register Report: Cris Santos Company | Utilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility; distribution and transmission in Florida and south Georgia; NERC DP, TO, TOP) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Utilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Input to the Reg S-K Item 106 description of risk management processes; the risk assessment the CIP-013-2 R1.1 process and the CIP-014-3 program rely on for prioritization (not a substitute for either) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and reliability committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All IT and OT systems across the control centers, 564 substations, the field network, the two clouds and two data centers, the two service lines, and the roughly 1,400 vendors (310 with system or data access). Business processes and impact values come from the enterprise BIA (P05). The Distribution Operations Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, customer operations, and IT (first line) own and treat risks. The GRC team, the Chief Risk Officer, and the Chief Compliance Officer's NERC compliance team (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Bulk electric system reliability and NERC compliance:** very low appetite. A known or potential NERC noncompliance is never accepted; it is mitigated and self-reported.
- **Public and worker safety:** very low appetite for technology-related harm (switching errors, clearances, hazard response).
- **Service continuity:** low appetite for cyber-caused outages of distribution service.
- **Customer data:** low appetite for unauthorized disclosure.
- **Regulatory and disclosure:** very low appetite for SEC, FTC, or state law failures.
- **Growth and innovation (service lines, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Bulk electric system reliability and NERC CIP | Low |
| ER-02 Distribution operations and public and worker safety | Moderate |
| ER-03 Compromise of customer data | Moderate |
| ER-04 Third-party and supply chain | Moderate |
| ER-05 Regulatory, disclosure, and compliance program | Low |
| ER-06 Enterprise IT continuity and fraud | Moderate |
| ER-07 Service line commitments (SL-1 and SL-2) | Moderate |
| ER-08 Responsible use of AI and models | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the risk and reliability committee |
| Very High | CEO and CFO jointly, reported to the risk and reliability committee at its next meeting |

Any acceptance expires after 12 months. Safety risks (ER-02) at High or above cannot be accepted without a dated treatment plan.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the utility threat picture (nation-state pre-positioning in OT, vendor remote access, physical attacks on substations, ransomware, storms); the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance, so one severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the risk and reliability committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 39 |
| Low | 16 |
| **Total** | **66** |

By threat source type: Adversarial 31, Structural 25, Accidental 9, Environmental 1.
By treatment: Mitigate 55, Accept 8, Avoid 2, Share/Transfer 1.
By status: In progress 52, Open 4, Closed (accepted) 8, Closed (avoided) 2.
**22 risks are outside tolerance**; each has a dated treatment plan and is reported to the board (`board_reported` = Yes).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Bulk electric system reliability and NERC CIP | Operational and compliance | 13 | 0 | 2 | 8 | 3 | **High** | Low | 10 |
| ER-02 | Distribution operations and public and worker safety | Operational | 16 | 1 | 3 | 10 | 2 | **Very High** | Moderate | 4 |
| ER-03 | Compromise of customer data | Compliance and reputational | 8 | 0 | 1 | 4 | 3 | **High** | Moderate | 1 |
| ER-04 | Third-party and supply chain | Operational | 5 | 0 | 1 | 2 | 2 | **High** | Moderate | 1 |
| ER-05 | Regulatory, disclosure, and compliance program | Compliance | 6 | 0 | 1 | 3 | 2 | **High** | Low | 4 |
| ER-06 | Enterprise IT continuity and fraud | Operational and financial | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-07 | Service line commitments (SL-1 and SL-2) | Strategic | 5 | 0 | 0 | 3 | 2 | **Moderate** | Moderate | 0 |
| ER-08 | Responsible use of AI and models | Strategic and operational | 7 | 0 | 0 | 5 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-02 (distribution operations)** carries the only Very High risk: a vendor remote support path into the ADMS (R-002), found live during Internal Audit testing and disabled the next day. The redesign is due 2026-11-30.
- **ER-01 (BES reliability and CIP)** has a low tolerance, so 10 of its 13 risks are outside it even though none is Very High. The two High risks are nation-state pre-positioning in OT (R-001) and a physical attack on Substation P (R-009). The CIP-specific findings (R-014, R-015, R-058, R-059, R-060) are Moderate or Low as risks, but each is also a potential noncompliance being self-reported (R-013), which is why the compliance view and the risk view are reported together.
- **ER-05 (regulatory and disclosure)** is outside tolerance because the SEC materiality process has never been exercised with an OT scenario (R-016) and the Identity Theft Prevention Program is stale (R-056).
- **ER-07 and ER-08** are within tolerance, but the fleet charging SOC 2 gap (R-052) and model drift (R-046) are the items to watch.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Attacker uses a vendor remote support path into the ADMS and issues unauthorized switching commands | Very High | ER-02 | Rebuild vendor support through jump hosts and OT PAM (POAM-001); quarterly path discovery | Director, OT Security | 2026-11-30 |
| R-001 | Nation-state actor pre-positioned in OT triggers coordinated outages | High | ER-01 | OT sensors at all fiber-connected distribution substations (POAM-004); quarterly OT threat hunts | CISO | 2027-12-31 |
| R-004 | Ransomware on corporate IT spreads to the OMS, the ADMS DMZ, and billing | High | ER-06 | Remove corporate-to-historian rules (POAM-002); ransomware exercise with the disclosure committee (POAM-011) | CISO | 2026-12-31 |
| R-005 | Bulk remote disconnect misuse cuts power to tens of thousands of customers | High | ER-02 | Two-person approval and per-command limit (POAM-018) | Vice President, Customer Operations | 2026-12-15 |
| R-009 | Coordinated physical attack on Substation P | High | ER-01 | Complete the barrier; document the R5 timeline revision (POAM-025) | Director, Corporate Security | 2027-03-31 |
| R-011 | Malicious code in a trusted OT vendor update | High | ER-04 | Integrity checks for all ADMS and field updates; SBOMs from tier-1 OT vendors | Director, Third-Party Risk Management | 2027-06-30 |
| R-012 | OMS fails or is cyber-degraded during a hurricane | High | ER-02 | Storm-volume standby test; cyber scenario in the hurricane exercise (POAM-027) | Vice President, Distribution Operations | 2027-05-31 |
| R-016 | Material OT incident disclosed late or inaccurately | High | ER-05 | BIA costs in the worksheet; OT tabletop 2026-11-18 (POAM-011) | General Counsel | 2026-12-15 |
| R-017 | Customer SSNs and bank account numbers stolen from the CIS or export area | High | ER-03 | SSN purge; fewer export rights; masked export area (POAM-026) | Vice President, Customer Operations | 2027-03-31 |
| R-028 | Hurricane damages the GOC (DCC, SOC, and storm command co-located) | High | ER-02 | Storm command backup at the Georgia Operations Center; split-site SOC staffing | Director, Emergency Management | 2027-05-31 |
| R-035 | Zero-day in an internet-facing edge device | High | ER-06 | Zero-trust broker; retire the legacy VPN | Director, Network Engineering | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **Vendor paths into OT (ER-02, ER-04).** 64 vendors have remote access paths into OT. 63 use the jump hosts or Intermediate Systems; the ADMS vendor appliance did not (R-002). Supply chain controls for CIP-scope purchases also slipped (R-030, R-011).
2. **Visibility at the grid edge (ER-02).** OT monitoring stops at 41% of distribution substations, and 159 substations use legacy gateways that cannot authenticate commands (R-006, R-007). These are multi-year capital items.
3. **NERC CIP findings (ER-01, ER-05).** Five potential noncompliances will be self-reported to SERC by 2026-09-30 (R-013), and the internal checks behind them were done by the team that operates the controls (R-040).
4. **Storms multiply cyber impact (ER-02).** The OMS standby, the GOC co-location, and the contact center surge are the weak points if a cyber event coincides with a hurricane (R-012, R-028).
5. **Customer data (ER-03, ER-05).** SSNs for closed accounts, broad export rights, and a stale Identity Theft Prevention Program (R-017, R-019, R-055, R-056).
6. **AI (ER-08).** 12 use cases; 8 reviewed; drift monitoring for load forecasting is manual (R-046), and theft analytics have not been tested for uneven flag rates (R-042). The deposit risk score was disabled pending review (R-044, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q4), about $27.6 million:** OT sensors at distribution substations ($6.2M), legacy gateway replacement first phase ($9.4M), ADMS console and historian refresh ($3.1M), ADMS failover automation ($1.2M), vendor support redesign ($0.4M), Substation P barrier ($4.8M), second LTE core site design ($0.9M), CIS data minimization and Red Flags program update ($0.8M), SL-2 SOC 2 readiness ($0.6M), and outside counsel for the disclosure tabletop ($0.2M). Items map to the POA&M in P07.
- **Accepted (8):** R-029, R-032, R-038, R-048, R-053, R-054, R-064, R-066. Each is Low residual with strong existing controls, accepted at the right level (section 1), and reviewed within 12 months. None is a NERC noncompliance.
- **Avoided (2):** R-041 (unapproved generative AI domains blocked) and R-044 (deposit risk score disabled until notice logic and fairness testing are reviewed).
- **Shared/transferred (1):** R-065 (cyber physical damage endorsement at the 2027 insurance renewal).
- **Very High risk R-002:** not accepted. The CEO and CFO approved the treatment plan and the residual target of Moderate on 2026-09-08; the risk and reliability committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and reliability committee (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with treatment status and KRI trend, the 22 risks outside tolerance, new risks, acceptances, and NERC self-report status. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and disclosure controls topics (R-016).
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-08.
- Risk and reliability committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or CIP-002 categorization change. KRIs are refreshed quarterly.
