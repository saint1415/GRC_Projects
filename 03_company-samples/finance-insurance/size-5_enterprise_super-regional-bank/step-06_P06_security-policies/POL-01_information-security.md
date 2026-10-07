# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (with Cris Santos Bank, N.A. and Cris Santos Investment Services, LLC) |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Board risk committee (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory basis | 12 CFR 30 App. B II.A, III.A to III.F; App. D I.E.7, II.A, II.C; 12 CFR 252.22; 17 CFR 248.30(a)(1)-(2), (a)(5) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer, client, and company information and supports the group's obligations under the Interagency Guidelines, the OCC heightened standards, the Federal Reserve risk committee rule, SEC disclosure rules, and Regulation S-P.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the parent, Cris Santos Bank, N.A., and Cris Santos Investment Services, LLC, at all sites in the six footprint states and remote locations, including the acquired bank's staff and systems from the merger date. Covers all systems and data, including the data centers, both clouds, SaaS, branches, ATMs, and systems that third parties operate for the group, and the services the group offers to institutional clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of directors and board risk committee | Approve this policy, the information security program, and the risk appetite statement; receive quarterly cyber risk reports and the annual report under App. B III.F; oversee cyber risk for Item 106 |
| Board audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Risk Officer | Chief Risk Executive; leads independent risk management, including second-line challenge of cyber risk |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Audit Executive | Independent assessment (third line) |
| Chief Privacy Officer | Customer notice decisions; GLBA privacy |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The group must maintain an information security program aligned to NIST CSF 2.0 that meets the Interagency Guidelines (12 CFR 30 App. B) and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The board must designate in writing the executive responsible for the information security program (the CISO). Second-line challenge of cyber risk must sit in independent risk management under the Chief Risk Officer; no front line unit executive may oversee it. (PM-2; GV.RR-02)
4.3 An enterprise cyber risk assessment must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive and second-line concurrence (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Regulatory and disclosure risks above Low must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No third party may access customer information until it is tiered, assessed, and bound by contract to security measures, incident notice within a stated time frame, and, for bank service providers, a bank-designated 12 CFR 53.4 contact. Broker-dealer service providers must agree to notify within 72 hours (17 CFR 248.30(a)(5)). SOC reports of critical third parties must be reviewed every year with complementary user entity controls mapped. (SA-9; SR-6; GV.SC-05)
4.9 Security controls of tier-1 systems and common control providers must be assessed at least annually by Internal Audit or another assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, payment controls, and customer authentication to enterprise standards within 12 months of the merger date. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk assessments, assessments, and notification determinations, must be retained for at least 7 years. (SI-12; GV.PO-02)
4.12 The CISO must report cyber risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and significant incidents, and must deliver the annual report required by App. B III.F. (PM-9; GV.OV-01)
4.13 Models, including AI models, that make or support credit, fraud, or BSA/AML decisions must be in the model inventory and independently validated before use; credit models must also pass fair lending testing. Generative AI use cases must be approved by the AI governance committee (STD-01.8). (RA-3; CA-7; GV.RM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Model and AI Risk Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, second-line reviews by independent risk management, the annual Internal Audit assessment (P07), and quarterly access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (Tables G-5 and I-2), approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a regulatory or disclosure risk above Low are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CBDC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
