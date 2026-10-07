# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Compliance Officer (with Privacy Counsel for personal information) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-7, SI-12, CP-9, AC-16 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 6.2.3 (data security), 6.2.4 (backups) |

## 1. Purpose
Classify the company's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including integrity rules for production volumes and controller logic.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary workers, including the roughly 4,000 contractor workers on company sites on a typical day) at headquarters, the IOC, the BCC, the Florida regional control room, 60 field offices and yards, and every well site and facility in the Permian, Mid-Continent, and Florida operating areas, including acquired assets (AQ-MC) from the date of closing. Covers all business IT and OT systems and data, including cloud, colocation, SaaS, field devices and communications, systems that vendors operate for the company, and the services the company offers to outside parties (SL-1 owner and partner services; SL-2 water services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification; approves new uses of Restricted data |
| Privacy Counsel (Legal) | Personal information rules and breach determinations |
| Data owners (system owners) | Classify their data; approve access |
| Vice President, Production and Revenue Accounting | Volume and owner data integrity rules (STD-04.4) |
| Vice President, Operations Technology and Automation | Controller logic, setpoint, and SCADA configuration integrity and backups |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All information must be classified as Restricted, Confidential, Internal, or Public. Restricted includes owner and employee personal information (taxpayer numbers, bank accounts, driver license numbers, health plan identifiers, geolocation), seismic and reservoir data, controller logic, and SCADA network and security details. (RA-2; AC-16; ID.AM-07)
4.2 Restricted and Confidential data must be encrypted at rest and in transit with approved cryptography (STD-04.1). Where legacy OT protocols cannot be encrypted, traffic must stay on private networks with monitoring until replaced (tailoring TR-06). (SC-8; SC-28; SC-13; PR.DS-01)
4.3 Restricted data must not be stored on file shares or sent by email outside approved secure transfer; owner bank details must be tokenized in reports and exports. (AC-3; SC-8; PR.DS-01)
4.4 Production volumes, run tickets, and LACT tickets must be protected against unauthorized change: every edit needs a reason code and an audit record, and SCADA, LACT, and accounting volumes must be reconciled daily (STD-04.4). (SI-7; AU-2; SI-10; PR.DS-01)
4.5 Controller logic, SCADA configuration, and historian data for every operating area must be backed up to a central repository, with an offline or immutable copy in a different location, and restore-tested at least annually (STD-04.3). (CP-9; CP-9(3); PR.DS-11)
4.6 Media and devices that held Restricted data, including retired HMIs and field controllers, must be sanitized before reuse or disposal and the sanitization recorded. (MP-6; PR.DS-01)
4.7 Restricted data must not be entered into AI tools unless the AI council has approved that tool for that class of data with no-training and deletion terms. (AC-3; PL-4; PR.DS-01)
4.8 Owner and employee records must include the state of residence so that breach notices can follow the law of each state where affected individuals reside. (SI-12; IR-6; ID.AM-07)
4.9 Records must be retained and destroyed according to the records retention schedule; personal information must not be kept longer than the schedule allows. (SI-12; ID.AM-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard (IT and OT)
- STD-04.4 Production Data Integrity Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT monitoring at the control centers), the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Contractor violations are handled under the contractor's agreement and can end site access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. OT exceptions also need the Director of OT Security's sign-off.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FSPA SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; NIST SP 800-82 Rev. 3.
