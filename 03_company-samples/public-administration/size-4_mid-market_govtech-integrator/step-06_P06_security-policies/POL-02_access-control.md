# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of Information Security |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-7, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| Agency requirements | CJISSECPOL v6.1 AC-2(3), AC-7, IA-2, PS-4, PS-5; Pub. 1075 sec. 4 AC-2, AC-7; 42 CFR 431.306(b); 18 U.S.C. 2721(a) |
| Supporting standards | STD-04 Remote administration of agency systems; STD-06 Authenticator and privileged access |

## 1. Purpose
Ensure only authorized people and systems can reach company systems, agency tenants, and agency-hosted systems, with the least privilege needed and only for as long as it is needed.

## 2. Scope
All workforce members and all accounts (workforce, administrator, service, and break-glass) on company systems, the ACMC, and agency systems the company administers through managed services. Agency user accounts in the ACMC are managed by each agency; this policy covers how the company configures and protects them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Information Security | Owns this policy; runs quarterly access reviews; approves privileged roles |
| Director of Cloud Operations | Operates privileged access to the landing zone and the FTI enclave |
| Director of Managed Services | Operates privileged access to agency-hosted systems through the vaulted path |
| HR Director | Sends hires, transfers, and terminations to the identity provider the same day |
| Managers and project leads | Approve access for their staff; request removal at project close |
| Agency administrators | Approve and remove their own users (complementary agency control) |

## 4. Policy statements
4.1 Every user has a unique account provisioned from the HR system. Shared accounts are not allowed, except agency-owned accounts on agency systems that the agency requires, which must be vaulted and rotated when anyone who knows them leaves. (AC-2; IA-5; PR.AA-01)
4.2 Access to agency tenants and agency systems is granted only for an assigned ticket, project, or support role, and removed at project close, within 24 hours of transfer, and within 24 hours of termination, including agency-side accounts on managed systems. Accounts that expire, lose their owner, violate policy, or sit inactive for 90 days are disabled within 1 week. (AC-2; AC-2(3); AC-6; PS-4; PS-5; PR.AA-05)
4.3 Multi-factor authentication is required for every account. By 2027-01-31, phishing-resistant authenticators are required for administrators and for anyone with access to regulated data or agency systems. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **No standing administrator rights.** Administrator rights in the ACMC are granted just in time with approval and a time limit. Credentials for agency systems are held in the credential vault, released per session, and rotated after use. (AC-6; AC-6(5); IA-5)
4.5 Access to regulated tenants (FTI, CJI, benefits, motor vehicle) and to agency systems is reviewed every quarter by the data owner's delegate; other access is reviewed every year. Reviews remove access not confirmed. (AC-2; PR.AA-05)
4.6 **Lockout.** Accounts that can reach CJI lock after 5 consecutive failed attempts in 15 minutes and are released by an administrator. Roles that can reach the FTI enclave lock after 3 failed attempts in 120 minutes. (AC-7)
4.7 **Remote administration.** ACMC administration is allowed only through the privileged access gateway. Administration of agency systems is allowed only through the vaulted managed services path with session recording (STD-04). No other path may connect the managed services platform to the landing zone. (AC-17; MA-4; PR.IR-01)
4.8 Secrets (passwords, keys, tokens, certificates) are stored only in the secrets manager or credential vault, never in code, wikis, tickets, chat, or email, and are rotated at least every 90 days and after any suspected exposure. (IA-5)
4.9 Two break-glass accounts per account tier, including the FTI enclave and the managed services platform, are sealed, monitored, and tested each quarter. (AC-2)
4.10 Agency users sign in through their agency identity providers with MFA. Platform-local accounts for municipal tenants must use MFA by 2026-12-31. (IA-8)
4.11 **FTI enclave and regulated tenants.** Only members of the screened enclave administrator group may administer the FTI enclave. Support staff reach regulated tenants only through a ticket-scoped role. Access to regulated data is blocked from outside the United States. (AC-3; AC-6)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.8. Compliance is checked through quarterly access reviews, privileged access logs, and the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 statement 4.7. Statements 4.2 (24-hour removal for CJI and FTI access), 4.6, and 4.11 cannot be excepted without the affected agency's written agreement.

## 7. Related documents
POL-01; POL-04; STD-04; STD-06; CJIS Security Policy v6.1; IRS Publication 1075 section 4
