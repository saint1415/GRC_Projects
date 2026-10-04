# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (with the Controls Engineering Manager for OT) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, IA-2, IA-2(1), IA-5, MA-4, MA-5, PE-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, GV.RR-04 |
| Rules | 9 CFR 417.5(b); 9 CFR 416.16(a); 29 CFR 1910.119(f)(4); C-FOOD-AG-R01 (benchmark: 21 CFR 121.135(a)) |
| Supporting standards | STD-02 OT access and remote access; STD-10 Authenticator and privileged access |

## 1. Purpose
Make sure only authorized people, using identities that can be traced to them, can reach company systems, control systems, and restricted areas, and that no single person can change how food is made without a second check.

## 2. Scope
All accounts and access paths to IT and OT at both plants and the corporate offices, including HMIs, SCADA, historians, the MES, refrigeration controllers, the cold-chain service, cloud accounts, SaaS, and physical access to production areas, engine rooms, and server rooms.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Director | Identity provider, cloud, and SaaS accounts; quarterly access reviews for IT |
| Controls Engineering Manager | OT accounts and roles; quarterly OT access reviews |
| Security Manager | Remote access gateway, privileged access management, vendor sessions |
| Vice President of Food Safety and Quality Assurance | Approves who may approve formulation, setpoint, and blend changes |
| Plant Managers | Physical access to restricted areas at their plant |
| HR Director | Joiner, mover, and leaver notices on or before the effective date |
| Managers | Approve and review their staff's access |

## 4. Policy statements
4.1 Every user must have a unique account on every system, including HMIs, SCADA, the MES, the Plant 2 label server, and the food safety records application. Shared or generic accounts are prohibited, except documented view-only operator accounts that cannot change setpoints, recipes, or records. (IA-2; AC-2; PR.AA-01; 9 CFR 417.5(b); 9 CFR 416.16(a))
4.2 Access must be role-based, least-privilege, and approved by the user's manager. Write access to PLC programs is limited to named controls engineers and named integrator staff during approved sessions. (AC-3; AC-6; PR.AA-05)
4.3 **Two-person rule for food safety values.** Changes to cure, brine, antimicrobial, or other formulations, to Plant 2 blend recipes and fat targets, and to setpoint ranges that enforce a critical limit (cook, chill, cold storage, foreign material detection) require a proposer and an FSQA approver. HMIs must enforce approved ranges. (AC-5; SI-10; 9 CFR 417.2(c)(3); C-FOOD-AG-R01 (benchmark: 21 CFR 121.135(a)))
4.4 MFA is required for all identity provider accounts, cloud administration, the records application, VPN, SaaS administrator consoles, engineering workstations, and **all remote access to OT**. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 **OT remote access.** Vendors and staff may reach OT only through the company remote access gateway, with a named account, MFA, a session approved for a stated purpose and time window, and session recording. Vendor accounts must be disabled between sessions. Always-on VPN accounts and cellular modems on OT equipment are prohibited. (AC-17; MA-4; PR.AA-05)
4.6 **Termination.** HR must open a termination ticket on or before the last day. IT must disable business access the same business day, or immediately for involuntary terminations. The Controls Engineering Manager must remove OT access the same day and, until shared accounts are eliminated, rotate every shared OT password the person knew. (PS-4; AC-2; GV.RR-04)
4.7 **Transfers.** When a worker changes line, plant, or role, access no longer needed must be removed within 5 business days. (PS-5; AC-2)
4.8 Managers must review their staff's access every quarter. The Controls Engineering Manager must review OT accounts and vendor accounts every quarter. Privileged accounts are reviewed monthly by the Security Manager. (AC-2; AC-6)
4.9 Passwords must be at least 14 characters and not on the banned list. Default passwords on every device, including controllers, x-ray units, metal detectors, sensors, gateways, and modems, must be changed before the device is connected, and checked at commissioning and in CCP verification. (IA-5; PR.AA-01)
4.10 Identity provider accounts lock after 10 failed sign-in attempts. HMIs do not lock out operators, because lockout during a process upset is a safety risk; HMIs must instead be physically protected and use quick badge or PIN sign-in. (AC-7; PE-3)
4.11 **Physical access.** Badge access is required to enter each plant. The cure and ingredient room, dosing skid room, OT server rooms and closets, and engine rooms are restricted to named roles. Visitors and contractors must sign in and be escorted in production areas and engine rooms. (PE-3; MA-5; PR.AA-06; 29 CFR 1910.119(f)(4))

## 5. Compliance and enforcement
Checked through quarterly reviews and the annual assessment (P07). Violations are handled under POL-01 section 5.

## 6. Exceptions
Follow POL-01 section 4.8. An exception for a shared OT account must name the compensating control (for example, physical presence and CCTV) and expire by 2027-03-31.

## 7. Related documents
POL-01; STD-02; STD-10; System Security Plan (P02) sections 10 and 11; HACCP plans
