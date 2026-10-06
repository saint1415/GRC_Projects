# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | General Counsel, with the IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, MP-4, MP-6, SC-8, SC-28, SI-12, SA-9 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10 |
| CISA CPG 2.0 and other rules | CPG 3.K; Fla. Stat. 501.171(2), (8); PCI DSS v4.0.1 Req. 3.2.1, 3.3.1.2, 9.4.1, 9.4.6 |
| Supporting standards | STD-04 Encryption and key management standard; STD-11 Records retention and disposal standard |

## 1. Purpose
Classify company information so that each kind gets protection, retention, and disposal that fit its sensitivity, and so that the company keeps personal information only as long as it needs it.

## 2. Scope
All information the company creates, receives, or holds, in any form, including information held for the company by vendors: tenant and visitor records, credentials and access history, video, building drawings and security plans, employee records, financial records, and card data.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Government ID numbers from visitor scans; employee Social Security numbers and bank details; tenant bank account data; face templates or other biometric data; card data (paper only, and only until it is eliminated) | Encrypted at rest and in transit; access by named role only; never in email or unapproved AI tools; shortest retention |
| **Confidential** | Credential records and badge photos; access history; video and analytics clips; tenant contact lists; leases; building drawings, security plans, and BAS programs; JV and lender reports | Encrypted at rest and in transit; role-based access; shared outside the company only under contract |
| **Internal** | Policies, procedures, work orders, internal communications | Company systems only |
| **Public** | Marketing materials, published building notices | No restriction |

## 4. Policy statements
4.1 Every system and data store must have an owner who assigns its classification and records it in the asset inventory. (RA-2; ID.AM-05)
4.2 Restricted and Confidential data must be encrypted at rest and in transit using STD-04 algorithms. Where an OT device cannot encrypt, segmentation and physical protection must compensate, and the exception must be recorded. (SC-28; SC-8; PR.DS-01; PR.DS-02; CPG 3.K)
4.3 **Card data.** Card numbers and security codes must be entered only into a P2PE terminal. They must never be written down, emailed, typed into any other system, or recorded. Phone bookings must be keyed directly into a terminal while the customer is on the line. (MP-4; SI-12; PCI DSS 3.2.1, 3.3.1.2)
4.4 **Retention.** Data must be kept only as long as STD-11 allows. Minimums set by this policy: visitor ID images and ID numbers deleted within 30 days (name, host, and visit time kept 1 year); video and analytics clips kept 30 days unless placed on legal hold; access history kept 1 year; credential records deleted 90 days after the credential is revoked. (SI-12; ID.AM-07; Fla. Stat. 501.171(2))
4.5 **Disposal.** Records containing personal information must be disposed of when no longer retained, by cross-cut shredding, certified destruction, or erasure that makes them unreadable, and media must be sanitized with a certificate before reuse or disposal. (MP-6; ID.AM-08; Fla. Stat. 501.171(8); PCI DSS 9.4.6)
4.6 **Building security information.** Building drawings, security plans, door schedules, and BAS programs are Confidential. They may be shared with contractors only under a contract with confidentiality terms, and only for the property and scope of work. (AC-3)
4.7 **Biometric data.** The company does not collect biometric data unless the COO approves a use case after a P10 assessment. Any approved use must have written notice, opt-in consent with a non-biometric alternative, a deletion schedule, and vendor terms that prohibit other uses. Face templates are treated as biometric data under Fla. Stat. 501.171 even where the law is unsettled. (SI-12; SA-9)
4.8 Restricted and Confidential data must not be entered into AI tools that are not on the approved list, and AI vendors must contractually agree not to use company data to train their models. (SA-9)
4.9 A legal hold issued by the General Counsel overrides retention and disposal rules for the records it names until it is released. (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the annual independent assessment (P07), the SAQ P2PE, and retention reports from the visitor management and video platforms.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may permit storing card security codes.

## 7. Related documents
POL-01; POL-05; STD-04; STD-11; P03 rows G-035 to G-042 and G-058 to G-062; P10 AI governance assessment
