# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager (with the Operations Manager for customer devices) |
| Approved by | General Manager |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-4, MP-6, MP-7, SC-8, SC-28, SI-12, CP-9, CM-8, PE-6 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Legal and contractual basis | Fla. Stat. 501.171(2), (8); FTC Act Section 5; FTC Disposal Rule 16 CFR 682.3 (background reports); PCI DSS v4.0.1 3.2.1, 3.3.1.2, 9.4, 9.5 (SAQ P2PE); NIST SP 800-88 Rev. 2 |

## 1. Purpose
Classify company and customer information by sensitivity and set handling rules so that protection matches the harm a disclosure would cause. For a repair company, that includes the contents of customers' devices.

## 2. Scope
All Cris Santos Company workforce members (employees, managers, temporary staff, and contractors) at Stores A to D and the Depot. Covers all company systems and data, customer devices and the data on them while they are in the company's custody, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns classification; implements encryption, backup, and retention controls |
| Operations Manager | Owns the customer data access standard and the sanitization standard |
| Data Recovery Lead | Custodian of recovered data; runs retention and deletion in the lab |
| Store Managers | Device custody, card data rules, and payment terminal inspections at their store |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer device content (photos, messages, health, location, files); device passcodes; recovered data; background check reports; card data (which must never be stored) | Minimum collection; access only as the job requires; encrypted at rest and in transit; retention limits below |
| **Confidential** | Customer records and tickets, business account data, payroll, contracts, security documents | Need-to-know; encrypted in transit |
| **Internal** | Procedures, schedules, parts pricing | Workforce only |
| **Public** | Website, price lists | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on company storage, including the lab storage array and bench PCs, and encrypted in transit. Recovered data must be delivered only by expiring secure link or on company-issued encrypted drives. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 **Collect less.** Staff must never ask for a customer's email or account password. A device passcode may be collected only when the repair cannot be tested without it, must be entered only in the SYS-01 restricted passcode field (never in notes or on paper tags), and is purged automatically when the device is released. (SC-28; SI-12; PR.DS-01)
4.4 **Customer data access standard.** Technicians may access a customer device's content only as far as the repair requires and the customer consented on the intake form, following the test checklist for that repair type (for example, open the camera app to test the camera, but do not open the photo library). Browsing, copying, photographing, or forwarding customer content is prohibited. Copying is allowed only for a data transfer or recovery service the customer ordered, and only to company encrypted storage. Bench sessions are logged. (AC-6; MP-7; PR.DS-10)
4.5 **Card data.** Card numbers and security codes may be entered only into the company's P2PE payment terminals. They must never be written on paper, typed into SYS-01 or any other system, or emailed. For phone payments, staff key the card number directly into a terminal during the call. Store Managers must keep a terminal list reconciled with the processor and inspect every terminal weekly for tampering, recording each inspection. (SI-12; CM-8; PE-6; PCI DSS 3.2.1, 3.3.1.2, 9.4.1, 9.5.1)
4.6 **Retention.** Recovered data must be deleted from the lab storage and delivery storage 30 days after delivery, unless the customer agrees in writing to a longer period (maximum 90 days). Data transfer caches on bench PCs must be wiped when the ticket closes. Ticket records are kept for 3 years after the last repair, then deleted. (SI-12; Fla. Stat. 501.171(8))
4.7 **Sanitization and disposal.** Devices and media leaving company custody for recycling, resale of company equipment, or return of loaners must be sanitized using the clear, purge, or destroy methods in NIST SP 800-88 Rev. 2, with the technique chosen for the media type. Each sanitized device must be verified and recorded on a certificate of sanitization (per SP 800-88 Rev. 2 section 4.6). The recycler's certificates must list serial numbers. Paper with customer or card data must be cross-cut shredded. Printed background check reports must be kept in the HR system only and shredded when no longer needed (16 CFR 682.3). (MP-6; ID.AM-08)
4.8 Backups of Restricted data must be encrypted, stored in a separate account with immutable retention, and restore-tested quarterly. Retention limits in 4.6 apply to backups as they age out. (CP-9; PR.DS-11)
4.9 Restricted and Confidential data must not be entered into AI tools unless the tool is on the approved list and its vendor has signed data-use terms (see P10 and POL-05). (SA-9)
4.10 Customer devices must be kept in locked storage when not on a bench, and released only after the customer shows photo ID or gives the one-time code sent to the phone on file. (MP-4; PE-3)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Misuse of a customer's device data is treated as serious misconduct. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the log reviews in POL-03.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; customer data access standard and repair test checklists; sanitization standard and certificate form; P10 approved AI tools list
