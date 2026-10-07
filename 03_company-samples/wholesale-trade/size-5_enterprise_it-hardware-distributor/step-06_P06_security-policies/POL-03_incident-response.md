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
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Key regulatory drivers | DFARS 252.204-7012(c)-(e); FAR 52.204-25(d); FAR 52.204-23; Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security and supply chain incidents quickly and lawfully, meets federal reporting, breach notification, and SEC disclosure deadlines, and keeps orders shipping during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary workers supplied by staffing agencies, contractors, and interns) at headquarters, the 6 distribution centers, the 15 sales offices, and remote locations, including AQ-1 and any future acquisition from its closing date. Covers all systems and data, including cloud, colocation, SaaS, distribution-center OT, the FSCE, and systems that vendors, carriers, 3PLs, and drop-ship partners operate for the company, and the services offered to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Chief Supply Chain Officer | Product lead for counterfeit, tampered, or covered product incidents |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Director, Government Contracts | Owns DIBNet, Section 889, Kaspersky, and contracting officer reports |
| Chief Privacy Officer | Breach assessments and notifications for personal information |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, including ransomware and supplier compromise introducing tampered or counterfeit products (P08). (IR-8; RS.MA-01)
4.2 Workforce must report suspected incidents to the SOC within 1 hour; supplier, carrier, and partner contracts must require notice of incidents affecting the company. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to decide whether the event is a cybersecurity incident under 17 CFR 229.106(a) and to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 Federal reports must meet their clocks: DIBNet within 72 hours of discovering a cyber incident affecting covered defense information; covered telecommunications equipment within 1 business day of identification; Kaspersky covered articles within 3 business days; each followed by further information within 10 business days where the clause requires it. At least 3 staff must hold DoD-approved medium assurance certificates. (IR-6; RS.CO-02)
4.7 The Chief Privacy Officer must document a breach assessment for every incident involving personal information, and notifications must meet the law of each state where affected individuals reside (P08 notification matrix). (IR-6; RS.CO-03)
4.8 No ransom or extortion payment may be made without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and one supply chain scenario a year; the FSCE incident response capability must be tested annually. (IR-3; IR-8; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Federal Reporting Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Supplier Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Federal Incident and Covered Equipment Reporting Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC Program Office's internal assessments for the FSCE. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCFP SSP; FSCE CMMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
