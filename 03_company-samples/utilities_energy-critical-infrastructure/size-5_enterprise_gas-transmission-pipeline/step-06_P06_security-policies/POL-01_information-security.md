# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 (version 2026.1; revises the 2025 version that Internal Audit tested in P07) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or a new TSA security directive |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, CM-3, SA-9, SI-2, SI-4, SI-12, AU-6, AU-11 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OV-01, GV.RM-01, GV.RM-06, GV.OC-03, GV.SC-05, ID.IM-01 |
| Regulatory drivers | TSA SD Pipeline-2021-01G (C-ENERGY-R02) and SD Pipeline-2021-02G (C-ENERGY-R03); 49 CFR 192.631 (C-ENERGY-R04); 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program for business IT and operational technology (OT), assign accountability from the board to every worker, and give every other security policy its authority. The program protects safe pipeline operation first, then reliable gas deliveries, and the confidentiality of Sensitive Security Information (SSI), Critical Energy Infrastructure Information (CEII), shipper data, and employee data. It is how the company meets the TSA security directives, the PHMSA control room management rule, and its SEC disclosure duties.

## 2. Scope
All Cris Santos Company employees, contractors, and authorized representatives in all 9 states. Covers all IT and OT systems and data: the three control rooms (GCC-1, GCC-2, PS3-CR), 96 compressor stations, meter and valve sites, SCADA telecommunications, both public clouds, both colocation data centers, SaaS, and systems that suppliers operate for the company. Covers the PS-3 pipeline system from its acquisition date, and the JV-1 to JV-3 pipelines the company operates for their owners (SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks jointly; take part in materiality determinations |
| Chief Operating Officer | Accountable executive for pipeline operations; authorizing official equivalent for the PSGCS (P02) |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Director of OT Security | Primary TSA Cybersecurity Coordinator; owns the Cybersecurity Implementation Plan and Cybersecurity Assessment Plan |
| Director of Security Operations | Runs the SOC and OT monitoring cell; alternate Cybersecurity Coordinator |
| Vice President, Gas Control | Owns the control room management procedures (49 CFR 192.631) |
| Chief Risk Officer | Enterprise risk management; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workers | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain a security program for IT and OT aligned to NIST CSF 2.0, documented in this policy hierarchy, in system security plans for tier-1 systems, and in the TSA-approved Cybersecurity Implementation Plan. (PM-1; PL-2; GV.PO-01)
4.2 The Director of OT Security must be designated in writing as the primary TSA Cybersecurity Coordinator, with at least one alternate. At least one of them must be a U.S. citizen eligible for a security clearance, one must be reachable 24 hours a day, and TSA must receive coordinator changes within 7 days. (PM-2; IR-7; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Risks to safe pipeline operation (ER-01) at Moderate or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Any change to a measure in the TSA-approved Cybersecurity Implementation Plan that is intended to last 45 days or more must be logged under PRC-01.3, and the amendment request must reach TSA no later than 50 calendar days after the change takes effect. A change of ownership or control of operations requires an amendment request before it takes effect. (PL-2; CM-3; GV.OC-03)
4.8 Suppliers must be tiered under STD-01.3. Suppliers with OT access or OT data must accept contract terms that require compliance with the plan measures that apply to them, notice to the company of any security incident affecting company systems or data within 24 hours, and software bills of materials for OT software they supply. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Tier-1 systems and common control providers must be assessed at least annually by assessors independent of their operation. The Cybersecurity Assessment Plan must assess at least one-third of the plan measures each year and all of them within three years, and must include an architecture design review at least every two years. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, endpoint, and OT controls to enterprise standards within 12 months of closing, or by the date in a TSA-approved plan amendment. (RA-3; SA-9; ID.RA-07)
4.11 Security documentation, including risk analyses, assessments, plans submitted to TSA, and control room management records, must be retained for at least 5 years from creation or last effective date, or longer where a regulation or the records schedule requires. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the risk committee of the board at least quarterly, including Very High and High risks, risks outside tolerance, the status of TSA plan schedules, and material incidents. (PM-9; GV.OV-01)
4.13 Changes that could affect control room operations (SCADA software, displays, points, alarm settings, station controls, telemetry, and analytics shown to controllers) must go through management of change with Gas Control participation, testing, and point-to-point verification where 49 CFR 192.631(c)(2) requires it. (CM-3; CM-4; PR.PS-01)
4.14 Security patches must be categorized and applied within the timelines in STD-01.8, with entries in CISA's Known Exploited Vulnerabilities Catalog prioritized. Where patching an OT component would severely degrade operations, the mitigations and a timeline must be documented. (SI-2; RA-5; ID.RA-01)
4.15 Every Critical Cyber System must forward security logs to the SIEM, keep them 12 months online, and be covered by network monitoring that detects deviations from its communications baseline. (AU-6; AU-11; SI-4; DE.CM-01)
4.16 Workers who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and Authorization Standard (includes the Cybersecurity Assessment Plan schedule)
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging Standard (event list, OT log sources, retention)
- STD-01.5 Configuration and Change Management Standard (includes management of change for control room operations)
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Patch and Vulnerability Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 TSA Plan Amendment Procedure
- PRC-01.4 Acquisition Security Due Diligence and Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, monthly tracking of Cybersecurity Implementation Plan measures, the annual Internal Audit assessment (P07), and the TSA Cybersecurity Assessment Plan. Violations are handled under PRC-01.1 (statement 4.16), from retraining to termination of employment or contract.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception never changes a TSA-approved plan measure; if it would, the plan amendment process (statement 4.7) applies as well. Requests that would leave an ER-01 safety risk at Moderate or above are refused unless a dated treatment plan exists. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; TSA-approved Cybersecurity Implementation Plan and Cybersecurity Assessment Plan; control room management procedures; P01 risk register; P02 PSGCS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
