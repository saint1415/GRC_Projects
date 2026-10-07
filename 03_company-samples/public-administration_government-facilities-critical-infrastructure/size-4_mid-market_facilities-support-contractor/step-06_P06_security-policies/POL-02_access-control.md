# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (Information Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4, PS-5, AU-2, AU-6 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, DE.CM-03 |
| Contract and legal drivers | State contract exhibit (AC, IA, AU families); County A addendum and Supervisor of Elections annex; County B and City addenda; FAR 52.204-21(b)(1)(i), (ii), (v), (vi); FAR 52.204-9(b) and GSAR 552.204-9 (PIV cards) |
| Supporting standards | STD-03 Third-party, subcontractor, and remote access; STD-06 Authenticator and device credential |

## 1. Purpose
Make sure only authorized people can reach company systems and customer building systems, only to the extent their job requires, and that every action on a building system can be traced to a person.

## 2. Scope
All workforce members and subcontractors. Covers company systems, the IFOP, the customer access control tenants and BAS clusters the company administers, customer building systems the company operates (BAS, access control, video), and GSA-issued PIV cards held by company staff.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Building Technology, Controls Engineering Manager, Security Systems Manager | Approve access to the BAS clusters and access control tenants; run the quarterly OT access reviews; approve vendor broker sessions |
| OT Security Engineer | Owns broker policy and the device credential vault |
| Program managers | Approve access for their contract's staff; confirm PIV card return for federal site staff |
| HR Director | Opens onboarding, transfer, and termination tickets the same day; collects PIV cards and badges |
| IT Director's team | Provisions and removes access; runs the identity provider and broker |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a named account. Shared or generic accounts are prohibited on company systems and on customer systems the company administers, including BAS clusters, access control tenants, and engineering workstations. Subcontractor technicians each get their own account. Where a field device cannot support named accounts, its password must be kept in the device credential vault and injected by the broker. (IA-2; AC-2)
4.2 Access must be role-based, least-privilege, and approved by the component owner before it is granted. BAS roles are operator (view and acknowledge), technician (schedules and setpoints), and engineer (programs). Integrators get device-level roles only, never tenant administrator. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all company accounts. Administrators of the cloud, identity provider, broker, and access control tenants must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Remote access to customer OT networks** is allowed only through the company remote access broker, with MFA, a ticket, per-session approval by a named Building Technology manager, and session recording. Always-on remote-support tools, vendor cloud relays, cellular modems, and direct VPN routes to site networks are prohibited for staff and subcontractors alike. Edge firewalls must accept management traffic only from the broker. (AC-17; MA-4; SC-7)
4.5 **Termination.** HR must open a termination ticket on or before the last day. Access must be removed **the same business day** (immediately for involuntary terminations) in the identity provider, every customer access control tenant, and every BAS cluster. HR must collect any GSA PIV card on the last day and tell the GSA sponsor the same day (FAR 52.204-9(b)). Device passwords the person knew must be rotated within 5 business days. (PS-4; AC-2)
4.6 **Transfers.** When a person moves between contracts, access to the previous customer's tenant, cluster, and sites must be removed within 5 business days. (PS-5; AC-2)
4.7 Component owners must review BAS cluster and access control tenant administrator accounts **quarterly**, and all other access at least quarterly. (AC-2; AC-6)
4.8 Accounts lock after 10 failed sign-in attempts where the system supports it. Workstations lock after 10 minutes idle (15 minutes for ROC consoles, with alarm walls kept visible). (AC-7; AC-11)
4.9 Passwords must be at least 14 characters and not on the banned-password list. Manufacturer default passwords must be changed before any device is connected to a network the company manages or maintains, and device passwords must never be kept in spreadsheets or shared by email. (IA-5; CM-6)
4.10 On GSA systems, staff follow GSA's access rules and use only GSA-provided access (virtual desktop or GSA-furnished equipment with PIV). Staff must not create other paths into GSA networks. (AC-17; AC-20)
4.11 Sign-ins, administrator actions, remote sessions, BAS program downloads, and door schedule changes must be logged, kept for at least 1 year, and reviewed under the logging standard (STD-02). (AU-2; AU-6; DE.CM-03)
4.12 **Elections warehouse.** Remote unlock of the voting equipment cage doors must be disabled in the County A tenant. Access to the cage follows the Supervisor of Elections annex: two-person access and a log export after each election. (AC-3; AC-6)
4.13 Customer access control tenants and BAS clusters must be connected to the identity provider for sign-in and deprovisioning where the platform supports it, or reconciled against the identity provider daily. (AC-2(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual control assessment (P07), the quarterly access reviews, and the weekly broker bypass check.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 section 4.4, and expire within 12 months. No exception may permit remote access outside the broker.

## 7. Related documents
POL-01; POL-05; STD-03; STD-06; remote access procedure (due 2026-12-31); P02 control statements AC-2, AC-17, IA-2, IA-5
