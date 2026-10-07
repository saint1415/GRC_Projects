# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-16 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2023 policies stated intent but had few supporting standards, so staff and vendors had no measurable rules for configuration, logging, vendors, or the devices in vehicles and stations (gap 11 in `../00_company-facts.md`; P03 164.316(a); P01 R-040 and R-041). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps, such as the manual dispatch binder) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-16) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress (gap 11) | 2027-03-31 | Benchmark-based secure baselines for workstations, consoles, cloud virtual machines, network devices, and SaaS tenants; documented deviations (for example CAD client requirements on consoles) with approval; monthly drift report; CAD updates tested in a test environment; integration engine and map data changes need a second reviewer | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 6) | 2027-01-31 | Required event types per system class; CAD, integration engine, ePCR, and billing platform audit logs sent to the SIEM; 1 year searchable and 6 years archived for logs that support required activities; MSSP high-severity call within 30 minutes; monthly ePCR access analytics and CAD time-edit review; egress volume alerting | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Compliance and Privacy Officer | Draft in progress (gap 7) | 2026-12-31 | Vendor tiers (Tier 1: PHI at scale, privileged access, or support for a High-criticality process; Tier 2: limited PHI; Tier 3: no PHI); BAA before any PHI, including client PHI; Tier 1 annual SOC 2 Type 2 review with CUEC mapping and bridge letter; Tier 2 every 2 years; breach notice terms of 5 business days for Tier 1; written interconnection terms for county CAD links; exit and data return terms | SA-9, SR-6, RA-3(1), SA-4, CA-3 |
| STD-04 | **Fleet and station device standard** | POL-02, POL-04 | Director of Field Operations with the Director of IT | Draft in progress (gap 5) | 2027-03-31 | Every router, MDC, tablet, cardiac monitor, and station alerting controller in the IT inventory; all routers in central management with remote administration off; device certificates for VPN; default passwords changed and vaulted before connection; station alerting on its own segment; vendor remote access only through the broker; dual-carrier SIMs at router refresh | CM-8, CM-7, IA-3, IA-5, SC-7, MA-4 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Medical Director with the vCISO and the Director of Revenue Cycle | Draft in progress (gap 9) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, clinical, and billing compliance review before use; BAA with a no-training clause for any tool touching PHI or caller audio; no AI may lower a dispatch priority or submit a claim without human review; 45 CFR 92.210 input-variable review for patient care decision support tools; monitoring metrics and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Director of IT | Existing (2023); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for administrators; named MDC sign-in; vaulted and rotated device and service credentials; break-glass accounts for the identity provider, CAD, and the cloud organization tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | Director of IT with the Director of Communications | Draft in progress (gap 1, gap 10) | 2026-12-15 | Recovery objectives from the BIA (P05); write-once backups for every company-managed workload; quarterly restore tests; annual CAD rebuild test; manual dispatch drills at both centers twice a year; annual relocation drill; the County A communications center continuity plan | CP-2, CP-4, CP-7, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Director of IT | Existing (2023); minor update | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher; IPsec for site and vehicle tunnels); encryption at rest for all Restricted data; company-managed keys; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2023); update due | 2026-12-31 | Monthly authenticated scans (moving from quarterly), including routers and station alerting controllers; weekly known-exploited vulnerability review; remediation targets: edge devices 7 days for known-exploited flaws, Critical 14 days for internet-facing systems and 30 days otherwise, High 60 days; consoles patched monthly against the CAD vendor compatibility list | RA-5, SI-2, SI-5 |
| STD-10 | Facility security standard | POL-01 | Director of Field Operations | Existing (2023); update for stations | 2027-03-31 | Badge access for both communications centers and all network closets; station door codes changed quarterly and after involuntary departures; visitor logs at headquarters and the centers; quarterly badge review | PE-2, PE-3, PE-8 |

**Summary:** 10 standards. The 5 new standards requested in the gap analysis (STD-01 to STD-05) are in draft. STD-06, STD-08, STD-09, and STD-10 exist from 2023 and need updates. STD-07 is new, and the County A agreement also requires it as part of the communications center continuity plan.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 Fleet and station devices; STD-06; STD-08; STD-10 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
