# Enterprise Risk Register Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm: 48 farms, 17 packing sites, 6 irrigation control centers; FL, GA, SC, NC) |
| Size tier | Enterprise (up to 12,000 employees at the seasonal peak) |
| Vertical | Agriculture, Forestry, Fishing and Hunting |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | NIST CSF 2.0 GV.RM and ID.RA outcomes (benchmark, P03); the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that support tier-1 processes or hold worker, grower, or customer information across the 48 farms, 17 packing sites, 6 regional irrigation control centers, two clouds, and two data center campuses, including the two acquired operations (AQ-01 and AQ-02) and about 1,100 vendors (190 with system access or sensitive data). Business processes and impact values come from the enterprise BIA (P05). The Farm Management and Irrigation Control Platform (FMICP) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business, IT, and OT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Worker and food safety:** very low appetite for technology-related harm to workers (fertigation, chemigation, equipment) or to the safety of food the company ships.
- **Regulatory and disclosure:** very low appetite for noncompliance with Produce Safety, H-2A, Worker Protection Standard, or SEC disclosure rules.
- **Crop and harvest continuity:** low appetite for disruption of irrigation, freeze protection, harvest, packing, and shipping.
- **Personal information:** low appetite for unauthorized disclosure of worker, grower, or customer information.
- **Growth and innovation (acquisitions, grower services, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Farm operations disruption from cyber and technology events | Moderate |
| ER-02 Compromise of worker, grower, and customer information | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired operations | Moderate |
| ER-05 Worker safety, food safety, and command integrity in OT | Low |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the food and agriculture threat picture (ransomware in harvest season, OT vendor remote access, field device vulnerabilities, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3): for example, Very High means more than $20 million cumulative loss, a plausible worker injury or chemical exposure, or a missed SEC filing.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (strategic, operational, safety, compliance, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 36 |
| Low | 18 |
| **Total** | **65** |

By threat source type: Adversarial 27, Structural 19, Accidental 17, Environmental 2.
By treatment: Mitigate 55, Accept 8, Avoid 1, Share/Transfer 1.
By status: In progress 42, Open 15, Closed (accepted) 8.
**23 risks are outside tolerance** and each has a dated treatment plan; all 23 are reported to the board risk committee.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Farm operations disruption from cyber and technology events | Operational | 13 | 1 | 3 | 8 | 1 | **Very High** | Moderate | 4 |
| ER-02 | Compromise of worker, grower, and customer information | Compliance and reputational | 10 | 0 | 1 | 4 | 5 | **High** | Moderate | 1 |
| ER-03 | Third-party and concentration risk | Operational | 10 | 0 | 2 | 5 | 3 | **High** | Moderate | 2 |
| ER-04 | Integration of acquired operations | Strategic | 5 | 0 | 2 | 3 | 0 | **High** | Moderate | 2 |
| ER-05 | Worker safety, food safety, and command integrity in OT | Safety | 7 | 0 | 1 | 5 | 1 | **High** | Low | 6 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 10 | 0 | 1 | 4 | 5 | **High** | Low | 5 |
| ER-07 | Financial reporting integrity and fraud | Financial | 4 | 0 | 0 | 3 | 1 | **Moderate** | Low | 3 |
| ER-08 | Responsible use of AI | Strategic | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |
| | **Total** | | **65** | **1** | **10** | **36** | **18** | | | **23** |

**Reading the profile:**
- **ER-01 (farm operations disruption)** carries the only Very High risk, enterprise ransomware in season (R-001). The acquisition pathway (R-003) and OT vendors outside the gateway (R-004) are the main reasons its likelihood is not lower. Freeze protection (R-007) and SCADA master recovery (R-012) are High because a single night or a day of heat can destroy a crop.
- **ER-05 (worker safety, food safety, and command integrity)** has the lowest tolerance and the most risks outside it (6 of 7). The driver is fertigation and chemigation change control: a combined edit-and-release role, missing change approvals, and stations without integrity checks (R-006, R-014, R-037).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has never been exercised with an OT outage scenario and the disclosure committee has 3 new members (R-017). Traceability readiness (R-026) and hub farm status (R-049) are the food regulatory items.
- **ER-08 (AI)** is within tolerance today, but 4 of 11 use cases lack committee review (R-045) and AI-001 bias testing is incomplete (R-043), so the rating depends on the reviews due by 2026-12-31 and 2027-01-31.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts IT systems, SCADA masters, and packing site systems across several regions during a harvest or freeze season | Very High | ER-01 | Close acquisition gaps (POAM-013); INT-4 and INT-5 onto the OT gateway (POAM-004); SCADA restore within RTO (POAM-011); enterprise ransomware exercise with OT outage and the disclosure committee (POAM-012) | CISO | 2027-01-31 |
| R-002 | Payroll, H-2A worker, and grower files are stolen during a ransomware attack | High | ER-02 | Egress anomaly models; remove payroll exports from file shares; warehouse minimization (R-053) | Director of Security Operations | 2027-03-31 |
| R-003 | Attacker enters through an AQ-01 flat network and reaches enterprise systems over the legacy site VPN | High | ER-04 | VPN rule removed 2026-09-04; SD-WAN migration and identity federation (POAM-013; POAM-001) | Vice President, Integration Management Office | 2027-03-31 |
| R-004 | Attacker uses INT-4 or INT-5 remote tools to reach pump station PLCs and change settings | High | ER-03 | Move onto the gateway; remove tools; amend agreements (POAM-004) | Director of OT Security | 2026-12-31 |
| R-005 | Shared logins in the AQ-02 pivot cloud service used to command about 180 pivots | High | ER-04 | Named accounts with MFA by 2026-11-15; migrate to company SCADA (POAM-002) | Vice President, Integration Management Office | 2027-06-30 |
| R-006 | Fertigation or chemigation settings changed without approval, exposing workers or water sources | High | ER-05 | Role split (POAM-007); change enforcement (POAM-006); integrity checks and automatic injection stop (POAM-019) | SCADA Engineering Manager | 2027-03-31 |
| R-007 | Freeze protection does not start on a freeze night because automation, alarms, or field links fail | High | ER-01 | Cyber outage injection in the November freeze drill (POAM-022); radio for the last 11 freeze stations | Vice President, Irrigation and Water Resources | 2026-11-30 |
| R-012 | SCADA masters cannot be restored within the 6-hour RTO | High | ER-01 | Pre-staged images, automated restore, retest (POAM-011) | SCADA Engineering Manager | 2027-01-31 |
| R-017 | A material incident is disclosed late or inaccurately because the materiality process fails under pressure | High | ER-06 | OT factors in the playbook; brief new members; tabletop 2026-11-17 (POAM-012) | General Counsel | 2026-11-30 |
| R-021 | A carrier outage on the private APN cuts about 80% of field OT traffic | High | ER-03 | Second carrier for pivots in R1 and R3; radio expansion (POAM-024) | Director of Network Engineering | 2027-06-30 |
| R-025 | A zero-day in an internet-facing edge device is exploited, including legacy AQ-01 firewalls | High | ER-01 | Retire AQ-01 edge devices with SD-WAN migration (POAM-013); 72-hour emergency patch SLA | Director of Network Engineering | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **OT third-party access (ER-03, ER-05).** Two irrigation integrators and the AQ-02 pivot cloud service reach field OT outside the OT remote access gateway, without MFA or recording (R-004, R-005). The same stations lack change approvals and integrity checks (R-006, R-014). These are the conditions most likely to turn a cyber event into a safety or crop-loss event. Treatment is due before or early in the 2026-27 freeze season.
2. **Acquisition integration (ER-04).** AQ-01 runs flat networks, a legacy directory, shared tally logins, and nightly-only backups (R-003, R-016, R-019); AQ-02 runs pivots from a vendor cloud (R-005). Treatment: SD-WAN migration, identity federation, and SCADA migration by 2027-06-30. Future deals must fund integration up front (R-059).
3. **Concentration (ER-03).** One APN carrier (R-021), one FMIS tenant (R-020), and one cold-chain monitoring SaaS without a SOC report (R-030) each sit under processes with short MTDs. Contracts and manual fallbacks carry most of the treatment.
4. **Recovery (ER-01).** The SCADA master restore missed its RTO by 3.5 hours (R-012), and the freeze plan has never been drilled with SCADA unavailable (R-007).
5. **Materiality and disclosure (ER-06).** The playbook has no OT outage or crop loss factors, and the disclosure committee has not exercised it since three members joined (R-017). A full tabletop is set for 2026-11-17.
6. **AI (ER-08).** AI-001 now feeds crew planning and draft H-2A job orders (R-042, R-043). Unapproved generative AI tools are blocked (R-041, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million:** OT gateway onboarding of INT-4, INT-5, and packing vendors ($420K), AQ-01 SD-WAN migration and identity federation ($1.3M), AQ-02 pivot migration onto SCADA ($1.6M), passive OT monitoring for 290 more pump stations ($1.1M), HMI replacement ($980K, 2027), pivot modem firmware and panel replacement ($850K), second carrier and radio expansion ($620K), SCADA restore automation ($240K), traceability data integration ($210K), and outside counsel for the disclosure tabletop ($40K). Items map to the POA&M in P07.
- **Accepted (8):** R-034, R-035, R-051, R-054, R-055, R-056, R-061, R-063. Each is Low or Moderate residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-041. Unapproved generative AI domains are blocked, and an approved enterprise assistant is offered.
- **Shared (1):** R-065. OT and contingent business interruption coverage will be negotiated at the 2027 cyber insurance renewal.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-038), and the disclosure controls topics (R-017, R-018). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
