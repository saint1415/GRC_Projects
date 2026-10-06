# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and its subsidiaries |
| Policy ID | POL-02 |
| Owner | Security Manager |
| Approved by | CEO |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 access control policy) |
| Review cycle | Annually (next review 2027-09-30), and after an acquisition, a major change, or an incident |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, DE.CM-06 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(c)(1), (c)(5) |
| HIPAA (group health plan) | 45 CFR 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |
| Supporting standards | STD-04 Privileged access and identity; STD-06 Authenticator |

## 1. Purpose
Make sure only authorized people can reach group, employee, customer, and plan information, and only to the extent their job requires. One directory and one identity provider serve every company in the group, so a weakness here affects all of them.

## 2. Scope
All workforce members, contractors, and service providers who access any group system, including subsidiary line-of-business systems, plant systems, and systems of acquired companies from the day they connect.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Subsidiary Presidents and department heads | Request and approve access for their staff; complete quarterly access reviews |
| VP of Human Resources | Records hires, transfers, and terminations in the HRIS the same day, for every employer in the group |
| Security Manager | Owns identity and privileged access standards; approves administrator access; runs reviews |
| VP of Information Technology | Provisions and removes access; runs the directory and service desk |
| Data owners (Finance President, Benefits Manager, Treasurer, Controller) | Approve every access to Finance customer information, plan PHI, treasury, and the ERP |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on counter, dispatch, and plant computers. Any exception needs compensating controls approved under POL-01 4.7. (IA-2; AC-2; 314.4(c)(1)(i); 164.312(a)(2)(i))
4.2 Every system that supports it must use the group single sign-on. A new system that cannot must be approved as an exception, and its accounts must be reviewed monthly. (AC-2; IA-2; PR.AA-01)
4.3 Access must be role-based, least-privilege, and approved by the user's manager. Access to another subsidiary's data needs that subsidiary President's approval. Access to Finance customer information needs the Finance President's approval. **Access to plan PHI is limited to the Benefits Manager, the Benefits Analyst, and the VP of Human Resources for plan administration only, as the plan documents describe** (45 CFR 164.504(f)(2)(iii)). (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii); 164.308(a)(4))
4.4 MFA is required for every user on every system that supports it, including service providers' staff and directory administration. Administrators and users in treasury, payables, HR, benefits, and Finance must use phishing-resistant security keys (by 2027-03-31). Only the Qualified Individual may approve an alternative, in writing. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; 314.4(c)(5); 164.312(d))
4.5 **Privileged access.** Administrators must use separate administrator accounts. No more than 2 people may hold standing global administrator rights in the identity provider. Directory administration follows the tier model in STD-04: Tier 0 accounts (domain controllers, identity synchronization) are used only from dedicated admin workstations through the privileged access broker. Service accounts may not be members of Domain Admins. Two break-glass accounts per critical system must be sealed offline and tested quarterly. (AC-6(2); AC-6(5); AC-2; PR.AA-05)
4.6 Service account and integration secrets (including the ACH signing account) must be stored in the secrets service, rotated at least yearly and whenever someone with access leaves, and never written in documents or tickets. (IA-5; AC-6)
4.7 **Termination.** HR must record a termination in the HRIS on or before the last day. IT must disable all access, including subsidiary systems, bank tokens, and badges, **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2; 314.4(c)(1); 164.308(a)(3)(ii)(C))
4.8 **Transfers.** When an employee moves between subsidiaries or roles, access to the former role must be removed within 5 business days. (PS-5; AC-2)
4.9 Managers must review their staff's access to Tier 1 systems (ERP, treasury, HRIS, loan servicing, directory, cloud, benefits site) every quarter. The Security Manager must review administrator roles, service accounts, and collaboration site permissions every quarter. (AC-2; AC-6; PR.AA-05; 164.308(a)(4)(ii)(C))
4.10 Remote access to group systems is allowed only from managed devices through the identity provider or the VPN, except email and files on a phone with the approved app. (AC-17; PR.AA-05)
4.11 **Vendor remote access.** Vendors (including machine vendors and IT providers) may connect only through the privileged access broker, on request, with time-limited sessions that are recorded. Always-on remote access tools are prohibited. (MA-4; AC-17; DE.CM-06)
4.12 Passwords must be at least 14 characters and not on the banned-password list. The service desk must verify identity with a video check and a callback to the manager's number on file before resetting MFA, and may not reset MFA for administrators by phone. (IA-5; PR.AA-02; 164.308(a)(5)(ii)(D))
4.13 Accounts lock after 10 failed sign-in attempts. Computers lock after 15 minutes idle, counter and dispatch PCs after 10 minutes, and tablets after 5 minutes. (AC-7; AC-11; 164.312(a)(2)(iii))
4.14 Segregation of duties must be kept in the ERP (vendor master separate from payment release) and the treasury system (a second approver for every payment). (AC-5; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the right level under POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; access review procedure; P02 control statements AC-2, AC-6, IA-2(1), IA-5
