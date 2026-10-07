# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations (with the Director of OT Security for OT incidents) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-8, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | MTSA 33 CFR 101.620(b)(6)-(7), 101.635, 101.650(g); 33 CFR 6.16-1; RMP 40 CFR 68.81, 68.90-68.96; CERCLA 40 CFR 302.6; EPCRA 40 CFR 355.40-355.43; SEC Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company puts people and the process in a safe state first, then detects, contains, recovers from, and reports security incidents quickly and lawfully, meets release reporting, MTSA, and SEC deadlines, and keeps critical supply (including water utility customers) going.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, integrators, and temporary staff) at all 14 plants, 9 distribution centers, 2 R&D centers, and offices, including acquired plants from their acquisition date. Covers all information technology (IT) and operational technology (OT): process control systems, safety instrumented systems, PLCs, terminal and loading rack automation, cloud, colocation, SaaS, and systems that vendors and integrators operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Plant manager (incident commander for process safety) | Decides safe state and shutdown; owns release reporting at the plant |
| Director of Security Operations | Incident commander for the cyber response; runs the SOC |
| Director of OT Security and plant CySO | OT containment and recovery; MTSA cyber reporting at PLT-01 |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Vice President, Process Safety and EHS | RMP and PSM incident investigation; release reporting standards |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with an intrusion into process control systems (P08), and a Cyber Incident Response Plan for each MTSA facility. (IR-8; RS.MA-01)
4.2 If the integrity of a control or safety system is in doubt, operators must take the affected unit to a safe state under the unit's untrusted-DCS procedure before any forensic or recovery work. Safety always takes priority over evidence. (IR-4; CP-2; SC-24; RS.MA-01)
4.3 Workforce, integrators, and vendors must report suspected incidents to the SOC and, at an MTSA facility, to the CySO within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.4 Releases at or above a reportable quantity must be reported immediately to the National Response Center, the SERC, and the LEPC, whatever the cause, using a notification path that does not depend on the business network. (IR-6; CP-8; RS.CO-02)
4.5 Evidence of an actual or threatened cyber incident at an MTSA facility must be reported immediately to the FBI, CISA, and the Captain of the Port. (IR-6; RS.CO-02)
4.6 For a severity-1 incident, including any OT incident that forces a plant to a safe state, the CISO must brief the General Counsel within 24 hours, and the disclosure committee, including the Senior Vice President, Manufacturing, must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.7 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.8 Any incident in which a control or safety system was manipulated at an RMP or PSM process must also be investigated as a process safety incident, starting within 48 hours. (IR-4; RS.AN-03)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Critical OT systems and tier-1 IT systems must have contingency plans with RTO and RPO from the BIA (P05). Each OT area must pass a restore test from the offline vault at least annually; safety logic must be restored only from the copy approved through MOC. (CP-2; CP-4; CP-9; CP-10; RC.RP-01)
4.11 Each MTSA facility must hold cybersecurity drills at least twice each calendar year and an exercise at least once each calendar year. The enterprise must exercise an OT incident with the disclosure committee at least annually. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register, the POA&M, and, for process safety incidents, the PHA and MOC systems. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard (IT and OT severity)
- STD-03.2 Notification Standard (regulatory, release, breach, and disclosure)
- STD-03.3 OT Recovery Standard
- PRC-03.1 OT Intrusion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Release Reporting Checklist

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT metrics), the annual Internal Audit assessment (P07), access certifications, and MTSA Cybersecurity Plan audits at PLT-01. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GC-PCBMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
