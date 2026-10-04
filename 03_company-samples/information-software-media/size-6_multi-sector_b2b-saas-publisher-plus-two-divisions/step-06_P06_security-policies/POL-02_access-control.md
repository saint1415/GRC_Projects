# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, IA-11, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory anchors | FTC Start with Security 2 and 3 (N51-R01); 16 CFR 314.4(c)(1), (c)(5) (N52-R03); 48 CFR 52.204-21(b)(1)(i)-(iii), (v)-(vi) (N54-R04); 45 CFR 164.312(a), (d) (N54-R06); PCI DSS 7 and 8 |
| Division supplements | Cloud Software: customer tenant administration and support access. Technology Consulting: implementation-partner access and the client access gateway. Payments and Payroll: CDE access and bank detail changes |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service identities (including cloud access keys and API tokens), and administrator accounts in every division and in corporate shared services, and the external identities (customer administrators, workers, merchants, employers) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners | Approve access to their data; Payments and Payroll owns the payroll handoff data wherever it is stored |
| Managers and project leads | Request and certify their staff's access every quarter; end project access at project close |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |
| Service identity owners | Keep each service identity's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. Identities from an acquired company must move to SYS-G1 within 18 months of closing, and until then must receive HR leaver events the same day. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege. Access to customer, payroll, payment, client, or health data must be approved by the data owner. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access. Administrators and anyone accessing the cardholder data environment must use phishing-resistant authenticators. Any exception for an external user population (for example, workers viewing pay statements) must be approved in writing by the relevant division's Qualified Individual or security lead. (IA-2(1); IA-2(2); PR.AA-03; 16 CFR 314.4(c)(5); PCI DSS 8.4.2)

4.4 **Machine credentials.** Service identities must use short-lived workload credentials wherever the platform supports them. **New static cloud access keys are prohibited** from 2026-11-30, and existing ones must be retired by 2026-12-31 or carry an approved exception with 90-day rotation. Every service identity must have a named owner, be in identity governance, be scoped to the minimum resources (for example, one tenant and one project), and be included in certification. Credentials must never be stored in source code, personal repositories, or documents. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire at the assignment end date. (PS-4; AC-2)

4.6 Managers and data owners must certify access every quarter, including privileged roles, service identities, and **implementation-partner roles that consultants hold inside customer tenants**. (AC-2; AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after the idle time in the division supplement (no more than 30 minutes for workforce sessions). (AC-7; AC-11; AC-12)

4.9 **Emergency access.** Each critical system and cloud account must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 Vendor and remote maintenance access must go through group PAM or the client access gateway with named accounts, MFA, and recording. Persistent vendor tunnels and VPNs without device checks are prohibited. (AC-17; MA-4)

4.11 **Partner and project access.** Access that a consultant needs inside a customer's or client's system must be requested per project, linked to a ticket, and set to expire at the project end date (at most 90 days, renewable). (AC-2; PS-7; AC-6)

4.12 **External identities.** Customer, employer, and merchant administrator accounts must use MFA. Changes to a worker's bank account require re-authentication and a notice to the worker's previously registered contact. (IA-8; IA-11; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and the monthly static key report.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04; division supplements; P02 SSP (AC and IA families); P04 cloud control map.
