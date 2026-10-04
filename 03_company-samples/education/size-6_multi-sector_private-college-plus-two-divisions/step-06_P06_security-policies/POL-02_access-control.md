# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, AU-6 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | 16 CFR 314.4(c)(1), (c)(5); 34 CFR 99.31(a)(1)(ii); 16 CFR 312.8(b)(3); 45 CFR 164.308(a)(3)-(4), 164.312(a), (d) |
| Division supplements | Higher Education: legitimate educational interest role design and SAIG access. Education Software: customer tenant access and family accounts. Student Health: clinical workstations, break-glass, and the legacy domain |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job, the data's legal purpose, and, for education records, a legitimate educational interest require.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services, and the external identities that group systems authenticate (students, applicants, parent borrowers, families, patients, and customer users).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners (university registrar; executive director of financial aid; Student Health Privacy Officer; customer institutions for their tenants) | Approve access to their data |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |
| Education Software support director | Runs customer tenant access under 4.10 |

## 4. Policy statements
4.1 Every workforce user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. Divisions still on a legacy directory (Student Health, SYS-S2) must migrate to SYS-G1 by 2027-03-31; until then, shared workstation logins are prohibited there too. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i); 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege, and the data owner must approve access to Restricted and Confidential data. Access to education records must be limited to records in which the user has a legitimate educational interest, enforced by technical controls wherever the system supports them. (AC-3; AC-6; PR.AA-05; 34 CFR 99.31(a)(1)(ii); 314.4(c)(1)(ii); 164.308(a)(4))

4.3 MFA is required for all workforce access and for all students. Administrators must use phishing-resistant authenticators. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. Any exception needs the Qualified Individual's written approval of equivalent controls for systems holding the college's customer information. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Adjunct and contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

4.6 Managers and data owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7); 164.308(a)(4)(ii)(C))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after the idle time in the division supplement (no more than 30 minutes for workforce users). (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2; 164.312(a)(2)(ii))

4.10 **Customer tenant access by Education Software staff.** Staff may access a customer tenant (including the Cris Santos College tenant) only to work a ticket, with the customer's approval recorded in the ticket, through PAM, for no more than 8 hours per grant, with read-only access unless the ticket requires more. Standing cross-tenant access is prohibited. Access logs must be available to the customer on request and summarized to the college data owners each month. This statement takes effect for the support console by 2026-12-31. (AC-6; AC-2; AU-6; 34 CFR 99.31(a)(1)(i)(B); 312.8(b)(3))

4.11 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

4.12 **External identities.** Students must use MFA for the SIS, LMS, and student financials. Bank detail changes require a fresh MFA challenge and out-of-band confirmation. Family and parent accounts on the District Platform must be offered MFA. Patient portal accounts must be offered MFA. (IA-8; IA-2; PR.AA-03)

4.13 **Local administrator accounts** on servers and workstations must have unique, automatically rotated passwords. Shared local administrator passwords are prohibited. (IA-5; AC-6; PR.AA-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04 (data classes and owners); `division-supplements.md`; P02 SSP; P07 assessment.
