# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director, Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and within 90 days after a Reportable Cyber Security Incident or an exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-6, IR-8, CP-1, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| NERC and other | Supports CIP-008-6, CIP-009-6, CIP-003-9 Attachment 1 Section 4, EOP-004-4; Form DOE-417; SEC Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure cyber incidents in IT and OT are detected, contained, reported, and recovered from quickly and safely; that every legal and regulatory clock is met; and that the company can keep the grid running while it responds.

## 2. Scope
All IT and OT systems, including the EMS, ADMS, OMS, substations, CIS, cloud, SaaS, and the service line platforms; all workforce members and vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director, Security Operations | Enterprise incident commander for cyber incidents; owns this policy and the runbooks |
| Director, Distribution Control Center; Director, Transmission Operations | Operational incident commanders for grid impact; decide on manual operation |
| CIP Senior Manager's delegate on duty | Determines whether an incident is a Reportable Cyber Security Incident or an attempt to compromise |
| Director, NERC Compliance | DOE-417, EOP-004, and CIP-008 filings |
| General Counsel | Legal privilege; chairs the disclosure committee |
| Chief Privacy Officer | Breach determinations under state laws |
| Director, Emergency Management | Crisis management team and storm plan coordination |

## 4. Policy statements
4.1 The company must maintain an incident response plan covering IT and OT, with an OT annex, the CIP-008-6 plan content, and the SEC materiality step, and test it at least once every 15 calendar months through an exercise or an actual Reportable incident. (IR-8; IR-3; RS.MA-01)
4.2 Any workforce member or vendor who sees a suspected cyber or physical security incident must report it immediately to the SOC or the control center. (IR-6; RS.MA-02)
4.3 Incidents involving the EMS, its EACMS, or medium impact substations must be evaluated against the documented criteria for a Reportable Cyber Security Incident and an attempt to compromise; the determination must be recorded with the time it was made. (IR-4; IR-6; RS.MA-02)
4.4 Notifications must meet the clocks in the P08 notification matrix: E-ISAC and CISA within 1 hour of a Reportable determination and by the end of the next calendar day for an attempt to compromise; DOE-417 within 1 hour, 6 hours, or by the end of the next calendar day (attempted compromise) or the later of 24 hours and the end of the next business day (System Report) by criterion; EOP-004 by the later of 24 hours or the end of the next business day; state breach laws as each state requires. (IR-6; RS.CO-02)
4.5 The CISO must brief the General Counsel on every severity-1 incident within 24 hours of declaration so the disclosure committee can assess materiality without unreasonable delay; the committee must record the time and basis of its determination. (IR-6; IR-8; RS.CO-02)
4.6 The materiality worksheet must use the BIA outage costs and safety factors, and the materiality step must be exercised with an OT scenario at least once a year. (IR-3; IR-8; RS.MA-03)
4.7 Grid safety comes first: control center operators may move to manual operation, isolate OT networks, or disable remote access without waiting for approval when they judge it necessary to keep the system safe. (IR-4; RS.MI-01)
4.8 Evidence must be preserved before rebuilding or restoring systems, per Cyber Asset capability, without delaying grid recovery. (IR-4; AU-9; RS.AN-03)
4.9 No ransom may be paid without approval by the CEO and the General Counsel, notice to the insurer, and an OFAC sanctions check; payment never removes notification or disclosure duties. (IR-4; RS.MA-01)
4.10 Recovery plans must exist for every tier-1 system and every high and medium impact BES Cyber System; recovery must follow the BIA priority order; plans must be tested at least once every 15 calendar months, with an operational exercise for high impact systems at least once every 36 calendar months. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 Backups of OT systems must include an offline copy at a separate site, and restores must be verified on a sample at least once every 15 calendar months. (CP-9; CP-9(1); PR.DS-11)
4.12 Lessons learned must be documented within 90 days after an exercise or a Reportable incident, and plans updated and roles notified within the same period. (IR-4; ID.IM-04)

## 5. Standards and procedures under this policy
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Notification and Disclosure Standard (NERC, DOE, SEC, state)
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 OT Intrusion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 DOE-417 and EOP-004 Filing Procedure

## 6. Compliance and enforcement
Compliance is monitored through case records, exercise reports, filing records, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7. Reporting deadlines and CIP-008 and CIP-009 requirements cannot be excepted.

## 8. Related documents
POL-01; P05 BIA; P08 runbook and notification matrix; CIP-008 incident response plan v9; CIP-009 recovery plans v6; storm and emergency plan.
