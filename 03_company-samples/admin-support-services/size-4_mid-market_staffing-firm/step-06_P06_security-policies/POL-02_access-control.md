# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Legal drivers | 8 CFR 274a.2(b)(4), (g)(1)(i); E-Verify MOU Art. II.A.3, II.A.15; 15 U.S.C. 1681b(b)(1)(A)(ii); 29 CFR 1630.14(b)(1), (c)(1); Fla. Stat. 501.171(2) |
| Supporting standards | STD-06 Authenticator and privileged access; STD-10 Payroll and bank-change controls |

## 1. Purpose
Make sure only authorized people can reach associate, candidate, clinician, and client information, only to the extent their job requires, and that no one can redirect pay without verification.

## 2. Scope
All workforce members, associates using self-service, client and supplier users, and every system in the APATP boundary, including vendor systems the firm configures (ATS, payroll, timekeeping, credentialing, VMS, E-Verify, screening provider portal, AI tools) and the cloud landing zone.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers (branch, on-site, department) | Request and approve access for their staff; complete quarterly access reviews |
| CHRO | Opens hire, transfer, and termination tickets the same day for internal staff |
| Director of Compliance and Privacy | Approves access to I-9, E-Verify, and consumer report records; reconciles E-Verify users monthly |
| Credentialing Manager | Approves access to clinician medical documents |
| Director of Payroll and Billing | Owns payroll roles and bank-change controls (STD-10) |
| IT Director | Provisions and removes access; runs the identity provider |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including E-Verify logins and staff use of kiosks. (IA-2; AC-2; E-Verify MOU Art. II.A.15)
4.2 Access must be role-based, least-privilege, and approved by the user's manager. These **restricted access groups** apply:
- **Form I-9 records, document images, and E-Verify results:** Onboarding and Compliance Specialists, compliance analysts, and the Director of Compliance and Privacy (8 CFR 274a.2(g)(1)(i)).
- **Consumer reports and drug test results:** the same roles and the hiring decision-maker for that candidate.
- **Clinician medical information** (immunizations, TB tests, physicals, fit tests, medical notes): credentialing specialists and the Credentialing Manager only; recruiters and clients see clearance status, not documents (29 CFR 1630.14(b)(1), (c)(1)).
- **Full SSNs and bank account numbers:** payroll roles only; reports and the data warehouse show the last 4 digits.
(AC-3; AC-6; PR.AA-05)
4.3 All staff systems holding personal information must use single sign-on with MFA through the identity provider where the vendor supports it. Payroll, billing, and administrator accounts must use phishing-resistant authenticators from 2027-03-31. SMS one-time codes are not allowed for any account that can change where pay is deposited, including associate accounts, after 2026-12-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03)
4.4 **Termination.** The CHRO (internal staff) or the branch (on-site staff) must open a termination ticket on or before the last day. IT must disable access **the same business day** in every system on the checklist, including E-Verify, the VMS, and the credentialing client portal, and immediately for involuntary terminations. (PS-4; AC-2; E-Verify MOU Art. II.A.3)
4.5 **Transfers.** Access for the prior role, including ATS branch assignments, must be removed within 5 business days of a transfer. (PS-5; AC-2)
4.6 **Reviews.** Managers must review their staff's access every quarter, including ATS roles. The Director of Compliance and Privacy reviews E-Verify users monthly against the HR roster. Client and supplier users in the client portal, credentialing client portal, and VMS are reviewed quarterly with each client's named contact. (AC-2; IA-8)
4.7 **Separation of duties in payroll.** The person who adds an associate or changes a pay rate may not approve the payroll register. New bank accounts entered by associates are verified by call-back or held for one payroll cycle before pay is deposited. Staff never accept bank changes by email, text, or an inbound call without call-back to the number on file (STD-10). (AC-5; PR.AA-02)
4.8 Accounts lock after 10 failed sign-in attempts (5 for associate accounts). Laptops lock after 10 minutes idle, SaaS sessions end after 30 minutes idle, and kiosks reset the session after each applicant. (AC-7; AC-11; AC-12)
4.9 Two break-glass administrator accounts per critical system must exist, sealed and stored offline, tested quarterly, and used only when the identity provider is unavailable. (AC-2)
4.10 **Service accounts and API keys** must be kept in the cloud secrets service, scoped to the job that uses them, rotated at least annually and after any change in the staff or contractors who could read them, and never stored in code, images, or documents. (IA-5; AC-6)
4.11 Administrators must use a separate administrator account and just-in-time elevation where the platform supports it. Standing administrator rights are reviewed quarterly. (AC-6(2); AC-6(5))
4.12 Remote and vendor access (the MSSP, the integration contractor, the timekeeping vendor) must use named accounts with MFA from managed devices or a monitored access path, with session approval for vendor maintenance. (AC-17; MA-4)
4.13 Client and supplier users must have a named owner at their organization and MFA where the system supports it. (IA-8)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 4.7. They must be written, risk-rated, approved at the risk acceptance level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; STD-06; STD-10; P02 control statements AC-2, AC-3, AC-5, IA-2, IA-5
