# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| PCI DSS v4.0.1 | Requirements 7 and 8 |
| Division supplements | Live Venues: seasonal box office accounts. Hotels and Restaurants: PMS accounts and full card number display. Ticketing and Streaming: client tenant administration and support access |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities (including seasonal and contractor identities), service accounts, and administrator accounts in every division and in corporate shared services, and the external identities (patrons, guests, subscribers, client tenant users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Role owners (division system owners) | Define roles and approve access to their systems |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day, including seasonal end dates |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Every workforce account for a system in PCI DSS scope must come from SYS-G1. Shared or generic accounts are prohibited, including shared front desk and box office logins. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1, 8.2.2)

4.2 Access must be role-based and least privilege. The permission to display full card numbers must be limited to named roles with a documented business need. (AC-3; AC-6; PR.AA-05; PCI DSS 3.4.1, 7.2)

4.3 MFA is required for all workforce access. Administrators and key custodians must use phishing-resistant authenticators. All access into a cardholder data environment requires MFA. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4)

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, and rotate any static key at least every 90 days. (AC-2; IA-5; PR.AA-01; PCI DSS 8.6)

4.5 **Termination.** Access must be disabled immediately on the HR termination event, and in no case later than 4 hours after it. Seasonal and contractor accounts must expire automatically at the end date recorded in HR. (PS-4; AC-2; PCI DSS 8.2.5)

4.6 Managers and role owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7); PCI DSS 7.2.4)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. Support access to a client tenant must be linked to a support ticket and visible to the client in the tenant's audit log. (AC-6(5); PR.AA-05; PCI DSS 7.2.2)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Console sessions end after 15 minutes idle. (AC-7; AC-11; AC-12; PCI DSS 8.2.8, 8.3.4)

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited, including integrator tunnels to CCTV and door access systems. (AC-17; MA-4; PCI DSS 8.2.7)

4.11 **External identities.** Patron, guest, subscriber, and client portals must offer MFA and screen passwords against known breached passwords. MFA must be required for client tenant administrators by 2027-01-31, because they can change content that patrons see. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
