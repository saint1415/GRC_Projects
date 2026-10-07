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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new contract types |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, SA-9, SR-3, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05, GV.OC-03 |
| Contract and legal basis | State exhibits (PL-1, PM family program controls); FAR 52.204-25 and 52.204-30 (screening); SEC 17 CFR 229.106 (governance) |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company and customer information and of the customer building systems the company operates, and supports the company's contract, FAR, CUI, CJIS, FERPA, state law, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor personnel working under company accounts) in all segments and acquired businesses from their acquisition date, in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, and the District of Columbia. Covers all company systems and data (cloud, colocation, SaaS, ROCs, endpoints, and the OT edge), the company's administration of customer building systems through the IBOP, customer data the company holds, and systems that vendors and subcontractors operate for the company. GSA systems that company staff use under GSA's authorization are governed by GSA policy; this policy governs the company staff who use them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity and physical safety risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Director of OT Security | Accountable for OT security standards, the OT remote access gateway, and OT monitoring |
| Chief Privacy Officer | Privacy program; breach determinations |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Vice President, Government Contracts Compliance | FAR clause compliance, supplier screening, CUI program |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its contract or regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that covers IT and OT, meets its contract and legal requirements, and is documented in this policy hierarchy and in system security plans for tier-1 systems (the IBOP and the FSP). (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as program owner, the Director of OT Security as accountable for OT security, and the Chief Privacy Officer as accountable for privacy. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes, acquisitions, or new contract types, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Physical safety risks (ER-01) at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. An exception can never waive a customer contract term or a law. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No supplier or subcontractor may access company or customer systems or data until it has been tiered, reviewed, and bound by the security addendum with the FAR flow-downs and a 24-hour incident notice term. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, remote access, logging, and endpoint controls to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, and incident records, must be retained for at least 3 years from creation or last effective date, or longer where a contract or customer records schedule requires. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity and OT risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 Every segment and acquired business must screen telecommunications, video surveillance, and network equipment against FAR 52.204-25 and 52.204-23 and against FASCSA orders before ordering or installing it, and Government Contracts Compliance must check SAM.gov for FASCSA orders at least quarterly. (SR-3; SR-6; GV.SC-05)
4.14 Each customer's security terms (exhibits, addenda, CJIS, FERPA, CUI, notice clocks, retention schedules) must be recorded in the contract obligations register with a named owner before the contract starts. (PL-2; SA-9; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging and Monitoring Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 OT Remote Access and Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Personnel Security Standard
- STD-01.9 Secure Development Standard
- STD-01.10 Vulnerability and Patch Management Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Supplier Screening Procedure (Section 889, Kaspersky, FASCSA)
- PRC-01.5 Subcontractor Onboarding Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and customer audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor violations are handled under the subcontract and may end the subcontractor's access.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a physical safety risk (ER-01) at High or above are refused unless a dated treatment plan exists. An exception never waives a customer contract term or a law. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 IBOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the contract obligations register.
