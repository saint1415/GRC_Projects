# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Cybersecurity Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.8; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner, and within 30 days of a directive revision that affects it |

## 1. Why this index exists
The 2023 policies stated intent, and the TSA-approved CIP describes measures for the Critical Cyber Systems, but several measurable rules sat only in the CIP (which is SSI and seen by few people) or nowhere at all. The gap analysis found the result: shared field passwords never rotated, OT outside the KEV review, logs not defined for CAD/CTC and the BOS, and no restore standard (P03 G-021, G-033, G-038, G-063; P01 R-006, R-019). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds, written so that staff and vendors can follow them without reading the CIP. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy or any CIP measure.
- **Link to the CIP:** where a standard implements a CIP measure, it cites the directive section. A change to such a standard that is a permanent change to a CIP measure is filed with TSA as an amendment request within 50 days (POL-01 4.5). Standards themselves are Internal, not SSI, because they state minimums and not the company's specific vulnerabilities.
- **Approval:** the owner drafts, the Cybersecurity Manager reviews for consistency with the CIP, and the parent policy's approver signs.
- **Exceptions:** under POL-01 statement 4.9, time-limited and recorded in the risk register.
- **Testing:** each standard is tested in the annual P07 assessment or the CAP schedule.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard (IT and OT baselines)** | POL-04, POL-05 | Director of Information Technology with the Director of Signals and Communications | Draft in progress (gap 8) | 2027-03-31 | Benchmark-based baselines for servers, workstations, consoles, network devices, cloud accounts, and SaaS tenants; vendor-certified baselines for CAD/CTC, BOS, and field controllers; application allowlisting on consoles and OT servers; every field controller configuration change recorded with a before-and-after copy and a second reviewer; monthly drift report | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Cybersecurity Manager | Draft in progress (gap 7) | 2027-01-31 | Required event types per system class with the rationale, including CAD/CTC logons, authority and route changes, administrator actions, BOS events, and field controller events; all TDPO sources in the SIEM; 1 year searchable and 3 years in the write-once archive; MSSP high-severity escalation within 30 minutes, including OT sensor alerts; weekly review of field traffic baselines | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Cybersecurity Manager with the Chief Financial Officer | Draft in progress (gap 10) | 2026-12-31 | Vendor tiers (Tier 1: reaches a Critical Cyber System, holds SSI or Restricted data at scale, or supports a High-criticality BIA process); annual SOC 2 Type 2 or equivalent review with CUEC mapping and a bridge letter for Tier 1; security and incident notice terms (24 hours for Tier 1 OT vendors); the CIP measures the vendor performs written into the contract (SD II.A.2 and II.A.3); remote access only through the PAM jump host; exit and data return terms | SA-4, SA-9, SR-2, SR-6 |
| STD-04 | **Field OT security standard** | POL-02, POL-04 | Director of Signals and Communications with the OT security engineer | Draft in progress (gaps 1, 2, 3, 8) | 2027-03-31 | Zone model for the field (code line, voice radio, wayside monitoring, management) with OT firewalls at the 6 hub towers and deny-by-default rules at every site; external connection register; no always-on vendor or cellular inbound access; default credentials changed before connection; complete OT asset inventory with firmware versions; diagrams updated within 30 days of change | SC-7, AC-4, CA-3, CM-8, IA-5 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Chief Engineer | Draft in progress (gap 12) | 2026-12-31 | AI inventory; risk tiering per P10; security, legal, and safety review before use; no-training and deletion terms for any vendor receiving company data; approved-AI list with permitted data classes; human review of outputs; no AI output replaces an FRA-required inspection; bias testing for employment uses; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator, privileged, and shared account standard | POL-02 | Director of Information Technology | Existing (2023); update in draft adds shared field accounts and the MFA exception list | 2026-12-31 | 14-character minimum and banned list; MFA everywhere it is supported; phishing-resistant MFA for administrators and (from 2027-03-31) finance, HR, and IT users; shared account inventory, PAM vaulting, and rotation at each departure and at least yearly; MFA exception list with compensating controls and timeframes (SD III.C.1.b, III.C.2); break-glass accounts tested quarterly | IA-2, IA-5, AC-2, AC-6(2), AC-6(5) |
| STD-07 | **Contingency and recovery standard** | POL-03, POL-04 | Director of Information Technology with the Director of Network Operations | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); clean-room restore of CAD/CTC, BOS, and crew management each quarter with malware scanning of the restored image; delayed-replication snapshot for CAD/CTC; manual dispatch drill in CTC territory at least yearly; RSSM outage-mode drill yearly; annual failover of the BOS and backup NOC | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Director of Information Technology | Existing (2023); minor update | 2027-06-30 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for Restricted data and SSI; link encryption for code line and detector paths over leased circuits; company-managed keys for cloud workloads; separate backup keys; PTC keys managed by the host's system | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Cybersecurity Manager | Existing (2024); update in draft adds OT to the KEV review | 2026-11-30 | Monthly authenticated scans of IT; passive OT discovery; weekly review of the CISA Known Exploited Vulnerabilities catalog against IT **and OT** inventories; remediation targets: Critical 14 days internet-facing and 30 days otherwise, High 60 days; OT patches within 30 days of vendor certification; where OT cannot be patched, documented mitigations and a timeline (SD III.E.3) | RA-5, SI-2, SI-5 |
| STD-10 | SSI handling standard | POL-04 | Director of Safety, Security, and Hazmat | Existing (2022); update in draft | 2026-11-30 | Restricted SSI library as the only electronic store; need-to-know list reviewed quarterly; vendor need-to-know records; marking template for CIP and CAP documents and drafts; marking check before each TSA filing; destruction method; quarterly search of file shares for SSI copies | AC-3, MP-3, MP-4, MP-6 |
| STD-11 | Physical security and key control standard | POL-02 | Director of Safety, Security, and Hazmat | Existing (2023); update for wayside sites | 2027-06-30 | Badge access to the NOCs, data centers, and server rooms with quarterly review; restricted-keyway locks and key logs for tower shelters and signal housings; door alarms at tower shelters; keys recovered at termination; onboard PTC housing seals checked at the daily locomotive inspection | PE-2, PE-3, PE-6 |

**Summary:** 11 standards. 6 are new and in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-07). 5 exist and need updates (STD-06, STD-08, STD-09, STD-10, STD-11).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-09 (2026-11-30); STD-10 (2026-11-30); STD-03, STD-05, STD-06, STD-07 (2026-12-31) |
| 2027 Q1 | STD-02 (2027-01-31); STD-01, STD-04 (2027-03-31) |
| 2027 Q2 | STD-08, STD-11 (2027-06-30) |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process; TSA-approved CIP (SSI)
