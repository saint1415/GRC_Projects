# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Safety, environmental, and risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(a)(1)(A)(ii), (b)(1), (d)); 17 CFR 229.106(b)-(c) |

## 1. Purpose
Establish the converged IT and OT information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the safety and reliability of drinking water service, the integrity of treatment and distribution control, and the confidentiality of customer and infrastructure information, and supports the company's SDWA section 1433, public notification, release reporting, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in all four regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee and in the two service lines, including acquired systems from their acquisition date. Covers all IT and OT systems and data: SCADA, PLCs, RTUs, telemetry, and HMIs at the 126 community water systems and 5 ROCCs; cloud, colocation, and SaaS; and systems that vendors and integrators operate or support for the company, including the services offered to municipal clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Safety, environmental, and risk committee of the board | Oversees cybersecurity and resilience risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Director of OT Security | OT security architecture, OT remote access gateway, OT monitoring |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Vice President, Resilience and Emergency Management | RRA and ERP program for the 86 covered systems |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether the 2026 independent assessment tested it (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that covers IT and OT, uses NIST SP 800-82 Rev. 3 as its OT guide, and is documented in this policy hierarchy and in system security plans for tier-1 systems, including each regional SCADA system. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be accountable for the converged IT and OT program, and the Director of OT Security must be designated in writing as the accountable lead for OT security. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, rolled up into the enterprise risk register following NIST IR 8286 Rev. 1, and exported into the cyber element of each covered system's RRA before each RRA review. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Public health and safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may access OT, hold customer personal information, or support a tier-1 system until security terms are in its contract (including notice of a breach within 10 days and remote access only through company-controlled paths) and the vendor has been tiered and assessed under STD-01.3. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and each ROCC SCADA system must receive an independent OT assessment at least every 3 years. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition of a water system must include an OT site assessment before signing and an integration plan that brings remote access, network segmentation, identity, backups, logging, and public notice procedures to enterprise standards within 12 months of closing. (RA-3; SA-9; ID.RA-04)
4.11 RRAs, ERPs, and their certifications must be retained for at least 5 years after each certification; public notices and 141.31(d) certifications for at least 3 years; other security documentation for at least 5 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity and OT risk to the safety, environmental, and risk committee at least quarterly, including Very High and High risks, risks outside tolerance, material incidents, and the EPA certification calendar. (PM-9; GV.OV-01)
4.13 Internal Audit must test each statement in the annual Item 106 disclosure against practice before the Form 10-K is filed. (CA-2; GV.OV-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and OT Vendor Security Standard
- STD-01.4 Audit Logging Standard (IT and OT)
- STD-01.5 Configuration and Change Management Standard (including PLC logic)
- STD-01.6 OT Asset Lifecycle and Maintenance Standard
- STD-01.7 Physical Security Standard (plants and remote sites)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 OT Change Management Procedure
- PRC-01.4 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, the annual independent assessment by Internal Audit and the co-sourced OT assessment firm (P07), and plant drills. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a public health and safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GCR-WTSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; each covered system's RRA and ERP.
