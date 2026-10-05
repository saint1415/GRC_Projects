# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, new CUI contracts, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, AC-5, SA-4, SA-9, SR-2, SR-5, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, PR.AA-05 |
| Federal contract requirements | FAR 52.204-21 (N23-R01); FAR 52.204-25 (N23-R02); DFARS 252.204-7012, 7019, 7020 (N23-R03); 32 CFR Part 170 and DFARS 252.204-7021 (N23-R04) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects:
- controlled unclassified information (CUI) and Federal Contract Information (FCI);
- payment instructions and bank details for owners, subcontractors, suppliers, employees, and the company's own SAM record;
- employee personal information;
- client facility security details (installed system layouts and credentials);
- bid and pricing data.

## 2. Scope
All workforce members (employees, temporary staff, interns, and contractors with company accounts) at headquarters, the regional office, the equipment yard and prefabrication shop, the MBSS monitoring room, and every jobsite. It covers all company systems and data, including systems that vendors operate for the company, the CUI Project Enclave, and any business the company acquires from the date it connects to company systems. Subcontractors are bound through their subcontracts (statement 4.12).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, CMMC readiness, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks; **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Operating Officer | Executive sponsor and PDPP system owner; approves POL-02 to POL-05 and the standards; accepts Moderate risks |
| Chief Financial Officer | Owns payment controls and the ERP; approves changes to the company's SAM EFT data |
| General Counsel | Reviews federal representations (SPRS, SAM, CMMC) and breach decisions |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Security Manager, security analysts, GRC analyst | Run the program day to day; own the SSP, POA&M, risk register, and SPRS score calculation |
| IT Director | Infrastructure, cloud, networks, endpoints, and recovery |
| Director of Contracts and Compliance | Flowdowns, SAM, SPRS submissions, Section 889 and DIBNet reports |
| FC-4 Project Executive | CUI custodian for FC-4 |
| Co-sourced internal audit firm | Independent annual assessment (P07) and reperformance of every SPRS score |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that meets FAR 52.204-21 on every system that holds FCI and NIST SP 800-171 Rev. 2 on every covered contractor information system that holds CUI, documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; DFARS 252.204-7012(b)(2)(i))
4.2 The Security Manager is the designated security program lead, and the CEO is the designated CMMC Affirming Official. Both designations must be in writing and reaffirmed each year. (PM-2; GV.RR-02; 32 CFR 170.22)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions and new CUI contracts), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. A risk that would make a federal representation or affirmation inaccurate may not be accepted; it must be fixed or disclosed. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, CMMC readiness, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. No exception may be granted against an SP 800-171 requirement for the CPE or a FAR 52.204-21 requirement while the company holds or seeks a CMMC status. (PL-1)
4.8 **Payment instruction changes.** Any new or changed bank details must be verified before use. This covers subcontractors, suppliers, owners, employees, and the company's own EFT information in SAM. Verification means all of these steps:
- a phone call to a number already on file (never a number or link in the requesting message), recorded with the date, the number called, and the person reached;
- approval by a second authorized person who did not enter the change;
- a record in the vendor master change log.

Urgency, seniority, or a project deadline is never a reason to skip a step, and no system may allow an override. The first payment to a changed account above $50,000 is held for 10 business days unless the Controller confirms the change in a second call. Changes to the company's SAM EFT data also need CFO approval. (AC-5; PR.AA-05)
4.9 **Remittance changes to owners.** The company never changes its own remittance instructions by email alone. Every prime contract and every pay app cover sheet must say so and give a verified phone number for confirmation. (AC-5; PR.AA-05)
4.10 **Third parties.** Before any vendor or external system holds CUI, FCI, Restricted data, or client facility security details, it must be on the approved external systems list (POL-04 4.4), pass a security review scaled to its tier (STD-03), and have contract terms covering confidentiality, incident notice, and no use of company data to train models. A cloud service that will hold CUI must be FedRAMP authorized at Moderate or higher, or proven equivalent, and must accept the reporting duties in DFARS 252.204-7012(c) to (g). (SA-9; GV.SC-05; DFARS 252.204-7012(b)(2)(ii)(D))
4.11 Tier 1 vendors (those holding CUI, FCI at scale, payment data, or client security details, or supporting a High-criticality process) must be reassessed each year, including a review of their SOC 2 report, FedRAMP package, or equivalent (STD-03; P09). (SR-6; GV.SC-07)
4.12 **Subcontract flowdown.** Subcontracts under federal prime contracts must include the substance of FAR 52.204-21 (when the subcontractor may hold FCI) and FAR 52.204-25. Subcontracts that involve covered defense information must include DFARS 252.204-7012 without alteration, and no subcontract subject to SP 800-171 may be awarded until the subcontractor's current SPRS assessment is verified (DFARS 252.204-7020(g)(2)). Once a prime contract includes DFARS 252.204-7021, subcontracts must flow down the CMMC level required by 32 CFR 170.23, and the subcontractor's current status and affirmation must be confirmed before award. No CUI may be released to a subcontractor until these steps are complete. (SA-4; SR-6; GV.SC-05)
4.13 **Section 889.** The company must not provide, install, rent, or use any equipment or service from an entity named in FAR 52.204-25, or its subsidiaries or affiliates, on any project or in company operations. Every submittal, purchase, rental, and lease of video surveillance, telecommunications, or networking equipment must confirm the actual manufacturer in writing. Identified covered equipment must be reported under POL-03 4.8. (SR-2; SR-5; GV.SC-05)
4.14 **Federal representations.** SPRS scores, SAM representations, and CMMC affirmations may be submitted only after the GRC analyst prepares an evidence binder, the co-sourced internal audit firm reperforms the score or reviews the evidence, and General Counsel reviews it. CMMC affirmations are made only by the CEO. (CA-2; GV.OV-01)
4.15 Security controls must be independently assessed at least annually (P07) and after major changes. The SP 800-171 self-assessment of the CPE must be repeated at least annually using the SP 800-171A objectives. (CA-2; DFARS 252.204-7019(b))
4.16 Security policies, risk assessments, assessments, POA&Ms, SPRS evidence, and incident records must be retained for at least 6 years. Certified payroll records must be retained for 3 years after the work is completed (FAR 52.222-8(a)). (SI-12; GV.PO-02)
4.17 AI tools must be approved through the AI review process before use (STD-05; P10). No AI tool may receive CUI or change payment data. (PM-9; GV.RM-01)
4.18 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Violations are handled under section 4.18. Compliance is checked through the annual independent assessment (P07), the SP 800-171 self-assessment, quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Gap Analysis (P03); FAR 52.204-21; FAR 52.204-25; DFARS 252.204-7012, 7019, 7020, 7021; 32 CFR Part 170
