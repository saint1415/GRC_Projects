# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group General Counsel, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PE-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | 524B(b)(2) (N31-33-R05); HIPAA 164.308(a)(3)-(4), 164.312(a), (d) for the DCC (N62-R01); 48 CFR 52.204-21(b)(1)(i), (ii), (v), (vi), (viii), (ix) (N42-R04); EAR technology access (N31-33-R04) |
| Division supplements | Medical Devices: signing key custody, plant operator accounts, hospital administrator MFA. Distribution: FCI enclave and warehouse handhelds. Testing: information barrier groups and client portal users |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems and data, and only to the extent their job, the data's owner, and any barrier or export rule allow.

## 2. Scope
All workforce identities, service and pipeline identities, administrator accounts, and plant and warehouse device accounts in every division and in corporate shared services, and the external identities (hospital users, customers, testing clients, suppliers, and contract manufacturers) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| System and data owners | Approve access to their systems and data; certify it every quarter |
| Group trade compliance director | Screens users before access to export-controlled technology |
| Group General Counsel | Defines information barrier groups between Testing and Medical Devices |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Key custodians (Medical Devices) | Operate signing ceremonies; never act alone |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited, including on MES test stations and warehouse handhelds. A documented exception must have compensating controls and an end date. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i); 52.204-21(b)(1)(v))

4.2 Access must be role-based and least privilege, approved by the data owner. Access to export-controlled technology requires trade compliance screening, repeated when a user's project changes. (AC-3; AC-6; PR.AA-05; 52.204-21(b)(1)(i)-(ii))

4.3 **Information barrier.** Medical Devices workforce members must not have access to Testing client data, findings, or collaboration spaces, and Testing staff working on a client engagement must not share it with any other client or division. Barrier groups are enforced in SYS-G1 and reviewed every quarter. (AC-4; AC-3; PR.AA-05)

4.4 MFA is required for all workforce access. Administrators and key custodians must use phishing-resistant authenticators. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d); 52.204-21(b)(1)(vi))

4.5 **Service and pipeline identities** must have a named owner, use workload identity or short-lived tokens where supported, rotate any static secret at least every 90 days, and be included in certification. (AC-2; IA-5; PR.AA-01)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor, supplier, and contract manufacturer accounts must expire automatically at the agreement end date and no later than 12 months after creation. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

4.7 Managers and data owners must certify access every quarter, including privileged, signing, service, and guest accounts. (AC-2; AC-6(7))

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. **Signing** requires two authorized custodians for every production signature. (AC-6(5); AC-5; PR.AA-05)

4.9 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. (AC-7; AC-11)

4.10 Vendor and remote maintenance access to plants, distribution center automation, and laboratories must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

4.11 **External identities.** Hospital administrators who can change device settings or drug libraries in the DCC must use MFA by 2027-03-31. Testing client portal users must use MFA. Customer ordering portal administrators must use MFA. (IA-8; IA-2; PR.AA-03)

4.12 **Physical access** to plants, distribution centers, laboratories, HSM rooms, and server rooms must be limited to authorized people. Visitors must be escorted and recorded in the visitor system. (PE-3; PE-8; PR.AA-06; 52.204-21(b)(1)(viii)-(ix))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
