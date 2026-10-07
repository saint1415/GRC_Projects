# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Compliance and Privacy Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, significant incidents, or exercises |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, MP-1, MP-6, SC-8, SC-12, SC-28, CP-9, CM-8, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| HIPAA Security Rule and other rules | 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A) |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard; STD-04 Fleet and station device standard |

## 1. Purpose
Classify company and client information by sensitivity and set handling rules, so protection matches the harm a disclosure or loss would cause.

## 2. Scope
All information the company creates, receives, maintains, or transmits, in any form, at every site, in every vehicle, and in every system, including client data handled for billing services and data held by vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance and Privacy Officer | Owns classification; approves new uses and new locations of Restricted data |
| Data owners (directors) | Classify their data; approve access and sharing |
| Director of IT | Implements encryption, backup, and disposal controls; keeps the Restricted data inventory |
| Director of Revenue Cycle | Keeps client data separated and returns or destroys it at contract end |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels: **Restricted** (ePHI, call audio and transcripts, client PHI, patient financial and insurance data, credentials); **Confidential** (county and client contracts, payroll, security documents, board materials); **Internal** (schedules, posting plans, procedures); **Public** (website). (RA-2; ID.AM-07; 164.308(a)(1)(ii)(A))
4.2 Restricted data must be encrypted at rest on every device, service, and backup, and in transit on every network, including vehicle links. External email containing PHI must use the enforced encryption option. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 Encryption keys for cloud workloads and backups must be managed in the company's key management service, with separate keys for the backup account and annual rotation. (SC-12; PR.DS-01; 164.312(a)(2)(iv))
4.4 Restricted data may be stored only in approved systems: CAD, the ePCR, the billing platform, the recording archive, the reporting database, approved file shares, the backup account, and approved vendor systems under a BAA. It must never be kept on personal devices or in personal accounts. Client data must stay in that client's billing workspace and approved exports. (AC-3; SA-9; PR.DS-01; 164.308(a)(4)(ii)(B))
4.5 The Director of IT must keep an inventory of where Restricted data is stored, including MDCs, tablets, routers, cardiac monitors, and station alerting controllers, and which vendors receive it. The inventory must be reconciled quarterly with fleet work orders. (CM-8; ID.AM-01; 164.310(d)(2)(iii))
4.6 Media and devices holding Restricted data must be sanitized (for reuse) or destroyed by a certified vendor that provides a certificate (for disposal), including devices returned to fleet or monitor vendors. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
4.7 Backups of Restricted data in company-managed systems (CAD database, integration engine, recording archive, reporting database) must be encrypted, stored in the separate backup account in a second region, protected by write-once retention, and restore-tested at least quarterly. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))
4.8 Restricted data must not be entered into AI tools unless the tool is approved under STD-05 and the vendor has a BAA that prohibits training on company or client data (P10). (SA-9; GV.SC-05; 164.308(b)(1))
4.9 Records are retained on the company schedule: EMS records at least 5 years (Rule 64J-1.014, F.A.C.), Medicare documentation 7 years from the date of service (42 CFR 424.516(f)), security documentation 6 years (POL-01 4.12), and client data as the client BAA requires, then returned or destroyed. (SI-12; GV.PO-02; 164.316(b)(2)(i); 42 CFR 424.516(f))

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and quarterly inventory reconciliation.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-04; STD-05; STD-07; STD-08; P04 cloud architecture; P10 approved-tools list; records retention schedule
