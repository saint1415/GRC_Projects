# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director and, for OT, the Group OT security lead) |
| Approved by | Group CISO, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PE-2, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | CISA CPG 2.0 goals 3.A-3.H (voluntary, adopted); PCI DSS v4.0.1 Req. 7 and 8; FAR 52.204-21(b)(1)(i)-(vi), (viii)-(ix) |
| Division supplements | Commercial Property: tenant administrators and badge lifecycle. Construction: external project users and BTI technicians. Hotels: PMS and POS accounts, vendor support access |

## 1. Purpose
Make sure only authorized people and processes reach group systems, building controls, and buildings, and only to the extent their job requires.

## 2. Scope
All workforce identities, service and device accounts, administrator accounts, and integrator and vendor access in every division and in corporate shared services; the external identities that group systems authenticate (tenant administrators, tenant app users, loyalty members, project partners); and physical access credentials (badges) issued by the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group OT security lead | Runs the OT remote access gateway and the OT credential rules |
| Group building technology director | Approves integrator sessions through the RBOC; owns BAACS roles |
| Commercial Property director of security operations | Owns badge issuance and revocation rules and tenant administrator onboarding |
| Managers and data owners | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1 or, for the CUI enclave, in the enclave identity domain. Shared or generic accounts are prohibited. Where an OT device supports only one account, the credential must be held in the group vault, checked out per session, and rotated after use. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege, scoped by region and property for building systems. Enterprise-wide administrator rights to the access control platform are limited to 6 named administrators. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators now; RBOC operators and BTI technicians must use them by 2027-03-31. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Service, device, and local OT accounts** must have a named owner, be recorded in identity governance or the group vault, have default passwords changed before the device connects to any network, and have static credentials rotated at least every 90 days. OT credentials must not be held in division or supplier vaults. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor and BTI technician accounts must expire automatically at the assignment end date. Badges are revoked with the account. (PS-4; AC-2)

4.6 Managers and data owners must certify access every quarter, including privileged accounts, BTI technician access to sites, and access control platform administrators. (AC-2; AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts where the system supports it. Workstations must lock after 10 minutes idle. Application and remote sessions must end after 30 minutes idle. (AC-7; AC-11; AC-12)

4.9 **Emergency access.** Each critical system (BAACS, PMS, ERP) must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 **Remote access to OT** must go only through the group OT remote access gateway, with a named account, MFA, per-session approval by the RBOC, and session recording. Always-on vendor remote-support tools on any building system are prohibited. (AC-17; MA-4; PR.AA-05)

4.11 **Badges.** Tenant badges unused for 90 days must be suspended automatically. Tenant administrators must attest to their badge holder lists every quarter. Group staff badges are revoked under 4.5. Legacy 125 kHz proximity badges must be replaced with encrypted credentials by 2027-12-31. (PE-2; PE-3; PR.AA-06)

4.12 **External identities.** Tenant administrators must use MFA in the access control platform. The tenant app and the loyalty program must offer MFA and require step-up verification for high-risk actions (mobile credential issuance, points redemption). External project users must be removed within 30 days of project closeout. (IA-8; AC-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, BAACS and division samples, quarterly certification results, and the OT gateway logs.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may allow an always-on vendor remote tool on a building system after 2026-12-31.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; OT security standard; common control catalog entries for SYS-G1 (P02).
