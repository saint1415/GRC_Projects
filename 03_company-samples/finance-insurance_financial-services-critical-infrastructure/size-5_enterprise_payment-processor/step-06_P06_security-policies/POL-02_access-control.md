# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, under 23 NYCRR 500.2(d)) |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, new sponsor banks, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IA-2, IA-5, AC-2, AC-3, AC-6, AC-5, IA-2(1), IA-2(2), PS-4, PS-7, AC-2(3), AC-6(9), AC-17, MA-4, IA-8 |
| CSF 2.0 | PR.AA-01, PR.AA-05, PR.AA-03 |
| Regulatory drivers | See `policy-control-map.csv` (one driver per statement) |

## 1. Purpose
Make sure only authorized people and processes reach the company's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in every location, and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d). Covers all systems and data, including Cloud A, Cloud B, DC-1, DC-2, SaaS, and systems that service providers operate for the company, and the services the company provides to merchants, ISV partners, and sponsor Banks A, B, and C.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-07), PAM, and identity governance |
| Managers, system owners, and vendor managers | Approve access; complete quarterly certifications; record contractor end dates |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Merchant and partner administrators | Manage their own users' accounts under their agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared interactive accounts are prohibited; system and application account credentials must be vaulted in PAM and must never be stored in scripts, configuration files, or source code. (IA-2; IA-5; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No one may both create and release a merchant funding file; developers must not have write access to production; cryptographic key operations must use dual control and split knowledge. (AC-5; PR.AA-05)
4.4 MFA is required for any individual accessing any company information system. Privileged users must use phishing-resistant authenticators. Any alternative must be approved in writing by the CISO through the exception process and reviewed at least annually. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Access must be disabled the same business day as a termination (immediately for involuntary terminations), and contractor accounts must be disabled automatically at the contract end date recorded by the vendor manager. (PS-4; PS-7; AC-2; PR.AA-05)
4.6 User accounts inactive for 90 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Owners must certify access to CDE systems every quarter, and application and system accounts at least every six months. (AC-2; AC-6; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and monitored. Standing administrator rights are prohibited for people and for pipeline or service identities. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access must go through PAM with approval and session recording, and must be enabled only for the approved window. (AC-17; MA-4; PR.AA-05)
4.10 Merchant and partner users must use MFA for administrator, refund, funding account, payout destination, and virtual terminal roles; all other customer sign-ins must be analyzed for risk dynamically. (IA-8; PR.AA-03)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 Merchant and Partner Authentication Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the PCI DSS quarterly reviews (PCI DSS 12.4.2), access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Core Payment Processing Platform SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
