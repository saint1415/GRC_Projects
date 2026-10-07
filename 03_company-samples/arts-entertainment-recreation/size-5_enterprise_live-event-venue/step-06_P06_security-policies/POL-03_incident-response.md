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
| Regulatory basis | PCI DSS v4.0.1 Requirement 12.10 (N71-R04); SEC Form 8-K Item 1.05; state breach notification laws |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, meets card brand, client, breach notification, and SEC disclosure deadlines, and keeps events and gate entry running safely during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, part-time and seasonal event staff, contractors, and interns) at headquarters, all 36 venues in 8 states, the 3 festivals, and the two contact centers, including acquired venues from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, venue operational technology, and systems that service providers and other vendors operate for the company, and the services the company offers to business clients (SL-1 white-label ticketing and SL-2 venue management).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Director of Payments and PCI Compliance | Acquirer, card brand, and client merchant notices |
| Chief Privacy Officer | Breach risk assessment and notification decisions |
| President, Venue Operations | Venue emergency plans and gate operations during outages |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with a ticketing platform breach exposing customer and card data (P08), and including card brand, client, and business recovery procedures. (IR-8; RS.MA-01)
4.2 Workforce, clients, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management, including incidents at acquired venues and festivals. (IR-5; IR-4; RS.MA-02)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2), including incidents where the company acts as a service provider to client venues. (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 On suspicion of a card data compromise, the Director of Payments and PCI Compliance must notify the acquirer within 24 hours (merchant agreement), make sure Visa is notified within 3 calendar days, and notify affected client merchants within 72 hours (client agreements). (IR-6; RS.CO-02)
4.7 Card numbers found where they are not expected must be handled as an incident under PRC-03.4: contained, removed or protected, and traced to their source. (IR-4; SI-12; RS.MA-01)
4.8 The Chief Privacy Officer must decide breach notifications under the P08 notification matrix, applying the law of each state where affected individuals reside and the company's third-party agent duties to client venues. (IR-6; RS.CO-03)
4.9 No ransom or extortion payment may be made without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and pass a recovery test at least annually, and every venue must pass an offline scanning drill before its season. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee, and after every major organizational change such as an acquisition. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach, Card Brand, and Client Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ticketing Platform Breach Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State and Client Notification Procedure
- PRC-03.4 Card Data Found in Unexpected Places Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's Reports on Compliance, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TVOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
