# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office and Compliance Manager (Information Security Officer and CUI program lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, CM-12, AC-21, MP-3, MP-4, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Customer and legal drivers | County security exhibit; 32 CFR Part 2002 and GSA Order PBS 3490.3 CHGE 1 (CT-F CUI); FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(2) and (8); 119.071(3); 119.0701(2)(b) |

## 1. Purpose
Sort company and customer information by the harm its loss or disclosure would cause, and set simple handling rules for each level, including CUI, exempt security records, and face templates.

## 2. Scope
All workforce members of Cris Santos Company and all information the company holds in any form: in SYS-01, SYS-02, the suite, the CMMS, on laptops, tablets, phones, USB drives, paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office and Compliance Manager | Owns this policy; keeps the system and data inventory; approves new tools and AI features; runs the CUI program |
| Lead Controls Technician | Keeps the engineering repository and the restore tests |
| MSP | Encryption, suite backup, restore tests, and device wiping, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Cardholder records, badge photos, access history, entrance video, face templates; CUI drawings from the federal building; security system layouts, door schedules, and building drawings of customer buildings (exempt under Fla. Stat. 119.071(3)); controller programs and gateway configurations; passwords and MFA codes; employee SSNs and background check results | Only in approved locations (4.4); encrypted at rest and in transit; need to know; never in personal accounts or public AI tools |
| **Internal** | Work orders (including FCI), contracts, invoices, schedules, security documents | Workforce, customers, and approved vendors only; encrypted in transit |
| **Public** | Website, service brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **CUI.** CUI drawings from the federal building may be kept only in the restricted CUI folder, open to the 2 PIV holders, the owner, and the Office and Compliance Manager. Copies must keep GSA's CUI markings. CUI may be shared only with named recipients who need it for the contract, through suite sharing to a named account or encrypted email; "anyone with the link" sharing is blocked on the folder. Paper CUI is kept in the locked office or a locked van cabinet. Any mis-sharing is reported under POL-03. CUI handlers complete CUI training before access. (AC-3; AC-21; MP-3; MP-4; SC-8; 32 CFR Part 2002)

4.3 **Exempt security records.** Security system plans, door schedules, and building drawings of customer buildings are labeled "Exempt: Fla. Stat. 119.071(3)" and stored as Restricted. Any public records request is sent to the customer's custodian under POL-02 A.8. (MP-3; Fla. Stat. 119.071(3); 119.0701(2)(b))

4.4 Restricted information may be kept only in: SYS-01 (cardholder data, video, face templates), SYS-02 (point lists and graphics), the restricted folders of the suite (CUI, engineering repository, security records), the CMMS, and company laptops with full-disk encryption. USB drives must be company-issued and encrypted. (AC-3; SC-28; PR.DS-01)

4.5 The Office and Compliance Manager must keep a one-page inventory of every company device, gateway, and SaaS tenant, where Restricted information is stored, and which customer devices each gateway reaches, and update it when anything is added or removed. It is reconciled with the CMMS asset list every quarter. (CM-8; CM-12; ID.AM-01; ID.AM-07)

4.6 Before any new vendor, app, device, or product feature receives Restricted information, the Office and Compliance Manager must approve it, the vendor must meet POL-02 A.5, and it must be added to the inventory. (SA-9; GV.SC-05)

4.7 **AI tools and biometric features.** Restricted information may be entered only into AI tools on the approved list. No AI or biometric feature may be turned on in a customer system (including face verification in SYS-01) without an approved P10 assessment and the customer's written request. Face templates must be deleted within 30 days after a person withdraws or leaves. Public AI chatbots must never receive Restricted information. (SA-9; PL-4; SI-12)

4.8 **Engineering records and backups.** Controller programs, door schedules, gateway configurations, and monthly SYS-01 and SYS-02 configuration exports must be saved to the engineering repository in the suite within one business day of any change, so the suite backup (SYS-08) copies them. Copies on laptops are working copies only. The MSP restores a sample from SYS-08 every quarter, and the Lead Controls Technician restores 3 controller programs to a test controller every quarter, with written results. (CP-9; CP-4; PR.DS-11)

4.9 **Disposal.** Devices and media that held Restricted information or FCI must be wiped before reuse or destroyed with a certificate. Paper goes to the cross-cut shredder. Old cardholder exports are deleted monthly. The Office and Compliance Manager keeps a disposal log. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(8))

4.10 **Retention and contract end.** Customer data is kept only as long as the contract needs it, then returned or destroyed as the contract requires (the county: within 30 days after contract end), following POL-02 A.8. (SI-12; Fla. Stat. 119.0701(2)(b))

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the quarterly inventory reconciliation, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; system and data inventory; P04 cloud control map; P10 AI risk assessment; CT-F statement of work (CUI)
