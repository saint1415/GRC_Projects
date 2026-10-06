# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO (Qualified Individual) |
| Approved by | Partnership Board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulations | 16 CFR 314.3, 314.4(a), (b), (e), (f), (g), (i); 26 CFR 301.7216-1(a); 45 CFR 164.308(a)(1), (a)(2) (business associate); Fla. Stat. 501.171(2) |

## 1. Purpose
Establish the firm's information security program (its written information security program under 16 CFR 314.3(a)), assign accountability from the Partnership Board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects taxpayer, client, and firm information and supports the firm's obligations under the FTC Safeguards Rule, IRC 7216, IRS e-file rules, HIPAA as a business associate, FAR 52.204-21, and state law.

## 2. Scope
All Cris Santos Company partners, employees, seasonal staff, contractors, and interns in all 64 offices and the 12 processing hubs, and staff of acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, the offshore provider workspace, and systems that service providers operate for the firm, and the services the firm offers to clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Partnership Board | Governing body for 16 CFR 314.4(i); approves this policy and the risk appetite; receives the Qualified Individual's annual written report |
| Audit and Risk Committee | Oversees Internal Audit and quarterly cyber risk reporting |
| CEO and Managing Partner; CFO | Accept Very High risks jointly |
| CISO | Qualified Individual (16 CFR 314.4(a)); program owner; chairs the policy governance committee; approves standards |
| Director of Security Operations | HIPAA Security Official for the business associate role (45 CFR 164.308(a)(2)); runs the SOC |
| Chief Privacy Officer | Privacy program; retention and disposal; breach determinations with the General Counsel |
| Chief Risk Officer | ERM; owns the enterprise risk register; chairs the AI governance committee |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The firm must maintain a written information security program aligned to NIST CSF 2.0, documented in this policy hierarchy and in system security plans for tier-1 systems, that meets 16 CFR 314.3 and 314.4. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the Qualified Individual, and the Director of Security Operations as the HIPAA Security Official for the business associate role. (PM-2; GV.RR-02)
4.3 A written enterprise risk assessment must be performed at least annually and after material changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and Managing Partner with the CFO (Very High). Fraud and regulatory risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security, privacy, or confidentiality policies, including improper use or disclosure of tax return information, must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No service provider may access customer information, tax return information, or PHI until it has been tiered and assessed under STD-01.3 and its contract includes security, incident notice, and IRC 7216 terms (and a business associate agreement where PHI is involved). Tier-1 and tier-2 providers must be reassessed at least annually. (SA-9; SR-6; GV.SC-05)
4.9 Every individual at a contractor who receives tax return information to program, maintain, repair, or test tax software or equipment must receive the written notice of IRC 6713 and 7216 before access. (SA-9; PS-7; GV.SC-05)
4.10 Every acquisition must include security due diligence before closing, a risk assessment within 90 days of closing, and an integration plan that brings identity, email, logging, endpoint, and tax platform controls to firm standards within 12 months. (RA-3; SA-9; GV.OC-01)
4.11 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.12 The Qualified Individual must report in writing to the Partnership Board at least annually on the overall status of the program and compliance with 16 CFR Part 314 and on material matters, and to the Audit and Risk Committee quarterly on risks outside tolerance. (PM-9; GV.OV-01)
4.13 Security documentation, including risk assessments, assessments, incident records, and Qualified Individual reports, must be retained for at least 7 years. (SI-12; GV.PO-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, partnership, or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception to a regulatory requirement (for example, an MFA alternative under 16 CFR 314.4(c)(5) or an encryption alternative under 314.4(c)(3)) also needs the Qualified Individual's written approval. Requests that would leave a fraud or regulatory risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Tax Engagement Platform SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
