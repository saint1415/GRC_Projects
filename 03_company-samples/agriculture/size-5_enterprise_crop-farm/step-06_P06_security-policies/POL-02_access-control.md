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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, AC-19, IA-1, IA-2, IA-2(1), IA-3, IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, DE.CM-06 |
| Regulatory and guidance drivers | CSF 2.0 (benchmark); SP 800-82 Rev. 3 6.2.1 and 6.2.10; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1) |

## 1. Purpose
Make sure only authorized people, devices, and processes reach the company's information, systems, and OT, only to the extent their role requires, that every record and command can be tied to the person who made it, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (year-round employees, seasonal and H-2A workers, contractors, and integrator and vendor staff working on company systems) at the 48 farms, 17 packing sites, 6 irrigation control centers, offices, and both data center campuses in Florida, Georgia, South Carolina, and North Carolina, including acquired operations from their acquisition date. Covers all systems and data, including cloud, data centers, SaaS, operational technology (irrigation, fertigation and chemigation, packing, cold-chain, and drying controls), drones and equipment telematics, systems that vendors operate for the company, and the services offered to external growers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-03) and identity governance |
| Director of OT Security | Runs the OT remote access gateway and OT vendor sessions |
| Managers and system owners | Approve access; complete quarterly certifications |
| Irrigation Control Center Managers | Approve each integrator session and each OT role in their region |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including the seasonal hiring roster |
| Vice President, Integration Management Office | Brings acquired-operation identities onto the identity platform |
| Grower administrators (SL-1, SL-2) | Manage their own staff's accounts under client agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 Every user, device, and service must have a unique identity. Shared accounts are prohibited for workforce, crew leads, and grower users; HMI operator stations use individual badge and PIN logins; device and service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person both create and release a fertigation or chemigation recipe, both change and download PLC logic, or both create and pay a vendor must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all cloud and administrative access, all access to the FMIS and payroll, and all grower portal access. Privileged users and engineers must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. Seasonal accounts must expire at the contract end date and be disabled within 1 business day of an early departure. (PS-4; AC-2; PR.AA-05)
4.6 Year-round accounts inactive for 60 days and seasonal accounts inactive for 14 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; control center managers must certify SCADA and integrator accounts every quarter; grower administrators must attest to their users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. PLC downloads must originate only from engineering workstations reached through PAM. (AC-6; CM-5(1); PR.AA-05)
4.9 All vendor and remote access to OT, including irrigation integrators, packing line vendors, and equipment dealers, must go through the OT remote access gateway or the zero-trust gateway with per-session approval, MFA, and session recording. Always-on vendor tools and vendor-run cloud control services outside the gateway are prohibited. (AC-17; MA-4; DE.CM-06)
4.10 Default passwords and keys must be changed before any device (including HMIs, PLCs, LoRaWAN gateways, and pivot modems) is connected to a company network. (IA-5; PR.AA-01)
4.11 Field devices must authenticate to company networks with device credentials (SIM credentials on the APN, device keys on LoRaWAN), and mobile devices used for tally or irrigation must be enrolled in mobile device management. (IA-3; AC-19; PR.AA-01)
4.12 Two sealed break-glass accounts per critical platform, including the SCADA masters, must exist, be tested quarterly, and have every use reviewed by the CISO. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard (including seasonal accounts)
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Privileged Access Standard
- STD-02.4 Remote and OT Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure (including the seasonal hiring roster)
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 OT Vendor Session Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and OT change and session reviews. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Vendor violations are handled under the contract and STD-01.9.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FMICP SSP; P03 gap analysis; P05 BIA; P08 runbook and notification matrix; P10 AI governance.
