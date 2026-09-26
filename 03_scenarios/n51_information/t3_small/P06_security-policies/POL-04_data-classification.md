# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | COO (privacy lead) |
| Approved by | Chief Executive Officer |
| Effective date | 2026-09-22 (replaces the December 2025 policy adopted for the SOC 2 Type 1) |
| Review cycle | Annually (next review 2027-09-22), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, SI-12, CP-9, SA-3(2), PT-2, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Also supports | SOC 2 C1.1, C1.2, CC6.5, CC6.7, A1.2; DPA use, deletion, and sub-processor terms; CCPA service-provider terms (N51-R03) |

## 1. Purpose
Classify company and customer information by sensitivity and set handling rules, so protection matches the harm a disclosure would cause and customer data is used only as the DPA allows.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), whether they work in the Florida office or remotely. Covers all company systems and data, including the Workforce Scheduling Platform (WSP), the staging environment, the source repository and CI/CD pipeline, corporate SaaS, laptops, and systems that sub-processors operate for the company. It applies to customer data (customer worker data the company processes as a service provider under the DPA) and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| COO (privacy lead) | Owns classification, the data inventory, and the data-use register; approves new uses of customer data |
| Platform Engineering Lead | Implements encryption, backup, and deletion controls |
| Engineering Manager | Keeps customer data out of logs and non-production environments |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer worker data in the WSP (names, contact details, schedules, time punches, pay rates), payroll export files, credentials, access keys, and secrets | Production and approved sub-processors only; encrypted at rest and in transit; access per POL-02 |
| **Confidential** | Company employee records, customer contracts, source code, security documents, SOC 2 reports | Encrypted in transit; need to know; SOC 2 reports shared under NDA |
| **Internal** | Procedures, internal plans, non-sensitive tickets | Workforce only |
| **Public** | Website, public status page, public sub-processor list | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted and Confidential data must be encrypted at rest and in transit (TLS 1.2 or higher). (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.3 Restricted customer data may be stored only in the production environment and at sub-processors listed in the DPA. It must not be copied to staging, development, laptops, chat, tickets (beyond what a customer attaches), or personal accounts. Test data must be synthetic or masked. (SA-3(2); PR.DS-01)
4.4 The COO must keep an inventory of where customer data is stored and which sub-processors receive it, and a data-use register of each purpose. A new feature or sub-processor may not use customer data until the privacy lead approves its entry. (CM-8; PT-2; ID.AM-07)
4.5 Customer data may be used only to provide the service as the DPA describes. It may not be used to train AI models, and it may be sent to the AI model provider only under a signed DPA with no retention or training, and only the minimum data the feature needs (no worker names). (PT-2; SA-9)
4.6 **Retention and deletion.** Customer data must be deleted within 90 days after a customer's contract ends, with a deletion record kept. Application logs must not contain worker names, phone numbers, or email addresses. Application logs are kept 30 days and audit logs 1 year (POL-02 4.9). (SI-12; ID.AM-08)
4.7 **Backups.** Backups of customer data must be encrypted, copied to a separate backup account with write-once retention that production administrators cannot delete, and restore-tested at least every 6 months against the BIA recovery objectives (P05). (CP-9; PR.DS-11)
4.8 Laptops must be wiped through device management before reuse, and retired laptops must go to a certified recycler that provides certificates of destruction. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the SOC 2 examination (P09), and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level set in POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; customer DPA and sub-processor list; data inventory and data-use register; P10 AI risk assessment
