# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Legal and contractual basis | Fla. Stat. 501.171(2); Manufacturer A agreement (named, MFA-protected portal accounts) |

## 1. Purpose
Make sure only authorized people can reach customer records, customer devices, and company systems, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (employees, managers, temporary staff, and contractors) at Stores A to D and the Depot. Covers all company systems and data, customer devices and the data on them while they are in the company's custody, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Store Managers and Operations Manager | Request and approve access for their staff; complete quarterly access reviews |
| HR and Payroll Specialist | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager and IT Support Technician | Provision and remove access; run the identity provider and device management |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique, named account in SYS-01, on bench PCs, and on manufacturer portals. Shared or store accounts are prohibited, including on counter tablets. (IA-2; AC-2; PR.AA-01)
4.2 SYS-01 access must be role-based: counter staff see contact and device details; technicians see their assigned tickets; only managers and the IT Manager can export. Nobody may see a stored passcode except the technician assigned to that repair. (AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all access to SYS-01, email, the identity provider, remote access, cloud administration, and manufacturer portals that support it. Counter tablets use badge-plus-PIN sign-in backed by the identity provider. (IA-2(1); PR.AA-03)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable all access, including manufacturer portal accounts, **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2)
4.5 Managers must review their staff's SYS-01 roles, export rights, and manufacturer portal accounts every quarter. (AC-2; AC-6)
4.6 Accounts lock after 10 failed sign-in attempts. Office PCs, counter tablets, and bench PCs lock after 10 minutes idle. (AC-7; AC-11)
4.7 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. Any use is reviewed by the Information Security Lead. (AC-2)
4.8 Passwords must be at least 14 characters and not on the banned-password list. Local administrator passwords on office and bench PCs must be unique per device and managed by the IT tool. Default passwords on any device or appliance must be changed before use. (IA-5)
4.9 Vendor remote access (including the SYS-01 vendor's support sessions) must be approved per session, use named accounts, and be logged. (AC-17)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Misuse of a customer's device data is treated as serious misconduct. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the log reviews in POL-03.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04 (customer data access standard); access review checklist; P02 control statements AC-2, AC-3, IA-2
