# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group export compliance director, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-3, IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| SP 800-171 Rev. 2 | 3.1.1 to 3.1.22; 3.5.1 to 3.5.11; 3.7.5; 3.9.2 |
| Division supplements | Aircraft Parts: MES and shop-floor accounts, machine vendor access. Engineering Services: field engineers, GFE, and customer systems. Defense Software: tenant support access and customer tenant administration |

## 1. Purpose
Make sure only authorized U.S.-person users, processes, and devices reach group systems that hold CUI, and only to the extent their job and the data's export controls allow.

## 2. Scope
All workforce identities, service accounts, administrator accounts, and devices in every division and in corporate shared services, and the external identities (prime and supplier users of the exchange gateway, customer users of the platform editions) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (both tenants; sign-in, MFA, PAM, identity governance) as a common control |
| Group export compliance office | Verifies U.S.-person status before any CUI access; owns export tags |
| Data owners (division VPs of engineering; Program H chief engineer; platform general managers) | Approve project, program, and tenant access |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. CUI systems must use only the SYS-G1 government-community tenant. Shared or generic accounts are prohibited; where equipment supports only one account (for example a machine controller), the exception must be documented with compensating controls in the SSP. (IA-2; AC-2; PR.AA-01; 3.5.1; 3.5.2)

4.2 **U.S.-person gating.** No account may receive access to CUI or export-controlled data until the export compliance office has recorded the user's U.S.-person status, or an Empowered Official has approved access under an export authorization. Access must follow the data's export tag. (AC-3; AC-21; PR.AA-05; 3.1.1; 22 CFR 120.56)

4.3 Access must be role-based and least privilege, approved by the data owner. Program H access requires the Program H chief engineer's approval and is limited to named staff. (AC-3; AC-6; PR.AA-05; 3.1.2; 3.1.5)

4.4 **MFA** is required for all access to CUI systems and for all remote and privileged access. Administrators must use phishing-resistant hardware keys. All CUI users must use phishing-resistant authenticators by 2027-03-31. (IA-2(1); IA-2(2); PR.AA-03; 3.5.3)

4.5 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static key at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01; 3.5.10)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations or insider threat referrals. Contractor accounts must expire at the assignment end date. Accounts inactive for 45 days must be disabled automatically, including local accounts on MES and other shop-floor systems. (PS-4; AC-2(3); 3.5.6; 3.9.2)

4.7 Managers and data owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7))

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. Support access to customer tenants in the platform editions must be linked to a customer ticket. (AC-6(5); PR.AA-05; 3.1.7; 3.1.15)

4.9 Accounts must lock after 10 failed attempts. Sessions must lock after 15 minutes idle with a pattern-hiding screen and end after the idle time in the division supplement (no more than 30 minutes for web applications). (AC-7; AC-11; AC-12; 3.1.8; 3.1.10; 3.1.11)

4.10 **External systems.** CUI may be used only on systems listed in the external systems register, which must show the basis for trust (contract, CRM, FedRAMP status, or customer agreement). Public AI services, personal cloud storage, and personal email must never hold CUI and are blocked from CUI endpoints. (AC-20; PR.AA-05; 3.1.20; 3.1.21)

4.11 Vendor and remote maintenance access, including machine and controller vendors, must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4; 3.1.12; 3.7.5)

4.12 **Device authentication.** Only enrolled, compliant devices may reach CUI systems. Thick CAD workstations must use certificate-based device authentication by 2027-03-31. (IA-3; PR.AA-03; 3.5.2)

4.13 **External identities.** Prime, supplier, and customer users must authenticate through their own organization's federation or with group-issued accounts that require MFA. (IA-8; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; POL-04 (export tags); `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
