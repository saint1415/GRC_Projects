# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2023 policies stated intent but had few supporting standards, so staff and vendors had no measurable rules for configuration, logging, or vendors (gap 8 in `../scenario-facts.md`; P03 164.316(a); P01 R-040 and R-041). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress (gap 8) | 2027-03-31 | Benchmark-based secure baselines for workstations, servers, cloud virtual machines, network devices, and SaaS tenants; documented deviations with approval; monthly drift report; baselines reviewed yearly and at major upgrades; change control for interface engine and EHR build changes with a second reviewer | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 8) | 2027-01-31 | Required event types per system class, with the rationale; all ECP components send logs to the SIEM (including PACS, interface engine, file services, and device monitoring); 1 year searchable in the SIEM and 6 years in the locked archive for EHR audit and security logs that support required activities; MSSP high-severity escalation within 30 minutes; monthly EHR access analytics review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Compliance and Privacy Officer | Draft in progress (gap 3) | 2026-12-31 | Vendor tiers (Tier 1: PHI at scale or supports a High-criticality process; Tier 2: limited PHI; Tier 3: no PHI); BAA before any PHI; Tier 1 annual SOC 2 Type 2 (or equivalent) review with CUEC mapping and bridge letter; Tier 2 reassessed every 2 years; breach notice terms of 5 business days for Tier 1; exit and data return terms | SA-9, SR-6, RA-3(1), SA-4 |
| STD-04 | **Medical device security standard** | POL-02, POL-04 | IT Director with the ASC Administrator and Imaging Center Director | Draft in progress (gap 1, gap 9) | 2027-03-31 | Complete device inventory (owner, OS, software bill of materials where available, support status, PHI storage); devices on a dedicated VLAN with deny-by-default rules at every site; default credentials changed before connection; security review before purchase (manufacturer disclosure statement); vendor remote access only through the access broker; compensating controls for unsupported devices; sanitization certificate on return | CM-8, SC-7, AC-4, SA-22, MA-4, MP-6 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Chief Medical Officer with the vCISO | Draft in progress (gap 7) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, and clinical review before use; BAA with no-training clause for any tool touching PHI; human review of outputs; recording consent for ambient tools; 45 CFR 92.210 input-variable review for patient care decision support tools; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2023); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for administrators; vaulted and rotated service account credentials; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | Draft in progress (gap 4) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests per practice-managed workload; annual DR exercise; downtime procedures per business unit, including the ASC cyber procedures under 42 CFR 416.54 | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2023); minor update | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for all Restricted data; company-managed keys for cloud workloads; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2023); update due | 2026-12-31 | Monthly authenticated scans (moving from quarterly); weekly known-exploited vulnerability review; remediation targets: Critical 14 days for internet-facing systems and 30 days otherwise, High 60 days; medical devices scanned passively | RA-5, SI-2, SI-5 |
| STD-10 | Facility security standard | POL-01 | Director of Clinic Operations | Existing (2023); update for Clinics 6-8 | 2027-03-31 | Badge access for all network closets; key logs where keys remain; visitor logs; quarterly badge review | PE-2, PE-3, PE-8 |

**Summary:** 10 standards. The 5 new standards requested in the gap analysis (STD-01 to STD-05) are in draft. STD-06, STD-08, STD-09, and STD-10 exist from 2023 and need updates. STD-07 is new, and it is also required for the ASC plan update.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 Medical device security; STD-06; STD-08; STD-10 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
