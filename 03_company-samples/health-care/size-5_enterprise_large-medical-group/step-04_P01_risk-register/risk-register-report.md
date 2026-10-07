# Enterprise Risk Register Report: Cris Santos Company | Health Care | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group: 140 clinics, 6 ASCs, 12 imaging centers, 1 central lab; FL, GA, AL, SC) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Health Care and Social Assistance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | HIPAA risk analysis and risk management (45 CFR 164.308(a)(1)(ii)(A)-(B)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that create, receive, maintain, or transmit ePHI or support tier-1 processes across the 159 sites, the two cloud estates and two colocation data centers, the eight acquired practices, and the roughly 900 vendors (320 with PHI). Business processes and impact values come from the enterprise BIA (P05). The Laboratory Information System is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Patient safety:** very low appetite for technology-related harm to patients.
- **Regulatory and disclosure:** very low appetite for noncompliance with HIPAA, CLIA, CMS conditions, Section 1557, or SEC disclosure rules.
- **Care delivery continuity:** low appetite for disruption of tier-1 clinical services.
- **Protected health information:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Care delivery disruption from cyber and technology events | Moderate |
| ER-02 Compromise of protected health information | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired practices | Moderate |
| ER-05 Patient safety from technology (devices, lab, clinical systems) | Low |
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

Patient-safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the Health Care sector threat picture (ransomware, third-party concentration, medical devices), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (strategic, operational, clinical, compliance, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 38 |
| Low | 16 |
| **Total** | **65** |

By threat source type: Adversarial 29, Structural 27, Accidental 8, Environmental 1.
By treatment: Mitigate 55, Accept 8, Avoid 2.
By status: In progress 43, Open 14, Closed (accepted) 8.
**19 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Care delivery disruption from cyber and technology events | Operational | 13 | 1 | 1 | 8 | 3 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of protected health information | Compliance and reputational | 13 | 0 | 1 | 9 | 3 | **High** | Moderate | 1 |
| ER-03 | Third-party and concentration risk | Operational | 8 | 0 | 3 | 4 | 1 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired practices | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-05 | Patient safety from technology (devices, lab, clinical systems) | Clinical | 8 | 0 | 3 | 2 | 3 | **High** | Low | 5 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 9 | 0 | 1 | 5 | 3 | **High** | Low | 6 |
| ER-07 | Financial reporting integrity and fraud | Financial | 3 | 0 | 0 | 1 | 2 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI | Strategic and clinical | 6 | 0 | 0 | 5 | 1 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (care delivery disruption)** carries the only Very High risk, enterprise ransomware (R-001). The acquisition pathway (R-003, ER-04) is the main reason its likelihood is not lower.
- **ER-05 (patient safety)** has the lowest tolerance and three High risks: unsupported medical devices (R-006) and two lab result-integrity risks (R-009, R-010).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised with the current disclosure committee (R-017).
- **ER-08 (AI)** is within tolerance today, but 5 of 14 use cases lack council review (R-013), so the rating depends on the reviews due 2026-11-30.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts clinical and business systems across multiple regions | Very High | ER-01 | Close acquisition gaps (R-003); EDR at AQ sites (POAM-013); LIS RTO fix (POAM-011); annual enterprise ransomware exercise including the disclosure committee (POAM-014) | CISO | 2027-01-31 |
| R-002 | Exfiltration of PHI during a ransomware attack (double extortion) | High | ER-02 | Egress anomaly models for cloud storage; data minimization in the warehouse (R-053) | Director of Security Operations | 2027-03-31 |
| R-003 | Attacker enters through an acquired practice's flat network and reaches enterprise systems over the site VPN | High | ER-04 | Restrict VPN to named hosts; SD-WAN migration; identity federation (POAM-016; POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| R-005 | Primary clearinghouse outage or compromise stops 70% of claims and most eligibility checks for weeks | High | ER-03 | Surge contract with the secondary clearinghouse; payer-portal fallback test (POAM-019) | Vice President, Revenue Cycle | 2027-01-31 |
| R-006 | Attacker exploits an unsupported operating system on a networked medical device or analyzer | High | ER-05 | Document deviations; segment remaining sites; refresh plan for unsupported devices (POAM-009; POAM-018) | Director of Clinical Engineering | 2027-06-30 |
| R-009 | Wrong lab results are released because an autoverification rule or test build change was not independently validated | High | ER-05 | Lab change board; role split; automated block (POAM-003); rule attribution (POAM-007) | Laboratory Director | 2026-12-15 |
| R-010 | A result is filed to the wrong patient or field, or altered after verification, and nobody detects it | High | ER-05 | Daily reconciliation and integrity alerting (POAM-006) | LIS Application Manager | 2027-03-31 |
| R-017 | A material incident is disclosed late or inaccurately because the materiality process fails under pressure | High | ER-06 | Update playbook; brief new members; full tabletop 2026-11-12 (POAM-014) | General Counsel | 2026-11-30 |
| R-025 | A third party with PHI suffers a breach | High | ER-03 | Review inherited contracts (POAM-022); continuous monitoring of tier-1 and tier-2 vendors | Director of Third-Party Risk Management | 2027-03-31 |
| R-030 | Malicious code arrives in a trusted vendor software update | High | ER-03 | Staged rollout for tier-1 software; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-048 | Zero-day in an internet-facing edge device (VPN or firewall) is exploited | High | ER-01 | Retire legacy AQ edge devices with SD-WAN migration (POAM-016); emergency patch SLA 72 h | Director of Network Engineering | 2027-01-31 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** Three acquired practices (AQ-06 to AQ-08) are on legacy identity and flat networks, and two run their own EHRs without SIEM audit feeds. These conditions raise the likelihood of enterprise ransomware (R-001, R-003), late terminations (R-004), undetected snooping (R-016), and data loss (R-015). Treatment: identity federation, SD-WAN migration, and EHR migration, all due by 2027-04-30. Going forward, deal approvals must include security due diligence and integration funding (R-061).
2. **Clearinghouse concentration (ER-03).** 70% of claims go through one clearinghouse, and the manual fallback has never been tested (R-005). The industry saw this failure mode in 2024. Treatment: contracted surge capacity and a fallback test by 2027-01-31.
3. **Medical devices (ER-05).** About 85% of 9,000 networked devices are inventoried, 1,100 run unsupported operating systems, and NAC covers 60% of sites (R-006, R-007, R-008). Testing found default passwords on 3 analyzers (R-058).
4. **AI (ER-08).** 14 use cases; 9 reviewed; bias testing only on vendor data (R-012, R-013). The AI resume-ranking feature was switched off pending review (R-043, treatment Avoid).
5. **Materiality and disclosure (ER-06).** The materiality playbook has not been exercised with the disclosure committee since the 2025 acquisitions (R-017). A full tabletop is set for 2026-11-12.
6. **Legacy audit logging.** The two acquired-practice EHRs send no audit logs to the SIEM (R-016, R-057).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $6.1 million:** acquired-practice identity federation ($1.4M), analyzer refresh brought forward ($2.3M), NAC expansion ($1.1M), SD-WAN migration of the AQ sites ($650K), device discovery ($420K), LIS vendor services for integrity controls ($145K), LIS standby database ($90K per year), and outside counsel for the disclosure tabletop ($35K). Items map to the POA&M in P07.
- **Accepted (8):** R-021, R-029, R-033, R-044, R-047, R-050, R-052, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041, R-043. Unapproved generative AI domains are blocked, and AI resume ranking is disabled until review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and the disclosure controls topics (R-017, R-019). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
