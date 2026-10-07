# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, IA-1, IA-2, AC-2, AC-3, AC-6, AC-5, IA-2(1), IA-2(2), PS-4, AC-2(3), AC-6(9), AC-17, MA-4, IA-5, AC-4 |
| CSF 2.0 | PR.AA-01, PR.AA-05, PR.AA-03 |
| Regulatory drivers | N23-R01 (52.204-21(b)(1)(i), (ii), (v), (vi)); N23-R03 (SP 800-171 R2 3.5.3; 252.204-7012(b)(2)); SOX IT general controls; client contract security terms |

## 1. Purpose
Make sure only authorized people, services, and devices reach company systems and client building systems, with the least privilege needed, strong authentication, and separation between the people who change payees and the people who release payments.

## 2. Scope
All Cris Santos Company workforce members (employees, craft workers, contractors, and interns) at headquarters (HQ-1), the nine regional offices, about 140 jobsites, the two yards, and the two colocation data centers in eight states, including acquired businesses (AQ-1 and AQ-2) from their acquisition date. Covers all company systems and data, including cloud, colocation, SaaS, the Federal Programs CUI Enclave (FPCE), jobsite technology, client building systems that BTS administers, systems that vendors and subcontractors operate for the company, and the services the company offers to external clients (SL-1 and SL-2). Subcontractor and design-team users of company systems are bound by the security terms in their subcontracts and access agreements.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-04), PAM, and identity governance |
| System owners (for the PDPP: Vice President, Project Controls and Systems) | Approve role templates and access; complete certifications |
| Project managers | Invite and remove external SYS-01 users on their projects; certify them monthly |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including AQ-1 and AQ-2 |
| Vice President, Integration Management Office | Brings acquired-business identities onto the identity platform |
| Vice President, Building Technology Services | Client-system credential vault and technician remote access |
| Director, CMMC Program Office | Separate FPCE identities and enclave administrators |

Role overlaps are limited by design: Internal Audit (third line) never operates the controls it tests, and the people who maintain payees never release payments (POL-02 4.3).

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in the 2026 PDPP assessment (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited, except time-capture kiosk accounts that cannot reach FCI. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No one person may both create or change a payee and release a payment. All wires and all ACH batches above $250,000 need two approvers. (AC-5; PR.AA-05)
4.4 MFA is required for all access to company systems. Privileged users, payment roles, executives, and FPCE users must use phishing-resistant authenticators; project management staff must use them by 2027-03-31. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations, including in acquired businesses. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days must be disabled automatically. External users must be removed within 30 days of project closeout or after 90 days of inactivity. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; project managers must certify external users on their projects every month. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and BTS technician remote access must go through the remote access gateway with approval and session recording. Client system credentials must be kept only in the BTS vault and rotated when a technician leaves the account. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device or system is connected, including devices installed for clients before turnover. (IA-5; PR.AA-01)
4.11 FPCE identities must be separate from commercial identities, with no federation, password synchronization, or shared administrators. (IA-2; AC-4; PR.AA-01)
4.12 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot weaken it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote, Vendor, and Client-System Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure (including monthly external-user review)
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, monthly payment-control exception reports, the annual Internal Audit assessment (P07), and the CMMC self-assessments (P03). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor and vendor violations are handled under their contracts and can lead to removal of access or the subcontract.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception can change how a CMMC requirement is scored.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 enterprise risk register; P02 PDPP SSP; P03 regulatory gap analysis (including the FPCE readiness check); P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; FPCE SSP (separate, CMMC Level 2).
