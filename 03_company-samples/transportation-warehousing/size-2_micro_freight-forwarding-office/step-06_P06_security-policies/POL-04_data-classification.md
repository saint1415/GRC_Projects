# Data Classification and Records Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office and Compliance Manager (Security Coordinator and recordkeeping contact under 19 CFR 111.21(d)) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Records rules | 19 CFR 111.21, 111.23, 111.24, 111.25; 19 CFR 163.5; 46 CFR 515.33; 15 CFR 30.10(a); Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and meet the customs, FMC, and export record rules for keeping, storing, and producing records.

## 2. Scope
All employees and all company information in any form: in the customs platform, email, the Client Records Archive, the accounting SaaS, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office and Compliance Manager | Owns this policy; recordkeeping contact for CBP (111.21(d)); keeps the inventory and data map; approves new tools; answers CBP record requests within 30 days (111.25(b)) |
| Licensed Customs Broker (Entry Supervisor) | Makes sure shipment files are complete; approves AI tool use for customs work (4.6) |
| MSP | Encryption, backup, restore tests, and device wiping, as directed |
| All employees | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Importer identification numbers (especially Social Security numbers), CBP Form 5106 data, POAs, entries and invoices, client bank details, the CBP employee list, employee HR files, passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; shared only as 111.24 allows; never in personal accounts or public AI tools |
| **Internal** | Rates, carrier contracts, booking data without client identity, security documents | Employees and approved vendors only; encrypted in transit |
| **Public** | Website, service descriptions | No restriction |

All customs records are client records under 111.24 and are at least Restricted unless the information is available from a public source. When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored and whenever it is sent outside company systems. Email to clients or agents that contains a Social Security number or bank details must use the suite's message encryption. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted information may be kept only in: the customs platform, the suite (email and the Client Records Archive), the accounting SaaS, the bank portal, the suite backup, and the locked file cabinets. Each must store customs records within the United States (111.23(a)). (AC-3; SA-9)

4.4 **Inventory and importer number data map.** The Security Coordinator must keep a one-page inventory of every device, SaaS account, and portal, and a data map of every place importer identification numbers are stored, and update both when anything changes. The data map is what lets the company list compromised importer numbers in a 72-hour CBP notice (111.21(b)). (CM-8; ID.AM-01; ID.AM-07)

4.5 Before any new vendor, app, device, or vendor-enabled feature receives Restricted information, the Security Coordinator must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list has one entry: the customs platform's document capture and classification suggestion feature (P10 AI-001), under the P10 conditions. Every AI classification suggestion for a product not classified before must be approved by a licensed broker before it is transmitted. Public or personal AI chatbots must never receive client information. (SA-9; PL-4)

4.7 **Scanned records (alternative storage).** Paper customs records may be scanned and the paper destroyed only after the advance written notice to CBP Regulatory Audit has been sent at least 30 days before (19 CFR 163.5(b)(1)) and under the written scanning procedure, which covers image quality checks, a naming rule (client, entry or shipment number, document type), indexing, and retrieval. The Security Coordinator tests retrieval of at least 20 random records every year and records the result (163.5(b)(2)(i), (ii), (iv)). (SI-12; CP-4)

4.8 **Backups.** The suite (mail and the Client Records Archive) must be backed up daily with at least 1 year of versions, in storage the company's users cannot delete. The MSP must restore a sample every quarter and give the Security Coordinator a written result. This backup is the "back-up copy" required by 163.5(b)(2)(vi). (CP-9; CP-4; PR.DS-11)

4.9 **Retention.** Customs records are kept at least 5 years after the date of entry; POAs until revoked and then 5 years after revocation or after the client stops being active, whichever is later (111.23(b)). Forwarder shipment files and export records are kept 5 years (46 CFR 515.33; 15 CFR 30.10(a)). The suite retention policy keeps mail and archive files for 6 years and prevents permanent deletion before then. Nothing may be deleted that CBP is seeking or likely to seek (111.26). (SI-12; GV.PO-02)

4.10 **Disposal.** After the retention period, devices and media that held Restricted information must be wiped or destroyed by a vendor that provides a certificate, and paper goes in the locked shred bin (Fla. Stat. 501.171(8)). The Security Coordinator keeps each record. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, quarterly restore results, the yearly retrieval test, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may shorten a legal retention period or skip the 163.5 notice.

## 7. Related documents
POL-02; POL-03; inventory and importer number data map; scanning and retrieval procedure; P04 cloud control map; P10 AI risk assessment
