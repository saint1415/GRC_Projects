# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Privacy and Compliance Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-2, MP-6, SC-8, SC-12, SC-28, CP-9, CM-12, SI-12, SA-9, PT-5, AC-3 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.OC-03 |
| PCI DSS v4.0.1 | Requirements 3, 4, 9.4 (N44-45-R01) |
| Other rules | FTC Act Section 5 (N44-45-R02); Fla. Stat. 501.171(2), (8) |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so protection matches the harm a disclosure or loss would cause, and so customer data is used only as the company has told customers it will be.

## 2. Scope
All information the company creates, receives, maintains, or transmits, in any form (including paper), at every site and in every system, including data held by vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Privacy and Compliance Manager | Owns classification; runs the data sharing review; approves new locations of Restricted data |
| Data owners (business leaders) | Classify their data; approve access and sharing |
| IT Director | Implements encryption, backup, data discovery, and disposal controls; keeps the data inventory and data flow maps |
| Store Managers and the Director of Fresh Departments | Apply the card data rules at service desks, deli, and bakery counters |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card data and sensitive authentication data, credentials, member-level loyalty and purchase history, customer accounts and app location data, employee Social Security numbers and bank details | Encrypted at rest and in transit; minimum necessary; approved systems only |
| **Confidential** | Supplier campaign and sales data, contracts, prices before release, security documents, board materials | Encrypted in transit; need-to-know; each supplier sees only its own data |
| **Internal** | Store schedules, procedures, internal announcements | Workforce only |
| **Public** | Weekly ads, website content | No restriction |

4.2 **Card data rules.** Card numbers may be captured only on company PIN pads, the processor's hosted payment fields and SDK, or the virtual terminal on designated service-desk PCs. Staff must never write full card numbers or security codes on paper, and must never accept or send card numbers by email, chat, or text. Security codes and other sensitive authentication data must never be kept after authorization. Card numbers received by email or chat must be deleted and the customer told to use a supported channel. (SI-12; PR.DS-01; PCI DSS 3.2, 3.3, 4.2)
4.3 Restricted data must be encrypted at rest on every device, service, and backup, and in transit on every network. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI DSS 4.2)
4.4 Encryption keys for cloud workloads and backups must be managed in the company's key management service, with separate keys for the backup account and annual rotation. (SC-12)
4.5 Restricted data may be stored only in approved systems: the POS, the e-commerce platform, the loyalty and CDP database, the data warehouse, approved file shares, the backup account, and approved vendor systems under contract. It must never be kept on personal devices, in personal cloud accounts, in email attachments sent outside the company, or in unapproved AI tools. (AC-3; SA-9)
4.6 Customer and loyalty data may be used only for the purposes described in the privacy notice. Any new use or sharing, including supplier data programs and agency exports, requires the data sharing review in POL-01 4.15 and a written agreement before data moves. (PT-5; GV.OC-03)
4.7 The IT Director must keep an inventory and data flow maps showing where Restricted data is stored and which vendors receive it, including paper records, and must reconcile them quarterly. (CM-12; ID.AM-07; PCI DSS 12.5)
4.8 Paper with Restricted data must be kept locked and destroyed by cross-cut shredding when no longer needed. Electronic media and POS hardware (registers, store server drives, PIN pads, handhelds) must be sanitized or destroyed, with a certificate, before disposal or return to a vendor. (MP-2; MP-6; ID.AM-08; PCI DSS 9.4; Fla. Stat. 501.171(8))
4.9 Backups of Restricted data must be encrypted, stored in the separate backup account in a second region, protected by write-once retention, and restore-tested at least quarterly for each company-managed workload. Store POS server images must also be copied off-site. (CP-9; PR.DS-11)
4.10 **Retention.** Loyalty purchase history must be kept no longer than 3 years after the transaction. Closed online accounts must be deleted within 90 days, as the privacy notice promises. Agency and supplier copies must be deleted when the agreed purpose ends. (SI-12)
4.11 Restricted and Confidential data must not be entered into AI tools unless the tool is on the approved list and the vendor contract prohibits training shared models on company data (P10). (SA-9)
4.12 Supplier campaign and sales data must be separated so that each supplier can see only its own data, and the separation must be tested at least annually. (AC-3)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual independent assessment (P07), quarterly data discovery scans, and quarterly inventory reconciliation.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow storage of sensitive authentication data after authorization.

## 7. Related documents
POL-01; POL-05; STD-05; STD-07; STD-08; P04 cloud architecture; P10 AI approved-tools list; privacy notice; catering order procedure
