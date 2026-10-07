# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory basis | 47 CFR 64.2009(b), (e); 64.2010(a); 47 CFR 1.20003(a), 1.20005(a); 17 CFR 229.106; Fla. Stat. 501.171(2) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer, network, and company information, and supports the company's CPNI, CALEA, outage reporting, SEC, state, and federal contract obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) and the agents of care vendors and other third parties who use company systems, in all four states, including acquired carriers from their closing date. Covers all systems and data, including the carrier network and its management plane, the lawful-intercept platform, cloud, data centers, SaaS, and systems that vendors operate for the company, and the services offered to business customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk and technology committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Compliance Officer | CPNI compliance officer; signs the annual CPNI certifications |
| Director, Lawful Intercept Compliance | CALEA senior officer for the main operating company; coordinates the subsidiaries' designees |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that provides the reasonable measures required to protect CPNI and meets other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The Chief Compliance Officer must be designated in writing as the CPNI compliance officer, and each operating carrier subsidiary must have a CALEA senior officer or employee designated in writing and named in its filed SSI policies. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Public safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members and vendor agents who misuse CPNI or violate security policies must be sanctioned under PRC-01.1, which names unauthorized use or disclosure of CPNI as a specific violation, in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive or access CPNI or customer personal information until a contract with CPNI confidentiality terms, notice of security incidents within 24 hours, and audit rights is signed and the vendor has been tiered and assessed under STD-01.3. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; ID.IM-01)
4.10 Every acquisition must include security due diligence before closing, a CALEA SSI filing plan that meets the 90-day refiling rule, and an integration plan that brings identity, network, logging, CPNI, and endpoint controls to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-03)
4.11 Security documentation must be retained at least 6 years; CPNI approval and notice records at least 1 year; CPNI breach records at least 2 years; CALEA intercept records as set in the SSI policies. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk and technology committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 Each annual CPNI certification must be supported by an evidence package, reviewed by Internal Audit, that shows how operating procedures ensure compliance, before the officer signs it. (CA-2; PM-1; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Network Element Security Standard
- PRC-01.1 Sanctions Procedure (including CPNI misuse)
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 CPNI Certification Evidence Procedure
- PRC-01.5 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CPNI certification evidence package. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of a vendor agent's access, in proportion to intent and harm. Misuse of CPNI is always a sanctionable violation.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a public safety risk at High or above are refused unless a dated treatment plan exists. Exceptions to a regulatory requirement (for example, a CPNI authentication rule) are never granted; only the timing of remediation can be risk-accepted, with compensating controls. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OSS/BSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
