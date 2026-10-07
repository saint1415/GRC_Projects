# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk and reliability committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, self-reports, or CIP-002 categorization changes |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-2(1), SA-9, SR-2, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| NERC CIP | Supports CIP-003-9 R1 and R3; the CIP Cyber Security Policy carries the CIP-specific topics |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of grid operations, customer information, and company information, and supports the company's NERC, DOE, SEC, FTC, and state law obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and vendor personnel with access) at all sites in Florida and Georgia, including the control centers, substations, operations centers, and data centers. Covers all IT and OT systems and data, including cloud, SaaS, and systems that vendors operate for the company, and the services offered to external clients (SL-1 Utility Services and SL-2 fleet charging).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and reliability committee of the board | Oversees cyber and physical security risk and CIP compliance; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CIP Senior Manager (SVP, Transmission and System Operations) | Approves the CIP Cyber Security Policy and CIP program documents the standards require; leads CIP compliance |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Chief Compliance Officer and Director, NERC Compliance | Second-line compliance, self-reports, SERC audits |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents and suspicious activity |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program for IT and OT aligned to NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for OT, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CIP Senior Manager must be identified by name and any change documented within 30 calendar days; delegations must be documented with the delegate, the actions, and the date. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Every capital project that adds or changes transmission Facilities, control center systems, or substation automation must pass a CIP-002 and CIP-014 applicability check at its design gate. (RA-2; SA-3; GV.OC-03)
4.5 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). A known or potential noncompliance with a NERC Reliability Standard must never be accepted as a risk; it must be mitigated and self-reported. (PM-9; GV.RM-06)
4.6 Policies must be reviewed at least annually; the CIP Cyber Security Policy at least once every 15 calendar months; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.7 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.8 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.9 No vendor may receive access to OT, customer personal information, or BES Cyber System Information until it has been tiered and assessed under STD-01.3, and contracts must include incident notification, vulnerability disclosure, and remote access terms. (SA-9; SR-6; GV.SC-05)
4.10 Every procurement of products or services for high or medium impact BES Cyber Systems and their EACMS and PACS must complete the CIP-013 supply chain risk assessment before the purchase order is issued. (SR-3; SR-6; GV.SC-06)
4.11 Security controls for tier-1 systems, common control providers, and the CIP program must be assessed at least annually by assessors independent of their operation; internal CIP compliance checks must be performed by the NERC compliance team, not by the teams that operate the controls. (CA-2; CA-2(1); ID.IM-01)
4.12 Security documentation, including risk analyses, assessments, and CIP evidence, must be retained for at least 7 years from creation or last effective date, unless a NERC standard or regulation requires longer. (SI-12; GV.PO-02)
4.13 The CISO must report cybersecurity risk and CIP compliance status to the risk and reliability committee at least quarterly, including Very High and High risks, risks outside tolerance, self-reports, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- OT-STD-01 OT Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (IT and OT)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, statement 4.8).

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. NERC Reliability Standard requirements and legal deadlines cannot be excepted internally; where a CIP requirement allows "where technically feasible," a Technical Feasibility Exception is requested from SERC. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; the CIP Cyber Security Policy; `policy-hierarchy.md`; P01 risk register; P02 DOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
