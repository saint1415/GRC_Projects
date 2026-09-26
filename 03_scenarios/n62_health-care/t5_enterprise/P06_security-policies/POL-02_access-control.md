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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |

## 1. Purpose
Make sure only authorized people and processes reach the group's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, providers, contractors, students, and volunteers) at all 159 sites in Florida, Georgia, Alabama, and South Carolina, including acquired practices from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, medical devices, and systems that business associates and other vendors operate for the group, and the services the group offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-02) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Integration Management Office | Brings acquired-practice identities onto the identity platform |
| Client administrators (SL-1, SL-2) | Manage their own staff's accounts under client agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce and client users; device service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could allow one person to change and release clinical results, or to create and pay a vendor, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all access to systems holding ePHI, all cloud and administrative access, and all client portal access. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days, and client portal accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; client administrators must attest to their users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access, including medical device vendors, must go through the zero-trust or PAM gateway with approval and session recording. Always-on vendor tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device or system is connected to the network. (IA-5; PR.AA-01)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Security Officer. (AC-2; PR.AA-05)

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
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 LIS SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
