# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group CISO for cardholder data |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after significant changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9, SR-6 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory basis | PCI DSS 3.2 to 3.5, 4.2, 9.4, 12.10.7; 16 CFR 314.4(c)(2), (c)(3), (c)(6); N51-R04 (28 CFR Part 202) |
| Division supplements | Payment Processing: dispute evidence and case files. Software: storefront consumer data and gateway logs. Merchant Consulting: client files and dispute evidence until migration |

## 1. Purpose
Classify group information by sensitivity and set handling rules so that cardholder data stays inside a cardholder data environment and all customer information is protected, kept only as long as needed, and disposed of securely.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms (the group data platform, email) and in an acquired company's systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the retention schedule, and data use rules |
| Group CISO | Owns cardholder data handling rules and PAN discovery |
| Data owners | Classify data; approve feeds and access |
| Group data platform director | Enforces tokens-only and PAN blocking on the data platform |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (cardholder data, sensitive authentication data, keys, credentials, customer information under the Safeguards Rule, merchant owner identity and bank data), **Confidential** (merchant and client business data), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. PAN may be stored only in a token vault inside a cardholder data environment. Everywhere else, only tokens or truncated PAN may be used. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI DSS 3.5, 4.2; 314.4(c)(3))

4.3 **No PAN by email, chat, or tickets.** The group must not ask for or accept card numbers by email, chat, or tickets. Dispute evidence and other documents with card data must be received through the evidence upload portal into the dispute platform, which masks PAN on upload. PAN that arrives anyway must be purged and recorded under POL-03 4.12. (AC-4; PR.DS-10; PCI DSS 3.2.1, 12.10.7)

4.4 Full PAN may be displayed only to roles with a documented business need; all other displays must mask PAN. (AC-3; PCI DSS 3.4.1)

4.5 **Retention.** Information must be kept according to the group retention schedule. Dispute case files must be purged 90 days after the dispute closes unless a card network rule or legal hold requires longer. Customer information must be disposed of no later than two years after its last use in providing a product or service, unless it is needed for business operations or required by law. The schedule must be reviewed every year. (SI-12; MP-6; 314.4(c)(6); PCI DSS 3.2.1)

4.6 **Shared data platforms** (SYS-G4) must hold tokens only. Every ingestion path, including application and debug logs, must pass through PAN blocking, and the platform and email must be scanned for PAN every week. (AC-4; CM-8; PR.DS-10; 314.4(c)(2))

4.7 Backups of Restricted information must be immutable, held with a different provider or site from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.8 Media holding Restricted information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; PCI DSS 9.4.7)

4.9 Restricted or Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard with no-training and retention terms. (SA-9; PL-4)

4.10 **Bulk sensitive data.** No vendor, employee, or app developer arrangement may give a country of concern or a covered person access to bulk U.S. sensitive personal data or government-related data. Vendor and app developer onboarding must screen for covered persons. (SR-6; SA-9; 28 CFR Part 202)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, SI-12, CM-8), weekly PAN discovery results, and the ROCs.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit PAN storage outside a cardholder data environment.

## 7. Related documents
POL-01; POL-02; POL-03; `division-supplements.md`; P02 SSP; P10 Group AI Standard; group retention schedule.
