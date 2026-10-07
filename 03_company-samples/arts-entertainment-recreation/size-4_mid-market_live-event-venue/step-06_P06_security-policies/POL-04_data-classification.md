# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | General Counsel (Privacy Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (new) |
| Review cycle | Annually (next review 2027-09-30), and after a new data use, a new managed venue, or an incident |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, SC-8, SC-28, SI-12, MP-6, PT-5, SA-9 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, GV.OC-03 |
| PCI DSS v4.0.1 (N71-R04) | 3.1 to 3.5; 4.2.2; 9.4; 12.5.2 |
| Law | Fla. Stat. 501.171(2) and (8); FTC Act Section 5, 15 U.S.C. 45(a) |
| Supporting standards | STD-08 Card data handling standard |

## 1. Purpose
Classify company data so that every person knows how to handle it, keep card data out of company systems entirely, and keep patron data only as long as it is needed.

## 2. Scope
All data the company creates, receives, or holds, in any form (electronic, paper, recordings), including data held for the company by service providers and data the company will hold for the County PAC.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| General Counsel | Owns this policy, the retention schedule, and the privacy notice |
| Data owners (business owners) | Classify their data; approve access and new uses |
| Security Manager | Runs quarterly card data discovery; sets technical protections |
| All workforce | Handle data according to its class |

## 4. Policy statements
4.1 **Classes.** All data must be classified as: **Restricted** (card numbers, security codes, card data in any form, passwords, API keys, and other secrets); **Confidential** (patron records, employee records, settlement and financial data, contracts, security logs, County PAC data); **Internal** (procedures, internal communications); or **Public** (published event information). (RA-2; ID.AM-05)
4.2 **Card data.** The company does not store card data. Card numbers may be entered only on validated P2PE devices or in the payment provider's own forms, never in the CRM, email, chat, spreadsheets, tickets, notes, or on paper. Card data must never be sent by end-user messaging. Security codes must never be recorded in any form. Premium installments must be charged only from the payment partner's card vault. (SI-12; PCI 3.2.1; 3.3.1; 4.2.2; 9.4)
4.3 **Patron data minimization.** Patron data copied out of the ticketing platform (the patron data platform, exports, segments) must be limited to what the stated purpose needs. Exports may be saved only to approved company storage and must expire within 30 days. (AC-3; SI-12; PR.DS-10)
4.4 Restricted and Confidential data must be encrypted in transit (TLS 1.2 or higher) and at rest with company-managed keys in cloud services and full-disk encryption on laptops. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.5 **Retention and disposal.** Data must be kept only as long as the retention schedule allows and then disposed of by shredding, secure erasure, or another method that makes it unreadable, including data held by service providers. Patron data in the patron data platform is kept for 5 years after the last purchase. (SI-12; MP-6; Fla. Stat. 501.171(8))
4.6 New uses of patron data, including new AI features and new marketing scores, require a review by the General Counsel and the Security Manager before go-live, and the privacy notice must be updated first when the use is new. (PT-5; GV.OC-03; 15 U.S.C. 45(a))
4.7 The Security Manager must run a card data discovery scan of the CRM, file shares, and mailboxes of staff who handle payments at least quarterly. Any card data found is handled as an incident under POL-03 section 4.10. (SI-12; PCI 12.5.2; 12.10.7)
4.8 Confidential data may be shared with a third party only under a written agreement with security and breach notice terms (POL-01 section 4.8). (SA-9)
4.9 **Event security data.** CCTV video is kept 30 days unless held for an investigation. Bot mitigation records of blocked sessions, flagged linked-account orders, and cancellation decisions are kept 12 months; other session records follow the vendor's 30-day default. Crowd analytics outputs contain counts only and are kept 90 days. (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Compliance is checked through quarterly card data discovery, the annual independent assessment (P07), and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow card data storage.

## 7. Related documents
POL-01; POL-03; POL-05; STD-08; retention schedule; privacy notice
