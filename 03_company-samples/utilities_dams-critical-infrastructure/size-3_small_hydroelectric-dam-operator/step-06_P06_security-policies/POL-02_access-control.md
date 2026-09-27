# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Controls Engineer (OT) and IT Manager (IT) |
| Approved by | Vice President of Operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually each November (next review 2027-11-15), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-17, AC-18, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| FERC Security Program Rev. 3A | Table 9.3a (access control and functional segregation), Table 9.3b (access control), 7.2 (key control), Form 3 Q12, Q13, Q21 |

## 1. Purpose
Make sure only authorized people can reach the control system, the project works, and company information, only to the extent their job requires, and that every gate and unit command can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and vendors with access). Covers the PCDMS (OT), the corporate network, SaaS and cloud services, and physical access to the control room, powerhouse, spillway, and instrument houses.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Plant Manager | Approves OT access and each vendor remote session; quarterly OT access review |
| Controls Engineer | Creates and removes OT accounts; runs the jump host and OT firewall |
| IT Manager | Runs the identity provider and corporate accounts |
| Compliance and Security Coordinator | Card access and key control |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day, with the OT step |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, **including control room operators on the HMI**. Shared or generic accounts are prohibited. Where a device cannot support individual accounts (for example, a PLC or governor panel), the exception must be documented with compensating controls: physical protection, network isolation, and logging of who had physical access. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the Plant Manager for OT or the user's manager for IT. Operators must not have administrator rights on HMI servers. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 **Remote access to OT** is allowed only through the company jump host, with MFA using a phishing-resistant authenticator, named accounts, and session recording. Direct VPN connections to the control LAN are prohibited. Until MFA is in place, after-hours remote access to the HMI must be view-only; gate and unit commands require an operator in the control room or at a local panel. (AC-17; IA-2(1); IA-2(2); PR.AA-03; Rev. 3A Table 9.3b)
4.4 **Vendor remote access** must be on demand, not always on. Each session must be requested in advance, approved by the Plant Manager or the Operations Supervisor on shift, limited in time, recorded, and reviewed at least weekly by the Controls Engineer. (MA-4; AC-17; DE.CM-06; Rev. 3A Form 3 Q12a-12c)
4.5 MFA is required for all access to email, the identity provider, the cloud console, SaaS applications, and remote access. Administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03)
4.6 **Termination.** HR must open a termination ticket on or before the last day. IT and the Controls Engineer must disable the user's IT and OT access **the same business day**, or immediately for involuntary terminations, and change any device or panel password the person knew. (PS-4; AC-2)
4.7 The Plant Manager must review OT accounts and the vendor access list every quarter; managers must review IT access every quarter. (AC-2; AC-6)
4.8 Default passwords must be changed before any device is connected to the control LAN, cellular network, or corporate network, including PLC and panel web interfaces, modems, and network equipment. Passwords must be at least 14 characters where the device allows, and must not appear on the banned-password list. (IA-5; Rev. 3A Form 1 Q6, Q9)
4.9 No wireless connection may be added to the OT environment (including cellular modems) without a documented risk evaluation approved by the Plant Manager. (AC-18; Rev. 3A Table 9.3a, 9.3b)
4.10 Physical access to the control room, powerhouse, spillway gate controls, and instrument houses is limited to people on the approved card access list or under escort. Keys are controlled through the key register and inventoried every year. (PE-2; PE-3; PR.AA-06; Rev. 3A 7.2)
4.11 Accounts lock after 5 failed sign-in attempts on OT systems and 10 on IT systems. (AC-7)

## 5. Compliance and enforcement
Violations are handled under the company's disciplinary procedure (POL-01 section 5). Sharing an OT password or bypassing the jump host is a serious violation. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT remote access procedure (due 2026-11-30); P02 control statements AC-2, AC-17, IA-2; FERC Security Plan key control procedures
