# Intake Report: Cris Santos Company Holdings | Communications | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company; Telecom Carrier, Network Engineering Services and Tower and Fiber Infrastructure divisions; corporate shared services) |
| Intake window | 2026-03-30 to 2026-04-24 |
| Collected by | Group GRC team (Group CISO's office), with the three division security and compliance leads, the Carrier CPNI compliance officer and the Group Chief Privacy Officer |
| Approved | Board risk committee, 2026-09-17, with the other deliverables |

## 1. Purpose and scope
Intake collected the group's own records before any assessment work began on 2026-05-04. It covers the legal entities, the systems that hold CPNI, subscriber and landowner personal information, federal contract information, or network and lighting control functions in each division and in corporate shared services, the suppliers that touch them, and the rules that may bind each entity. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Items are grouped by division: the title of each row starts with Group, Telecom Carrier, Network Engineering Services or Tower and Fiber Infrastructure. Later steps add their own fieldwork evidence (interviews, document reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analyses (P03) and the control assessment (P07).

## 2. Sources collected
| Division | Area | Evidence IDs | System of record | As of |
|---|---|---|---|---|
| Group | Entities, workforce and revenue | EV-001 to EV-003 | Entity management system; ERP HR module and contractor register; ERP and Form 10-K | 2025-12-31 to 2026-03-31 |
| Group | Identity and access (SYS-G1) | EV-004 to EV-007 | Identity platform, identity governance and PAM consoles; endpoint and zero-trust consoles | 2026-03-31 |
| Group | Security operations (SYS-G2) | EV-008 to EV-012 | SIEM; case management; EDR; scanner and patch consoles; penetration test report | 2026-03-20 to 2026-03-31 |
| Group | Policies and common controls | EV-013 to EV-015 | Policy repository; GRC tool | 2026-03-31 |
| Group | Cloud platform (SYS-G3) | EV-016 to EV-020 | Cloud consoles and asset inventory; guardrail service and firewall management; key management; backup vault; TLS scanner | 2026-03-27 to 2026-03-31 |
| Group | Incident, disclosure, risk and audit | EV-021 to EV-024 | SOC library and legal; SEC filings; board minutes and GRC tool; internal audit | 2026-01-15 to 2026-03-31 |
| Group | Workforce, vendors, AI and records | EV-025 to EV-033 | Learning system; HR system; vendor master and third-party risk tool; vendor portals; procurement; legal contract system; AI discovery; records management | 2025-12-31 to 2026-04-20 |
| Telecom Carrier | Filings, customers, CALEA, CPNI, authentication, contact centers, OSS/BSS, management plane, CDRs, continuity, NOC, chatbot, deposit model | EV-034 to EV-052 | FCC filings; BSS and OSS reporting and consoles; lawful-intercept records; campaign tool; CCaaS and contracts; AAA and backup servers; lifecycle register; continuity library; NOC procedures; chatbot console; model registry | 2026-02-27 to 2026-04-15 |
| Network Engineering Services | MNO contracts, gateways, procedures, federal contracts, FCI enclave, project offices | EV-053 to EV-058 | Contract management; gateway consoles and PAM vault; MNO procedures; enclave account; facility records | 2026-03-31 |
| Tower and Fiber Infrastructure | Structures and RMUs, alarm center, leases and landowners, smart locks, fiber records | EV-059 to EV-063 | SYS-T2 inventory and structure registrations; continuity library; SYS-T1 and payment procedures; lock console; SYS-T3 | 2026-03-31 |

## 3. Observations by area
**Entities and scale.** The holding company is an SEC registrant with three divisions in wholly owned subsidiaries. The Carrier has 10 operating companies in 14 states, 2 of them acquired in 2024; no division lists operations in California, Colorado, Texas or Utah (EV-001). The workforce is 45,000, plus about 2,100 agents at two outsourced contact center vendors (EV-002). FY2025 revenue was about $18.0 billion: Carrier $12.4 billion, Engineering $2.3 billion external, Tower $3.3 billion (EV-003).

**Group identity and access.** All workforce and outsourced agent accounts use MFA with number matching, and IT administrators use hardware keys (EV-004). Identity governance runs from HR events; the outsourced vendors send agent leavers in a weekly file; inactive accounts are disabled after 45 days (EV-005). Privileged access is just in time through PAM; 3 OSS and BSS integrations use static secrets older than 1 year (EV-006). Remote access goes through the zero-trust service (EV-007).

**Group security operations.** The SOC runs 24x7 with 1 year of searchable logs and 6 years archived. Element logs from the 2 acquired regions, SYS-E1 gateway logs and RMU and smart lock logs are not in the SIEM source list (EV-008). One case register serves as the CPNI breach record; the Tower division uses its own 3-level severity scale; isolation playbooks have no step that checks 911 or lighting effects; no exercise has covered cross-division notification (EV-009). EDR covers endpoints, servers and cloud hosts (EV-010). Network elements and SBCs in the acquired regions are not in authenticated scanning, and the 14-day target for known exploited vulnerabilities was met for 97% of IT assets and 81% of network devices in 2026 (EV-011). The 2026-03 penetration test covered the portal, API gateway and cloud boundary (EV-012).

**Policies and common controls.** The 2025 group policies are aligned to CSF 2.0 (EV-013). The Engineering supplement (2026-03) permits persistent tunnels in its MNO remote access standard; the Tower standards date from 2023, have no owner, allow shared RMU passwords and use their own severity scale (EV-014). The common control catalog lists 102 controls; inheritance is documented for the Carrier and Engineering, and no Tower matrix was provided (EV-015).

**Group cloud platform.** Provider A hosts the landing zone and most Carrier, Engineering and Tower cloud workloads; provider B hosts the disaster recovery copies, the backup vault and the SYS-E1 gateways (EV-016). Firewalls deny by default between division accounts (EV-017). Storage is encrypted with customer-managed keys (EV-018). Backups are immutable, and tier 1 restores are tested each quarter (EV-019). External endpoints accept TLS 1.2 or higher only (EV-020).

**Incident notification, disclosure and risk.** The IR plan v2025 does not list FAA lighting reports, CALEA compromise reports or Engineering customer notices as reportable, and the group matrix has never been exercised (EV-021). The disclosure committee has not rehearsed a cyber materiality decision (EV-022). The risk strategy sets acceptance authority by level (EV-023), and internal audit plans the common control assessment for July and August (EV-024).

**Workforce, vendors, AI and records.** Outsourced agents are at 74% completion of the CPNI course, and no CPNI course is assigned to the affiliate operators on the service assurance platform (EV-025). Screening and termination records are on file (EV-026). The vendor master lists the suppliers in the vendor register (EV-027); SOC 2 reports are on file for the cloud providers and six other vendors (EV-028). Covered equipment screening is a manual requisition check with no field for the result (EV-029). No intercompany CPNI, interconnection or tenant agreement covers the shared service assurance platform or the SYS-E1 tunnels (EV-030). AI in use at intake: the chatbot, the deposit model, NOC anomaly detection, MNO triage, a design assistant, lease abstraction, an enterprise assistant, a coding assistant and an unregistered inspection imagery subscription (EV-031).

**Telecom Carrier.** CPNI certifications for all 10 operating companies were filed 2026-02-27, and the covered equipment certification is on file (EV-034). About 4.9 million mass-market accounts, 1.9 million voice lines and 41,000 enterprise accounts; about 1.4 million accounts are in Florida and 610,000 voice lines in the acquired regions (EV-035). The 2 acquired operating companies' SSI policies were not refiled after the 2024 merger and their appendix names a former employee (EV-036). Approval flags and the campaign tool are in place; the 2025-10 biennial notice does not name the receiving affiliates (EV-037). The legacy billing system sends no notice for address-of-record changes, and supervisors at one outsourced vendor can override the password prompt (EV-038); that vendor's contract has no 24-hour incident notice term (EV-039). A legacy role lets about 410 Engineering and 60 Tower operators read Carrier tickets on the shared service assurance platform (EV-040). In the acquired regions, about 38% of access elements and 22 SBCs use shared local administrator accounts (EV-041), element configurations are backed up to one server per region, and the lawful-intercept management path shares SYS-C5 segments (EV-042). 9 of 140 SBCs run releases past vendor support (EV-043). Object-level read logging is off on the CDR store (EV-044). The service assurance platform has no failover test with all three tenants (EV-045). PSAP contacts in the acquired regions were last confirmed in 2024 (EV-046). The chatbot has run since 2025-11-03 for signed-in users (EV-047). Online and chat orders have no adverse action notice step for deposits (EV-048).

**Network Engineering Services.** 64 MNO customers; 41 contracts require 24-hour and 23 require 72-hour incident notice; 37 require a SOC 2 Type 2 report by the end of 2027 (EV-053). SYS-E1 keeps persistent tunnels into 64 customer networks and the Carrier's acquired-region management plane, with 6 shared administrator accounts (EV-054). Customer notices are sent by email with no register (EV-055). 12 federal contracts carry FAR 52.204-21, 52.204-23 and 52.204-25; there are no DoD contracts (EV-056). The FCI enclave is limited to 140 named staff (EV-057). Visitor logs and disposal certificates were provided for 4 of the 6 project offices (EV-058).

**Tower and Fiber Infrastructure.** About 6,200 lit structures; about 1,100 legacy RMUs use public IP addresses and shared credentials over one cellular provider (EV-059). The contingency plan v2023 has no written fallback to daily observation, and outage records are kept in spreadsheets (EV-060). SYS-T1 holds data for about 11,800 landowners; the lease management vendor contract has no incident notice term, and bank changes are accepted by email (EV-061). Crew members share smart lock credentials (EV-062). Route maps are shared with all three divisions (EV-063).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Tower inheritance matrix for group common controls | Tower security and compliance lead | 2026-04-06 | None exists; documented in P02 (POAM-021) |
| Recorded results of covered equipment screening for 2025 and 2026 purchases | Group procurement director | 2026-04-07 | No records kept (EV-029); carried into P03 (G-047, NE-G18) and P07 (SR-3) |
| MNO customer notice register | Engineering MNO general manager | 2026-04-09 | None exists (EV-055); carried into P03 (NE-G23) and P09 (CC7.4) |
| Counsel's position on whether the dark fiber leases are common carriage | Group General Counsel | 2026-04-08 | Answered in P03 fieldwork by the 2026-07-20 counsel memo (EV-084) |
| Workforce use of generative AI tools outside the approved tools | Group CISO | 2026-04-20 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue by division (EV-003), customer and line counts (EV-035), backup, DR and continuity records (EV-019, EV-042, EV-045, EV-060), NOC and outage procedures (EV-046), and dependencies from the asset and vendor registers |
| P02 SSP | The OSS/BSS boundary from the asset inventory; as-found configuration from EV-004 to EV-020 and EV-034 to EV-052; common controls from EV-015 |
| P04 Cloud mapping | Cloud components (EV-016 to EV-020, EV-040, EV-044, EV-054, EV-059) and provider assurance (EV-028) |
| P01 Risk registers | Likelihood inputs from configuration exports, inventories, contracts and plans in all four parts of the group (the `likelihood_basis` column) |
| P03 Gap analyses | The obligations register (which rules apply to which entity) and every observation above, compared with the requirements |
| P06 Policies | The 2025 group policies and standards (EV-013) and the division supplements (EV-014) |
| P07 Control assessment | Populations to sample from (EV-002, EV-005, EV-026, EV-029, EV-041, EV-043, EV-059) |
| P08 IR runbook | Notification duties per entity from the obligations register; the IR plan and matrix (EV-021); contract notice terms (EV-039, EV-053, EV-061) |
| P09 SOC 2 | MNO customer commitments (EV-053), the Engineering inheritance matrix (EV-015) and vendor reports (EV-028) |
| P10 AI governance | AI tools found (EV-031, EV-047, EV-048) |
