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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-8, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.MI-01, RC.RP-01, ID.IM-02, PR.IR-03 |
| Regulatory and guidance drivers | CSF 2.0 (benchmark); SP 800-82 Rev. 3 6.4 and 6.5; SEC Form 8-K Item 1.05; state breach laws (Fla. Stat. 501.171 worked example) |

## 1. Purpose
Detect, contain, and recover from incidents quickly, keep workers and crops safe while systems are down, meet notification and disclosure deadlines, and keep irrigation, freeze protection, harvest, packing, and shipping running through the recovery order in the BIA (P05).

## 2. Scope
All Cris Santos Company workforce members (year-round employees, seasonal and H-2A workers, contractors, and integrator and vendor staff working on company systems) at the 48 farms, 17 packing sites, 6 irrigation control centers, offices, and both data center campuses in Florida, Georgia, South Carolina, and North Carolina, including acquired operations from their acquisition date. Covers all systems and data, including cloud, data centers, SaaS, operational technology (irrigation, fertigation and chemigation, packing, cold-chain, and drying controls), drones and equipment telematics, systems that vendors operate for the company, and the services offered to external growers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Runs the SOC and the incident response plan |
| Director of OT Security | Leads OT incidents with the Irrigation Control Center Managers |
| Irrigation Control Center Managers and Regional Farm Directors | Order OT safe states and start manual irrigation and freeze procedures |
| General Counsel | Chairs the disclosure committee; leads legal and notification decisions with the Chief Privacy Officer |
| Chief Privacy Officer | Breach determinations and multi-state notices |
| Vice President, Corporate Communications | Media, worker, grower, and customer communications |
| Chief Operating Officer | Crisis lead for operational recovery |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 The company must maintain an incident response plan with an OT annex and runbooks for its most likely severe incidents, starting with ransomware on farm-management and irrigation control systems with data theft (P08). (IR-8; RS.MA-01)
4.2 Workforce, integrators, and vendors must report suspected incidents to the SOC within 1 hour. Control center operators must also report any unexplained setpoint, schedule, or recipe change immediately. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 In an OT incident, the first step is a safe state: fertigation and chemigation injection stop, and affected pumps and pivots go to local or manual control under PRC-03.3, before any containment action that could stop water. Safety interlocks must never be bypassed to restore service. (IR-4; SI-6; RS.MI-01)
4.4 Every incident must be logged, classified by severity under STD-03.1 (including safety and crop-loss factors), and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-03)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 4 hours, and the disclosure committee must convene within 24 hours to begin the materiality assessment under PRC-03.2. (IR-6; IR-8; RS.MA-04)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay, and amended within 4 business days when missing information becomes available. (IR-6; RS.CO-02)
4.7 The Chief Privacy Officer must determine for every incident involving personal information which states' laws apply, by the residence of each affected person, and notices must meet the deadlines in the P08 notification matrix. Retail and foodservice customers must be notified within 24 hours of any event that could affect product safety, lot traceability, or committed volumes. (IR-6; RS.CO-02)
4.8 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. Each region must keep and drill a manual irrigation and freeze-protection procedure every November. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 Field OT links must keep an alternate path (licensed radio or a second carrier) for freeze-protection stations, and the field network design must avoid dependence on one carrier for more than half of field devices by 2027-06-30. (CP-8; PR.IR-03)
4.11 The incident response plan must be exercised at least annually, including one exercise a year that combines an OT outage with the disclosure committee, and after every major organizational change such as an acquisition. Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-3; IR-8; ID.IM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard (with the OT safe-state annex)
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Manual Irrigation and Freeze-Protection Procedure (one per region)
- PRC-03.4 Multi-State Breach Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and OT change and session reviews. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Vendor violations are handled under the contract and STD-01.9.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FMICP SSP; P03 gap analysis; P05 BIA; P08 runbook and notification matrix; P10 AI governance.
