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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(b)(2)-(4)); 40 CFR 141.202; 40 CFR 302.6 and 355.40; Form 8-K Item 1.05; state breach laws (Fla. Stat. 501.171 worked example) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully; keeps safe water flowing during an OT incident by moving to manual operation; and meets public notification, release reporting, breach notification, and SEC disclosure deadlines.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in all four regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee and in the two service lines, including acquired systems from their acquisition date. Covers all IT and OT systems and data: SCADA, PLCs, RTUs, telemetry, and HMIs at the 126 community water systems and 5 ROCCs; cloud, colocation, and SaaS; and systems that vendors and integrators operate or support for the company, including the services offered to municipal clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the 24x7 SOC |
| ROCC shift supervisor and plant operators | Move processes to manual control and isolate OT when control is in doubt |
| OT incident lead (Director of OT Security) | Leads OT containment and recovery with the system owner |
| Regional water quality manager and state utility president | Tier 1 public notice decision and primacy agency consultation |
| Director of Environmental Health and Safety | Release reporting to the National Response Center, LEPCs, and SERCs |
| CISO | Executive incident lead; briefs the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee |
| Chief Privacy Officer | Breach determinations and notices for customer personal information |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether the 2026 independent assessment tested it (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with remote-access compromise of a treatment-plant HMI (P08) and enterprise ransomware, and must include the OT playbook in each covered system's ERP. (IR-8; RS.MA-01)
4.2 Workforce, vendors, and integrators must report suspected incidents to the SOC within 1 hour. Operators must report any unexplained HMI action, setpoint change, or mode change to the ROCC shift supervisor immediately. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 When unauthorized control of treatment, chemical feed, or pumping is suspected, the shift supervisor must move the affected processes to manual (local) control and may isolate the OT network at the OT DMZ without waiting for further approval. (IR-4; CP-2; RS.MI-01)
4.4 The regional water quality manager must decide, within 2 hours of a suspected loss of treatment control or unsafe water, whether a Tier 1 notice is required; if it is, the notice must go out and primacy agency consultation must begin no later than 24 hours after the system learns of the situation. (IR-6; RS.CO-02)
4.5 Any release of a hazardous substance at or above its reportable quantity must be reported immediately to the National Response Center and to the LEPC and SERC, whatever the cause, including a cyber incident. (IR-6; RS.CO-02)
4.6 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee, including the Chief Operating Officer, must convene within 48 hours to begin the materiality assessment (PRC-03.2), using quantitative and public health factors. (IR-6; IR-8; RS.CO-02)
4.7 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.8 The Chief Privacy Officer must determine whether customer personal information was breached and must meet the notice deadlines of each state where affected individuals reside (Florida: individuals and, for 500 or more Florida residents, the Department of Legal Affairs, no later than 30 days after determination). (IR-6; RS.CO-03)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and a sanctions check against OFAC lists. (IR-4; RS.MI-01)
4.10 Tier-1 systems, including every ROCC SCADA system, must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; every plant must hold manual-operation drills at least twice a year. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually at each ROCC, including one exercise a year with the disclosure committee that uses an OT and public health scenario. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register, the POA&M, and the affected systems' RRAs and ERPs. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Notification Standard (public notice, release reporting, breach, SEC)
- STD-03.3 Contingency, Manual Operation, and Recovery Standard
- PRC-03.1 HMI Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Tier 1 Public Notice Procedure (cyber trigger)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, the annual independent assessment by Internal Audit and the co-sourced OT assessment firm (P07), and plant drills. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GCR-WTSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; each covered system's RRA and ERP.
