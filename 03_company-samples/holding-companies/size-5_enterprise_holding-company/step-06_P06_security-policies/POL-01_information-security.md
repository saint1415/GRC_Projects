# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (holding company, GBS, and all subsidiaries) |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-04, GV.SC-05 |
| Regulatory drivers | Reg S-K Item 106(b)-(c) (N55-R01); Rule 13a-15 and SOX 404 (N55-R03); 16 CFR 314.3(a), 314.4(a)-(b), (f), (i) for Finance |

## 1. Purpose
Establish the group information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of the group's financial reporting, payments, customer, employee, and operational information, and supports the group's SEC, SOX, FTC Safeguards Rule, HIPAA plan sponsor, and state law obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the holding company, Global Business Services (GBS), and every subsidiary (Building Products, Home Services, Manufacturing, and Finance), at all sites in the six operating states, including acquired businesses from their closing date. Covers all systems and data, including cloud, data centers, SaaS, plant OT, systems that vendors operate for the group, and the services offered to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives the CISO report each quarter (Item 106(c)) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; certify disclosure controls and ICFR; take part in materiality determinations |
| CISO | Group program owner; chairs the policy governance committee; approves standards |
| Subsidiary Presidents and BISOs | Apply the program in each subsidiary; sub-certify quarterly |
| Finance Information Security Officer | Finance's Qualified Individual (16 CFR 314.4(a)); reports annually to Finance's board |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 The group must maintain an information security program aligned to NIST CSF 2.0 that covers the holding company, GBS, and every subsidiary, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is accountable for the group program. Each subsidiary must designate a business information security officer, and Finance must designate its Qualified Individual in writing. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Plant-safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 Vendors must be tiered by criticality, including whether they can change identities, release payments, or reach customer or employee data. No vendor may receive that access until security terms are in its contract, and tier-1 vendors must be reassessed at least annually. (SA-9; SR-6; GV.SC-04; GV.SC-05)
4.9 Controls for tier-1 systems must be assessed at least annually by an assessor independent of their operation, and every common control provider must be assessed by Internal Audit at least once every 3 years. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include technical cyber due diligence before signing and an integration plan, funded in the deal approval, that brings identity, network, logging, and endpoint controls to group standards within 12 months of closing. (RA-3; SA-9; GV.SC-06)
4.11 Security documentation, including risk assessments, assessments, and exception records, must be retained for at least 7 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, and quarterly sub-certifications from every subsidiary must include cybersecurity incident questions. (PM-9; GV.OV-01)
4.13 A new AI use, including an AI feature turned on in an existing product, must be registered and assessed by the AI governance committee before use (P10). (RA-3; ID.RA-04)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Acquisition Cyber Diligence and Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly sub-certifications, access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Exceptions touching Finance customer information also need the Finance Information Security Officer's written agreement. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SCSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; Finance WISP annex (SUP-FIN); Manufacturing OT annex (SUP-MFG).
