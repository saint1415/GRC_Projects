# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc., adopted by Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-6, AT-2, IR-4, IR-8, IR-5, CP-2, CP-4, CP-9, CP-9(3), IR-3, CA-5 |
| CSF 2.0 | DE.AE-02, RS.MA-02, RS.AN-03, RS.CO-02, RS.MA-01, RC.RP-01, PR.DS-11, ID.IM-04, ID.IM-03 |
| Regulatory drivers | See `policy-control-map.csv` (N53-R01 Safeguards Rule citations for each statement) |

## 1. Purpose
Make sure incidents, including attempts to divert client funds, are detected, contained, investigated, reported, and learned from, that regulatory notices and SEC disclosures are made on time, and that critical processes recover within the times set in the BIA (P05). For Title and Escrow this policy and its procedures are the written incident response plan required by 16 CFR 314.4(h).

## 2. Scope
All Cris Santos Company, Inc. employees, the about 38,000 contractor sales associates who use company systems, contractors, and temporary staff, in all 9 states, and the employees of Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC, which adopted this hierarchy by resolution. Acquired firms are covered from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, contractor agents' own devices when they access company systems, and systems that vendors operate for the company, and the services offered to business clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Owns this policy; runs the SOC and incident command |
| Funds response desk (Title and Escrow) | Bank recall requests and consumer support during funds incidents |
| General Counsel | Legal privilege; chairs the disclosure committee |
| Chief Privacy Officer | Breach determinations and notifications |
| Disclosure committee | Form 8-K Item 1.05 materiality decisions |
| System owners | Contingency plans and recovery |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every employee and contractor agent must report a suspected incident, including any changed wire instructions or suspicious payoff letter, to the SOC or the funds response desk immediately, and the case system must record the date of first report as the discovery date. (IR-6; AT-2; DE.AE-02)
4.2 Incidents must be classified and escalated under STD-03.1; any suspected diversion of funds is severity 1 and starts the bank recall procedure (PRC-03.4) within 30 minutes. (IR-4; IR-8; RS.MA-02)
4.3 Every incident must be handled in the SOC case system, including incidents at acquired firms, and closed only with a root cause and lessons learned. (IR-4; IR-5; RS.AN-03)
4.4 The CISO must brief the General Counsel within 24 hours of a severity-1 incident, and the disclosure committee must assess materiality without unreasonable delay under PRC-03.2, including whether related incidents form a series. (IR-6; IR-8; RS.CO-02)
4.5 Notifications to the FTC, state regulators, individuals, and business clients must follow STD-03.2 and the P08 notification matrix, and the FTC must be notified no later than 30 days after discovery of a notification event involving 500 or more consumers. (IR-6; RS.CO-02)
4.6 No ransom or extortion payment may be made without CEO approval, legal review, and an OFAC sanctions check. (IR-4; RS.MA-01)
4.7 Tier-1 systems must have contingency plans that meet the BIA RTO and RPO, tested at least annually, with results fed back into the plan. (CP-2; CP-4; RC.RP-01)
4.8 Backups of tier-1 data must be immutable, kept in a separate account, copied weekly to an offline location, and restore-tested at least quarterly. (CP-9; CP-9(3); PR.DS-11)
4.9 The incident response plan must be exercised at least annually, including a funds-diversion scenario with the disclosure committee. (IR-3; ID.IM-04)
4.10 Weaknesses found in incidents must be entered in the POA&M with an owner and date. (CA-5; IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Regulatory Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 BEC and Funds Diversion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Funds Recall Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of the agent agreement, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TMCC SSP; P03 gap analysis; P08 BEC runbook and notification matrix; P10 AI governance.
