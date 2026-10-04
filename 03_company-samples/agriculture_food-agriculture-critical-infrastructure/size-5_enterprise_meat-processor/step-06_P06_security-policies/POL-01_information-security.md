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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CM-3, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05, PR.PS-01 |
| Regulatory drivers | 21 CFR 121.4(d), 121.157; 9 CFR 417.4(a)(3); 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, and employee information, and the integrity of the processes that make food safe, and supports the company's FSIS, FDA, EPA reporting, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, agency temporary workers, contractors, and interns) at the 8 plants, 4 distribution centers, headquarters, and regional offices in Florida, Georgia, Alabama, North Carolina, Tennessee, and Texas, including acquired operations from their acquisition date. Covers all IT and OT systems and data, including plant control systems, refrigeration controls, cloud, colocation, SaaS, and systems vendors operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Director of OT Security | Leads OT security under the CISO |
| Senior Vice President, Food Safety and Quality Assurance | Enterprise Food Defense Coordinator; decides product holds and FSIS and FDA notices |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that covers IT and OT, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The Director of OT Security must lead OT security under the CISO. The SVP FSQA must be designated in writing as the enterprise Food Defense Coordinator, and the PLT-07 FSQA Manager as the person responsible for Part 121 compliance at PLT-07. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1. It must include scenarios in which process controls are used to adulterate food, disrupt CCPs, or upset ammonia systems, and it must be rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Food safety and worker safety risks at High or above must not be accepted; they must be treated with a dated plan. (PM-9; GV.RM-06)
4.5 Security and food defense work together. The SVP FSQA must receive the risk register each year and after each update, and for PLT-07 must record whether new information requires a food defense reanalysis. (RA-3; ID.RA-01)
4.6 OT change control. No change to a PLC program, HMI, recipe or setpoint range, smokehouse or oven cycle, MES release service, or OT network may go live without a recorded request, a test, engineering approval, and plant FSQA sign-off for any change that touches a CCP. Any change that could affect PLT-07's plant-based process must also be screened for a food defense reanalysis before it goes live. (CM-3; CM-4; PR.PS-01)
4.7 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.8 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.9 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm. Intentional tampering with process controls, formulations, or food safety records is grounds for termination and referral to law enforcement. (PS-8; GV.RR-04)
4.10 No vendor may receive OT remote access or Restricted data until it accepts the company's security terms (named accounts, MFA, approved sessions, incident notice) and has been tiered and assessed under STD-01.3. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.11 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.12 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, OT boundary, logging, and record systems to enterprise standards within 18 months of closing. (RA-3; SA-9; GV.OC-01)
4.13 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 3 years. Food safety and food defense records follow POL-04. (SI-12; GV.PO-02)
4.14 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard (IT and OT)
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard (plant reference architecture)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 OT Change Procedure (with FSQA sign-off and food defense screen)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, OT monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.9), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls and a linked POA&M item, and limited to 12 months. Requests that would leave a food safety or worker safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPCM SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the PLT-07 food defense plan and the plant HACCP plans.
