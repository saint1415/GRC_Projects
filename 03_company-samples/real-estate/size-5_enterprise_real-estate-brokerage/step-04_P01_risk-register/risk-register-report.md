# Enterprise Risk Register Report: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage with title and settlement, property management, and relocation lines; about 410 sales offices and 140 closing offices in 9 states) |
| Size tier | Enterprise (12,000 employees; about 38,000 contractor agents) |
| Vertical | Real Estate and Rental and Leasing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Title and Escrow's written risk assessment (16 CFR 314.4(b)(1)) and periodic reassessment (314.4(b)(2)); input to the Reg S-K Item 106(b) description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All four business lines (brokerage, title and settlement, property management, relocation), the two cloud estates and two colocation data centers, about 550 offices, the acquired firms AQ-06 to AQ-09, the 38,000 contractor agents who use company systems from their own devices, and the roughly 1,400 vendors (230 with customer information or other personal data). Business processes and impact values come from the enterprise BIA (P05). The TMCC is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Client funds:** very low appetite for loss or diversion of funds the company holds or disburses for clients.
- **Regulatory and disclosure:** very low appetite for noncompliance with the Safeguards Rule, state escrow and licensing rules, fair housing law, or SEC disclosure rules.
- **Closing continuity:** low appetite for disruption of closings and disbursements.
- **Customer and consumer information:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Fraud and diversion of client funds | Low |
| ER-02 Compromise of customer and consumer information | Moderate |
| ER-03 Disruption of closings and transactions | Moderate |
| ER-04 Third-party and platform concentration | Moderate |
| ER-05 Integration of acquired firms | Moderate |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Contractor agent identity and conduct | Moderate |
| ER-08 Responsible use of AI and fair housing | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive; for Title and Escrow risks, the President of Title and Escrow as the senior overseer of the Qualified Individual |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel, President of Title and Escrow), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Client-funds risks (ER-01) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the real estate threat picture (BEC and wire fraud against closings, seller impersonation, platform concentration), the BIA (P05), the gap analysis (P03), the Internal Audit assessment (P07), and the company's own incident history (3 diverted wires in 2026 H1).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 37 |
| Low | 13 |
| **Total** | **64** |

By threat source type: Adversarial 30, Structural 24, Accidental 9, Environmental 1.
By treatment: Mitigate 58, Accept 5, Avoid 1.
By status: In progress 50, Open 9, Closed (accepted) 5.
**25 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Fraud and diversion of client funds | Financial and fiduciary | 12 | 1 | 3 | 7 | 1 | **Very High** | Low | 11 |
| ER-02 | Compromise of customer and consumer information | Compliance and reputational | 9 | 0 | 2 | 4 | 3 | **High** | Moderate | 2 |
| ER-03 | Disruption of closings and transactions | Operational | 9 | 0 | 1 | 6 | 2 | **High** | Moderate | 1 |
| ER-04 | Third-party and platform concentration | Operational | 8 | 0 | 2 | 5 | 1 | **High** | Moderate | 2 |
| ER-05 | Integration of acquired firms | Strategic | 4 | 0 | 1 | 3 | 0 | **High** | Moderate | 1 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 9 | 0 | 1 | 4 | 4 | **High** | Low | 5 |
| ER-07 | Contractor agent identity and conduct | Operational | 6 | 0 | 2 | 3 | 1 | **High** | Moderate | 2 |
| ER-08 | Responsible use of AI and fair housing | Strategic and compliance | 7 | 0 | 1 | 5 | 1 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (client funds)** carries the only Very High risk, a coordinated BEC campaign that diverts closing funds (R-001). Because the tolerance is Low, almost every funds risk is outside tolerance. The three treatments that move it most are phishing-resistant MFA for agents (POAM-001), payee verification coverage (POAM-006), and closing the AQ-09 single-approver gap (POAM-005).
- **ER-07 (contractor agents)** feeds ER-01: relay phishing against agents (R-053) and slow agent offboarding (R-012) are how attackers reach transaction threads.
- **ER-04 (concentration)** has two High risks for the two vendor platforms (R-033, R-034). They cannot be engineered away; the treatment is contract terms and a tested fallback.
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the materiality playbook has no fraud-loss scenario and no method for a series of related incidents (R-044).
- **ER-08 (AI and fair housing)** is outside tolerance for one risk: tenant screening ADMT in California and Colorado needs notices, an appeal path, and records before 2027-01-01 (R-059).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Coordinated business email compromise campaign takes over agent and closer mailboxes and diverts closing funds with altered wire instructions across several transactions | Very High | ER-01 | Phishing-resistant MFA and session binding for agents (POAM-001); payee verification to 98% and independent callback numbers (POAM-006); legacy tenant migration (POAM-004); fraud-loss materiality scenario and tabletop (POAM-008) | CISO | 2027-03-31 |
| R-002 | Spoofed payoff letter or altered payee bank details redirect a loan payoff or seller proceeds | High | ER-01 | Independent-source callback numbers enforced in the Hub; expand verification to non-portal lenders and exchange accommodators (POAM-006) | President, Title and Escrow | 2027-03-31 |
| R-004 | Funds are diverted at AQ-09, where wires below $100,000 need one approver and payee accounts are not verified | High | ER-01 | Bank-enforced dual approval on all AQ-09 wires by 2026-10-31; migration into SYS-02 and the Disbursement Hub (POAM-005) | President, Title and Escrow | 2027-02-28 |
| R-005 | BEC through the legacy email tenants at AQ-06 to AQ-08 goes undetected because they lack the enterprise email security stack and SIEM feeds | High | ER-05 | SIEM connectors and forwarding-rule alerts (POAM-003); migration to the enterprise tenant (POAM-004) | Chief Information Officer | 2027-03-31 |
| R-011 | Bank API client secrets are misused to submit payment files outside the Disbursement Hub | High | ER-01 | Rotate and vault the secrets; pipeline guardrail against secrets in variables (POAM-010) | Director of Closing Platform Engineering | 2026-10-31 |
| R-012 | Departed contractor agents keep access to SYS-01, email, and client files for days after leaving | High | ER-07 | Daily feed from agent services and state license status into identity governance (POAM-002) | Executive Vice President, Brokerage Operations | 2027-01-31 |
| R-013 | Attackers mass-download closing documents (identity documents, bank statements, Social Security numbers) from compromised agent or closer accounts | High | ER-02 | Download limits in SYS-01; session binding (POAM-001) | Director of Security Operations | 2027-03-31 |
| R-014 | Ransomware with data theft hits the colocation file servers holding 610,000 legacy scanned closing files | High | ER-02 | Retention review, disposal, and migration of the rest to an encrypted archive (POAM-013) | Chief Privacy Officer | 2027-06-30 |
| R-024 | Ransomware encrypts enterprise systems and stops closings and transactions in several states | High | ER-03 | Close the Disbursement Hub RTO gap (POAM-011); ransomware tabletop each year | CISO | 2027-01-31 |
| R-033 | A transaction management platform outage longer than 24 hours stops brokerage transactions in all 9 states | High | ER-04 | Contract amendment for an 8-hour RTO; tested company fallback with daily exports (POAM-007) | Chief Operating Officer | 2027-04-30 |
| R-034 | A title production platform outage or compromise stops about 91% of closings | High | ER-04 | Annual joint recovery exercise with the vendor | President, Title and Escrow | 2027-04-30 |
| R-044 | Material BEC losses, or a series of related incidents, are disclosed late or inaccurately because the materiality playbook covers ransomware only | High | ER-06 | Add fraud-loss and related-incident criteria; tabletop on 2026-11-17 (POAM-008) | General Counsel | 2026-11-30 |
| R-053 | Relay phishing kits defeat contractor agents' push MFA | High | ER-07 | Device-bound passkeys for agents (POAM-001) | Director of Identity and Access Management | 2027-03-31 |
| R-059 | Tenant screening ADMT is used in California and Colorado after 2027-01-01 without the required notices, appeal, and records | High | ER-08 | Notices, human appeal, and record keeping before 2027-01-01 (POAM-021) | President, Property Management | 2026-12-15 |

