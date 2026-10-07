# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-12, SC-13, SC-28, MP-6, SI-12, AC-3, AC-4 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | FedRAMP CMU rules and Class D SC controls (C-IT-R01); DFARS flow-down (C-IT-R03); DOJ Data Security Program (C-IT-R04); HIPAA 164.312(a)(2)(iv), (e) (business associate); Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Classify company and customer information, and protect it according to its class, with special rules for customer content, federal data, and cryptographic keys.

## 2. Scope
All information the company creates or handles, including customer content (which the company processes but does not own), federal data and CUI in G1, PHI in HIPAA-eligible services, keys and signing material, and company confidential information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Policy owner |
| Director of Key Management and PKI | Cryptography and key management (STD-04.1) |
| Data owners | Classify company data |
| Customers | Classify their own content; the company protects all customer content at the Customer Content level |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All information must be classified as Public, Internal, Confidential, Customer Content, or Restricted (keys, signing material, credentials, federal data in G1). Customer content is always handled at the Customer Content level or higher. (RA-2; ID.AM-05)
4.2 Customer content must not be accessed, used, or moved except to provide the service, under a customer-approved access request, or as law requires. (AC-3; AC-4; PR.DS-01)
4.3 Customer content and Restricted information must be encrypted at rest and in transit with cryptographic modules that hold active CMVP validations; G1 must use only such modules (STD-04.1). (SC-8; SC-13; SC-28; PR.DS-01)
4.4 Keys must be generated and held in HSMs, with dual control for key ceremonies and no export of signing keys. (SC-12; PR.DS-01)
4.5 A cryptographic module inventory must be maintained for every FedRAMP offering, with validation status reviewed monthly. (SC-13; CM-8; ID.AM-08)
4.6 Federal data and CUI in G1 must stay in G1 and the out-of-band vault copy encrypted with G1-held keys. (AC-4; SC-28; PR.DS-01)
4.7 Media that held customer content must be sanitized per NIST SP 800-88 Rev. 2 or destroyed on site, with a certificate per drive. (MP-6; PR.DS-01)
4.8 Restricted and Customer Content must not be placed in tickets, chat, or AI tools outside the approved list (STD-05.3). (SI-12; AC-3; PR.DS-10)
4.9 Information must be retained only as long as the retention schedule, contract, or law requires, and then disposed of. (SI-12; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Cryptography and Key Management Standard
- STD-04.2 Media Protection and Sanitization Standard
- STD-04.3 Backup Standard
- STD-04.4 Customer Content Handling Standard
- PRC-04.1 Customer Access Request Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the FedRAMP independent assessment, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.6), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5 (PRC-01.2).

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HCP-G SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
