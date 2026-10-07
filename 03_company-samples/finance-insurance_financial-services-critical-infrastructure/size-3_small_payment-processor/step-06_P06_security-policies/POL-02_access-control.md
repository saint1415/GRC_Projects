# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after significant changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| PCI DSS v4.0.1 | Requirements 7 and 8 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(1), (c)(5) |

## 1. Purpose
Make sure only authorized people and processes can reach company systems and data, with the least access they need. Authentication must be strong enough to protect cardholder data and merchant funds.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) and all accounts on company systems. That includes workforce accounts, merchant portal users (customer users), cloud IAM roles, service and application accounts, API keys, and repository tokens.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns this policy; runs the identity provider; leads access reviews |
| Platform Engineering Lead | Cloud IAM roles, service accounts, secrets, repository tokens |
| CTO | Merchant portal authentication design |
| Managers and data owners | Approve access for their staff and systems; confirm it in reviews |
| HR Manager | Sends hire, transfer, and termination notices the same day |
| Merchant Support Manager | Verifies merchant identity before any account change requested by phone |

## 4. Policy statements
4.1 Every user must have a unique ID. Shared or generic accounts are prohibited, except the two break-glass cloud accounts. Those must be stored offline, used only in emergencies, and reviewed after every use. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1, 8.2.2)

4.2 Access must be granted by job need and least privilege, approved by the manager and the system owner, and recorded. (AC-6; AC-2; PR.AA-05; PCI DSS 7.2.1, 7.2.2; 16 CFR 314.4(c)(1))

4.3 **Workforce MFA.** All workforce access to company systems must use single sign-on with MFA. Two further rules apply:
- Administrators and all access into the CDE must use phishing-resistant authenticators (hardware keys).
- Push-based MFA must use number matching.

(IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4.1, 8.4.2, 8.4.3; 16 CFR 314.4(c)(5))

4.4 **Merchant portal users.** MFA is required for merchant users who can:
- issue refunds
- change funding bank accounts
- use the virtual terminal
- administer users

Every other merchant user must either use MFA, or be covered by dynamic risk analysis of their account's security posture. The Qualified Individual must approve that alternative in writing. (IA-8; IA-5; PR.AA-03; PCI DSS 8.3.10.1; 16 CFR 314.4(c)(5))

4.5 **Termination.** All access must be removed by the end of the last working day: single sign-on, repository tokens, API keys, cloud roles, and SaaS local accounts. For involuntary terminations, access must be removed immediately. Contractor accounts must carry an end date. (PS-4; AC-2; PR.AA-05; PCI DSS 8.2.5)

4.6 Accounts inactive for 90 days must be disabled automatically or by review. (AC-2; PCI DSS 8.2.6)

4.7 **Access reviews:**
- User access to the CDE and privileged roles: at least every six months.
- Application and system accounts: at least every six months (frequency set by the targeted risk analysis required by POL-01 4.4).
- All accounts reconciled to the HR roster every quarter.

Managers must confirm or remove each access, and the review must be recorded. (AC-2; AC-6(5); PR.AA-05; PCI DSS 7.2.4, 7.2.5.1)

4.8 **Service and application accounts:**
- Each must have a named owner and be scoped to one workload.
- None may hold administrator-level roles without COO approval.
- Their secrets must be stored in the secrets service, never in code, and rotated as the targeted risk analysis sets.

(IA-5; AC-6(5); PR.AA-05; PCI DSS 7.2.5, 8.6.1, 8.6.2, 8.6.3)

4.9 Repository and pipeline tokens must be tied to single sign-on and expire within 30 days. Long-lived personal access tokens are prohibited. (IA-5; PCI DSS 8.6.3)

4.10 Administrative access to the CDE must pass only through the bastion. Sessions must be logged and sent to the SIEM. (AC-17; AU-12; PCI DSS 8.4.2)

4.11 **Passwords and sessions:**
- Passwords at least 12 characters with letters and numbers.
- Lockout after no more than 10 failed attempts, for at least 30 minutes.
- Re-authentication after 15 minutes idle.

(IA-5; AC-7; AC-11; PCI DSS 8.3.4, 8.3.6, 8.2.8)

4.12 **Funding bank account changes.** A change to a merchant's funding bank account needs step-up MFA in the portal, or a call-back to the phone number on file when requested through support. A 3-business-day hold with notice to the merchant applies before the first funding to the new account. (AC-3; IA-2; PR.AA-03; 16 CFR 314.4(c)(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.14. Compliance is checked through the access reviews (4.7), the quarterly reviews in POL-01 4.7, and the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.13. They must be written, risk-rated, approved by the policy owner (or by the majority owner and CEO for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; System Security Plan (P02); PCI DSS Requirements 7 and 8; 16 CFR 314.4(c)
