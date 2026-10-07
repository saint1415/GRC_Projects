# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Manager (index); each standard has its own owner below |
| Approved by | Chief Technology Officer, 2026-09-29 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2023 policies stated intent, but engineers had few measurable rules for machine credentials, logging, recovery, retention, or AI features. Those are exactly where the 2026 assessments found gaps (`../00_company-facts.md` section 4; P03 G-007, G-014, G-002; P01 R-001, R-002, R-006). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the GRC Manager reviews it for consistency and SOC 2 evidence, the Director of Security reviews the security content, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or the SOC 2 auditor checks; the GRC tool collects the evidence.
- **Automation first:** where a rule can be enforced by a guardrail, a CI check, or a policy-as-code test, the standard requires the automated control and treats manual review as the fallback.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-29) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | VP Platform Engineering | Draft in progress | 2026-12-31 | All production resources defined in infrastructure code by 2027-03-31; benchmark baselines for container images, the search cluster, and cloud accounts; guardrails as policy-as-code; drift report weekly; emergency changes approved after the fact within 1 business day | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Director of Security | Draft in progress (gap 4) | 2026-12-31 | Required events per system class, including object-level reads of attachments and database query audit for customer data stores; cloud audit logs 1 year write-once; 6 years for HIPAA-required records; detections for bulk reads, snapshot sharing, and unusual-source credential use; MDR coverage of cloud workloads; support view session review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor and sub-processor risk standard** | POL-01 | GRC Manager with the Associate General Counsel, Privacy | Draft in progress (gap 15) | 2026-12-31 | Tiers (Tier 1: customer content at scale or production access; Tier 2: limited customer data; Tier 3: no customer data); DPA before any customer data; subcontractor BAA before any healthcare cell data; Tier 1 annual SOC 2 Type 2 review with complementary user entity controls mapped and a bridge letter; DOJ Data Security Program screening questions; 30-day customer notice of new sub-processors | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | Secure software development standard | POL-01 | VP Engineering | Existing (2024); update due | 2026-12-31 | Design review with threat modeling for features touching tenant data, authentication, or new sub-processors; required code review; static analysis and dependency scanning; cross-tenant authorization tests as a merge gate; break-glass deploy with two-person approval | SA-3, SA-8, SA-11, SA-15, CM-3 |
| STD-05 | **AI development and use standard** | POL-01, POL-05 | VP Product with the Director of Security | Draft in progress (gap 7) | 2026-12-15 | AI inventory; risk tiering per P10; evaluation suite with thresholds (accuracy, groundedness, prompt injection, subgroup performance) before release and after model changes; zero-retention, no-training provider terms; tenant-scoped retrieval; human handoff for customer-facing AI; approved tools list for staff; recording consent for AI summarizers | PM-9, SA-9, SA-11, RA-3, PL-4 |
| STD-06 | Authenticator, secrets, and privileged access standard | POL-02 | Director of Security | Existing (2023); update due | 2026-10-31 | 14-character minimum and banned list; security keys for privileged access; just-in-time access for production; no long-lived cloud keys (inventory and 90-day rotation for any exception); secrets only in the secrets manager; break-glass tested quarterly | IA-2, IA-5, IA-5(7), AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | VP Platform Engineering | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); write-once backups with separate administrators; cross-region search snapshots; regional failover exercise twice a year from 2027; DR plan with emergency mode procedures for the healthcare cell (45 CFR 164.308(a)(7)) | CP-2, CP-4, CP-7, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Director of Security | Existing (2023); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data with company-managed keys; separate keys for the healthcare cell; annual key rotation | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | VP Platform Engineering | Existing (2023); update due | 2026-12-31 | Continuous image and account scanning; deploy blocked for critical findings older than 15 days; fix targets Critical 15 days, High 30 days; bug bounty triage in 3 business days; annual penetration test with retest | RA-5, RA-5(11), SI-2, CA-8 |
| STD-10 | Data retention and deletion standard | POL-04 | Associate General Counsel, Privacy | New (gap 13) | 2026-11-30 | Retention schedule per data type; tenant deletion within 30 days across database, attachments, search, caches, and vector indexes; monthly deletion evidence report; log redaction; no ticket text in the warehouse | SI-12, MP-6, PT-2 |

**Summary:** 10 standards. Five are new or rewritten in draft (STD-01, STD-02, STD-03, STD-05, STD-07), one is new (STD-10), and four exist and need updates (STD-04, STD-06, STD-08, STD-09).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-06 (2026-10-31); STD-10 (2026-11-30); STD-05 (2026-12-15); STD-01, STD-02, STD-03, STD-04, STD-07, STD-09 (2026-12-31) |
| 2027 Q1 | STD-08 |

All standards except STD-08 must be issued before the 2027 SOC 2 examination period starts on 2027-01-01 (P09).

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P09 readiness gates; P10 AI governance process
