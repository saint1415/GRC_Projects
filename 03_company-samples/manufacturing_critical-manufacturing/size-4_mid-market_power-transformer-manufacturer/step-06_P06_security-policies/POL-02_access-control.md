# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4, PS-7, IA-2(2), PS-5, CM-7, PE-8 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06, GV.RR-04 |
| Drivers | FAR 52.204-21(b)(1)(i), (ii), (v), (vi), (viii); utility addenda secs. 3 and 6; CSF 2.0 benchmark |
| Supporting standards | STD-04 OT security standard; STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people, services, and devices can reach company systems, plant equipment, and customer systems, with the least privilege needed.

## 2. Scope
All accounts and access paths: identity provider, cloud, ERP, MES, HMIs, engineering workstations, test PCs, OEM and vendor remote access, the FMS, and company access to utility systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Owns this policy and STD-06; privileged access reviews |
| IT Director | Account administration for IT and cloud |
| OT Security Engineer | OT accounts, the remote access gateway, and OEM access |
| Managers and Plant Managers | Approve access for their staff; quarterly reviews |
| HR Director | Termination and transfer triggers |
| Director of Field Service | Utility access notices for field technicians |
| Director of Manufacturing Engineering | Physical access to control rooms and server rooms at the plants |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including MES supervisor accounts, HMI logins, test PCs, and OEM remote access. Where plant equipment cannot support individual accounts, a documented exception must name the compensating controls (role accounts with individual PINs, physical access limits, and logging). (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based, least-privilege, and approved by the user's manager. No more than 3 named administrators may hold ERP super-user rights, and no user may both maintain supplier bank details and approve payments. (AC-3; AC-5; AC-6; PR.AA-05)

4.3 MFA is required for email, the ERP, the identity provider, VPN, cloud consoles, the FMS administration, and all remote access into either plant. Every privileged account must use a phishing-resistant authenticator (FIDO2 security key). (IA-2(1); IA-2(2); PR.AA-03)

4.4 Service accounts must have only the rights their function needs, must never be members of domain administrator groups, and must have vaulted credentials rotated at least yearly. Trusts between directory domains must be one-way and documented. (AC-6; IA-5; PR.AA-05)

4.5 **Termination and transfer.** HR must open a termination ticket on or before the last day. All access, including MES accounts, badges, and OEM or utility access, must be disabled the same business day, or immediately for involuntary terminations. On transfer, prior roles must be removed within 5 business days. For field technicians, the Director of Field Service must notify each addendum utility within 1 business day that the technician's access should no longer be granted. (PS-4; AC-2; PS-5; GV.RR-04)

4.6 Managers must review their staff's ERP roles, MES accounts, and shared-site access every quarter. The Security Manager must review privileged accounts, and the OT Security Engineer must review OT and OEM accounts, every quarter. (AC-2; AC-6; PR.AA-05)

4.7 Default passwords must be changed before any system or device, including HMIs, controllers, network equipment, and cameras, is connected to a company network. Unused web or remote configuration interfaces must be turned off. (IA-5; CM-7; PR.AA-01)

4.8 Passwords must be at least 14 characters and not on the banned list. Local administrator passwords must be unique per device. Passwords must be kept in the company password manager and never saved on shared devices. (IA-5; PR.AA-01)

4.9 **Supplier remote access into either plant** must go through the company remote access gateway, with a named account, MFA, per-session approval by the plant Controls Lead or the OT Security Engineer, and session recording. Cellular or modem connections for OEMs must stay powered off except during an approved session, and are to be retired at Plant 2 by 2026-12-31. (AC-17; MA-4; PR.AA-03; DE.CM-06)

4.10 **Access to utility systems.** Field technicians may connect to a utility's systems only through that utility's own MFA-protected remote access, one session at a time, from a laptop assigned to them by name. (AC-17; PR.AA-03)

4.11 Two break-glass administrator accounts must exist for each administrative plane (identity provider, cloud organization, corporate directory). Their credentials must be sealed offline, tested quarterly, and used only when normal sign-in fails. Every use is reviewed by the Security Manager. (AC-2; PR.AA-05)

4.12 Physical access to server rooms, control rooms, and the OT DMZ cabinet must use individual badges, reviewed quarterly. Visitors and OEM technicians must be logged and escorted. (PE-3; PE-8; PR.AA-06)

4.13 Federal contract information must be accessible only to the named project team, on the systems listed in the SSP. (AC-3; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.13. Compliance is verified through quarterly access reviews and the annual control assessment (P07: AC-2, AC-6, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4).

## 6. Exceptions
Exceptions follow POL-01 section 4.12. Plant equipment that cannot support individual accounts or MFA is the most common exception; each one must name its compensating controls and expire within 12 months.

## 7. Related documents
POL-01; STD-04 OT security standard; STD-06 Authenticator and privileged access standard; P02 section 11 (digital identity acceptance); FAR 52.204-21(b)(1)(i), (ii), (v), (vi), (viii); utility addenda secs. 3 and 6
