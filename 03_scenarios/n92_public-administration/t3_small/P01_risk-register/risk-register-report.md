# Risk Register Report: Cris Santos Company | Public Administration | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator) |
| Size tier | Small (60 employees) |
| Vertical | Public Administration |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | SP 800-53 RA-3 (contract requirement); the risk assessment inputs agencies expect under Pub. 1075 and CJISSECPOL RA-3 |
| Prepared | 2026-07-24 by the IT Manager (Information Security Officer); R-011 added 2026-08-07 |
| Approved | 2026-08-31 by the Chief Operating Officer (Moderate and below) and the Chief Executive Officer (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Agency Case Management Platform (ACMP) and the business processes in the BIA (P05). That covers the production tenant, the integration gateway, non-production environments, backups, logging, the AI eligibility assistant pilot, and the SaaS services and endpoints that administer them (`../scenario-facts.md` section 3). It also covers the contract risk of failing the agencies' security terms, because for this company a failed CJIS or IRS review can end a contract as surely as an outage can.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the Chief Operating Officer may accept, with a treatment plan or a documented reason.
- High and Very High: only the Chief Executive Officer may accept, and only temporarily with a dated treatment plan. A risk that would breach a CJIS Security Addendum or Pub. 1075 Exhibit 7 term may not be accepted at all; it must be treated or the regulated data removed.

This is the company's first documented risk assessment since the platform launched in 2023.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the gap analysis (P03), the BIA (P05), interviews with the Cloud Operations Lead, Customer Support Manager, Director of Engineering, and Data and AI Lead, and the agency contract terms.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact, and the two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Impact on agencies and the people in their records counts, not only impact on the company.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 5 |
| Moderate | 19 |
| Low | 7 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through a stolen cloud administrator session encrypts databases and deletes backups | Very High | Immutable separate-account backups; just-in-time admin access; 24x7 detection | Cloud Operations Lead | 2026-12-31 |
| R-002 | Theft of FTI and CJI followed by extortion | High | Egress allow-list; transfer alerting; 7-year logs | Cloud Operations Lead | 2027-01-31 |
| R-004 | Agency or IRS review finds unscreened staff with CJI or FTI access | High | Remove access until screened; screening gate | HR Manager | 2026-10-31 |
| R-005 | FTI and CJI disclosed to the unapproved ticketing vendor | High | Avoid: block attachments, purge, secure in-platform support | Contracts and Compliance Manager | 2026-10-15 |
| R-007 | Backups cannot be restored within the 8-hour contract recovery time | High | Contingency plan; quarterly timed restore tests | Cloud Operations Lead | 2027-03-31 |
| R-012 | Compromised pipeline or dependency inserts malicious code | High | Image signing and verification; pipeline hardening | Director of Engineering | 2027-03-31 |

The Very High and High risks share two themes:
- **The platform could not survive a determined attacker who reaches a cloud administrator account** (R-001, R-002, R-007). Administrators have standing rights, backups sit where those rights can delete them, and nobody watches after hours.
- **The company is out of step with the agency terms that let it hold CJI and FTI at all** (R-004, R-005). These are contract and legal risks: the Security Addendum and Exhibit 7 give the agencies the right to end the contract.

Fixing the first theme also lowers R-009, R-016, and R-024. Fixing the second also lowers R-003, R-006, and R-021.

R-011 was added on 2026-08-07 after control assessment testing (P07) found the AC-02 interface key in plain text in a pipeline variable.

## 4. Treatment summary
- **Funded (FY2027 security budget, $186,000):**
  - Managed detection and response with 24x7 coverage ($62,000 per year)
  - Backup redesign with immutable copies in a second U.S. region ($14,000 per year)
  - Seven-year write-once log archive ($9,000 per year)
  - SOC 2 Type 1 examination for P09 ($48,000)
  - Just-in-time access and secrets management tooling ($18,000 per year)
  - Authenticated vulnerability scanning and container runtime protection ($21,000 per year)
  - Fingerprinting, background investigation, and training fees for designated staff ($4,000)
  - Staff time and a contingency reserve ($10,000)
- **Accepted:**
  - R-023: Low, encryption and remote wipe (COO)
  - R-026: Moderate, existing guardrails (COO)
  - R-027: Low, remote work covers loss of the office (COO)
  - R-028: Low, provider DDoS protection (COO)
- **Avoided:** R-005, by stopping regulated data from reaching the ticketing vendor.
- **Agency disclosures:** the 2025 staging copy (R-006) and the ticket exposure (R-005) go to the AC-01 disclosure officer and the AC-02 local agency security officer by 2026-09-15, so each agency can decide on its own reporting duties.

## 5. Approval
- Chief Operating Officer: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Chief Executive Officer: approved the Very High and High treatment plans and the FY2027 budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, an incident, or a new CJISSECPOL version.
