# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.5; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but measurable rules existed only for Windows endpoints and the enclave desktops (gap 12 in `../00_company-facts.md`; P01 R-038). The gap analysis (P03) and the control assessment (P07) found the same pattern in logging, OT, vendor oversight, and product integrity. Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.6, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress (gap 12) | 2027-03-31 | Benchmark-based baselines for workstations, servers, cloud virtual machines, network devices, SaaS tenants, and the enclave; monthly drift report; documented deviations; change control for ERP, WMS, network, enclave, and integrator changes to DC automation | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 7) | 2027-01-31 | Required event types per system class; all DOP components, including ERP, WMS, portal, FIL firewall, and DC automation, send logs to the SIEM; 1 year searchable and 3 years archived; MSSP high-severity escalation within 30 minutes; weekly privileged activity review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Third-party and service provider risk standard** | POL-01 | Security Manager with the Vice President of Supply Chain | Draft in progress (gap 8) | 2026-12-31 | Vendor tiers (P09); FedRAMP Moderate equivalency before any CUI; FAR 52.204-21 terms before any FCI; annual SOC 2 review for Tier 1 with CUEC mapping; customer responsibility matrix for every External Service Provider; 72-hour incident notice terms | SA-9, SR-6, SA-4, PS-7 |
| STD-04 | **OT security standard** | POL-02 | Director of Distribution Operations with the Security Manager | Draft in progress (gap 4) | 2027-03-31 | OT asset inventory; OT VLAN with deny-by-default rules; vendor access only through the remote access gateway; default credentials changed; compensating controls for unsupported servers; integrator changes through the change board | SC-7, AC-17, MA-4, CM-8, SA-22 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Director of Inventory Planning | Draft in progress (gap 10) | 2026-12-31 | AI inventory; risk tiering per P10; review before use; no CUI or FCI in AI tools; human review of consequential outputs; adverse impact analysis for employment tools; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Director of Information Technology | Existing (2024); update due | 2027-01-31 | 14-character minimum and banned list; MFA for all; security keys for administrators and enclave users; access broker for all administrator planes; service account rotation annually; break-glass accounts tested quarterly | IA-2, IA-5, AC-6, AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | Director of Information Technology | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests per workload; annual DR exercise; downtime procedures for DC-1 manual mode, TMS outage, and the ERP queue-and-replay | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Security Manager | Existing (2024); update for FIPS mode | 2026-12-31 | TLS 1.2 or higher; FIPS 140-validated modules for every CUI path, with FIPS mode enabled; company-managed keys for backups and the CUI library | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans, including the enclave and FIL network devices; weekly known-exploited review; Critical 15 days internet-facing and 30 days otherwise, High 60 days; OT scanned passively | RA-5, SI-2, SI-5 |
| STD-10 | Facility security standard | POL-05 | Director of Distribution Operations | Existing (2024); update for DC-2 and the Integration Center | 2026-12-31 | Badge access at all sites; electronic visitor and driver logs kept 1 year; escorts in the FIL and Integration Center; quarterly badge reconciliation at every site | PE-2, PE-3, PE-8 |

**Summary:** 10 standards. STD-01 to STD-05 are new and in draft, and STD-07 is new as well. STD-06 and STD-08 to STD-10 exist from 2024 and need updates.

## 4. Related plans and procedures
| Document | Owner | Status | Notes |
|---|---|---|---|
| C-SCRM plan (NIST SP 800-161 Rev. 1) | Vice President of Supply Chain | Draft 2025; approval due 2026-11-30 (POAM-023) | Adds private-label imports, FASCSA screening, and single-source lines |
| Counterfeit detection and avoidance procedure QP-14 | Director of Quality and Product Compliance | Existing 2025; update due 2026-12-31 | Must meet all 12 DFARS 252.246-7007(c) criteria (P03) |
| Enclave SSP 1.0 | Federal Integration Lab Manager | Merged into the DOP SSP 2026-09-17 | Configuration detail kept as an appendix |
| P08 runbooks | Security Manager | Approved 2026-09-17 | Supplier compromise and ransomware |

## 5. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Third-party risk; STD-05 AI use; STD-07 Contingency and recovery; STD-08; STD-09; STD-10 |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 OT security; STD-06 |

## 6. Related documents
POL-01 to POL-05; `policy-control-map.csv` (47 statements, 29 assessed in P07); P03 roadmap; P07 POA&M; P10 AI governance process
