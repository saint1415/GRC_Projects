# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of Information Security |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after significant changes |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(5), AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PE-2, PE-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| PCI DSS v4.0.1 | 7.1 to 7.3, 8.1 to 8.6 (including 8.3.10.1), 9.2, 9.3 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(1), (c)(5) |
| Supporting standards | STD-04 Privileged access and service account standard |

## 1. Purpose
Make sure only authorized people and systems can reach company systems and data, with the least access they need, and that access ends when the need ends.

## 2. Scope
All workforce members, contractors, vendors, merchant and ISV portal users, and service accounts, on every platform: Cloud A, Cloud B, the colocation cages, and SaaS.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Information Security | Owns this policy and the access review program |
| IT Director | Runs the identity provider and the HR-driven provisioning |
| VP Platform Engineering and Director of Integrated Payments Engineering | Cloud IAM, PAM entitlements, and service accounts for their platforms |
| Managers and system owners | Approve access requests and complete access reviews |
| HR Director | Sends hires, transfers, and terminations to the identity provider the same day |

## 4. Policy statements
4.1 Every person must have a unique identity in the company identity provider. Shared and generic user accounts are prohibited. Break-glass accounts must be sealed, tested quarterly, and alert the MSSP when used. (IA-2; IA-4; PR.AA-01; PCI DSS 8.2.1, 8.2.2)

4.2 Access must be granted by job need and least privilege, from a documented role catalog for each platform, with manager and system owner approval. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2.1, 7.2.2; 16 CFR 314.4(c)(1))

4.3 All workforce users must use MFA. Administrators and anyone with access into a CDE must use phishing-resistant authenticators (security keys) and reach the CDE only through PAM. (IA-2(1); IA-2(2); AC-17; PR.AA-03; PCI DSS 8.4.1, 8.4.2, 8.4.3; 16 CFR 314.4(c)(5))

4.4 **Customer users.** On every merchant and partner portal, users with administrator, refund, funding account, or virtual terminal rights must use MFA. Other customer users who sign in with a password only must be covered by dynamic analysis of account security posture, approved in writing by the Qualified Individual as reasonably equivalent. (IA-8; IA-5; PR.AA-03; PCI DSS 8.3.10.1; 16 CFR 314.4(c)(5))

4.5 **Termination.** All access, including cloud access keys, API tokens, repository tokens, SaaS local accounts, PAM entitlements, and cage badges, must be removed by the end of the last working day. Contractor accounts must carry an end date. (PS-4; AC-2; PR.AA-05; PCI DSS 8.2.5)

4.6 **Transfers.** Prior roles must be removed within 5 business days of a transfer unless the new manager approves keeping them in writing. (PS-5; AC-2; PCI DSS 7.2.4)

4.7 User accounts and privileges on every platform must be reviewed at least every six months by managers and system owners. HR and the identity provider must be reconciled every quarter. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2.4; 16 CFR 314.4(c)(1))

4.8 **Service accounts.** Each service account must serve one function with the least privilege it needs, must not be used interactively without approval, must keep its secrets in the company vault (never in code), and must be reviewed at least every six months. (AC-6(5); IA-5; PR.AA-05; PCI DSS 7.2.5, 7.2.5.1, 8.6.1, 8.6.2, 8.6.3)

4.9 **No standing administrator roles** in any cloud or cage. Administrative rights must be granted just in time through PAM, with session recording. Cloud IAM users with long-lived keys are prohibited for people. (AC-6(2); AC-6(5); PR.AA-05; PCI DSS 7.2.2)

4.10 Workforce and customer accounts inactive for 90 days must be disabled. (AC-2(3); PCI DSS 8.2.6)

4.11 Vendor remote access, including hardware and HSM vendor support, must go through PAM, be approved per session, and be recorded. (MA-4; AC-17; PCI DSS 8.2.7)

4.12 **Funding account changes.** A change to a merchant's funding bank account on any portal or by any support channel requires step-up MFA, a 3-business-day hold, and a call-back to a phone number already on file. (AC-3; IA-2; PR.AA-03; 16 CFR 314.4(c)(1))

4.13 **Physical access to the colocation cages** is limited to a list approved by the VP Platform Engineering and reviewed every quarter. Visitors must be escorted, and the escort must be recorded on the visit ticket. (PE-2; PE-3; PR.AA-06; PCI DSS 9.2.1, 9.3.1, 9.3.2)

## 5. Compliance and enforcement
Compliance is checked through the six-month access reviews, the quarterly reviews in POL-01 4.7, and the annual assessment (P07). Violations are handled under POL-01 section 4.14.

## 6. Exceptions
Exceptions follow POL-01 section 4.13. No exception may remove MFA from administrative access into a CDE.

## 7. Related documents
POL-01; POL-04; STD-04; SSP (P02) AC, IA, and PE controls; P01 R-001, R-004, R-011, R-012, R-026
