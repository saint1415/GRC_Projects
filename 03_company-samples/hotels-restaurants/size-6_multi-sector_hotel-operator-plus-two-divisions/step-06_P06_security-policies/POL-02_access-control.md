# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | PCI DSS Requirements 7 and 8 (N72-R01, N71-R04, N53-R04); 16 CFR 314.4(c)(1) and (c)(5) (N53-R01); 15 U.S.C. 45(a) (N72-R02) |
| Division supplements | Hotels: PMS card-display rights, legacy POS local accounts, front desk key issuance. Attractions: seasonal staff, ride engineering access. Vacation Ownership: legacy directory until 2027-03-31; owner portal |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities (about 38,500), contractor and vendor identities (about 6,200), service accounts, and administrator accounts in every division and in corporate shared services, and the external identities (loyalty members, owners, passholders, and parents) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data and system owners | Approve access to their systems and data |
| Managers (including outlet, front office, and park managers) | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day; seasonal end dates at hire |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |
| Qualified Individual | Approves in writing any MFA equivalent for the finance subsidiary |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited. Legacy POS local accounts are a documented exception until the legacy POS is retired (target 2027-06-30); they must be listed, certified, locked after 6 failed attempts, and monitored at the segment boundary. (IA-2; AC-2; PR.AA-01; Req 8.2)

4.2 Access must be role-based and least privilege and approved by the system owner. Full card number display in the PMS is limited to roles with a documented business need, reviewed every 6 months. A service account or integration may read only the data fields its function needs; no integration may read another division's customer data without the Group Chief Privacy Officer's approval. (AC-3; AC-6; PR.AA-05; Req 3.4, 7.2; 314.4(c)(1))

4.3 MFA is required for all workforce access to any information system that holds Restricted data, for all access into a cardholder data environment, and for all remote access. Administrators must use phishing-resistant authenticators. In the finance subsidiary, any individual accessing any information system must use MFA unless the Qualified Individual has approved a reasonably equivalent control in writing. (IA-2(1); IA-2(2); PR.AA-03; Req 8.4; 314.4(c)(5))

4.4 **Service accounts** must have a named owner, be managed in identity governance, store credentials only in the group secret store, rotate any static key at least every 90 days, never be cached on endpoints or POS servers, and be included in access certification. (AC-2; IA-5; PR.AA-01; Req 8.6)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Seasonal staff access must be disabled automatically at the end of the last scheduled shift. Contractor accounts must expire at the assignment end date. (PS-4; AC-2; Req 8.2.5)

4.6 Managers and system owners must certify access every quarter, including privileged, service, and legacy POS local accounts. (AC-2; AC-6; Req 7.2.4)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after no more than 10 failed attempts (6 for legacy POS PINs). Workstations must lock after 15 minutes idle; front desk and outlet workstations after 5 minutes. (AC-7; AC-11; Req 8.3.4, 8.2.8)

4.9 **Emergency access.** Each critical system (PMS, lock servers, ticketing, payment services) must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 **Vendor and remote maintenance access** must go through group PAM with named accounts, per-session approval, group MFA, and recording, and must be disabled when not in use. Vendor-operated always-on remote tools are prohibited. Ride and show control maintenance requires ride engineering approval for each session. (AC-17; MA-4; Req 8.2.7, 8.4.3)

4.11 **External identities.** Loyalty, passholder, and owner accounts must offer MFA. MFA must be required for owner portal actions that change payment details or redeem points from 2027-03-31, and step-up verification must be required for loyalty point redemptions above the threshold in the Hotels supplement. Parents' kids' club accounts must be verified as the parent's (16 CFR 312.6(a)(3)). (IA-8; IA-2; PR.AA-03)

4.12 **Guest identity at the front desk and contact center.** Staff must verify a guest's identity under the Hotels supplement before issuing a room key or disclosing reservation details. (IA-8; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and PCI DSS validations.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04 (classes and purpose rules); `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
