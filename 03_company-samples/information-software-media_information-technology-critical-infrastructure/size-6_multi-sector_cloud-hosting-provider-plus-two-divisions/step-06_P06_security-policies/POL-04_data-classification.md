# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, SC-8, SC-13, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory references | FedRAMP CMU and MAS rules (G1); NIST SP 800-171 Rev. 2, 3.13.11 (CUI); 16 CFR 314.4(c)(3) and (c)(6); PCI DSS v4.0.1 Requirements 3 and 4; 45 CFR 164.312(a)(2)(iv) and (e) |
| Division supplements | Cloud Hosting: G1 data and metadata. Managed IT: CUI and client credentials. Payment Processing: account data and consumer information |

## 1. Purpose
Classify group information by sensitivity and by the regulated environment it belongs to, and set handling rules so that federal customer data, CUI, cardholder data, and customer data stay inside their documented scopes.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including logs, alerts, and metadata.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns the classes and handling rules |
| Owners of regulated environments | Define what may leave G1, the CDE, and the CUI enclave |
| System owners | Classify their data and apply handling rules |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (federal customer data and metadata in G1, CUI and covered defense information, cardholder and other account data, consumer nonpublic personal information, PHI, customer and client data, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with group-managed keys. Federal customer data in G1 and CUI must be protected with FIPS 140 validated cryptographic modules, and the modules must be documented. (SC-28; SC-8; SC-13; PR.DS-01; PR.DS-02)

4.3 **Environment boundaries.** Federal customer data stays in G1; CUI stays in the CUI enclave; cardholder data stays in the CDE. None of them may be copied to another environment, including another division's, without the environment owner's written approval and an update to its documented scope. (AC-4; PR.DS-10)

4.4 **Logs and alert context.** Logs and alerts that leave a regulated environment (for example, to the group SIEM or to an AI service) must be minimized. Alert context sent to any third-party service must not include G1 resource identifiers, CUI, or account data unless that service is inside the relevant documented scope. (AC-4; SA-9)

4.5 Backups of Restricted information must be immutable, held at external provider X with a separate backup identity, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.6 Media holding Restricted information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08)

4.7 Information must be retained per the group retention schedule. Consumer and customer information held by Payment Processing must be disposed of no later than two years after its last use unless retention is required by law or necessary for business (16 CFR 314.4(c)(6)). (SI-12)

4.8 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard for that class of data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, SC-13, CM-8) and the external assessments.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard.
