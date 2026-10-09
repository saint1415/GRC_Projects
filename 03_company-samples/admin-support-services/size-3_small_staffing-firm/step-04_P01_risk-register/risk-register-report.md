# Risk Register Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm, NAICS 561320) |
| Size tier | Small (60 internal staff; about 450 temporary associates on assignment in an average week) |
| Vertical | Administrative and Support and Waste Management and Remediation Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | "Reasonable measures" under Fla. Stat. 501.171(2); the records security program for electronic Forms I-9 (8 CFR 274a.2(g)); NIST CSF 2.0 ID.RA (P03 benchmark) |
| Prepared | 2026-07-24 by the IT Manager (Information Security Lead) with the HR and Compliance Manager |
| Approved | 2026-08-31 by the COO (Moderate and below) and the President (High) |

## 1. Scope and risk framing
**Scope.** The Associate Payroll and Applicant Tracking Platform (APATP) and the business processes in the BIA (P05). That covers every system that holds candidate, associate, and client data at headquarters and the 3 other branches, plus the vendors that hold that data for the firm ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**What the firm is protecting.** About 31,000 current and former associate records with SSNs and bank accounts, about 1,500 consumer reports a year, Form I-9 records and document images, and a weekly payroll of about $270,000.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan. Risks that would stop associates from being paid on time are not acceptable at High.

This is the firm's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, the BIA, the intake evidence, and interviews with the Payroll Manager, HR and Compliance Manager, Director of Recruiting, and two Branch Managers (EV-052). The gap analysis (P03) ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the ticket history (EV-028), configuration exports, contracts, walk-throughs and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables with a script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 21 |
| Low | 11 |
| **Total** | **35** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Payroll platform account takeover; associate register exported and pay diverted | High | SSO with number-matching MFA on the payroll platform; export and bank-change alerts | Payroll Manager | 2026-11-30 |
| R-005 | Bulk theft of SSNs and bank accounts from the reporting database | High | Stop copying full SSNs and bank accounts; restrict access to 3 report builders | IT Manager | 2026-11-30 |
| R-004 | Backups lost along with production, including the scanned Form I-9 archive | High | Immutable, separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-002 | Fraudulent direct deposit change | Moderate | Call-back verification and a 1-payroll hold on new accounts | Payroll Manager | 2026-10-31 |
| R-013 | AI screening tool disadvantages a protected group | Moderate | Sort-only mode; bias testing and monitoring (P10) | Director of Recruiting | 2026-10-15 |
| R-010 | Background check disclosure is not a standalone document | Moderate | Counsel-reviewed disclosure-only form | HR and Compliance Manager | 2026-09-30 |

The three High risks share one theme: **the firm holds a large store of worker identity and bank data in places that are easy to reach and hard to recover.** The payroll platform has the weakest sign-in of any system (R-001), a reporting copy holds far more SSNs than any report needs (R-005), and backups would not survive an attacker with cloud admin rights (R-004). Fixing these also reduces five related Moderate risks (R-002, R-003, R-009, R-017, R-035).

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-034 was added on 2026-08-07 after testing found that a departed Onboarding Specialist's E-Verify login had been used by a colleague after the departure date (EV-IA-2, EV-IA-5). The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $54,000):**
  - Payroll platform SSO tier and alerting ($7,000 per year)
  - 24x7 EDR monitoring upgrade with the managed IT provider ($11,000 per year)
  - Backup redesign ($6,000 per year in cloud cost)
  - Kiosk and guest network separation at 4 offices ($5,000)
  - Phishing exercises and payroll fraud training ($3,000 per year)
  - Independent statistical review of the AI screening tool ($9,000; P10)
  - Outside counsel review of the FCRA disclosure, E-Verify practices, and breach notice templates ($8,000)
  - Certified device destruction and records purge project ($5,000)
- **Accepted (Low, by the COO):** R-027, R-028, R-029, R-030.
- **Contract actions:** AI vendor data use addendum (R-025, 2026-10-31); timekeeping and screening provider security terms (R-023, R-024, 2027-03-31); ATS data-return clause (R-009, 2027-03-31).

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-08-31.
- President: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, placing workers outside Florida or turning the AI tool back to auto-advance) or an incident.
