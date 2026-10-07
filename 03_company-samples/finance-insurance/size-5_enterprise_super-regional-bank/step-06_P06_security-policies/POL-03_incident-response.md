# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (with Cris Santos Bank, N.A. and Cris Santos Investment Services, LLC) |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Cyber Defense |
| Approved by | Executive risk committee |
| Approval date | 2026-09-18 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g, III.C.1.h and Supplement A; 12 CFR 53.3; 12 CFR 225.302; 12 CFR 21.11; Form 8-K Item 1.05; 17 CFR 248.30(a)(3)-(4) |

## 1. Purpose
Make sure the group detects, responds to, and recovers from incidents quickly, meets every notification and disclosure deadline, and keeps critical banking services running within the recovery objectives in the BIA.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the parent, Cris Santos Bank, N.A., and Cris Santos Investment Services, LLC, at all sites in the six footprint states and remote locations, including the acquired bank's staff and systems from the merger date. Covers all systems and data, including the data centers, both clouds, SaaS, branches, ATMs, and systems that third parties operate for the group, and the services the group offers to institutional clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Cyber Defense | Incident commander; runs the 24x7 Cyber Defense Center |
| CISO | Executive incident lead; briefs the General Counsel |
| General Counsel | Chairs the disclosure committee |
| Chief Privacy Officer | Customer notice decisions |
| BSA/AML Officer | SAR decisions and law enforcement liaison |
| Chief Operating Officer | Chairs the crisis management team |
| Director of Enterprise Resilience | Contingency plans and tests |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The group must maintain an incident response plan and runbooks for its most likely severe incidents, starting with business email compromise and fraudulent wire transfers (P08) and destructive attacks. (IR-8; RS.MA-01)
4.2 Workforce, contractors, and third parties must report suspected incidents to the Cyber Defense Center within 15 minutes; suspected payment fraud must also go immediately to Payments Operations so a recall can start. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified under STD-03.1, linked to any fraud or BSA case, and tracked to closure. (IR-5; IR-4; RS.MA-02)
4.4 For every severity 1 or 2 incident, the incident commander and the CISO must decide whether it is a notification incident and record the decision with date and time. If it is, the OCC and, when the parent is affected, the Federal Reserve must receive notice within 36 hours of that determination. (IR-6; RS.CO-02)
4.5 The BSA/AML Officer must be told of any incident involving suspected fraud within 1 business day so a SAR can be filed within 30 calendar days of initial detection. (IR-6; RS.CO-02)
4.6 For a severity 1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours. Related incidents must be assessed together. If an incident is determined to be material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.7 The Chief Privacy Officer must document every customer notice decision under Supplement A, Regulation S-P (broker-dealer: no later than 30 days), and the law of each state where affected individuals reside, using the P08 notification matrix. (IR-6; RS.CO-03)
4.8 No ransom or extortion payment may be made without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; plans must cover the failure of critical third parties. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least twice a year, including once with the disclosure committee, and after a major organizational change such as an acquisition. (IR-3; IR-8; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard (includes notification incident criteria)
- STD-03.2 Customer and Regulator Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 BEC and Wire Fraud Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Notification Incident Determination Procedure (12 CFR 53.3 and 225.302)
- PRC-03.4 Destructive Attack Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, second-line reviews by independent risk management, the annual Internal Audit assessment (P07), and quarterly access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CBDC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
