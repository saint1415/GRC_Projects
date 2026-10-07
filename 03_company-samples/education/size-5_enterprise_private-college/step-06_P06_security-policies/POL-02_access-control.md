# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after material changes, incidents, or new service lines |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, IA-11, IA-12, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Key regulatory requirements | 16 CFR 314.4(c)(1), (c)(5); 34 CFR 99.31(a)(1)(ii); 34 CFR 668.16(c)(2) |

## 1. Purpose
Make sure only authorized people and processes reach the company's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed. This policy is how the company uses "reasonable methods" so that school officials reach only education records in which they have a legitimate educational interest (34 CFR 99.31(a)(1)(ii)).

## 2. Scope
All Cris Santos Company workforce members (employees, including full-time and adjunct faculty, contractors, student workers, and volunteers) at headquarters, the 23 campuses, and the 4 student support centers, and all remote workers in any state. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors and the Title IV third-party servicer operate for the company, and the services the company offers to other organizations (SL-1 Workforce Education Services and SL-2 Online Program Services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05) and identity governance |
| Data owners (University Registrar; Vice President, Financial Aid; Vice President, Student Finance) | Approve roles that reach their data |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including adjunct contract ends |
| SL-1 employer administrators and SL-2 partner administrators | Manage their own users under their agreements and attest quarterly |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce, partner, employer, and vendor users, including file transfer accounts; service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the data owner before it is granted. Access to education records must be limited to records in which the user has a legitimate educational interest. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No role may both authorize Title IV payments and disburse funds for the same student, and the person who enters a grade must not approve a change to that grade after it is posted. (AC-5; PR.AA-05)
4.4 MFA is required for any individual accessing any information system that holds customer information, including workforce, vendors, SL-1 employer users, and students. Privileged users must use phishing-resistant authenticators. Any alternative requires the Qualified Individual's written approval of equivalent or stronger controls. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Changes to refund bank details must require re-authentication with MFA and out-of-band confirmation, and new bank details must be held 72 hours before the first payment. (IA-11; SI-4; PR.AA-03)
4.6 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. An adjunct contract that ends without a renewal is a termination. (PS-4; AC-2; PR.AA-05)
4.7 Workforce accounts inactive for 60 days, and partner, employer, and student-worker accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.8 Managers must certify their staff's access every quarter; SL-1 employer administrators and SL-2 partner administrators must attest to their users every quarter. (AC-2; PR.AA-05)
4.9 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.10 MFA resets and account recovery must be completed only after verified identity proofing under PRC-02.5 (video verification with manager approval for workforce; documented proofing for students), and each reset must alert the SOC. (IA-5; IA-12; PR.AA-02)
4.11 Default passwords must be changed before any device or system, including printers and scanners, is connected to the network. (IA-5; CM-6; PR.AA-01)
4.12 Vendor and remote maintenance access must go through the zero-trust or PAM gateway with approval and session recording. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification and Partner Attestation Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Identity Verification for MFA Reset and Account Recovery Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the Qualified Individual's annual report to the board. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SRLP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
