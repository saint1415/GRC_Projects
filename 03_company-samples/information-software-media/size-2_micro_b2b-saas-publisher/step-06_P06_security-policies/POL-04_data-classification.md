# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations and Finance Manager (privacy lead), with the CTO for technical rules |
| Approved by | Chief Executive Officer, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after a new data type, sub-processor, or AI feature |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, SC-8, SC-28, CP-9, CP-4, SA-3(2), SA-9, SI-12, SI-12(1), MP-6, AU-2 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Regulatory drivers | N51-R01 (FTC Act Section 5: reasonable security; accurate data-use statements); Fla. Stat. 501.171(2); customer DPA (use limits, 60-day deletion, sub-processor notice); SOC 2 C1.1, C1.2 |

## 1. Purpose
Sort the company's information by how much harm its loss or disclosure would cause, and set simple handling rules for each level, with extra rules for vendors' taxpayer identification numbers.

## 2. Scope
Everyone who works for the company and all company and customer information in any form: in the production platform, backups, logs, SaaS tools, email, laptops, and any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations and Finance Manager | Owns this policy; keeps the data inventory and the sub-processor list; runs customer data deletion |
| CTO | Approves technical handling (encryption, masking, backups, logging); keeps the approved AI tools list |
| Senior Software Engineer | Operates backups, restore tests, and log redaction |
| MSP | Laptop encryption and wiping |
| Everyone | Handle information according to its level |

## 4. Policy statements
4.1 Information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Everything customers store in the platform (vendor records, contacts, certificates, licenses, W-9s); taxpayer identification numbers (most sensitive, see 4.3); passwords, keys, and other secrets; database extracts and backups | Only in approved locations (4.2); encrypted at rest and in transit; minimum necessary; never on laptops, in personal accounts, or in unapproved AI tools |
| **Internal** | Source code, architecture and security documents, contracts, financials, employee files, sales pipeline | Staff, the contractor, and approved vendors only; encrypted in transit |
| **Public** | Website, published documentation, status page | No restriction, but statements must be approved under POL-02 A.4 |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Approved locations for Restricted customer data:** the production database and document bucket, the separate backup account, and, only as each one's DPA allows, the listed sub-processors. Support tickets may hold customer screenshots only if the customer sends them, and tickets are deleted 12 months after closing. Customer data must never be stored on laptops. (AC-3; SA-3(2); PR.DS-01)

4.3 **Taxpayer identification numbers.** The full TIN may be kept only inside the stored W-9 document. The platform stores the TIN type and the last 4 digits as data fields and shows the full number only to customer administrators. Before any document text is sent to the AI model provider or written to a log, Social Security numbers must be masked. The website and sales material may describe this protection only once it is verified (POL-02 A.4). (SI-12(1); SC-28; PR.DS-01)

4.4 **Encryption.** Restricted information must be encrypted at rest (provider-managed keys are acceptable) and in transit with TLS 1.2 or higher. Every company laptop must use full-disk encryption. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.5 **Data inventory.** The Operations and Finance Manager must keep a one-page inventory of every place Restricted information is stored or sent (systems, sub-processors, and data elements) and update it before any new system, vendor, or data flow goes live. The CTO checks it against the cloud account and SaaS tools every quarter. (CM-8; ID.AM-01; ID.AM-07)

4.6 **New vendors and data flows.** Before any vendor, contractor, or new feature receives Restricted information, the CTO must approve the data flow, a written agreement must be in place, the vendor must be added to the published sub-processor list if the DPA requires, and customers must receive 30 days' notice (POL-02 A.5). (SA-9; GV.SC-05)

4.7 **AI tools.** Restricted information may be sent only to AI tools on the approved list, kept by the CTO:

| Tool | Approved use | Conditions |
|---|---|---|
| AI model provider (SYS-06), for the product's document extraction | Customer documents, with Social Security numbers masked | Signed DPA with no-training and zero-retention terms; listed sub-processor; P10 conditions met |
| Company-licensed AI coding assistant (staff use) | Source code and Internal documents only | Business terms with no training on inputs; no customer data, secrets, or keys |
| Public or personal AI chatbots | None | Must never receive Restricted or Internal information |

(SA-9; PL-4)

4.8 **Test data.** Development, debugging, and testing must use the synthetic test data set. Production data may be used outside production only with the Chief Executive Officer's written approval for a specific incident, in the production account, and deleted afterwards. (SA-3(2))

4.9 **Backups.** The production database and document bucket must be backed up at least daily, with copies kept for at least 35 days in a separate backup account under write-once retention that production administrators cannot change. Document bucket versioning must stay on. The Senior Software Engineer must restore a sample at least twice a year, time it against the BIA RTO, and record the result. (CP-9; CP-4; PR.DS-11)

4.10 **Retention and deletion.** Customer data is kept for the life of the contract and deleted within 60 days after termination, including backups as they expire, with a deletion certificate sent to the customer. Superseded documents follow each customer's retention setting. Logs are kept for 1 year. Security records are kept as POL-02 A.7 requires. (SI-12; ID.AM-08)

4.11 **Logs.** Applications must not write Restricted data to logs or error reports. Taxpayer identification numbers, document text, and secrets must be redacted before anything is sent to the error tracking service. Object read logging on the document bucket and database audit logging must stay on. (AU-2; SI-12)

4.12 **Disposal.** Laptops must be wiped through the MSP's device management before reissue or disposal, and the MSP keeps the record. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.10. Compliance is checked through the quarterly inventory check, the twice-yearly restore results, the deletion certificates, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; data inventory; published sub-processor list; DPA; P04 cloud control map; P05 BIA; P10 AI risk assessment
