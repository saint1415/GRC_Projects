# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group CMMC program director for CUI and FCI |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, MP-2, MP-6, MP-7, SC-8, SC-13, SC-28, CP-9, SI-12, PT-2, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory drivers | N42-R03 (SP 800-171 R2 3.1.3, 3.8.1 to 3.8.9, 3.13.8, 3.13.11, 3.13.16); 32 CFR 2002.14(g); N42-R04 (52.204-21(b)(1)(vii)); N44-45-R01 (PCI DSS v4.0.1 Req. 3, 4); N44-45-R08 (15 U.S.C. 45f(a)(3)-(4)); N42-R08 (Cal. Civ. Code 1798.150) |
| Division supplements | IT Distribution: CUI handling in the FFE; ITAD sanitization. Logistics: 3PL client data. Online Retail: cardholder data, call recordings, seller compliance data |

## 1. Purpose
Classify group information by sensitivity and by the rules that govern it, and set handling rules so each class stays in the systems approved for it.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including information on customer and client devices handled by Lifecycle Services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns the classes and personal information rules |
| Group CMMC program director | Owns CUI and FCI handling rules and the list of systems approved for each |
| Online Retail PCI compliance manager | Owns cardholder data rules and the PCI DSS scope |
| Data owners | Classify and label data; approve sharing |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted-Federal** (CUI and FCI), **Restricted-Payment** (cardholder data and sensitive authentication data), **Restricted** (personal information, seller compliance data, 3PL client data, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 **CUI** may be stored, processed, or transmitted only in the Federal Fulfillment Enclave and the government-community collaboration tenant. It must not be attached to commercial ERP records, sent from the commercial tenant, or entered into any AI tool not approved for CUI. (AC-4; AC-21; 3.1.3, 3.1.20)

4.3 **FCI** may be processed only in systems that meet FAR 52.204-21 (the ERP, EDI hub, WMS, and FFE) and in vendor services whose contracts carry the same safeguards. (SA-9; 52.204-21(b)(1))

4.4 **Cardholder data** must not be stored by the group. Card numbers must be entered only into the payment service provider's hosted fields or virtual terminal. Call recordings must not capture card numbers or security codes; recording must pause automatically during card entry. (SI-12; SC-28; PCI DSS 3.2.1, 3.3.1)

4.5 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys; CUI must use FIPS-validated cryptography. (SC-28; SC-8; SC-13; PR.DS-01; PR.DS-02; 3.13.11)

4.6 **Seller compliance data** collected under the INFORM Consumers Act must be used only for compliance and must be visible only to the marketplace verification team. (PT-2; AC-3; 15 U.S.C. 45f(a)(3)-(4))

4.7 Backups of Restricted information must be immutable, held in a different account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11; 3.8.9)

4.8 Media and devices holding Restricted information, including customer devices received by Lifecycle Services, must be sanitized under NIST SP 800-88 with documented verification sampling on every processing line, and a certificate must be issued. (MP-6; ID.AM-08; 3.8.3)

4.9 Removable storage must be blocked on managed endpoints except issued encrypted drives, and blocked entirely on FFE workstations. (MP-7; 3.8.7, 3.8.8)

4.10 Information must be retained per the group retention schedule. Call recordings must be kept no longer than 90 days unless a dispute hold applies. (SI-12)

4.11 Restricted, Restricted-Federal, and Restricted-Payment information must not be entered into any AI tool unless the tool is approved for that class under the Group AI Standard. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 5. Compliance is checked through the P07 assessment (AC-3, AC-4, AC-20, MP-6, SI-12), the CUI discovery scan each quarter, and PCI DSS scope confirmation.

## 6. Exceptions
Exceptions follow POL-01 section 4.14.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard.
