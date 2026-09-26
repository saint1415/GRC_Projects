# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC and its subsidiaries |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | CEO |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after an acquisition, a major change, or an incident |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(c)(1), (c)(5) |

## 1. Purpose
Make sure only authorized people can reach group, employee, and customer information, and only to the extent their job requires. Because one identity system serves every company in the group, a weakness here affects all of them.

## 2. Scope
All workforce members (owners, managers, employees, contractors, and temporary staff) of Cris Santos Company, LLC and each subsidiary, at every site and when working remotely. Covers all systems and data the group owns or uses, including the Shared Corporate Services Platform, each subsidiary's own systems, and systems that service providers run for the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Subsidiary Presidents and department heads | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Records hires, transfers, and terminations in the HRIS the same day |
| IT Manager | Provisions and removes access; runs the identity provider; approves administrator access |
| Finance President | Approves every access to Finance customer information |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on counter and dispatch computers. Any exception needs compensating controls approved under POL-01 4.7. (IA-2; AC-2; 314.4(c)(1)(i))
4.2 Every system that supports it must use the group single sign-on. A new system that cannot must be approved as an exception. (AC-2; IA-2; PR.AA-01)
4.3 Access must be role-based, least-privilege, and approved by the user's manager. Access to another subsidiary's data requires approval from that subsidiary's President. Access to Finance customer information requires the Finance President's approval. (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))
4.4 MFA is required for every user on every system that supports it, including service providers' staff. Administrators and users in payables, treasury, HR, and Finance must use phishing-resistant hardware security keys. Only the Qualified Individual may approve an alternative, in writing. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))
4.5 No more than 2 people may hold standing global administrator rights. MSP staff must request time-limited elevation for each task. Two break-glass accounts must be stored sealed and offline, tested quarterly, and used only when single sign-on fails. (AC-6(5); AC-2)
4.6 **Termination.** HR must record a termination in the HRIS on or before the last day. IT must disable all access, including subsidiary systems and bank tokens, **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2; 314.4(c)(1))
4.7 **Transfers.** When an employee moves between subsidiaries or roles, access to the former role must be removed within 5 business days. (AC-2)
4.8 Managers must review their staff's access every quarter. The IT Manager must review collaboration site permissions and administrator roles every quarter. (AC-2; AC-6; PR.AA-05)
4.9 Remote access to group systems is allowed only from managed devices, except email and files on a phone with the approved app. (AC-17)
4.10 Passwords must be at least 12 characters and must not appear on the banned-password list. The help desk must verify identity by calling back the employee's manager and a video check before resetting MFA; the MSP may not reset MFA. (IA-5)
4.11 Accounts lock after 10 failed sign-in attempts. Computers lock after 15 minutes idle; tablets after 5 minutes. (AC-7; AC-11)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the right level under POL-01 4.5, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, IA-2(1)
