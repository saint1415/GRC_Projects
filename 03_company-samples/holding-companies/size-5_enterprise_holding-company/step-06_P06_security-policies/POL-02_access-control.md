# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (holding company, GBS, and all subsidiaries) |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-14 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-6(9), AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory drivers | 16 CFR 314.4(c)(1), (c)(5) for Finance; SOX IT general controls (N55-R03); 45 CFR 164.314(b)(2)(ii) for plan PHI (N55-R06) |

## 1. Purpose
Make sure only authorized people and processes reach the group's information and systems, only to the extent their role requires; that credentials cannot be reset by someone pretending to be the user; and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the holding company, Global Business Services (GBS), and every subsidiary (Building Products, Home Services, Manufacturing, and Finance), at all sites in the six operating states, including acquired businesses from their closing date. Covers all systems and data, including cloud, data centers, SaaS, plant OT, systems that vendors operate for the group, and the services offered to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the group identity platform (SYS-04), PAM, and identity governance |
| Managers and system owners | Approve access; complete certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events for employees and contractors |
| Outsourced service desk provider | Performs credential resets only under PRC-02.5 |
| Vice President, Integration Management Office | Brings acquired-business identities onto the group platform |
| Dealer and customer administrators (SL-1, SL-2) | Manage their own staff's accounts under their agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited. Every service account must have a named owner and be vaulted in PAM or replaced by a managed identity. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No one may hold roles that allow them both to change vendor bank details and release payments, to prepare and approve the same journal, or to administer and approve in the same system. (AC-5; PR.AA-05)
4.4 MFA is required for all access. Privileged users, treasury users, and payment approvers must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 A password or MFA reset may be performed only after verified identity proofing under PRC-02.5 (live video check against the HR photo record, or an in-person check). Knowledge-based questions alone are never enough. This applies to the outsourced service desk. (IA-5; PR.AA-02)
4.6 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. Contractors must be recorded in the HRIS so their end dates drive the same process. (PS-4; AC-2; PR.AA-05)
4.7 Workforce accounts inactive for 60 days, and dealer and customer accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.8 Access to SOX systems and to systems with Finance customer information must be certified quarterly; other access semiannually. (AC-2; PR.AA-05)
4.9 Privileged access must be granted just in time through PAM and recorded. Directory administration must follow the tiering model, and no service account may hold domain administrator rights. (AC-6; AC-6(5); AC-6(9); PR.AA-05)
4.10 Remote and vendor access, including integrator access to plant OT, must go through the zero-trust or PAM gateway with approval and session recording. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the CISO. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification, Authentication, and Account Recovery Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Identity-Verified Credential Reset Procedure (service desk)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly sub-certifications, access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SCSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; Finance WISP annex (SUP-FIN); Manufacturing OT annex (SUP-MFG).
