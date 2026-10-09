# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Analyst (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.7; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent for IT but had no OT standards, so controls engineers, integrators, and refrigeration contractors had no measurable rules for remote access, change, backup, or monitoring (intake policy library, EV-030; P03 rows on 417.4(a)(3), 417.5(d), and 1910.119(l); P01 R-006, R-048). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the GRC Analyst reviews it for consistency, the Security Manager reviews it technically, and the parent policy's approver signs it. Standards that touch CCPs or formulations also need the VP FSQA's sign-off; standards that touch refrigeration controls need the Director of Engineering and Maintenance's sign-off.
- **Exceptions:** under POL-01 section 4.8, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and hardening standard (IT and OT)** | POL-01, POL-04 | Security Manager with the OT security engineer | Draft in progress (EV-013, EV-030) | 2027-03-31 | Benchmark-based baselines for endpoints, servers, cloud virtual machines, network devices, and SaaS tenants; OT baselines for HMIs, SCADA, historians, MES, and engineering workstations (unneeded services off, USB blocked, application allowlisting where agents cannot run); default credentials changed at commissioning; quarterly drift check | CM-2, CM-6, CM-7, CM-7(5) |
| STD-02 | **OT access and remote access standard** | POL-02 | Security Manager with the Controls Engineering Manager | Draft in progress (EV-007, EV-016, EV-017) | 2026-12-31 | Named HMI and MES accounts with badge or PIN sign-in; view-only operator accounts only; emergency operator access procedure; all remote access through the gateway with MFA, approval per session, a time window, and recording; vendor accounts disabled between sessions; no modems or always-on VPNs; quarterly OT access review | AC-2, AC-17, MA-4, IA-2(1) |
| STD-03 | **OT change management standard** | POL-01 | Controls Engineering Manager with the VP FSQA and the Director of Engineering and Maintenance | Draft in progress (EV-027, EV-065) | 2026-12-31 | One change ticket for PLC, HMI, recipe, blend, SCADA, MES, controller, network, and remote access changes; required fields for HACCP reassessment (9 CFR 417.4(a)(3)), SSOP revision (416.14), PSM and RMP management of change (1910.119(l); 68.75), and food defense reanalysis; two-person approval; test in the sanitation window; post-change comparison of running logic with the repository | CM-3, CM-4, CM-5 |
| STD-04 | **Logging and monitoring standard (IT and OT)** | POL-03 | Security Manager | Draft in progress (EV-011, EV-024) | 2027-01-31 | Required events per system class, including HMI setpoint changes, recipe releases, engineering downloads, controller logins, and new OT devices; OT sensor alerts and OT logs sent to the MSSP; 1 year searchable in the SIEM and 2 years in the locked archive; MSSP high-severity escalation within 30 minutes; OT alert triage playbook | AU-2, AU-6, AU-11, SI-4 |
| STD-05 | **Electronic records integrity standard** | POL-04 | VP FSQA with the IT Director | Draft in progress (EV-009, EV-025) | 2026-12-31 | The "appropriate controls" for 9 CFR 417.5(d) and 416.16(b): audit trails always on and protected; authenticated named sign-off; synchronized clocks; record locking after pre-shipment review with reasoned corrections; administrators separated from record entry; quarterly integrity review by FSQA | AU-8, AU-9, AU-10, SI-7 |
| STD-06 | **OT backup and recovery standard** | POL-03, POL-04 | Controls Engineering Manager with the IT Director | Draft in progress (EV-022, EV-023) | 2027-01-31 | Recovery objectives from the BIA (P05); company-owned repository for all PLC programs, recipes, blend definitions, and controller configurations at both plants; immutable offline copies; quarterly restore tests in the sanitation window; verified restart checklist | CP-2, CP-4, CP-9, CP-10 |
| STD-07 | **Vendor and supply chain risk standard** | POL-01 | GRC Analyst | Draft in progress (EV-048, EV-049) | 2027-03-31 | Vendor tiers (P09); security, change notice, and incident notice terms (notice within 72 hours for Tier 1); annual SOC 2 Type 2 or equivalent review for Tier 1 with CUEC mapping; OT vendor security questions added to PSM contractor evaluation; exit and data return terms | SA-4, SA-9, SR-2, SR-6 |
| STD-08 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); OT update due | 2026-12-31 | Monthly authenticated IT scans; known-exploited vulnerabilities on internet-facing devices fixed within 72 hours; other Critical 14 days internet-facing and 30 days otherwise; High 60 days; OT: passive vulnerability identification, risk-ranked fixes in sanitation windows within 90 days, or a documented compensating control | RA-5, SI-2, SI-5 |
| STD-09 | **AI use standard** | POL-01, POL-05 | VP FSQA with the vCISO | Draft in progress (EV-058, EV-059) | 2026-12-31 | AI inventory; risk tiering per P10; review before use; no AI system replaces a CCP or a food safety decision; vendor data-use terms; model updates as OT changes; bias and performance monitoring; approved tools list | PM-9, SA-9, PL-4 |
| STD-10 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for administrators; privileged access management for SaaS and OT administrators; vaulted and rotated service account credentials; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |

**Summary:** 10 standards. 8 are new drafts (STD-01 to STD-07 and STD-09), requested by the gap analysis. STD-08 and STD-10 exist from 2024 and need OT updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-02 OT access and remote access; STD-03 OT change management; STD-05 Electronic records integrity; STD-08 update; STD-09 AI use |
| 2027 Q1 | STD-01 Configuration and hardening; STD-04 Logging and monitoring; STD-06 OT backup and recovery; STD-07 Vendor and supply chain; STD-10 update |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
