# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management (with the Director of OT Security for OT) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(9), AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | 21 CFR 121.135(a), 121.305(f); 9 CFR 417.5(b) |

## 1. Purpose
Make sure only authorized people and processes reach the company's information, plant control systems, and restricted rooms, only to the extent their role requires, and that every change to how food is made can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (employees, agency temporary workers, contractors, and interns) at the 8 plants, 4 distribution centers, headquarters, and regional offices in Florida, Georgia, Alabama, North Carolina, Tennessee, and Texas, including acquired operations from their acquisition date. Covers all IT and OT systems and data, including plant control systems, refrigeration controls, cloud, colocation, SaaS, and systems vendors operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-08) and identity governance |
| Director of OT Security | OT account standard, OT remote access gateway, OT directories |
| Plant controls engineers | Plant OT accounts and quarterly OT access reviews |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including agency workers |
| Vice President, Integration Management Office | Brings PLT-08 identities onto the identity platform |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user must have a unique identity, including on HMIs, SCADA, the central MES, and the food safety records platform. Shared accounts are prohibited except documented view-only operator displays that cannot change setpoints or formulations. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. Write access to PLC logic is limited to named plant controls engineers and named integrator staff during approved sessions. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Formulations and critical setpoints. Changes to cure, brine, cook, and CIP parameters require two people: a recipe author and a different FSQA approver in the MES, and, at the HMI, a supervisor and a second badge from an FSQA technician (enforced from 2027-03-31). (AC-5; CM-5; PR.AA-05)
4.4 MFA is required for all remote access, all cloud and administrative access, the MES, the records platform, and customer portals. Privileged users and formulation approvers must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 OT remote access. Vendors and staff may reach OT only through the enterprise OT remote access gateway, with a named account, MFA, a session approved for a stated purpose and time window, and recording. Always-on VPN accounts and modems are prohibited. (AC-17; MA-4; PR.AA-05)
4.6 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. OT accounts must be removed the same day; any shared OT password the person knew must be rotated until shared accounts are eliminated. (PS-4; AC-2; PR.AA-05)
4.7 Workforce and OT accounts inactive for 60 days, and customer portal accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.8 Managers must certify their staff's IT access every quarter. Plant controls engineers must review OT accounts and vendor access every quarter. (AC-2; PR.AA-05)
4.9 Privileged access must be granted just in time through PAM or the OT gateway, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.10 Default passwords must be changed before any device or system is connected, including refrigeration controllers, inspection systems, sensors, and gateways. The commissioning checklist must record the change. (IA-5; CM-6; PR.AA-01)
4.11 The identity platform locks accounts after 10 failed sign-ins. HMIs must not lock out operators, because lockout during a process upset is a safety risk; HMIs must instead use badge sign-in and revert to view-only after 10 minutes without input. (AC-7; AC-11; PR.AA-03)
4.12 Physical access. Badge access is required at every site. Cure and ingredient rooms, server rooms, engine rooms, and the PLT-07 plant-based room are restricted to named roles. Visitors must sign in and be escorted in production areas. (PE-2; PE-3; PR.AA-06)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 OT Account and HMI Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 OT Vendor Session Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, OT monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.9), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPCM SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the PLT-07 food defense plan and the plant HACCP plans.
