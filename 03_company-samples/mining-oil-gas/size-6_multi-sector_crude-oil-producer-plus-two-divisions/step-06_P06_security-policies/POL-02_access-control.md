# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crude Oil Production, Power Generation, Crude Logistics) and corporate shared services |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director; OT rules by the Group OT Security Director) |
| Approved by | Group CISO, under authority of POL-01 (2026-09-17) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-4, AC-6, AC-6(5), AC-7, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory and benchmark drivers | NIST SP 800-82 Rev. 3 sections 6.2.1 and 6.2.10 (benchmark); NERC CIP-003-9 R2 Attachment 1 Sections 3 and 6; Fla. Stat. 501.171(2) |
| Division supplements | Production: SCADA console accounts and field device credentials. Power Generation: CIP-003-9 electronic access and vendor remote access. Crude Logistics: pipeline controller accounts, shipper portal, and dispatch access |

## 1. Purpose
Make sure only authorized people and processes reach group systems, and that every path from business IT into OT is controlled, owned by one division, and visible to the SOC.

## 2. Scope
All workforce identities, service accounts, administrator accounts, local OT accounts (SCADA, HMI, DCS, and field device accounts), vendor and integrator identities, and external identities (shipper users, royalty owner portal users) in every division and in corporate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group OT Security Director | Owns the OT DMZ standard, the jump server design, and OT access rules |
| Division OT owners | Approve OT access for their systems and keep local OT accounts named and reviewed |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Local OT accounts must be named and tied to that identity. Shared accounts are prohibited, except a documented console account where the OT software supports only one, with physical access control and logging as compensating controls. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege. OT roles must separate view, operate, and engineer rights. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access to business systems. Administrators and all remote access into OT must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **No direct IT-to-OT paths.** Access into any OT network must pass through that division's OT DMZ. Jump servers must serve one division only and be reachable only from privileged access workstations, never from general desktops or the virtual desktop pool. (AC-17; SC-7; AC-4; PR.IR-01; PR.AA-05)

4.5 **Service accounts that cross an OT DMZ** must be read-only, serve one division, and be documented in an interconnection agreement. Data must flow outward from OT; no service may pull from, or write into, an OT DMZ from the corporate or cloud side. (AC-4; AC-6; CA-3; PR.IR-01; PR.AA-05)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Local OT accounts must be removed the same day. Contractor accounts must expire at the assignment end date. (PS-4; AC-2; PR.AA-01)

4.7 Managers and data owners must certify access every quarter, including privileged, service, and local OT accounts. (AC-2; PR.AA-05)

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.9 Accounts must lock after 10 failed attempts. Operator consoles in control rooms may be exempt from lockout where lockout could delay a safety response, with physical access control and logging as compensating controls. (AC-7; PR.AA-03)

4.10 **Vendor and integrator remote access** must go through group PAM with named accounts, MFA, approval for each session, recording, and OT sensor monitoring, and must be possible to disable at once. Persistent or always-on vendor paths are prohibited. (AC-17; MA-4; SI-4; PR.AA-05; DE.CM-06)

4.11 **Device credentials.** Default vendor passwords must be changed before any field or plant device is connected. Device and modem management passwords must be unique per site or device and stored in the group vault. (IA-5; IA-3; PR.AA-03)

4.12 **Emergency access.** Each control room must keep sealed local break-glass accounts that work without SYS-G1, tested quarterly and reviewed after every use. (AC-2; PR.AA-01)

4.13 **External identities.** Shipper portal and owner portal users must use MFA; shipper administrators manage their own users under the platform's terms. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment of common controls and division samples, the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may weaken a safety function or extend a legal notice deadline.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02); group OT DMZ standard.
