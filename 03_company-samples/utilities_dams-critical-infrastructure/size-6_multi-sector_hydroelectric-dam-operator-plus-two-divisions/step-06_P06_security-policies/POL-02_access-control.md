# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (IT identity operated by the group identity director; OT identity operated by the Director, OT Security) |
| Approved by | Group CISO under authority of POL-01; CIP topics approved by the CIP Senior Manager, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | C-DAMS-R03 (CIP-004-7 R4 to R6; CIP-005-7 R2 and R3; CIP-007-6 R5; CIP-003-9 Att. 1 Sec. 3 and 6); C-DAMS-R01 (Table 9.3a and 9.3b access control; Form 3 Q12); N23-R04 (SP 800-171 Rev. 2 3.1, 3.5) |
| Division supplements | Hydro: OT identity domain, Intermediate Systems, commissioning sessions. Constructors: FPE access, external project platform users. Engineering: DSMS client tenants |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems and data, and only to the extent their job requires. In OT, the purpose is also physical: nobody should be able to move a spillway gate or change a unit setpoint without authority.

## 2. Scope
All workforce identities, service accounts, administrator accounts, and external identities (subcontractors, vendors, DSMS client users) in every division, in both IT and OT.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control for IT |
| Director, OT Security | Runs the OT identity domain, OT PAM, and the Intermediate Systems |
| Data and system owners | Approve access to their systems, BCSI, CEII, and CUI |
| Managers | Request and certify their staff's access every quarter |
| Group HR | Records joiners, movers, and leavers the same day |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited, except documented OT accounts that a device supports only in that form; those must be inventoried, restricted to named people, and have their passwords changed when a person who knows them leaves. (IA-2; AC-2; PR.AA-01; CIP-007-6 R5 Parts 5.2 and 5.3)

4.2 Access must be role-based, least privilege, and approved by the data or system owner. Access to BCSI, CEII, and CUI requires a documented need and owner approval. (AC-3; AC-6; PR.AA-05; CIP-004-7 R6 Part 6.1; SP 800-171 Rev. 2 3.1.1)

4.3 MFA is required for all workforce access to IT, for all Interactive Remote Access to OT, and for all privileged access. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03; CIP-005-7 R2 Part 2.3; SP 800-171 Rev. 2 3.5.3)

4.4 **OT identity is separate.** OT systems must not trust corporate identity. OT accounts live in the OT identity domain, and corporate credentials must not grant OT access. (AC-2; SC-7; PR.AA-01)

4.5 **Remote access to OT** must pass through the Intermediate Systems with encryption, MFA, and session recording. Vendor sessions are on demand, approved per session, and must be possible to see and disable centrally. Cellular routers, remote support tools, and any other path that bypasses the Intermediate Systems are prohibited inside Hydro plants. (AC-17; MA-4; CIP-005-7 R2 Parts 2.1 to 2.5; CIP-003-9 Att. 1 Sec. 6; Form 3 Q12)

4.6 **Transient devices** (laptops, test sets, commissioning kits) may connect to OT only if Hydro manages them, or if Hydro has reviewed them before each connection under CIP-003-9 Attachment 1 Section 5.2 (or CIP-010-4 R4 at the HOCs). This applies to affiliates' devices. (AC-20; SI-3)

4.7 **Termination.** Access must be removed within 4 hours of the HR termination event for IT, and within 24 hours for unescorted physical access and Interactive Remote Access to CIP-scope systems (CIP-004-7 R5 Part 5.1). Subcontractor accounts must expire at the project end date. (PS-4; AC-2)

4.8 Managers and owners must certify access every quarter. For CIP-scope systems, verify authorization records every calendar quarter and privileges at least every 15 calendar months; verify BCSI access at least every 15 calendar months. (AC-2; AC-6(7); CIP-004-7 R4 Parts 4.2 and 4.3; R6 Part 6.2)

4.9 Privileged access must be granted just in time through PAM (IT) or OT PAM (OT), with approval and session recording. (AC-6(5); PR.AA-05)

4.10 Accounts must lock or alert after 5 failed attempts in OT and 10 in IT. Workstations lock after 15 minutes idle, except HOC operator displays that must stay visible inside a Physical Security Perimeter. (AC-7; AC-11; CIP-007-6 R5 Part 5.7)

4.11 **External identities.** Subcontractor and owner users of the project platform, and DSMS client users, must use MFA. DSMS client administrators manage their own users. (IA-8; IA-2(1))

4.12 **Physical access** to Hydro Physical Security Perimeters, control rooms, and gate houses is limited to authorized people; visitors are escorted and logged. (PE-2; PE-3; PR.AA-06; CIP-006-6 R1 and R2)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 and OT controls, CIP evidence reviews, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit remote access to OT that bypasses the Intermediate Systems.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog (P02); HPCDMS SSP (P02).
