# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 (approved 2026-09-15) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PE-3, PE-8, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | N23-R01 FAR 52.204-21(b)(1)(i), (ii), (v), (vi), (ix); N23-R04 32 CFR 170.15 (Level 1) and NIST SP 800-171 R2 families 3.1 and 3.5 (Level 2 enclave); N53-R04 PCI DSS Requirement 8 (parking) |
| Division supplements | Construction: TSSI client credentials and jobsite trailers. Property: integrator access and parking portal accounts. A&E: enclave guest accounts for subconsultants |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services; the external identities (owners, subcontractors, design consultants, tenants) that group systems authenticate; integrator and technician access to building systems; and physical access to locations where FCI or CUI is handled, including jobsite trailers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| PDPP system owner | Runs external user accounts in the PDPP |
| Enclave operations manager | Runs identities inside the CUI enclave's authorized boundary |
| Project executives and data owners | Approve project roles and access to their data |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Systems Integration Director | Custodian of client system credentials (TSSI) |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited. A documented exception (for example, a building controller that supports only one account) must have compensating controls and be recorded under POL-01 4.10. (IA-2; AC-2; PR.AA-01; FAR 52.204-21(b)(1)(v))

4.2 Access must be role-based and least privilege. Project roles must be approved by the project executive, and access to CUI must be approved by the federal practice leader for that DoD project. (AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(i)-(ii))

4.3 **MFA.** MFA is required for all workforce access. Administrators, finance and treasury staff, project executives, and SAM Entity Administrators must use phishing-resistant authenticators. All other workforce users must use at least number-matching MFA, and must move to phishing-resistant authenticators for remote access by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2)

4.6 Managers and data owners must certify access every quarter, including privileged and service accounts. (AC-2; AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after no more than 60 minutes idle (stricter where a division supplement says so). (AC-7; AC-11; AC-12)

4.9 **External users.** PDPP accounts for owners, subcontractors, and design consultants must expire automatically at project closeout and be disabled after 90 days of inactivity. MFA is required for owner approvers and subcontractor administrators by 2027-03-31 and offered to all other external users. Subcontractors must report leavers within 5 business days, as their subcontracts require. (AC-2(3); IA-8; PS-7; PR.AA-01)

4.10 **Vendor, integrator, and technician access** (including to building systems and TSSI client systems) must go through group PAM with named accounts, MFA, approval, and recording. Persistent vendor tunnels and integrator-owned VPNs are prohibited. (AC-17; MA-4; PR.AA-05)

4.11 **Client system credentials** held by the TSSI unit must be stored in per-client vault partitions, released only for an approved work order, and rotated when a system is handed over to the client and when a technician with access leaves. (IA-5; AC-6; PR.AA-05)

4.12 **SAM and SPRS roles.** Each contracting entity must have no more than 3 SAM Entity Administrators, each using phishing-resistant MFA. SAM EFT data must be reconciled to the bank every month. (AC-6; IA-2(1); FAR 52.232-33)

4.13 **Physical access where FCI or CUI is handled.** Offices, plan rooms, and jobsite trailers that hold FCI or CUI must limit physical access to authorized people. Visitors must be escorted and logged; jobsite trailers use the electronic visitor sign-in on the trailer tablet. Visitor logs must be kept for 1 year and reviewed monthly. (PE-3; PE-8; PR.AA-06; FAR 52.204-21(b)(1)(viii)-(ix))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls and division samples, quarterly certification results, and the CMMC self-assessments.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04 (CUI and FCI handling); `division-supplements.md`; common control catalog entries for SYS-G1 (P02); PDPP SSP (P02); enclave SSP.
