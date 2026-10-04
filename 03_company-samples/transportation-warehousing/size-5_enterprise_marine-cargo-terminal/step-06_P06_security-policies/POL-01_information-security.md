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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions or Cybersecurity Plan amendments |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, SA-9, SR-8, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| 33 CFR Part 101 Subpart F | 101.620; 101.625; 101.630; 101.640; 101.650(e)(1), (f); 101.655 |

## 1. Purpose
Establish the enterprise information security program across IT and OT, assign accountability from the board to every worker, designate the Cybersecurity Officer required by 33 CFR Part 101 Subpart F, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the safety of terminal operations and the confidentiality, integrity and availability of company, customer and port partner information, and supports the company's Subpart F, MTSA, SEC and state law obligations.

## 2. Scope
All Cris Santos Company employees, contractors, temporary staff and interns at headquarters, the enterprise planning center and the 8 terminals (T-01 to T-08) in Florida, Georgia, South Carolina and Texas, including acquired terminals from their acquisition date. Longshore workers ordered through the hiring halls and OEM and vendor technicians are covered when they use company IT or OT, through the hiring hall arrangements and their contracts. Covers all IT and OT systems and data, including cloud, colocation, SaaS, cranes and automation, gate systems, and the services the company provides to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of Maritime Cybersecurity | Cybersecurity Officer (CySO) for all 8 facilities; owns the Cybersecurity Assessment and the Cybersecurity Plans |
| Terminal OT Security Leads | Alternate CySOs for their terminals |
| Vice President, Maritime Security and the FSOs | FSPs, TWIC access control, MTSA reporting, drills |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment and Cybersecurity Plan audits (third line) |
| All workers | Follow policies, standards and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that covers IT and OT and meets 33 CFR Part 101 Subpart F and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The owner must designate in writing, by name and title, a Cybersecurity Officer for every facility who is reachable by the Coast Guard 24 hours a day, 7 days a week, and an alternate at each terminal. Once a Plan is approved, a change of CySO must be notified to the Coast Guard within 96 hours. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, rolled up into the enterprise risk register following NIST IR 8286 Rev. 1, and used as input to the annual Cybersecurity Assessment. (RA-3; PM-9; GV.RM-01)
4.4 Risk must be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Safety risks at High or above must not be accepted without a dated treatment plan, and an accepted Subpart F gap must be recorded as an unresolved vulnerability in Section 12 of the Cybersecurity Plan. (PM-9; RA-7; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workers who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No IT or OT vendor, OEM or service provider may receive network, OT or data access until it has been tiered and assessed under STD-01.3 and its contract requires notice of cybersecurity vulnerabilities and reportable cyber incidents without delay. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-8; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and Cybersecurity Plan audits must be performed by people with no regularly assigned cybersecurity duties at the facility. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing, a funded integration plan that brings identity, network, logging, endpoint and OT controls to enterprise standards within 12 months of closing, and a Cybersecurity Assessment of each acquired facility. (RA-3; SA-9; GV.OC-01)
4.11 Records required by Subpart F and 33 CFR 105.225 (training, drills, exercises, cyber threats, reportable cyber incidents, Plan audits) must be kept at least 2 years, protected against unauthorized deletion or amendment, and longer where the records schedule requires. (SI-12; AU-11; GV.PO-02)
4.12 The CISO and the CySO must report cybersecurity risk and Subpart F status to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance and material incidents. (PM-9; GV.OV-01)
4.13 Every facility must have a Coast Guard-approved Cybersecurity Plan. Facilities of similar operations may share one Plan only if it contains a facility-specific annex for each, and Plans must be submitted no later than 2027-07-16. (PL-2; GV.PO-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard (zones, approved list, device credentials, KEVs)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Cybersecurity Plan Maintenance and Amendment Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications and, once the Cybersecurity Plans are approved, the annual Plan audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a safety risk at High or above are refused unless a dated treatment plan exists. An exception to a Subpart F measure must also be documented in the Cybersecurity Plan as a compensating control or an unresolved vulnerability, or handled through a waiver, equivalence or temporary deviation notice under 33 CFR 101.665. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 6.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ETOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the Cybersecurity Plans and FSPs (SSI).
