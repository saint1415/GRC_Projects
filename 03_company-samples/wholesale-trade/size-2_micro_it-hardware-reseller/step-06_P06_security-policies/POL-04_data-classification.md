# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations Manager (security and compliance lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-22, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, PL-4, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Contract and regulatory basis | FAR 52.204-21(b)(1)(i), (iii), (iv), (vii); 32 CFR 170.19(b); Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and keep CUI out of the company's systems.

## 2. Scope
All workforce members and all company information in any form: in the ERP, email, shared folders, supplier portals, on laptops and the setup bench, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the inventory; approves new tools and vendors |
| Owner | Decides on any CUI received; approves posting to public sites |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Operations Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Federal Contract Information (DoD equipment lists, asset tags, user and room assignments, delivery details); personal information (employee Social Security and bank account numbers, customer account credentials); supplier bank details; passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; only staff who need it; never in personal accounts or public AI tools |
| **Internal** | Pricing, quotes, supplier terms, contracts, security documents, the item master | Staff and approved vendors only; encrypted in transit |
| **Public** | Catalog content, the website, marketing material | No restriction once approved for posting (4.10) |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every laptop, the setup bench, and any phone that holds it, and whenever it is sent outside company systems. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))

4.3 Restricted information may be kept only in: the ERP, the suite's FCI and HR folders, company laptops, and the backup service. The setup bench may hold the settings file and equipment list for the active job only; they are deleted when the job is delivered. (AC-3; FAR 52.204-21(b)(1)(i), (iii))

4.4 **No CUI.** The company does not accept Controlled Unclassified Information. A document marked CUI, or a request to handle network drawings, configuration files, or other technical information that a DoD customer says is controlled, must not be opened further, copied, or forwarded. The recipient tells the Owner at once, and the Owner asks the sender to withdraw it and decides with counsel whether the order can proceed. Accepting CUI would bring DFARS 252.204-7012, NIST SP 800-171, and CMMC Level 2 into force and requires a new risk assessment first. (AC-3; RA-2)

4.5 The Operations Manager must keep a one-page inventory of every device, network device, SaaS service, and place Restricted information is stored, with the manufacturer of record for each device, and update it when anything is added or removed. (CM-8; ID.AM-01; 32 CFR 170.19(b))

4.6 Before any new vendor, app, or device receives Restricted information, the Operations Manager must approve it under POL-02 A.7, and it must be added to the inventory. (SA-9; GV.SC-05)

4.7 **Backups.** The suite must be backed up nightly, with versions kept at least 1 year in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter and give the Operations Manager a written result. (CP-9; CP-4; PR.DS-11)

4.8 **Disposal.** Laptops, drives, and other media must be wiped with a recorded method before reuse or disposal, or destroyed by a vendor that issues a certificate of destruction. Paper with Restricted information is shredded. The Operations Manager keeps a disposal log. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(8))

4.9 **AI tools.** Restricted information may be entered only into AI tools on the approved list, and today no AI tool is approved for FCI. The ERP's AI reorder feature is approved only with DoD orders excluded from its data feed and with the conditions in P10. One business AI assistant is approved for Internal and Public information. Public or personal AI chatbots must never receive Restricted or Internal information. (SA-9; PL-4; FAR 52.204-21(b)(1)(iii))

4.10 **Public posting.** Nothing about DoD customers, delivery locations, setup orders, or the people the company equips may be posted on the website, marketplaces, or social media. The Owner approves each post. (AC-22; FAR 52.204-21(b)(1)(iv))

4.11 **Retention.** Security and assessment records are kept for 6 years (POL-02 A.12). Order records follow the company's accounting retention schedule. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the annual Level 1 self-assessment, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.13. No exception may allow CUI into company systems.

## 7. Related documents
POL-02; POL-03; device and data inventory; P04 cloud control map; P10 AI risk assessment
