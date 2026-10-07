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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-5, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(a)(1)(A)(ii), (b)(1)) |

## 1. Purpose
Make sure only authorized, identified people reach company systems, especially systems that can change treatment, chemical feed, or pumping, and that each person has only the access the job needs.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in all four regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee and in the two service lines, including acquired systems from their acquisition date. Covers all IT and OT systems and data: SCADA, PLCs, RTUs, telemetry, and HMIs at the 126 community water systems and 5 ROCCs; cloud, colocation, and SaaS; and systems that vendors and integrators operate or support for the company, including the services offered to municipal clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Owns this policy; runs the identity platform and OT identity domains |
| Director of OT Security | Owns the OT remote access gateway and its approval workflow |
| System owners (including the GCR SCADA Manager and each ROCC SCADA manager) | Approve access to their systems; certify it quarterly |
| ROCC shift supervisors | Approve each vendor remote session before it connects |
| Chief Human Resources Officer | Sends termination and transfer events on the same business day |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether the 2026 independent assessment tested it (P07).

4.1 Every user must have a unique named account, including on operator HMIs, engineering workstations, and panel HMIs. Shared accounts are prohibited except control room shift accounts that an individual signs in to at shift start, as recorded in the tailoring record. (AC-2; IA-2; PR.AA-01)
4.2 Access must be approved by the system owner and limited to the least privilege the role needs; the SCADA engineer role (logic and alarm-limit changes) must be limited to named OT engineers and SCADA technicians. (AC-3; AC-6; PR.AA-05)
4.3 Multi-factor authentication is required for all remote access, all privileged access, and all access to cloud and SaaS administration. Privileged users and all remote OT users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.4 All remote access to OT must go through the OT remote access gateway, with approval by the ROCC shift supervisor before the session connects, session recording, and a time-limited window. Always-on vendor remote tools and vendor-owned devices on OT networks are prohibited. (AC-17; MA-4; PR.AA-05)
4.5 Access must be disabled on the same business day as termination, including OT domain accounts and any local HMI or device accounts the person knew. (AC-2; PS-4; PR.AA-01)
4.6 Privileged and OT access must be certified quarterly by system owners; all other access semiannually. (AC-2; PR.AA-05)
4.7 Default and commissioning credentials on any device, including PLCs, RTUs, telemetry gateways, and network equipment, must be changed before the device goes into service, and device credentials must be stored in the PAM vault. (IA-5; PR.AA-01)
4.8 Privileged access to servers, cloud consoles, and OT hosts must go through PAM with session recording. (AC-6(9); AC-2; PR.AA-05)
4.9 Break-glass accounts, including the sealed control room emergency accounts, must be used only when normal sign-in fails during an operational emergency; each use must be logged and reviewed within 1 business day and the account reset. (AC-2(2); PR.AA-05)
4.10 Engineering workstations, servers, and office devices must lock after 15 minutes of inactivity. Operator HMIs in staffed, badge-controlled control rooms may stay unlocked for alarm response, as the SP 800-82 Rev. 3 OT overlay allows. (AC-11; PR.AA-06)
4.11 Mutual aid operators, visitors, and contractors without a company account must never receive SCADA credentials; they may operate equipment only under the direct supervision of a company operator. (AC-2; PS-7; PR.AA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 OT Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Control Room Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, the annual independent assessment by Internal Audit and the co-sourced OT assessment firm (P07), and plant drills. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GCR-WTSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; each covered system's RRA and ERP.
