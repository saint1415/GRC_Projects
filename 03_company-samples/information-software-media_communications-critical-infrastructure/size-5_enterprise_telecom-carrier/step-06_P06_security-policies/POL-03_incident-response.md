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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory basis | 47 CFR 64.2009(f), 64.2011; 47 CFR 4.9, 4.18; 47 CFR 1.20003(c); Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully; meets the CPNI, outage, CALEA, SEC, and state notification deadlines; and keeps voice, 911, and broadband service running during incidents.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) and the agents of care vendors and other third parties who use company systems, in all four states, including acquired carriers from their closing date. Covers all systems and data, including the carrier network and its management plane, the lawful-intercept platform, cloud, data centers, SaaS, and systems that vendors operate for the company, and the services offered to business customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Vice President, Network Operations Center | Service impact decisions, PSAP and 988 notices, NORS and DIRS |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | CPNI breach determination and notifications |
| Director, Lawful Intercept Compliance | CALEA compromise reports |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with a network intrusion exposing CPNI (P08). (IR-8; RS.MA-01)
4.2 Workforce, acquired carriers, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified under STD-03.1, and tracked to closure. The Chief Privacy Officer, with counsel, must document the date and basis of any reasonable determination of a CPNI breach. (IR-5; IR-4; RS.MA-02)
4.4 For a CPNI breach, the USSS and FBI must be notified through the FCC reporting facility as soon as practicable and no later than 7 business days after reasonable determination (internal target: 2 business days). Customers and the public must not be told until 7 full business days after that notice, unless the investigating agency agrees or directs otherwise. The breach record must be kept at least 2 years. (IR-6; RS.CO-02)
4.5 Containment actions that could affect voice, 911, or broadband service must be approved jointly by the incident commander and the NOC. Outages that potentially affect a 911 or 988 special facility must be notified to it within 30 minutes of discovery, and reportable outages filed in NORS on time. (IR-4; CP-2; RS.CO-02)
4.6 Any compromise of a lawful interception or of call-identifying information, and any unlawful electronic surveillance on company premises, must be reported by the CALEA senior officer to the affected law enforcement agencies within a reasonable time upon discovery. (IR-6; RS.CO-02)
4.7 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.8 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay under Item 1.05(c), or the 64.2011 hold applies and the company has filed EDGAR correspondence under Item 1.05(d) by the original due date. (IR-6; RS.CO-02)
4.9 If an opt-out mechanism fails to a degree that customers' inability to opt out is more than an anomaly, written notice must be given to the FCC within 5 business days. (IR-6; RS.CO-02)
4.10 No ransom or extortion payment may be made without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.11 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.12 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and the NOC, and after every acquisition. (IR-3; IR-8; ID.IM-02)
4.13 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard (including the 12-month update rule for the state law matrix)
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 CPNI Intrusion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 PSAP, 988, and NORS Notification Procedure
- PRC-03.5 CALEA Compromise Reporting Procedure (restricted distribution)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CPNI certification evidence package. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of a vendor agent's access, in proportion to intent and harm. Misuse of CPNI is always a sanctionable violation.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OSS/BSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
