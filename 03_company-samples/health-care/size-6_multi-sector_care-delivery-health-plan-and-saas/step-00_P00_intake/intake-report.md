# Intake Report: Cris Santos Company Holdings | Health Care | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company; Care Delivery, Health Plan and Health-Tech SaaS divisions; corporate shared services) |
| Intake window | 2026-03-30 to 2026-04-24 |
| Collected by | Group GRC team (Group CISO's office), with the three division security and compliance leads and the Group Chief Privacy Officer |
| Approved | Board risk committee, 2026-09-10, with the other deliverables |

## 1. Purpose and scope
Intake collected the group's own records before any assessment work began on 2026-05-01. It covers the legal entities, the systems that create, receive, maintain or transmit PHI in each division and in corporate shared services, the suppliers that touch them, and the rules that may bind each entity. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Items are grouped by division: the title of each row starts with Group, Group Data Platform, Care Delivery, Health Plan or Health-Tech SaaS. Later steps add their own fieldwork evidence (interviews, document reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analyses (P03) and the control assessment (P07).

## 2. Sources collected
| Division | Area | Evidence IDs | System of record | As of |
|---|---|---|---|---|
| Group | Entities, workforce and revenue | EV-001 to EV-004 | Entity management system; HR system; ERP and Form 10-K; legal contract system | 2025-12-31 to 2026-03-31 |
| Group | Identity and access (SYS-G1) | EV-005 to EV-009 | Identity platform, identity governance and PAM consoles; endpoint and zero-trust consoles | 2026-03-31 |
| Group | Security operations (SYS-G2) | EV-010 to EV-014 | SIEM; case management; EDR; scanner and patch consoles; penetration test report | 2026-03-20 to 2026-03-31 |
| Group | Policies and common controls | EV-015 to EV-017 | Policy repository; GRC tool | 2026-03-31 |
| Group | Cloud platform (SYS-G3) | EV-018 to EV-024 | Cloud consoles and asset inventory; guardrail service; firewall management; key management; backup vault; TLS scanner | 2026-03-27 to 2026-03-31 |
| Group | Group Data Platform | EV-025 to EV-030 | GDP catalog and policy engine; pipelines; warehouse; privacy office records; document vault | 2026-02-27 to 2026-03-31 |
| Group | Incident, disclosure, risk and audit | EV-031 to EV-035 | SOC library; SEC filings; board minutes; GRC tool; internal audit | 2026-01-15 to 2026-03-31 |
| Group | Workforce, vendors, AI and records | EV-036 to EV-044 | Learning system; HR system; vendor master and third-party risk tool; vendor portals; procurement and SaaS discovery; records management | 2025-01-15 to 2026-04-15 |
| Care Delivery | Sites, networks, systems, plans, contracts, patient app, AI | EV-045 to EV-057 | CMDB and biomedical system; network documentation; EHR and legacy EHR consoles; continuity library; contract management; practice management reporting; badge system; site walk-throughs; SYS-D4 console | 2025-11-30 to 2026-04-14 |
| Health Plan | Licenses, standards, backups, logs, UM model, portals, vendors | EV-058 to EV-067 | Regulatory affairs; policy library; compliance records; backup console; application consoles; model registry and UM minutes; portal consoles; vendor management | 2024-03-31 to 2026-03-31 |
| Health-Tech SaaS | Contracts, SOC 2, subcontractors, AI feature, architecture, support | EV-068 to EV-077 | Contract management; compliance office; vendor management; change system and release notes; architecture repository; build pipeline; support tool | 2025-09-30 to 2026-04-15 |

## 3. Observations by area
**Entities and scale.** The holding company is an SEC registrant. Care Delivery and the Health Plan are legally separate subsidiaries; no affiliated covered entity designation is recorded; corporate shared services sit in the parent (EV-001). The workforce is 45,000: Care Delivery about 20,000, Health Plan about 14,000, SaaS about 6,000, corporate about 5,000 (EV-002). FY2025 revenue was about $18 billion: Care Delivery $7.2 billion, Health Plan $9.6 billion in premiums, SaaS $1.2 billion (EV-003). The intercompany BAAs were signed in 2024 (Care Delivery) and 2019 (Health Plan, before the Group Data Platform); the Care Delivery BAA does not mention the white-label practices' PHI (EV-004).

**Group identity and access.** All 45,000 workforce identities use MFA with number matching; administrators use hardware keys (EV-005). Identity governance runs joiner-mover-leaver workflows from HR events and quarterly certification; 34 Group Data Platform service accounts are kept in a separate spreadsheet outside certification; Care Delivery locum end dates are entered by hand (EV-006, EV-037). Privileged access is just in time through PAM with session recording (EV-007). The Q1 2026 certification was completed (EV-008).

**Group security operations.** The SOC runs 24x7. The legacy EHR at the 14 acquired practices and the Health Plan claims middleware are not in the SIEM data source list; account analytics cover interactive users only; egress rules are set at the hub, not per platform zone (EV-010). Health Plan incident cases use the Health Plan's own 2024 severity scale (EV-011). EDR covers managed endpoints, servers and cloud hosts (EV-012). Scans run weekly (EV-013), and the 2026-03 penetration test covered the platform and landing zones (EV-014).

**Policies and common controls.** The 2025 group policies are aligned to CSF 2.0; the library has no AI standard (EV-015). The Care Delivery and SaaS supplements are aligned to the 2025 policies; the Health Plan supplement was last aligned 2024-03 and has no owner or review date (EV-016). The Health Plan standards allow 90-day log retention and SMS codes on the broker portal (EV-059). The common control catalog lists 82 controls; inheritance is documented for Care Delivery and the SaaS, and no Health Plan matrix was provided (EV-017). The 2025 Health Plan assessment does not list inherited controls (EV-060).

**Group cloud platform.** Provider A hosts the landing zone, the Group Data Platform and division cloud workloads; provider B hosts SaaS production, the platform DR replica and the backup vault; some workloads run in one region (EV-018). 97% of resources meet the guardrail benchmarks (EV-019). Hub firewalls deny by default between division accounts (EV-020). Keys are per division and per zone; 9 platform service principals use static keys older than 1 year (EV-021). Backups are immutable, kept 35 days with monthly copies for 1 year, and restored monthly on a sample (EV-022). Storage is encrypted at rest (EV-023), and endpoints accept TLS 1.2 or higher only (EV-024).

**Group Data Platform.** Care Delivery and Health Plan PHI tables share storage areas, and purpose tags cover 61% of tables (EV-025). SaaS exports land in staging before de-identification, and staging is not purged on a schedule (EV-026). 12 of 34 service accounts can read every zone, and 48 analysts hold standing roles in both covered-entity zones (EV-027). Feeds between the divisions are approved one at a time with no minimum-necessary protocol attached (EV-028). The 2026-02 DR test met the 24-hour RTO for a region failover; it did not include recovery after ransomware (EV-030).

**Incident notification, disclosure and risk.** The draft multi-regulator notification matrix has no state insurance regulator contacts or customer BAA terms and has not been exercised; exercises to date are technical (EV-031). The disclosure committee charter has no written materiality criteria for a multi-division incident (EV-032). The board risk committee receives quarterly cyber reports (EV-033). The 2025 risk registers and the risk strategy are on file (EV-034).

**Workforce, vendors and AI.** Training completion is 98.7%, with monthly reminders and quarterly phishing exercises (EV-036). The vendor program is tiered; onboarding does not screen for covered persons under 28 CFR Part 202 (EV-039); vendor SOC 2 reports are on file for the cloud providers, identity, EHR and catalog vendors (EV-040). AI in use: the AI scribe, EHR predictive models, the UM model, the fraud, waste and abuse model, care summary assist (released 2026-04-15), a coding assistant and an enterprise assistant pilot; an imaging AI tool is in procurement (EV-041). Division retention schedules set different periods for security records (EV-043).

**Care Delivery.** 160 clinic sites, 14 ASCs, 22 imaging centers and 2 labs; 41 devices on unsupported operating systems; the device list for acquired practices is partial (EV-045). LIS and PACS servers at 23 older sites share a flat management network with workstations; guest Wi-Fi at 9 sites is not separated; 5 ASCs have a single core switch (EV-046, EV-047). Report-writer rights were granted broadly in the 2024 EHR migration; privacy monitoring alerts are reviewed weekly (EV-048). The legacy EHR at the 14 acquired practices uses local passwords, is not federated, and keeps its logs locally (EV-049). Continuity plans assume short outages and do not list the acquired practices (EV-050). Two imaging vendors hold persistent remote tunnels; the EHR contract sets RTO 4 hours (EV-051). 85% of claims go through one clearinghouse, and payment changes are verified by email only at 3 regional offices (EV-052). There are about 2.1 million active patients, about 210,000 of them also Health Plan members (EV-053). Facility, destruction and wipe records are on file; locked shred bins are not in all exam areas (EV-054, EV-055). Patient MFA on SYS-D4 is optional, and the 38 white-label practices ask for a SOC 2 report by the end of 2027 (EV-056). The AI scribe serves about 400 providers with verbal consent; the decision support inventory lists EHR tools only (EV-057).

**Health Plan.** HMO and insurer licenses in 6 states, none in New York; about 540,000 Medicare Advantage and 360,000 commercial members (EV-058). The claims core restore is tested once a year, last 2026-03, and its runbooks sit on the claims file share (EV-061). Claims, UM and portal applications keep logs 90 days; the claims middleware has been out of vendor support since 2025 (EV-062). The UM model auto-approves about 38% of requests, routes the rest with a recommendation, and cannot deny; UM committee minutes to 2026-03 do not mention it; there is no subgroup monitoring of auto-approval rates (EV-063). Member MFA is optional, and 4,200 broker accounts may use SMS codes (EV-064). 14 delegated vendors are reviewed yearly (EV-065).

**Health-Tech SaaS.** About 420 customers and 12 million patients' records; standard BAA notice is 10 calendar days for breaches, 72 hours for 42 customers; 97 pre-2022 BAAs do not expressly permit de-identification (EV-068). The SOC 2 Type 2 report for the period ending 2025-09-30 covers Security, Availability and Confidentiality and predates the AI feature (EV-069). The model provider signed a subcontractor BAA in 2026-03 with zero data retention; no retention attestation has been received (EV-070). Care summary assist was released 2026-04-15 with change board approval and no privacy impact analysis attached; it logs requests by tenant, not by patient (EV-071). The service uses a shared database schema with tenant filters in application code (EV-072); pipeline secrets and customer API keys are long-lived (EV-073); support staff can search records without a ticket (EV-074). 3 of 12 offboarded customers waited more than 60 days for a deletion certificate (EV-076).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Health Plan inheritance matrix for group common controls | Health Plan security and compliance lead | 2026-04-06 | None exists; documented in P02 (POAM-015) |
| Confirmation that no affiliated covered entity designation exists | Group General Counsel | 2026-04-02 | Answered in P03 fieldwork by the 2026-08-14 legal memo (EV-089) |
| Medical device list for the 14 acquired practices | Care Delivery IT director | 2026-04-08 | Partial list received; carried into P03 (G-041) |
| Specialty clinical applications that use age, sex or other protected-trait inputs | Care Delivery chief medical information officer | 2026-04-10 | Not provided at intake; tools named in P03 interviews (EV-086); inventory incomplete (CD-018, POAM-023) |
| Model provider attestation of zero data retention | SaaS general counsel | 2026-04-09 | Not received; carried into P01 (HT-007) and P07 (POAM-018) |
| Workforce use of public generative AI tools outside the approved tools | Group CISO | 2026-04-20 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue by division (EV-003), patient and member volumes (EV-053, EV-058), backup and DR records (EV-022, EV-030, EV-061, EV-072), vendor recovery terms (EV-051), and dependencies from the asset and vendor registers |
| P02 SSP | The Group Data Platform boundary from the asset inventory; as-found configuration from EV-005 to EV-030; common controls from EV-017 |
| P04 Cloud mapping | Cloud and platform components (EV-018 to EV-030, EV-056, EV-072) and provider assurance (EV-040, EV-069) |
| P01 Risk registers | Likelihood inputs from configuration exports, inventories, contracts and plans in all four divisions (the `likelihood_basis` column) |
| P03 Gap analyses | The obligations register (which rules apply to which entity) and every observation above, compared with the requirements |
| P06 Policies | The 2025 group policies and standards (EV-015) and the division supplements (EV-016, EV-059) |
| P07 Control assessment | Populations to sample from (EV-002, EV-006, EV-011, EV-022, EV-025, EV-027) |
| P08 IR runbook | Notification duties per entity from the obligations register; the draft matrix (EV-031); BAA notice terms (EV-004, EV-068) |
| P09 SOC 2 | The SaaS SOC 2 report (EV-069), vendor reports (EV-040) and the white-label agreements (EV-056) |
| P10 AI governance | AI tools found (EV-041, EV-057, EV-063, EV-071) |
