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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory drivers | 9 CFR 417.3(b), 418.2; 21 CFR 121.145, 121.157(b)(3); 21 U.S.C. 350f(d); 40 CFR 302.6, 355.40; Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, protects consumers by holding product that may be unsafe, meets FSIS, FDA, EPA, state, and SEC deadlines, and keeps plants and cold storage running safely during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, agency temporary workers, contractors, and interns) at the 8 plants, 4 distribution centers, headquarters, and regional offices in Florida, Georgia, Alabama, North Carolina, Tennessee, and Texas, including acquired operations from their acquisition date. Covers all IT and OT systems and data, including plant control systems, refrigeration controls, cloud, colocation, SaaS, and systems vendors operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| Director of OT Security | OT containment and recovery lead with plant controls engineers |
| Senior Vice President, Food Safety and Quality Assurance | Product hold, FSIS notice, and Reportable Food Registry decisions with plant FSQA managers |
| Director of Refrigeration and Process Safety | Refrigeration safe state and release reporting |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Deputy General Counsel, Privacy | Breach determinations for personal information |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with ransomware halting processing lines and cold-chain monitoring (P08). (IR-8; RS.MA-01)
4.2 Workforce, agency workers, and vendors must report suspected incidents to the SOC within 1 hour, including unexpected setpoint or formulation changes, signs of tampering, and monitoring alarms that stop arriving. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 Food safety first. When an incident affects process controls, CCP monitoring, formulations, or food safety records, the plant FSQA manager must hold affected product, evaluate it as an unforeseen deviation, and record the decision in the incident case before the case is closed. (IR-4; RS.MA-01)
4.5 Suspected tampering is a food defense event. At PLT-07 it must trigger the food defense corrective action procedure and a reanalysis decision; at other plants, the functional food defense plan's response steps. (IR-4; RS.MA-01)
4.6 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.7 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.8 Notifications must meet the deadlines in the P08 notification matrix: FSIS within 24 hours of determining adulterated or misbranded product entered commerce; the Reportable Food Registry within 24 hours for PLT-07 products; the National Response Center, LEPC, and SERC immediately for a reportable ammonia release; and state breach laws where affected individuals reside. (IR-6; RS.CO-03)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Tier-1 systems, including plant OT and the central MES, must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. Restored formulations must be verified against the signed masters before production restarts. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee, one with plant FSQA managers and controls engineers, and one after every acquisition. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register, the POA&M, and, where relevant, the food defense reanalysis. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 OT Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Product Hold and Regulatory Notification Procedure (FSIS, FDA, EPA)
- PRC-03.4 Multi-State Breach Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, OT monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.9), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPCM SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the PLT-07 food defense plan and the plant HACCP plans.
