# Risk Register Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company: about 520 sites in 38 states and DC; 12,000 internal employees; about 78,000 associates on assignment a week) |
| Size tier | Enterprise |
| Vertical | Administrative and Support and Waste Management and Remediation Services (NAICS 561320) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | The "reasonable measures" duty of state data security laws (Florida worked example: Fla. Stat. 501.171(2)); the Form I-9 records security program (8 CFR 274a.2(g)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |
| Register | `risk-register.csv` (64 risks) |

## 1. Scope and risk framing
**Scope.** All systems that hold associate, candidate, client, or pay data or support tier-1 processes across the four segments, about 520 sites, the two cloud estates and two colocation data centers, ACQ-1 and ACQ-2, and the roughly 1,400 vendors (220 with personal information). Business processes and impact values come from the enterprise BIA (P05). The Associate Lifecycle and Payroll Platform (ALPP) is also covered at system level in the SSP (P02).

**What is different about a staffing firm.** Most of the people whose data the firm holds are not its customers: they are applicants and temporary associates, and the firm is their employer. The firm moves about $65 million to them every Friday. So the two dominant risk families are **pay** (fraud and missed payroll) and **identity records** (SSNs, Form I-9 documents, bank accounts, consumer reports), not intellectual property or customer accounts.

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Associate pay:** very low appetite for associates not being paid correctly and on time, whatever the cause.
- **Regulatory and disclosure:** very low appetite for noncompliance with employment eligibility, FCRA, federal contract, state privacy, or SEC disclosure rules.
- **Personal information:** low appetite for unauthorized disclosure of worker and candidate data.
- **Client service continuity:** low appetite for disruption of managed-program and payrolling services.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision, and AI in hiring is reviewed before use.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Payroll and operations disruption from cyber and technology events | Moderate |
| ER-02 Compromise of worker and candidate personal information | Moderate |
| ER-03 Payroll integrity and payment fraud | Low |
| ER-04 Third-party, client integration, and concentration risk | Moderate |
| ER-05 Integration of acquired firms | Moderate |
| ER-06 Regulatory and disclosure compliance (employment eligibility, FCRA, SEC, contracts) | Low |
| ER-07 Patient and worker safety from staffing technology | Low |
| ER-08 Responsible use of AI in hiring | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (segment president or functional head) |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board's risk and technology committee |
| Very High | CEO and CFO jointly, reported to the board's risk and technology committee at its next meeting |

Payroll integrity risks (ER-03) and patient-safety risks (ER-07) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the staffing sector threat picture (payroll diversion, help desk social engineering, fraudulent remote candidates, data theft and extortion), the BIA (P05), the gap analysis (P03), the Internal Audit assessment (P07), and the firm's 2025 fraud loss data.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board's risk and technology committee sees each quarter.

**Worked example (R-001).** Associate account takeover for payroll diversion: likelihood of initiation **Very High** (it happened 214 times in 2025) and likelihood of adverse impact **High** (once an account is taken over, nothing stops the bank change) give an overall likelihood of **Very High** (Table G-5). Impact is **High**: one coordinated campaign against a single payroll could divert millions, harm thousands of associates, and draw regulators and media. Table I-2 gives **High**.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 33 |
| Low | 19 |
| **Total** | **64** |

By threat source type: Adversarial 30, Structural 25, Accidental 8, Environmental 1.
By treatment: Mitigate 54, Accept 8, Avoid 2.
By status: In progress 33, Open 21, Closed (accepted) 8, Closed (avoided) 2.
**22 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Payroll and operations disruption from cyber and technology events | Operational | 11 | 1 | 1 | 5 | 4 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of worker and candidate personal information | Compliance and reputational | 11 | 0 | 1 | 7 | 3 | **High** | Moderate | 1 |
| ER-03 | Payroll integrity and payment fraud | Financial | 10 | 0 | 4 | 5 | 1 | **High** | Low | 9 |
| ER-04 | Third-party, client integration, and concentration risk | Operational | 10 | 0 | 1 | 5 | 4 | **High** | Moderate | 1 |
| ER-05 | Integration of acquired firms | Strategic | 4 | 0 | 1 | 2 | 1 | **High** | Moderate | 1 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 9 | 0 | 1 | 4 | 4 | **High** | Low | 5 |
| ER-07 | Patient and worker safety from staffing technology | Operational (safety) | 3 | 0 | 1 | 1 | 1 | **High** | Low | 2 |
| ER-08 | Responsible use of AI in hiring | Strategic and compliance | 6 | 0 | 1 | 4 | 1 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (disruption)** carries the only Very High risk: ransomware during the payroll window (R-002). The unproven payroll engine RTO (R-005) and the ACQ-1 pathway (R-004) are the main reasons its likelihood is not lower.
- **ER-03 (payroll integrity and fraud)** has the most risks outside tolerance (9 of 10), because the board set a Low tolerance and four High risks sit there: associate account takeover (R-001), Associate Service Center social engineering (R-013), pay rule changes without independent approval (R-018), and unverified pay files (R-019). These are the firm's highest-frequency losses, and they share one root cause: money moves on the strength of a weak identity check or a single approver.
- **ER-02 (personal information)** is driven by mass exfiltration (R-003). Its exposure would drop to Moderate once the data platform extract is tokenized (POAM-004).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised with the current disclosure committee (R-010).
- **ER-08 (AI)** is High because the AI ranking tool is monitored for bias only on vendor data (R-009). It will fall to Moderate once firm-data monitoring starts (POAM-014).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Ransomware encrypts the payroll engine and integration platform during the payroll window, and a weekly payroll is missed | Very High | ER-01 | Payroll RTO fix (POAM-010); ACQ-1 containment (POAM-002, POAM-003); ransomware exercise with the disclosure committee (POAM-013) | CISO | 2027-01-31 |
| R-001 | Fraud ring takes over associate app accounts and changes direct deposit accounts | High | ER-03 | Passkeys or app push; out-of-band confirmation and 3-day hold for first bank change; anomaly scoring (POAM-001) | Senior Vice President, Payroll and Associate Services | 2027-01-31 |
| R-003 | Attacker exfiltrates SSNs and bank account numbers for millions of people | High | ER-02 | Tokenize the extract and mask columns (POAM-004); bulk export detection (POAM-016); retention purge (POAM-005) | Chief Data Officer | 2027-03-31 |
| R-004 | Attacker enters through ACQ-1's legacy environment | High | ER-05 | SIEM feeds (POAM-003); federation (POAM-002); migration 2027-03-31 | Vice President, Integration Management Office | 2027-03-31 |
| R-007 | A client VMS integration key or shared account is stolen | High | ER-04 | Per-client credentials, rotation, anomaly alerts (POAM-008) | Vice President, Payroll Technology | 2027-03-31 |
| R-009 | AI ranking screens out qualified applicants from a protected group | High | ER-08 | Firm-data bias monitoring; council reviews (POAM-014) | Chief Data Officer | 2027-01-31 |
| R-010 | A material incident is disclosed late or inaccurately | High | ER-06 | Playbook update with a cost model; tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| R-013 | Associate Service Center agents are socially engineered into bank changes | High | ER-03 | App-based caller verification; no bank changes by phone (POAM-018) | Vice President, Associate Service Center | 2026-12-31 |
| R-018 | A pay rule change without independent approval causes systemic pay errors or diversion | High | ER-03 | Role split; system-enforced second approver (POAM-015) | Vice President, Payroll Technology | 2026-12-31 |
| R-019 | A bank or paycard file is altered between approval and transmission | High | ER-03 | Hash at generation, verify before transmission, auto-hold (POAM-019) | Treasurer | 2026-12-31 |
| R-023 | Help desk social engineering resets a payroll administrator's MFA; data export and bank changes follow | High | ER-01 | Video verification for privileged resets; alert on reset followed by export (P08 runbook) | Director of Identity and Access Management | 2026-12-31 |
| R-034 | A clinician with a lapsed license works a shift because ACQ-1 credential data is stale | High | ER-07 | Daily expiry check against the verification service until migration | President, Healthcare Staffing | 2026-12-31 |

## 6. Themes from the 2026 analysis
1. **Money moves on weak identity (ER-03).** Associates sign in with SMS codes (R-001), agents verify callers with data criminals already hold (R-013), help desk resets rely on knowable facts (R-023), and smishing imitates the firm's own texts (R-062). Treatment: phishing-resistant sign-in for associates, out-of-band confirmation of every first bank change, and no bank changes by phone. Expected effect: an 80% fall in fraudulent changes within two quarters.
2. **One approver, one file (ER-03).** Pay rules can be changed and released by the same person (R-018), and pay files are not hash-verified after approval (R-019). Both are cheap to fix and are due by 2026-12-31.
3. **Copies of the crown jewels (ER-02).** The payroll engine tokenizes SSNs and bank numbers, but the nightly extract to the data platform does not (R-003, R-048), and nothing is purged (R-020).
4. **Acquisitions (ER-05).** ACQ-1 is the least controlled environment connected to the firm (R-004, R-057, R-058) and the source of the stale credential risk (R-034). Future deals need security due diligence and integration funding before signing (R-061).
5. **AI in hiring (ER-08).** Federal disparate impact enforcement has receded (see P10), but NYC Local Law 144 is in force, Colorado's ADMT law applies to decisions from 2027-01-01, and private Title VII claims remain. Treatment centers on firm-data bias monitoring and the council reviews (R-009, R-041, R-043).
6. **New finding from the control assessment.** Internal Audit found the vendor default administrator PIN on 9 of 25 sampled on-site time clocks (P07). It is now R-060 and POAM-024.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $4.9 million:** associate app passkeys and bank-change verification ($1.3M), data platform tokenization and masking ($850K), client integration credential redesign ($700K), ACQ-1 SIEM onboarding and federation ($600K), payroll engine standby automation ($240K per year), cloud time clock service ($520K), pay file hashing ($90K), kiosk network moves ($310K), Associate Service Center verification redesign ($180K), AI bias monitoring ($260K), and outside counsel for the disclosure tabletop and Colorado design ($75K). Items map to the POA&M in P07.
- **Accepted (8):** R-028, R-030, R-036, R-038, R-039, R-047, R-050, R-063. Each is Low residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-040 and R-044. Unapproved generative AI domains are blocked, and the candidate chatbot no longer asks free-text screening questions.
- **Very High risk R-002:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend (including fraudulent bank changes per payroll), risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and the disclosure controls topics (R-010, R-055). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
