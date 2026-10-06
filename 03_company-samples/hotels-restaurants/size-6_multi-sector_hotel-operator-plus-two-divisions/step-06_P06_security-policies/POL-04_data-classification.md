# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, PT-5, AC-4, CM-8, CM-12, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | PCI DSS Requirements 3 and 4 (N72-R01, N71-R04, N53-R04); 16 CFR 314.4(c)(3) and (c)(6) (N53-R01); 16 CFR 312.10 (N71-R06); 16 CFR 682.3 (N72-R03); Fla. Stat. 501.171(8), 509.101(2), 721.13(12)(c) |
| Division supplements | Hotels: guest register and identity documents. Attractions: biometric templates, children's information, location data. Vacation Ownership: customer information, consumer reports, owner bank data |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling, retention, and disposal rules so that each division's customers' information is used only for its stated purpose and kept no longer than needed.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms such as the guest profile hub (SYS-G5) and group payment services (SYS-G4).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the purpose catalog for SYS-G5, and the retention schedule |
| Data owners (division leads) | Classify datasets; approve uses and feeds |
| Group Director of Payments and PCI Compliance | Owns card data handling and discovery scans |
| Qualified Individual | Owns customer information handling for the finance subsidiary |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 **Classes.**
- **Restricted:** card data; bank account and routing numbers; Social Security numbers; government identity document numbers; consumer reports; biometric templates; children's personal information; precise location history; loan files.
- **Confidential:** guest, visitor, and owner profiles, stay and visit history, loyalty data, employee records, and non-public financial information.
- **Internal:** operational data with no personal information.
- **Public:** approved for publication.
(RA-2; ID.AM-07)

4.2 Restricted and Confidential information must be encrypted in transit over external networks and at rest. Card data must be protected with strong cryptography on any network transmission. Finance subsidiary customer information must be encrypted at rest and in transit unless the Qualified Individual approves compensating controls in writing. (SC-28; SC-8; PR.DS-01; PR.DS-02; Req 3.5, 4.2; 314.4(c)(3))

4.3 **Card data** may be stored only as tokens or inside SYS-G4. Card numbers must not be accepted or kept in email, chat, card authorization forms, or file shares; when discovered they must be purged and handled under POL-03. Security codes must never be stored after authorization. (CM-12; SI-12; Req 3.2, 3.3.1, 12.10.7)

4.4 **Purpose tags.** Every dataset in the guest profile hub must carry the division that collected it and the purposes stated in that division's privacy notice. Data collected by one division may be used by another (for example, hotel and park guest data for vacation ownership tours) only when the collecting division's notice clearly discloses that use. Finance subsidiary customer information must not be stored in the hub; owners' bank data stays tokenized in SYS-V3. (PT-2; PT-3; AC-4; PR.DS-10; 15 U.S.C. 45(a); 314.4(c)(1))

4.5 **Children's information** from the kids' club must be kept in its own store, disclosed to a third party only with separate verifiable parental consent and written assurances, and retained under the written children's data retention policy published in the online notice. (PT-2; SA-9; 312.5(a)(2), 312.8(c), 312.10)

4.6 **Retention schedule** (minimums are legal floors, not reasons to keep data longer):
| Information | Keep | Basis |
|---|---|---|
| Florida guest register (PMS) | At least 2 years | Fla. Stat. 509.101(2) |
| Identity document numbers captured at check-in | 30 days after checkout | Business need |
| Inactive guest and loyalty profiles | Delete after 7 years without activity | Business need; Fla. Stat. 501.171(8) |
| Finger-scan gate templates | 30 days after the pass or ticket expires | Business need; Fla. Stat. 501.171(8) |
| Kids' club child profiles | 12 months after last activity, or on a parent's request | 16 CFR 312.10 |
| Inventory reservation decision records (Florida plans) | 5 years from each determination | Fla. Stat. 721.13(12)(c) |
| Finance subsidiary customer information | No later than 2 years after last use for the customer, unless needed for business, required by law, or not feasible to target | 16 CFR 314.4(c)(6) |
| Declined credit applications and consumer reports | Per the finance subsidiary schedule (Regulation B and FCRA counsel review) | 16 CFR 682.3; 314.4(c)(6) |
(SI-12; ID.AM-08)

4.7 **Disposal** of Restricted information must use methods that make it unreadable, including consumer report information. Disposal vendors must certify destruction. (MP-6; ID.AM-08; 16 CFR 682.3)

4.8 Immutable backups must be kept in a separate cloud provider, with restore tests at least quarterly for group services and at least annually for each division system. (CP-9; PR.DS-11)

4.9 No Restricted or Confidential information may be entered into an AI tool unless the tool is on the approved list for that class (P10). (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked by quarterly card data discovery scans, retention job reports, and the P07 assessment (SC-28, SI-12).

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal retention limit or permit card data in email.

## 7. Related documents
POL-01; POL-02; POL-03; `division-supplements.md`; privacy notices of each division; P03 gap analyses.
