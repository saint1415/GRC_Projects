# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations Manager (Security and Privacy Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Legal drivers | 8 CFR 274a.2(b)(2)-(4); Fla. Stat. 448.095(2)(d); 16 CFR 682.3; Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Sort firm information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and say how long the firm keeps its most sensitive records and how it disposes of them.

## 2. Scope
All staff of Cris Santos Company and all firm information in any form: in the ATS, the payroll service, the productivity suite, the screening portal, E-Verify, the accounting SaaS, on laptops and phones, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the device and data inventory; approves new tools; runs the annual purge |
| Onboarding and Payroll Coordinator | Keeps the paper Form I-9 files and their index |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Operations Manager |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Firm information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSNs, dates of birth with names, bank account numbers, Forms I-9 and identity document copies, E-Verify case data, consumer reports, payroll and tax records, passwords and MFA codes | Only in approved locations (4.3); encrypted at rest and in transit; access per POL-02 B.2; never in personal accounts, texts, or public AI tools |
| **Internal** | Resumes and applicant records, job orders, client contacts and bill rates, contracts, security documents | Staff and approved vendors only; encrypted in transit |
| **Public** | Job ads, website, career site text | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, including on every laptop and phone, and whenever it is sent outside firm systems. Staff must not ask candidates to email or text identity documents or forms; they send the ATS upload link. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted information may be kept only in: the payroll service; the ATS onboarding packets; the screening portal; E-Verify; the restricted "Onboarding" folder in the shared drive (Operations Manager and Coordinator only); and the locked Form I-9 cabinet. Email may carry Restricted information only to an approved vendor through its secure channel. (AC-3; Fla. Stat. 501.171(2))

4.4 The Operations Manager must keep a one-page inventory of every device, every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07)

4.5 Before any new vendor, app, or device receives Restricted information, the Operations Manager must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Firm information may be entered only into AI tools on the approved list, which the Operations Manager keeps with this policy. Today: the ATS AI match feature in sort-only mode under the P10 conditions (applicant records only), and the ATS generative writer for job ads and messages (no Restricted information). Public or personal AI chatbots must never receive Restricted or Internal information about any person. (SA-9; PL-4)

4.7 **Form I-9 records.** Paper is the firm's only record of retention for Forms I-9. The Coordinator photocopies every identity document presented (the same practice for every new hire) and keeps the copies with the form. Forms I-9 and document images must not be scanned into the shared drive, email, or phones. Existing scans are deleted once each paper file is checked as complete (target 2026-12-31). (SI-12; 8 CFR 274a.2(b)(3)-(4))

4.8 **Retention schedule.**

| Record | Keep for | Then |
|---|---|---|
| Form I-9 with document copies and E-Verify case results | 3 years after the date of hire or 1 year after employment ends, whichever is later (8 CFR 274a.2(b)(2)(i)(A)), and never less than 3 years (Fla. Stat. 448.095(2)(d)) | Shred in the annual purge |
| Consumer reports | Not kept by the firm; the screening portal keeps them under the provider's terms. Any downloaded copy is deleted within 30 days after the hiring decision | Delete |
| Payroll and tax records | As the payroll vendor and the outside CPA firm advise for tax purposes | Vendor deletes at exit |
| Applicant records not hired | 2 years after the last activity | ATS purge |
| Security records | 5 years (POL-02 A.7) | Delete |

(SI-12; ID.AM-08)

4.9 **Backups.** The productivity suite must be backed up daily, with versions kept at least 90 days in storage that cannot be changed or deleted within that period, and with MFA on the backup console. The MSP must restore a sample every quarter and give the Operations Manager a written result. The Senior Recruiter exports ATS candidate and placement data every quarter into the restricted folder. (CP-9; CP-4; PR.DS-11)

4.10 **Disposal.** Paper with Restricted information goes in the locked shred bin, emptied by a shredding vendor that issues certificates. Laptops, phones returned to the firm, and the scanner's storage must be wiped before reuse, return, or disposal, or destroyed by a vendor that provides a certificate. The Operations Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; 16 CFR 682.3; Fla. Stat. 501.171(8))

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the annual purge record, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may shorten a legal retention period.

## 7. Related documents
POL-02; POL-03; device and data inventory; Form I-9 index; P04 cloud control map; P10 AI risk assessment
