# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-07 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | 21 CFR 121.135(a), 121.305(f); 9 CFR 417.5(b); NIST SP 800-82 Rev. 3 (benchmark) |

## 1. Purpose
Make sure only authorized people can reach company systems and process controls, only to the extent their job requires, and that every change to a process or a food safety record can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary and agency workers, and contractors) at the Florida plant and outlet store. Covers all systems and data, including process control systems, cloud and SaaS services, and systems that vendors operate or maintain for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Line supervisors and department managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day, including for agency workers |
| IT Manager | Provisions and removes business and cloud access; runs the identity provider and remote access gateway |
| Controls Engineer | Provisions and removes OT access; approves engineering access |
| Workforce | Protect credentials and badges; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including on HMIs, SCADA, the recipe system, and the food safety records application. Shared or generic accounts are prohibited except documented operator view-only accounts that cannot change setpoints or formulations. (IA-2; AC-2; PR.AA-01; 9 CFR 417.5(b); 21 CFR 121.305(f))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Write access to PLC programs is limited to the Controls Engineer and named integrator staff during approved sessions. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 **Formulations and critical setpoints.** Changes to cure, brine, or other formulations, and to CCP and CIP setpoint ranges, require two people: a batching supervisor to propose and the FSQA Manager to approve. (AC-5; 21 CFR 121.135(a))
4.4 MFA is required for email, the identity provider, cloud administration, the records application, the IT VPN, and **all remote access to OT**. Cloud administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03)
4.5 **OT remote access.** Vendors and staff may reach OT only through the company's OT remote access gateway, with a named account, MFA, a session approved for a stated purpose and time window, and session recording. Always-on VPN accounts and modems are prohibited. (AC-17; MA-4; PR.AA-05)
4.6 **Termination.** HR must open a termination ticket on or before the last day. IT must disable business access the same business day, or immediately for involuntary terminations. The Controls Engineer must remove OT access the same day and, until shared accounts are eliminated, rotate any shared OT password the person knew. (PS-4; AC-2)
4.7 Managers must review their staff's access every quarter. The Controls Engineer must review OT accounts and vendor access every quarter. (AC-2; AC-6)
4.8 Passwords must be at least 14 characters and not on the banned list. Default passwords on every device, including controllers, sensors, and gateways, must be changed before the device is connected. (IA-5)
4.9 Accounts in the identity provider lock after 10 failed sign-in attempts. HMIs do not lock out operators, because lockout during a process upset is a safety risk; HMIs must instead be physically protected and use short-time badge or PIN sign-in. (AC-7; PE-3)
4.10 **Physical access.** Badge access is required to enter the plant. The cure and ingredient room, server room, engine room, and seafood room ingredient area are restricted to named roles. Visitors must sign in and be escorted in production areas. Keys to restricted areas must be logged and changed when a key holder leaves. (PE-3; PR.AA-06; 21 CFR 121.135(a))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.9). Compliance is checked through the annual control assessment (P07) and the quarterly access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT remote access procedure; P02 control statements AC-2, AC-17, IA-2; food defense plan
