# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-16 (index and issue schedule), with the VP Operations agreeing to the OT standards |
| Authority | POL-01 statements 4.1 and 4.7; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies set intent for the whole company, but the measurable rules behind them were written for the OCC and business IT. Field controllers, flow computers, vendor access paths, and OT backups outside the Panhandle had no standard, which is why most gaps in the 2026 assessments are gaps in scale (P03 section 3; P01 themes). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, thresholds, and who checks them. Procedures and runbooks (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts the standard, the Security Manager reviews it for consistency, the SCADA and Automation Manager reviews any OT content for operational and safety impact (POL-01 4.5), and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.10, time-limited and recorded in the risk register. OT exceptions need the VP Operations' agreement.
- **Testing:** each standard names what the co-sourced internal audit firm checks in P07.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-16) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | Secure configuration, network, and encryption standard | POL-02, POL-04 | Security Manager with the OT Security Engineer | Existing (2024); OT network sections being added | 2027-03-31 | Benchmark-based baselines for endpoints, servers, cloud, and SaaS; OT baselines for SCADA servers, HMIs, and engineering workstations at every control site; allowed IT/OT and cloud network flows listed (the "network standard" the P04 control map cites); deny by default; no dual-homed devices; TLS 1.2 or higher and company-managed keys; documented OT encryption exceptions | CM-2, CM-6, CM-7, SC-7, SC-8, SC-28 |
| STD-02 | **OT change and configuration management standard** | POL-01, POL-04 | SCADA and Automation Manager | Draft in progress (gap 5) | 2027-03-31 | Change advisory board for SCADA servers, HMIs, PLCs, RTUs, and flow computers in all 3 areas; controller program repository covering every controller; monthly logic compare against the repository; pump station setpoint and MOP-related changes need a second reviewer and the Pipeline Compliance Manager's sign-off, and every setpoint write raises an alarm; flow computer and LACT configuration changes logged nightly and reviewed by the Measurement Supervisor; emergency changes recorded within 1 business day | CM-3, CM-4, CM-5, SI-7 |
| STD-03 | **Supply chain and vendor risk management standard** | POL-01 | General Counsel with the GRC Analyst | Draft in progress (gap 8) | 2027-03-31 | Vendor tiers (Tier 1: SCADA network access, Restricted data at scale, or support for a High-criticality BIA process; Tier 2: limited data or access; Tier 3: no data or access); security schedule before access; Tier 1 annual SOC 2 Type 2 review with CUEC mapping, or an OT vendor assessment for OT vendors without a SOC 2; incident notice within 72 hours of confirmation for Tier 1 (contract term, shorter than the 10 days in Fla. Stat. 501.171(6)); vendor change triggers; firmware authenticity checks for field devices; exit and data return terms | SA-4, SA-9, SR-2, SR-3, SR-6, SR-11 |
| STD-04 | **Remote and third-party access standard** | POL-02 | OT Security Engineer | Draft in progress (gap 3) | 2026-12-31 | Jump host is the only remote path to OT; named accounts and MFA per person; per-session approval by the OCC shift lead; recording kept 1 year and reviewed weekly; sessions end at work completion; no always-on gateways, modems, or remote tools; quarterly external scan of company and cellular address ranges for exposed management interfaces | AC-17, MA-4, IA-2(1), SC-7 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Production Engineering Manager with the Security Manager | Draft in progress (gap 13) | 2026-12-31 | AI inventory; risk tiering per P10; intake, review, and decision steps; approved-tools list by data level; no write path from any AI tool to SCADA; human review of outputs; bias and performance testing plan for High and Medium tools; no AI employment screening without an adverse impact test and HR review; decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Identity, authenticator, and privileged access standard | POL-02 | Security Manager | Existing (2024); OT update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for IT, cloud, and (by 2027-06-30) OT administrators; named HMI accounts at every control site; vaulted service credentials rotated annually; controller passwords unique per area and changed on departures; break-glass accounts tested quarterly | IA-2, IA-5, AC-2, AC-6(5) |
| STD-07 | **Backup and recovery standard** | POL-03, POL-04 | SCADA and Automation Manager with the VP IT | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); daily cloud backups with 35-day write-once retention; weekly SCADA images and controller programs kept offline in 2 locations, one with no network path (headquarters safe); quarterly SCADA image restore on a spare server; BCC full failover test twice a year, before and after hurricane season; annual restore test of Part 195 records | CP-2, CP-4, CP-6, CP-7, CP-9, CP-10 |
| STD-08 | Logging and monitoring standard | POL-03 | Security Manager | Existing (2024); OT update due | 2027-03-31 | Required event types per system class with the rationale; SCADA server, HMI, and engineering workstation logs at every control site forwarded to the SIEM; 1 year searchable retention; OT sensor alerts monitored 24x7 under the MDR contract (by 2027-06-30); time synchronization for field controllers and flow computers; MDR high-severity escalation within 30 minutes | AU-2, AU-6, AU-8, AU-11, SI-4 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Analyst with the OT Security Engineer | Existing (2024); OT update due | 2026-12-31 | Monthly authenticated scans of corporate and cloud systems; no active scanning of the SCADA network or field devices, passive OT detection instead; monthly matching of CISA ICS advisories against the OT inventory; remediation targets: corporate Critical 14 days (internet-facing) or 30 days, High 60 days; OT patches qualified by the SCADA vendor and installed through the CAB within 90 days, or compensating controls recorded | RA-5, SI-2, SI-5 |
| STD-10 | Security awareness and training standard | POL-05 | HR Director with the Security Manager | Existing (2024); field and OT content update due | 2026-12-31 | Annual training for all; quarterly phishing simulations for office staff; field safety meeting briefing for crews and drivers; annual OT refresher for Production Controllers, automation technicians, and integrator staff; payment fraud content for finance and land; insider threat content from 2027; completion tracked by HR | AT-2, AT-2(3), AT-3 |

**Summary:** 10 standards. Five are drafts requested by the gap analysis (STD-02, STD-03, STD-04, STD-05, STD-07). STD-01, STD-06, STD-08, STD-09, and STD-10 exist from 2024 and need OT or field updates. Physical security minimums for the OCC, the BCC, and field sites are in POL-02 4.13 directly rather than in a separate standard.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-04 Remote and third-party access; STD-05 AI use; STD-07 Backup and recovery; STD-09 Vulnerability and patch management; STD-10 Security awareness and training |
| 2027 Q1 | STD-01 Secure configuration, network, and encryption; STD-02 OT change and configuration management; STD-03 Supply chain and vendor risk management; STD-06 Identity, authenticator, and privileged access; STD-08 Logging and monitoring |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
