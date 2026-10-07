# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Officer); client security information rules owned by the Senior Health Physicist (Part 37 services lead) |
| Approved by | Principal Health Physicist (owner), 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, MP-7, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Client and legal drivers | 10 CFR 37.43(d)(1), (2), (7), (8) and 37.31 flowed down by the Part 37 client contracts (C-NUCLEAR-S01); reactor contract terms on SGI and media (C-NUCLEAR-S03); Fla. Stat. 501.171(2) |

## 1. Purpose
Sort practice and client information by how much harm its loss or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All staff and all practice and client information in any form: in the suite, SYS-02, SYS-03, on laptops, lab workstations, and USB drives, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory; approves new tools |
| Senior Health Physicist (Part 37 services lead) | Owns the Client Security-Related level, the restricted folders, and the handling procedure SEC-INFO-01 |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Practice and client information has four levels:

| Level | Examples | Handling |
|---|---|---|
| **Client Security-Related** | Part 37 clients' security plans, implementing procedures, lists of individuals approved for unescorted access, security and access authorization program review reports and drafts, LLEA coordination records | Only in that client's restricted folder; only client-approved staff; never in email attachments, on USB drives, on lab workstations, or in any AI tool; delivered only by named-recipient link or encrypted mail; returned or destroyed at the end of the engagement |
| **Restricted** | Personal information (Social Security numbers, driver license numbers, payroll, dose records), passwords and MFA codes, any background investigation information seen at a client | Encrypted at rest and in transit; minimum necessary; never in personal accounts or public AI tools |
| **Confidential** | Other client reports, client instrument lists and calibration results, shielding drawings, contracts, security documents | Staff and approved vendors only; encrypted in transit |
| **Public** | Website, brochures, blank certificate templates | No restriction |

When unsure, treat information as the higher level. (RA-2; ID.AM-07)

4.2 Client Security-Related and Restricted information must be encrypted wherever it is stored and whenever it leaves the practice's systems. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 **Where information may be kept.** Client Security-Related information may be kept only in its client's restricted folder in the suite, handled under procedure **SEC-INFO-01** (client information handling), which follows each client's own information protection procedure. In addition:
- **Background investigation records seen at a client must never be copied, photographed, or carried away.** Record sample identifiers only.
- **Safeguards Information must never be accepted.** If anything marked SGI arrives, do not open it further, forward, or copy it; isolate it and call the field services lead (POL-03 4.8).
- Restricted and Confidential information may be kept in the suite, SYS-02, SYS-03, and on encrypted company laptops and drives.
(AC-3; 37.43(d)(1), (2), (7); 37.31)

4.4 The Office Manager must keep a one-page inventory of every computer, every company USB drive (with its holder), every SaaS service, and every place Client Security-Related or Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07)

4.5 Before any new vendor, app, or device receives Confidential or higher information, the Office Manager must approve it and its terms (POL-02 A.5) and add it to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** The approved AI list has one entry: the SYS-02 calibration drift prediction module (P10), for instrument data only, under the P10 conditions. The suite's built-in AI assistant must stay turned off until a P10 assessment approves it. No AI tool, public or approved, may ever receive Client Security-Related or Restricted information. (SA-9; PL-4)

4.7 **Backups.** The suite must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter and give the Office Manager a written result. SYS-02 records (certificates, readings, leak test results, source inventory) must be exported monthly into the suite. Lab workstation 2 must be imaged monthly. (CP-9; CP-4; PR.DS-11)

4.8 **Disposal.** Laptops, lab workstations, and USB drives must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. Company USB drives are wiped after every reactor outage. Paper with Client Security-Related or Restricted information goes in the locked shred bin. The Office Manager keeps each wipe or destruction record. (MP-6; ID.AM-08)

4.9 **Retention and engagement close-out.** At the end of each Part 37 engagement, the Part 37 services lead must return or destroy all copies of the client's Client Security-Related information as the contract requires, confirm it to the client in writing, and keep only the confirmation. Restricted information with no business or license reason (for example, dose reports that show full Social Security numbers) must be replaced with redacted copies or deleted. Records the practice's own license requires are kept as the license requires. (SI-12; 37.43(d)(8) flow-down; 501.171(2))

## 5. Compliance and enforcement
Breaking this policy leads to action under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), the monthly folder reconciliation (POL-02 B.5), quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may allow Client Security-Related information outside its restricted folder.

## 7. Related documents
POL-02; POL-03; SEC-INFO-01 client information handling procedure (due 2026-10-31); inventory; P04 cloud control map; P10 AI risk assessment
