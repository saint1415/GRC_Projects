# SOC 2 Readiness Summary: Cris Santos Company Holdings | Dams | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Hydro, Constructors, Engineering, and corporate shared services) |
| Tier / Vertical | Multi-Sector / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is AICPA's |
| Scoping | Per division (section 1). One readiness report: the Engineering division's **Dam Safety Monitoring Service (DSMS, SYS-E1)** in `soc2-readiness.csv`. Hydro and Constructors are out of scope, with reasons |
| Categories in scope (DSMS) | Security, Availability, Confidentiality, Processing Integrity. Privacy is out of scope |
| Target report | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 (POAM-026) |
| Prepared | 2026-09-10 by the Engineering security and compliance lead and the DSMS General Manager, reviewed by the Group Chief Risk Officer's assurance team |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. For each division the question is whether it runs a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Engineering | **DSMS**: collects, stores, and analyzes dam safety instrument data for 61 external clients (212 dams) and 68 Hydro dams; includes the AI-001 anomaly model | **Yes.** Clients rely on DSMS data, alerts, and availability as part of their own dam safety programs. **23 contracts renewing in 2027 require a Type 2 report** | **In scope.** First readiness assessment | Security, Availability, Confidentiality, Processing Integrity | Type 1 as of 2027-03-31; Type 2 for 2027-04-01 to 2027-09-30 |
| Engineering | Design, inundation mapping, Part 12D inspections, A-E contracts | No. These are professional services delivered as sealed reports and drawings; clients do not rely on Engineering's systems for their own controls | Out of scope. Client CEII duties are covered by NDAs (P03 EG-008) | n/a | n/a |
| Hydro | Generation, ancillary services, recreation | **No.** Hydro sells energy and capacity into Balancing Authority Areas. Counterparties receive schedules and telemetry; Hydro hosts and operates nothing for them | **Out of scope** (reasons below) | n/a | n/a |
| Constructors | Construction and rehabilitation | **No.** Owners buy built works. The project platform (SYS-C1) is a vendor SaaS that owners use under their own terms; Constructors does not offer it as a service | **Out of scope** (reasons below) | n/a | n/a |

**Why Hydro is out of scope:**
1. **No user entities.** The Balancing Authorities and Transmission Operators do not build controls on Hydro systems; ICCP data exchange is governed by CIP-012-2 and operating agreements.
2. **Assurance comes from regulators.** Hydro's assurance is regulatory: SERC CIP audits (last 2025-04), FERC dam security inspections and Annual Security Compliance Certification Letters, Part 12D independent consultant inspections, and the independent ODSP audit (P03).
3. **Hydro is a user entity of the DSMS.** For its 68 dams, Hydro relies on an Engineering service. It will receive the DSMS SOC 2 report like any client and must run the complementary user entity controls in section 2 (00_company-facts.md section 2: the DSMS is treated as an intercompany service provider).

