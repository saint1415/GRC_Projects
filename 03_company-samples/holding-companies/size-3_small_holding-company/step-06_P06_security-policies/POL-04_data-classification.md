# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC and its subsidiaries |
| Policy ID | POL-04 |
| Owner | CFO |
| Approved by | CEO |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after an acquisition, a major change, or an incident |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-28, SI-12, CP-9, AC-21 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |

## 1. Purpose
Classify group information by sensitivity and set handling rules so protection matches the harm a disclosure would cause, including harm to another company in the group.

## 2. Scope
All workforce members (owners, managers, employees, contractors, and temporary staff) of Cris Santos Company, LLC and each subsidiary, at every site and when working remotely. Covers all systems and data the group owns or uses, including the Shared Corporate Services Platform, each subsidiary's own systems, and systems that service providers run for the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CFO | Owns classification; approves new uses of Restricted data |
| Information owners (Controller, HR Director, Treasury and Payments Analyst, Finance President, Corporate Development Director) | Classify their data; approve access |
| IT Manager | Implements encryption, labels, backup, and disposal controls; keeps the data inventory |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Finance customer information (SSNs, bank accounts, credit reports, loan files); ACH files; employee SSNs and bank details; benefits enrollment data; bank and system credentials; material non-public acquisition information | Encrypted at rest and in transit; access approved by the information owner; labeled; approved systems only; no anonymous or all-employee sharing |
| **Confidential** | Financial statements before release, lender reports, contracts, pricing, security documents | Encrypted in transit; need-to-know; internal sharing only |
| **Internal** | Procedures, schedules, org charts | Workforce only |
| **Public** | Websites, marketing | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit over external networks. ACH and other bank files must be encrypted with a group-managed key and readable only by the named treasury staff and one administrator. Any exception needs the Qualified Individual's written approval of compensating controls. (SC-28; SC-8; SC-12; PR.DS-01; PR.DS-02; 314.4(c)(3))
4.3 One subsidiary's Restricted data must not be shared with another subsidiary's staff unless the owning President approves. Collaboration sites holding Restricted data must carry a Restricted label, which blocks anonymous links, all-employee access, and AI assistant retrieval. (AC-21; AC-3)
4.4 The IT Manager must keep an inventory of where Restricted data is stored and which suppliers receive it, and update it at least annually. (ID.AM-07; CM-12; 314.4(c)(2))
4.5 **Retention and disposal.** Information must be kept only as long as the retention schedule allows. ACH files must be deleted 90 days after settlement. Finance customer information must be disposed of no later than two years after it was last used to serve the customer, unless the schedule records a legal or business reason to keep it. Disposal must make the data unreadable. The schedule must be reviewed each year. (SI-12; MP-6; ID.AM-08; 314.4(c)(6); Fla. Stat. 501.171(8))
4.6 Backups of Restricted data must be encrypted, stored in a separate account and region, protected from alteration or deletion, and restore-tested quarterly. Email and files must be backed up independently of the provider. (CP-9; PR.DS-11)
4.7 Restricted data must not be entered into AI tools or other services unless the tool is on the approved list and the purpose is approved (see POL-05 and P10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the right level under POL-01 4.5, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; retention schedule; data inventory; P10 AI approved-tools list
