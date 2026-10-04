# Enterprise Risk Register Report: Cris Santos Company | Educational Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company; one private, for-profit college with 23 campuses in six states and an online division serving all 50 states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Educational Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | The written risk assessment in the FTC Safeguards Rule (16 CFR 314.4(b)(1)), including criteria for evaluating risks, criteria for assessing confidentiality, integrity, and availability, and how risks will be mitigated or accepted; input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO (Qualified Individual); updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the board risk committee, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that create, receive, maintain, or transmit customer information (16 CFR 314.2) or education records, or that support tier-1 processes, across the 23 campuses, 4 student support centers, headquarters, two cloud estates, one colocation data center, about 1,100 vendors (260 with student data), and the two service lines (SL-1 and SL-2). Business processes and impact values come from the enterprise BIA (P05). The Student Records and Learning Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Title IV eligibility:** very low appetite for anything that could impair administrative capability or Title IV participation.
- **Students' money and identity:** very low appetite for fraud against students or Title IV funds.
- **Regulatory and disclosure:** very low appetite for noncompliance with the Safeguards Rule, FERPA, state law, or SEC disclosure rules.
- **Instruction continuity:** low appetite for disruption of online or campus instruction during a session.
- **Student data:** low appetite for unauthorized disclosure of education records or customer information.
- **Growth and innovation (new programs, partners, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of instruction and student services from cyber and technology events | Moderate |
| ER-02 Compromise of student and financial aid data | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Title IV eligibility and administrative capability | Low |
| ER-05 Fraud against students and Title IV funds | Low |
| ER-06 Regulatory and disclosure compliance (SEC, FERPA, state law) | Low |
| ER-07 Financial reporting integrity | Low |
| ER-08 Responsible use of AI and student data | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, Chief Operating Officer, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Risks to Title IV eligibility (ER-04) or fraud against students (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the education sector threat picture (ransomware against colleges, refund fraud, synthetic-identity enrollment), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter, and it is the risk section of the Qualified Individual's annual written report (16 CFR 314.4(i)(2)).

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 14 |
| Moderate | 34 |
| Low | 17 |
| **Total** | **66** |

By threat source type: Adversarial 31, Structural 25, Accidental 8, Environmental 2.
By treatment: Mitigate 52, Accept 12, Avoid 2.
By status: In progress 44, Open 10, Closed (accepted) 12.
**24 risks are outside tolerance** and each has a dated treatment plan. All 24 are reported to the board risk committee.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of instruction and student services from cyber and technology events | Operational | 14 | 1 | 3 | 6 | 4 | **Very High** | Moderate | 4 |
| ER-02 | Compromise of student and financial aid data | Compliance and reputational | 14 | 0 | 4 | 7 | 3 | **High** | Moderate | 4 |
| ER-03 | Third-party and concentration risk | Operational | 10 | 0 | 2 | 6 | 2 | **High** | Moderate | 2 |
| ER-04 | Title IV eligibility and administrative capability | Compliance (Title IV) | 6 | 0 | 1 | 4 | 1 | **High** | Low | 5 |
| ER-05 | Fraud against students and Title IV funds | Financial | 4 | 0 | 2 | 1 | 1 | **High** | Low | 3 |
| ER-06 | Regulatory and disclosure compliance (SEC, FERPA, state law) | Compliance | 9 | 0 | 1 | 3 | 5 | **High** | Low | 4 |
| ER-07 | Financial reporting integrity | Financial | 2 | 0 | 0 | 1 | 1 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI and student data | Strategic | 7 | 0 | 1 | 6 | 0 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (instruction and services)** carries the only Very High risk, enterprise ransomware (R-001). The legacy imaging system (R-007), the help desk MFA reset path (R-004), and the unproven SIS recovery time (R-010) are the main reasons its likelihood and impact are not lower.
- **ER-04 (Title IV)** has the lowest tolerance and the most risks outside it (5 of 6). The driver is FAFSA-derived data in the analytics platform (R-008), which FSA could cite in a compliance audit, plus the SAIG server and change control findings (R-019, R-024).
- **ER-05 (fraud)** has two High risks that hit students and Title IV funds directly: refund redirection through student account takeover (R-003) and synthetic-identity enrollment (R-006).
- **ER-08 (AI)** is outside tolerance only because of the admissions scoring model (R-014). Colorado SB26-189 and the California ADMT rules make this more pressing from 2027-01-01 (P10).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts the SIS, integration services, and campus systems across the enterprise | Very High | ER-01 | Retire the imaging system (POAM-008); prove the SIS RTO (POAM-006); verified MFA resets (POAM-013); ransomware exercise with the disclosure committee (POAM-011) | CISO | 2027-01-31 |
| R-002 | Exfiltration of student records and customer information during a ransomware attack | High | ER-02 | Bulk-export detection (POAM-015); remove ISIR-derived fields from analytics (POAM-004); disposal (POAM-010) | Director of Security Operations | 2027-03-31 |
| R-003 | Student account takeover redirects Title IV credit balance refunds | High | ER-05 | Required student MFA; step-up MFA and out-of-band confirmation for bank changes; 72-hour hold (POAM-002) | Vice President, Student Finance | 2026-12-15 |
| R-004 | Help desk social engineering resets MFA for a workforce or adjunct account | High | ER-02 | Video identity verification with manager approval (POAM-013) | Director of Identity and Access Management | 2026-12-31 |
| R-006 | Synthetic identities enroll in online programs to obtain Title IV funds | High | ER-05 | Identity verification before first disbursement; shared fraud signals (POAM-023) | Vice President, Enrollment | 2027-03-31 |
| R-007 | Attacker exploits the unsupported imaging system | High | ER-02 | Migrate and retire (POAM-008); interim log forwarding (POAM-009) | CIO | 2027-06-30 |
| R-008 | FAFSA-derived ISIR fields used outside aid administration | High | ER-04 | Remove fields, purge copies, register uses (POAM-004) | Chief Data and Analytics Officer | 2026-11-30 |
| R-010 | SIS recovery exceeds the 8-hour RTO | High | ER-01 | Automate rebuild of integration and SAIG servers; retest (POAM-006) | Vice President, Enterprise Applications | 2027-01-31 |
| R-011 | LMS vendor outage longer than the BIA RTO | High | ER-03 | Contract RTO of 8 hours; observed failover test; weekly course packets (POAM-007) | Provost and Chief Academic Officer | 2027-03-31 |
| R-012 | A third party holding student data is breached | High | ER-03 | Complete reviews; amend legacy contracts (POAM-005) | Director of Third-Party Risk Management | 2027-03-31 |
| R-013 | Material incident disclosed late or Title IV consequences missed | High | ER-06 | Update the playbook; tabletop 2026-11-12 (POAM-011) | General Counsel | 2026-11-30 |
| R-014 | Admissions scoring model deprioritizes applicants through proxies | High | ER-08 | Local fairness test; applicant notice; human review rule (POAM-019; P10) | Vice President, Enrollment | 2026-12-15 |
| R-021 | Default passwords on financial aid processing scanners | High | ER-02 | Passwords changed 2026-08-13; CMDB; baseline (POAM-012) | Director of Endpoint Engineering | 2026-10-31 |
| R-040 | A privileged cloud administrator account is compromised | High | ER-01 | PAM session analytics (SI-4(20)) | Director of Cloud Platform Engineering | 2027-03-31 |
| R-048 | Zero-day in an internet-facing edge device is exploited | High | ER-01 | Retire legacy VPN concentrators; emergency patch SLA 72 hours | Director of Network Engineering | 2027-01-31 |

## 6. Themes from the 2026 analysis
1. **Identity at the edges (ER-02, ER-05).** The workforce core is strong (SSO, MFA, PAM, quarterly certification), but the edges are not: adjunct accounts stay active between terms (R-005), the help desk can reset MFA on weak proof (R-004), students are not required to use MFA (R-003, R-034), and scanners kept default passwords (R-021). Treatment: student MFA and bank-change controls by 2026-12-15, verified resets and adjunct automation by 2026-12-31.
2. **Title IV data and eligibility (ER-04).** FAFSA-derived ISIR fields have spread into the analytics platform and models (R-008, R-051). This is the single finding most likely to appear in an FSA compliance audit. Treatment: remove and purge by 2026-11-30.
3. **Fraud (ER-05).** Refund redirection cost about $0.9 million in 2025-26, and synthetic-identity applications target the online programs (R-003, R-006). Treatment combines identity controls with fraud referral to the Department's Office of Inspector General (34 CFR 668.16(g)).
4. **Concentration (ER-03, ER-01).** One LMS carries all online instruction for the College and 14 partners with a 24-hour contract RTO (R-011), and the SIS recovered in 11.5 hours against 8 (R-010).
5. **Legacy (ER-02).** The imaging system holds about 14 million aid documents on an unsupported operating system with no SIEM logs (R-007, R-054). Testing also found default passwords on scanners that feed it (R-021).
6. **AI (ER-08).** 16 use cases; 10 reviewed. The admissions scoring model was enabled inside the CRM before review (R-014). The AI writing-detection score was switched off for misconduct decisions (R-043, treatment Avoid).
7. **Materiality and disclosure (ER-06).** The playbook omits Title IV consequences and has not been exercised with the current disclosure committee (R-013). A full tabletop is set for 2026-11-12.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.0 million:** imaging migration and retirement ($2.1M), student MFA and refund fraud controls ($1.3M), identity verification for first-time online students ($0.9M), legacy VPN retirement ($0.8M), SIS DR automation ($0.6M), SIEM log onboarding and detection content ($0.4M), vendor reviews and contract amendments ($0.35M), AI fairness testing and state law readiness ($0.3M), help desk video verification ($0.25M), and outside counsel for the disclosure tabletop ($40K). Items map to the POA&M in P07.
- **Accepted (12):** R-026, R-027, R-032, R-036, R-046, R-047, R-049, R-050, R-057, R-058, R-059, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041, R-043. Unapproved generative AI domains are blocked, and AI writing-detection scores may not be used in misconduct decisions.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Board risk committee (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03) as the **Qualified Individual's annual written report** under 16 CFR 314.4(i): overall status of the information security program and compliance with Part 314, and material matters (risk assessment, risk management and control decisions, service provider arrangements, testing results, security events, and recommended changes). The full board was briefed on 2026-09-24.
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and disclosure controls (R-013, R-063). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Board risk committee: reviewed the enterprise risk profile and received the Qualified Individual's annual report, 2026-09-10.
- Next full review: June to July 2027, or sooner after a material change (16 CFR 314.4(b)(2)), incident, new service line, or acquisition. KRIs are refreshed quarterly.
