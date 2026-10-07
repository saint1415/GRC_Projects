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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-4(2), CP-7, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| HIPAA Security Rule | 164.308(a)(6), (a)(7); breach notification 164.400-164.414 |

## 1. Purpose
Make sure the company keeps dispatching ambulances during any cyber or technology incident, detects and contains incidents quickly, meets every notification and disclosure duty on time, and learns from each incident.

## 2. Scope
All Cris Santos Company workforce members (employees, field clinicians, dispatchers, contractors, students, and volunteers) at all 231 sites and in every ambulance, including acquired operations from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, communications centers, fleet devices, and systems that business associates and other vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; owns this policy |
| Communications center supervisors | Start manual dispatch and notify county PSAPs without waiting for the security response |
| Chief Operating Officer | Chairs the crisis management team |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach risk assessments and notifications |
| Vice President, Government Relations and County Contracts | County contract notices |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with ransomware against computer-aided dispatch (P08). (IR-8; RS.MA-01)
4.2 Workforce, acquired operations, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 The Chief Privacy Officer must document a four-factor breach risk assessment (45 CFR 164.402) for every incident involving PHI, and notifications must meet the deadlines in the P08 notification matrix, including state laws where affected individuals reside and duties to SL-1 and SL-2 clients as a business associate. (IR-6; RS.CO-03)
4.7 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.8 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.9 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee, and after every major organizational change such as an acquisition. (IR-3; IR-8; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)
4.11 Every communications center must drill manual dispatch at least quarterly and be able to hand its positions to another center; center-to-center failover must be tested at least annually for each center (STD-03.4). (CP-4(2); CP-7; RC.RP-01)
4.12 When dispatch moves to manual mode or a CAD-to-CAD interface fails, the dispatch supervisor must notify the affected county PSAPs immediately and the county contract manager as each agreement requires (PRC-03.4). (IR-6; RS.CO-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- STD-03.4 Manual Dispatch and Center Failover Standard
- PRC-03.1 CAD Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 County Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EDPCP SSP; P05 BIA; P08 runbook and notification matrix; applicable regulations listed in P03.
