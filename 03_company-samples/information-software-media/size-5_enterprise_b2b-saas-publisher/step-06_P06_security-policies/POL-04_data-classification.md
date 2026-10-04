# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-4, SC-8, SC-12, SC-28, SI-12, CA-3, PT-2, PT-3 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory drivers | FTC Act Section 5 (N51-R01); customer DPA; CCPA service provider rules (Cal. Code Regs. tit. 11, 7050-7051); Fla. Stat. 501.171(8); 28 CFR Part 202 |

## 1. Purpose
Classify information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match. Customer data is held on customers' behalf and may be used only as the contract allows.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and vendor agents with company accounts) in every office and remote location, including acquired companies from their acquisition date. Covers all systems and data, including the Operations Cloud, Data Cloud, Government Edition, AQ-01, cloud accounts, SaaS, endpoints, and systems that sub-processors and other vendors operate for the company. Where the Government Edition's FedRAMP package sets a stricter requirement, the stricter requirement applies inside its boundary.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and data-use rules; approves new uses of customer data |
| Data owners (system owners) | Classify their data; approve access; run deletion |
| CISO | Encryption, backup, and disposal standards |
| Chief Data and AI Officer | Data use for AI, including model training |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (customer data, end-customer personal information, credentials and keys, employee sensitive personal information), Confidential (financial, legal, security, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit using STD-04.1, with per-tenant keys for customer data. (SC-28; SC-8; SC-12; PR.DS-01)
4.3 Customer data must be logically separated by tenant in every data store, cache, queue, index, and export, and isolation must be tested on every release. (SC-4; AC-3; PR.DS-01)
4.4 Customer data may be used only to provide and support the service for that customer. It must not be used to train or improve any model that serves other customers, and must not be sold or shared. (PT-3; PT-2; GV.OC-03)
4.5 Exports of customer data to internal systems or partners must be minimized to the fields needed, scoped to one tenant, covered by an interconnection agreement, and land only in accounts inside the landing zone. (CA-3; AC-6; PR.DS-01)
4.6 Customer data must be deleted from production within 30 days and from backups within 90 days after termination, and deletion must be reconciled monthly against the list of terminated tenants. (SI-12; MP-6; ID.AM-08)
4.7 Production customer data must not be copied to non-production environments; synthetic or masked data must be used. (SI-12; SA-3(2); PR.DS-01)
4.8 Restricted data must not be entered into any AI tool or sent to any model provider unless the AI governance council has approved the use case and the provider is a contracted sub-processor with no-training and zero-retention terms. (SA-9; PL-4; GV.SC-05)
4.9 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal; cloud media sanitization is inherited from the cloud providers. (MP-6; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Key Management Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup and Retention Standard
- STD-04.4 Tenant Isolation Standard
- PRC-04.1 Customer Data Export and Interconnection Procedure
- PRC-04.2 Tenant Offboarding and Deletion Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the quarterly public statement review. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
