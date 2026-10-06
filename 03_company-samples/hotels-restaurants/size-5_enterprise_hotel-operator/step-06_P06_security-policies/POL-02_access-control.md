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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory basis | PCI DSS 7, 8; FTC Act Section 5 |

## 1. Purpose
Make sure only authorized people and processes reach the company's information and systems, including the PMS and CRS used by franchisee staff, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at headquarters, the regional offices, the contact center, and the 110 company-operated hotels in 33 states and DC, including acquired hotels from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, payment devices, and hotel building and guest-room technology, and the systems and services the company provides to franchisees and distribution clients (SL-1 and SL-2). Franchisees are bound through the brand technology standards and the franchise agreement, not directly by this policy.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-09) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Franchisee hotel administrators | Request and attest to their staff's PMS and CRS accounts under BS-TECH-02 |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Integration Management Office | Brings acquired-hotel identities onto the identity platform |
| Vice President, Hotel Technology | Sponsors vendor access to property systems |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce and franchisee staff; POS and device service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. The PMS card display permission may be granted only to roles approved by the Director of Payments and PCI Compliance and must be reviewed monthly. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person both change vault keys or payment configuration and approve the change, or both create and approve a refund above the set limit, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all access into the cardholder data environment, all PMS and CRS users including franchisee staff, and all cloud and administrative access. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Workforce and franchisee accounts inactive for 90 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; franchisee hotel administrators must attest to their users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access, including POS, door lock, and building system vendors, must go through the zero-trust or PAM gateway with approval, MFA, and session recording. Vendor-managed, always-on remote tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device or system is connected to a company or hotel network. (IA-5; PR.AA-01)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)
4.12 Loyalty members must use MFA or a passkey before redeeming points or changing profile, payment, or contact details. (IA-8; PR.AA-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's PCI DSS assessments, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Franchisee violations of brand technology standards are handled under the franchise agreement.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; brand technology standards BS-TECH-01 to BS-TECH-06.
