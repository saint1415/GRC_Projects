# Enterprise Risk Register Report: Cris Santos Company | Healthcare and Public Health | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Healthcare and Public Health |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | HIPAA risk analysis and risk management (45 CFR 164.308(a)(1)(ii)(A)-(B)); the security risk analysis measure for the Promoting Interoperability Program (42 CFR 495.24); the facility-based risk assessment input to the unified emergency plan (42 CFR 482.15(a)(1) and (f)(4)(ii)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-05-04 to 2026-06-26 by the GRC team for the CISO; updated 2026-08-07 with Internal Audit findings (P07) and 2026-08-14 with the AI review (P10) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-08-24; reviewed by the risk committee of the board, 2026-09-15 |

## 1. Scope and risk framing
**Scope.** All systems that create, receive, maintain, or transmit ePHI or support tier-1 processes across the 8 hospitals (including H-08), 3 freestanding EDs, 46 clinics, 4 imaging centers, the two data centers and two clouds, the two service lines sold to other organizations, and the roughly 1,500 vendors (430 with PHI). Business processes and impact values come from the enterprise BIA (P05). The ECIS is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the hospitals and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Patient safety:** very low appetite for technology-related harm to patients, including harm from delayed emergency care during an outage.
- **Regulatory and disclosure:** very low appetite for noncompliance with HIPAA, CMS conditions of participation, EMTALA, CLIA, Section 1557, 42 CFR Part 2, or SEC disclosure rules.
- **Care delivery continuity:** low appetite for disruption of emergency, inpatient, and surgical services.
- **Protected health information:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI, service lines):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Care delivery disruption from cyber and technology events | Moderate |
| ER-02 Compromise of protected health information | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of the acquired hospital (H-08) and future acquisitions | Moderate |
| ER-05 Patient safety from technology (devices, clinical systems, downtime, diversion) | Low |
| ER-06 Regulatory, CMS conditions, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Risk level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel, Chief Medical Officer), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Patient-safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the health sector threat picture (ransomware against hospitals, third-party concentration, medical devices) in the SOC's threat intelligence (EV-070), the BIA (P05), the intake evidence, the 2025 risk analysis (EV-029), and risk workshops with the SOC, Clinical Engineering, the Integration Management Office, Revenue Cycle, Emergency Management, the Laboratory, Pharmacy, Third-Party Risk, Digital Health, Data Center Operations and Finance (EV-083). The gap analysis (P03) ran in the same fieldwork window, as is usual for a HIPAA risk analysis, and the two shared findings. The Internal Audit assessment (P07) fed the second pass, and the AI review (P10) updated the AI risks.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: threat intelligence, the SOC case history (EV-022), coverage and configuration exports from the enterprise systems of record, contract and vendor records, the workshops, the gap analysis samples, and, for risks updated in the second pass, the P07 test results. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Any plausible patient harm or forced diversion at more than one hospital is Very High.
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
| Moderate | 38 |
| Low | 16 |
| Very Low | 0 |
| **Total** | **66** |

By threat source type: Adversarial 32, Structural 22, Accidental 11, Environmental 1.
By treatment: Mitigate 55, Accept 10, Avoid 1.
By status: In progress 51, Open 5, Closed (accepted) 10.
**26 risks are outside tolerance**, and each has a dated treatment plan. 26 risks are reported to the board (every High and Very High risk, and every risk outside tolerance).

