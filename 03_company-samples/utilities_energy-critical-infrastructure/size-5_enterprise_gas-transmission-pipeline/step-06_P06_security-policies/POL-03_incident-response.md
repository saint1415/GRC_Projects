# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations, with the Director of OT Security for OT and TSA reporting |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 (version 2026.1) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), after every severity-1 incident, and when a TSA security directive is renewed with changes |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10, SC-7 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MI-01, RS.AN-03, RS.CO-02, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory drivers | SD Pipeline-2021-01G Section II.C (C-ENERGY-R02); SD Pipeline-2021-02G Section III.F (C-ENERGY-R03); 49 CFR 192.615 and 192.631 (C-ENERGY-R04); 49 CFR Part 191; SEC Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company keeps its pipelines safe during any cyber incident, detects and contains incidents quickly, isolates OT from IT when needed, decides on a precautionary shutdown deliberately and per pipeline system, and meets its TSA, PHMSA, SEC, and state reporting deadlines.

## 2. Scope
All workers, suppliers, and authorized representatives; all IT and OT systems in POL-01 section 2, including PS-3 and the JV pipelines the company operates.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for cyber incidents; runs the SOC and OT monitoring cell |
| Director of OT Security | Primary TSA Cybersecurity Coordinator; reports to CISA; leads OT containment |
| CISO | Executive incident lead; briefs the General Counsel and the CEO |
| Vice President, Gas Control | Authority to isolate IT from OT; recommends operate, manual operation, or shutdown per pipeline system |
| Chief Operating Officer | Approves any precautionary shutdown of a whole pipeline system |
| Vice President, Pipeline Safety and Compliance | PHMSA incident notices under 49 CFR Part 191 |
| General Counsel | Chairs the disclosure committee; engages outside counsel; breach notice decisions |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain a Cybersecurity Incident Response Plan for its Critical Cyber Systems and runbooks for its most likely severe incidents, starting with ransomware on business IT that could force a precautionary shutdown (P08). The plan must be integrated with the emergency plans (49 CFR 192.615) and the control room management procedures (49 CFR 192.631). (IR-8; CP-2; RS.MA-01)
4.2 Anyone who suspects an incident must report it to the SOC within 1 hour. Anything that affects SCADA, station controls, field devices, or what a controller sees must be reported to the controller on duty at once. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure. Severity 1 applies whenever OT is affected or suspected. (IR-5; IR-4; RS.MA-02)
4.4 **Safety first.** Controllers and field personnel must follow the control room management and emergency procedures for any abnormal or emergency condition, whatever the cause, and must never wait for IT to take a safety action. (IR-4; RS.MA-01)
4.5 **Isolation authority.** The Vice President, Gas Control, or the shift supervisor at the affected control room, may close the IT/OT DMZ connections at any time when an IT incident could spread to OT. Isolation must not wait for proof of compromise. The isolation capability must be exercised at every control room at least once a year. (IR-4; SC-7; RS.MI-01)
4.6 **Shutdown decision.** A precautionary shutdown or curtailment of a pipeline system for cyber reasons must follow the decision criteria in the P08 runbook, be decided per pipeline system and segment, and be approved by the Chief Operating Officer, except where a controller or field supervisor must act at once for safety under the emergency plan. (IR-4; CP-2; RS.MI-01)
4.7 Cybersecurity incidents must be reported to CISA by the Cybersecurity Coordinator as soon as practicable and no later than 72 hours after identification (SD 01G Section II.C), with supplements within 24 hours of new information. Pipeline incident notices under 49 CFR Part 191 are decided by the Vice President, Pipeline Safety and Compliance. All other notices follow the P08 notification matrix. (IR-6; RS.CO-02)
4.8 For every severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment under PRC-03.2, including curtailment and shutdown factors. If the incident is determined to be material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, an OFAC sanctions check, and a report to the FBI or CISA. (IR-4; RS.MI-01)
4.10 Tier-1 systems must have contingency plans with recovery objectives from the BIA (P05) and must be recovery-tested at least annually. Backup SCADA systems must be tested at least once each calendar year at intervals not exceeding 15 months. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The Cybersecurity Incident Response Plan must be exercised at least annually, testing at least two of its objectives (containment, segregation, backup integrity, IT/OT isolation) with the positions named in the plan taking part. At least one exercise a year must include the disclosure committee. (IR-3; ID.IM-02)
4.12 Responders must preserve volatile memory before powering off or reimaging an affected device, and must label and secure affected equipment. (IR-4; RS.AN-03)
4.13 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register, the POA&M, and, where control room actions were involved, controller training (49 CFR 192.631(g)). (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
- STD-03.1 Incident Classification, Escalation, and Reporting Standard (CISA reporting criteria and content)
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware and Precautionary Shutdown Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 IT/OT Isolation Procedure (one annex per control room)
- PRC-03.4 Multi-State Breach Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through SOC case metrics, the CISA reporting clock in the case system, exercise reports, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1 (POL-01 statement 4.16).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. No exception may remove a controller's authority to act for safety (statement 4.4) or the CISA reporting deadline (statement 4.7).

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; Cybersecurity Incident Response Plan v5; emergency plans; control room management procedures; P05 BIA; P08 runbook and notification matrix.