**Why Constructors is out of scope:**
1. **No user entities.** Owners and agencies buy construction. They assess Constructors through contract terms, prequalification, and, for USACE, federal requirements.
2. **The relevant assurance is CMMC.** For CUI work, the assurance product is the CMMC Level 2 assessment of the Federal Projects Enclave by a C3PAO, scheduled 2027-03-15 (P03; POAM-023). A SOC 2 report would not replace it.
3. **Revisit trigger:** if Constructors starts operating systems for owners after handover (for example, operating a client's plant control system under a service contract), assess whether a SOC 2 or SOC 1 report is needed.

**Other assurance options considered.** The vertical overlay names no sector alternative to SOC 2. Some DSMS clients asked about ISO/IEC 27001 certification; Engineering chose SOC 2 because the renewing contracts name it.

## 2. System description (DSMS scope)
- **Services:** collection of dam safety instrument readings from client gateways and Hydro historians (about 14,900 instruments), storage, trend displays, rules-based threshold alerts, AI-001 anomaly alerts (Hydro since 2025-10; 19 client pilots since 2026-03), and reports.
- **Infrastructure and software:** DSMS application, ingestion, alerting, and the AI-001 model service on cloud provider A (warm standby region); backups to the group immutable vault on provider B.
- **Group shared services included in the system:** identity (SYS-G1), SOC and vulnerability management (SYS-G2), cloud platform guardrails (SYS-G3), HR screening and training. They are run by the same corporate group under intercompany agreements, so they are described and tested as part of the system, not carved out. Their evidence is the common control testing in P07.
- **Subservice organization (carve-out):** cloud provider A (and provider B for the backup vault). The service auditor will rely on their SOC reports; Engineering reviews them every year (CC9.2).
- **People:** the DSMS team, the Director of Data Science's team, and group SOC, identity, and cloud staff.
- **Data:** client instrument readings, alert histories, and client CEII (instrument layouts and inundation data). No consumer personal information.
- **Complementary user entity controls (clients, including Hydro):**
  - provision and remove their own users and keep MFA on;
  - validate the data their gateways send and secure the gateways;
  - **keep dam safety decisions, trigger-point checks, and manual review schedules with their own dam safety engineers**: the DSMS and AI-001 support those decisions and do not make them (P10);
  - review DSMS alerts and acknowledge them within their own procedures;
  - for Hydro: keep the data path one-way from OT (POAM-005).

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 6 | 2 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **31** | **9** | **3** | **18** |

**Why so many Ready criteria for a first-time report:** control environment, risk, monitoring, identity, SOC, and cloud criteria are met by group common controls that P07 already tested, and the DSMS met its availability commitment (99.93% over 12 months against 99.5%, DR tested 2026-05).

**Not ready:**
- **CC2.3** (communication with external parties): no system description; threshold and model changes made without the client notice the contracts promise (EG-005); the AI-001 addendum omits the back-test rate and the rule that the model does not replace manual review (EG-007); a 2025 brochure claims the model never misses a seepage event (EG-015).
- **CC8.1** (change management): 41 threshold changes in 2026 without review and 3 AI-001 releases before 2026-08 without a defined validation test (P07 CM-03 and SA-11 findings; POAM-012).
- **PI1.3** (system processing): the same root cause as CC8.1. Processing logic is exactly what clients rely on.

**Partially ready:** CC2.1 and CC9.2 (the Hydro data exchange has no agreement or documented flows), CC3.4 (Hydro's reduction of manual readings at 31 dams was not assessed as a significant change), CC5.3 (the Engineering supplement lacks DSMS change control and AI rules), CC6.6 (two-way replication from 17 Hydro plants), CC7.4 (the 48-hour client notice has never been exercised), C1.1 (client CEII in open project shares), PI1.1 (processing specifications and AI-001 limits not published to clients), and PI1.2 (no check for plausible false data from a compromised client gateway).

**Why Processing Integrity is in scope.** Clients use DSMS alerts inside their dam safety programs. Whether readings are complete and alerts are produced by approved logic is the question their engineers and regulators ask. Including it makes the change control gap visible to the service auditor instead of hiding it.

**The main risk to the timeline.** CC8.1 and PI1.3 must operate from 2027-04-01 for the Type 2 period. If the change control process is not live by 2026-12-31, the Type 1 date moves and some 2027 renewals would close without a Type 2 report (EN-007).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect | Owner |
|---|---|---|---|
| 2026 Q4 | CC8.1, PI1.3, CC5.3 | Change procedure for thresholds and models; first change records with dam safety impact review and client notices; updated Engineering supplement (POAM-012) | Director of Data Science; DSMS General Manager |
| 2026 Q4 | CC2.3, PI1.1 | System description draft; AI-001 addendum amended; brochure withdrawn; processing specifications published | DSMS General Manager with counsel |
| 2026 Q4 | CC2.1, CC9.2 | Intercompany agreement with Hydro and data flow diagrams (POAM-005) | DSMS General Manager; Director, OT Security |
| 2026 Q4 | CC3.4 | Significant-change assessment of Hydro's reliance on AI-001; weekly readings restored at the 31 dams (POAM-025) | Chief Dam Safety Engineer; DSMS General Manager |
| 2026 Q4 | CC7.4 | Client notice exercised in the 2026-11-17 tabletop (POAM-009) | DSMS General Manager; General Counsel |
| 2026 Q4 | C1.1 | Client CEII moved to restricted libraries; DLP rules (POAM-015) | Engineering security and compliance lead |
| 2027 Q1 | CC6.6, PI1.2 | One-way transfer at all 17 plants; gateway plausibility rules. Type 1 as of 2027-03-31 | Director, OT Security; DSMS General Manager |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the Type 2 period (2027-04-01 to 2027-09-30) | DSMS General Manager |

**Communication:** the DSMS General Manager sends all 61 clients a readiness letter with the 2027 timeline by 2026-11-30, and offers clients renewing before the Type 2 report the Type 1 report plus a bridge letter. Hydro's Chief Dam Safety Engineer receives the same letter as a client.
