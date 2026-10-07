# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | PCI DSS v4.0.1 Req. 7 and 8 (N44-45-R01); 16 CFR 314.4(c)(1), (c)(5) (N44-45-R03); FTC Act Section 5 (N44-45-R02) |
| Division supplements | Grocery Retail: store back office, lanes, and the payment switch. Grocery Wholesale: OT vendor access and portal customer accounts. Financial Services: call center access and card platform administration |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, application and system accounts, and administrator accounts in every division and in corporate shared services, plus the external identities (shoppers, cardholders, independent grocer users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group digital director | Runs customer identity in SYS-G4 |
| Data and system owners | Approve access to their systems and data |
| Managers | Request and certify their staff's access |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Application and system account owners | Keep each account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited, except where a system supports only one account and a documented exception with compensating controls exists. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1, 8.2.2)

4.2 Access must be role-based and least privilege, approved by the system or data owner. Access to card data, Financial Services customer information, and consumer reports is limited to roles that need it. (AC-3; AC-6; PR.AA-05; PCI DSS 7.2; 16 CFR 314.4(c)(1))

4.3 MFA is required for all workforce access and for all access into the cardholder data environment. Administrators must use phishing-resistant authenticators. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4.1 to 8.4.3; 16 CFR 314.4(c)(5))

4.4 **Application and system accounts** must have a named owner, be managed in identity governance or a vault, rotate any static password or key at a frequency set by targeted risk analysis (no longer than 12 months), and be included in access reviews. Interactive use of these accounts is prohibited except in an emergency. (AC-2; IA-5; PR.AA-01; PCI DSS 8.6)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire automatically. (PS-4; AC-2; PCI DSS 8.2.5)

4.6 Access to systems in the cardholder data environment must be reviewed at least every six months; other group applications every quarter, including privileged and application accounts. (AC-2; AC-6(7); PCI DSS 7.2.4, 7.2.5.1)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after no more than 10 failed attempts for at least 30 minutes. Sessions idle for more than 15 minutes must require re-authentication. (AC-7; AC-11; AC-12; PCI DSS 8.3.4, 8.2.8)

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly and reviewed after every use. (AC-2)

4.10 **Vendor and remote maintenance access**, including POS vendors and OT integrators, must go through group PAM with named accounts, MFA, and recording, enabled only when needed. Always-on vendor connections are prohibited. (AC-17; MA-4; PCI DSS 8.2.7)

4.11 **External identities.** Shopper, cardholder, and independent grocer portals must offer MFA and check passwords against breached-password lists. MFA must be required for cardholders when they enroll and when they change contact details, and for every independent grocer portal user from 2027-03-31. Independent grocer accounts must be named to one person. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, access review results, and the QSA ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; `division-supplements.md`; common control catalog entries for SYS-G1 and SYS-G4 (P02).
