# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Controller |
| Approved by | General Manager (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-2, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9, CP-4, PT-3 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, GV.OC-03 |
| PCI DSS v4.0.1 (N71-R04) | 3.2, 3.3, 3.4, 4.2, 9.4 |
| Law | FTC Act Section 5 (N71-R05); Fla. Stat. 501.171(8) (disposal of customer records) |

## 1. Purpose
Tell everyone which company information needs the most protection and how to store, share, keep, and destroy it. The most important rule: **the company does not keep card numbers.**

## 2. Scope
All Cris Santos Company employees, owners, and temporary staff, and every contractor with access to company information, in any form: electronic, paper, or spoken (for example a phone order).

## 3. Classification levels
| Level | Examples | Core handling |
|---|---|---|
| **Prohibited to keep** | Full card numbers, card security codes, PINs, magnetic stripe or chip data | Never write down, type into email or chat, save, photograph, or record. Enter only into approved payment devices or the ticketing checkout, while the customer is present or on the line |
| **Restricted** | Patron records and exports, marketing lists, API keys and passwords, show settlements and artist bank details, employee records, CCTV footage | Company systems only; encrypted at rest and in transit; shared only through controlled links with expiry; access reviewed quarterly |
| **Internal** | Show holds calendar, event-day plans, vendor contracts | Company systems; not shared outside without a business need |
| **Public** | Published event calendar, published prices (with total price), press releases | No restrictions once approved for publication |

## 4. Policy statements
4.1 Data owners must classify the information their teams create using section 3. When unsure, treat it as Restricted. (RA-2; ID.AM-05)
4.2 Card numbers and card security codes must never be written, stored, emailed, or kept in any form, including paper phone-order notes. Phone payments must be keyed directly into an approved payment device while the caller is on the line. (SI-12; MP-2; PR.DS-01; PCI 3.2; 3.3)
4.3 Any paper found with card data must be cross-cut shredded at once, with a second person present, and reported under POL-03. (MP-6; PR.DS-01; PCI 9.4; Fla. Stat. 501.171(8))
4.4 Screens and reports must show no more than the last 4 digits of a card number. (AC-3; PR.DS-01; PCI 3.4)
4.5 Restricted data must be encrypted in transit and at rest. Patron exports must not be sent as email attachments or stored in publicly accessible storage. (SC-8; SC-28; PR.DS-01; PR.DS-02; PCI 4.2)
4.6 Patron data may be used only for purposes stated in the privacy notice. New uses, including new AI features, require a P10 review. (PT-3; GV.OC-03; 15 U.S.C. 45(a))
4.7 Retention: patron marketing exports 30 days; settlement records 7 years (finance); CCTV 30 days unless held for an incident; security logs 12 months (POL-03). Records past retention must be destroyed so they cannot be read or rebuilt. (SI-12; MP-6; ID.AM-07)
4.8 Restricted data in the cloud tenant must be backed up daily to a separate account with immutable retention, and restores must be tested every quarter. (CP-9; CP-4; PR.DS-11)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Writing down a card number or security code is a serious violation. Compliance is checked through the annual control assessment (P07) and spot checks at the box office.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may be granted to statement 4.2.

## 7. Related documents
POL-01; POL-02; POL-03; P03 Gap Analysis (Requirement 3 and 9.4 rows); Fla. Stat. 501.171
