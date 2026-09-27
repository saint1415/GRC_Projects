# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Head of Technology and Cyber Risk, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, IA-11, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | 12 CFR 30 App. B II.B.3, III.C.1.a, III.C.1.e; 12 CFR 225 App. F III.C.1.a, III.C.1.e |
| Division supplements | Banking: wire operations, treasury management entitlements, core administrator roles. Financial Software: support console, tenant administration, client administrator onboarding. Commercial Real Estate: loan funding approvals, building access systems |

## 1. Purpose
Make sure only authorized people and processes reach group systems, customer information, and payment functions, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services, and the external identities (consumers, business users, client institution administrators) that group systems authenticate. Statement 4.13 also covers the verification of payment instructions in every division.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| System and data owners | Approve access to their systems, tenants, and data |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1, and every system that can federate must use it. Shared or generic accounts are prohibited. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege, approved by the system or data owner. **Standing access to more than one client tenant, or to another division's customer data, is prohibited after 2026-12-31.** Such access must be requested per support ticket, time-limited, and logged. (AC-3; AC-6; PR.AA-05; App. B III.C.1.a)

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Sessions.** Workforce single sign-on sessions must be bound to managed devices and last no more than 8 hours by 2026-11-30. Sensitive console actions (tenant settings, user lists, limits, beneficiaries, entitlements) require re-authentication. (AC-12; IA-11; PR.AA-03)

4.5 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static key at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2)

4.7 Managers and system owners must certify access every quarter, including privileged, support console, and service accounts. (AC-2; AC-6(7))

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.9 **Separation of duties.** Every outgoing wire must be keyed by one person and approved by another. Staff who approve payments must not maintain beneficiary templates or limits. Changes to customer limits, entitlements, and dual-approval thresholds need a second person's approval. (AC-5; App. B III.C.1.e)

4.10 Accounts must lock after 10 failed workforce attempts and 5 failed end-user attempts. Workstations must lock after 10 minutes idle (5 minutes for payments and teller workstations). (AC-7; AC-11)

4.11 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.12 **External identities.** Business payment users and client administrators must use MFA in every tenant of the digital banking platform. From 2027-03-31 the platform must not allow any tenant to switch off MFA for business payment users. Consumer MFA must offer an option other than SMS by 2027-06-30. (IA-8; IA-11; PR.AA-03; App. B II.B.3)

4.13 **Payment instruction verification (all divisions).** Any new or changed payment instruction (beneficiary, account number, remittance details, or loan disbursement instructions) received by email, phone, chat, or document must be verified by a callback to an **independently verified number on file**, never a number supplied in the request or its attachments, and recorded before any payment. A second person must confirm the callback record before release. This applies to bank wire operations, CRE loan funding, client billing and remittance changes in the Financial Software division, and vendor payments by group finance. (AC-5; IA-11; PR.AA-05; App. B III.C.1.a; App. F III.C.1.a)

4.14 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the P07 assessment of SYS-G1 common controls, CDBP and division samples, quarterly certification results, and monthly callback sampling in each division that sends payments.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may be granted to 4.13.

## 7. Related documents
POL-01; POL-03; `division-supplements.md`; common control catalog entries for SYS-G1 (P02); P08 runbook.
