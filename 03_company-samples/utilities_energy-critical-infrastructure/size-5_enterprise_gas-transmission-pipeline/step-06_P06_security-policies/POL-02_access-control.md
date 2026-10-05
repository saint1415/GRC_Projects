# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management (IT); Director of OT Security (OT sections) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 (version 2026.1) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(9), AC-17, CA-3, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-3, PS-4, PS-5, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Regulatory drivers | SD Pipeline-2021-02G Section III.C (C-ENERGY-R03); 49 CFR 192.631(b)(5) (C-ENERGY-R04) |

## 1. Purpose
Make sure only authorized people and processes reach company systems, only to the extent their role requires, and that access ends promptly. In OT, access rules must never stop a controller from seeing and acting on the pipeline; where a standard control would, the compensating control is documented in the Cybersecurity Implementation Plan.

## 2. Scope
All workers, suppliers, and authorized representatives with access to company IT or OT, including the OT domain, SCADA consoles, station HMIs, engineering workstations, the OT remote access gateway, cloud accounts, and SaaS. PS-3 legacy systems are in scope from the acquisition date and run under exception EXC-2026-015 until migration.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Enterprise identity platform, IT privileged access, access certifications |
| Director of OT Security | OT access standard (STD-02.4), OT remote access gateway, OT privileged access |
| Director of SCADA Engineering | OT domain administration and OT account changes |
| Vice President, Gas Control; Director of Compression Engineering | Approve OT access for control room and station roles |
| Managers | Request and certify their staff's access |
| Chief Human Resources Officer | Timely leaver and mover events from the HR system |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are allowed only where STD-02.4 permits them as critical for operations (station HMI operator accounts), must be registered, must be limited to operator functions, and their passwords must be changed within 24 hours after anyone who knew them leaves or transfers. Shared administrator accounts are prohibited. (IA-2; AC-2; IA-5; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved before it is granted. OT access also needs the approval of the Vice President, Gas Control (control room roles) or the Director of Compression Engineering (station roles). Only controller-role accounts may send commands to field devices. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No single person may both make and approve a SCADA or station control configuration change, or both create and pay a vendor. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all privileged and engineering access to OT, all cloud administration, and all access to business systems from outside the network. Where MFA at control room consoles would put safe operation at risk, the compensating controls documented in the Cybersecurity Implementation Plan apply (badge and PIN to the control room floor, console bound to the controller role and desk, session logging). (IA-2(1); IA-2(2); PR.AA-03)
4.5 Business access must be disabled the same business day as a termination, and immediately for involuntary terminations. OT accounts must be disabled within 4 hours of the HR leaver event. Access of transferred workers must be reviewed and adjusted within 5 business days. (PS-4; PS-5; AC-2; PR.AA-05)
4.6 OT and privileged access must be certified every quarter by the approving owner; other access every six months by managers. (AC-2; PR.AA-05)
4.7 Privileged access must be granted through IT privileged access management or OT privileged access, for the approved window only, and every privileged session must be logged. (AC-6; AC-6(9); PR.AA-05)
4.8 Supplier and remote access to OT must go through the OT remote access gateway with a named account, MFA, approval for each session by the system owner, and session recording. The controller on duty must be told before any session that can change live displays or points. Always-on supplier connections, including cellular modems, are prohibited. (AC-17; MA-4; PR.AA-05)
4.9 There must be no trust relationship between the business domain and the OT domain. Trust relationships in each domain must be reviewed every quarter. (CA-3; SC-7; PR.IR-01)
4.10 Manufacturer default passwords must be changed before any device or system is connected. Memorized secrets must be reset on the STD-02.4 schedule (365 days for user accounts; 180 days for privileged and shared accounts). Components that cannot meet the schedule must have documented mitigations and a timeframe. (IA-5; PR.AA-01)
4.11 Physical access to control rooms, DMZ equipment rooms, and compressor station control buildings must be by badge; control room floors also require a PIN. Visitors must be escorted and logged. (PE-3; PR.AA-06)
4.12 Each control room must keep sealed break-glass OT accounts that are tested every quarter, and every use must be reviewed by the Director of OT Security. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Supplier Access Standard
- STD-02.4 OT Access Standard (shared operational accounts, console access, supplier sessions, memorized secret reset schedule)
- PRC-02.1 OT Access Request and Review Procedure
- PRC-02.2 Shared Station Account Procedure
- PRC-02.3 Break-Glass OT Account Procedure

## 6. Compliance and enforcement
Compliance is monitored through access certifications, OT account analytics, gateway session reviews, the annual Internal Audit assessment (P07), and the Cybersecurity Assessment Plan. Violations are handled under PRC-01.1 (POL-01 statement 4.16).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. Current access exceptions include EXC-2026-007 (shared operator accounts on legacy station HMIs), EXC-2026-015 (PS-3 local accounts and PS3-CR console controls), and EXC-2026-022 (7 supplier modems until removal), listed in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; TSA-approved Cybersecurity Implementation Plan; P02 PSGCS SSP section 11; P07 results for AC-2, AC-17, IA-2, IA-5, MA-4, PE-3, and PS-4.
