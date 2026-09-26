# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-12, SI-15, CM-12, AC-21, CP-9, CP-4, PT-3 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| PCI DSS v4.0.1 (N44-45-R01) | 3.1-3.4, 4.2, 9.4 |
| Law | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) (N44-45-R02); FACTA receipt truncation, 15 U.S.C. 1681c(g) (N44-45-R05) |

## 1. Purpose
Classify company information by sensitivity and set handling rules so that protection matches the harm a disclosure would cause. Keep card data out of company systems entirely.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and temporary staff) and contractors with access to company systems, including the marketing contractor. Covers the store, online ordering, and all systems and data, including systems that service providers operate for the company (storefront, payment processor, POS vendor, cloud provider, pricing engine vendor). It applies to cardholder data wherever it could appear, customer and loyalty member data, workforce data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns classification; implements encryption, backup, and disposal controls |
| E-commerce and Marketing Manager | Owner of customer, loyalty, and pricing data; approves new uses and new recipients |
| Store Manager | Front-end handling of receipts, card data, and customer contacts |
| All workforce and contractors | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Prohibited** | Full card numbers, security codes, PINs, magnetic stripe or chip data | Must never be written down, typed, stored, or sent by the company. Captured only on P2PE PIN pads or in the processor's payment form |
| **Restricted** | Loyalty member data, online account data, delivery addresses, order history, credentials, API keys, employee Social Security numbers | Encrypted at rest and in transit; minimum necessary; approved systems only |
| **Confidential** | Payroll, contracts, pricing strategy, security documents, SAQs | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures | Workforce only |
| **Public** | Website, weekly ad | No restriction |

(RA-2; ID.AM-07)

4.2 The company must not store full card numbers or sensitive authentication data anywhere. Card numbers received by email, chat, or on paper must be deleted or shredded the same day, and the customer told to use the payment form. (SI-12; PR.DS-01; PCI DSS 3.2; 3.3; 4.2)
4.3 Restricted data must be encrypted at rest and in transit. Restricted data must not be sent as email attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.4 Restricted data may be shared with a service provider only under a written agreement (POL-01 4.8), through an access-controlled share, and only the fields the purpose needs. Loyalty files for marketing must not include phone numbers or email addresses unless the E-commerce and Marketing Manager approves in writing. (AC-21; SA-9)
4.5 Customer and loyalty data may be used only for the purposes described in the privacy notice. Any new use, including new uses by the pricing and offers engine, must be approved by the E-commerce and Marketing Manager after a P10 review. (PT-3; FTC Act 45(a))
4.6 The IT Manager must keep an inventory of where Restricted data is stored and which providers receive it. (CM-12; ID.AM-07)
4.7 Loyalty exports must be deleted within 90 days. Other retention periods follow the retention schedule (due 2026-12-31). (SI-12)
4.8 Backups of Restricted data must be encrypted, kept in a separate cloud account with immutable retention, and restore-tested quarterly. (CP-9; CP-4; PR.DS-11)
4.9 Devices and media holding Restricted data must be wiped before reuse and destroyed by a vendor that provides a certificate when retired. (MP-6; ID.AM-08; PCI DSS 9.4)
4.10 Printed card receipts must show no more than the last 4 digits of the card number and no expiration date. A test receipt must be checked after every POS update. (SI-15; FACTA 15 U.S.C. 1681c(g))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.10. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the quarterly access reviews (POL-02 4.6), and the PCI DSS self-assessment each year.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), recorded in the risk register, and expire within 12 months. No exception may allow card numbers to be entered or stored outside the P2PE devices and the processor's payment form.

## 7. Related documents
POL-01; POL-05; data inventory; retention schedule (due 2026-12-31); P10 AI risk assessment
