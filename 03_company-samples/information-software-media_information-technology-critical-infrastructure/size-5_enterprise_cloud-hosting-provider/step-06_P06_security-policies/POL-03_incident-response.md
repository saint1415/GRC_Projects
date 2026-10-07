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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-4, IR-6, IR-8, CP-2, CP-4, CP-9, CP-10, AU-6, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, DE.AE-02 |
| Regulatory drivers | FedRAMP IEC rules (C-IT-R01); bank service provider rule (C-IT-R05); DFARS 252.204-7012(c)-(g) (C-IT-R03); SEC Form 8-K Item 1.05; HIPAA 164.410; state breach laws (Fla. Stat. 501.171(6) worked example) |

## 1. Purpose
Detect, contain, and recover from incidents quickly, notify customers, agencies, regulators, and investors on time, and keep the services customers depend on available within their recovery objectives.

## 2. Scope
All incidents and disruptions affecting company systems, customer workloads the company operates or can reach (including through fleet automation and the legacy RMM tool), suppliers that process company or customer data, and all service lines.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Policy owner; incident commander for security incidents |
| Director of FedRAMP Compliance | FedRAMP reportability and agency reports |
| General Counsel | Chairs the disclosure committee; privilege; law enforcement |
| Chief Privacy Officer | Breach determinations for personal information and PHI |
| Senior Vice President, Customer Support | Customer and bank notices; status page |
| System owners | Contingency plans and recovery tests |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan, reviewed annually and after each major incident, with runbooks for the highest risks in P01, including provider tooling compromise (PRC-03.1). (IR-8; RS.MA-01)
4.2 The SOC must monitor all production, G1, and provider tooling 24x7. Automated response that isolates hosts or suspends customer accounts must have human approval in G1 and for bank customers, and every automated action must be reviewable (P10). (SI-4; AU-6; IR-4; DE.AE-02)
4.3 Every incident must be classified within 30 minutes using STD-03.1, including whether it is a FedRAMP Reportable Incident and its PAIN rating. (IR-4; IR-5; RS.MA-02)
4.4 FedRAMP Reportable Incidents must be reported to all affected parties within the IEC timeframes for each offering's class (Class C: 1 hour; Class D: 15 minutes, for PAIN 3 to 5), with ongoing and final reports as the rules require. (IR-6; RS.CO-02)
4.5 Each affected bank must be notified as soon as possible after the company determines that an incident has materially disrupted or degraded, or is reasonably likely to, covered services for four or more hours. (IR-6; RS.CO-03)
4.6 Customers must be notified of security incidents affecting their data without undue delay and within 72 hours of confirmation, and DIB, health care, and state agency customers within the shorter or specific timeframes in their agreements and applicable law (STD-03.2). (IR-6; RS.CO-03)
4.7 Every severity-1 incident must be escalated to the General Counsel within 12 hours for a materiality assessment under PRC-03.2, and the disclosure committee must document its determination. (IR-6; IR-8; GV.OV-01)
4.8 Evidence, including host images and monitoring data, must be preserved under chain of custody; for DIB customers, for at least 90 days from the incident report. (IR-4; AU-11; RS.AN-03)
4.9 Every tier-1 process in the BIA (P05) must have a contingency plan meeting its RTO and RPO, tested at least annually; failed tests must be retested within 6 months. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 Control plane state, keys, and configuration must be backed up to immutable storage across regions and to an out-of-band vault outside the company cloud, and restores must be tested at least annually. (CP-9; CP-6; PR.DS-11)
4.11 Incident responders must be trained at least annually, using simulated technical events for G1 responders. (IR-2; PR.AT-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Provider Tooling Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Customer, Bank, and Multi-State Notification Procedure
- PRC-03.4 FedRAMP Incident Reporting Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the FedRAMP independent assessment, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.6), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5 (PRC-01.2).

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HCP-G SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
