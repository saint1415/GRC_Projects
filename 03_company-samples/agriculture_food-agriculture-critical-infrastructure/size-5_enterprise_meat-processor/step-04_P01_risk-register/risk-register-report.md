# Enterprise Risk Register Report: Cris Santos Company | Food and Agriculture | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products: 8 plants, 4 distribution centers; FL, GA, AL, NC, TN, TX) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Food and Agriculture (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk, with SP 800-82 Rev. 3 for OT threat context; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | The PLT-07 food defense reanalysis (21 CFR 121.157(b)(2)) for cyber-physical process steps; the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO, with the SVP FSQA and the Director of OT Security; updated 2026-08-28 with Internal Audit findings (P07) and the AI council review (P10) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** The 8 plants, 4 distribution centers, headquarters, the two cloud estates and two colocation sites, the acquired plant PLT-08, and the roughly 1,400 vendors (65 with OT remote access). Business processes and impact values come from the enterprise BIA (P05). The Plant Production and Cold-Chain Monitoring System (PPCM) is also covered at system level in the SSP (P02).

**What makes this register different from an office IT register.** Many risks here end in adulterated or temperature-abused food, or in an ammonia release, not in lost data. Impact ratings therefore weigh consumer health, product holds and recalls, worker safety, and FSIS or FDA action, as well as downtime and cost.

**Three lines.** Risk owners in operations, FSQA, and IT (first line) own and treat risks. The GRC team, the OT Security team's risk analyst, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Food safety and product integrity:** very low appetite for any technology event that could put adulterated or misbranded product into commerce.
- **Worker and process safety:** very low appetite for technology events that could cause an ammonia release or machinery harm.
- **Regulatory and disclosure:** very low appetite for noncompliance with FSIS, FDA, EPA reporting, or SEC disclosure rules.
- **Production continuity:** low appetite for multi-plant disruption; moderate for single-line disruption.
- **Data protection:** low appetite for disclosure of personal information, formulations, or customer specifications.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Production and supply disruption from cyber and technology events | Moderate |
| ER-02 Food safety and product integrity from cyber-physical tampering or error | Low |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired operations | Moderate |
| ER-05 Worker and process safety from OT (ammonia, machinery) | Low |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Data protection and fraud (personal data, trade secrets, payments) | Moderate |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel, SVP FSQA), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Food safety (ER-02) and worker safety (ER-05) risks at High or above cannot be accepted; they must be treated with a dated plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 (OT threats and vulnerabilities), the sector threat picture (ransomware against food processors, vendor remote access, cyber-physical tampering), the BIA (P05), the gap analysis (P03), the AI council review (P10), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3), which include food safety and worker safety.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance, so one severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 32 |
| Low | 20 |
| **Total** | **65** |

By threat source type: Adversarial 28, Structural 27, Accidental 8, Environmental 2.
By treatment: Mitigate 55, Accept 8, Avoid 2.
By status: In progress 33, Open 22, Closed (accepted) 8, Closed (avoided) 2.
**26 risks are outside tolerance** and each has a dated treatment plan. All 26 are reported to the board (`board_reported` = Yes).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Production and supply disruption from cyber and technology events | Operational | 13 | 1 | 2 | 8 | 2 | **Very High** | Moderate | 3 |
| ER-02 | Food safety and product integrity from cyber-physical tampering or error | Food safety | 11 | 0 | 2 | 7 | 2 | **High** | Low | 9 |
| ER-03 | Third-party and concentration risk | Operational | 9 | 0 | 2 | 3 | 4 | **High** | Moderate | 2 |
| ER-04 | Integration of acquired operations | Strategic | 4 | 0 | 1 | 3 | 0 | **High** | Moderate | 1 |
| ER-05 | Worker and process safety from OT (ammonia, machinery) | Safety | 5 | 0 | 2 | 2 | 1 | **High** | Low | 4 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 10 | 0 | 1 | 4 | 5 | **High** | Low | 5 |
| ER-07 | Data protection and fraud (personal data, trade secrets, payments) | Compliance and reputational | 7 | 0 | 1 | 2 | 4 | **High** | Moderate | 1 |
| ER-08 | Responsible use of AI | Strategic | 6 | 0 | 1 | 3 | 2 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (production disruption)** carries the only Very High risk, multi-plant ransomware (R-001). PLT-05 and PLT-08, which sit outside the OT DMZ standard, are the main reason its likelihood is not lower.
- **ER-02 (food safety)** has the lowest tolerance and the most risks outside it (9). The two High risks are about who can change formulations: HMI overrides without a second approval (R-003) and a compromise of the central MES that would reach every plant at once (R-004).
- **ER-05 (worker and process safety)** is outside tolerance because refrigeration controllers can be reached through a contractor modem at PLT-05 (R-006) and, until 2026-08-14, with default passwords at DC-03 (R-016).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the materiality process has never been exercised with a production halt and recall (R-010).
- **ER-08 (AI)** is within its Moderate tolerance overall but holds one High risk: PLT-03 cut manual inspection after AI vision went live (R-012).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware spreads from IT to plant OT and the central MES and halts lines and cold-chain monitoring at several plants | Very High | ER-01 | Close PLT-05 and PLT-08 boundary gaps (POAM-001, POAM-003); MES RTO retest (POAM-010); OT monitoring at all plants (POAM-011); ransomware exercise with the disclosure committee (POAM-014) | CISO | 2027-03-31 |
| R-002 | Attacker enters through PLT-08's flat network or its integrator VPN without MFA | High | ER-04 | Supervised VPN sessions now; segmentation, identity, and gateway (POAM-001, POAM-002) | Vice President, Integration Management Office | 2027-03-31 |
| R-003 | Supervisor-level HMI override of cure or brine setpoints puts over-cured or under-cured product into commerce | High | ER-02 | Second-badge overrides and alerts (POAM-005); batch-start verification (SI-6) | SVP FSQA | 2027-03-31 |
| R-004 | Compromise of the central MES pushes altered formulations to every connected plant | High | ER-02 | Automated integrity comparison (SI-7(1)); signing key custody under FSQA | Vice President, Engineering | 2027-03-31 |
| R-005 | Cold-chain monitoring vendor outage removes monitoring at all sites; manual fallback untested at 9 sites | High | ER-03 | Contracted RTO; manual log exercises at every site (POAM-008) | Vice President, Distribution and Transportation | 2027-03-31 |
| R-006 | PLT-05 refrigeration controller reached through the contractor modem | High | ER-05 | Modem disconnected except supervised sessions; OT DMZ and gateway (POAM-003) | Director of Refrigeration and Process Safety | 2026-12-31 |
| R-007 | Exploit of an unsupported HMI or engineering workstation | High | ER-01 | Replace or isolate unsupported assets (POAM-004) | Director of OT Security | 2027-12-31 |
| R-008 | OT recovery fails or overruns its RTO | High | ER-01 | Automated MES failover; restore tests at 4 more plants (POAM-010) | Vice President, Engineering | 2027-01-31 |
| R-010 | Material incident disclosed late or inaccurately; production-halt and recall scenario never exercised | High | ER-06 | Playbook update; tabletop 2026-11-18 (POAM-014) | General Counsel | 2026-11-30 |
| R-011 | Compromised OT vendor remote access used to reach SCADA | High | ER-03 | Remaining 14 vendors to the gateway; tier-1 reviews (POAM-015) | Director of Third-Party Risk Management | 2027-03-31 |
| R-012 | Reliance on AI vision leads to reduced manual inspection and foreign material ships | High | ER-08 | Restore inspection at PLT-03; HACCP reassessment gate (POAM-021) | SVP FSQA | 2026-10-31 |
| R-014 | Employee and online customer personal information exfiltrated in a ransomware attack | High | ER-07 | Egress anomaly detection; data minimization | Director of Security Operations | 2027-03-31 |
| R-016 | Default password on a refrigeration controller or X-ray system used by an attacker | High | ER-05 | Passwords changed 2026-08-14; credential sweep at 12 sites (POAM-012) | Director of OT Security | 2026-12-31 |

