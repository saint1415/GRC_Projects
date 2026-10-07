# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-08-24 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AT-1, CP-1, IR-1, IR-6, IR-4, IR-8, IR-5, CP-2, CP-4, CP-10, CP-9, AT-3, IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, ID.IM-01, ID.IM-02, DE.AE-03, RC.RP-03, PR.DS-01, PR.DS-10, PR.AT-01 |
| HIPAA Security Rule and other drivers | 164.308(a)(6); 164.308(a)(6)(ii); 164.308(a)(7)(ii)(A); 164.308(a)(7)(ii)(B); 164.308(a)(7)(ii)(C); 164.308(a)(7)(ii)(D); 164.404(a)(2); see `policy-control-map.csv` for each statement's driver |

## 1. Purpose
Make sure the system detects, responds to, and recovers from security incidents and IT outages in a way that keeps patients safe, keeps emergency departments operating within EMTALA, meets breach and disclosure deadlines, and restores services in the order the business needs.

## 2. Scope
All Cris Santos Company workforce members (employees, medical staff, agency and contracted staff, students, and volunteers) at the 8 hospitals, 3 freestanding emergency departments, 46 clinics, 4 imaging centers, the data centers, and corporate offices in Florida, Georgia, and Alabama, including H-08 and any future acquisition from its closing date. Covers all systems and data, including the data centers, both clouds, SaaS, medical devices, building OT, systems that vendors operate for the system, and the services sold to other organizations (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; owns the runbooks |
| Chief Operating Officer | Chairs system incident command during major outages |
| Hospital presidents | Hospital incident commanders; decide ambulance diversion with the ED medical director and house supervisor |
| Vice President, Emergency Management | Links incident response to the unified emergency plan; System Transfer and Command Center |
| Chief Privacy Officer | Breach risk assessments and notices |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| EHR Technical Director | ECIS recovery |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every workforce member must report a suspected security incident, privacy incident, or lost device to the service desk or SOC immediately, at any hour. (IR-6; RS.MA-01; RS.MA-02)
4.2 The SOC must classify every incident under STD-03.1; a severity-1 declaration must activate system incident command, the affected hospitals' incident command, and clinical downtime procedures. (IR-4; IR-8; ID.IM-01; ID.IM-02)
4.3 The time of discovery must be recorded for every incident that may involve PHI, using the first day the incident was known, or by reasonable diligence would have been known, to any workforce member. (IR-5; IR-6; DE.AE-03; RS.MA-02; RS.MA-01)
4.4 The CISO must brief the General Counsel within 24 hours of any severity-1 declaration, and the disclosure committee must convene within 48 hours to assess materiality and record its determination with the date and time. (IR-6; IR-8; RS.MA-01; RS.MA-02; ID.IM-01)
4.5 The Privacy Officer must complete and document the four-factor breach risk assessment, check for Part 2 records, and send notices under STD-03.2 and the law of each state where affected individuals reside. (IR-6; RS.MA-01; RS.MA-02)
4.6 Ambulance diversion because of an IT outage may be declared only by the hospital president (or delegate) with the ED medical director and house supervisor, using the IT-outage diversion criteria in STD-03.4, and must be coordinated through the System Transfer and Command Center with county EMS. Diversion never stops the screening and stabilization of anyone who comes to the emergency department. (CP-2; IR-4; ID.IM-01; ID.IM-02)
4.7 No ransom may be paid without approval by the CEO, the General Counsel, and the insurer, and an OFAC sanctions check, with a report to the FBI or CISA. (IR-4; ID.IM-01; ID.IM-02)
4.8 Tier-1 systems must have contingency plans that meet the BIA recovery objectives; the ECIS must be recoverable from the immutable vault within 24 hours in a cyber event, demonstrated by an annual test. (CP-2; CP-4; CP-10; ID.IM-01; ID.IM-02; RC.RP-03)
4.9 Backups of tier-1 systems must be kept in an immutable vault in a separate account, restore-tested monthly by sample and fully once a year. (CP-9; PR.DS-01; PR.DS-10)
4.10 BCA downtime computers must be checked monthly at every hospital, and charge nurses, ED staff, and unit clerks must complete downtime training annually. (CP-2; AT-3; ID.IM-01; ID.IM-02; PR.AT-01)
4.11 An enterprise exercise must be held each year that includes EHR downtime at two or more hospitals, diversion decisions, and the disclosure committee; it may serve as the additional annual exercise under 42 CFR 482.15(d)(2)(ii). (IR-3; CP-4; ID.IM-02; RC.RP-03)
4.12 A lessons-learned review must be held within 14 days of recovery from a severity-1 incident or an IT outage over 2 hours, with a written report within 30 days filed with the emergency program records. (IR-4; ID.IM-01; ID.IM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- STD-03.4 Downtime and IT-Outage Diversion Standard
- PRC-03.1 Ransomware and Diversion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Hospital IT-Outage Diversion Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the emergency preparedness program's exercises. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, contract, or privileges, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ECIS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the unified emergency preparedness plan.
