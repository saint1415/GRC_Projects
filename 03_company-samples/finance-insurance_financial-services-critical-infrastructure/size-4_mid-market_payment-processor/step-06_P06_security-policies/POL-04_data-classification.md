# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Information Security, with the Chief Risk and Compliance Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-13, SC-28, SI-7, SI-12, AC-5 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| PCI DSS v4.0.1 | 3.1 to 3.7, 4.2, 9.4, 12.5.2, 12.10.7 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |
| Supporting standards | STD-05 Cryptography and key management standard |

## 1. Purpose
Classify company and customer information by sensitivity and set the handling rules for each class, so that card data stays in the CDE, is kept only as long as needed, and is protected wherever it is stored or sent.

## 2. Scope
All information the company creates, receives, stores, or transmits, in every system and on paper, including information held by service providers.

## 3. Classification levels
| Class | Examples | Where it may live |
|---|---|---|
| **Restricted** | Account data (PAN, cardholder name with PAN, expiry); sensitive authentication data (never stored after authorization); cryptographic keys | Only in a CDE (both token vaults, the settlement database and archive, the payment HSMs) |
| **Confidential** | Merchant owner NPI (SSNs, bank accounts); merchant funding files; security configurations and logs; model training data; contracts | Approved company systems with access control and encryption |
| **Internal** | Policies, procedures, internal reports | Company systems |
| **Public** | Published material | Anywhere |

## 4. Policy statements
4.1 Every system owner must classify the data in their system and record it in the data inventory, which is reviewed with the PCI DSS scope every six months. (RA-2; ID.AM-07; PCI DSS 12.5.2; 16 CFR 314.4(c)(2))

4.2 Restricted data may be stored, processed, or transmitted only in a CDE. Tokens, truncated PAN (first 6 and last 4 at most), or masked PAN must be used everywhere else. (SC-28; PR.DS-01; PCI DSS 3.4.1, 3.5.1)

4.3 **Sensitive authentication data** (card verification codes, full track data, PINs and PIN blocks) must never be stored after authorization, including in call recordings, chat transcripts, tickets, and logs. Contact center recordings must pause automatically when an agent opens a payment screen. (SI-12; PR.DS-01; PCI DSS 3.3.1)

4.4 Restricted data at rest must be encrypted with keys protected by payment HSMs or an equivalent key service approved by the Director of Information Security. Key management must use dual control and split knowledge on every platform, and keys must be replicated to the disaster recovery site after every rotation. (SC-12; SC-13; SC-28; AC-5; PR.DS-01; PCI DSS 3.6, 3.7; 16 CFR 314.4(c)(3))

4.5 Restricted and Confidential data in transit over external networks must use TLS 1.2 or higher or an approved private encrypted link. (SC-8; PR.DS-02; PCI DSS 4.2.1; 16 CFR 314.4(c)(3))

4.6 **Retention.** Full PAN may be kept only while a merchant's token is active or, in the settlement archive, for 18 months (the dispute window). Merchant onboarding files must be disposed of two years after the relationship ends unless a law or a sponsor agreement requires longer. A quarterly process must find and delete data held beyond its retention period. (SI-12; PR.DS-01; PCI DSS 3.2.1; 16 CFR 314.4(c)(6))

4.7 Media and records must be disposed of so that the data cannot be read or reconstructed: shredding under certificate for drives and tapes, and secure deletion for cloud storage. (MP-6; PR.DS-01; PCI DSS 9.4.7; Fla. Stat. 501.171(8))

4.8 **Model training and analytics data** must be tokenized and minimized. Every load into the data platform must pass an automated PAN block, and the data platform must be scanned for PAN monthly. (RA-2; PR.DS-01; PCI DSS 3.2.1)

4.9 PAN discovery scans must run at least monthly on stores outside the CDE where card data could appear: ticketing, chat, call recordings, email archives, the data warehouse, and shared drives. Findings are handled under POL-03 4.10. (RA-2; SI-12; PCI DSS 12.5.2, 12.10.7)

4.10 **Funding files** are Confidential with High integrity. They must be released under dual control (preparer and treasury approver), validated against control totals, and, from 2027-03-31, digitally signed with an HSM-held key before transfer to a sponsor bank. (SI-7; AC-5; PR.DS-01)

4.11 Restricted or Confidential data must not be entered into any AI tool that is not on the approved-tools list, and approved tools may receive only the classes their approval allows (STD-10; P10). (RA-2; PL-4)

## 5. Compliance and enforcement
Compliance is checked through the monthly PAN discovery results, the quarterly retention process, the annual assessment (P07), and the QSA's ROC. Violations are handled under POL-01 section 4.14.

## 6. Exceptions
Exceptions follow POL-01 section 4.13. No exception may allow sensitive authentication data to be stored after authorization.

## 7. Related documents
POL-01; POL-03; POL-05; STD-05; P03 gaps G-012 and G-013; P01 R-018, R-019, R-045, R-052
