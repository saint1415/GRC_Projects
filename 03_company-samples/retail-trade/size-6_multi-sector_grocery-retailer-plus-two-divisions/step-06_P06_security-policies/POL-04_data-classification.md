# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-8, CM-12, SC-8, SC-28, CP-9, MP-6, SI-12, PT-2, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory drivers | PCI DSS v4.0.1 Req. 3, 4, 9.4, 12.5.2, 12.10.7 (N44-45-R01); 16 CFR 314.4(c)(2), (c)(3), (c)(6) (N44-45-R03); 12 CFR 1022.21; 16 CFR 682.3; 21 CFR 1.361 |
| Division supplements | Grocery Retail: card data, EBT data, and loyalty data. Grocery Wholesale: traceability records and customer pricing. Financial Services: customer information, consumer reports, and affiliate sharing |

## 1. Purpose
Classify group information by sensitivity and by whose program governs it, and set handling rules so that card data stays inside the cardholder data environment and Financial Services customer information is protected wherever it is handled, including on other divisions' systems.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms and affiliate systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, permitted uses, and affiliate sharing rules |
| Data owners | Classify data, approve flows and access |
| Grocery Retail CISO | Owns the PCI scope document and quarterly data discovery |
| Financial Services CISO | Sets the protection standard for Financial Services customer information wherever it is handled |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (payment card data, Rewards Card numbers and codes, EBT data, other Financial Services customer information, consumer report information, credentials, and keys), **Confidential** (customer and loyalty data, independent grocer pricing, employee data), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit over external networks with approved algorithms and group-managed keys. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI DSS 3.5, 4.2; 16 CFR 314.4(c)(3))

4.3 **Card data stays in the CDE.** Full card numbers must never be stored outside the systems listed in the PCI scope document. Data discovery must run at least quarterly across the CDE and every file share, mailbox store, and data platform that could receive card data. Any card number found outside the CDE must be handled as an incident and deleted or truncated within 30 days. (CM-12; SI-12; PCI DSS 3.2.1, 12.5.2, 12.10.7)

4.4 **Financial Services customer information on other divisions' systems.** Any division that collects or holds Financial Services customer information (for example, the Rewards Card field at checkout or card data in the CDP) does so on behalf of Financial Services, must follow the Financial Services protection standard, and must list the flow in the Financial Services data inventory. (AC-4; CM-8; PR.DS-10; 16 CFR 314.4(c)(2))

4.5 **Affiliate marketing.** Eligibility information received from an affiliate (for example, Rewards Card transaction data) may be used for marketing solicitations only where the consumer received notice and has not opted out, or a documented exception applies (12 CFR 1022.21(c)). Opt-outs must reach every system that builds audiences within 1 business day. (AC-21; PT-2; PR.DS-10)

4.6 Backups of Restricted and Confidential information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. Records that FDA may request must be retrievable within 24 hours from backups. (CP-9; PR.DS-11; 21 CFR 1.361)

4.7 Media holding Restricted information, including consumer report information, must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; PCI DSS 9.4.7; 16 CFR 682.3)

4.8 Information must be retained per the group retention schedule. Financial Services customer information must be disposed of no later than two years after last use unless the schedule records a business or legal need. Staging copies must be purged within 7 days. (SI-12; 16 CFR 314.4(c)(6))

4.9 Restricted or Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and its contract prohibits training on group data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, AC-21, CM-8, CM-12, SC-28), quarterly discovery reports, and the QSA ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit storage of full card numbers outside the CDE.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the EPP; PCI scope document; P10 Group AI Standard.
