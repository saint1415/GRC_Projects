# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer (with the Vice President, Resilience and Emergency Management for Restricted infrastructure information) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, SC-8, SC-28, CP-9, MP-6, SI-7, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(d)); state breach and disposal laws (Fla. Stat. 501.171(2), (8) worked example) |

## 1. Purpose
Classify company information so that infrastructure details useful to an attacker and customer personal information get the protection they need, and keep process and compliance data accurate.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in all four regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee and in the two service lines, including acquired systems from their acquisition date. Covers all IT and OT systems and data: SCADA, PLCs, RTUs, telemetry, and HMIs at the 126 community water systems and 5 ROCCs; cloud, colocation, and SaaS; and systems that vendors and integrators operate or support for the company, including the services offered to municipal clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns this policy for customer and employee personal information |
| Vice President, Resilience and Emergency Management | Owns Restricted infrastructure information (RRAs, ERPs) |
| Data owners | Classify data and approve access |
| All workforce | Label and handle data by class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether the 2026 independent assessment tested it (P07).

4.1 All information must be classified as Restricted (RRAs, ERPs, SCADA network diagrams, OT asset inventories, credentials, and maps of critical assets), Confidential (customer and employee personal information, bank account numbers, non-public financial information), Internal, or Public. (RA-2; ID.AM-05)
4.2 Restricted information must be kept only in the restricted repository or in OT systems, shared on a need-to-know basis, and never sent outside the company except by Legal-approved channels. (AC-3; PR.DS-01)
4.3 Confidential and Restricted information must be encrypted at rest and in transit with FIPS-validated cryptography, except inside OT control zones where the SP 800-82 Rev. 3 tailoring record documents compensating controls. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.4 Customer personal information must be collected only for billing, service, and legal duties; every extract outside the CIS must be registered, and unregistered extracts are deleted after 90 days. (SI-12; PR.DS-01)
4.5 Payment card numbers must never be entered or stored in company systems; customers pay only through the payment processor's hosted pages and IVR. (AC-3; PR.DS-01)
4.6 IT backups must be immutable and copied off site. Offline backups of PLC logic, HMI projects, and SCADA server images must be taken monthly and after every approved change, kept at two sites, and restore-tested at least annually. (CP-9; PR.DS-11)
4.7 Process, water quality, and compliance data must not be altered; any correction must be logged with the reason and the approver. (SI-7; PR.DS-01)
4.8 Media and devices must be sanitized per NIST SP 800-88 before reuse or disposal, and customer records disposed of so they are unreadable. (MP-6; PR.DS-01)
4.9 Records must be retained per the retention schedule, including RRAs and ERPs for at least 5 years after each certification. (SI-12; PR.DS-01)
4.10 Restricted information may be shared with government agencies only through Legal, which decides whether to request protection for it (for example as Protected Critical Infrastructure Information). (AC-3; GV.OC-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard (IT and OT)
- STD-04.4 Restricted Infrastructure Information Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, the annual independent assessment by Internal Audit and the co-sourced OT assessment firm (P07), and plant drills. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GCR-WTSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; each covered system's RRA and ERP.
