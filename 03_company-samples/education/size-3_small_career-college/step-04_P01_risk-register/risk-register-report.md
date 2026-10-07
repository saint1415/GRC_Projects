# Risk Register Report: Cris Santos Company | Educational Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college, about 900 students) |
| Size tier | Small (60 employees) |
| Vertical | Educational Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | FTC Safeguards Rule written risk assessment, 16 CFR 314.4(b)(1), and the periodic reassessment in 314.4(b)(2) |
| Prepared | 2026-07-17 by the IT Director (Qualified Individual); R-007 added 2026-07-31 |
| Approved | 2026-08-21 by the Campus President (Moderate and below) and the Board chair (High) |

## 1. Scope and risk framing
**Scope.** The Student Information and Financial Aid Platform (SIFAP) defined in the SSP (P02), the systems connected to it (LMS, admissions CRM, email, lab computers), the contracted financial aid servicer, and the business processes in the BIA (P05). See `../00_company-facts.md` section 3.

**What is being protected.** Two overlapping kinds of information:
- **Customer information** under the Safeguards Rule (16 CFR 314.2(d)): information obtained in providing a financial service to a student, such as Title IV aid administration. The college holds it for about 6,400 consumers.
- **Education records** under FERPA (34 CFR Part 99) for about 900 current and many former students.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Director may accept.
- Moderate: the Campus President may accept, with a treatment plan or a documented reason.
- High and Very High: only the Board chair may accept, and only temporarily with a dated treatment plan. Risks that could put Title IV eligibility at stake are not accepted at High.

The last risk assessment was dated June 2024. This one replaces it and meets the 314.4(b)(1) content requirements: criteria for rating risks (section 2), criteria for assessing confidentiality, integrity, and availability and the adequacy of existing controls (the `existing_controls` and rating columns), and how each risk will be mitigated or accepted (the treatment columns).

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Director of Financial Aid, Registrar, Business Office Manager, Dean of Academic Affairs, and Lab Coordinator, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, regulatory, student harm, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 19 |
| Low | 10 |
| **Total** | **33** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts endpoints and cloud workloads | High | Managed EDR with 24x7 alerting; phishing exercises; immutable backups | IT Director | 2027-01-31 |
| R-002 | Exfiltration of financial aid and education records (double extortion) | High | Remove standing exports; encrypt required exports; outbound transfer alerting | IT Director | 2026-12-31 |
| R-004 | Takeover of a servicer administrator account on the student-facing aid portal (no MFA) | High | Contract amendment requiring MFA or federation | Director of Financial Aid | 2026-10-31 |
| R-019 | Backups destroyed along with production | High | Separate-account immutable backups; quarterly restore tests | IT Director | 2026-12-31 |
| R-011 | Intrusion through a valid account goes undetected | Moderate | Weekly sign-in review; monthly SIS and FAMS export review | IT Director | 2026-10-31 |
| R-014 | GLBA audit finding puts administrative capability in question | Moderate | This assessment; first written report to the Board on 2026-10-15 | Campus President | 2026-10-15 |
| R-013 | Missed FTC, FSA, or Florida notice deadlines | Moderate | Written incident response plan and P08 runbook | IT Director | 2026-10-31 |

The four High risks share one theme: **student financial aid data is easy to reach and hard to recover.** Unencrypted exports sit on a file server (R-002), a vendor's administrators can reach the aid portal with a password alone (R-004), there is no detection capability (R-001), and the backups would not survive an attack (R-019). Closing these also reduces six related Moderate risks (R-003, R-009, R-011, R-012, R-013, R-032).

R-007 was added on 2026-07-31 after control assessment testing (P07) found 11 active LMS accounts belonging to former adjunct faculty.

## 4. Treatment summary
- **Funded (2026-27 budget, $61,000):**
  - Managed endpoint detection and response with 24x7 alerting ($26,000 a year)
  - Backup redesign in a separate account and region ($5,000 a year)
  - First external penetration test and a scanning tool ($14,000)
  - Badge reader and rekey for the records room ($4,000)
  - Identity verification service for online applicants ($12,000 a year)
- **Accepted:**
  - R-027: Low, staff can work remotely during an outage
  - R-028: Low, vendor-managed
  - R-029: Low, full-disk encryption on every staff laptop
- **Avoided:** R-021, by keeping the CRM applicant-scoring feature turned off until P10 approves it.
- **Contract actions:** MFA amendment for the financial aid servicer (R-004) by 2026-10-31; SOC 2 report requests to the SIS, LMS, and FAMS vendors (R-009), completed for the SIS and LMS vendors in P09.

## 5. Approval
- Campus President: approved Moderate and Low treatments and acceptances, 2026-08-21.
- Board chair (majority owner): approved the High-risk treatment plans and the budget, 2026-08-21. The results will be part of the Qualified Individual's first written report to the Board of Managers on 2026-10-15 (16 CFR 314.4(i)).
- Next full review: July 2027, or sooner after a material change (314.4(b)(2), (g)) or a security event.