**The common thread.** Most High risks are about **who can change what the plant does, and from where.** Three entry paths stay open (PLT-08, the PLT-05 modem, legacy vendor paths), and two control points are weaker than the rest of the design (HMI overrides and MES recovery). Closing them also lowers several Moderate risks, including R-021, R-022, R-026, R-028, R-046, and R-065.

**Food defense link.** R-003, R-004, and R-047 are intentional adulteration scenarios carried out through the control system rather than by hand. For PLT-07 they are inputs to the reanalysis required after the MES migration (21 CFR 121.157(b)(1); R-009; POAM-006). For the other plants they feed the voluntary functional food defense plans.

**New risks from testing and review.** R-016 was added on 2026-08-14 after Internal Audit found default passwords (P07). R-012 was raised to High on 2026-08-26 after the AI council learned of the PLT-03 inspection change (P10).

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** PLT-08 is on a legacy directory, a flat network, an integrator VPN without MFA, and a legacy eHACCP application (R-002, R-062, R-065). Treatment: integration by 2027-03-31. Going forward, deal approvals must include security due diligence and integration funding (R-061).
2. **Setpoint and recipe integrity (ER-02).** The central MES made recipe control stronger and more concentrated at the same time: one place to enforce two-person approval, and one place an attacker would aim for (R-003, R-004, R-047).
3. **Cold-chain concentration (ER-03).** One vendor, no contracted recovery time, an exception in its SOC 2 report, and a manual fallback exercised at only 3 of 12 sites (R-005).
4. **Legacy OT (ER-01).** 118 unsupported HMIs, 9 unsupported engineering workstations, and OT patching limited to sanitation windows (R-007, R-026).
5. **Disclosure readiness (ER-06).** The disclosure committee has never practiced a production halt with product holds and recalls, which is how a food company's material incident would most likely look (R-010).
6. **AI governance (ER-08).** A plant changed a food safety staffing practice because of an AI tool without HACCP reassessment or council approval (R-012).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q4), about $9.4 million:** PLT-08 integration security work ($2.1M); OT DMZ, gateway, and monitoring at PLT-05 ($640K); replacement of unsupported HMIs and engineering workstations ($3.8M over two years); HMI second-badge override and integrity comparison in the MES ($720K); MES failover automation ($310K); OT monitoring and EDR at PLT-05 and PLT-08 ($460K); cold-chain contract renegotiation and manual log exercises ($180K); vendor review backlog ($240K); plant training kiosks ($520K); outside counsel and a facilitator for the disclosure tabletop ($60K); credential sweep and commissioning checks ($90K); PLT-03 inspection staffing restored ($280K a year). Items map to the POA&M in P07.
- **Accepted (8):** R-033, R-036, R-044, R-048, R-049, R-050, R-052, R-055. Each is Low residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 and R-043. Unapproved generative AI domains are blocked, and individual identification is disabled in the worker safety camera analytics.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-020), and disclosure controls topics (R-010, R-019). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or the PLT-07 food defense reanalysis. KRIs are refreshed quarterly.
