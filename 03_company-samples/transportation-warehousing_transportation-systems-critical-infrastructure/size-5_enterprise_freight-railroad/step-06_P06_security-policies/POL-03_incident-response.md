# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), after every severity-1 incident, and after an SD renewal with substantive changes |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, PR.DS-11 |
| TSA / regulatory basis | SD 1580-21-01E Sec. II.C, II.D; SD 1580/82-2022-01E Sec. III.D.4; 49 CFR 1570.203; 49 CFR 1580.203(d); Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents in a way that keeps trains moving safely under operating rules, meets every reporting clock, and restores systems in the order the business needs them.

## 2. Scope
All 64 railroads, both NOCs, DC-1 and DC-2, cloud and SaaS services, field and onboard OT, vendors that support Critical Cyber Systems, and SL-1 and SL-2 customers affected by an incident.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; primary Cybersecurity Coordinator; escalates to the General Counsel and CEO |
| Vice President, Network Operations | Manual dispatch and operating restrictions; operations incident lead |
| Director of Train Control Systems | PTC restrictions and restoration; FRA reporting for PTC failures |
| Assistant Vice President, Rail Security | TSA Security Coordinator; 1570.203 reports; RSSM location answers |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain a Cybersecurity Incident Response Plan for Critical Cyber Systems and runbooks for its most likely severe incidents, starting with ransomware on dispatch and train control back-office systems (P08). The plan must name responsible positions and resources. (IR-8; RS.MA-01)
4.2 Employees, acquired railroads, and vendors must report suspected incidents to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 Reportable cybersecurity incidents must be reported to CISA with the explicit statement that the report is made under the SD, with a company target of 24 hours and never later than 72 hours after identification, and to TSA within 24 hours of discovery for any railroad not covered by that report (1570.203). (IR-6; RS.CO-02)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). If the incident is determined to be material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.6 The SOC must be able to isolate IT from OT through pre-approved steps, and the NOC must be able to keep trains moving under manual operating procedures while systems are isolated. (IR-4; SC-7; RS.MI-01)
4.7 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.8 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; manual operations for each signaled railroad must be exercised at least every two years. (CP-2; CP-4; CP-10; RC.RP-01)
4.9 Backups of Critical Cyber Systems must be kept offline or immutable and scanned for malicious artifacts when made and when restored. (CP-9; PR.DS-11)
4.10 The incident response plan must be exercised at least annually, testing at least two of the plan objectives with the named positions taking part, plus one exercise a year with the disclosure committee and after every acquisition. (IR-3; IR-8; ID.IM-02)
4.11 Personal information breaches must be assessed by the General Counsel's office, and notifications must meet the deadlines in the P08 notification matrix for each state where affected individuals reside. (IR-6; RS.CO-03)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
- STD-03.1 Incident Classification, Escalation, and Regulatory Reporting Standard
- STD-03.2 Breach Notification and SSI Release Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware Runbook for Dispatch and Train Control Back-Office Systems (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 RSSM Location Request Fallback Procedure (draft; test due 2026-11-30, POAM-019)
- PRC-03.5 Manual Dispatch and CTC Local Control Procedure

## 6. Compliance and enforcement
Compliance is monitored through exercise results, DR test reports, report timeliness metrics, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1 (POL-01 statement 4.7).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. No exception may extend a regulatory reporting deadline.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P05 BIA; P08 runbook and notification matrix; TDPB contingency plan v6; applicable regulations listed in P03.
