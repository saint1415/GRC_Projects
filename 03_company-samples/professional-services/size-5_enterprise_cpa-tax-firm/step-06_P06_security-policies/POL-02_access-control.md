# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, AC-20, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulations | 16 CFR 314.4(c)(1), (c)(5); 26 CFR 301.7216-2(c)(2); 45 CFR 164.312(a), (d); FAR 52.204-21(b)(1)(i)-(iii), (v), (vi) |

## 1. Purpose
Make sure only authorized people and processes reach the firm's information and systems, only to the extent their engagement or role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company partners, employees, seasonal staff, contractors, and interns in all 64 offices and the 12 processing hubs, and staff of acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, the offshore provider workspace, and systems that service providers operate for the firm, and the services the firm offers to clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-04), PAM, and identity governance |
| Engagement partners and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including seasonal end dates |
| Chief Integration Officer | Brings acquired-firm identities onto the identity platform |
| SL-2 client administrators | Manage their own users under client agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce and client users; service accounts must be vaulted in PAM and have a named owner. (IA-2; AC-2; PR.AA-01)
4.2 Access to client data must be granted by engagement or role, on least privilege, and approved by the engagement partner or system owner. Tax repositories in the DMS must be limited to the engagement team. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person prepare, approve, and release a return for e-file, or create and pay a vendor, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for every individual accessing any firm information system, including client portal users. Workforce users must use phishing-resistant authenticators; any other method needs the Qualified Individual's written approval as an exception. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, immediately for involuntary terminations, and automatically on the recorded end date for seasonal staff and contractors. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 45 days, and client portal accounts inactive for 24 months, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Engagement partners and system owners must certify access quarterly; privileged access and service accounts must be certified quarterly by the system owner. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Remote access must go through the zero-trust access broker with device posture checks. Email and firm applications may be reached only from managed devices or managed apps. (AC-17; AC-20; PR.AA-05)
4.10 Access to tax return information from outside the United States requires prior approval under the travel procedure; it is blocked otherwise. (AC-3; CM-2(7); PR.AA-05)
4.11 Default passwords must be changed before any device or system is connected to a firm network, including printer-scanners. (IA-5; PR.AA-01)
4.12 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, partnership, or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Tax Engagement Platform SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
