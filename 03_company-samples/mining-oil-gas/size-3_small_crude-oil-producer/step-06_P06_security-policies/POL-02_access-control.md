# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager, with the SCADA and Automation Supervisor for OT |
| Approved by | CFO and VP Operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-4, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-3, PS-4, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 5.2.3 (network security), 6.2.1 (identity and access), 6.2.10 (remote access) |

## 1. Purpose
Make sure only authorized people and devices can reach company systems and the SCADA network, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary workers) at headquarters, both field offices, the OCC, and every well site and facility. Covers all business IT and OT systems, including systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and Field Superintendents | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes corporate, SaaS, and cloud access; runs the identity provider and the vendor jump host |
| SCADA and Automation Supervisor | Provisions and removes SCADA and controller accounts; approves OT access |
| OCC shift lead | Approves each vendor remote session to SCADA |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are prohibited, except for OCC HMI operator stations where the SCADA software cannot switch users quickly enough for safe operation. Any such exception must be documented with compensating controls (badge-controlled room, shift sign-in log, and monthly event review), consistent with the SP 800-82 Rev. 3 OT overlay. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Controller programming rights are limited to named automation technicians and engineers. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, SaaS applications, the corporate VPN, cloud administration, and all remote access to the SCADA network. IT administrators must use phishing-resistant hardware keys. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Vendor and remote access to SCADA.** Remote access to the SCADA network is allowed only through the company jump host, with a named account and MFA for each person. Each session must be approved by the OCC shift lead, recorded, and disconnected when the work ends. Always-on remote access tools are prohibited on SCADA systems. (AC-17; MA-4; PR.AA-05)
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT and the SCADA and Automation Supervisor must disable all access, including SCADA local accounts, **the same business day**, or immediately for involuntary terminations. Contractor access must end on the contract end date. (PS-4; AC-2)
4.6 Managers must review their staff's access every quarter. The SCADA and Automation Supervisor must review all SCADA and controller accounts every quarter. (AC-2; AC-6)
4.7 Corporate accounts lock after 10 failed sign-in attempts, and corporate workstations lock after 10 minutes idle. OCC HMIs are exempt from screen lock so alarms stay visible; the OCC must remain badge-controlled and staffed. Field office HMIs must lock after 15 minutes idle. (AC-7; AC-11; PR.AA-03)
4.8 **Emergency access.** Two break-glass administrator accounts for the identity provider and cloud tenant, and one for the SCADA servers, must exist, sealed and stored offline, tested quarterly, and used only when normal access is unavailable. Any use is reviewed by the IT Manager. (AC-2)
4.9 Passwords must be at least 14 characters and must not appear on the banned-password list. Default passwords on any device (modems, radios, controllers, drives, network equipment) must be changed before the device is connected. Shared credentials must be changed when anyone who knows them leaves. (IA-5; PR.AA-01)
4.10 **IT/OT boundary.** The SCADA network must connect to the corporate network and the cloud only through the OT DMZ, with rules approved by the SCADA and Automation Supervisor. Devices may not be connected to both networks at once. No field device may have a management interface reachable from the internet. (SC-7; AC-4; PR.IR-01)
4.11 Physical access to the OCC and server rooms is by badge. Keys and gate combinations for field sites must be logged and changed when a holder leaves, and gate combinations at least quarterly. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT remote access procedure (due 2026-12-31); P02 control statements AC-2, AC-17, IA-2, MA-4, SC-7
