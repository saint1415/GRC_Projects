# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Contracts Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-21, MP-1, MP-2, MP-3, MP-4, MP-5, MP-6, SC-8, SC-28, CP-9, CM-12, SI-12, SR-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Contract and legal drivers | 32 CFR Part 2002 and GSA Order PBS 3490.3 (CUI); FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(2) and (8); Fla. Stat. 119.071(3)(a) and 119.0701 |
| Supporting standards | STD-08 Encryption and key management; STD-10 CUI handling |

## 1. Purpose
Classify the information the company holds by sensitivity and set handling rules, so that building security information, CUI, cardholder data, and face templates get protection that matches the harm a disclosure would cause.

## 2. Scope
All workforce members and subcontractors, and all information the company creates or receives, in any form (electronic, paper, drawings in a job box, photos on a phone).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Contracts Director | Owns classification; CUI program lead; keeps the data location register |
| IT Director's team | Implements encryption, storage restrictions, data loss rules, backup, and disposal controls |
| Security Systems Manager | Retention and deletion settings for cardholder data, video exports, and face templates |
| Program managers | Handling at site offices (locked storage, shred bins) |
| General Counsel | Public records questions; routing of requests to customer custodians |
| All workforce | Label and handle information under this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | GSA CUI drawings; security system plans, door schedules, and camera layouts; cardholder records; face templates; video exports; device credentials and broker recordings | Encrypted at rest and in transit; named access only; stored only in approved locations; never on personal devices or in unapproved AI tools |
| **Confidential** | Other building drawings, work orders and asset lists (including FCI), contracts, payroll, employee and applicant data | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures, training material | Workforce only |
| **Public** | Website, marketing | No restriction |

(RA-2; ID.AM-07)

4.2 **CUI from GSA** must keep its CUI marking on every copy and derivative (32 CFR 2002.20). It must be stored only in the CUI library, shared only with subcontractors that signed CUI handling terms and need it for the work, and sent only through the library's secure links. Email attachments marked CUI are blocked. Paper CUI must be kept in locked storage and carried in an opaque, marked envelope. (MP-3; MP-4; AC-21; SC-8)
4.3 **Security system plans** for state, county, and city buildings are exempt from public disclosure under Fla. Stat. 119.071(3)(a). They must be handled as Restricted and disclosed only as that statute allows. (AC-21)
4.4 **Public records requests.** Staff must not answer public records requests themselves. A request to inspect or copy records about a public agency contract must be made to the agency (Fla. Stat. 119.0701(3)(a)); any request that reaches the company goes to General Counsel, who routes it to the customer's records custodian named in the contract. (SI-12)
4.5 Restricted data must be encrypted at rest on every device and service and encrypted in transit. Where a building protocol (for example BACnet) cannot encrypt, the network segment must be isolated instead. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.6 The Contracts Director must keep a register of where state, county, city, and federal information is stored, including copies held by subcontractors. (CM-12; ID.AM-07)
4.7 Media and devices holding Restricted or Confidential data must be wiped for reuse or destroyed with a record. Paper with personal information or Restricted content must be shredded, including at site offices (Fla. Stat. 501.171(8)). Copier and printer storage must be wiped at lease return. Controller and NVR drives removed from customer sites must be wiped or handed to the customer with a signed receipt. (MP-6; ID.AM-08; SR-12)
4.8 Backups of IFOP data must be encrypted, kept in the separate backup account and region, protected from alteration, and restore-tested quarterly. Controller programs must be backed up to the central repository, not only to laptops. (CP-9; PR.DS-11)
4.9 Restricted data must not be entered into AI tools unless the tool is on the approved list (P10 and POL-05). Face templates are created only for enrolled, consenting employees at approved entrances and deleted within 30 days after a person withdraws or leaves. (SI-12)
4.10 Customer data is kept for the contract term and then transferred to the customer or destroyed as the contract and Fla. Stat. 119.0701(2)(b)4. require. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual control assessment (P07), quarterly checks of the CUI library, and the monthly face template deletion check.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 section 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; STD-08; STD-10; P10 AI approved-tools list; GSA Order PBS 3490.3 CHGE 1; customer contracts
