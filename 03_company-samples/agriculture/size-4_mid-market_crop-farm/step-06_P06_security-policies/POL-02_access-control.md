# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, AC-19, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, IA-8, MA-4, PE-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| Other requirements | 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1)-(2); Fla. Stat. 501.171(2); NIST SP 800-82 Rev. 3 sections 6.2.1 and 6.2.10 |
| Languages | Issued in English; a Spanish summary is given to crew leads and Irrigation Technicians |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 OT security standard |

## 1. Purpose
Make sure only authorized people and systems can reach company systems and data, only to the extent their job requires, and that every record, every settlement change, and every change to irrigation, fertigation, ripening, or cold storage settings can be traced to a person.

## 2. Scope
All workforce members, contract growers using the grower portal, vendors, and service accounts with access to company systems at every site and in every cloud and SaaS service. It includes crew lead tablets, SCADA and HMI accounts, PLC programming access, the pivot manufacturer's cloud service, the equipment dealer's telematics portal, and vendor remote support.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers (Farm Managers, Packinghouse Manager, department heads) | Request and approve access; complete quarterly access reviews for their staff |
| System owners (FMIS, SCADA, ERP, grower portal, cloud) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations (including seasonal end dates) in the HR system on or before the effective date |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager | Runs privileged access management and the vendor access broker; reviews privileged and vendor activity |
| Director of Irrigation and Water Resources; Packinghouse Manager | Approve each vendor session to OT; keep OT account lists and keys |
| Workforce | Protect passwords and PINs; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including crew leads on harvest tablets, SCADA operators and engineers, and vendor technicians. Shared or generic accounts are prohibited. Where an OT device cannot support named accounts (for example, legacy HMIs), the OT control owner must document an exception with compensating controls: named operator PINs, a staffed or locked room, and network isolation (SP 800-82 Rev. 3 section 6.2.1). (IA-2; AC-2; PR.AA-01; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1))
4.2 **Crew tablets.** Crew leads must sign in to SYS-01 with their own account and a device PIN on managed tablets in kiosk mode. Tally entries made under another person's sign-in are a policy violation. (IA-2; AC-19)
4.3 Access must be role-based and least-privilege and approved by the user's manager and the system owner before it is granted. Only irrigation operator roles may change irrigation schedules and setpoints; only settlement analyst roles may run settlements, and no one may approve their own settlement run. Personnel, payroll, and H-2A files are limited to HR and payroll staff. (AC-2; AC-3; AC-5; AC-6; PR.AA-05)
4.4 MFA is required for all workforce access to company systems through the identity provider, for remote access, and for every administrator. Administrators must use phishing-resistant authenticators by 2027-03-31. Grower portal users who can view settlements or change bank details must use MFA by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); IA-8; PR.AA-03)
4.5 **Departures.** HR must record the termination on or before the last day. Identity provider access is disabled automatically that day, or immediately for involuntary terminations. SYS-01 mobile accounts, SCADA and HMI accounts, badges, and pump-station keys must be removed within 24 hours. At the end of each season, all seasonal accounts must be disabled within 2 business days of the last workday. (PS-4; AC-2; AC-2(3))
4.6 **Transfers.** Access from the prior role, including SYS-01 farm permissions, must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.7 **Access reviews.** Managers must review their staff's access to SYS-01, the identity provider groups, the ERP, the grower portal staff console, and SCADA every quarter. System owners must review privileged, export, and settlement rights every quarter. (AC-2; AC-6; PR.AA-05)
4.8 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through the privileged access management service, with sessions logged. This applies to the directory, SYS-01, the ERP, the cloud, and SCADA engineering. No vendor or service account may hold standing administrator rights. (AC-6(2); AC-6(5); PR.AA-05)
4.9 **Vendor remote access to OT and systems.** No vendor may have always-on access. Each session by the SCADA integrator, pivot manufacturer, refrigeration contractor, equipment dealer, or development firm must be requested, approved by the system owner, run through the company's access broker with a named account and MFA, recorded, and ended when the work is complete. Remote access tools installed by vendors on company systems are prohibited. (AC-17; MA-4; DE.CM-06; SP 800-82 Rev. 3 section 6.2.10)
4.10 Default credentials must be changed before any device connects to a company network, including controllers, gateways, modems, cameras, and time clocks. Passwords must be at least 14 characters and not on the banned-password list. OT and service account credentials must be stored in the company password vault, never on paper in panels, and rotated when anyone with knowledge of them leaves. (IA-5)
4.11 Accounts lock after 10 failed sign-in attempts. Laptops and tablets lock after 10 minutes idle. HMIs in the IOC and packinghouse control room may stay unlocked while the room is staffed. (AC-7; AC-11)
4.12 **Emergency access.** Break-glass accounts must exist for the identity provider, the cloud organization, SYS-01 administration, and SCADA, stored sealed and offline, tested quarterly, and used only when normal access fails. Every use is reviewed by the Security Manager within 1 business day. (AC-2)
4.13 **Physical access to OT.** The IOC, server rooms, and packinghouse control room require badges. Pump stations, fertigation skids, and chemical storage must be locked with restricted keys issued from the key list; control panel doors must be closed and locked when unattended. (PE-3; PR.AA-06)
4.14 Bank detail changes for growers, vendors, or workers must be confirmed by a call to the number on file, never a number in the request, and portal bank changes are held 48 hours. (IA-8; PR.AA-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. OT exceptions under 4.1 must list the compensating controls and be reviewed every 12 months.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5, MA-4; P07 findings for AC-02, AC-06, AC-17, IA-05, MA-04, PE-03, PS-04
