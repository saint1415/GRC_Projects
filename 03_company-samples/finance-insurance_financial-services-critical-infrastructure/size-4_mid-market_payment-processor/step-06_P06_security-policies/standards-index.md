# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Director of Information Security (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.12; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner, and when a platform is added or migrated |

## 1. Why this index exists
The 2024 policies stated intent, but the supporting standards were thin and were written for the core platform only. The acquired Integrated Payments gateway (Cloud B) follows none of them (gap 15 in `../00_company-facts.md`; P03 rows 1.1, 2.1, 6.1, 10.1; P01 R-040 and R-047). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them. Every standard applies to Cloud A, Cloud B, the colocation cages, and SaaS unless it says otherwise.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the Director of Information Security reviews it for consistency, and the COO signs it.
- **Exceptions:** under POL-01 section 4.13, time-limited and recorded in the risk register.
- **PCI DSS link:** where PCI DSS lets the company set a frequency, the standard cites the targeted risk analysis (PCI DSS 12.3.1) that sets it.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Cloud platform guardrails standard** | POL-01, POL-02 | VP Platform Engineering | New; draft in progress | 2026-12-31 | Organization guardrails in every cloud (deny public storage, unencrypted volumes, disabled logging, unapproved regions); posture management in every account with weekly triage; landing zone account pattern for new workloads; Cloud B brought under the same guardrails until migration | CM-6, CA-7, SC-7 |
| STD-02 | **Configuration and hardening standard** | POL-01 | VP Platform Engineering | Exists for Cloud A (2024); extension to Cloud B and settlement servers in progress | 2027-03-31 | Benchmark-based baselines for container images, cage servers, network devices, and SaaS tenants; no vendor default credentials on any interface including baseboard management; one primary function per component; monthly drift report; documented compensating controls for unsupported components | CM-2, CM-6, CM-7, SA-22 |
| STD-03 | **Logging and monitoring standard** | POL-03 | Director of Information Security | Draft in progress | 2027-01-31 | Required event types per component class (PCI DSS 10.2.1); every CDE component logs to the SIEM within 90 days of joining scope; 12 months retention with 3 months searchable; write-once archive; silent-source and failed-agent alerts within 1 hour; MSSP high-severity escalation within 30 minutes | AU-2, AU-5, AU-6, AU-9, AU-11, SI-4 |
| STD-04 | **Privileged access and service account standard** | POL-02 | Director of Information Security | Draft in progress | 2026-12-31 | Security keys for administrators; PAM with just-in-time elevation and session recording on every platform; no IAM users with long-lived keys for people; service accounts scoped to one function, secrets vaulted and rotated at least every 12 months (frequency set by targeted risk analysis); six-month service account reviews | AC-2, AC-6(2), AC-6(5), IA-5 |
| STD-05 | Cryptography and key management standard | POL-04 | VP Platform Engineering | Exists (2024); update for Cloud B and DR key replication | 2026-12-31 | Approved algorithms (AES-256; RSA 3072 or higher; TLS 1.2 or higher); payment HSMs for PAN keys; dual control and split knowledge; key replication to the DR cage after every rotation; cryptographic architecture description kept current (PCI DSS 3.6.1.1); funding file signing keys in HSMs | SC-12, SC-13, SC-28 |
| STD-06 | Secure development and change standard | POL-01, POL-05 | CTO | Exists (2024) for the core platform; extension to Integrated Payments | 2026-12-31 | Secure coding training each year; two approvals for CDE changes, one from outside the author's team; signed builds; static analysis and dependency scanning on every repository; labeled and security-reviewed AI-assisted changes; payment page script inventory and integrity checks (PCI DSS 6.4.3) | CM-3, SA-10, SA-11, SI-7 |
| STD-07 | Third-party and service provider standard | POL-01 | Chief Risk and Compliance Officer | Exists (2024); update for acquired vendors and ISVs | 2026-12-31 | Tiers (Tier 1: account data or CDE influence, or supports a High-criticality BIA process); current AOC or ROC inclusion and a responsibility matrix for every PCI DSS service provider; annual Tier 1 review of AOC or SOC 2 Type 2 with complementary user entity controls mapped; security incident notice within 24 hours in Tier 1 contracts; security schedule for the 20 largest ISVs | SA-4, SA-9, SR-6, RA-3(1) |
| STD-08 | **Contingency and recovery standard** | POL-03 | VP Platform Engineering | Draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); automated failover for authorization; semiannual failover tests; annual settlement DR test with both sponsor banks informed in advance; quarterly restore tests per database; recovery runbook for every High-criticality process | CP-2, CP-4, CP-9, CP-10 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Director of Information Security | Exists (2024); update due | 2026-12-31 | Authenticated internal scans quarterly and after significant change on every platform; ASV scans quarterly; critical patches within 30 days and High within 60 days; monthly maintenance windows for settlement servers; known-exploited vulnerabilities reviewed weekly | RA-5, SI-2, SI-5 |
| STD-10 | **AI and model risk standard** | POL-01, POL-05 | Chief Risk and Compliance Officer with the Head of Data Science | New; draft in progress | 2026-12-31 | AI and model inventory; risk tiering per P10; independent validation before production and annually for High-tier models; bias testing for models that affect people; approved AI tools list; no-training contract terms; monitoring and decommissioning criteria | PM-9, RA-3, SA-9, PL-4 |

**Summary:** 10 standards. Five are new or substantially new (STD-01, STD-03, STD-04, STD-08, STD-10). Five exist from 2024 and need updates to reach Cloud B, the settlement servers, or the acquired vendors (STD-02, STD-05, STD-06, STD-07, STD-09).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-01 Cloud guardrails; STD-04 Privileged access and service accounts; STD-05 Cryptography; STD-06 Secure development; STD-07 Third parties; STD-08 Contingency and recovery; STD-09 Vulnerability and patch; STD-10 AI and model risk |
| 2027 Q1 | STD-02 Configuration and hardening; STD-03 Logging and monitoring |

Interim measures for the 2026 ROC (Cloud B logging, PAM, and egress controls) are in the P07 POA&M and do not wait for the standards to be issued.

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
