# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-5, MA-4, PS-4, AU-2, AU-6 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, DE.CM-03 |
| Contract and legal drivers | State contract exhibit (AC, IA, AU families); county addendum; FAR 52.204-21(b)(1)(i), (ii), (v), (vi); FAR 52.204-9(b) and GSAR 552.204-9 (PIV cards) |

## 1. Purpose
Make sure only authorized people can reach company systems and customer building systems, only to the extent their job requires, and that every action on a building system can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff) and subcontractors. Covers company systems, the FOTP, customer building systems the company operates (BAS, access control, video), and GSA-issued PIV cards held by company staff.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Controls Engineering Manager and Security Systems Supervisor | Approve access to the BAS and access control platforms; run the monthly administrator review |
| Site Managers | Approve access for their site staff; confirm PIV card return for federal site staff |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day; collects PIV cards and badges |
| IT/OT Systems Administrator | Provisions and removes access; runs the identity provider and jump host |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a named account. Shared or generic accounts are prohibited on company systems and on customer building systems the company administers, including BAS supervisory servers and engineering workstations. Where a device cannot support named accounts, its password must be kept in the company password vault and rotated when anyone with access leaves. (IA-2; AC-2)
4.2 Access must be role-based, least-privilege, and approved by the component owner before it is granted. BAS roles are operator (view and acknowledge), technician (schedules and setpoints), and engineer (programs). (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, the CMMS, the cloud console, the identity provider, access control administrator portals, and all remote access. Cloud administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03)
4.4 **Remote access to customer OT networks** is allowed only through the company jump host, with MFA, a ticket, and session recording. Always-on remote-support tools and direct VPN routes to site networks are prohibited. Vendor and integrator sessions must be approved per session by the Controls Engineering Manager or Security Systems Supervisor and are disconnected when the work ends. (AC-17; MA-4)
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must disable all access **the same business day** (immediately for involuntary terminations), including access control administrator accounts. HR must collect any GSA PIV card on the last day and tell the GSA sponsor the same day (FAR 52.204-9(b)). Shared device passwords the person knew must be rotated within 5 business days. (PS-4; AC-2)
4.6 Component owners must review BAS and access control administrator accounts **monthly** and all other access **quarterly**. (AC-2; AC-6)
4.7 Accounts lock after 10 failed sign-in attempts where the system supports it. Company workstations lock after 10 minutes idle. ROC workstations lock too; alarms are shown on the wall display. (AC-7; AC-11)
4.8 Passwords must be at least 14 characters and not on the banned-password list. Manufacturer default passwords must be changed before any device is connected to a network the company manages or maintains. (IA-5; CM-6)
4.9 On GSA systems, staff follow GSA's access rules and use only GSA-provided access (virtual desktop or GSA-furnished equipment with PIV). Staff must not create other paths into GSA networks. (AC-17; AC-20)
4.10 Sign-ins, administrator actions, remote sessions, and door schedule changes must be logged and kept for at least 1 year, and reviewed weekly. (AU-2; AU-6; DE.CM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07) and the monthly and quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; remote access procedure (due 2026-11-30); P02 control statements AC-2, AC-17, IA-2, IA-5
