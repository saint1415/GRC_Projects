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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, RA-3, CA-5, PS-8, SA-9, SR-6, SA-4, CA-2, CA-2(1), SI-12, AC-5, IA-12, SI-10, AU-10 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.OV-01, GV.RR-02, GV.RM-01, GV.RM-06, GV.RR-04, GV.SC-05, ID.IM-01, GV.OC-01, PR.AA-05 |
| Regulatory drivers | N23-R01 (52.204-21(b)(1)); N23-R03 (252.204-7012(b)(2)); N23-R04 (32 CFR 170.19, 170.21, 170.22, 170.23; 252.204-7021(f)); 252.204-7020(g)(2); FAR 52.232-27(c)(1); 17 CFR 229.106(b)-(c); SOX Section 404 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects project, payment, federal contract, employee, and client information, keeps money moving only to verified accounts, and supports the company's federal contract (FAR, DFARS, CMMC), SEC, SOX, and state law obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, craft workers, contractors, and interns) at headquarters (HQ-1), the nine regional offices, about 140 jobsites, the two yards, and the two colocation data centers in eight states, including acquired businesses (AQ-1 and AQ-2) from their acquisition date. Covers all company systems and data, including cloud, colocation, SaaS, the Federal Programs CUI Enclave (FPCE), jobsite technology, client building systems that BTS administers, systems that vendors and subcontractors operate for the company, and the services the company offers to external clients (SL-1 and SL-2). Subcontractor and design-team users of company systems are bound by the security terms in their subcontracts and access agreements.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Risk Officer | Enterprise risk management; owns the enterprise risk register |
| Chief Compliance Officer | Tracks legal, regulatory, and contract requirements (second line) |
| President, Federal Group | CMMC Affirming Official (32 CFR 170.22(a)(1)); business owner of the FPCE |
| Director, CMMC Program Office | Maintains the FPCE and enterprise FCI scopes, their SSPs, self-assessments, and SPRS records |
| Vice President, Treasury and Director of Payment Operations | Own payee verification and payment release (statement 4.13) |
| Chief Audit Executive | Independent assessment (third line); reports to the audit committee |
| All workforce | Follow policies, standards, and procedures; report incidents and suspicious payment requests |

Role overlaps are limited by design: Internal Audit (third line) never operates the controls it tests, and the people who maintain payees never release payments (POL-02 4.3).

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in the 2026 PDPP assessment (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, documented in this policy hierarchy, in system security plans for tier-1 systems, and in a system security plan for each CMMC assessment scope. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is the program owner. The President, Federal Group is the CMMC Affirming Official, and the Director, CMMC Program Office maintains the FPCE and enterprise FCI scopes and their SSPs. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Federal eligibility and safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. A deviation from a CMMC requirement that cannot be on a CMMC POA&M must be escalated to the Affirming Official. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor or subcontractor may receive FCI or CUI until the required flowdown terms are signed. For contracts with DFARS 252.204-7021, the subcontractor's CMMC status and affirmation, and for CUI its SPRS assessment, must be verified before award and annually. (SA-9; SR-6; SA-4; GV.SC-05)
4.9 Tier-1 systems and CMMC scopes must be assessed at least annually by an assessor independent of their operation. No CMMC affirmation or SPRS entry may be made without an evidence binder reviewed by counsel. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing, enterprise payee verification and SOC monitoring from day one, and an integration plan that brings identity, network, and logging to enterprise standards within 12 months. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, CMMC artifacts, and incident records, must be retained for at least 6 years from creation, last effective date, or the CMMC status date, whichever is later. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, CMMC status, and material incidents. (PM-9; GV.OV-01)
4.13 Every new payee and every change to payee bank details must be verified by Payment Operations through a call-back to a number on file and the bank account validation service, recorded in a structured record, and released by a different person. No business unit or acquired company may run its own payee change process. (AC-5; IA-12; SI-10; AU-10; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot weaken it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Subcontractor Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Acquisition Security Integration Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 CMMC Self-Assessment and Affirmation Procedure
- PRC-01.5 Payee and Bank Account Verification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, monthly payment-control exception reports, the annual Internal Audit assessment (P07), and the CMMC self-assessments (P03). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor and vendor violations are handled under their contracts and can lead to removal of access or the subcontract.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (SP 800-30 Tables G-5 and I-2), approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot make a CMMC requirement "met": a requirement that is not met is scored as not met in the self-assessment and SPRS, whatever the exception register says, and any such gap is escalated to the Affirming Official (statement 4.6). Requests that would leave a federal eligibility or safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 enterprise risk register; P02 PDPP SSP; P03 regulatory gap analysis (including the FPCE readiness check); P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; FPCE SSP (separate, CMMC Level 2).
