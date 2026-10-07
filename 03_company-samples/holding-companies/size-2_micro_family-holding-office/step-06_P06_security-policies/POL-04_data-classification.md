# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Family Office Director (Qualified Individual) |
| Approved by | Principal, 2026-09-18 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, CM-12, MP-6, SC-8, SC-28, CP-9, CP-4, SA-4, SI-12 |
| CSF 2.0 | ID.AM-02, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulation | 16 CFR 314.4(c)(2), (c)(3), (c)(4), (c)(6); Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Sort office information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and say how long information is kept and how it is destroyed.

## 2. Scope
All workforce members and all office information in any form: in SYS-01 to SYS-11, in email, on paper, on personal phones that hold office email, and in any vendor's system. It covers information about the family, the subsidiaries, household and office employees, and the office itself.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Family Office Director | Owns this policy; keeps the data inventory; approves new tools (4.6) |
| Controller | Owns the retention schedule and the disposal log |
| Executive Assistant | Files family documents in the vault under 4.3 |
| MSP | Encryption, backups, restore tests, and device wiping, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Office information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Family members' SSNs, tax returns, passports, driver licenses, estate plans, health care directives, medical bills, account numbers with access details, travel plans and home security details; household and office employees' SSNs and bank accounts; passwords, MFA codes, security keys, bank tokens; private deal documents; subsidiary board packs | Only in the approved locations in 4.3; need-to-know access by family branch or subsidiary; encrypted at rest and in transit; never in personal accounts or unapproved AI tools; never sent as an email attachment outside the office |
| **Internal** | Subsidiary monthly packages, consolidated reports, office contracts, security documents, schedules without family details | Workforce, guests for their own subsidiary, and approved vendors only; encrypted in transit |
| **Public** | Office address and main phone number | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored and whenever it leaves the office's systems. Laptops use full-disk encryption; personal phones may hold office email only under the app protection policy (POL-02 B.7). If encryption is infeasible anywhere, the Qualified Individual must approve compensating controls in writing. (SC-28; SC-8; PR.DS-01; PR.DS-02; 16 CFR 314.4(c)(3))

4.3 **Where Restricted information may live:**
- Family identity documents, tax returns, estate plans, directives, and medical bills: **only in the vault (SYS-07)**, in each family member's folder, and in the bill pay platform (SYS-03) for bills being paid.
- Family investment information: SYS-06 and the custodians' portals.
- Payroll data: SYS-04. Partnership tax data: SYS-11.
- Subsidiary board packs: the Subsidiaries site, in that subsidiary's folder.
- Working copies in SYS-02 must be deleted within 30 days once filed.
Sharing with the CPA firm and counsel uses vault share links that expire within 30 days. (AC-3; 16 CFR 314.4(c)(1)(ii))

4.4 The Family Office Director must keep a data inventory that lists, for each Restricted category, the systems and folders that hold it and who can reach it, and must update it when a system or vendor changes. (CM-12; CM-8; ID.AM-07; 16 CFR 314.4(c)(2))

4.5 **Retention and disposal.** The Controller must keep a retention schedule approved by counsel and the CPA firm. Customer information must be disposed of no later than two years after it was last used to serve the family member it relates to, unless it is needed for business operations, required by law, or cannot feasibly be removed (16 CFR 314.4(c)(6)(i)). Paper goes to the locked shredding bin; electronic records are deleted from every system, including working copies; devices are wiped by the MSP before reuse or disposal. Each disposal is recorded in the disposal log. The schedule is reviewed every August. (SI-12; MP-6; ID.AM-08; Fla. Stat. 501.171(8))

4.6 **New tools and AI.** No new SaaS tool, browser extension, or AI tool may receive Restricted or Internal information until the Family Office Director has completed the new-tool checklist (security evidence, data use and training terms, MFA, deletion) and added it to the approved-tools list. The approved-tools list today: SYS-01 to SYS-07 and SYS-11. The SYS-10 AI assistant is approved only for the users and conditions set in P10 and only after those conditions are met. Free public AI chatbots are not approved for any office information. (SA-4; PL-4; 16 CFR 314.4(c)(4))

4.7 **Backups.** Mail and files in SYS-02 must be backed up to an independent service in a separate account; SYS-11 snapshots must be copied to a separate account. A restore must be tested every quarter and recorded. (CP-9; CP-4; PR.DS-11)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. The Family Office Director checks compliance through the quarterly access review, the disposal log, restore test records, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; data inventory; retention schedule and disposal log; approved-tools list; P10 AI risk assessment
