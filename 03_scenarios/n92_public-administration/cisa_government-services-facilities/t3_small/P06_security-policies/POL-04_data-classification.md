# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Contracts Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-21, MP-1, MP-2, MP-3, MP-4, MP-6, SC-1, SC-8, SC-28, CP-9, CM-12, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Contract and legal drivers | 32 CFR Part 2002 and GSA Order PBS 3490.3 (CUI); FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(2) and (8); Fla. Stat. 119.071(3) and 119.0701 |

## 1. Purpose
Classify the information the company holds by sensitivity and set handling rules, so that building security information, CUI, and personal information get protection that matches the harm a disclosure would cause.

## 2. Scope
All Cris Santos Company workforce members and subcontractors, and all information the company creates or receives, in any form (electronic, paper, drawings on a job box, photos on a phone).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Contracts Manager | Owns classification; CUI program lead; keeps the data location register |
| IT/OT Systems Administrator | Implements encryption, storage restrictions, backup, and disposal controls |
| Site Managers | Handling at site offices (locked storage, shred bins) |
| All workforce | Label and handle information under this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | GSA CUI drawings; security system plans, door schedules, and camera layouts for state and county buildings; cardholder records; face templates; credentials and device passwords | Encrypted at rest and in transit; named access only; stored only in approved locations; never on personal devices |
| **Confidential** | Other building drawings, work orders and asset lists (including FCI), contracts, payroll, employee data | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures, training material | Workforce only |
| **Public** | Website, marketing | No restriction |

(RA-2; ID.AM-07)
4.2 **CUI from GSA** must keep its CUI marking on every copy and derivative (32 CFR 2002.20). It must be stored only in the restricted CUI library, shared only with subcontractors that signed CUI handling terms and need it for the work, and sent only by encrypted transfer. Paper CUI must be kept in locked storage and carried in an opaque envelope. (MP-3; MP-4; AC-21; SC-8)
4.3 **Security system plans** for state and county buildings are exempt from public disclosure under Fla. Stat. 119.071(3)(a). They must be handled as Restricted and disclosed only as that statute allows (for example to the property owner or another agency for its official duties). (AC-21)
4.4 **Public records requests.** Staff must not answer public records requests themselves. Every request goes to the customer's records custodian named in the contract (Fla. Stat. 119.0701). (SI-12)
4.5 Restricted data must be encrypted at rest on every device and service and encrypted in transit. Where a building protocol (for example BACnet) cannot encrypt, the network segment must be isolated instead. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.6 The Contracts Manager must keep a register of where state, county, and federal information is stored and which subcontractors receive it. (CM-12; ID.AM-07)
4.7 Media and devices holding Restricted or Confidential data must be wiped for reuse or destroyed with a record. Paper with personal information or Restricted content must be shredded, including at site offices (Fla. Stat. 501.171(8)). Controller and NVR drives removed from customer sites must be wiped or handed to the customer with a signed receipt. (MP-6; ID.AM-08; SR-12)
4.8 Backups of company and FOTP data must be encrypted, kept in a separate account and region, protected from alteration, and restore-tested quarterly. Controller programs must be backed up to the central repository, not only to laptops. (CP-9; PR.DS-11)
4.9 Restricted data must not be entered into AI tools unless the tool is on the approved list (P10 and POL-05). Face templates are created only in the approved pilot and deleted within 30 days after a person opts out or leaves. (SI-12)
4.10 Customer data is kept for the contract term and then transferred to the customer or destroyed as the contract and Fla. Stat. 119.0701(2)(b)4 require. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07) and quarterly checks of the CUI library.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; GSA Order PBS 3490.3 CHGE 1; customer contracts
