# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Assurance, LLP) |
| Policy ID | POL-02 |
| Owner | Chief Information Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(1), AC-2(3), AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, IA-8, IA-12, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(1), (c)(5) |
| Other | 26 CFR 301.7216-2(c)(2); 45 CFR 164.308(a)(3)-(4), 164.312(a), (d); IRS Pub. 1345 (e-signature identity verification) |
| Supporting standards | STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people can reach client and Company information, only to the extent their work requires, and that the methods used to prove identity resist the attacks the Company actually faces (session token theft, help desk impersonation, and credential stuffing against the client portal).

## 2. Scope
All workforce members, seasonal staff, interns, offshore vendor staff, contractors, service accounts, and clients who use the portal, across every system in the Tax and Client Data Platform, the CAS platform, the audit and SOC engagement platform, and every SaaS service that holds Company data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and practice leaders | Request and approve access; complete quarterly access reviews for their staff |
| System owners (tax software, DMS, CAS platform, workpaper application, cloud) | Approve role design; review privileged and export rights quarterly |
| Chief People Officer | Records hires, seasonal end dates, transfers, and terminations in the HR system on or before the effective date |
| Chief Information Officer | Runs the identity provider, provisioning, and break-glass accounts |
| Director of Information Security | Runs privileged access management and vendor access; reviews privileged activity |
| IT Operations Manager | Service desk identity verification for resets |
| Workforce | Protect credentials and security keys; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic sign-ins are prohibited; shared mailboxes are reached only through delegated access. (IA-2; AC-2; 314.4(c)(1)(i); 164.312(a)(2)(i))

4.2 Access must be role-based and least-privilege, approved by the user's manager and the system owner before it is granted. Client folders in the DMS must be limited to the client's engagement team, and PHI to the health care engagement team in the restricted enclave. (AC-2; AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii); 164.308(a)(4))

4.3 **MFA.** MFA is required for every individual who accesses any Company information system (314.4(c)(5)). Number matching is the minimum. Administrators, partners, finance staff, and CAS payroll and bill-pay staff must use phishing-resistant security keys by 2027-01-15. Mail and file access requires a compliant Company device from the same date. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03)

4.4 **Clients.** Client portal accounts must use MFA from 2027-01-15. Before resetting a client's MFA or changing a client's email or phone, staff must call the client back on the number on file. Clients who sign Forms 8879 electronically must pass the identity verification IRS Pub. 1345 requires. (IA-8; IA-12; 314.4(c)(5))

4.5 **Every SaaS service must federate to the identity provider** where the service supports it. Local accounts are allowed only by exception under POL-01 4.8 and must be reconciled with HR records monthly. The CAS payroll and bill-pay services must federate by 2026-12-31. (AC-2; IA-2)

4.6 **Termination and seasonal end dates.** Seasonal staff, interns, and contractors get an end date when their account is created. Access must be disabled automatically on the termination or end date, or immediately for involuntary terminations. Badges and any local accounts must be disabled within 24 hours. (PS-4; AC-2; AC-2(3); 164.308(a)(3)(ii)(C))

4.7 **Transfers.** Access from the prior role, including DMS folder rights, must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)

4.8 **Access reviews.** Managers must review their staff's access every quarter. System owners must review privileged, export, and bank-change rights every quarter. Reviews of seasonal accounts are added at the end of each season. (AC-2; AC-6; 164.308(a)(4))

4.9 **Privileged access.** Administrators must use a separate privileged account with a security key, elevated just in time through the privileged access management service, with sessions recorded. No standing directory or productivity suite administrator rights are allowed on daily accounts. Service account credentials must be vaulted and rotated at least annually. (AC-6(2); AC-6(5); IA-5)

4.10 **Emergency access.** The identity provider, productivity suite, cloud organization, and tax software tenant must each have break-glass accounts stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Qualified Individual within 1 business day. (AC-2; 164.312(a)(2)(ii))

4.11 **Separation of duties.** E-file release requires a reviewer different from the preparer. Any change to refund bank fields after review requires re-review. In CAS, bank changes and payment releases need two different approvers. (AC-5)

4.12 **Remote access.** Remote access to Company systems must use the identity provider with MFA and a device check. Sign-in from outside the United States is blocked unless the Director of Information Security approves documented travel, because tax return information may go to firm personnel outside the United States only with consent (26 CFR 301.7216-2(c)(2)). Offshore vendor staff may reach only the virtual desktop pool, from approved source ranges. (AC-17; 314.4(c)(5))

4.13 **Vendor remote access** must use named accounts with MFA through the privileged access broker, be approved per session, be recorded, and end when the work is complete. (MA-4; AC-17)

4.14 **Service desk resets.** Before resetting a password or MFA method, the service desk must verify identity by video call with ID or in person, or get approval from the user's manager in the identity provider. Help desk resets for administrators also need the Director of Information Security's approval. (IA-5; AT-3)

4.15 Passwords must be at least 14 characters and not on the banned-password list. Accounts lock after 10 failed attempts. Screens lock after 10 minutes idle; the tax software ends sessions after 30 minutes and the portal after 15 minutes idle. (IA-5; AC-7; AC-11; AC-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 4.14. Compliance is checked through the quarterly access reviews and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 4.8. Exceptions to 4.3 need the Qualified Individual's written approval of equivalent controls.

## 7. Related documents
POL-01; POL-05; STD-06; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-02, AC-06, IA-02, IA-05, PS-04
