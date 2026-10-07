# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Associate General Counsel, Privacy, with the Director of Security |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and when a new data type or data flow is added |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-12, SC-8, SC-12, SC-13, SC-28, SI-12, MP-6, SA-3(2), PT-2, AC-4 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, GV.OC-03 |
| Regulatory drivers | N51-R01 (FTC Start with Security lessons 1 and 4; deception for data-use and deletion promises); N51-R03 (service-provider use limits); HIPAA as a business associate, 45 CFR 164.312(a)(2)(iv), 164.312(e), 164.310(d) |
| Supporting standards | STD-08 Encryption and key management; STD-10 Data retention and deletion |

## 1. Purpose
Classify company and customer data so everyone knows how to protect it, where it may go, and when it must be deleted, and so the company keeps its data-use and deletion promises.

## 2. Scope
All data the company creates or processes, in any system, including copies in logs, analytics, backups, AI prompts, and sub-processors.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Customer content (tickets, chats, attachments, end-consumer contact data); PHI in the healthcare cell; credentials, keys, and API tokens; employee Social Security numbers | Encrypted at rest and in transit; access per POL-02; never in development, staging, logs, or unapproved AI tools; PHI only inside the healthcare cell and subcontractors under BAAs |
| **Confidential** | Source code, security reports, contracts, financials, customer lists, aggregated usage data | Need-to-know access; encrypted in company SaaS; shared externally only under NDA |
| **Internal** | Policies, internal wiki, org charts | Company accounts only |
| **Public** | Marketing site, published help articles, trust center | Approved before publishing (security and AI statements by the General Counsel, POL-01 4.11) |

## 4. Policy statements
4.1 Data owners must classify data at creation; customer content is always Restricted. The Associate General Counsel, Privacy keeps a data map of every store and flow of Restricted data, reviewed quarterly and before any new flow goes live. (RA-2; CM-12; ID.AM-07)
4.2 Restricted data must be encrypted at rest with company-managed keys and in transit with TLS 1.2 or higher (STD-08). The healthcare cell must use its own keys. (SC-28; SC-8; SC-12; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 **PHI boundary.** PHI must stay in the healthcare cell and in subcontractors with a signed BAA. No export, analytics feed, log, or AI call may carry healthcare cell data elsewhere without written approval from the Associate General Counsel, Privacy and the Director of Security. (AC-4; PT-2; 164.308(b))
4.4 **No production data outside production.** Customer data may not be copied to development, staging, or sandboxes. Testing uses synthetic data. (SA-3(2); PR.DS-01)
4.5 **Internal analytics** may use usage counts and aggregated metrics. Ticket text, subject lines, or attachments may not be loaded to the data warehouse. (PT-2; SI-12)
4.6 **AI processing.** Customer content may be sent only to AI providers on the sub-processor list, under terms that prohibit training and, from 2026-11-30, through zero-retention endpoints. Prompts must contain only the minimum data needed for the feature. (PT-2; SA-9)
4.7 **Retention and deletion.** Customer data must be deleted within 30 days after contract termination from every store, including attachments, search indexes, caches, and vector indexes; backups age out within 35 days. Deletion must produce evidence (STD-10). (SI-12; MP-6; ID.AM-08)
4.8 Application logs and error reports must not contain Restricted data. A shared redaction library must be used in all services by 2026-12-31. (SI-12; AU-9)
4.9 Card numbers pasted into tickets must be redacted by default; tenants that disable redaction accept responsibility in their contract. (SI-12)
4.10 Laptops must use full-disk encryption; removable media for Restricted data is blocked. Retired devices must be wiped with a certificate kept. (SC-28; MP-6; 164.310(d)(2)(i))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the quarterly data map review, the deletion evidence report, the independent assessment (P07), and the SOC 2 Confidentiality criteria (P09).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may move PHI outside the healthcare cell without a BAA, or extend customer data retention beyond a contractual promise.

## 7. Related documents
POL-01; POL-02; STD-08; STD-10; data map; DPA and BAA templates; P03 rows G-002, G-003, G-038, G-039
