# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory anchors | E-Verify MOU Art. II.A.3 and II.A.15; 8 CFR 274a.2(g)(1)(i); 29 CFR 1630.14(b)(1); HIPAA 164.308(a)(3)-(4), 164.312(a), (d); FAR 52.204-21(b)(1)(i)-(ii), (v)-(vi) |
| Division supplements | Staffing: E-Verify users, client VMS integrations, kiosks. Consulting: client-issued accounts and the Federal Solutions enclave. Home Health: EHR accounts for per diem clinicians and field tablets |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job and the data's permitted purpose require.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services; external identities that group systems authenticate (associates and employees in self-service, candidates, client users); and accounts that group workforce members hold in systems the group does not operate (E-Verify, client EHRs and other client systems, federal agency systems).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners | Approve access to their data: the Staffing Vice President, Employment Compliance for Form I-9 and E-Verify data; the group credentialing director for medical screening files; the Home Health HIPAA Privacy Officer for patient data |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Engagement managers (Consulting) | Request and remove client-issued accounts for their consultants |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited, including in systems the group does not operate (E-Verify, client systems, agency systems). (IA-2; AC-2; PR.AA-01; MOU Art. II.A.15; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege. Form I-9 images and consumer reports are limited to onboarding and compliance roles; clinician medical screening files to credentialing roles, kept separate from other personnel files; patient data to Home Health roles with a treatment, payment, or operations need. (AC-3; AC-6; PR.AA-05; 8 CFR 274a.2(g)(1)(i); 29 CFR 1630.14(b)(1); 164.308(a)(4))

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))

4.4 **Self-service and bank changes.** Changes to pay destinations must be confirmed out of band through a factor other than the one used to sign in, and a first-time destination change must be held for 3 days with notice to the worker. SMS codes must not be the only factor for bank changes after 2027-03-31. (IA-2(2); IA-8; PR.AA-03)

4.5 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. Client integration accounts must be unique per client. (AC-2; IA-5; PR.AA-01)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. E-Verify accounts are on the termination checklist and are reconciled to HR monthly. Accounts of per diem and contract clinicians expire at their assignment end date. (PS-4; AC-2; 164.308(a)(3)(ii)(C); MOU Art. II.A.3)

4.7 **Accounts in systems the group does not operate.** Consulting must keep a register of every client-issued account its workforce holds, ask the client in writing to remove the account within 1 business day of roll-off, and reconcile the register with each client every quarter. (AC-20; PS-4; 164.308(a)(3)(ii)(C))

4.8 Managers and data owners must certify access every quarter, including privileged, service, and E-Verify accounts. (AC-2; 164.308(a)(4)(ii)(C))

4.9 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.10 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle; field tablets after 5 minutes. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.11 Each critical system must have sealed break-glass accounts, tested quarterly and reviewed after every use. (AC-2; 164.312(a)(2)(ii))

4.12 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. (AC-17; MA-4)

4.13 The Federal Solutions enclave is reachable only from managed devices through SYS-G1 with MFA, and only by consultants assigned to a federal contract. (AC-3; AC-17; FAR 52.204-21(b)(1)(i), (ii), (vi))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
