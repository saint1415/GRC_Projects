# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions; adopted by CPA Partners |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(2), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory basis | 16 CFR 314.4(c)(1), (c)(5); 26 CFR 301.7216-2(c)(2); 17 CFR 248.30(a)(2) and 248.201; 45 CFR 164.312(a), (d) |
| Division supplements | Tax and Advisory: seasonal staff, office access, office intake mailboxes. Wealth: money-movement authentication. Practice Cloud: customer tenant administration and support access. CPA Partners: engagement-team access |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job and the data's permitted purpose require.

## 2. Scope
All workforce identities (permanent and seasonal), service accounts, and administrator accounts in every division, CPA Partners, and corporate, and the external identities (tax clients, Wealth clients, Practice Cloud customer users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group HR and the seasonal workforce team | Record hires, end dates, background check results, and training completion before access is activated |
| Office managers and managers | Request and certify their staff's access every quarter |
| Data owners (Chief Tax Officer, Wealth Chief Compliance Officer, Practice Cloud CISO, CPA Partners risk and quality partner) | Approve access to their regulated data |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. Shared mailboxes must be accessed by named users through delegation, never by a shared password. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))

4.2 Access must be role-based and least privilege, and the data owner must approve access to regulated data. In SYS-T1, access is limited to the user's office queue; regional or national access must be time-limited and approved for a named purpose. (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii); 301.7216-2(c)(2))

4.3 **No access before prerequisites.** No account, permanent or seasonal, may be activated for systems holding tax return information or customer information until the background check is complete and the user has completed security and IRC 7216 training. (PS-3; AT-2; PR.AA-02; 314.4(e)(1))

4.4 MFA is required for every individual accessing any group information system. Administrators must use phishing-resistant authenticators. Legacy authentication protocols that cannot perform MFA must be blocked; any exception needs the Qualified Individual's written approval of equivalent controls and expires within 12 months. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))

4.5 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static key at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.6 **Termination and season end.** Access must be disabled within 4 hours of the HR termination event, immediately for involuntary terminations, and on the HR end date for seasonal staff. Extensions of seasonal access must be entered by HR, not granted in a system by an office manager. (PS-4; AC-2(2); 314.4(c)(1)(i))

4.7 Managers and data owners must certify access every quarter, including privileged and service accounts. Seasonal access must be certified monthly during the season. (AC-2; AC-6(7))

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.9 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after the idle time in the division supplement (no more than 30 minutes). (AC-7; AC-11; AC-12)

4.10 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

4.11 **External identities.** Tax client portal accounts, Wealth client portal accounts, and Practice Cloud administrator accounts must require MFA. Wealth money-movement requests made online require step-up authentication. Practice Cloud must make MFA the default for new customer tenants. (IA-8; IA-2; PR.AA-03; 248.201)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
