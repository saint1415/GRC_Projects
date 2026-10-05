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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions. CIP-003-9 R1 content is also approved by the CIP Senior Manager at least once every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-7, CP-9 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | CIP-008-6; CIP-009-6; CIP-003-9 Attachment 1 Section 4; 18 CFR 12.10; FERC Security Program 4.2, 7.4; EOP-004-4; SEC Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company keeps its dams under control, detects and contains security incidents, recovers in the right order, and meets its safety, NERC, FERC, SEC, and breach notification duties on time.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and interns) at the headquarters, 14 offices, two Hydro Operations Centers, the Contract Operations Center, and all 46 developments in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, including the Piedmont developments from their acquisition date. Covers all systems and data: IT, OT (fleet SCADA, plant control, spillway and gate control, dam safety instrumentation and warning), cloud, colocation, SaaS, and systems that vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Director, Hydro Operations Center; HOC shift supervisors | Incident commander for operations; local control decisions |
| Vice President, Dam Safety | 18 CFR 12.10 reports; EAP activation decisions with the plants |
| Director, NERC Compliance | CIP-008 and EOP-004 notifications |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Vice President, Corporate Security | FERC security reports; law enforcement liaison |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan covering IT and OT, including the CIP-008-6 plan for medium impact systems and the CIP-003-9 Section 4 plan for low impact assets, and runbooks for its most consequential incidents, starting with unauthorized access to spillway and turbine controls (P08). (IR-8; RS.MA-01; RS.MA-05)
4.2 When OT compromise is suspected, operators must put affected gates and units under local control and confirm physical positions before any other response step. Operators may do this without waiting for approval. (IR-4; CP-2; RS.MA-02; RS.MA-03; RC.RP-03)
4.3 Workforce, contractors, vendors, and service line staff must report suspected incidents and suspicious activity to the SOC or security dispatch within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-01; RS.MA-02)
4.4 Every incident must be classified under STD-03.1. Determinations of Reportable Cyber Security Incidents must be recorded with the time, and E-ISAC and CISA notified within 1 hour of a determination for medium impact systems; the Chief Dam Safety Engineer's staff decide on the 18 CFR 12.10 report for any security incident at a project. (IR-6; IR-5; RS.MA-01; RS.MA-02; RS.MA-03)
4.5 For a severity-1 incident the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.MA-01; RS.MA-02; RS.MA-05)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of the determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.MA-01; RS.MA-02)
4.7 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MA-02; RS.MA-03)
4.8 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05). CIP-009-6 recovery plans must be tested at least once every 15 calendar months, and HOC failover must be exercised annually. (CP-2; CP-4; CP-7; RC.RP-03; PR.IR-02; ID.IM-02)
4.9 The incident response plan must be exercised at least once every 15 calendar months, including one exercise a year with the disclosure committee and one with law enforcement and county emergency management. (IR-3; ID.IM-02)
4.10 Lessons learned must be documented and the plan updated within 90 days of a test or Reportable Cyber Security Incident, and fed into the risk register and POA&M. (IR-4; IR-8; RS.MA-02; RS.MA-03; RS.MA-01)
4.11 SCADA backups must run nightly with weekly offline copies; PLC, governor, and gate logic copies must be taken at least quarterly and after every change, stored offline with hashes, and restore-tested. (CP-9; RC.RP-03; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Recovery Standard (CIP-009-6; Rapid Recovery)
- PRC-03.1 OT Intrusion Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Regulatory Reporting Procedure (CIP-008, CIP-003 Section 4, 18 CFR 12.10, FERC, EOP-004, DOE-417)
- PRC-03.4 Local Control Fallback Procedure (by river system)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access verifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot excuse a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HFCDMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
