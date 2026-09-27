# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory basis | 12 CFR 30 App. B II.B, III.C.1.c, III.C.1.h, III.C.4; 12 CFR 225 App. F III.C.1.c, III.C.1.h; state breach notification laws (generic) |
| Division supplements | Banking: SAR confidentiality and customer information. Financial Software: client institution data and conversion files. Commercial Real Estate: guarantor financial statements and closing packages |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that customer information, client institution data, and guarantor information are protected and used only as permitted.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including data held for client institutions on the digital banking platform and the data services platform.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, handling rules, and the data inventory |
| Data owners | Classify data sets; approve sharing and access |
| Client risk and assurance director | Makes sure client data is handled as client contracts require |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (customer information, client institution customer data, guarantor personal information, SAR information, credentials, keys, and payment instructions), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. Each client tenant's data must use its own key. (SC-28; SC-8; PR.DS-01; PR.DS-02; App. B III.C.1.c)

4.3 **Client institution data** may be used only to provide the contracted service. It must not be copied into group analytics, used to train models, or combined with other clients' data without the client's written agreement. (AC-4; AC-21; PT-2; PR.DS-10)

4.4 **Guarantor and closing information** must be stored in the CRE loan system, not in mailboxes or file shares, from 2027-03-31, with the guarantor's state of residence recorded so breach duties can be sized quickly. (CM-8; SI-12; ID.AM-07)

4.5 **Bulk transfers** (core conversions, client data extracts) must use the group secure file exchange. Restricted bulk data must never be sent by email. (AC-4; SC-8)

4.6 Backups of Restricted information must be immutable, held with a different provider or site from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11; App. B III.C.1.h)

4.7 Media holding Restricted information must be sanitized or destroyed with a serial-number certificate. (MP-6; ID.AM-08; App. B II.B.4; III.C.4)

4.8 Information must be retained per the group records schedule. Client conversion files must be deleted within 30 days of go-live with a certificate to the client. (SI-12)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and its contract prohibits training on group or client data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the P07 assessment, the data inventory, and mailbox retention reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard.
