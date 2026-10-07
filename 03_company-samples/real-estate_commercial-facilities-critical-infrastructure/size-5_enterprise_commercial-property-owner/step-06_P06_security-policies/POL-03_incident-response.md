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
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory drivers | CPG 2.0 goals 1.C, 4.B, 5.A, 5.B, 6.A (R05); Form 8-K Item 1.05 (R04); state breach laws; PCI DSS Req. 12.10.1 (R01) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, keeps occupants safe and buildings operating during outages, and meets breach notification, contractual notice, and SEC disclosure deadlines.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and TRS staff) at all 140 operated properties in Florida, Texas, Georgia, North Carolina, Arizona, and California, including acquired properties from their acquisition date. Covers all systems and data: IT, OT (building automation, access control, video), cloud, colocation, SaaS, systems that integrators and other vendors operate for the company, and the services the TRS offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the Cyber Defense Center |
| Senior Vice President, Engineering | OT safety lead: building safety and degraded-mode operations |
| Vice President, Corporate Security | Physical security and RSOC operations during incidents |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach determinations and notification decisions |
| Chief Operating Officer | Chairs the crisis management team |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with ransomware on building automation systems (P08). (IR-8; RS.MA-01)
4.2 Workforce members, property staff, integrators, and vendors must report suspected incidents to the Cyber Defense Center within 1 hour, including OT events such as unexplained setpoint changes, door unlocks, or remote sessions nobody approved. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in the case management system. (IR-5; IR-4; RS.MA-02)
4.4 In an OT incident, chief engineers must make the building safe first (local hand control and manual rounds) before containment changes reach OT systems, and nobody may power off or reset field controllers or door controllers without the Director of OT Security's approval. (IR-4; CP-2; RS.MI-01)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.7 The Chief Privacy Officer must document, with counsel, whether personal information was accessed and the date of each breach determination, and notifications must meet the deadlines in the P08 notification matrix, including state laws where affected individuals reside, lease notice clauses, and client contracts. (IR-6; RS.CO-03)
4.8 No ransom may be paid without approval from the CEO, the CFO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; BAS platforms must be restore-tested at sampled properties every quarter, and each RSOC must take over another region for a full shift at least once a year. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 Every property must have written degraded-mode procedures for running plant equipment, lighting, and doors by hand, tested at least annually. (CP-2; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and engineering, and after every major change such as an acquisition. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Disclosure Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- STD-03.4 OT Incident and Degraded-Mode Operations Standard
- PRC-03.1 BAS Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Tenant and Contractual Notice Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 BAACS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
