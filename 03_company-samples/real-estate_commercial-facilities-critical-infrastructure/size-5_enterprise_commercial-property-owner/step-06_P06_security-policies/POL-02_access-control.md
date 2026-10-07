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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, MA-4, PE-2, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory drivers | CPG 2.0 goals 1.E, 3.A-3.H (R05); 11 CCR 7123(c)(1) and (c)(3) (R03) |

## 1. Purpose
Make sure only authorized people and processes reach company information, building systems, and buildings, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and TRS staff) at all 140 operated properties in Florida, Texas, Georgia, North Carolina, Arizona, and California, including acquired properties from their acquisition date. Covers all systems and data: IT, OT (building automation, access control, video), cloud, colocation, SaaS, systems that integrators and other vendors operate for the company, and the services the TRS offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05) and identity governance |
| Director of OT Security | Runs the OT remote access gateway; sets OT account rules (STD-02.4) |
| Vice President, Corporate Security | Owns tenant credentials and access control platform roles |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief engineers | Approve integrator sessions; keep local OT accounts until migrated |
| Tenant administrators | Request and attest to their staff credentials under the lease |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce members, integrators, contractors, and guard contractor viewers; device and service credentials must be vaulted. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person both approve and issue a credential, or both create and pay a vendor, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all administrative and cloud access, the OT remote access gateway, and the access control platform console. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations, including local OT accounts and security console accounts. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days must be disabled automatically, and tenant credentials unused for 90 days must be suspended automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter, including OT and access control platform administrator roles; tenant administrators must attest to their credential holders every quarter. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. Full administrator roles on the access control platform must not exceed the number approved in STD-02.1. (AC-6; AC-6(9); PR.AA-05)
4.9 All vendor and remote access to OT systems must go through the OT remote access gateway with named accounts, MFA, per-session approval by the chief engineer on duty, and session recording. Always-on vendor remote-support tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device or system is connected to any network. (IA-5; PR.AA-01)
4.11 Two sealed break-glass accounts per critical administration plane must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)
4.12 Tenant credentials must be issued only at the request of the tenant's designated administrator, and phone requests to issue credentials or unlock doors must be verified by call-back to a number on file. (PE-2; IA-4; PR.AA-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 OT Account and Remote Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Tenant Credential Lifecycle Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 BAACS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
