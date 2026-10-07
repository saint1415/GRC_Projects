# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, AC-20, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Binding requirements served | FAR 52.204-21(b)(1)(i), (ii), (v), (vi); utility addenda secs. 3 and 6 (CIP-013-2 R1.2.3, R1.2.6 flow-down) |

## 1. Purpose
Make sure only authorized people, processes, and devices reach the company's information, plant control systems, and customer-facing services, only to the extent their role requires, and that access ends promptly, including the notice owed to utilities when a field representative's access should end.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 7 plants, 9 service centers, 3 spare yards, and offices in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, including the acquired Ohio plant (AQ-01) from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant control systems (OT), test systems, and systems that suppliers operate for the company, and the products and services the company supplies to utilities (TMU firmware and configuration software, the Fleet Monitoring Service, and the Spare Transformer Reserve Service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-02) and identity governance |
| Director of OT Security | Runs the OT remote access gateway and OT credential standards |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Spares and Services | Access-revocation notices to utilities for field technicians |
| Supplier administrators | Manage their own staff's portal accounts under supplier agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce and supplier users. Where an OT device supports only shared logins, an approved exception with compensating controls is required. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that would let one person both change and release production master data or schedules, both create and pay a supplier, or both build and approve signing of firmware must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all privileged and cloud access, all ERP access, and all supplier portal access. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. For field technicians, the utility access-revocation notice task must be created the same day. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days, and supplier portal accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access to tier-1 systems every quarter; supplier administrators must attest to their users annually. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 OEM and vendor remote access to plant systems must go only through the OT remote access gateway with per-session approval, MFA, and recording. Always-on modems, cellular routers, and vendor-installed remote tools are prohibited. (AC-17; MA-4; PR.AA-03)
4.10 Default passwords must be changed before any device or system is connected to a network, including the web configuration interfaces of OT devices. (IA-5; PR.AA-01)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)
4.12 At customer sites, company representatives must use only the utility's own access methods and must not save utility credentials on company devices. (AC-17; AC-20; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard (including the OT remote access gateway)
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Utility Access-Revocation Notice Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EPSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
