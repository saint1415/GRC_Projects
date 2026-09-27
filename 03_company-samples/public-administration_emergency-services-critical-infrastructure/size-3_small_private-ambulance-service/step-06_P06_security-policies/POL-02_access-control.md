# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, AC-17, AC-19, IA-2, IA-2(1), IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.310(c); 164.312(a), (d) |

## 1. Purpose
Make sure only authorized people can reach patient and dispatch information, only to the extent their job requires, and that every action can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, students on clinical rotations, and ride-along observers) at headquarters, Station 2, and in company ambulances. Covers all systems and data, including systems that business associates operate for the company. It applies to electronic protected health information (ePHI), dispatch data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Communications Center Supervisor, Operations Manager, Billing and Compliance Manager | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and departure tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider and CAD accounts |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account in every system, including CAD at dispatch consoles and on mobile data computers. Shared, position, or per-vehicle accounts are prohibited. Any temporary exception must be approved under POL-01 4.6 and have a compensating control. (IA-2; AC-2; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 MFA is required for all access to email, the ePCR, billing, the identity provider, CAD administration, remote access, and cloud administration. Administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03; 164.312(d))
4.4 **Departures.** HR must open a departure ticket on or before the last day. IT must disable the user's access in every system **the same business day**, or immediately for involuntary departures. (PS-4; AC-2; 164.308(a)(3)(ii)(C))
4.5 Managers must review their staff's CAD, ePCR, and identity provider access every quarter. The Billing and Compliance Manager must also review who can edit billed service levels. (AC-2; AC-6)
4.6 Accounts must lock after 10 failed sign-in attempts. Office workstations must lock after 10 minutes idle, ePCR sessions must end after 15 minutes idle, and mobile data computers must require crew sign-in at shift start. Dispatch consoles are exempt from idle lock because dispatchers must see live calls; they must stay inside the badge-controlled dispatch room. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))
4.7 **Emergency access.** Two break-glass administrator accounts and a sealed CAD administrator credential must exist, stored offline, tested quarterly, and used only when the identity provider or the MSP is unavailable. Any use must be reviewed by the Security Officer. (AC-2; 164.312(a)(2)(ii))
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords and device passwords (including vehicle routers) must be unique per device and must never be left at the manufacturer default. (IA-5; 164.308(a)(5)(ii)(D))
4.9 Vendor and MSP remote access must use named accounts with MFA and be restricted to approved sources. (AC-17; IA-2(1))
4.10 Mobile data computers and ePCR tablets must be enrolled in device management with encryption and remote wipe before use in an ambulance. (AC-19)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, IA-2
