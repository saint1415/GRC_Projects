# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group General Counsel, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-21, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | N48-49-R01 (33 CFR 101.650(a)(1)-(7), (e)(3)(v), (f)(3)); N42-R04 (52.204-21(b)(1)(i), (ii), (v), (vi)); 46 U.S.C. 41106(2) |
| Division supplements | Marine Terminals: VMT and gate booth sign-in, OT HMI accounts, longshore operator IDs. Freight Trading: federal sales workspace and scale PCs. Port Real Estate: integrator accounts on building systems |

## 1. Purpose
Make sure only authorized people, processes and devices reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, longshore operator IDs, service accounts, administrator accounts and vendor and integrator accounts in every division and in corporate shared services, on IT and OT, and the external identities (truckers, cargo owners, tenants) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners (terminal general managers; division leads) | Approve access to their systems and data; certify it each quarter |
| Managers | Request access for their staff |
| Group HR and division HR | Record joiners, movers and leavers the same day; pass hiring hall registration changes weekly |
| Service account owners | Keep each service account's purpose, permissions and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited on IT and OT, including gate booth workstations, scale PCs and vendor accounts. A documented exception (for example, an HMI that supports only one account) must have compensating controls recorded in the Cybersecurity Plan. (IA-2; AC-2; PR.AA-01; 101.650(a)(6); 52.204-21(b)(1)(v))

4.2 Access must be role-based and least privilege, approved by the data owner. **A data owner must not be the requester's own manager when the requester belongs to another division.** Access by one division to another division's customer data requires approval under the affiliate data-sharing standard (POL-01 4.7). (AC-3; AC-6; AC-21; PR.AA-05; 101.650(a)(5); 46 U.S.C. 41106(2))

4.3 MFA is required for all workforce access to password-protected IT systems and for any remote access to OT. Administrators must use phishing-resistant authenticators. Where MFA is not feasible (for example, a local HMI), compensating controls must be documented. (IA-2(1); IA-2(2); PR.AA-03; 101.650(a)(4))

4.4 Passwords must be at least 14 characters where systems support it. Default passwords must be changed before any IT or OT device is used, and every new device must be checked before it joins a network. (IA-5; 101.650(a)(2)-(3))

4.5 Accounts must lock after 5 failed attempts on all password-protected IT systems. Workstations must lock after 15 minutes idle; gate booth and VMT sessions end at shift change. (AC-7; AC-11; AC-12; 101.650(a)(1))

4.6 **Service accounts** must have a named owner, be managed in identity governance, use certificates or short-lived tokens where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.7 **Termination.** Access must be disabled on the last day, and immediately for involuntary terminations. Longshore operator IDs must be disabled when the hiring hall registration lapses. Local accounts on systems not federated to SYS-G1 must be reconciled weekly. (PS-4; AC-2; 101.650(a)(7))

4.8 Data owners must certify access every quarter, including privileged, service and vendor accounts. (AC-2; AC-6(7))

4.9 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05; 101.650(a)(5))

4.10 **Vendor and integrator remote access** to IT, OT and building systems must go through the group jump host with named accounts, MFA, per-session approval and recording. Persistent vendor tunnels, modems and internet-exposed remote access are prohibited. Any remotely accessible OT must have a documented justification. (AC-17; MA-4; 101.650(e)(3)(v); 101.650(f)(3))

4.11 **Emergency access.** Each critical system must have sealed break-glass accounts, held by the FSO at each terminal or the system owner elsewhere, tested quarterly and reviewed after every use. (AC-2)

4.12 **External identities.** The customer portal and tenant portal must offer MFA; MFA must be required for cargo owner and tenant administrator accounts by 2026-12-31 and for all trucker users by 2027-03-31. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; `division-supplements.md`; affiliate data-sharing standard; P02 SSP section 11; 33 CFR 101.650(a); FAR 52.204-21.
