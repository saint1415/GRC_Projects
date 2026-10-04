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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Key regulatory drivers | FAR 52.204-21(b)(1)(i), (ii), (v), (vi); SP 800-171 R2 3.1 and 3.5 (FSCE) |

## 1. Purpose
Make sure only authorized people, devices, and processes reach the company's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary workers supplied by staffing agencies, contractors, and interns) at headquarters, the 6 distribution centers, the 15 sales offices, and remote locations, including AQ-1 and any future acquisition from its closing date. Covers all systems and data, including cloud, colocation, SaaS, distribution-center OT, the FSCE, and systems that vendors, carriers, 3PLs, and drop-ship partners operate for the company, and the services offered to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-07) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including staffing agency rosters |
| Vice President, Integration Management Office | Brings AQ-1 identities onto the identity platform |
| Reseller administrators (SL-1) | Manage their own users under the platform terms |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user, service, and device must have a unique identity. Shared accounts are prohibited, including shared kiosk and handheld accounts in distribution centers; service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person create and pay a vendor, change prices and enter orders, or set and release credit must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all administrative and cloud access, all workforce access to the OCFP, and all reseller platform users. Privileged users and finance, credit, and pricing roles must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as an employee termination, and within 1 business day of a staffing agency's separation notice, with daily reconciliation of agency rosters. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days, and reseller platform users inactive for 120 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; reseller administrators must attest to their users each year. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access, including OT vendors, must go through the zero-trust or PAM gateway with approval and session recording. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 API credentials for reseller and partner integrations must be short-lived, bound to the client, and rotated at least every 90 days. (IA-5; PR.AA-03)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote, Vendor, and API Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC Program Office's internal assessments for the FSCE. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCFP SSP; FSCE CMMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
