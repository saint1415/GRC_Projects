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
| Implements (SP 800-53 Rev. 5) | PM-1, PL-2, PM-2, RA-3, PM-9, PL-1, CA-5, PS-8, SA-9, SR-6, CA-2, CA-2(1), SI-12, CM-3, CM-5 |
| CSF 2.0 | GV.PO-01, GV.RR-02, GV.RM-01, GV.RM-04, GV.PO-02, GV.RR-04, GV.SC-05, ID.IM-01, GV.SC-06, GV.OV-01, ID.RA-07 |
| Binding rules served | N56-R03 (8 CFR 274a.2(g)(1)); Fla. Stat. 501.171(2); E-Verify MOU Art. II.A.15; N56-R02 (15 U.S.C. 1681b(b)); Fla. Stat. 501.171(6); N56-R03 (8 CFR 274a.2(e)(4)); SEC S-K 106(c) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of associate, candidate, client, and company information, keeps associates paid correctly and on time, and supports the firm's Form I-9, E-Verify, FCRA, federal contract, state privacy, AI employment, and SEC obligations.

## 2. Scope
All Cris Santos Company internal employees, contractors, and temporary associates while they use company systems (the associate app, time clocks, kiosks), at all of its about 520 sites in 38 states and the District of Columbia, including acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors operate for the firm, and the services the firm offers to clients (SL-1 Workforce Management Platform and SL-2 payrolling).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and technology committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Privacy Officer | Privacy program; breach determinations |
| Vice President, Employment Compliance | Form I-9, E-Verify, FCRA, and records retention program (CCP-09) |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The firm must maintain an information security program aligned to NIST CSF 2.0, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is accountable for the security program, the Chief Privacy Officer for the privacy program, and the Vice President, Employment Compliance for the Form I-9, E-Verify, and FCRA records program; each designation must be in writing. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at these authority levels: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Payroll integrity and patient-safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-04)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who misuse associate or candidate data, E-Verify, or consumer reports, or otherwise violate security policies, must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive associate, candidate, or client personal information until it has been tiered and assessed under STD-01.8 and its contract includes security, 72-hour incident notice, and data return terms. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before signing, funded integration, and a plan that brings identity, logging, network, and records controls (including Forms I-9) to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.SC-06)
4.11 Security documentation, including risk analyses, assessments, and POA&Ms, must be retained for at least 7 years under STD-04.2. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the risk and technology committee of the board at least quarterly, including Very High and High risks, risks outside tolerance, fraud losses, and material incidents. (PM-9; GV.OV-01)
4.13 Changes to payroll rules, tax tables, bank file settings, Form I-9 and E-Verify configuration, and AI tool settings must go through change control with approval by someone other than the person making the change (PRC-01.3). (CM-3; CM-5; ID.RA-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Security Planning and Baseline Standard
- STD-01.2 Risk Assessment Standard
- STD-01.3 Configuration, Change, and Maintenance Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 System Protection and Integrity Standard
- STD-01.6 Security Assessment and Authorization Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Third-Party, Acquisition, and Supply Chain Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (including payroll, Form I-9, E-Verify, and AI configuration)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and the fraud and KRI dashboards. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a payroll integrity or patient-safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ALPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
