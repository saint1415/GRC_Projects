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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, SA-9, SA-10, SR-4, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.OV-01, GV.RM-03, GV.SC-05, PR.PS-06 |
| Binding requirements served | SEC Reg S-K Item 106 (program description); FAR 52.204-21; utility addenda (CIP-013-2 R1.2 flow-down) |

## 1. Purpose
Establish the enterprise information security program for IT, OT, and products; assign accountability from the board to every workforce member; set the policy hierarchy and the exceptions process; and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, and supplier information, keeps grid equipment production safe and running, and supports the company's SEC, federal contract, export, DOE, and utility contract obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 7 plants, 9 service centers, 3 spare yards, and offices in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, including the acquired Ohio plant (AQ-01) from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant control systems (OT), test systems, and systems that suppliers operate for the company, and the products and services the company supplies to utilities (TMU firmware and configuration software, the Fleet Monitoring Service, and the Spare Transformer Reserve Service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of OT Security | Accountable for OT security standards across all plants |
| Director of Product Security | Accountable for product security and vulnerability disclosure |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, using NIST SP 800-82 Rev. 3 for OT, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be accountable for the program; the Director of OT Security must be designated in writing for OT security at every plant, and the Director of Product Security for products supplied to customers. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-03)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Process safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-04)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; ID.RA-07)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No supplier may receive system access or company data until it is tiered and assessed under STD-01.3 and its contract includes security, breach notice, and audit terms. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation; OT controls must be tested by an assessor with OT qualifications. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence, including OT, before closing and a funded integration plan that brings identity, network, logging, and OT controls to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.SC-06)
4.11 Every contractual or regulatory cybersecurity obligation (utility addenda, federal contract clauses, SEC, EAR, DOE records) must be recorded in the obligations register with its owner, trigger, and deadline within 30 days of contract signature or effective date. (SA-4; PM-9; GV.OC-03)
4.12 Security documentation, including risk analyses, assessments, and decisions, must be retained for at least 7 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02)
4.13 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.14 Firmware and software supplied to customers must be built under STD-01.9, signed with a key held in a hardware security module, released with hashes and an SBOM, and covered by coordinated vulnerability disclosure that meets each customer contract. (SA-10; SA-11; SR-4; PR.PS-06)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard (zones, OT DMZs, plant changes)
- STD-01.9 Product Security and Secure Development Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Obligations Register Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (Tables G-5 and I-2), approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a process safety risk at High or above are refused unless a dated treatment plan exists. Exceptions to a contract or regulatory requirement (for example a utility addendum term) cannot be granted internally; they need the counterparty's written agreement, obtained by the General Counsel. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EPSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
