# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after significant changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | PCI DSS 7.2, 7.3, 8.2 to 8.6; 16 CFR 314.4(c)(1), (c)(5); SOC 2 CC6.1 to CC6.3 |
| Division supplements | Payment Processing: dispute platform roles, detokenization, key custodians. Software: ISV credentials, merchant administrator MFA, engineer production access. Merchant Consulting: interim rules for SYS-M1 until migration |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service identities, and administrator accounts in every division and in corporate shared services, including identities from an acquired company's identity provider, and the external identities (merchant users, ISVs) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Role owners (division application owners) | Define roles and approve access to their applications |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Service identity owners | Keep each service identity's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. **No identity provider other than SYS-G1 may grant access to a cardholder data environment after 2027-03-31**; until then, a federated identity provider (SYS-M1) must meet 4.3 and be reconciled against HR every week. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1)

4.2 Access must be role-based and least privilege, approved by the role owner. Permissions that release full PAN or bulk data (detokenization, case export, report extracts) must be limited to named roles with a documented need and, for bulk export, a ticket. (AC-3; AC-6; PR.AA-05; PCI DSS 7.2; 314.4(c)(1))

4.3 **MFA** is required for all workforce access to any information system. Administrators must use phishing-resistant authenticators, and all access into a cardholder data environment must use them by 2027-03-31. **SMS one-time codes are not accepted for access into a cardholder data environment after 2026-12-31.** MFA exemptions of any kind (trusted locations, device exceptions) require the Group CISO's written approval. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4, 8.5; 314.4(c)(5))

4.4 **Service identities** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01; PCI DSS 8.6)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations, in SYS-G1 and in any federated identity provider. Contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2; PCI DSS 8.2.5)

4.6 Managers and role owners must certify access every quarter, including privileged and service identities and users from other divisions. Accounts inactive for 90 days must be disabled. (AC-2; AC-2(3); AC-6(7); PCI DSS 7.2.4, 8.2.6)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05; PCI DSS 8.4.1)

4.8 Accounts must lock after no more than 10 failed attempts for at least 30 minutes. Sessions idle for 15 minutes must require re-authentication. (AC-7; AC-11; AC-12; PCI DSS 8.3.4, 8.2.8)

4.9 **Cross-division access.** A user from one division may access another division's cardholder data environment, support console, or customer data only with a ticket that names the purpose, approval from the receiving division's role owner, and an expiry of 90 days or less. Standing cross-division access is prohibited. (AC-2; AC-6; PR.AA-05)

4.10 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.11 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4; PCI DSS 8.2.7)

4.12 **External identities.** Merchant portal users must use MFA for refund, funding account, and virtual terminal roles, and all other merchant users must be covered by risk-based sign-in analysis. Merchant administrators on the commerce software must use MFA by 2027-03-31. ISV and merchant API credentials must be shown only once at creation and stored so they cannot be read by staff. (IA-8; IA-5; PR.AA-03; PCI DSS 8.3.10.1, 8.3.2)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and the ROCs.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may remove MFA from access into a cardholder data environment.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