## 6. Themes from the 2026 analysis
1. **Funds diversion is the dominant risk (ER-01).** Attackers do not need to break the company's platforms; they need one mailbox in a transaction thread and one payee that is not verified. The defenses that matter are the ones on that path: no instructions outside the Hub, payee verification, dual approval, and phishing-resistant sign-in for the people in the thread.
2. **Contractor agents are most of the user base (ER-07).** 38,000 agents use their own devices, change brokerages often (about 9,100 departures a year), and authenticate with relayable push MFA. Their accounts are the most common entry point in the 2026 incidents.
3. **Acquisitions (ER-05).** AQ-06 to AQ-08 run legacy email tenants without enterprise detection (R-005), and AQ-09 disburses from its own trust accounts with a single approver below $100,000 (R-004). Going forward, deal approvals must include a security sign-off and integration budget (R-042).
4. **Platform concentration (ER-04).** One vendor platform carries every brokerage transaction with a contract RTO three times the BIA RTO (R-033).
5. **AI and fair housing (ER-08).** 12 AI use cases, 7 reviewed; tenant screening bias testing uses vendor data only (R-058, R-061). New state ADMT rules apply from 2027-01-01 (R-059).
6. **Disclosure (ER-06).** A BEC campaign produces many small losses rather than one outage. The disclosure committee has no method yet for deciding when a series of related occurrences becomes material (R-044).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million:** agent passkey rollout and session binding ($2.1M), legacy tenant migration ($1.6M), payee verification expansion ($0.9M per year), AQ-09 migration into SYS-02 ($1.2M), Disbursement Hub recovery automation ($0.3M), legacy file review and archive migration ($0.6M), tenant screening ADMT compliance and bias testing ($0.4M), transaction platform contract amendment and fallback tooling ($0.25M), and outside counsel for the disclosure tabletop ($0.05M). Items map to the POA&M in P07.
- **Accepted (5):** R-020, R-028, R-030, R-039, R-051. Each is Low residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-022. Unapproved generative AI tools are blocked; only the approved enterprise assistant is allowed.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-052), and disclosure controls topics (R-044, R-046). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Title and Escrow board of managers (annually):** the Qualified Individual's written report under 16 CFR 314.4(i), delivered 2026-09-15, uses this register for the risk assessment and risk management decisions it must cover.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
