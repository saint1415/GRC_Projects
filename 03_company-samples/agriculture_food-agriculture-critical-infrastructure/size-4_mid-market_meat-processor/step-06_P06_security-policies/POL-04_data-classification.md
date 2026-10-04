# Data Classification and Records Integrity Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Vice President of Food Safety and Quality Assurance (food safety records and formulations) with the IT Director (all other data) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (new; the 2024 set had no classification policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AU-9, AU-10, AU-11, SC-8, SC-28, SI-7, SI-12, MP-6, CP-9 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, PR.PS-04 |
| Rules | 9 CFR 417.5(b)-(f); 9 CFR 416.16; 9 CFR 430.4(c)(7); Fla. Stat. 501.171(2), (8) |
| Supporting standards | STD-05 Electronic records integrity; STD-06 OT backup and recovery |

## 1. Purpose
Classify company information so it gets protection matched to the harm its loss or alteration would cause, and make electronic food safety records trustworthy enough to support every shipping decision and every FSIS review.

## 2. Scope
All company information in any form, at both plants and the corporate offices, including OT data (setpoints, PLC logic, recipes), food safety records, and data held by vendors.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Formulations (including cure, brine, and antimicrobial levels) and blend recipes; food defense plans and vulnerability assessments; PLC programs and OT network diagrams; employee Social Security numbers, bank accounts, and benefits data; credentials | Named access only; MFA; encrypted at rest and in transit; no personal devices; no unapproved AI tools; access list reviewed quarterly |
| **Food safety record** (integrity-critical) | CCP monitoring, corrective action, verification, pre-shipment review, Sanitation SOP, and Listeria records; historian CCP data | Integrity controls in section 4; retention per 9 CFR 417.5(e) and 416.16(c) |
| **Confidential** | Customer contracts and pricing; production plans; supplier lists; internal audit reports | Business need to know; encrypted at rest in company systems |
| **Internal** | Policies, procedures, training material | Company systems only |
| **Public** | Published product information, recall notices | No restriction |

## 4. Policy statements
4.1 Every data owner must classify the data they own using section 3. Unlabeled data is treated as Confidential. (RA-2; ID.AM-05)
4.2 Restricted data must be stored only in approved locations: the restricted FSQA library, the MES and OT repositories, the HR SaaS, and approved cloud workloads. It must never be on open file shares. (AC-3; PR.DS-01)
4.3 Restricted and Confidential data must be encrypted at rest and in transit using STD-01 settings (TLS 1.2 or higher). Industrial protocols inside OT zones are exempt, and are protected by segmentation instead. (SC-8; SC-28; PR.DS-02)
4.4 **Electronic food safety records.** Systems that hold food safety records must: keep an audit trail that cannot be turned off or edited by users; record each entry with the system date and time from a synchronized clock and the authenticated identity of the employee making it; lock records after pre-shipment review, with any later correction recorded as a new entry with a reason; and separate system administration from record entry. These are the company's "appropriate controls" under 9 CFR 417.5(d) and 416.16(b). (AU-9; AU-10; SI-7; PR.DS-10; PR.PS-04)
4.5 Food safety records must be retained for at least 2 years (covering the longest period in 9 CFR 417.5(e)) and Sanitation SOP records at least 6 months (416.16(c)), and must be retrievable on site within 24 hours of an FSIS request. (AU-11; SI-12)
4.6 Restricted and food safety data must be backed up to isolated, immutable storage, and restores must be tested at least quarterly (STD-06). (CP-9; PR.DS-11)
4.7 Signed paper formulation masters must be kept in the FSQA office and compared with the MES and blend recipes after any incident and at least monthly. (SI-7)
4.8 Restricted and Confidential data must not be entered into AI tools that are not on the approved list (POL-05 4.7; STD-09). (AC-3)
4.9 Media and documents containing Restricted or Confidential data must be disposed of so they cannot be read (certified shredding or destruction, NIST SP 800-88 methods for drives). (MP-6; Fla. Stat. 501.171(8))

## 5. Compliance and enforcement
Checked through the annual assessment (P07) and the VP FSQA's quarterly records integrity review. Violations are handled under POL-01 section 5.

## 6. Exceptions
Follow POL-01 section 4.8. No exception may disable a records audit trail.

## 7. Related documents
POL-01; POL-05; STD-05; STD-06; HACCP plans; Sanitation SOPs; Listeria program
