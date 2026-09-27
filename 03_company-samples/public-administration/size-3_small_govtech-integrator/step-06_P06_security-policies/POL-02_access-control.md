# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Agency requirements | CJISSECPOL v6.1 AC-7, AC-11, IA-2(1)-(2), IA-5; Pub. 1075 section 4 AC and IA controls |

## 1. Purpose
Make sure only authorized people can reach agency data and company systems, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members, wherever they work. Covers the ACMP, the cloud accounts, and every service that administers them. It applies to workforce accounts, service accounts, and the platform-local accounts the company issues to agency users.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day; confirms screening before access to CJI or FTI |
| Cloud Operations Lead | Grants and removes cloud and platform administrative access |
| IT Manager | Runs the identity provider; reviews privileged access |
| Customer Support Manager | Approves ticket-linked support access to tenants |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every person must have a unique account. Shared or group accounts and shared credentials are prohibited. Service accounts must have a named owner. (IA-2; AC-2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Access to the AC-01 (FTI) and AC-02 (CJI) tenants additionally requires the conditions in POL-01 4.5. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all workforce access. Cloud and platform administrators must use phishing-resistant hardware keys. Platform-local agency accounts must use MFA. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.4 **Privileged access is temporary.** Administrator rights in production are granted just in time, for a stated task, and expire within 8 hours. Support access to a tenant must be tied to a ticket and expire when the ticket closes. (AC-6; AC-2)
4.5 **Termination and transfer.** HR must open a termination ticket on or before the last day, and IT must disable access **the same business day** (immediately for involuntary terminations). A transfer triggers a review of the person's access within 5 business days. (PS-4; PS-5; AC-2)
4.6 Managers must review their staff's access every quarter, including tenant access and administrator roles. Accounts inactive for 90 days are disabled. (AC-2)
4.7 Accounts lock after **5 failed sign-in attempts within 15 minutes** and stay locked until an administrator releases them, as the CJIS Security Policy requires. Laptops lock after 15 minutes idle and platform sessions after 30 minutes idle. (AC-7; AC-11; AC-12)
4.8 **Secrets.** API keys, certificates, and service credentials must be stored only in the secrets manager, never in code, pipeline variables, tickets, or chat. They are rotated at least every 90 days and immediately when someone with access leaves the team. (IA-5)
4.9 **Emergency access.** Two break-glass administrator accounts with hardware keys are kept sealed, tested quarterly, and used only when the identity provider is unavailable. Any use is reviewed by the IT Manager within 1 business day. (AC-2)
4.10 Remote administrative access must come from company-managed, compliant laptops and from inside the United States. (AC-17; AC-19)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through quarterly access reviews and the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They may not waive agency contract terms.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, IA-2, IA-5
