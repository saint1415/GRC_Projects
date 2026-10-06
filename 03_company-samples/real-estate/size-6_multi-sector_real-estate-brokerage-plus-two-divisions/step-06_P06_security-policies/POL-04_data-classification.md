# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| FTC Safeguards Rule and other | 16 CFR 314.4(c)(2), (c)(3), (c)(6); FCRA disposal rule 16 CFR 682.3; RESPA 12 CFR 1024.15; state disposal laws (Fla. Stat. 501.171(8) worked example) |
| Division supplements | Brokerage: consumer reports and transaction files. Mortgage and Title: closing files and loan files. Homebuilding: buyer files and smart-home data |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each institution's customer information and each division's client data is used only for its permitted purpose and kept only as long as needed.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms such as the TMCC and the Group Data Platform.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the data sharing register, and the retention schedule |
| Data owners | Classify and tag datasets; approve feeds and sharing |
| System owners | Enforce tags, retention, and disposal in their systems |
| All workforce and contractor agents | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (customer information of Home Loans and Title, consumer reports, Social Security and account numbers, wire and payee instructions, identity documents, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit over external networks. Where encryption is infeasible, compensating controls must be approved in writing by the Qualified Individual. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.3 **Wire instructions** are Restricted and must be delivered to consumers only through the Closing Communications Portal. They must never be sent or forwarded by email or text message. (SC-8; AC-4; PR.DS-02)

4.4 **Affiliate sharing.** Customer information and client data may move between divisions only for a purpose recorded in the data sharing register, with the consent or other legal basis recorded, and with the Affiliated Business Arrangement Disclosure given where a referral is made (12 CFR 1024.15(b)(1)). Lead and file APIs must carry only the fields the register allows. (AC-21; PT-2; PT-3; PR.DS-10)

4.5 **Tagging on shared platforms.** Every dataset holding Restricted information on a shared platform must carry tags for the institution or division it belongs to and its permitted purpose. Safeguards Rule customer information must be stored in zones separate from brokerage-only data. Untagged datasets must not be queryable after 2027-03-31. (PT-3; CM-8; ID.AM-07)

4.6 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.7 Media holding Restricted information must be sanitized or destroyed with a certificate. Paper must be shredded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))

4.8 **Retention and disposal.** Customer information must be disposed of no later than two years after it was last used for the customer, unless needed for business operations or required by law (for example, state record-keeping rules for escrow and closing files), as stated in the group retention schedule. Consumer reports must be disposed of securely when the retention period ends. The schedule must be reviewed every year. (SI-12; MP-6; 314.4(c)(6)(i)-(ii); 16 CFR 682.3)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and covered by a contract that prohibits training on group data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, AC-21, SI-12) and data sharing register reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; TMCC SSP (P02); Group AI Standard (P10).
