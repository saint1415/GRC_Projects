# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crop Farming, Food Processing, Farm Supply) and corporate shared services |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-28, SC-8, CM-12, PM-5(1), AC-3, AC-6, SI-12, CP-9, AU-9, SI-7, AU-10, PT-2, PT-3, MP-6, AC-20, PL-4 |
| CSF 2.0 | ID.AM-05, PR.DS-01, ID.AM-07, PR.AA-05, PR.DS-11, GV.OC-03 |
| Division supplements | Food Processing: food defense plan handling; Farm Supply: grower credit files and portal data use |

## 1. Purpose
Classify group information so each type gets the right protection, keep records the law requires for as long as it requires, and keep personal and customer data only where it belongs.

## 2. Scope
All information the group creates, receives, or holds in any form, in IT, OT, SaaS, and paper.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classification, the data map, and retention |
| Data owners | Classify data sets and approve access and transfers |
| Records owners (food safety, labor compliance, quality) | Own regulated records and their retention |
| All workforce | Handle data according to its label |

## 4. Policy statements
4.1 Four levels: Public; Internal; Confidential (yields, prices, grower agronomic data, food defense plans, OT designs); Restricted (Social Security, passport, visa, and bank account numbers, card data, credit files, credentials). (RA-2; ID.AM-05)

4.2 Restricted data must be encrypted at rest and in transit, kept only in approved systems of record, and never copied to staging areas, file shares, or data hubs without a data owner approval recorded in the data map. (SC-28; SC-8; CM-12; PR.DS-01)

4.3 The data map must be reviewed each quarter, and stray copies of Restricted data found must be purged and reported as a policy exception. (CM-12; PM-5(1); ID.AM-07)

4.4 **Food defense plans and OT designs** are Confidential and need-to-know: access only for food defense qualified individuals, plant managers, and OT staff who need them. (AC-3; AC-6; PR.AA-05)

4.5 **Records retention.** Each division must keep regulated records at least as long as the law requires, including: Produce Safety records 2 years (21 CFR 112.164); preventive controls and food defense records 2 years (21 CFR 117.315; 121.315); H-2A earnings records 3 years after the certification (20 CFR 655.122(j)(4)); WPS application information 2 years after the restricted-entry interval (40 CFR 170.311(b)(6)); Subpart J records as 21 CFR 1.360 sets. Records held in SaaS must also be exported monthly to a group-held copy. (SI-12; CP-9; PR.DS-11)

4.6 Records relied on for food safety, food defense, Produce Safety, or H-2A pay must be protected from undetected change: locked after sign-off, with edits creating new versions and recorded with the editor and reason. (AU-9; SI-7; AU-10; PR.DS-01)

4.7 Grower and cooperative data in the Grower Agronomy Portal may be used only to provide the service unless the grower agrees to more. Any new use (including AI training) needs a data-use review approved by the Group Chief Privacy Officer. (PT-2; PT-3; GV.OC-03)

4.8 Media and devices, including HMIs and controllers, must be sanitized before disposal or reuse. (MP-6; PR.DS-01)

4.9 Restricted or Confidential data must not be entered into AI tools that are not on the approved-tools list. (AC-20; PL-4; PR.DS-01)

## 5. Compliance and enforcement
Compliance is checked through the annual common control assessment and division samples (P07), quarterly access certifications, the annual supplement attestations, and OT change reviews. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions follow POL-01 4.11. OT exceptions also need the division OT security manager's written safety reasoning.

## 7. Related documents
POL-01; POL-05; P02 data map; P10 Group AI Standard.
