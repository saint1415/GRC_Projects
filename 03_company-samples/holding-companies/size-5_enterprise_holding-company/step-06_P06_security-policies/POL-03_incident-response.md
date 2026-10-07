# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (holding company, GBS, and all subsidiaries) |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-14 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-03 |
| Regulatory drivers | Form 8-K Item 1.05 (N55-R02); Rule 13a-15(b); 16 CFR 314.4(h) and (j) for Finance; 45 CFR 164.314(b)(2)(iv) (N55-R06); state breach laws (Florida worked example: Fla. Stat. 501.171) |

## 1. Purpose
Make sure the group detects, contains, recovers from, and reports security incidents quickly and lawfully, wherever in the group they start; that the disclosure committee can make a timely materiality determination; and that notices to regulators, individuals, subsidiaries, and counterparties meet their deadlines.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the holding company, Global Business Services (GBS), and every subsidiary (Building Products, Home Services, Manufacturing, and Finance), at all sites in the six operating states, including acquired businesses from their closing date. Covers all systems and data, including cloud, data centers, SaaS, plant OT, systems that vendors operate for the group, and the services offered to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; briefs the General Counsel |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Subsidiary BISOs and plant leaders | Report incidents in their subsidiary or plant to the SOC |
| Finance Information Security Officer | Finance notification decisions, including the FTC notice |
| Chief Privacy Officer | Breach assessments for personal information and plan PHI |
| Treasurer | Payment fraud response and bank recalls |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 The group must maintain an incident response plan and runbooks for its most likely incident types (P08) that cover the holding company, every subsidiary, plant OT, and incidents that start at a vendor. (IR-8; RS.MA-01)
4.2 Workforce members must report suspected incidents immediately. Subsidiaries, plants, and contract owners who receive a vendor incident notice must tell the SOC within 1 hour. (IR-6; RS.MA-02)
4.3 Incidents must be triaged, classified under STD-03.1, and tracked to closure in case management, recording the entity affected. (IR-4; IR-5; RS.MA-02)
4.4 The CISO must brief the General Counsel within 24 hours of declaring any severity-1 incident or any incident that could be material, and the disclosure committee must convene within 48 hours of declaration. (IR-6; RS.CO-02)
4.5 The SOC must review open and recent incidents across all subsidiaries at least monthly to identify related occurrences that together may be one cybersecurity incident. (IR-5; RS.AN-03)
4.6 Regulatory, contractual, and law enforcement notices must meet the deadlines in the notification matrix. GBS must tell an affected subsidiary the same day it learns of a breach of a system it runs for that subsidiary, and the group health plan of any security incident involving plan information. (IR-6; RS.CO-02; RS.CO-03)
4.7 A ransom or extortion payment may be made only with approval of the CEO and the General Counsel, after notice to the insurer and a documented OFAC sanctions check. (IR-4; RS.MI-01)
4.8 The plan must be tested at least annually, including the disclosure committee, and tier-1 recovery must be tested annually. (IR-3; CP-4; ID.IM-02)
4.9 Systems must be recovered in the BIA priority order (P05) from known-good sources. (CP-10; RC.RP-01)
4.10 A lessons-learned review must be held within 14 days of recovery, with a written report within 30 days that updates the risk register and this plan. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Regulatory Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Shared-Services Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State and Regulatory Notification Procedure
- PRC-03.4 Payment Fraud Response and Bank Recall Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly sub-certifications, access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SCSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; Finance WISP annex (SUP-FIN); Manufacturing OT annex (SUP-MFG).
