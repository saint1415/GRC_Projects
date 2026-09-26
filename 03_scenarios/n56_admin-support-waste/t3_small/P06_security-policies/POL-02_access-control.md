# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-12, IA-2, IA-2(1), IA-2(2), IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Legal drivers | 8 CFR 274a.2(b)(4), (g)(1)(i); E-Verify MOU Art. II.A.3, II.A.15; 15 U.S.C. 1681b(b)(1)(A)(ii); Fla. Stat. 501.171(2) |

## 1. Purpose
Make sure only authorized people can reach candidate, associate, and client information, and only to the extent their job requires.

## 2. Scope
All workforce members and every system in the APATP boundary, including vendor systems the firm configures (ATS, payroll, timekeeping, E-Verify, screening provider portal, AI add-on) and the cloud tenant.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Branch Managers, Payroll Manager, Director of Recruiting | Request and approve access for their staff; complete quarterly access reviews |
| HR and Compliance Manager | Opens onboarding, transfer, and termination tickets the same day; approves access to I-9, E-Verify, and background check records |
| IT Manager | Provisions and removes access; runs the identity provider |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including E-Verify logins and lobby kiosks used by staff. Sharing a password is a sanctionable offense (POL-01 4.7). (IA-2; AC-2; E-Verify MOU Art. II.A.15)
4.2 Access must be role-based, least-privilege, and approved by the user's manager. **Form I-9 records, document images, and E-Verify results** are limited to Onboarding and Compliance Specialists and the HR and Compliance Manager (8 CFR 274a.2(g)(1)(i)). **Consumer reports** are limited to the same roles and the hiring decision-maker for that candidate. Full SSNs and bank account numbers are limited to payroll roles. (AC-3; AC-6; PR.AA-05)
4.3 All systems holding personal information must use single sign-on with MFA through the identity provider where the vendor supports it. SMS codes are not allowed for systems that can pay money or export SSNs. Administrators must use number-matching push MFA now and phishing-resistant keys from 2027. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable access **the same business day** in every system on the checklist, including the payroll platform and **E-Verify** (MOU Art. II.A.3), or immediately for involuntary terminations. (PS-4; AC-2)
4.5 Managers must review their staff's access every quarter. The HR and Compliance Manager reviews E-Verify users monthly against the HR roster. (AC-2)
4.6 **Separation of duties in payroll.** The person who changes an associate's bank account may not approve the payroll that pays it. Bank changes require a call-back to the phone number on file, and new accounts are held for one payroll cycle before large payments. Bank changes are never accepted by email or text. (AC-5; PR.AA-02)
4.7 Accounts lock after 10 failed sign-in attempts. Laptops lock after 10 minutes idle, and SaaS sessions end after 30 minutes idle. Kiosks reset the session after each applicant. (AC-7; AC-11; AC-12)
4.8 Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. (AC-2)
4.9 Passwords must be at least 14 characters and must not appear on the banned-password list. Integration service credentials are kept in the cloud secrets service and rotated at least annually and after any staff change in IT. (IA-5)
4.10 Managed IT provider and vendor support access must use named accounts with MFA, approved sessions only. (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; access review procedure; P02 control statements AC-2, AC-3, AC-5, IA-2
