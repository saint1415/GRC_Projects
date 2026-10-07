# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Privacy and Compliance Manager (with the Depot Director for customer devices and sanitization) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-6, MP-1, MP-4, MP-5, MP-6, MP-7, SC-8, SC-28, SI-4, SI-12, CP-9, CM-8, PE-3, PE-6, PL-4, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Legal and contractual basis | Fla. Stat. 501.171(2), (8); FTC Act Section 5; FTC Disposal Rule 16 CFR 682.3 (background reports); PCI DSS v4.0.1 3.2.1, 3.3.1.2, 9.4, 9.5 (SAQ P2PE) and the SAQ A eligibility criteria; Partner agreements; NIST SP 800-88 Rev. 2 |
| Supporting standards | STD-04 Media sanitization and device disposal standard; STD-08 Customer data access and bench standard; STD-10 Facility, device custody, and payment terminal standard |

## 1. Purpose
Classify company, customer, and partner information by sensitivity and set handling rules so that protection matches the harm a disclosure would cause. For a repair company, that includes the contents of customers' devices.

## 2. Scope
All workforce members at all sites. Covers all company systems and data, customer devices and the data on them while in the company's custody, recovered data, partner claim data, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Privacy and Compliance Manager | Owns classification and the retention schedule; confirms purges |
| IT Director | Implements encryption, backup, and retention controls in systems |
| Depot Director | Owns STD-04 (sanitization) and STD-08 (customer data access and bench standard) with the Director of Retail Operations |
| Data Recovery Manager | Custodian of recovered data; runs retention and deletion in the lab and delivery storage |
| Director of Retail Operations | Device custody, card data rules, and terminal inspections at the stores |
| Chief Financial Officer | Card data rules for the contact center and the e-commerce channel |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer device content (photos, messages, health, location, files); device passcodes; recovered data; background check reports; card data (which must never be stored) | Minimum collection; access only as the job requires; encrypted at rest and in transit; retention limits below |
| **Confidential** | Customer records and tickets, partner claim data, business account data, payroll, contracts, security documents | Need-to-know; encrypted in transit and at rest in company systems |
| **Internal** | Procedures, schedules, parts pricing | Workforce only |
| **Public** | Website, price lists | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on company storage, including the lab storage array, bench workstation transfer caches, and backups, and encrypted in transit. Recovered data must be delivered only by expiring link with a one-time code or on company-issued encrypted drives. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 **Collect less.** Staff must never ask for a customer's email or account password. A device passcode may be collected only when the repair cannot be tested without it, must be entered only in the SYS-01 restricted passcode field (never in notes, on paper, or in chat), and is purged automatically at release. Legacy notes holding passcodes or passwords must be redacted. (SC-28; SI-12; PR.DS-01)
4.4 **Customer data access.** Technicians may access a customer device's content only as far as the repair requires and the customer consented, following the STD-08 test checklist for that repair type (for example, open the camera to test it, but do not open the photo library). Browsing, copying, photographing, or forwarding customer content is prohibited. Copying is allowed only for a data transfer or recovery service the customer ordered, and only to company encrypted storage. Bench sessions are recorded; personal phones and storage must not be connected to bench workstations. (AC-6; MP-7; PR.DS-10)
4.5 **Card data.** Card numbers and security codes may be entered only into the company's P2PE terminals or by the customer into the payment gateway's hosted fields. They must never be written on paper, typed into SYS-01 or any other system, emailed, or taken by the overflow answering service. Contact center recordings must pause during payments. Store Managers must keep the terminal list reconciled with the processor and inspect every terminal weekly, recording each inspection. (SI-12; CM-8; PE-6; PCI DSS 3.2.1, 3.3.1.2, 9.4.1, 9.5.1)
4.6 **Checkout page.** Every script loaded on the mail-in checkout page must be inventoried, justified, and authorized, and the page must be monitored for unauthorized changes (STD-11). (CM-8; SI-4; PCI DSS 6.4.3, 11.6.1; SAQ A eligibility)
4.7 **Retention.** Recovered data must be deleted from the lab storage and delivery storage 30 days after delivery, unless the customer agrees in writing to a longer period (maximum 90 days). Transfer caches on bench workstations are wiped when the ticket closes. Customer records and tickets are kept for 3 years after the last service, then deleted. Partner claim data is kept as the partner agreement states. Purge jobs must alert on failure. Retention applies to backups as they age out. (SI-12; Fla. Stat. 501.171(8))
4.8 **Sanitization and disposal.** Devices and media leaving company custody for recycling, resale of company equipment, or return of loaners must be sanitized at the Depot sanitization line using the clear, purge, or destroy methods in NIST SP 800-88 Rev. 2, with the technique chosen for the media type. Each sanitization must be verified and validated (SP 800-88 Rev. 2 sections 4.5.1 and 4.5.2) and recorded on a certificate of sanitization for each device (section 4.6). The recycler's certificates must list serial numbers. Paper with customer or card data must be cross-cut shredded. Background check reports must be kept in the HR system only and never printed (16 CFR 682.3). (MP-6; ID.AM-08)
4.9 Backups of Restricted and Confidential data must be encrypted, stored in the separate backup account with write-once retention, and restore-tested quarterly. (CP-9; PR.DS-11)
4.10 Restricted and Confidential data must not be entered into AI tools unless the tool is on the approved list and its vendor has signed data-use terms (STD-05; P10). (SA-9)
4.11 Customer devices must be kept in locked storage when not on a bench and shipped only with tracking and signature. Data recovery drives stay in the lab safe. (MP-4; MP-5; PE-3)
4.12 **Health care clients.** The company does not perform data recovery or data transfer for HIPAA covered entities. Intake must ask business and walk-in clients whether the device belongs to a health care practice, and decline those services if so. (PL-4)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Misuse of a customer's device data is treated as serious misconduct. Compliance is checked through the annual control assessment (P07), monthly retention and sanitization metrics, and the log reviews in POL-03.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow storage of card data or collection of account passwords.

## 7. Related documents
POL-01; POL-02; POL-05; STD-04; STD-08; STD-10; STD-11; retention schedule; certificate of sanitization form; P10 approved AI tools list
