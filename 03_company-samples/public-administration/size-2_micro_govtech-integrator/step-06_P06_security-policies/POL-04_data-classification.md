# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations Manager (Security and Compliance Officer) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, CM-12, MP-2, MP-6, SC-8, SC-13, SC-28, CP-9, CP-4, SI-12, SA-9 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Contract and legal drivers | CJISSECPOL v6.1 SC-13 and SC-28 (AC-01); Pub. 1075 Exhibit 7 I(3), I(5) and sec. 1.8.2 (SC-01); SP 800-53 Moderate (AC-02, AC-03, AC-04); Fla. Stat. 501.171(2); Fla. Stat. 119.0701(2)(b) |

## 1. Purpose
Sort the information the company handles by how much harm its loss or disclosure would cause, and set simple handling rules for each level, so that agency data stays only where the contracts allow.

## 2. Scope
All staff and all information the company handles in any form: in the platform, SYS-02, the suite, the helpdesk, the repository, on laptops and phones, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the inventory and the approved locations list; approves new tools |
| Lead Platform Engineer | Exports, backups, restore tests, encryption settings, and deletion of working files |
| MSP | Laptop encryption, USB restrictions, wiping, and disposal records, as directed by the Operations Manager |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Information has four levels:

| Level | Examples | Handling |
|---|---|---|
| **Regulated** | CJI and CHRI (AC-01); FTI (SC-01, which never enters company systems) | Only the approved locations in 4.3 (never for FTI); only screened staff (POL-02 B.2); encrypted with FIPS 140-3 certified modules in transit and 256-bit encryption at rest; never in email, chat, or tickets |
| **Restricted** | Other agency personal information: Social Security numbers, income documents, driver license numbers, names and addresses in agency files; passwords, keys, and tokens | Only the approved locations in 4.3; encrypted at rest and in transit; minimum necessary; never in personal accounts or public AI tools |
| **Internal** | Contracts, invoices, payroll, security documents, configurations without agency data | Staff and approved vendors only; encrypted in transit |
| **Public** | Website, marketing material | No restriction |

When unsure, treat information as Regulated. (RA-2; ID.AM-07)

4.2 Regulated and Restricted information must be encrypted wherever it is stored, including on every laptop (full-disk encryption with 256-bit keys), and whenever it moves. CJI in transit must use FIPS 140-3 certified modules (CJISSECPOL v6.1 SC-13). USB storage devices are blocked on laptops except by approved exception. (SC-8; SC-13; SC-28; MP-2; PR.DS-01; PR.DS-02)

4.3 **Approved locations.**
- Regulated (CJI): the AC-01 workspace; the SYS-02 working folder only until the nightly load finishes (deleted automatically after a successful load); the write-once export storage.
- Restricted: the agency workspaces; the write-once export storage; the suite only during an implementation, in the project folder, deleted within 30 days after go-live.
- Not approved for any agency data: the helpdesk (attachments from agency users are blocked or deleted), the repository, laptops' download folders, phones, and the office.
(AC-3; CM-12)

4.4 **Inventory.** The Operations Manager must keep a one-page inventory of every laptop, SaaS service, and place agency data is stored, update it when anything changes, and run a quarterly scan of the suite for Social Security number and taxpayer identification number patterns. (CM-8; CM-12; ID.AM-01)

4.5 **FTI stays in the agency.** FTI may be viewed only inside the revenue agency's virtual desktop. It must never be typed, pasted, photographed, printed, or copied into any company system, file, note, or ticket, including defect logs. Defect logs use record keys only. Anyone who finds FTI outside the agency's environment must report it at once under POL-03 4.2 and 4.4, and not delete it until the agency directs how. (Pub. 1075 Exhibit 7 I(3); sec. 1.8.2; SI-12)

4.6 **AI tools.** Agency data may go only to AI services on the approved list kept by the Operations Manager. On 2026-08-31 the list has one entry: the platform's AI add-on, for the AC-02 workspace only, and only once the P10 conditions are met. Public or personal AI tools must never receive agency data, code containing credentials, or security documents. (SA-9; PL-4)

4.7 **Backups and logs.** AC-01 and AC-02 workspace data must be exported at least every 4 hours, and AC-03 and AC-04 data every night, to write-once storage in a separate account, kept 30 days. A record-level restore from the exports must be tested every quarter and the result written down. Audit logs from the platform and SYS-02 are copied weekly to write-once storage and kept 1 year. (CP-9; CP-4; AU-11; PR.DS-11)

4.8 **Retention and disposal.** Working files are deleted when their task ends. Laptops and media that held agency data must be wiped before reuse, or destroyed by a vendor that gives a certificate; the MSP keeps a record of each. At the end of an agency contract, the company exports the agency's records in a usable format, transfers them at no cost, deletes its copies (including exports and backups) when they expire, and gives the agency a written deletion certificate. At the end of SC-01, the company certifies that no FTI is held on its systems (Pub. 1075 Exhibit 7 I(5)). (MP-6; SI-12; Fla. Stat. 119.0701(2)(b)4.)

4.9 **Public records requests.** Agency records the company holds are the agency's public records. Any request to inspect or copy them goes to the agency's records custodian the same day; staff never release agency records themselves, and exempt or confidential records stay protected during and after the contract (Fla. Stat. 119.0701(2)(b)3., (3)(a)). (SI-12)

4.10 **Office.** No agency data may be stored or printed in the office. (PE-17; MP-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the quarterly suite scan (4.4), quarterly restore results (4.7), the MSP's monthly encryption report, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may place FTI in a company system or CJI in an unapproved location.

## 7. Related documents
POL-02; POL-03; inventory and approved locations list; P04 cloud control map; P10 AI risk assessment; contract-end checklist