**Two passes.** Pass 1 was completed on 2026-06-26 from the intake evidence and the May and June fieldwork. Pass 2 followed the Internal Audit assessment (P07): R-056 was added on 2026-08-07 after testing found default vendor passwords on 2 of 16 device integration gateways (EV-IA-5), and the risks that P07 tested were updated with the results (R-012, R-013, R-027, R-030, R-057 and R-058; their `last_reviewed` date is 2026-08-07 and their `likelihood_basis` cites the P07 evidence ID). The AI review (P10) updated R-010, R-035, R-036 and R-038 on 2026-08-14. The `assessment_pass` column shows which pass produced each risk.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low or below | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Care delivery disruption from cyber and technology events | Operational | 14 | 1 | 2 | 6 | 5 | **Very High** | Moderate | 3 |
| ER-02 | Compromise of protected health information | Compliance and reputational | 14 | 0 | 1 | 9 | 4 | **High** | Moderate | 1 |
| ER-03 | Third-party and concentration risk | Operational | 7 | 0 | 3 | 3 | 1 | **High** | Moderate | 3 |
| ER-04 | Integration of the acquired hospital (H-08) and future acquisitions | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-05 | Patient safety from technology (devices, clinical systems, downtime, diversion) | Clinical | 14 | 0 | 3 | 10 | 1 | **High** | Low | 13 |
| ER-06 | Regulatory, CMS conditions, and disclosure compliance | Compliance | 6 | 0 | 0 | 4 | 2 | **Moderate** | Low | 4 |
| ER-07 | Financial reporting integrity and fraud | Financial | 2 | 0 | 0 | 0 | 2 | **Low** | Low | 0 |
| ER-08 | Responsible use of AI | Strategic and clinical | 4 | 0 | 1 | 2 | 1 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (care delivery disruption)** carries the only Very High risk: ransomware across several hospitals with EHR downtime and diversion (R-001). What keeps it Very High is recovery time when both data centers are affected (R-004) and unvaulted service accounts (R-012).
- **ER-05 (patient safety)** has the lowest tolerance and the most risks outside it: diversion decisions without agreed criteria (R-009), unsupported medical devices (R-006), default passwords on device gateways (R-056), and the patient-safety side of downtime (R-043, R-058).
- **ER-06 (regulatory and disclosure)** is outside tolerance because the materiality process has not been rehearsed with hospital incident command (R-015) and because the unified emergency plan does not yet score cyber hazards (R-039).
- **ER-08 (AI)** is outside tolerance because of the sepsis model version 2 (R-010). The other AI risks are Moderate or lower.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts clinical systems across several hospitals, forcing EHR downtime and ambulance diversion | Very High | ER-01 | Isolated recovery environment and 24-hour restore (POAM-003); vault service accounts (POAM-001); H-08 containment (POAM-006); multi-hospital downtime and diversion exercise with the disclosure committee (POAM-004; POAM-005) | CISO | 2027-03-31 |
| R-002 | PHI is exfiltrated during a ransomware attack (double extortion) | High | ER-02 | Egress anomaly models for cloud storage; reduce identified data in analytics sandboxes (R-053) | Director of Security Operations | 2027-03-31 |
| R-003 | Attacker enters through H-08 and reaches enterprise systems over the legacy site VPN | High | ER-04 | Restrict the VPN to named hosts and ports; EDR to 100% at H-08; SD-WAN migration and identity federation before the EHR conversion (POAM-006; POAM-022) | Vice President, Integration Management Office | 2027-03-01 |
| R-004 | After a ransomware event that reaches both data centers, the ECIS cannot be restored within 24 hours | High | ER-01 | Finish the isolated recovery environment; parallel restore streams; retest to 24 hours (POAM-003) | EHR Technical Director | 2027-03-31 |
| R-005 | The primary clearinghouse is down or compromised for weeks and 80% of claims stop | High | ER-03 | Surge contract with the secondary clearinghouse; payer-portal fallback test for the top 12 payers (POAM-019) | Vice President, Revenue Cycle | 2027-01-31 |
| R-006 | Attacker exploits an unsupported operating system on a networked medical device | High | ER-05 | Document deviations and compensating controls for each model; replacement plan with capital funding (POAM-009) | Director of Clinical Engineering | 2027-06-30 |
| R-009 | Hospitals make inconsistent ambulance diversion decisions during an IT outage, overloading neighbors or breaching EMTALA | High | ER-05 | Adopt the BIA diversion triggers at all hospitals with county EMS; add cyber hazards to the unified plan; exercise (POAM-004; POAM-018) | Vice President, Emergency Management | 2026-12-31 |
| R-010 | The sepsis model misses or delays sepsis recognition for some patient groups after its version 2 update | High | ER-08 | Subgroup mitigation and threshold decision after the P10 revalidation; universal screening at all 7 hospitals (POAM-020) | Chief Medical Information Officer | 2026-12-31 |
| R-012 | An attacker uses an unvaulted service account to move laterally and reach EHR databases | High | ER-01 | Vault and rotate all service accounts; retire unused ones (POAM-001) | Director of Identity and Access Management | 2026-12-31 |
| R-019 | A third party with PHI suffers a breach | High | ER-03 | Clear the overdue reassessments; continuous monitoring for tier-1 vendors (POAM-014) | Director of Third-Party Risk Management | 2027-03-31 |
| R-020 | Malicious code arrives in a trusted vendor software update | High | ER-03 | Staged rollout for all tier-1 software; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-056 | Default vendor passwords on clinical device integration gateways let an attacker change device data feeding the EHR | High | ER-05 | Change passwords and vault them; check every gateway quarterly (POAM-010) | Director of Clinical Engineering | 2026-10-31 |

