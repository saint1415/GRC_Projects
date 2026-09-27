# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | CFO |
| Approved by | CFO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, CM-12, MP-6, SC-8, SC-28, SI-12, CP-9, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Benchmark and law | SP 800-82 Rev. 3 section 6.2.3 (data security); Fla. Stat. 501.171(2) |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure or change would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary workers) at headquarters, both field offices, the OCC, and every well site and facility. Covers all business IT and OT systems, including systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CFO | Owns classification; approves new uses of Restricted data |
| Production Accounting Manager | Data owner for royalty owner and production data |
| Reservoir Engineering Manager | Data owner for seismic and reservoir data |
| SCADA and Automation Supervisor | Data owner for controller programs, SCADA configurations, and OT network drawings |
| IT Manager | Implements encryption, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Royalty owner and employee Social Security numbers, driver license numbers, and bank details; employee vehicle location history; credentials; controller programs, SCADA configurations, and OT network drawings; seismic and reservoir interpretations (trade secret) | Encrypted at rest and in transit where technically feasible; need-to-know; approved systems only |
| **Confidential** | Daily production volumes, contracts, joint interest statements, security documents | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, field routes | Workforce only |
| **Public** | Website, published permits | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit. Where an OT device or protocol cannot encrypt, the exception must be documented with compensating controls (segmentation, physical protection) under POL-01 4.7. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))
4.3 Restricted data may be stored only in approved systems: production accounting, the HR and payroll service, the data platform (restricted folders), the SCADA servers and program repository, and the backup vault. Exports of royalty owner data must not be saved to shared file areas or sent by ordinary email; use the approved secure transfer. (AC-3; PR.DS-01)
4.4 The IT Manager must keep an inventory of where Restricted data is stored and which vendors receive it. (CM-12; ID.AM-07)
4.5 Media and devices holding Restricted data, including retired HMIs, controllers, and tablets, must be wiped (for reuse) or destroyed with a certificate of destruction (for disposal). (MP-6; ID.AM-08)
4.6 **Backups.** Backups of Restricted and operational data must be encrypted, stored apart from production (separate cloud account and, for SCADA, an offline copy at a different site), protected from alteration or deletion, and restore-tested at least quarterly. Current controller programs must be kept in the program repository and included in the offline copy. (CP-9; PR.DS-11)
4.7 Restricted and Confidential data must not be entered into AI tools or other third-party services unless the tool is on the approved list (see P10 and POL-05) and the supplier has signed the security schedule (POL-01 4.9). (SA-9)
4.8 Records are retained according to the company records retention schedule. Security documentation is retained per POL-01 4.12. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; records retention schedule; Fla. Stat. 501.171
