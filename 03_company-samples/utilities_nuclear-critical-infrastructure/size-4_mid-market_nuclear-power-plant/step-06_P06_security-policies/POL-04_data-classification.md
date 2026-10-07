# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Security |
| Approved by | Site Vice President |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2022 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-4, MP-6, SC-7, AC-3, MP-2, SC-8, SC-28, CP-9, SI-12, MP-7, AC-19, AC-2 |
| CSF 2.0 | ID.AM-05, PR.AA-05, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01 |
| Regulatory drivers | C-NUCLEAR-S01, C-NUCLEAR-S02, C-NUCLEAR-S04, C-NUCLEAR-R01, C-NUCLEAR-R04, C-NUCLEAR-S06 |
| Supporting standards | STD-08 Encryption and key management; STD-10 Security-Related Information handling (see `standards-index.md`) |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so that Safeguards Information stays in the SGI program, Security-Related Information stays in restricted locations, and personal information is protected.

## 2. Scope
All company information in any form, on any system or vendor service, created or received by the workforce.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security | Owns this policy and the SGI program; designates SGI and SRI determining individuals |
| Information owners | Classify information in their area |
| IT Director | Technical controls (encryption, labels, DLP, backups) |
| All workforce | Mark and handle information by its class |

## 4. Policy statements
4.1 **Classes.** (1) **Safeguards Information** (10 CFR 73.21-73.22): handled only under the SGI program, never on the business network or in the cloud. (2) **Restricted:** Security-Related Information (the CSP, CDA inventory, assessments, defensive architecture drawings, security CAP entries), access authorization files, and other sensitive personal information. (3) **Confidential:** business and contract data, PPA settlement data, engineering data. (4) **Internal.** (5) **Public.** (RA-2; ID.AM-05; C-NUCLEAR-S01 (73.21; 73.22))
4.2 SGI may be processed only on the stand-alone SGI computers or other NRC-approved systems, stored in locked security containers, marked on the top and bottom of each page, and destroyed so it cannot be reconstructed. Devices must be free of recoverable SGI before reuse, with a second verifier. (MP-4; MP-6; SC-7; PR.DS-01; C-NUCLEAR-S01 (73.22(c), (d), (g), (i)))
4.3 Restricted information is stored only in EDMS restricted folders or the access authorization enclave, carries a sensitivity label, and is protected by DLP that blocks external sharing. It may not be placed in general shares, email to external parties, the cloud workloads account, or any AI tool. (AC-3; MP-2; PR.DS-01; C-NUCLEAR-S01; C-NUCLEAR-S02 (73.56(m)))
4.4 Restricted and Confidential data must be encrypted in transit (TLS 1.2 or higher) and at rest. (SC-8; SC-28; PR.DS-01; PR.DS-02; C-NUCLEAR-S04 (501.171(2)))
4.5 Business systems must be backed up daily to the recovery account with write-once retention, and CSP-supporting records copied monthly to long-term retention. (CP-9; SI-12; PR.DS-11; C-NUCLEAR-R01 (73.54(h)))
4.6 Portable media and mobile devices are assigned to one security level. Business (Level 2) devices must be labeled and may never be used at Level 3 or 4; media for CDAs must pass the PMMD kiosk. (MP-7; AC-19; PR.PS-01; C-NUCLEAR-R01 (RG 5.71 B.1.19); C-NUCLEAR-R04 (CIP-003-9 Att. 1 Sec. 5))
4.7 Media are sanitized or destroyed before disposal or reuse, with certificates. (MP-6; PR.DS-01; C-NUCLEAR-S06)
4.8 Restricted-folder access is reviewed each quarter, and general shares are searched quarterly for misplaced Restricted documents. (AC-3; AC-2; PR.AA-05; C-NUCLEAR-S01)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the metrics reported to the audit committee, and, for anything in 73.54 scope, the 73.55(m) program review. Violations are handled under POL-01 4.13.

## 6. Exceptions
Exceptions follow POL-01 4.8: written, risk-rated, approved by the right authority under POL-01 4.5, recorded in the risk register, and limited to 12 months. No exception may permit a known regulatory noncompliance.

## 7. Related documents
POL-01; POL-05; STD-08 Encryption and key management standard; STD-10 Security-Related Information handling standard; SGI program procedures
