# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, significant incidents, a new TSA directive or directive revision, or an acquisition by the sponsor |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, CA-7, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.IM-01 |
| Regulatory basis | C-TRANSPORTATION-R01 (SD 1580/82-2022-01E II.B, III.F, VI; SD 1580-21-01E II.B, II.E); C-TRANSPORTATION-S01 (1570.105, 1570.201); C-TRANSPORTATION-S06 (172.802) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the safety of train operations, the movement of customers' freight, and the information the company holds, and it carries out the measures in the company's TSA-approved Cybersecurity Implementation Plan (CIP).

## 2. Scope
All workforce members (employees, contractors, and vendor staff with access) at the HQ campus and Central Yard, the backup NOC at Jacksonville Terminal Yard, Southern Yard and the other yards, shops, transload terminals, tower sites, wayside locations, and on locomotives. It covers all information technology and operational technology: the Train Dispatch and PTC Operations Platform (TDPO), the field network, onboard PTC equipment, the cloud landing zone, and the SaaS and managed services that vendors operate for the company. It covers the shared dispatch and car management service the company provides to other railroads.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports and the summary of the TSA CAP annual report |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and TDPO system owner; approves POL-02 to POL-05; accepts Moderate risks; reviews CIP milestones monthly |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Cybersecurity Manager | Runs the program day to day; primary TSA Cybersecurity Coordinator; owns the CIP and CAP; incident commander |
| Director of Information Technology | IT and cloud operations; alternate TSA Cybersecurity Coordinator |
| Director of Safety, Security, and Hazmat | Primary TSA Security Coordinator; hazmat security plan; SSI; TSA security training program |
| Chief Dispatcher on duty | Alternate TSA Security Coordinator through the 24/7 NOC |
| Director of Network Operations, Director of Signals and Communications, PTC Program Manager, Chief Mechanical Officer | Apply policies to the dispatch, field, PTC, and onboard systems they own; approve access; own manual procedures |
| General Counsel | Legal and regulatory interpretation; SSI disclosure questions; contracts |
| Co-sourced internal audit firm | Independent annual control assessment (P07), counted toward the CAP |
| All workforce | Follow the policies and report suspected incidents immediately |

**Where roles overlap.** The Cybersecurity Manager owns the CIP and also leads incident response, and the Director of IT both runs and secures IT. At 850 employees the company does not separate these further. The compensating controls are the independent assessment by the co-sourced internal audit firm (statement 4.10), monthly CIP milestone review by the COO (4.5), and audit committee reporting (4.6).

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the supporting standards, the System Security Plan (P02), and the TSA-approved CIP and CAP. For Critical Cyber Systems, the CIP is the controlling document; no policy or standard may weaken a CIP measure. (PM-1; PL-2; GV.PO-01)
4.2 **Coordinators.** The company must designate in writing a primary and at least one alternate TSA Cybersecurity Coordinator (at least one a U.S. citizen) and a primary and at least one alternate Security Coordinator, all at the corporate level and reachable 24 hours a day. Coordinator details must be sent to TSA within 7 days of any change (SD 1580-21-01E II.B.1.e) and Security Coordinator details within 37 calendar days of any change (49 CFR 1570.201(e)). (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and coordinated with the annual review of the hazmat security plan risk assessment (49 CFR 172.802(a)). Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. No risk that could plausibly contribute to a train accident, a roadway worker injury, or a hazmat release may be accepted above Low. (PM-9; GV.RM-01)
4.5 **Keeping the approved plan.** CIP measures must be implemented on the schedule TSA approved. The COO reviews the CIP milestone tracker monthly. If a measure will not be met on time, the Cybersecurity Manager must notify TSA before the date passes and request an amendment. Any permanent change to Critical Cyber Systems, or to the policies and measures the CIP describes, must be filed with TSA as an amendment request no later than 50 days after the change takes effect (SD 1580/82-2022-01E VI.B and VI.D). (CA-5; PM-9; GV.OV-01)
4.6 The vCISO must report to the audit committee each quarter on the top risks, CIP milestone status, CAP progress, POA&M status, and incidents. (PM-9; GV.OV-01)
4.7 **Applicability checks.** The Director of Safety, Security, and Hazmat must confirm each year, and before any new or modified operation, whether the company still meets 49 CFR 1580.101, and notify TSA as 1570.105 requires. The Cybersecurity Manager must review each new or renewed TSA directive within 30 days of issue. (PM-9; GV.OC-03)
4.8 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.9 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. An exception may not conflict with a CIP measure unless TSA has approved the change. (PL-1; GV.PO-01)
4.10 **Assessment.** Security controls must be independently assessed at least annually, and the Cybersecurity Assessment Plan must assess at least one-third of CIP measures each plan year and all of them over any 3 years, including a cybersecurity architecture design review at least every 2 years (SD 1580/82-2022-01E III.F.2). (CA-2; CA-7; ID.IM-01)
4.11 **Sanctions.** Workforce members who violate security policies must be disciplined in proportion to intent and harm, from retraining to termination. For employees covered by a collective bargaining agreement, the agreement's procedures apply. (PS-8; GV.RR-04)
4.12 **Vendors.** Before a vendor gets access to a Critical Cyber System, SSI, or Restricted data, it must pass a security review scaled to its tier (STD-03), and its contract must include security requirements, incident notice terms, and the CIP measures the vendor performs. The company remains responsible for CIP measures delegated to a managed security service provider or other authorized representative (SD 1580/82-2022-01E II.A.2 and II.A.3). (SA-9; GV.SC-05)
4.13 Tier 1 vendors must be reassessed each year, including a review of their SOC 2 Type 2 report or an equivalent assessment (STD-03; P09). (SR-6; GV.SC-07)
4.14 Security policies, risk assessments, CIP and CAP records, assessment results, and incident records must be kept for at least 5 years, and longer where a rule or contract requires. SSI records follow POL-04. (SI-12; GV.PO-02)
4.15 AI tools must be approved through the AI governance process (STD-05; P10) before use with company data or in any operational decision. No AI output may replace an inspection or decision that an FRA rule assigns to a qualified person. (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under statement 4.11. Compliance is checked through the annual independent assessment (P07), the CAP schedule, quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow statement 4.9. They must be written, risk-rated, approved by the right authority under 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis (P03); TSA-approved CIP and CAP (SSI, restricted library); hazmat security plan; SD 1580/82-2022-01E; SD 1580-21-01E; 49 CFR parts 1520, 1570, and 1580
