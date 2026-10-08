# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but the company had few supporting standards. Staff and vendors had no measurable rules for OT security, configuration, logging, vendor risk, or secure development (intake policy library review, EV-033; P03 GV.PO-01; P01 R-039). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them (for example, the freeze-night manual start procedure under STD-07).

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it. OT standards are also signed by the Director of Irrigation and Water Resources and the Packinghouse Manager.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | IT Director | Draft in progress (EV-033, EV-020) | 2027-03-31 | Benchmark-based baselines for laptops, servers, cloud virtual machines, network devices, SaaS tenants, **SCADA servers, and HMIs**; no email, browsing, or vendor remote tools on SCADA servers; documented deviations with approval; monthly drift report; application allowlisting on SCADA servers and packinghouse line PCs | CM-2, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (EV-033, EV-026) | 2027-01-31 | Required event types per system class, including SYS-01 record edits, settlement changes, SCADA operator and engineering actions, and PLC program downloads; OT events collected passively where devices cannot forward logs; 1 year searchable and 3 years archived; MSSP call within 30 minutes on high severity; egress volume alerts; weekly tally edit review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Security Manager | Draft in progress (EV-048) | 2026-12-31 | Supply chain risk strategy; vendor tiers (Tier 1: privileged or OT access, personal information at scale, or supports a High-criticality process; Tier 2: limited data, no privileged access; Tier 3: no data or access); purchasing gate for SaaS, OT equipment, and AI services; Tier 1 annual SOC 2 Type 2 (or equivalent) review with CUEC mapping; Tier 2 reassessed every 2 years; contract schedule with named accounts, brokered access, breach notice within 72 hours, secure development terms for code vendors, data-use limits, and exit and deletion terms | SA-4, SA-9, SR-2, SR-3, SR-6, RA-3(1), PM-30 |
| STD-04 | **OT security standard** | POL-02, POL-04 | Director of Irrigation and Water Resources, with the Packinghouse Manager and IT Director | Draft in progress (EV-015, EV-013) | 2027-03-31 | Zones and conduits per SP 800-82 Rev. 3 section 5 (pump-station, fertigation, packinghouse control, and SCADA zones; deny-by-default rules); complete OT inventory kept current by passive discovery; default credentials changed before connection; vendor access only through the broker; change log for PLC logic, HMI screens, fertigation recipes, and ripening programs with a second reviewer; offline versioned program backups after every change; passive scanning only on live PLCs; OT alarm triage criteria for security events; hash check of vendor media; restricted keys and panel door alarms at pump stations | CM-3, CM-8, SC-7, AC-4, IA-5, MA-4, PE-3, SI-4 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Precision Agriculture Manager, with the vCISO | Draft in progress (EV-065) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, and business review before use; no-training and deletion terms for vendor tools; human approval before AI acts on irrigation, spraying, or settlements unless P10 approves automatic action with plausibility limits; monitoring metrics and decommissioning criteria | PM-9, SA-9, PL-4, RA-3, SI-10 |
| STD-06 | **Authenticator and privileged access standard** | POL-02 | IT Director | Draft in progress (EV-007, EV-006) | 2027-03-31 | 14-character minimum and banned list; MFA for all workforce access; phishing-resistant MFA for administrators; named crew accounts with device PINs; vaulted and rotated OT and service account credentials; just-in-time privileged access for directory, SYS-01, ERP, cloud, and SCADA; break-glass accounts tested quarterly; quarterly access reviews | IA-2, IA-5, AC-2, AC-6(2), AC-6(5) |
| STD-07 | **Contingency and recovery standard** | POL-03, POL-04 | IT Director, with the OT owners | Draft in progress (EV-024, EV-025, EV-039) | 2026-12-31 | Recovery objectives from the BIA (P05); recovery procedures for SCADA, PLCs, packinghouse controls, the farm data hub, and the grower portal; freeze-night manual start procedure tested each November; quarterly restore tests; validation checklist before automatic operation resumes; paper downtime procedures for tally, pesticide displays, H-2A statements, and FDA record requests; annual DR exercise | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data, including the local SCADA backup device; company-managed keys for cloud workloads; separate backup keys; review of radio and LoRaWAN encryption | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated IT scans (moving from quarterly); weekly known-exploited vulnerability review; Critical fixed in 7 days on internet-facing systems and 30 days otherwise; High in 60 days; OT: passive identification, ICS advisory matching, integrator-tested quarterly SCADA patching in maintenance windows, compensating controls for unsupported HMIs | RA-5, SI-2, SI-3, SI-5 |
| STD-10 | Facility and field site physical security standard | POL-02 | Director of Irrigation and Water Resources, with the IT Director | Draft in progress | 2027-03-31 | Badges for the IOC, server rooms, and packinghouse control room; restricted keys for pump stations, fertigation skids, and chemical storage; key list reviewed each season; panel door switches wired to SCADA alarms; visitor logs | PE-2, PE-3, PE-6 |
| STD-11 | **Secure development standard** | POL-01 | Vice President of Grower Services | Draft in progress (EV-053) | 2027-03-31 | Secure design principles for the grower portal; static analysis and dependency scanning in the pipeline; settlement regression tests against prior weeks; company approval before production deployment; second review of every settlement logic change; developers on managed devices or virtual desktops; annual penetration test | SA-8, SA-11, SA-15, CM-3, CM-5 |

**Summary:** 11 standards. Nine are new and in draft: STD-01 to STD-07, STD-10, and STD-11. STD-08 and STD-09 exist from 2024 and need updates. The 5 standards the 2024 library did not include (OT security, configuration, logging, vendor risk, secure development; EV-033) are STD-04, STD-01, STD-02, STD-03, and STD-11.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency and recovery (freeze procedure first, by 2026-11-30); STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 OT security; STD-06 Authenticator and privileged access; STD-08 Encryption; STD-10 Facility and field sites; STD-11 Secure development |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
