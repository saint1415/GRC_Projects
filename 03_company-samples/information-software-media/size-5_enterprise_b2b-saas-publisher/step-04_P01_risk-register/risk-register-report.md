# Enterprise Risk Register Report: Cris Santos Company | Information | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher; about 9,800 business customers; Operations Cloud, Data Cloud, Conversational AI service, Government Edition) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Information |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | The Reg S-K Item 106(b)(1) description of processes for assessing, identifying, and managing material cybersecurity risks; the CCPA cybersecurity audit (first audit period 2027); the risk assessment step in the SOC 2 reports (CC3.2) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the cybersecurity and risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that hold customer data or support tier-1 processes: the Operations Cloud production platform (SYS-01), the Data Cloud (SYS-02), the Government Edition (SYS-03), the identity platform (SYS-04), the software factory (SYS-05), security operations (SYS-06), corporate SaaS and ERP (SYS-07), about 14,500 endpoints (SYS-08), the acquired AQ-01 platform (SYS-09), about 1,450 vendors including 58 sub-processors (SYS-10), and the AI portfolio (SYS-11). Business processes and impact values come from the enterprise BIA (P05). The OCP is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and engineering (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Customer trust and tenant isolation:** very low appetite for any exposure of one customer's data to another party, and for public statements that do not match practice.
- **Regulatory, contractual, and disclosure:** very low appetite for missed notices or inaccurate SEC disclosure.
- **Service availability:** low appetite for outages that breach customer SLAs.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Service availability and resilience | Moderate |
| ER-02 Compromise of customer data | Moderate |
| ER-03 Third-party and supply chain | Moderate |
| ER-04 Integration of acquired companies | Moderate |
| ER-05 Product security and tenant isolation | Low |
| ER-06 Regulatory, contractual, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CTO, CIO, CISO, General Counsel, Chief Privacy Officer), reported to the board's cybersecurity and risk committee |
| Very High | CEO and CFO jointly, reported to the cybersecurity and risk committee at its next meeting |

Risks under ER-05 (product security and tenant isolation) or ER-06 (regulatory, contractual, and disclosure) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the SaaS threat picture (credential and token theft, software supply chain, tenant isolation failures, cloud provider and DNS outages), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Because one failure can reach thousands of customers, any event that could expose many tenants is rated Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board's cybersecurity and risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 27 |
| Low | 24 |
| **Total** | **64** |

