# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Compliance and Privacy Officer, with the Product Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, SC-8, SC-12, SC-13, SC-28, MP-6, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | HIPAA 164.310(d), 164.312(a)(2)(iv), 164.312(e) (N62-R01); FD&C Act 524B(b)(2) (N31-33-R05); FDA premarket guidance Appendix 1 (cryptography; nonbinding) |
| Supporting standards | STD-08 Cryptography and key management; STD-05 AI use |

## 1. Purpose
Classify company and customer information so everyone knows how to protect it, and set the minimum handling rules for each class.

## 2. Scope
All information the company creates, receives, or holds, in any form, including data held in the CCC for hospitals, cryptographic keys, and information about unfixed vulnerabilities.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | PHI in the CCC; release signing keys, the device certificate authority keys, and HSM credentials; details of unfixed vulnerabilities under embargo | Named access only; encrypted at rest and in transit; keys only in the HSM; no copies outside approved systems; access logged |
| **Confidential** | Source code; design history and risk files; threat models; unreleased SBOMs; test data; supplier contracts; employee records | Need-to-know access; encrypted at rest on endpoints; shared only under agreement |
| **Internal** | Procedures, training, internal communications | Company systems only |
| **Public** | Published advisories, customer security guides, released SBOMs shared with customers, marketing | Approved for release |

## 4. Policy statements
4.1 Every information asset must have an owner and a classification recorded in the asset inventory or document system. (RA-2; ID.AM-05)
4.2 Restricted data must be encrypted at rest and in transit with approved algorithms (STD-08), using company-managed keys in the cloud. (SC-28; SC-8; SC-13; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 Release signing keys and device certificate authority keys must be generated and used only inside the HSM, under dual control. Software-held issuing keys (including on the factory provisioning server) are prohibited after 2026-12-31. Key recovery must be exercised at least yearly. (SC-12; PR.DS-01; 524B(b)(2))
4.4 PHI must stay in the CCC production account. It must not be copied to non-production, sent in logs or tickets to any vendor without a subcontractor BAA, or kept in support cases beyond the minimum needed. (AC-4; AC-3; PR.DS-01; 164.308(b)(1))
4.5 Details of unfixed vulnerabilities must be handled only in the PSIRT workspace, shared on a need-to-know basis, and released only on the coordinated disclosure date. (AC-3; AC-6; RS.CO-03)
4.6 Media, endpoints, and returned devices must be sanitized before disposal or reuse, and the sanitization recorded, including lab devices returned from hospital pilots. (MP-6; PR.DS-01; 164.310(d)(2)(i)-(ii))
4.7 Records must be kept for the periods in the retention schedule, including 6 years for security records and 2 years beyond device life for 806.20 records, and then disposed of securely. (SI-12; PR.DS-11; 164.316(b)(2)(i))
4.8 Restricted and Confidential data must not be entered into AI tools that are not on the approved list (STD-05). (AC-4; PL-4)

## 5. Compliance and enforcement
Data owners confirm classifications during the annual review. Data loss prevention alerts and P07 testing check handling. Violations are handled under POL-01 section 4.11.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may allow PHI to reach a vendor without a subcontractor BAA.

## 7. Related documents
POL-01; POL-05; STD-05; STD-08; P04 control map; retention schedule (eQMS)
