# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, new CJISSECPOL versions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-2, PS-3, PS-6, PS-8, RA-3, CA-2, CA-7, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| Agency requirements | CJIS Security Addendum sec. 3.01 and CJISSECPOL v6.1 PS-3, SA-9; Pub. 1075 sec. 2.C.3 and Exhibit 7; 42 CFR 431.306(b); 18 U.S.C. 2721-2722; Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of agency data and of the services agencies rely on, and keeps the company inside the contract terms that let it hold federal tax information (FTI), criminal justice information (CJI), benefits data, and motor vehicle records.

## 2. Scope
All workforce members (employees, contractors, and staffing firm personnel), wherever they work, in every business line: the Agency Case Management Cloud (ACMC), managed services for agency-hosted systems, delivery, and corporate functions. It covers all company systems and data, agency systems the company administers, systems vendors operate for the company, and any business the company acquires, from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; approves POL-02 to POL-05; accepts Moderate risks; chairs the crisis management team |
| Chief Technology Officer | ACMC system owner; approves the SSP |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Director of Information Security | Information Security Officer; runs the program day to day; security contact in agency contracts |
| Security Operations Manager and GRC Manager | Security operations, incident command, risk register, SSP, POA&M, assurance evidence |
| Director of Contracts and Compliance | Agency security terms, notices to agencies, vendor contracts, privacy |
| HR Director | Screening, designated positions, training records, sanctions with the Director of Contracts and Compliance |
| Business line leaders (VP of Engineering, Director of Cloud Operations, Director of Managed Services, VP of Customer Delivery, Director of Customer Support) | Apply the policies in their teams; approve access; own their procedures |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents within 1 hour |

## 4. Policy statements
4.1 The company must maintain an information security program that meets the NIST SP 800-53 Rev. 5 Moderate baseline for the ACMC, as every agency contract requires, and the stricter values of the CJIS Security Policy, IRS Publication 1075, and other agency terms where they apply. The program is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01)
4.2 The Director of Information Security is the designated Information Security Officer and the security contact named in agency contracts. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02)
4.3 A risk assessment must be performed at least annually using NIST SP 800-30 Rev. 1, and after major changes, including acquisitions, new states, and new CJISSECPOL versions. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. **No one may accept a risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or DPPA term**; it must be treated, or the regulated data or access removed. (PM-9; GV.RM-01)
4.5 **Screening before access.** Positions with access to CJI, FTI, or motor vehicle records are designated in the HR system. No one may be given that access until the required screening is complete (fingerprint-based record checks for CJI; Pub. 1075 background investigations for FTI), the CJIS Security Addendum certification or FTI penalty notice is signed, and the required training is complete (STD-10). (PS-2; PS-3; PS-6; GV.RR-04)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. Statement 4.4's prohibition cannot be excepted. (PL-1)
4.8 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm, from retraining to termination. Misuse of CJI, FTI, or motor vehicle records is reported to the affected agency, and HR and the Director of Contracts and Compliance document every sanction. (PS-8; GV.RR-04)
4.9 **Vendors.** No vendor may receive agency data or access to agency systems until it passes a review scaled to its tier and signs contract terms (security, breach notice, data use, return and deletion) under STD-03. A vendor may not receive FTI unless the agency has obtained IRS approval and the contract carries the Exhibit 7 terms; a vendor may not receive CJI without the CJIS Security Addendum. Purchasing must not issue a purchase order to such a vendor without that approval. (SA-9; GV.SC-05)
4.10 Tier 1 vendors must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07)
4.11 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress on SOC 2 and GovRAMP. Monthly metrics go to the COO. (CA-7; PM-9; GV.OV-01)
4.12 Security controls must be independently evaluated at least annually (P07) and after major changes. The assessor must not design or operate the controls it assesses. (CA-2)
4.13 Security records (policies, risk assessments, assessments, incident records, and logs that support them) must be retained for at least 7 years. (SI-12)
4.14 **AI.** AI features the company builds for agencies, and AI tools staff use, must be approved through the AI governance process before use (STD-05; P10). No AI output may replace a decision that law gives to agency staff. (PM-9; GV.RM-01)
4.15 **New states and acquisitions.** Before the company contracts with an agency in a new state, counsel maps that state's security, breach, and AI requirements into the notification matrix and the SSP. An acquired business may not connect to company systems or handle agency data until a security assessment is complete. (RA-3; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (4.8). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow statement 4.7. They must be written, risk-rated, approved by the right authority under 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); CJIS Security Policy v6.1 and the CJIS Security Addendum; IRS Publication 1075; Fla. Stat. 501.171