By threat source type: Adversarial 24, Structural 26, Accidental 11, Environmental 3.
By treatment: Mitigate 55, Accept 7, Avoid 2.
By status: In progress 35, Open 21, Closed (accepted) 7, Closed (avoided) 1.
**25 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Service availability and resilience | Operational | 11 | 0 | 2 | 4 | 5 | **High** | Moderate | 2 |
| ER-02 | Compromise of customer data | Compliance and reputational | 9 | 1 | 1 | 2 | 5 | **Very High** | Moderate | 2 |
| ER-03 | Third-party and supply chain | Operational | 4 | 0 | 1 | 2 | 1 | **High** | Moderate | 1 |
| ER-04 | Integration of acquired companies | Strategic | 6 | 0 | 3 | 3 | 0 | **High** | Moderate | 3 |
| ER-05 | Product security and tenant isolation | Operational | 10 | 0 | 2 | 4 | 4 | **High** | Low | 6 |
| ER-06 | Regulatory, contractual, and disclosure compliance | Compliance | 13 | 0 | 2 | 7 | 4 | **High** | Low | 9 |
| ER-07 | Financial reporting integrity and fraud | Financial | 3 | 0 | 0 | 1 | 2 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI | Strategic | 8 | 0 | 1 | 4 | 3 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-02 (customer data)** carries the only Very High risk: credential compromise reaching many tenants (R-001). Long-lived keys, live secrets in repositories, and the AQ-01 export path are the reasons its likelihood is not lower.
- **ER-04 (acquisition integration)** has 3 High risks, all from AQ-01: the leaked-key path to the shared export (R-002, the P08 scenario), the pivot path into the OCP (R-003), and the public build logs Internal Audit found (R-058).
- **ER-05 (product security and tenant isolation)** has the lowest tolerance with ER-06 and ER-07; 6 of its risks are outside tolerance, led by tenant isolation defects (R-005) and secrets in repositories (R-007).
- **ER-06 (regulatory, contractual, and disclosure)** has the most risks outside tolerance (9): untrue trust page statements (R-020), the materiality process (R-017), customer notice terms (R-018), the bank service provider notice (R-019), retention against the deletion commitment (R-022, R-023), the CCPA cybersecurity audit (R-024), the Government Edition POA&M (R-025), and protected health information placed in free-text fields against the terms (R-043).
- **ER-08 (AI)** is outside tolerance because AQ-01 still trains on pooled customer transcripts (R-021).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Attacker uses stolen cloud or pipeline credentials to read customer data across many tenants | Very High | ER-02 | Remove long-lived keys and revoke live secrets (POAM-002); bulk-read and export detections (POAM-003); minimize and re-scope the AQ-01 export (POAM-001); annual exercise with the disclosure committee (2026-11-12) | CISO | 2027-01-31 |
| R-002 | A leaked AQ-01 CI access key is used through the cross-account role to copy the shared export of Operations Cloud transcripts | High | ER-04 | Scope the role to one prefix per customer and minimize exports (POAM-001); remove AQ-01 static keys and federate (POAM-002); onboard AQ-01 logs (POAM-003); guardrails for AQ-01 (POAM-019) | Vice President, Integration Management Office | 2026-12-15 |
| R-003 | Attacker moves from the AQ-01 cloud organization into the OCP through the integration path | High | ER-04 | Interconnection agreement and API scope review (POAM-001); AQ-01 migration into the landing zone by 2027-03-31 | Vice President, Integration Management Office | 2027-03-31 |
| R-004 | A support or operations engineer opens a customer tenant without need and views or exports data | High | ER-02 | Retire the legacy console path; require a ticket link; customer approval by default for Enterprise tenants; behavioral analytics (POAM-004) | Vice President, Customer Support | 2027-01-31 |
| R-005 | A software defect in tenant isolation exposes one customer's data to another customer | High | ER-05 | Make isolation tests a merge gate for every new service (2026-12-31); fuzzing of tenant routing (2027-03-31) | Vice President, Platform Engineering | 2027-03-31 |
| R-007 | Secrets committed to source repositories are found and used by an attacker | High | ER-05 | Automated revocation within 24 hours of detection; push protection on all repositories including AQ-01 (POAM-002) | Director of Product Security | 2027-01-31 |
| R-009 | Ransomware or a destructive attack on corporate systems spreads to production through engineer endpoints | High | ER-01 | Annual destructive-attack exercise; isolate engineer workstations for production access (privileged access workstations) by 2027-06-30 | CISO | 2027-06-30 |
| R-012 | A malicious open-source package reaches production builds | High | ER-03 | Package age and reputation gate in the registry proxy (2027-03-31) | Director of Product Security | 2027-03-31 |
| R-016 | An outage at the single managed DNS provider makes every product unreachable | High | ER-01 | Add a secondary DNS provider and test failover (2027-03-31); add to the contingency plan (POAM-017) | Director of Cloud Platform Engineering | 2027-03-31 |
| R-017 | A material incident is disclosed late or inaccurately because the materiality process fails under pressure | High | ER-06 | Update the playbook and brief new members; full tabletop 2026-11-12 (POAM-012) | General Counsel | 2026-11-30 |
| R-020 | Trust page statements on support access and recording are untrue, creating deception exposure | High | ER-06 | Correct the trust page now; restore only when true (POAM-021); quarterly statement review | General Counsel | 2026-10-30 |
| R-021 | AQ-01 uses shared customers' transcripts to improve its models, contrary to the company's no-cross-customer-training statement | High | ER-08 | Stop pooled training on customer transcripts; retrain or delete affected models; align terms and notify customers (POAM-020) | Chief Data and AI Officer | 2026-11-30 |
| R-058 | Secrets in publicly readable AQ-01 CI build logs are harvested | High | ER-04 | Apply landing zone guardrails to the AQ-01 organization; scan all AQ-01 storage (POAM-019) | Vice President, Integration Management Office | 2026-11-15 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** AQ-01 runs outside the landing zone with static keys, unfederated identities, logs outside the SIEM, and a broad cross-account role over the shared export. Internal Audit found its CI build logs publicly readable, one with a live key (R-058). Treatment: minimize the export, guardrails, key removal, federation, and log onboarding, all due by 2027-03-31. Going forward, deal approvals must include security diligence and integration funding (R-061).
2. **Credentials and secrets (ER-02, ER-05).** Non-human identities and long-lived keys are now the main path to customer data (R-001, R-007, R-030). Treatment: short-lived workload credentials everywhere and automatic revocation of found secrets.
3. **Support access and public statements (ER-02, ER-06).** The tenant access tool works as designed for restricted tenants, but the trust page promises more than the tool delivers for everyone else (R-004, R-020). The statement is corrected first; the tool follows.
4. **Commitments the company cannot yet prove (ER-06).** Deletion within 90 days (R-022, R-023), 24-hour and 48-hour notices (R-018), and the bank service provider notice (R-019) all depend on processes that were never reconciled against the contracts.
5. **AI (ER-08).** AI Assist is generally available to about 2,300 customers; prompt injection (R-026) and AQ-01's pooled training (R-021) are the main issues; the portfolio is reviewed in P10.
6. **Resilience (ER-01).** 13 of 14 cells meet the RTO; Cell 4 does not (R-008). The single DNS provider (R-016) is now the largest availability exposure.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $9.4 million:** AQ-01 landing zone migration and identity federation ($2.6M), non-human identity and secrets program ($1.8M), tenant access tool rebuild and behavioral analytics ($1.2M), Cell 4 split and restore automation ($1.1M), secondary DNS provider ($0.4M), CCPA cybersecurity audit readiness and external auditor ($0.9M), contract obligations register ($0.5M), AI Assist prompt-injection hardening ($0.6M), and outside counsel for the disclosure tabletop ($0.3M). Items map to the POA&M in P07.
- **Accepted (7):** R-038, R-039, R-047, R-052, R-057, R-060, R-063. Each is Low residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-046, R-053. Unapproved generative AI domains are blocked, and guardrails block copies of production snapshots to non-production accounts.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the cybersecurity and risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Cybersecurity and risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032, R-063), and disclosure controls topics (R-017, R-034). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Cybersecurity and risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
