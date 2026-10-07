# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory drivers | MTSA 33 CFR 101.620, 101.625, 101.630(f); RMP 40 CFR 68.15, 68.75; PSM 29 CFR 1910.119(l); Reg S-K Item 106; CFATS RBPS 8 (voluntary benchmark) |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, and process information and, above all, the integrity of the control and safety systems that keep hazardous chemicals contained. It supports the company's MTSA, RMP, PSM, DOT, release reporting, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, integrators, and temporary staff) at all 14 plants, 9 distribution centers, 2 R&D centers, and offices, including acquired plants from their acquisition date. Covers all information technology (IT) and operational technology (OT): process control systems, safety instrumented systems, PLCs, terminal and loading rack automation, cloud, colocation, SaaS, and systems that vendors and integrators operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity and process safety risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | Authorizing official equivalent for OT systems |
| CISO | Program owner for IT and OT security; chairs the policy governance committee; approves standards |
| Director of OT Security | Leads the OT Security Center of Excellence; owns OT standards and the enterprise OT security services |
| Plant Cybersecurity Officers (CySO) | PLT-01 CySO under 33 CFR 101.620(b)(3); plant OT security leads at other plants |
| Vice President, Process Safety and EHS | Process safety program; makes sure MOC and PHA cover control system changes and cyber scenarios |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program for IT and OT aligned to NIST CSF 2.0, with OT controls based on NIST SP 800-82 Rev. 3, documented in this policy hierarchy and in system security plans for tier-1 systems and critical OT systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be accountable for IT and OT security. Each MTSA facility must have a Cybersecurity Officer designated in writing by name and title, accessible 24 hours a day, with an alternate. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. It must feed the MTSA Cybersecurity Assessment and the PHA program. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Process safety risks at Moderate or above must not be accepted without a dated treatment plan and the concurrence of the Vice President, Process Safety and EHS. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor or integrator may access OT, or hold Restricted or SSI information, until it has been tiered and assessed under STD-01.9 and its contract includes security requirements and a duty to notify the company of vulnerabilities and cyber incidents without delay. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; SA-4; GV.SC-05)
4.9 Security controls for tier-1 systems, critical OT systems, and common control providers must be assessed at least annually by an assessor independent of their operation. Auditors of an MTSA Cybersecurity Plan must have no regularly assigned cybersecurity duties at that facility. (CA-2; ID.IM-01)
4.10 Every acquisition must include OT and IT security due diligence before closing and an integration plan that brings remote access, segmentation, accounts, logging, and backups to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 6 years, and MTSA records for at least the period in 33 CFR 105.225. (SI-12; GV.PO-02)
4.12 The CISO, jointly with the Vice President, Process Safety and EHS for process safety risks, must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 Any change to a control system, safety instrumented system, alarm limit, or recipe, and any change that could move a chemical above a regulatory threshold or listing concentration (for example, buying hydrogen peroxide at 52% or more), must go through management of change, with a security impact question answered before approval. (CM-3; CM-4; PR.PS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Network and Communications Security Standard (annex A: OT reference architecture)
- STD-01.3 Configuration and Change Management Standard (annex B: OT hardening baselines)
- STD-01.4 Security Awareness and Training Standard
- STD-01.5 Personnel Security Standard
- STD-01.6 Logging and Monitoring Standard
- STD-01.7 Contingency and Recovery Standard (IT and OT)
- STD-01.8 Security Assessment and Authorization Standard
- STD-01.9 Supply Chain and Third-Party Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 OT Change and MOC Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT metrics), the annual Internal Audit assessment (P07), access certifications, and MTSA Cybersecurity Plan audits at PLT-01. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. OT exceptions also need the plant manager's sign-off, and any exception that touches a safety instrumented system or a PSM or RMP process needs the concurrence of the Vice President, Process Safety and EHS. An exception can never waive a regulatory requirement; at an MTSA facility, a measure that cannot be met is handled through documented compensating controls where the rule allows them, or a waiver or equivalence request to the Coast Guard (33 CFR 101.665). Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GC-PCBMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
