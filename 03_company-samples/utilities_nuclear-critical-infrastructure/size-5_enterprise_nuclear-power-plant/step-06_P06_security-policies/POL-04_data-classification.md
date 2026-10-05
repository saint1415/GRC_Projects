# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Compliance Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-10, within the 15 calendar months CIP-003-9 R1 allows), and after major changes, incidents, acquisitions, or a final NRC rule |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-4, MP-6, SC-7, SC-8, SC-28, CP-9, AC-3, AC-21, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | 10 CFR 73.21-73.22; 73.56(m); 26.37; Part 810 (810.2); 20.2106; state data security laws (Fla. Stat. 501.171(2) and (8) worked example) |

## 1. Purpose
Classify company information and set handling rules that match the law and the harm of disclosure. Safeguards Information, security-related information about the stations, export-controlled reactor technology, access authorization and fitness-for-duty information, and dose records each carry specific legal handling rules.

## 2. Scope
All Cris Santos Company workforce members (about 12,000 employees, the supplemental contractors who support refueling outages, and other contractors and vendors with company accounts) at the corporate campus in Florida, the four stations (Florida, Georgia, South Carolina, and Alabama), the Generation Dispatch Center, and the data centers DC-1 and DC-2. Covers all business systems and data, including the two public clouds, SaaS, the plant business networks, Station 4 legacy systems from the 2025-07-01 acquisition date, and the services sold to outside companies (SL-1 monitoring and diagnostics; SL-2 dosimetry processing). **Critical digital assets (CDAs) are governed by each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54.** This policy supports the CSPs and never overrides them; where a CSP or a NERC CIP requirement is stricter, the stricter rule applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Policy owner; data classification scheme |
| Director, Nuclear Security | SGI program and access authorization information |
| Director, Nuclear Cyber Security | Security-related information about CSPs, CDAs, and networks |
| Export Compliance Officer | Part 810 and Part 110 technology controls |
| Director, Dosimetry Laboratory | Dose records for the fleet and SL-2 clients |
| Data owners | Classify and approve access to their data |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Public, Internal, Confidential, or Restricted. Restricted includes SGI, security-related information (cyber security plans, CDA inventories, network diagrams), BES Cyber System Information and CEII, export-controlled technology, access authorization and FFD data, Social Security numbers, and dose records. (RA-2; ID.AM-07)

4.2 Confidential and Restricted information must be encrypted at rest and in transit with FIPS-validated cryptography. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.3 SGI must be processed only on stand-alone SGI computers and stored in locked security containers. SGI must never be placed in email, the WMS, cloud or SaaS systems, or AI tools, and networked copiers are prohibited in SGI areas. (SC-7; MP-4; PR.DS-01)

4.4 Printed Confidential and Restricted information must be marked and kept in controlled areas. (MP-3; MP-4; PR.DS-01)

4.5 Export-controlled technology must be marked, stored only in locations tagged for it, and shared outside the company only through the controlled transfer workflow. (AC-21; AC-3; PR.DS-01)

4.6 Backups of Confidential and Restricted information must be immutable and separate from production, and restores must be tested at least annually, including dose records. (CP-9; PR.DS-11)

4.7 Media must be sanitized under NIST SP 800-88 before reuse or disposal. Systems used for SGI must be free of recoverable SGI before reuse, with a record. (MP-6; PR.DS-01)

4.8 Confidential or Restricted information must not be entered into AI tools without AI governance committee approval and contract terms that forbid training on company data. (SA-9; PR.DS-01)

4.9 Access authorization and fitness-for-duty information must stay in SYS-10. Exports are prohibited except registered restricted reports (PRC-04.1). (AC-3; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it, the CSPs, or a NERC CIP requirement.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Security-Related Information Handling Standard
- PRC-04.1 Restricted Report and Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certification, the annual Internal Audit assessment (P07), Nuclear Oversight reviews of the security program (73.55(m)), NRC cyber security inspections, and NERC Regional Entity audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract. A violation by a person with unescorted access is also reported to the access authorization program, which decides whether it affects trustworthiness and reliability under 10 CFR 73.56.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may waive a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 WMS-PBN SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; station cyber security plans and implementing procedures (controlled documents, not attached).
