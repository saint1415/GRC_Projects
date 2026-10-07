# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Qualified Individual) |
| Approved by | Owner CPA, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, SC-8, SC-28, SA-4, SA-9, PT-4, PL-4, CP-9, CP-4, SI-12, MP-6, PE-3 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05, GV.SC-06, GV.OC-03 |
| FTC Safeguards Rule (N54-R01) | 314.4(c)(2), (c)(3), (c)(4), (c)(6), (f) |
| IRC 7216 (N54-R02) | 26 CFR 301.7216-2(c)(2), (d)(1), (h)(1); 301.7216-3(a)(1), (a)(3), (b)(1), (b)(4) |
| IRS (N54-R03) | Pub. 1345 (Form 8879 retention) |

## 1. Purpose
Sort firm information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and make sure tax return information is shared only as IRC 7216 allows.

## 2. Scope
All workforce members and all firm and client information in any form: in the tax software, the portal, email and cloud storage, the payroll and accounting platforms, AI tools, on devices and the MFP, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner CPA | Approves the retention schedule and any new disclosure purpose; signs off on IRC 7216 consent forms |
| Office Manager | Owns this policy; keeps the asset and data inventory and the approved-tools list; runs the pre-adoption checklist |
| Senior Tax Accountant | Business owner of the AI assistant; keeps AI use within 4.7 |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Firm information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Tax return information (everything a client gives the firm to prepare a return, and anything derived from it); SSNs and ITINs; bank and account numbers; payroll employee data; client financial records; IRS notices; passwords and MFA codes | Only in approved locations (4.3); encrypted at rest and in transit; shared only under 4.6; never in personal accounts or unapproved AI tools |
| **Internal** | Firm payroll and HR files, contracts, security documents, schedules without client details | Workforce and approved vendors only; encrypted in transit |
| **Public** | Website, office hours, newsletters | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, including every laptop and desktop, and whenever it leaves the firm's systems. Where encryption is not feasible, the Qualified Individual must approve a compensating control in writing. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.3 Restricted information may be kept only in the tax software, the portal, the suite (email and the client folders), the payroll and client accounting platforms, the backup service, and locked cabinets for paper during the season. Scans must not be kept on the MFP or a desktop longer than one business day. (AC-3; ID.AM-07)

4.4 The Office Manager keeps a one-page inventory of every device (including the MFP and staff phones with firm email), every SaaS service and AI tool, and every place Restricted information is stored, and updates it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; 314.4(c)(2))

4.5 **Pre-adoption checklist.** Before any new vendor, application, AI tool, or new feature of an existing product receives Restricted information, the Office Manager must record: the vendor's security evidence (a SOC 2 report or equivalent), where the data is processed and stored, the contract's security and breach notice terms, and the IRC 7216 basis for the disclosure (4.6). The Owner CPA approves. (SA-4; SA-9; GV.SC-06; 314.4(c)(4); 314.4(f)(1)-(2))

4.6 **IRC 7216.** Tax return information may be disclosed or used only: within the firm by U.S.-based staff (301.7216-2(c)(2)); to another tax return preparer in the United States for preparation, e-file, or auxiliary services that involve no substantive determinations, such as the tax software vendor, and the portal vendor once its U.S. processing is confirmed (301.7216-2(d)(1); P03 G-045); to contractors only as needed and only after each technician signs the written notice (301.7216-2(d)(2)); for the same client's bookkeeping and payroll work (301.7216-2(h)(1)); or with the client's prior written consent on the firm's consent form (301.7216-3). Consent is signed before the disclosure, never made a condition of service, and a copy is given to the client. No consent may be sought to send a Form 1040 filer's SSN to a preparer outside the United States (301.7216-3(b)(4)). (PT-4; GV.OC-03)

4.7 **AI tools.** Only AI tools on the approved list may be used for firm work. Today the list has one entry, the business-plan AI assistant (SYS-09), for the 3 enrolled users, under these rules until counsel confirms an IRC 7216 basis: no client names, SSNs, account numbers, addresses, or uploaded client documents; use a client code; a CPA or enrolled agent checks every figure and cited authority before anything is sent (P10). Public or personal AI chatbots must never receive Restricted information. AI features inside existing products (for example, the tax software's AI extraction) stay off until they pass 4.5. (SA-9; PL-4; 301.7216-3(a)(1))

4.8 **Backups.** Mailboxes and client folders must be backed up daily, with copies kept at least one year in storage that an administrator cannot change or delete within that period. The MSP restores a full mailbox and a full client folder tree every quarter and gives the Office Manager a written result. (CP-9; CP-4; PR.DS-11)

4.9 **Retention.** Client records are kept only as long as the retention schedule allows: what law requires (including Forms 8879 for 3 years from the return due date or IRS received date, whichever is later), what the client engagement needs, and nothing more. Customer information is disposed of no later than 2 years after it was last used to serve the client, unless one of the exceptions in 314.4(c)(6)(i) applies and is recorded. The Owner CPA reviews the schedule each June. (SI-12; ID.AM-08; 314.4(c)(6)(i)-(ii); Pub. 1345)

4.10 **Disposal.** Devices and media that held Restricted information must be wiped before reuse or return, or destroyed by a vendor that provides a certificate. The MFP's drive is wiped, with a certificate, or kept by the firm when the lease ends. Paper goes in the locked shred bin. The Office Manager keeps each wipe and destruction record. (MP-6; ID.AM-08; 314.4(c)(6)(i); Fla. Stat. 501.171(8))

4.11 **Paper and the front desk.** Client paper stays in locked cabinets when not in use, is never left at the front desk overnight, and is returned or shredded after scanning as the engagement letter says. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.5. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the monthly program review, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.11.

## 7. Related documents
POL-02; POL-03; asset and data inventory; approved-tools list; IRC 7216 consent form; retention schedule; P04 cloud control map; P10 AI risk assessment
