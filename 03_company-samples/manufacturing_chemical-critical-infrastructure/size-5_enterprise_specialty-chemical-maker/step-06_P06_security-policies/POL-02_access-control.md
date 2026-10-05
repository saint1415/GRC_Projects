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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, IA-2, IA-5, IA-8, PE-3, PS-4, MA-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Regulatory drivers | MTSA 33 CFR 101.650(a), (e)(3)(v), (f)(3), (i)(1); DOT 49 CFR 172.802(a)(2); CFATS RBPS 8 (voluntary benchmark) |

## 1. Purpose
Make sure only authorized people, using their own credentials, can reach company systems, and that access to process control and safety systems is tighter than access to office systems, because a misuse there can cause a release.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, integrators, and temporary staff) at all 14 plants, 9 distribution centers, 2 R&D centers, and offices, including acquired plants from their acquisition date. Covers all information technology (IT) and operational technology (OT): process control systems, safety instrumented systems, PLCs, terminal and loading rack automation, cloud, colocation, SaaS, and systems that vendors and integrators operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Identity platform; IT account lifecycle; access certification |
| Director of OT Security | OT access standard; remote access gateway; integrator access |
| Plant controls engineering managers | OT directory accounts, DCS roles, SIS keys |
| Shift supervisors | Approve each remote OT session |
| Managers and system owners | Approve access and certify it quarterly |
| Chief Human Resources Officer | Timely leaver and mover events |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user must have a unique account; shared accounts are prohibited on IT systems and on OT systems that support individual accounts. Role logons on OT panels that cannot support individual accounts need an approved exception with compensating physical controls. (AC-2; IA-2; PR.AA-01)
4.2 Access must follow least privilege. Engineer and administrator rights on DCS, batch, and SIS systems must be limited to named controls staff and reviewed quarterly. (AC-6; PR.AA-05)
4.3 Recipe authoring and approval, and control logic preparation and approval, must be done by different people. (AC-5; PR.AA-05)
4.4 Access must be certified quarterly for IT systems in scope for SOX and for all OT systems. (AC-2; PR.AA-05)
4.5 Accounts must be disabled the same business day as a termination for IT and the remote access gateway, and within 24 hours for OT directory and local OT accounts. (PS-4; AC-2; PR.AA-01)
4.6 All remote access to OT must go through the central remote access gateway with named accounts, MFA, per-session approval by the shift supervisor, and session recording. No other remote access path to OT is allowed. Logic downloads and SIS changes must not be made remotely. (AC-17; AC-17(1); MA-4; IA-2(1); PR.AA-05)
4.7 MFA is required for all remote access, all privileged IT access, and all cloud and SaaS access. Local OT console logons may rely on physical access control instead, under an approved exception. (IA-2(1); IA-2(2); PR.AA-03)
4.8 Default passwords must be changed before any IT or OT device is used. Passwords must meet STD-02.2 where the device supports it. (IA-5; PR.AA-03)
4.9 Accounts must lock after repeated failed logons on IT systems and the gateway. Operator stations are exempt so an operator is never locked out during an upset; failed logons there must be alerted. (AC-7; PR.AA-03)
4.10 Integrator and vendor users must be sponsored by a company engineer, screened under contract, trained before access, and reviewed monthly. (IA-8; PS-7; PR.AA-02)
4.11 Physical access to control rooms, rack rooms, and SIS cabinets must be limited to authorized people, logged, and monitored. (PE-3; PE-6; PR.AA-06)
4.12 Break-glass accounts for IT and OT must be sealed, tested quarterly, and reviewed after every use. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Privileged Access Standard
- STD-02.4 OT Access Standard (DCS roles, SIS keys, remote access gateway, panel HMIs)
- STD-02.5 Physical Access to OT Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 IT Break-Glass Procedure
- PRC-02.4 Integrator Onboarding Procedure
- PRC-02.5 OT Access Certification Procedure
- PRC-02.6 PLT-01 OT Provisioning Procedure
- PRC-02.7 OT Break-Glass Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT metrics), the annual Internal Audit assessment (P07), access certifications, and MTSA Cybersecurity Plan audits at PLT-01. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GC-PCBMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
