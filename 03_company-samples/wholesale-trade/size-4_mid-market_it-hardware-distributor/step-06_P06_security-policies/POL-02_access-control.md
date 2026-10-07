# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of Information Technology |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-7, AC-11, AC-17, AC-18, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Contract and regulatory basis | SP 800-171 Rev. 2 3.1, 3.5, 3.7.5, 3.9.2; FAR 52.204-21(b)(1)(i)-(iii), (v)-(vi) |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 OT security standard |

## 1. Purpose
Make sure only authorized people, systems, and devices can reach company, customer, and federal information, and only to the extent their job requires.

## 2. Scope
All workforce members, reseller portal users, service providers, and the DC automation integrator, and every system in the Distribution Operations Platform, including the Federal Integration Enclave and DC automation.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Information Technology | Owns this policy; runs account management and access reviews |
| Security Manager | Privileged access, the access broker, and monitoring of privileged activity |
| Federal Integration Lab Manager | Approves every enclave and FIL access request and leads enclave access reviews |
| System and data owners (Vice President of Sales Operations, Director of Distribution Operations, Chief Financial Officer) | Approve access to their systems and review it quarterly |
| HR Director | Sends hires, transfers, and terminations to the identity provider feed the same day |
| Managers | Request only the access their staff need and confirm reviews |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are not allowed, except documented operator accounts on DC automation workstations until they are replaced (exception due to end 2027-03-31). (IA-2; AC-2; PR.AA-01)
4.2 Access must be approved by the system or data owner and limited to what the role needs. (AC-3; AC-6; PR.AA-05)
4.3 **Enclave access.** Access to the enclave, the CUI library, and the FIL requires a background check, U.S. person confirmation, CUI training, and approval by the Federal Integration Lab Manager. Access is granted per prime program. (AC-3; PS-3; PR.AA-05)
4.4 MFA is required for all workforce access to company systems. Administrators and enclave users must use phishing-resistant security keys. (IA-2(1); IA-2(2); PR.AA-03)
4.5 **Privileged access.** Administrators must use separate privileged accounts and obtain time-limited elevation through the access broker. This applies to cloud, server, ERP, WMS, and enclave tenant administration (the latter three by 2027-01-31). The number of standing administrators per system must be approved by the Security Manager. (AC-6(5); AC-6; PR.AA-05)
4.6 Access must be reviewed quarterly for the ERP, WMS, enclave, and privileged accounts, and annually for other systems. (AC-2; PR.AA-05)
4.7 **Leavers and movers.** Access must be removed on the last working day, including enclave accounts, WMS accounts, and FIL badges. On transfer, access from the old role must be removed within 5 business days. (PS-4; PS-5; AC-2; PR.AA-05)
4.8 Accounts inactive for 45 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.9 Remote access must go through the identity provider with MFA or, for CUI, only through enclave virtual desktop sessions that block clipboard, drive mapping, and local printing. (AC-17; PR.AA-05)
4.10 **Vendor and integrator access.** Nonlocal maintenance and vendor remote access, including the DC automation integrator, must use the remote access gateway with per-session approval, MFA, session recording, and automatic termination. Always-on vendor remote tools are prohibited. (MA-4; AC-17; PR.AA-05)
4.11 Reseller portal accounts must use MFA from 2027-01-31, and reseller administrators must review their users each quarter. (IA-8; PR.AA-03)
4.12 Default passwords must be changed before any device, including OT controllers and network devices, connects to a company network. Service account secrets must be vaulted and rotated at least annually. (IA-5; PR.AA-01)
4.13 Accounts lock after repeated failed sign-ins, and devices lock after 15 minutes of inactivity. (AC-7; AC-11; PR.AA-03)
4.14 Separation of duties must be kept between purchase order entry, receiving, and payment approval, and between system administration and audit log administration. (AC-5; PR.AA-05)

## 5. Compliance and enforcement
Compliance is checked by quarterly access reviews, the annual independent assessment (P07), and access broker reports. Violations are handled under POL-05 section 4.12.

## 6. Exceptions
Exceptions follow POL-01 section 4.6.

## 7. Related documents
POL-01; POL-04; STD-06; STD-04; System Security Plan (P02); P07 POA&M items POAM-002, POAM-003, POAM-004, POAM-013, POAM-014, POAM-026
