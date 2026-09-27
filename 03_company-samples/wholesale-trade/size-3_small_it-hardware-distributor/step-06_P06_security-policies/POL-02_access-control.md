# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-8, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-4, IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| SP 800-171 Rev. 2 | 3.1.1, 3.1.2, 3.1.5, 3.1.8 to 3.1.12, 3.1.15, 3.5.1 to 3.5.3, 3.5.6, 3.7.5, 3.9.2; FAR 52.204-21(b)(1)(i), (ii), (v), (vi) |

## 1. Purpose
Make sure only authorized people and devices can reach company information, especially CUI and FCI, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary warehouse staff, and contractors), the MSP, and reseller portal users. Covers all company systems, including the ERP, WMS and handhelds, the file server and CUI share, the reseller portal configuration, the identity provider, the cloud tenant, and endpoints.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| Configuration Lab Lead | Approves the CUI access list with the Chief Operating Officer |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| Systems Administrator | Provisions and removes access; runs the identity provider |
| IT Manager | Owns this policy; approves MSP remote sessions; reviews privileged access |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including the WMS zone accounts on handhelds. Any exception must be documented, approved under POL-01 4.6, and have compensating controls. (IA-2; AC-2; FAR 52.204-21(b)(1)(v))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. The ERP may have no more than 2 administrator accounts. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 **CUI access.** Only people on the CUI access list, approved by the Configuration Lab Lead and the Chief Operating Officer, may access the CUI share, the lab workstations, or CUI printouts. The list is reviewed quarterly. (AC-3; SP 800-171 3.1.1, 3.1.2)
4.4 MFA is required for email, the ERP, the VPN, the cloud console, the identity provider, the CUI share, and all administrator access. Administrators must use phishing-resistant hardware keys. Reseller portal users must use MFA from 2026-12-31. (IA-2(1); IA-2(2); PR.AA-03; SP 800-171 3.5.3)
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must disable access **the same business day**, or immediately for involuntary terminations. Lab staff must return badges, keys, and any CUI on a lab exit checklist. (PS-4; AC-2; SP 800-171 3.9.2)
4.6 Managers must review their staff's ERP roles, WMS roles, and identity provider groups every quarter. The IT Manager reviews all privileged accounts every quarter. (AC-2; AC-6)
4.7 Accounts lock after 10 failed sign-in attempts. Screens lock after 15 minutes idle on all endpoints, including lab workstations. Accounts unused for 90 days are disabled. (AC-7; AC-11; IA-4)
4.8 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. Any use is reviewed by the IT Manager. (AC-2)
4.9 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords must be unique per device and managed by the IT tool. (IA-5)
4.10 Administrators must use a separate privileged account for administrative work and their everyday account for email and browsing. Privileged activity is logged. (AC-6; AU-2)
4.11 **Remote and vendor access.** Remote access is allowed only through the company VPN with MFA. MSP access through its remote management tool requires named accounts with MFA, a written authorization that lists what the MSP may do, IT approval for each session, and a 30-minute idle timeout. (AC-17; MA-4; SP 800-171 3.1.15, 3.7.5)
4.12 Company systems must show a sign-in notice stating that use is monitored and that CUI must be handled under POL-04. (AC-8; SP 800-171 3.1.9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; account management and CUI access procedures (due 2026-11-30); P02 control statements AC-2, AC-3, IA-2, IA-2(2)
