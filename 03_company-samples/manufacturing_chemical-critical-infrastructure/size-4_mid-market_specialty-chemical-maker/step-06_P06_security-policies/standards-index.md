# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Analyst (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-22 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had no supporting standards for OT security, configuration, logging, or vendors (gap 14 in `../00_company-facts.md`; P01 R-044). The USCG Cybersecurity Plan must "describe in detail how the requirements of subpart F will be met" (33 CFR 101.630(a)); the standards below are where that detail lives, and each one maps to the plan section it feeds. Policies say **what** must happen. Standards set the **measurable minimums**. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy or the approved Cybersecurity Plan.
- **Approval:** the owner drafts, the GRC Analyst checks consistency, the CySO checks USCG alignment, and the parent policy's approver signs.
- **OT changes:** any standard setting that changes how a control system is configured is implemented through MOC (POL-01 4.11).
- **Exceptions:** under POL-01 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or the annual Cybersecurity Plan audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-22) | Target issue date | Key minimum requirements | Main SP 800-53 controls | USCG plan section |
|---|---|---|---|---|---|---|---|---|
| STD-01 | **OT security standard** | POL-01, POL-02 | OT Security Engineer with the Controls Engineering Manager | Draft in progress (gap 14) | 2026-12-31 | Zone and conduit model (control, supervisory, terminal, SIS, OT DMZ) for both plants; remote access only through a gateway with MFA, logged approval, and recording; no always-on remote tools; unique console accounts by 2027-03-31; console lockout exemption with compensating controls; SIS changes only with keyswitch, two people, and MOC; monthly SIS logic compare; critical IT and OT systems list approved by the CySO | AC-3, AC-17, IA-2, SC-7, CM-5, SI-7 | 6, 7, 8 |
| STD-02 | **Configuration and network standard** | POL-01 | Controls Engineering Manager (OT) and IT Director (IT and cloud) | Draft in progress (gap 14) | 2026-12-31 | Approved hardware, firmware, and software list; baselines for every OT device class including terminal PLCs, tank gauging, and loading bay controllers; benchmark baselines for servers and cloud virtual machines; default passwords changed before use; unused ports and services disabled; allowlisting on all critical OT workstations; firewall rules reviewed quarterly and changed under MOC; network map updated after every OT change | CM-2, CM-6, CM-7, CM-7(5), CM-8, SC-41 | 6, 7 |
| STD-03 | **Logging, monitoring, and records standard** | POL-03, POL-04 | Information Security Manager (CySO) | Draft in progress (gap 14) | 2027-01-31 | Required event types per system class; all IT/OT conduits, gateway sessions, DCS security events, and SIS EWS events sent to the SIEM; 24x7 review of OT alerts (MSSP from 2027-01-31); logs readable only by privileged users; retention 12 months searchable and 2 years archived for USCG and FSP records (longer where a rule requires) | AU-2, AU-6, AU-9, AU-11, SI-4 | 4, 9 |
| STD-04 | **Third-party and OT vendor security standard** | POL-01 | GRC Analyst with the General Counsel | Draft in progress (gap 7) | 2026-12-31 | Vendor tiers (Tier 1: OT access, critical IT, or TTRS sub-service; Tier 2: system or data access; Tier 3: none); security criteria in every IT and OT purchase; notice of vulnerabilities and reportable cyber incidents without delay in every Tier 1 and Tier 2 contract; annual Tier 1 review with SOC 2 or equivalent and CUEC mapping; per-zone gateway rights; contractor cyber training before access | SA-4, SA-9, SR-6, SR-8, PS-7 | 4 |
| STD-05 | **Backup and recovery standard** | POL-03, POL-04 | Controls Engineering Manager (OT) and IT Director (IT) | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05); nightly online and weekly offline copies of all DCS, batch, SIS, terminal, and Inland PLC configurations; monthly second copy off site; quarterly partial and yearly full OT restore tests; quarterly restore tests of cloud workloads; post-event configuration compare before restart | CP-2, CP-4, CP-9, CP-10 | 3, 9 |
| STD-06 | **Vulnerability and patch management standard** | POL-01 | Security Analyst with the Controls Engineering Manager | Existing for IT (2024); OT section new | 2026-12-31 | Monthly KEV match against the IT and OT asset registers; KEVs in critical IT or OT patched or covered by a documented compensating control without delay (target 14 days to decision); IT critical patches 14 days internet-facing, 30 days otherwise; OT patches qualified with the vendor and applied at the next outage or turnaround; passive scanning only on live OT; public vulnerability intake address; USCG-scoped penetration test with each plan renewal | RA-5, SI-2, SI-5, CA-8 | 6, 11, 12 |
| STD-07 | **AI use standard** | POL-01, POL-05 | Director of Data and Analytics with the CySO | Draft in progress (gap 12) | 2026-11-30 | Approved tools list; risk tiering per P10; no AI write path to control systems; safe-limit checks for any model that recommends setpoints; MOC for AI-001 changes; human review of AI-drafted SDSs; no SSI or Restricted data in public tools; monitoring and retirement criteria | PM-9, SA-9, PL-4, RA-3, CM-3 | Not a plan section (internal) |
| STD-08 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum where supported and banned list; MFA for all IT and remote OT; phishing-resistant MFA for administrators and configuration-capable gateway users; lockout after 10 failures on IT; vaulted and rotated service credentials; break-glass accounts tested quarterly; documented compensating controls for devices that cannot meet the rule | IA-2, IA-2(1), IA-5, AC-6(5), AC-7 | 7 |

**Summary:** 8 standards. STD-01 to STD-05 and STD-07 are new and in draft; STD-06 and STD-08 exist from 2024 and need updates. Together with the policies and the SSP (P02), they supply most of Cybersecurity Plan Sections 3, 4, 6, 7, 8, and 9.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-07 AI use (2026-11-30); STD-01 OT security; STD-02 Configuration and network; STD-04 Third-party and OT vendor; STD-05 Backup and recovery; STD-06 Vulnerability and patch (all by 2026-12-31) |
| 2027 Q1 | STD-03 Logging, monitoring, and records (with the MSSP OT service, 2027-01-31); STD-08 update (2027-03-31) |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 USCG roadmap; P07 POA&M; P10 AI governance
