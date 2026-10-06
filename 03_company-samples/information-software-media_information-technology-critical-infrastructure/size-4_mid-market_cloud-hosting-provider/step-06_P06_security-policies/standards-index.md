# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Manager (index); each standard has its own owner below |
| Approved by | Chief Technology Officer, 2026-09-22 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.9; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner, and after any FedRAMP rules release that changes it |

## 1. Why this index exists
The 2024 standards were written for the government partition. The commercial partition and DC-1 followed them loosely or not at all (gap 1, "two-speed security", in `../00_company-facts.md`). The 2026 FedRAMP rules also add measurable duties (PAIN ratings, monthly verification, third-party resource records) that need a home. Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy.
- **One standard, two partitions:** each standard applies to both partitions and all three data centers. Where the government partition needs more (for example FIPS 140-validated modules or U.S.-person access), the standard says so.
- **Approval:** the owner drafts, the GRC Manager checks consistency with the SSP (P02) and the FedRAMP rules (P03), and the parent policy's approver signs.
- **Exceptions:** under POL-01 section 4.8, time-limited and recorded in the risk register.
- **Testing:** P07 and the FedRAMP annual assessment check the minimums.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-22) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Asset and boundary inventory standard** | POL-04 | GRC Manager with the VP Platform Engineering | New; draft | 2026-12-31 | Every CMDB item tagged with partition, data classification, and whether it handles or can affect federal customer data; third-party information resources listed with usage, justification, mitigations, and compensating controls; monthly reconciliation against discovery and cloud APIs | CM-8, CM-12, SA-9, PL-2 |
| STD-02 | **Privileged access and authenticator standard** | POL-02 | Security Engineering Lead | Revised 2026-09 (extends the 2024 government version to all partitions) | Issued 2026-10-01 | Hardware authenticators for all workforce; PAM with just-in-time elevation for every cluster and production account; break-glass accounts sealed and tested quarterly; machine credentials in the vault with owner and 90-day maximum life; RMM two-person approval for multi-customer actions; idle timeouts (portal 30 minutes, PAM 60 minutes) | AC-2, AC-6, AC-17, IA-2, IA-5 |
| STD-03 | **Secure configuration standard** | POL-04 | VP Platform Engineering | Revised 2026-09 | Issued 2026-10-01 | Benchmark-based baselines as code for hosts, hypervisors, BMCs, network devices, containers, and cloud accounts; weekly drift checks for all clusters (daily in the cloud); deviations approved and recorded; FedRAMP significant change evaluation in every change ticket | CM-2, CM-3, CM-6, CM-7 |
| STD-04 | **Logging and monitoring standard** | POL-03 | Security Operations Manager | Revised 2026-09 | Issued 2026-10-01 | Required event types per system class; every in-scope source in the SIEM, including all DC-1 clusters and the RMM tool; 1 year online and 3 years archived for both partitions; source-silence alerts at 30 minutes; weekly privileged activity review; AI triage limits and weekly sampling | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-05 | **Secure development and software supply chain standard** | POL-04 | VP Software Engineering | Existing (2024); update due | 2027-03-31 | Two approvers per change; static analysis and secret scanning on every pull request; HSM signing and deploy-time verification for templates and releases in both partitions; SBOM and signed build provenance per release; KEV gate before template release | SA-10, SA-11, SA-15, SI-7, SR-3 |
| STD-06 | **Encryption and key management standard** | POL-04 | Security Engineering Lead | Existing (2024); update due | 2026-12-31 | TLS 1.2 or higher; FIPS 140-validated modules for federal data, documented per service; company-managed keys; signing keys only in the HSM; yearly rotation with two custodians | SC-8, SC-12, SC-13, SC-28 |
| STD-07 | **Contingency and recovery standard** | POL-03 | VP Platform Engineering | New; draft | 2026-12-31 | Recovery objectives from the BIA (P05); one contingency plan for both partitions and all data centers; quarterly control plane restore tests in both partitions; yearly data center failover exercise; immutable backups with two-person deletion | CP-2, CP-4, CP-6, CP-7, CP-9, CP-10 |
| STD-08 | **Vulnerability and patch management standard** | POL-04 | Security Engineering Lead | Being rewritten for the 2026 rules | 2026-12-07 | Monthly authenticated scanning of all in-scope resources (resources likely to drift every 14 days); evaluation of exploitability, internet reachability, and PAIN for each finding; remediation within the FedRAMP Class C PAIN timeframes; KEVs by the CISA due date; findings older than 192 days marked accepted; quarterly BMC firmware cycle | RA-5, SI-2, SI-5, CA-5 |
| STD-09 | **Vendor and supply chain risk standard** | POL-01 | GRC Manager | Revised 2026-09 | Issued 2026-10-01 | Vendor tiers (Tier 1: access to customer data at scale or supports a High-criticality process); Tier 1 annual review of the SOC 2 report or FedRAMP package with exception follow-up; incident notice within 72 hours in every Tier 1 contract; 28 CFR Part 202 check; hardware receiving inspection | SA-4, SA-9, SR-2, SR-6, SR-10 |
| STD-10 | **AI use standard** | POL-01, POL-05 | Director of Security with the AI review group | New; draft | 2026-12-31 | AI inventory and risk tiering (P10); review before use; no federal data in AI tools without approval; human review of outputs that reach customers, code, or hiring; no auto-close of privileged or tooling alerts; bias review for any tool used in employment decisions | PM-9, SA-9, PL-4, RA-3 |

**Summary:** 10 standards. 4 were revised for both partitions and issued with the policies on 2026-10-01 (STD-02, STD-03, STD-04, STD-09). STD-05 and STD-06 exist from 2024 and need updates. STD-08 is being rewritten for the FedRAMP VDR and VER rules. STD-01, STD-07, and STD-10 are new.

## 4. Issue schedule
| Date | Standards |
|---|---|
| 2026-10-01 | STD-02, STD-03, STD-04, STD-09 (issued) |
| 2026-12-07 | STD-08 (FedRAMP VDR and VER maintaining date) |
| 2026-12-31 | STD-01, STD-06, STD-07, STD-10 |
| 2027-03-31 | STD-05 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
