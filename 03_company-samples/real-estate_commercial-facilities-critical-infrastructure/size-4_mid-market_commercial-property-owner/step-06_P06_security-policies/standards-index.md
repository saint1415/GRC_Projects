# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Analyst (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had few supporting standards, so engineers, integrators, and security staff had no measurable rules for OT configuration, logging, vendors, or recovery (gap 12 in `../00_company-facts.md`; P01 R-040). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the GRC Analyst reviews it for consistency, the Security Manager reviews it technically, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.
- **OT first:** where a standard covers OT, it follows NIST SP 800-82 Rev. 3 and the "OT:" lines in CISA CPG 2.0, and it must be workable by chief engineers and integrators, not only by IT.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress | 2027-03-31 | Benchmark-based baselines for endpoints, console PCs, servers, cloud workloads, network devices, and SaaS tenants; documented deviations; monthly drift report; firewall rule review every quarter, with expiry dates on temporary rules | CM-2, CM-6, CM-7, SC-7 |
| STD-02 | **OT security standard (building systems)** | POL-01, POL-02 | Building Technology Manager with the OT security analyst | Draft in progress (gaps 1-5) | 2027-03-31 | SP 800-82 Rev. 3 zones and conduits at every property; OT asset inventory (owner, firmware, location, support status) kept current through change tickets and passive discovery; default credentials changed at commissioning; OT change procedure with ticket, impact review, and controller program export after each change; integrator access only through the gateway; USB scanning kiosk; acquisition due diligence checklist; life-safety separation walkdown each year | AC-4, CM-3, CM-8, IA-5, MA-4, PL-8, SC-7 |
| STD-03 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 3) | 2027-01-31 | Required event sources by system class, including BAS servers, the gateway, access control platform administrator events, firewalls, and OT network monitoring; 1 year searchable in the SIEM and 3 years in the locked bucket; alert if a source stops sending; MSSP escalation within 30 minutes for high severity; OT use cases (unexpected setpoint changes, controller downloads, door schedule changes) | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-04 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for Restricted and Confidential data; company-managed keys for cloud workloads; separate backup keys; recorded exceptions for OT protocols with segmentation as the compensating control | SC-8, SC-12, SC-13, SC-28 |
| STD-05 | **Vendor risk management standard** | POL-01 | GRC Analyst with the General Counsel | Draft in progress (gap 7) | 2026-12-31 | Vendor tiers (Tier 1: privileged or remote access to building systems, personal information at scale, or support for a High-criticality process; Tier 2: limited access or data; Tier 3: neither); security addendum before access; Tier 1 annual SOC 2 Type 2 (or equivalent) review with CUEC mapping and bridge letter; Tier 2 every 2 years; 72-hour incident notice; supply chain risk management plan | SA-4, SA-9, SR-2, SR-6, RA-3(1) |
| STD-06 | **AI use standard** | POL-01, POL-05 | vCISO with the General Counsel | Draft in progress (gap 9) | 2026-12-31 | AI and feature intake; risk tiering per P10; security, privacy, and fairness review before use; no-training clause; human review of outputs that affect people or building systems; company-enforced limits on any AI that writes to building systems; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-07 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 16-character minimum and banned list; MFA for all; security keys for administrators; named OT accounts; break-glass accounts tested quarterly; 6 or fewer access control platform administrators | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-08 | **Contingency and recovery standard** | POL-03 | IT Director with the Vice President of Engineering | Draft in progress (gap 4) | 2026-12-31 | Recovery objectives from the BIA (P05); BAACS contingency plan; written degraded-mode procedures at every property; nightly images of every BAS server; controller program and graphics copies after each change; quarterly restore tests; SCC failover drill each quarter | CP-2, CP-4, CP-9, CP-10, CP-7 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated IT scans; weekly review of CISA known exploited vulnerabilities and ICS advisories; remediation targets: Critical 14 days internet-facing, 30 days otherwise, High 60 days; OT assessed passively; firmware updates for cameras and controllers twice a year through integrators; monthly external scan | RA-5, SI-2, SI-5 |
| STD-10 | Facility security standard | POL-01 | Director of Security Operations | Existing (2024); update for Platform B engineering rooms | 2027-03-31 | Badge access and cameras on data rooms, engineering rooms, network closets, and the SCC at every property; key control logs where keys remain; visitor records for restricted rooms; P2PE terminal inspections monthly | PE-2, PE-3, PE-6, PE-8 |
| STD-11 | **Records retention and disposal standard** | POL-04 | General Counsel | Draft in progress (gap 10) | 2026-12-31 | Retention schedule (visitor ID images 30 days; visit records 1 year; video and analytics clips 30 days; access history 1 year; credential records 90 days after revocation; security records 5 years); legal hold procedure; disposal methods and certificates | SI-12, MP-6 |

**Summary:** 11 standards. Seven are new and in draft (STD-01, STD-02, STD-03, STD-05, STD-06, STD-08, and STD-11). Four exist from 2024 and need updates (STD-04, STD-07, STD-09, and STD-10).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-05 Vendor risk; STD-06 AI use; STD-08 Contingency and recovery; STD-09 Vulnerability and patch; STD-11 Records retention |
| 2027 Q1 | STD-01 Configuration; STD-02 OT security; STD-03 Logging and monitoring; STD-04; STD-07; STD-10 |

The issue dates match the P07 POA&M (POAM-022 tracks the standards set as a whole).

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
