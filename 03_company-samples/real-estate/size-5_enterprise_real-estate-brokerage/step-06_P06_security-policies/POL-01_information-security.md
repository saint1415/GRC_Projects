# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc., adopted by Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PL-2, PM-2, RA-3, PM-9, PL-1, CA-5, PS-8, SA-9, SA-4, SR-6, CA-2, CA-2(1), CA-8, CM-3, CM-5 |
| CSF 2.0 | GV.PO-01, GV.RR-02, GV.RM-01, GV.RM-06, GV.PO-02, GV.RR-04, GV.SC-05, ID.IM-01, GV.OC-01, PR.PS-01, GV.OV-01 |
| Regulatory drivers | See `policy-control-map.csv` (N53-R01 Safeguards Rule citations for each statement) |

## 1. Purpose
Establish the enterprise information security program for all entities, assign accountability from the board to every employee and contractor agent, set the policy hierarchy and the exceptions process, and give every other security policy its authority. For Cris Santos Title and Escrow, LLC this program is the written information security program required by the FTC Safeguards Rule (16 CFR 314.3(a)).

## 2. Scope
All Cris Santos Company, Inc. employees, the about 38,000 contractor sales associates who use company systems, contractors, and temporary staff, in all 9 states, and the employees of Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC, which adopted this hierarchy by resolution. Acquired firms are covered from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, contractor agents' own devices when they access company systems, and systems that vendors operate for the company, and the services offered to business clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| Title and Escrow board of managers | Governing body for the Safeguards Rule program; receives the Qualified Individual's annual report (16 CFR 314.4(i)) |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner and Qualified Individual for Title and Escrow; chairs the policy governance committee; approves standards |
| President, Title and Escrow | Senior overseer of the Qualified Individual for Title and Escrow (16 CFR 314.4(a)(2)) |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All employees and contractor agents | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain one information security program aligned to NIST CSF 2.0 that covers all entities and meets the FTC Safeguards Rule for Title and Escrow, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the Qualified Individual for Title and Escrow, and the President of Title and Escrow as the senior member who directs and oversees the Qualified Individual. The intercompany services agreement must require the parent to maintain a program that protects Title and Escrow under Part 314. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed and documented at least annually and after major changes, incidents, or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Client-funds risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Employees and contractor agents who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive, maintain, or process customer information or other personal data until it has been tiered, assessed, and contracted under STD-01.3, including security, breach notice within 10 days, and audit terms. Tier-1 vendors must be reassessed at least annually. (SA-9; SA-4; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and internet-facing systems that hold or connect to customer information must be penetration tested at least annually. (CA-2; CA-2(1); CA-8; ID.IM-01)
4.10 Every acquisition must have security due diligence and a risk assessment before closing and an integration plan under STD-01.7 that brings identity, email, logging, and funds controls to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Changes to production systems that hold or connect to customer information must follow PRC-01.3, including two approvals for any change to wire-instruction templates, approval rules, or bank connectors, even in an emergency. (CM-3; CM-5; PR.PS-01)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, and in writing to the Title and Escrow board of managers at least annually on program status, compliance, and material matters. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment and Risk Acceptance Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging and Monitoring Standard
- STD-01.5 Secure Development, Configuration, and Change Standard
- STD-01.6 Physical Security Standard
- STD-01.7 Acquisition Security Integration Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of the agent agreement, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (Tables G-5 and I-2), approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a client-funds risk at High or above are refused unless a dated treatment plan exists. Exceptions to a Safeguards Rule element that the rule itself allows (encryption compensating controls under 314.4(c)(3) and MFA equivalents under 314.4(c)(5)) also need the Qualified Individual's written approval. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TMCC SSP; P03 gap analysis; P08 BEC runbook and notification matrix; P10 AI governance.
