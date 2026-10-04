# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, SC-7, SC-8, SC-28, SI-3, SI-4, CP-9, MP-6, SI-12, PT-2 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, DE.CM-09 |
| Key regulatory drivers | DFARS 252.204-7012(b); DFARS 252.204-7021(d)(2); FAR 52.204-21; Cal. Civ. Code 1798.150; Fla. Stat. 501.171 |

## 1. Purpose
Classify company, customer, and federal information and set handling rules for each class, so that CUI stays in the FSCE, FCI stays in systems covered by the Level 1 scope, and personal information is protected under privacy and breach laws.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary workers supplied by staffing agencies, contractors, and interns) at headquarters, the 6 distribution centers, the 15 sales offices, and remote locations, including AQ-1 and any future acquisition from its closing date. Covers all systems and data, including cloud, colocation, SaaS, distribution-center OT, the FSCE, and systems that vendors, carriers, 3PLs, and drop-ship partners operate for the company, and the services offered to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns this policy and the privacy program |
| Director, CMMC Program Office | CUI handling rules and the CUI spill procedure |
| Data owners | Classify data and approve access |
| All workforce | Handle data by its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Public, Internal, Confidential (pricing, contracts, personal information, FCI), or Restricted (CUI), and labeled where the system supports it. (RA-2; ID.AM-05)
4.2 CUI may be processed, stored, or transmitted only in the FSCE. CUI that arrives anywhere else, including by customer upload, email, or EDI, is a spill and must be handled under PRC-04.2. (AC-4; SC-7; PR.DS-01)
4.3 FCI may be processed only in systems inside the enterprise Level 1 scope and shared only with vendors whose contracts include FAR 52.204-21 safeguarding terms. (SA-9; AC-3; PR.DS-01)
4.4 Confidential and Restricted data must be encrypted at rest and in transit using STD-04.1; CUI must use FIPS-validated cryptography. (SC-8; SC-28; PR.DS-01)
4.5 Files uploaded by customers and partners must be scanned for malware and, on the reseller platform, for CUI markings before they are stored. (SI-3; SI-4; DE.CM-09)
4.6 Backups of tier-1 data must be immutable, kept in separate backup accounts, and restore-tested at least quarterly. (CP-9; PR.DS-11)
4.7 Media and devices must be sanitized or destroyed with a certificate before reuse, resale, or disposal. (MP-6; PR.DS-01)
4.8 Confidential data may be used in AI tools only if the tool is on the approved list for that class (STD-05.3); Restricted data (CUI) must never be entered in any AI tool outside the FSCE. (AC-20; SA-9; PR.DS-10)
4.9 Data must be kept no longer than the retention schedule allows, and personal information of license registrants must be minimized after 3 years. (SI-12; PR.DS-01)
4.10 Personal information must be handled in line with privacy notices and consumer rights requests under the CCPA and other state laws. (PT-2; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 CUI and FCI Handling Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 CUI Spill Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC Program Office's internal assessments for the FSCE. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCFP SSP; FSCE CMMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
