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
| Regulatory basis | PCI DSS 12.10; state breach notification laws; SEC Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, meets card brand, breach notification, and SEC disclosure deadlines, keeps hotels operating during outages, and coordinates with franchisees, owners, and clients when their guests or systems are affected.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at headquarters, the regional offices, the contact center, and the 110 company-operated hotels in 33 states and DC, including acquired hotels from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, payment devices, and hotel building and guest-room technology, and the systems and services the company provides to franchisees and distribution clients (SL-1 and SL-2). Franchisees are bound through the brand technology standards and the franchise agreement, not directly by this policy.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Director of Payments and PCI Compliance | Acquirer and card brand reporting; PCI Forensic Investigator engagement |
| Chief Privacy Officer | Breach risk assessment and notification decisions |
| Director of Franchise Technology Compliance | Franchisee coordination under PRC-03.4 |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with a POS and reservation system compromise (P08). (IR-8; RS.MA-01)
4.2 Workforce and vendors must report suspected incidents to the SOC within 1 hour. Franchisees must report incidents that may affect brand systems or guest data under BS-TECH-06. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 Suspected card data compromise must be reported to the acquirer and card brands within the contract and card brand deadlines in the P08 notification matrix, and a PCI Forensic Investigator engaged when a card brand requires one. (IR-6; RS.CO-02)
4.7 The Chief Privacy Officer must document a breach assessment for every incident involving personal information, and notices must meet the law of each state where affected individuals reside. Franchisees, owners, and SL-2 clients whose guests are affected must be told in time to meet their own duties. (IR-6; RS.CO-03)
4.8 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and one scenario that starts at a franchised hotel, and after every major change such as an acquisition. (IR-3; IR-8; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)
4.12 Card numbers found anywhere outside the vault must be handled as an incident under PRC-04.1: contained, purged, and the cause fixed. (IR-4; CM-12; RS.MA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Card Brand Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 POS and Reservation System Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Franchise Incident Coordination Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's PCI DSS assessments, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Franchisee violations of brand technology standards are handled under the franchise agreement.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; brand technology standards BS-TECH-01 to BS-TECH-06.
