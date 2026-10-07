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
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d). Privacy Rule 164.514(d)(2) |
| Division supplements | Care Delivery: EHR break-glass and clinical device accounts. Health Plan: broker and member authentication. SaaS: customer tenant administration and engineer production access |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job and the data's permitted purpose require.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services, and the external identities (patients, members, brokers, SaaS customer users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners (division Privacy Officers; SaaS data platform lead) | Approve access to their PHI zones and datasets |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. A documented exception (for example, a medical device that supports only one account) must have compensating controls. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege, and the data owner must approve access to PHI. Access to another covered entity's PHI must name the permitted purpose and be approved by that covered entity's Privacy Officer. Standing access to both covered entities' PHI zones is prohibited; time-limited access for an approved purpose is allowed. (AC-3; AC-6; PR.AA-05; 164.308(a)(4); 164.514(d)(2))

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static key at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor and locum accounts must expire automatically at the assignment end date. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

4.6 Managers and data owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7); 164.308(a)(4)(ii)(C))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after the idle time in the division supplement (no more than 30 minutes). (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2; 164.312(a)(2)(ii))

4.10 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

4.11 **External identities.** Patient, member, broker, and SaaS customer portals must offer MFA. MFA must be required for broker accounts and for SaaS customer administrator accounts. SMS codes must not be the only second factor for broker accounts after 2027-03-31. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04 (purpose tags); `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
