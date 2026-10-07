# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Agency and federal drivers | CJISSECPOL v6.1 AC-7, AC-11, IA-2(1), IA-2(2) ([Priority 1]); Pub. 1075 sec. 4 AC and IA; SP 800-171 Rev. 2 3.1 and 3.5; 45 CFR 164.312(a), (d) |
| Division supplements | GovTech: tenant-scoped support access and agency-issued accounts. IT Consulting: CUI enclave access and the acquired firm's VPN until migration. Software: RMS support by state and customer administrator MFA |

## 1. Purpose
Make sure only authorized and screened people and processes reach group systems and agency, federal, and customer data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services; the external identities (agency users, federal users, customer administrators) that group systems authenticate; and the acquired consulting firm's identity provider and VPN until they are retired.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| System owners | Define roles; approve access to their systems |
| GovTech personnel security manager; division security leads | Confirm screening in the group register before access to CJI, FTI, CUI, or motor vehicle records |
| Managers | Request and certify their staff's access every quarter |
| Group HR | Records joiners, movers, and leavers the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege. Access to CJI, FTI, CUI, or motor vehicle records must be **scoped to the tenant, agency, or program** the person supports, and granted only after the group screening register shows the required checks for every state or program involved (POL-01 4.7). Standing cross-tenant support access is prohibited. (AC-3; AC-6; PR.AA-05; CJISSECPOL v6.1 PS-3; Pub. 1075 Exhibit 7 I(2))

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. Remote access to any environment holding agency or federal data, including VPNs inherited through acquisitions, must use phishing-resistant MFA; SMS codes must not be used after 2026-10-31. (IA-2(1); IA-2(2); PR.AA-03; CJISSECPOL v6.1 IA-2; SP 800-171 Rev. 2 3.5.3)

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static credential at least every 12 months (90 days for agency interface credentials once automation is live), and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Subcontractor accounts must expire at the assignment end date. Staff with agency-issued accounts must be reported to the agency for removal on their last day. (PS-4; AC-2)

4.6 Managers and system owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. No standing administrator rights are allowed in production environments holding agency or federal data. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 5 failed attempts in 15 minutes until an administrator releases them. Endpoints must lock after 15 minutes idle; application sessions must end after no more than 30 minutes idle. (AC-7; AC-11; AC-12; CJISSECPOL v6.1 AC-7, AC-11)

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4)

4.11 **External identities.** Agency and federal users must authenticate through their organization's identity provider with MFA or through group-provided MFA. Customer administrator accounts in group SaaS products must use MFA. (IA-8; IA-2; PR.AA-03)

4.12 **Directory trusts** with acquired or external directories are allowed only for a migration with an end date approved by the Group CISO, must be monitored by the group SOC, and must be removed at migration. (AC-20; AC-17; SI-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certifications, and the screening register.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
