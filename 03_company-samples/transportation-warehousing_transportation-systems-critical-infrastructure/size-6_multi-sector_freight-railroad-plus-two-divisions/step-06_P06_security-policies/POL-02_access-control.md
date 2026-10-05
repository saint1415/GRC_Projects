# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO, with the Group identity director |
| Approved by | Group CISO, after review by the division security and compliance leads |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-17, IA-2, IA-2(1), IA-5, MA-4, CA-3 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| TSA and other | SD 1580/82-2022-01E III.C.1-6; FAR 52.204-21(b)(1)(i), (ii), (v), (vi) |
| Division supplements | Freight Railroad: dispatch console compensating controls, PTC key custody, CTC accounts. Transload and Wholesale: terminal kiosks and loading rack vendors. Real Estate: building OT vendor consoles |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems, with the least access they need, and that shared and vendor access to OT is controlled.

## 2. Scope
All accounts on group IT and OT systems, including the rail OT directory, cloud consoles, SaaS applications, terminal and building OT, and vendor and customer accounts.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (SSO, MFA, PAM, identity governance) |
| System owners | Approve access to their systems; certify it every quarter |
| Director, Rail OT Security | Rail OT directory, CTC and PTC accounts, the CIP access measures |
| Division security and compliance leads | Terminal and building OT accounts; vendor access approvals |
| HR | Reports joiners, movers, and leavers the same day |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are prohibited except where critical for operations and approved by the division security and compliance lead; approved shared accounts must be vaulted in PAM and checked out by named people. (AC-2; IA-2; PR.AA-01; SD III.C.4)

4.2 Access must follow least privilege and separation of duties. Where a system cannot enforce them, the system owner must document compensating controls. (AC-6; AC-5; PR.AA-05; SD III.C.3)

4.3 MFA is required for all remote access, all privileged access, email, cloud consoles, and every system holding FCI or personal information. Where OT components cannot support MFA, the compensating controls must be documented and, for Critical Cyber Systems, described in the CIP. (IA-2(1); IA-2(2); PR.AA-03; SD III.C.2)

4.4 Memorized secrets follow NIST SP 800-63: no forced periodic change, but a reset is required on evidence of compromise and whenever a person who knew a shared secret leaves or changes role. Components that cannot follow this rule must have documented mitigations and a timeframe. (IA-5; SD III.C.1, III.C.4.b)

4.5 Accounts must be disabled within 4 hours of termination and access reviewed within 5 days of a transfer. Privileged and OT access must be certified quarterly; other access every 6 months. (AC-2; AC-2(3); PS-4; PR.AA-05)

4.6 Directory and domain trust relationships must be documented, justified, and reviewed at least annually. No trust may exist between an OT directory and the corporate directory without approval by the Group CISO. (AC-3; CA-3; SD III.C.5)

4.7 Vendor remote access to any OT (dispatch, PTC, CTC, wayside, terminal racks and tank controls, building systems) must go through group PAM with MFA, per-session approval, time limits, and session recording. Always-on vendor access and vendor-owned modems are prohibited. (AC-17; MA-4; PR.IR-01)

4.8 Privileged administration must use separate privileged accounts checked out through PAM. (AC-6(5); PR.AA-05)

4.9 Physical access to NOCs, data centers, terminal control rooms, and building OT rooms must be limited to authorized people and logged. PTC components on locomotives must be kept in locked, sealed housings, as the CIP specifies. (PE-3; PR.AA-06; SD III.C.6)

4.10 Customer and tenant users (CDS customers, wholesale customers, tenants) must have MFA available, and it is required for CDS customers. (IA-8; PR.AA-03)

## 5. Compliance and enforcement
Checked through quarterly certifications and the P07 assessment (AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5, AC-17).

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; `division-supplements.md`; P02 common control catalog; the CIP access control section (SSI).