## 6. Themes from the 2026 analysis
1. **Recovery when both data centers are hit (ER-01).** Failover works, but ransomware that reaches the shared directory affects DC-1 and DC-2 together. The 41-hour vault restore and the unfinished isolated recovery environment (R-004; EV-023, EV-024) are the main reason R-001 is Very High.
2. **Diversion and downtime at scale (ER-05).** EMTALA lets a hospital divert ambulances only when it lacks the staff or facilities to accept more emergency patients, and anyone who arrives must still be screened (42 CFR 489.24). Only H-01 has agreed IT-outage criteria, and no exercise has tested several hospitals in downtime at once (R-009, R-018, R-043, R-058; EV-052, EV-089).
3. **H-08 integration (ER-04).** The acquired hospital's flat network, legacy directory, partial EDR, and missing log feeds raise the likelihood of R-001 and R-003 until the 2027-03-01 conversion (EV-007, EV-010, EV-013, EV-021, EV-056).
4. **Medical devices (ER-05).** About 88% of 41,000 networked devices are inventoried and about 2,600 run unsupported operating systems (R-006, R-007; EV-012). Testing found default passwords on 2 device integration gateways (R-056; EV-IA-5), which went into this register as a new risk.
5. **Third parties (ER-03).** Clearinghouse concentration (R-005; EV-041) and 41 overdue vendor reassessments (R-019; EV-038).
6. **AI (ER-08).** The sepsis model's version 2 update went live without local revalidation (R-010; EV-078); P10 measured subgroup gaps and set conditions.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million:** isolated recovery environment and restore automation ($2.6M), H-08 SD-WAN, EDR, encryption, and identity work ahead of conversion ($1.3M), medical device replacement brought forward ($1.9M), device discovery and NAC at H-06 to H-08 ($780K), service account vaulting ($310K), clearinghouse surge contract and fallback test ($220K), sepsis model revalidation and monitoring ($160K), and outside counsel for the joint disclosure tabletop ($45K). Items map to the POA&M in P07.
- **Accepted (10):** R-032, R-033, R-042, R-047, R-050, R-051, R-055, R-059, R-063, R-064. Each is within tolerance with existing controls, accepted at the right level (section 1), and reviewed within 12 months.
- **Avoided (1):** R-037. Unapproved generative AI domains are blocked and an approved enterprise assistant is provided.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-08-24; the board risk committee reviewed it on 2026-09-15.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-15 meeting received this report, the Internal Audit results (P07), and the compliance roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-034), and disclosure controls (R-015). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Quality and patient safety committee (quarterly):** patient-safety technology risks (ER-05) and AI risks (ER-08).
**Management:** the executive risk committee meets monthly and reviews KRIs for every risk outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-08-24.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-08-24.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-15.
- Next full review: May to June 2027, or sooner after a major change (the H-08 conversion), an incident, or an acquisition. KRIs are refreshed quarterly.
