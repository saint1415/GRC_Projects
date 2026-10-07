# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-19, IA-2, IA-2(1), IA-2(2), IA-3, IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |
| Division supplements | Ambulance Services: vehicle devices and crew sign-in. Urgent Care: legacy clinic accounts until migration. BDS: dispatch consoles, client agency users, and contact center agents |

## 1. Purpose
Make sure only authorized people, devices, and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, administrator accounts, vendor support accounts, and device identities (vehicle routers, mobile data computers, tablets) in every division and in corporate shared services, and the external identities (client agency users, patients) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| System and data owners | Approve access to their systems and client partitions |
| Managers and station supervisors | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Vendor managers | Request vendor access through PAM for each support session |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. A documented exception (for example, a device that supports only one account) must have compensating controls and an end date. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege, and the data owner must approve access to PHI. Client agency users must see only their own agency's incidents. (AC-3; AC-6; PR.AA-05; 164.308(a)(4))

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. Dispatch consoles may use badge plus PIN as the second factor. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))

4.4 **Vendor access.** Vendor support access must go through group PAM with a named account per vendor engineer, approval for each session, MFA, and session recording. Standing vendor administrator accounts and persistent vendor tunnels are prohibited. (AC-17; AC-6(5); MA-4)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Per-diem and contractor accounts must be suspended after 30 days without a scheduled shift and expire at the assignment end date. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

4.6 Managers and data owners must certify access every quarter, including privileged, service, and vendor accounts. (AC-2; AC-6(7); 164.308(a)(4)(ii)(C))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle, except dispatch consoles on a badge-controlled dispatch floor (the documented equivalent measure). Application sessions must end after the idle time in the division supplement (no more than 30 minutes). (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.9 **Emergency access.** Each critical system, including the CAD at each communications center, must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2; 164.312(a)(2)(ii))

4.10 **Devices.** Every device that connects to the CAD or holds ePHI (routers, MDCs, tablets) must be in the group inventory, authenticate with its own credential or certificate, and have no factory default or shared administrative passwords. (IA-3; IA-5; AC-19; CM-8)

4.11 **External identities.** Client agency users must sign in through federation with their agency's identity provider or through SYS-G1 guest accounts with MFA. (IA-8; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
