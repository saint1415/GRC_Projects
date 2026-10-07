# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.MI-01, RC.RP-01, RC.RP-05, ID.IM-02 |
| Binding requirements served | SEC Form 8-K Item 1.05; utility addenda secs. 1 to 4 (CIP-013-2 R1.2 flow-down); FAR 52.204-23(c), 52.204-25(d), 52.204-30(c)(4); state breach laws (Fla. Stat. 501.171 worked example) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly, safely, and lawfully; keeps workers safe and plants in a known state during cyber events; meets SEC disclosure and contract notice deadlines; and restores grid equipment production in BIA order.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 7 plants, 9 service centers, 3 spare yards, and offices in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, including the acquired Ohio plant (AQ-01) from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant control systems (OT), test systems, and systems that suppliers operate for the company, and the products and services the company supplies to utilities (TMU firmware and configuration software, the Fleet Monitoring Service, and the Spare Transformer Reserve Service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for cyber incidents; runs the SOC |
| Director of OT Security | OT incident lead with the Vice President, Manufacturing Engineering |
| Plant managers | Safe-state and restart decisions at their plant |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| COO | Chairs the crisis management team |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Compliance Officer | Contract and regulatory notices from the notification matrix |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with ransomware that disrupts production of grid equipment (P08). (IR-8; RS.MA-01)
4.2 Workforce, plants, and suppliers must report suspected incidents to the SOC within 1 hour. Plant staff must report unexpected HMI or controller behavior to the shift supervisor immediately. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-03)
4.4 During a cyber incident the plant manager decides safe states for plant equipment; responders must not override process safety systems. No plant equipment may restart until controls engineering has verified its programs and settings and the plant manager approves. (IR-4; CP-10; RC.RP-05)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.MA-04)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.7 Contract and regulatory notices must meet the deadlines in the P08 notification matrix, including each utility's own incident notice deadline (24 or 48 hours), access-revocation notices within 1 business day, vulnerability disclosure within 30 days, FAR reports within their clauses' clocks, and breach notices under the law of each state where affected individuals reside. (IR-6; SR-8; RS.CO-02)
4.8 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; every plant must pass an OT controller program restore test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and one OT scenario a year, and after every acquisition. (IR-3; IR-8; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)
4.12 Evidence must be preserved with chain of custody before systems are rebuilt. (IR-4; AU-9; RS.AN-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Notification Standard (contract and regulatory notices)
- STD-03.3 Contingency and Disaster Recovery Standard
- STD-03.4 OT Recovery Standard
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Plant Safe-State and Manual Operations Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EPSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
