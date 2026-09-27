# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Controller (retention and disposal); IT Manager (technical safeguards) |
| Approved by | COO |
| Effective date | 2026-09-21 |
| Review cycle | Annually (next review 2027-09-21), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| FTC Safeguards Rule (16 CFR 314) | 314.4(c)(2), (c)(3), (c)(6) |

## 1. Purpose
Classify company information by sensitivity and set handling, retention, and disposal rules so protection matches the harm a disclosure or an alteration would cause.

## 2. Scope
All Cris Santos Company workforce members: owners, employees, and the affiliated sales associates who work under the Broker of Record's license as independent contractors. Covers information in every form (electronic, paper, and on personal devices) and information held by service providers for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Controller | Owns the retention schedule and the annual purge; confirms legal retention periods with counsel |
| IT Manager (Qualified Individual) | Implements encryption, backup, and disposal controls; keeps the data inventory; approves any compensating control for encryption in writing |
| Closing Services Manager and Director of Property Management | Apply this policy to closing files and to tenant screening data |
| All workforce members | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer information under 16 CFR 314.2(d); Social Security, driver license, and passport numbers; bank account numbers and **wire instructions**; loan and payoff data; tenant consumer reports; passwords and MFA secrets | Encrypted at rest and in transit; approved systems only; never sent by ordinary email; wire instructions only through the Closing Communications Portal |
| **Confidential** | Contracts, commission data, owner and tenant ledgers, security documents | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, training material | Workforce only |
| **Public** | Listings, website content, marketing | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device, storage system, and service, and encrypted in transit over external networks. Where encryption is not feasible, the Qualified Individual must approve a compensating control in writing before the data is stored or sent. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))
4.3 Restricted data may be stored only in approved systems: the transaction platform, the closing software, the property management platform, the productivity suite (company accounts only), the Closing Communications Portal, and the backup vault. It must never be kept in personal email, personal cloud storage, or unmanaged device storage. (AC-3)
4.4 **Closing documents and wire instructions** must be delivered to clients only through the Closing Communications Portal. Contractor sales associates must not forward wire instructions. An email that must carry Social Security or account numbers must use the productivity suite's enforced encryption option. (SC-8; 314.4(c)(3))
4.5 The IT Manager must keep an inventory of where customer information is stored (systems, paper, and devices) and which service providers receive it, and update it at least annually. (CM-8; ID.AM-07; 314.4(c)(2))
4.6 **Retention and disposal.** The Controller must maintain a retention schedule. Customer information must be securely disposed of no later than two years after it was last used to provide a product or service to that customer, unless it is needed for business operations or another legitimate business purpose, the law requires a longer period, or targeted disposal is not reasonably feasible. Longer periods in the schedule must name their reason, for example the Florida duty to keep brokerage books, accounts, and records for at least 5 years (Fla. Stat. 475.5015) and title agency trust fund records (Fla. Stat. 626.8473(5)). (SI-12; 314.4(c)(6)(i))
4.7 The Controller must review the retention schedule every year and run an annual purge, to minimize unnecessary retention. (SI-12; ID.AM-08; 314.4(c)(6)(ii))
4.8 Paper with Restricted data must be kept locked and disposed of through the shredding vendor. Drives and devices must be wiped for reuse or destroyed by a vendor that issues a certificate of destruction. Disposal must make the information unreadable. (MP-4; MP-6; ID.AM-08; Fla. Stat. 501.171(8))
4.9 Backups of Restricted data must be encrypted, kept in a separate account from production with immutable retention, and restore-tested quarterly. Email and transaction platform data must have an independent backup. (CP-9; PR.DS-11)
4.10 Tenant screening reports are consumer reports. They may be used only for the rental decision they were obtained for and must be disposed of under 4.8 (16 CFR 682.3). Restricted data must not be entered into AI tools unless the tool is on the approved list (POL-05 4.8). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 4.7. Compliance is checked through the annual control assessment (P07) and the annual purge record.

## 6. Exceptions
Exceptions follow POL-01 4.6. They must be written, risk-rated, approved under POL-01 4.4, and expire within 12 months. An exception to 4.2 also needs the Qualified Individual's written approval of a compensating control.

## 7. Related documents
POL-01; POL-02; POL-05; retention schedule (due 2027-03-31); FTC Safeguards Rule 16 CFR 314.4(c)(3) and (c)(6); FCRA disposal rule 16 CFR Part 682; Fla. Stat. 475.5015 and 501.171(8)
