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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new contract types |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Contract and legal basis | State exhibits (IR and CP families); customer notice terms; GSA BTTRG v3.0 sections 1.6.1 and 1.6.2; SEC Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, keeps people in customer buildings safe while it does so, meets customer, breach, and SEC deadlines, and keeps alarm monitoring and access administration running during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor personnel working under company accounts) in all segments and acquired businesses from their acquisition date, in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, and the District of Columbia. Covers all company systems and data (cloud, colocation, SaaS, ROCs, endpoints, and the OT edge), the company's administration of customer building systems through the IBOP, customer data the company holds, and systems that vendors and subcontractors operate for the company. GSA systems that company staff use under GSA's authorization are governed by GSA policy; this policy governs the company staff who use them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Director of OT Security | OT technical lead; building-safe containment |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| Chief Operating Officer | Chairs the crisis management team |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach determinations and notification decisions |
| Segment presidents and Site Managers | Customer notices and coordination with customer security staff |
| Vice President, Remote Operations | ROC continuity and manual-mode coordination |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its contract or regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with intrusion into building access control and automation systems (P08) and ransomware. (IR-8; RS.MA-01)
4.2 Workforce, acquired businesses, subcontractors, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident, including incidents at acquired businesses, must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-4; IR-5; RS.MA-02)
4.4 When an incident may affect doors, life-safety supervision, or building conditions, the customer's security staff must be told and a safe building state established before evidence collection or restoration begins. (IR-4; RS.MI-01)
4.5 Customer notices must meet each contract's clock (immediately for GSA, within 1 hour for public safety customers, within 24 hours for state and local customers) using the STD-03.2 matrix, with a named owner in each segment. (IR-6; RS.CO-02)
4.6 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours and the disclosure committee must convene within 48 hours. If the committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.7 No ransom may be paid on a customer's behalf. Any payment for the company's own systems requires approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.8 The Chief Privacy Officer must document a breach determination for every incident involving personal information, and notices must meet the deadlines in the P08 matrix, including each state where affected individuals reside. (IR-6; RS.CO-03)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and pass a recovery test at least annually; every IBOP building and every federal building must have exercised manual-mode procedures. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and one with a customer, and after every acquisition. (IR-3; IR-8; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Customer and Regulatory Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 OT Intrusion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Building Manual-Mode Procedures
- PRC-03.5 Ransomware Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and customer audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor violations are handled under the subcontract and may end the subcontractor's access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception never waives a customer contract term or a law.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 IBOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the contract obligations register.
