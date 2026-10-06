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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new CJISSECPOL versions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, RA-7, CA-2, CA-5, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.OV-01, GV.RM-01, GV.RM-06, GV.SC-05 |
| Key requirements | CJIS Security Addendum sec. 3.01; Pub. 1075 Exhibit 7 and sec. 3.3.1; 45 CFR 164.308(a)(1)-(2), 164.316 (AG-04 scope); 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects agency data and the company's own information, and supports the contract duties (SP 800-53 Moderate, CJIS, Pub. 1075, business associate terms), the direct duties (DPPA, Florida and other state law, federal clauses), and SEC disclosure duties.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor staff) in every state and delivery center, including AQ-1 staff from the acquisition date. Covers all company systems, the hosted agency environments (ACMC, IES, legacy hosting, AQ-1), the CUI enclave, and all agency data the company receives, wherever it is stored or processed.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of Regulated Data Compliance | CJIS and Pub. 1075 program; HIPAA security official for the AG-04 business associate scope |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets the SP 800-53 Moderate baseline required by agency contracts and the CJIS, Pub. 1075, and business associate overlays, documented in this hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as program owner, and the Director of Regulated Data Compliance as the CJIS and Pub. 1075 program lead and the HIPAA security official for the AG-04 business associate scope. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes, acquisitions, or new CJISSECPOL versions, using NIST SP 800-30 Rev. 1, and rolled into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the levels in STD-01.1: risk owner (Low), CISO with the segment president (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). No risk that breaches a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term may be accepted. (PM-9; RA-7; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and sanctions involving CJI or FTI must be reported to the affected agency. (PS-8; GV.RR-04)
4.8 No vendor or subcontractor may receive agency data until it has been tiered and assessed under STD-01.3 and its contract carries the required flowdowns (CJIS Security Addendum; Pub. 1075 Exhibit 7 with the agency's IRS notification; business associate terms; DPPA terms; FAR and DFARS clauses). Tier-1 suppliers must be reviewed annually. (SA-9; SR-6; PS-7; GV.SC-05)
4.9 Tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation (Internal Audit, a co-sourced firm, or a third-party assessor). (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and a funded integration plan. Acquired environments may not reach company or agency systems until identity, MFA, logging, and screening meet company standards. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk assessments, assessments, incident records, and audit logs of FTI systems, must be retained for at least 7 years. (SI-12; AU-11; GV.PO-02)
4.12 The CISO must report cyber risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 All work on agency data, including support and administration, must be performed in the United States by staff and vendors located in the United States. (SA-9(5); SA-9; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Subcontractor Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Regulated Data Contract Flowdown Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and agency audits (CJIS audits, IRS safeguard reviews). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. **No exception may be granted against a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term, or a statute**; those gaps are fixed, or the regulated data or access is removed until they are. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ACMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; agency contracts; CJIS Security Policy v6.1; IRS Publication 1075.
