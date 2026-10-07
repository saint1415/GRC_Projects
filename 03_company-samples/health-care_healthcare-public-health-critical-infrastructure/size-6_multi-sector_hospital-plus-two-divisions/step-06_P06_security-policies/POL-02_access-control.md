# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.310(a)(2)(iv); 164.312(a), (d). Privacy Rule 164.514(d)(2) |
| Other drivers | 16 CFR 314.4(c)(1), (c)(5) (College); 34 CFR 99.31(a)(1)(ii) (FERPA reasonable methods) |
| Division supplements | Hospital System: EHR break-glass, student and trainee accounts, clinical device accounts. Health Plan: broker and member authentication. College: SIS and financial aid access until migration to SYS-G1 |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job, their rotation, and the data's permitted purpose require.

## 2. Scope
All workforce identities (including students, trainees, agency, and locum staff), service accounts, administrator accounts, and vendor accounts in every division and in corporate shared services, and the external identities (patients, members, brokers, community-connect practice users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners (division privacy officers; College Registrar) | Approve access to PHI, member data, and education records |
| Managers and clinical placement coordinators | Request and certify their staff's and students' access |
| Group HR and division HR; staffing office | Record joiners, movers, leavers, and assignment end dates the same day |
| Clinical engineering director | Owns device vendor access requests |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited. A documented exception (for example, a medical device that supports only one account) must have compensating controls. The College must move its users to SYS-G1 by 2027-06-30; until then its directory must meet this policy. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege, and the data owner must approve access to PHI, member data, and education records. Access to the other covered entity's PHI is allowed only through an approved feed or protocol (POL-04 4.3). (AC-3; AC-6; PR.AA-05; 164.308(a)(4); 164.514(d)(2); 34 CFR 99.31(a)(1)(ii))

4.3 **MFA** is required for remote access, email, privileged access, and any access to a system that holds College customer information (unless the College Qualified Individual approves an equivalent control in writing). Clinical workstations must use badge tap and PIN or another two-factor method. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d); 16 CFR 314.4(c)(5))

4.4 **Students, trainees, agency, and locum staff** may receive accounts only through identity governance, from an approved placement roster or staffing contract. Every such account must have an end date no later than the rotation or assignment end, must use the same authentication as employees, and may be activated only after the hospital records the person's security and privacy training. (AC-2; AC-2(3); PS-7; 164.308(a)(3)(ii)(A)-(C))

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Accounts with an end date expire automatically; schools and agencies must report early withdrawals within 1 business day under their agreements. (PS-4; PS-7; AC-2; 164.308(a)(3)(ii)(C))

4.6 Managers and data owners must certify access every quarter, including privileged, service, student, and vendor accounts. (AC-2; AC-6(7); 164.308(a)(4)(ii)(C))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle (2 minutes in public clinical areas). Application sessions must end after the idle time in the division supplement (no more than 60 minutes). (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.9 **Emergency access.** Each critical clinical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed by the Privacy Officer after every use. (AC-2; 164.312(a)(2)(ii))

4.10 **Vendor and remote maintenance.** All vendor access, including medical device vendor support, must go through group PAM with named accounts, MFA, approval for each session, and recording. Persistent vendor connections are prohibited after 2026-12-31. (AC-17; MA-4; 164.310(a)(2)(iv); 164.312(d))

4.11 **Service accounts** must have a named owner, be managed in identity governance, store credentials in the group vault, rotate any static password or key at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.12 **External identities.** Patient, member, broker, and community-connect portals must offer MFA. MFA must be required for brokers and for community-connect practice users (through federation with the practice's identity provider). SMS codes must not be the only second factor for brokers after 2027-03-31. (IA-8; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and monthly student account reconciliations.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04 (minimum-necessary protocols); `division-supplements.md`; common control catalog entries for SYS-G1 (P02); affiliation agreements with schools.
