# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | President and General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or a TSA designation notice |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Regulatory basis | C-TRANSPORTATION-BM; C-TRANSPORTATION-S03 (1520.9(a)(2)); C-TRANSPORTATION-S04 (236.1006(a)) |

## 1. Purpose
Make sure only authorized people and systems can reach company information and operational technology, with the least privilege they need.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) at Central Yard, North Yard, South Yard, the tower sites, and on trains. Covers all company systems and data, including operational technology (dispatch, radio, wayside, and onboard PTC equipment) and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department heads (Vice President of Operations, Chief Engineer, Chief Mechanical Officer, Car Management and Customer Service Manager, Director of Finance and Administration) | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider and the jump host |
| Signal and Communications Supervisor | Controls keys and credentials for tower sites, detectors, and crossing monitors |
| All workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including on dispatch consoles and the PTC administration workstation. Shared or generic accounts are prohibited. Documented exceptions must have compensating controls. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the user's department head before it is granted. Only dispatcher roles may issue or void movement authority in the CAD system. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, the TMS, the identity provider, the cloud console, the PTC back office portal, every VPN, and every administrator account. Administrators, PTC administrators, and vendors must use phishing-resistant hardware keys. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable the user's accounts and crew tablet access **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.5 Department heads must review their staff's access every quarter. The IT Manager must review administrator accounts every quarter. (AC-2; AC-6)
4.6 Accounts lock after 10 failed sign-in attempts. Office workstations lock after 15 minutes idle. **Dispatch consoles are exempt from idle lock** because the dispatch center is badge-controlled and staffed at all times. (AC-7; AC-11)
4.7 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline in the dispatch center safe, tested quarterly, and used only when the identity provider is unavailable. Any use is reviewed by the IT Manager. (AC-2)
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Default passwords on any device, including detector modems, crossing monitors, radio equipment, and network gear, must be changed before the device is connected. (IA-5; PR.AA-01)
4.9 **Vendor and remote access.** Vendors and the MSP must use named accounts with MFA, through the company jump host, with sessions recorded. Vendor access to operations systems is enabled only for an approved ticket and disabled when the work ends. No always-on vendor connections. (AC-17; MA-4; PR.IR-01)
4.10 The PTC administration workstation and dispatch consoles are used only for their operational purpose. No email or web browsing. (AC-6; CM-7)
4.11 **Physical access.** Badge access to HQ and the dispatch center is approved by the Manager of Safety and Security and reviewed quarterly. Tower shelters and detector bungalows use site-specific keys with a key log. Onboard PTC housings stay locked and sealed. (PE-3; PR.AA-06)
4.12 Access to SSI is limited to named people with a need to know, as listed by the Manager of Safety and Security. (AC-3; 1520.9(a)(2))

## 5. Compliance and enforcement
Violations are handled under the discipline procedure in POL-01 section 4.8. Consequences range from retraining to termination, depending on intent and harm; for employees covered by a collective bargaining agreement, the agreement's procedures apply. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; access review procedure; P02 control statements AC-2, AC-6, AC-17, IA-2, MA-4
