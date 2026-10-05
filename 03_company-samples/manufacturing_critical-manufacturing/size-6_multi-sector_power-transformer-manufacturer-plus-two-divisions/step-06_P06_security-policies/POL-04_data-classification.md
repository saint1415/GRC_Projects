# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Version | v2026.1 |
| Owner | Group CISO, with the Group Chief Privacy Officer for personal information |
| Approved by | Group CISO, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-21, CM-8, SC-8, SC-12, SC-28, SI-7, CP-9, MP-6, SI-12, SA-9, PL-4 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.RA-09, ID.AM-08 |
| Regulatory and contract drivers | N22-R01 CIP-011-3 and CIP-004-7 R6 (BCSI); client CIP-011-3 terms; 18 CFR 388.113 (CEII); N54-R04 FAR 52.204-21 (FCI); C-CRITICAL-MFG-R03 EAR (15 CFR 762.6); utility addendum sec. 5 (integrity of supplied firmware); state breach laws (Fla. Stat. 501.171 worked example) |
| Division supplements | Manufacturing: designs, test data, firmware, customer NDA drawings. Electric Utility: BCSI repository and customer personal information. Grid Engineering: client BCSI and CEII on the project platform |

## 1. Purpose
Classify group information by sensitivity and by whose information it is, and set handling rules so that grid-sensitive information, customer information, and the integrity of what the group ships are protected.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including information that customers and clients entrust to the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information owners | Classify and label information; approve sharing |
| Group CISO | Sets handling standards and encryption and key standards |
| Group Chief Privacy Officer | Owns personal information rules and breach determinations |
| Electric Utility NERC compliance director | Owns the BCSI program (CIP-011-3) and BCSI access authorization (CIP-004-7 R6) |
| Grid Engineering project platform director | Enforces client handling terms on the project platform |
| Chief product security officer | Owns firmware integrity and signing keys |

## 4. Policy statements
4.1 Information must be classified as:
- **Restricted:** BES Cyber System Information (BCSI), CEII, customer and employee Social Security numbers and bank account numbers, credentials, and cryptographic and signing keys;
- **Confidential:** transformer designs and calculations, customer specifications and NDA drawings, test data, federal contract information (FCI), and other personal information;
- **Internal**; or **Public**. (RA-2; ID.AM-07)

4.2 Restricted and Confidential information must be encrypted at rest and in transit with approved algorithms and group-managed keys. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.3 **BCSI.** The Electric Utility's BCSI may be stored only in locations its CIP-011-3 program designates, and access must be authorized through its CIP-004-7 R6 process. Group and affiliate platforms are not designated locations unless the utility designates them in writing. Client BCSI held by Grid Engineering must sit in restricted folders whose members the client has authorized. (AC-3; AC-21; PR.DS-10)

4.4 **CEII.** Grid Engineering may request CEII from FERC about a client facility only with the client's written authorization or under a FERC non-disclosure agreement (18 CFR 388.113). CEII must be handled as Restricted information and as the client contract requires. (AC-21)

4.5 **FCI** must be labeled and access limited to the staff on the contract team. (AC-3; N54-R04 FAR 52.204-21(b)(1)(i))

4.6 **Export records.** Export screening results and export records must be kept for at least 5 years (15 CFR 762.6(a)); the group keeps them 7 years in the GEPS. Technology for an export must be checked by trade compliance before release. (SI-12)

4.7 **Product and deliverable integrity.** Firmware, software, and patches the group supplies must be signed, and published with hashes. Signing keys must be held in a hardware security module under split control. Protection settings and configuration files delivered to clients must carry a hash that field staff check before deployment. (SC-12; SI-7; ID.RA-09)

4.8 **Backups.** Backups of Restricted and Confidential information and of High-criticality systems must be immutable, held with a different provider or account from production, and restore-tested at least quarterly. Plant controller programs and MES data must be backed up after every change and at least weekly, to the group vault. (CP-9; PR.DS-11)

4.9 Media holding Restricted or Confidential information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08)

4.10 Information must be kept per the group retention schedule. Customer and client information must be returned or destroyed at contract end as the contract requires, with a certificate. (SI-12)

4.11 Restricted or Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and its terms prohibit training on group or customer data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-3, SC-12, SI-7, CP-9), platform permission reports, and the Electric Utility's CIP-011-3 reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. BCSI exceptions also need the CIP Senior Manager's approval.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; Electric Utility CIP-011-3 information protection program; Manufacturing firmware release procedure; Group AI Standard (P10).
