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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or CMMC scope changes |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| SP 800-171, CMMC, and other drivers | SP 800-171 Rev. 2 3.11.1, 3.12.1 to 3.12.4; DFARS 252.204-7012(b), (m); 252.204-7021(d)(3), (f); 32 CFR 170.22 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, and Government information, and supports the company's DFARS, CMMC, export control, NISPOM, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 8 sites in Florida, Georgia, Alabama, Texas, Kansas, and Arizona and at the 2 data centers, including acquired operations from their acquisition date. Covers all company systems and data, including the government-community and commercial clouds, SaaS, plant OT, and systems that suppliers and service providers operate for the company, with added rules for the CUI Engineering Enclave (CEE) and the Manufacturing Operations Zone (MOZ). The classified information system at FL-1 also follows NISPOM and DCSA requirements, which prevail where stricter.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and technology committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | CMMC Affirming Official; authorizing official equivalent for the CEE |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director, CMMC Program Office | SSPs, CMMC scope, SPRS entries, supplier CMMC verification |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets NIST SP 800-171 Rev. 2 for every system that holds CUI and the other requirements in P03, documented in this policy hierarchy and in system security plans for every CMMC scope. (PM-1; PL-2; GV.PO-01)
4.2 The Chief Operating Officer is the CMMC Affirming Official. No affirmation may be submitted in SPRS until Internal Audit and the General Counsel have reviewed the evidence that every applicable requirement is MET for the scope being affirmed. (PM-2; CA-7; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes, acquisitions, or new sites, using NIST SP 800-30 Rev. 1 and threat intelligence, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1. A known failure to meet a DFARS 252.204-7012 duty, processing CUI for a contract on a system without the required CMMC status, or an unauthorized export must never be accepted. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No supplier may receive CUI until its purchase order carries the DFARS 252.204-7012 and, where required, 252.204-7021 clauses, and the CMMC Program Office has confirmed in SPRS that the supplier holds the CMMC status its subcontract needs. (SA-9; SR-6; SR-3; GV.SC-05)
4.9 Security controls for every CMMC scope and every common control provider must be assessed at least annually by an assessor independent of their operation, and a POA&M must track every weakness to closure. (CA-2; CA-5; ID.IM-01)
4.10 No new site, acquisition, production line, or system may store, process, or transmit CUI until the CMMC Program Office approves the scope change and updates the SSP, and contracts that include DFARS 252.204-7021 may be performed only on systems covered by the required CMMC status. (RA-3; PL-2; CM-4; GV.OC-03)
4.11 Security documentation, including SSPs, assessments, POA&Ms, affirmation evidence, and incident records, must be retained for at least 6 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the risk and technology committee at least quarterly, including CMMC status and affirmation readiness, Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 CMMC Scope Management Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 CMMC Affirmation Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC readiness checks before each affirmation. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Vice President, Trade Compliance for a voluntary disclosure decision.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception never removes a DFARS 252.204-7012 duty, never permits CUI on a system without the required CMMC status, never permits an unauthorized export, and never covers a requirement that cannot be on a CMMC POA&M (32 CFR 170.21(a)(2)(iii)). Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CEE SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
