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
| Implements (SP 800-53 Rev. 5) | IR-8, IR-6, IR-4, IR-5, CP-2, CP-4, CP-10, IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03, RC.RP-04 |
| Binding rules served | SEC 8-K 1.05; State breach laws (Fla. Stat. 501.171(3)-(5)); E-Verify MOU Art. II.A.16; Fla. Stat. 448.095(2)(c); E-Verify MOU Art. II.A.8 |

## 1. Purpose
Make sure the firm detects, contains, recovers from, and reports security incidents quickly and lawfully, meets breach notification, E-Verify, client, agency, and SEC disclosure deadlines, and keeps associates paid during outages.

## 2. Scope
All Cris Santos Company internal employees, contractors, and temporary associates while they use company systems (the associate app, time clocks, kiosks), at all of its about 520 sites in 38 states and the District of Columbia, including acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors operate for the firm, and the services the firm offers to clients (SL-1 Workforce Management Platform and SL-2 payrolling).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach risk assessment and notification decisions in each state |
| Senior Vice President, Payroll and Associate Services | Payroll continuity (prior-week advance procedure) |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The firm must maintain an incident response plan and runbooks for its most likely severe incidents, starting with a payroll and HR system breach exposing worker personal information (P08). (IR-8; RS.MA-01)
4.2 Workforce, acquired firms, and vendors must report suspected incidents to the SOC within 1 hour, including suspected payroll fraud reported to the Associate Service Center. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1 (raised one level inside the weekly payroll window), and tracked to closure in SOC case management. (IR-4; IR-5; RS.MA-03)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 The Chief Privacy Officer must decide breach notifications under the law of each state where affected individuals reside (PRC-03.3), and DHS must be notified immediately of any suspected or confirmed breach of E-Verify personal data. (IR-6; RS.CO-02)
4.7 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.8 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05), including the prior-week advance procedure for payroll, and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.9 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee, and after major organizational changes such as an acquisition or new committee members. (IR-3; IR-8; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)
4.11 When E-Verify is unavailable, the onboarding team must document the outage for each day it lasts and create the cases after recovery (PRC-09.3). (CP-2; RC.RP-04)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Contingency and Disaster Recovery Standard
- STD-03.3 Breach Notification Standard
- PRC-03.1 Payroll and HR Data Breach Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Payroll Engine Recovery Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and the fraud and KRI dashboards. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ALPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
