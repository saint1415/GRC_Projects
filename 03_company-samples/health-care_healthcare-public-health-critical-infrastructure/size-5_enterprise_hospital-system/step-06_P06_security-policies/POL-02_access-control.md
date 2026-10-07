# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-08-24 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, IA-1, MA-1, PS-1, SC-1, IA-2, AC-2, IA-5, AC-3, AC-6, AC-5, IA-2(1), IA-2(2), IA-8, PS-4, PS-7, AC-2(3), AC-6(9), AC-17, MA-4, SC-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-10, GV.RR-04, DE.CM-06, PR.DS-01 |
| HIPAA Security Rule and other drivers | 164.308(a)(3)(ii)(C); 164.308(a)(4); 164.308(a)(4)(ii)(B); 164.308(a)(4)(ii)(C); 164.308(a)(5)(ii)(D); 164.308(b)(1); 164.312(a)(2)(i); 164.312(a)(2)(ii); 164.312(d); 164.312(e)(1); see `policy-control-map.csv` for each statement's driver |

## 1. Purpose
Make sure only authorized people and processes reach the system's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed, including for agency staff, affiliate practices, and vendors.

## 2. Scope
All Cris Santos Company workforce members (employees, medical staff, agency and contracted staff, students, and volunteers) at the 8 hospitals, 3 freestanding emergency departments, 46 clinics, 4 imaging centers, the data centers, and corporate offices in Florida, Georgia, and Alabama, including H-08 and any future acquisition from its closing date. Covers all systems and data, including the data centers, both clouds, SaaS, medical devices, building OT, systems that vendors operate for the system, and the services sold to other organizations (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-02) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events for employees |
| Chief Nursing Officer | Agency and contracted nursing staff start and end dates |
| Vice President, Integration Management Office | Brings H-08 identities onto the identity platform |
| Practice administrators (SL-1) | Manage their own staff's affiliate accounts under hosting agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce and affiliate users; service accounts must be vaulted in PAM with automatic credential rotation. (IA-2; AC-2; IA-5; PR.AA-01; PR.AA-03; PR.AA-05)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-01; PR.AA-05; PR.DS-10)
4.3 Duties that could let one person build and migrate clinical content (order sets, drug database, decision support rules), or administer security and also perform clinical work, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all cloud and administrative access, and all affiliate access; on site, badge tap must be paired with a PIN. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-01; PR.AA-03)
4.5 Access must be disabled the same business day as a termination and immediately for involuntary terminations. Agency and contracted staff accounts must carry an end date and be disabled at the end of the last shift. (PS-4; PS-7; AC-2; GV.RR-04; DE.CM-06; PR.AA-01)
4.6 Workforce accounts inactive for 60 days, and affiliate accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-01; PR.AA-05)
4.7 Managers must certify their staff's access every quarter; SL-1 practice administrators must attest to their users quarterly. (AC-2; PR.AA-01; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access, including medical device and analyzer vendors, must go through the zero-trust gateway or PAM with approval and session recording. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device, gateway, or system is connected to a hospital network, and checked quarterly on medical device gateways. (IA-5; PR.AA-01; PR.AA-03)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Security Officer. (AC-2; PR.AA-01; PR.AA-05)
4.12 Records with extra legal protection, including Part 2 records from the H-03 program, must carry a sensitive-record flag that limits access; break-the-glass access requires a reason and is reviewed by the Privacy Office. (AC-3; SC-4; PR.AA-05; PR.DS-10; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Agency Staff Access Reconciliation Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the emergency preparedness program's exercises. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, contract, or privileges, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ECIS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the unified emergency preparedness plan.
