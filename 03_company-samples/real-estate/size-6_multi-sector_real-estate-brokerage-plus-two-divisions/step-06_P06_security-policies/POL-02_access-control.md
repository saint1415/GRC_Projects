# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-2(12), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, IA-12, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(1), (c)(5) |
| Division supplements | Brokerage: contractor agent lifecycle and SYS-B1 visibility. Mortgage and Title: Title closer roles and vendor access to SYS-M2. Homebuilding: smart-home roles at handover |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, contractor agent identities, service accounts, and administrator accounts in every division and in corporate shared services, and the external identities (buyers, sellers, borrowers, tenants, homeowners) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance, the contractor agent tier) as a common control |
| Data owners (system owners; President, Title for Title data in the TMCC) | Approve access to their systems and data |
| Managers and managing brokers | Request and certify access every quarter; report departures the same day |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every employee and contractor agent must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))

4.2 Access must be role-based and least privilege. In the transaction platform, agents see only the transactions of their own team; Title documents are visible only to the agents and staff on that transaction. (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))

4.3 **MFA is required for every individual accessing any group information system,** including all contractor agents. Administrators and staff who publish wire instructions or approve or release wires must use phishing-resistant hardware keys. No exception may be granted unless the Qualified Individual approves reasonably equivalent or more secure controls in writing. From 2027-01-01, accounts without MFA are disabled. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, and rotate any static secret at least every 90 days. (AC-2; IA-5; PR.AA-01)

4.5 **Removal.** Employee access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor agent access must be disabled within 1 business day after the agent leaves or transfers their license; managing brokers must report the departure the same day, and the license transfer feed disables the account automatically. Accounts inactive for 60 days are disabled. (PS-4; PS-7; AC-2; AC-2(3); 314.4(c)(1)(i))

4.6 Managers, managing brokers, and data owners must certify access every quarter, including privileged, Title closer, and service accounts. (AC-2; AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after 30 minutes idle, and consumer portal sessions after 15 minutes. (AC-7; AC-11; AC-12)

4.9 Sign-in risk analytics (impossible travel, new device, anonymizing networks) must cover every identity tier, including contractor agents, with alerts to the SOC. (AC-2(12); DE.CM-03; 314.4(c)(8))

4.10 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, approval, and recording. Vendors' own remote tools are prohibited unless the Group CISO approves an exception. (AC-17; MA-4)

4.11 **External identities.** Buyers and sellers must complete identity proofing before wire instructions are first shown and re-authenticate before each display. Borrower portal MFA must be required by 2027-06-30. Homebuilding must remove builder administrator roles from a home's smart-home devices at closing and must not use shared device passcodes. (IA-8; IA-12; IA-5; AC-2)

4.12 **Personal devices.** Contractor agents may use personal devices only through approved apps with app protection (no copy, no unmanaged backup) and browser access without downloads from unmanaged laptops. (AC-20; AC-19; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. An exception to 4.3 must be approved in writing by the Qualified Individual.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02); TMCC SSP section 11 (P02).
