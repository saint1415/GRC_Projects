# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Practice Administrator |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, IA-2, IA-2(1), IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |

## 1. Purpose
Make sure only authorized people can reach patient and practice information, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, students, and volunteers) at Clinic A and Clinic B. Covers all systems and data, including systems that business associates operate for the practice. It applies to electronic protected health information (ePHI) and all other practice information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Clinic Managers and Billing Manager | Request and approve access for their staff; complete quarterly access reviews |
| HR and Payroll Specialist | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on medical device workstations. Documented exceptions must have compensating controls. (IA-2; AC-2; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 MFA is required for all access to email, the EHR, the identity provider, remote access, and cloud administration. Administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03; 164.312(d))
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable the user's access **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2; 164.308(a)(3)(ii)(C))
4.5 Managers must review their staff's EHR roles and identity provider access every quarter. The Billing Manager must also review EHR report and export rights. (AC-2; AC-6)
4.6 Accounts lock after 10 failed sign-in attempts. Workstations lock after 10 minutes idle, and EHR sessions end after 15 minutes idle. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))
4.7 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. Any use is reviewed by the Security Officer. (AC-2; 164.312(a)(2)(ii))
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords must be unique per device and managed by the IT tool. (IA-5; 164.308(a)(5)(ii)(D))
4.9 Vendor and MSP remote access must use named accounts with MFA and be restricted to approved sources. (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, IA-2
