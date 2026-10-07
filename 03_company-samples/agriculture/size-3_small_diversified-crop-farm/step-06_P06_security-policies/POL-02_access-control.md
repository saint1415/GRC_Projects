# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations and Technology Manager |
| Approved by | Majority owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, AC-18, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PE-3 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| Other requirements | 20 CFR 655.122(j)(1); 21 CFR 112.161(a)(4); Fla. Stat. 501.171(2); NIST SP 800-82 Rev. 3 sections 6.2.1 and 6.2.10 |
| Languages | Issued in English; a Spanish summary is given to all field staff |

## 1. Purpose
Make sure only authorized people can reach farm systems and data, only to the extent their job requires, and that every record and every change to irrigation settings can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (owners, year-round and seasonal employees including H-2A workers, and contractors such as the MSP and the irrigation integrator when they work on farm systems) at the Home Block and the North Block. Covers all farm systems and data, including the irrigation, pump, fertigation, and cooler operational technology (OT) and the systems vendors operate for the farm.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Farm Manager and Office and HR Manager | Request and approve access for their staff; complete access reviews |
| Office and HR Manager | Starts the departure checklist on or before each worker's last day |
| Operations and Technology Manager | Provisions and removes access; runs the identity provider and the remote access jump host |
| Irrigation Technician | Approves each integrator remote session |
| Workforce | Protect passwords and PINs; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including crew leads on harvest tablets and operators on the HMI. Shared or generic accounts are prohibited. Where a device cannot support named accounts, the security lead must approve a documented exception with compensating controls (for example, a locked room and a sign-in sheet). (IA-2; AC-2; PR.AA-01; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1))
4.2 Access must be role-based and least-privilege, and approved by the user's manager before it is granted. Only manager roles may change irrigation schedules. Personnel, payroll, and H-2A files are limited to the Office and HR Manager and the majority owner. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, files, the identity provider, the farm management platform (web and mobile), the cloud console, the equipment dealer portal, and any remote access into farm networks. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Departures.** The Office and HR Manager must start the departure checklist on or before a worker's last day, and access must be removed **the same business day**. At the end of each season, all seasonal accounts must be disabled within 2 business days of the last workday. (PS-4; AC-2)
4.5 Managers must review their staff's access at the end of each season and every quarter. (AC-2; AC-6; PR.AA-05)
4.6 **Remote access to OT.** No supplier may have always-on access to the HMI, PLC, or pivot controls. Each integrator session must be requested, approved by the Irrigation Technician, run through the farm's jump host with a named account and MFA, and logged. The session must be ended when the work is done. (AC-17; MA-4; IA-8; DE.CM-06)
4.7 Equipment dealer access to the telematics account must be granted per service request and removed afterwards. (AC-2; SA-9)
4.8 Default passwords must be changed before any device is connected, including gateways, modems, cameras, and controllers. Passwords must be at least 12 characters, not on the banned-password list, and kept in the farm password manager, not on paper in panels. (IA-5)
4.9 Accounts lock after 10 failed sign-in attempts. Office computers and tablets lock after 10 minutes idle. The HMI may stay unlocked while the pump house is locked and staffed operators use named accounts. (AC-7; AC-11)
4.10 **Emergency access.** Two break-glass administrator accounts must exist for the identity provider and the cloud tenant, stored sealed and offline, tested quarterly, and used only when normal sign-in fails. Any use is reviewed by the security lead. (AC-2)
4.11 Pump-house, chemical storage, and pivot panels must be locked. Keys are issued from the key list kept by the Farm Manager. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.9. Consequences range from retraining to termination, depending on intent and harm, and are applied the same way to every worker regardless of visa status. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner and General Manager for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; departure checklist; remote access procedure; P02 control statements AC-2, AC-17, IA-2, MA-4
