# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-7, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3.8 (incident response capability), 6.4 (respond), 6.5 (recover) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, keeps the field safe and under control during outages, meets SEC disclosure, PHMSA, EPA, and state breach deadlines, and restores remote operations within the BIA objectives.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary workers, including the roughly 4,000 contractor workers on company sites on a typical day) at headquarters, the IOC, the BCC, the Florida regional control room, 60 field offices and yards, and every well site and facility in the Permian, Mid-Continent, and Florida operating areas, including acquired assets (AQ-MC) from the date of closing. Covers all business IT and OT systems and data, including cloud, colocation, SaaS, field devices and communications, systems that vendors operate for the company, and the services the company offers to outside parties (SL-1 owner and partner services; SL-2 water services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Director of OT Security | OT incident lead; decides with operations on isolating the IT/OT boundary |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| Chief Operating Officer and regional Vice Presidents of Operations | Manual operations and shut-in decisions; crisis management team |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Privacy Counsel (Legal) | Breach determinations and state notification decisions |
| Vice President, Health, Safety, and Environment; Pipeline Compliance Manager | EPA and PHMSA release notices (PRC-03.4) |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan with an OT annex and runbooks for its most likely severe incidents, starting with ransomware that spreads from business IT toward field SCADA (P08). (IR-8; RS.MA-01)
4.2 Workforce, contractors, acquired sites, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1 (including OT and safety impact), and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 Production Controllers may isolate the IT/OT boundary and move an operating area to manual operations on the OT incident lead's call without waiting for executive approval. Safety shutdowns must never be bypassed to keep producing during an incident. (IR-4; CP-2; RS.MI-01)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.MA-04)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.7 Privacy Counsel must document a breach determination for every incident involving personal information, and notices must meet the deadlines in the P08 notification matrix under the law of each state where affected individuals reside. (IR-6; RS.CO-03)
4.8 A release that follows a cyber incident must be reported under PRC-03.4: immediately to the National Response Center for a reportable oil discharge (40 CFR 110.6), and within one hour of confirmed discovery for a qualifying release from a regulated rural gathering line (49 CFR 195.52), with an initial estimate made by the manual method when SCADA data is unavailable. (IR-6; IR-8; RS.CO-02)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Tier-1 systems, including the SCADA platform at the IOC, BCC, and Florida, must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; the IOC-to-BCC failover must be tested at least once each calendar year. (CP-2; CP-4; CP-7; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee using an OT scenario, and after every acquisition. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard (with OT roles)
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard (includes regional manual operations)
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Regulatory Release Reporting Procedure (PHMSA and EPA)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT monitoring at the control centers), the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Contractor violations are handled under the contractor's agreement and can end site access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. OT exceptions also need the Director of OT Security's sign-off.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FSPA SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; NIST SP 800-82 Rev. 3.
