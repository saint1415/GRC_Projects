# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC |
| Owner | Security Manager (Qualified Individual) (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-29 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.7; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but set few measurable rules for the places where the 2026 assessments found gaps: payee changes, SaaS logging, service providers, the portal's code, and retention (`../00_company-facts.md` section 4; P03). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) then standard (STD) then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-29) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and SaaS baseline standard** | POL-01 | IT Director | Draft in progress | 2027-03-31 | Benchmark-based baselines for laptops, closing-room PCs, servers, and cloud images; documented security baselines for the identity provider, productivity suite, SYS-01, and SYS-02 (sharing, forwarding, legacy protocols, payee workflow settings); monthly drift report; SaaS setting changes through change control | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 3) | 2027-01-31 | Required events per system, including SaaS application events (payee and bank account changes, exports, role changes, forwarding rules); all TMCC components send logs to the SIEM; 1 year searchable and 3 years in the locked archive; MSSP high-severity escalation within 30 minutes; monthly review of payee change reports by the data owners | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Service provider risk management standard** | POL-01 | Security Manager with General Counsel | Draft in progress (gap 4) | 2026-12-31 | Tiers (Tier 1: customer information at scale, privileged access, or supports a High BIA process; Tier 2: limited customer or consumer information; Tier 3: none); security, breach notice (5 business days for Tier 1), audit, and exit terms in every service provider contract; Tier 1 annual SOC 2 Type 2 review with CUEC mapping and bridge letter; Tier 2 every 2 years; SaaS security review procedure before purchase | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | **Secure development standard** | POL-01 | Security Manager | Draft in progress (gap 10) | 2027-01-31 | Applies to the Closing Communications Portal and any future in-house application: threat model per major release; code and dependency scanning in the pipeline with no unresolved Critical or High findings at release; named developer identities; company approver for production deployments; security sign-off per release; annual penetration test; terms in the development contract | SA-8, SA-11, SA-15, CM-3 |
| STD-05 | **Payment instruction and payee verification standard** | POL-04 | President, Title and Closing, with the Controller and the CFO | Draft in progress (gap 2) | 2026-11-30 | Callback script and approved number sources; two-person rule for every payee add or edit in SYS-02, SYS-10, SYS-13, and bank platforms; 10-business-day hold on the first payment to a changed owner or agent payout account unless confirmed in person; payoffs only from lender portals or published numbers; callback log retained 5 years; quarterly sample test of 25 changes by internal audit | AC-5, SI-7, AT-3, IA-8 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for every user including contractor agents; security keys for administrators and payment staff; just-in-time SaaS admin roles; no more than 4 standing global administrators; secrets in the key vault with yearly rotation; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03 | IT Director | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05); downtime procedures for SYS-01, SYS-02, SYS-04, and SYS-10; independent backup of SaaS email, files, and transaction data; quarterly restore tests per cloud workload; annual downtime drill for closings | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data; automatic email encryption for sensitive patterns; company-managed keys for cloud workloads; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated internal scans; quarterly external scans; scans after material changes such as acquisitions; remediation targets: Critical 14 days for internet-facing systems and 30 days otherwise, High 60 days; weekly known-exploited vulnerability review | RA-5, SI-2, SI-5 |
| STD-10 | **Records retention and disposal standard** | POL-04 | General Counsel | Draft in progress (gap 7) | 2027-03-31 | Retention periods for closing files, escrow records, consumer reports, rental applications, transaction files, and email, each with its legal, regulatory, or underwriter basis; two-year disposal default for customer information under 314.4(c)(6); annual purge with certificates; annual schedule review | SI-12, MP-6 |
| STD-11 | **AI use standard** | POL-01, POL-05 | Chief Operating Officer with the vCISO and General Counsel | Draft in progress (gap 9) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, and fair housing review before use; no-training contract terms; human review of every adverse housing decision; disparity testing for High-tier tools; fair housing review of AI-drafted advertising; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |

**Summary:** 11 standards. Eight are new and in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-07, STD-10, and STD-11); STD-01 replaces informal practice. Three exist from 2024 and need updates (STD-06, STD-08, and STD-09).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Service provider risk; STD-05 Payment verification; STD-06; STD-07 Contingency and recovery; STD-09; STD-11 AI use |
| 2027 Q1 | STD-01 Configuration and SaaS baseline; STD-02 Logging and monitoring; STD-04 Secure development; STD-08; STD-10 Retention and disposal |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
