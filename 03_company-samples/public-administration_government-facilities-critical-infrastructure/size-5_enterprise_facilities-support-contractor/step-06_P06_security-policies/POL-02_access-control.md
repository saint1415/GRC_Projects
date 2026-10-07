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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new contract types |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Contract and legal basis | State exhibits (AC and IA families); FAR 52.204-21(b)(1)(i), (ii), (v), (vi); FAR 52.204-9(b) |

## 1. Purpose
Make sure only authorized people and processes reach company systems, customer building systems, and customer data, only to the extent their role requires, and that access ends promptly when it is no longer needed. Access to door control and building automation is treated as access to physical safety.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor personnel working under company accounts) in all segments and acquired businesses from their acquisition date, in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, and the District of Columbia. Covers all company systems and data (cloud, colocation, SaaS, ROCs, endpoints, and the OT edge), the company's administration of customer building systems through the IBOP, customer data the company holds, and systems that vendors and subcontractors operate for the company. GSA systems that company staff use under GSA's authorization are governed by GSA policy; this policy governs the company staff who use them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-02), PAM, and identity governance |
| Director of OT Security | Runs the OT remote access gateway and device credential vault |
| Managers and system owners | Approve access; complete quarterly certifications |
| Customer tenant administrators | Approve access levels and manage their own console users under STD-02.3 |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events; PIV card collection |
| Vice President, Integration Management Office | Brings acquired identities and remote access onto enterprise platforms |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its contract or regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited for workforce, subcontractors, and customer console users; device and service account passwords must be held in the PAM vault. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted; access levels inside a customer tenant also need the customer's approval. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 No one may both approve and enter an access-level or door schedule change, or both create and pay a vendor. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, cloud and administrative access, the IBOP, the FSP, and the customer console. Privileged users, OT gateway users, and roles that can change doors, schedules, or controller programs must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. PIV cards must be collected and returned to GSA. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 45 days, and customer console accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; customer tenant administrators must attest to their console users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 All remote access to customer OT networks, by technicians, subcontractors, and vendors, must go through the OT remote access gateway with approval tied to an FSP ticket and session recording. Always-on remote-support tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device is connected or handed over at commissioning, and device credentials must be stored in the PAM vault. (IA-5; CM-6; PR.AA-01)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)
4.12 Badge revocations requested by a customer must be applied in the PACS within 1 hour when marked urgent and within 4 hours otherwise. (AC-2; PS-4; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Customer Console and Tenant Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged and OT Remote Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Badge Enrollment and Revocation Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and customer audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor violations are handled under the subcontract and may end the subcontractor's access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception never waives a customer contract term or a law.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 IBOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the contract obligations register.
