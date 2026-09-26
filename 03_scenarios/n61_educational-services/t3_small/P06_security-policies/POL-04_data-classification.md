# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Policy ID | POL-04 |
| Owner | Registrar (FERPA compliance officer), with the Director of Financial Aid for customer information |
| Approved by | Campus President |
| Approved / effective | Approved 2026-08-21; effective 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, SI-12, CP-9, PT-3, PM-21, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.PO-02 |
| Regulatory basis | 16 CFR 314.4(c)(2), (c)(3), (c)(6) (N61-R02); 34 CFR 99.32 and 99.33 (N61-R01); HEA sec. 483 limits on FAFSA data; Fla. Stat. 501.171(8) disposal |

## 1. Purpose
Classify college information by sensitivity and set handling rules so that protection matches the harm a disclosure would cause to students and families.

## 2. Scope
All Cris Santos Company workforce members: employees, full-time and adjunct faculty, contractors, and student workers, and service providers that handle college data. It covers information in every format (electronic and paper) and every location, including vendor systems, the cloud tenant, email, and staff devices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Registrar | Owns classification of education records; approves new uses of Restricted education records; keeps the FERPA disclosure record |
| Director of Financial Aid | Owns customer information and the financial aid data map; approves any export of aid data |
| IT Director | Implements encryption, backup, and disposal controls; approves compensating controls in writing when encryption is infeasible |
| Director of Institutional Effectiveness | Keeps FAFSA data and federal tax information out of the reporting database |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer information (SSNs, ISIR and FAFSA data, federal tax information, verification documents, bank account details for refunds); education records (grades, transcripts, disciplinary records, immunization and background check documents for clinical placements); credentials | Encrypted at rest and in transit; approved systems only; access by role (POL-02 4.2) |
| **Confidential** | Employee HR and payroll data, contracts, security documents, the risk register | Encrypted in transit; need-to-know |
| **Internal** | Class schedules, procedures, internal memos | Workforce only |
| **Public** | Catalog, website, published program outcomes | No restriction |

(RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest on every device, service, and file store, and encrypted in transit over external networks. External email containing SSNs, ISIR data, or other Restricted information must use the college's enforced message encryption. Where encryption is infeasible, the Qualified Individual must approve compensating controls in writing (POL-01 4.7). (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.3 Restricted information may be stored only in approved systems:
- the SIS;
- the FAMS;
- the restricted financial aid folder on the file server (financial aid staff only);
- the backup vault.

Standing spreadsheet exports of aid data are not allowed. The business office must use its FAMS report role instead of receiving emailed spreadsheets. Restricted information must never be kept on personal devices, lab computers, or personal cloud accounts. (AC-3; SC-28; 314.4(c)(3))

4.4 The Director of Financial Aid, with the IT Director, must keep a **data map** of where customer information and education records are stored, who can reach them, and which service providers receive them. The map must be reviewed each year and whenever a system or vendor changes. (CM-8; ID.AM-07; 314.4(c)(2))

4.5 FAFSA data and federal tax information must be used only for the application, award, and administration of student aid. They must be tagged in the SIS and FAMS and must not be copied to the reporting database, the early-alert model, or any other use without a documented legal basis approved by the Director of Financial Aid. (PT-3; AC-3; HEA sec. 483)

4.6 Customer information must be securely disposed of no later than two years after it was last used to provide a service to the student or family. The exceptions are information needed for business operations, information that law or regulation requires the college to keep, including Title IV records under 34 CFR 668.24, and information where targeted disposal is not reasonably feasible. Paper must be shredded by a vendor that issues certificates of destruction. Drives must be wiped with a logged method, or destroyed with a certificate. (MP-6; ID.AM-08; 314.4(c)(6)(i); Fla. Stat. 501.171(8))

4.7 Backups of Restricted information must be encrypted, stored apart from production (a separate account and region), protected from deletion or alteration for the retention period, and restore-tested every quarter. (CP-9; PR.DS-11)

4.8 The college must keep a **retention schedule** covering customer information and education records, aligned to Title IV record retention requirements and FERPA. The Registrar and the Director of Financial Aid must review it every year to minimize unnecessary retention and run the annual disposal. (SI-12; GV.PO-02; 314.4(c)(6)(ii))

4.9 Every request for, and disclosure of, personally identifiable information from education records must be recorded in the student's SIS disclosure record. Financial aid, career services, and the Registrar all use the same record, and each entry names the party and its legitimate interest. Every disclosure must carry the redisclosure notice. (PM-21; 34 CFR 99.32(a); 99.33(a))

4.10 Restricted information must not be entered into AI tools or other third-party services unless:
- the tool is on the approved list (P10);
- the vendor's contract prohibits training on or other secondary use of college data;
- the vendor meets POL-01 4.8.

(SA-9; 34 CFR 99.31(a)(1)(i)(B))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.10). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the annual data map review, and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; P10 AI approved-tools list; records retention schedule (due 2027-03-31); FERPA annual notice; FSA Handbook Vol. 2 Ch. 7
