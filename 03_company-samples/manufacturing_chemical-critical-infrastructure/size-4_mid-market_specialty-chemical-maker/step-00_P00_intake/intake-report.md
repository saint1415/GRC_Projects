# Intake Report: Cris Santos Company | Chemical | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager; Port plant, Inland plant, Distribution center and corporate headquarters in Florida) |
| Intake window | 2026-06-15 to 2026-07-02 (one late answer received 2026-07-08) |
| Collected by | GRC Analyst, with the Information Security Manager (CySO) and the OT Security Engineer |
| Approved | Chief Operating Officer, 2026-09-22 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-06. It covers the organization, the IT, OT and cloud systems at all four sites, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

Records that are SSI (the Facility Security Plan sections) were reviewed on site with the Facility Security Officer and are described here only at the level needed to cite them.

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-009 | Identity provider; privileged access vault; HR and payroll system; DCS security configuration; Inland SCADA server; loading bay card system; remote access gateway | 2026-06-22 to 2026-06-30 |
| Devices, OT networks and patching | EV-010 to EV-018 | EDR and endpoint consoles; OT asset records and allowlisting console; OT sensor; OT engineering library; firewall management; Inland network configuration; DCS vendor portal; scanning platform; penetration test report | 2026-03-31 to 2026-06-30 |
| Cloud and backups | EV-019 to EV-021 | Cloud organization console; backup account; OT backup server and fire safe log | 2026-06-30 |
| Monitoring and incidents | EV-022 to EV-025 | MSSP portal and contract; DCS log settings; incident register | 2026-06-26 to 2026-06-30 |
| Maritime security and the USCG rule | EV-026 to EV-030 | FSO files; terminal office; General Counsel files; CySO project folder; training platform | 2026-06-22 to 2026-06-30 |
| Contractors, policies and governance | EV-031 to EV-033 | Badge system and contractor files; intranet policy library; corporate secretary files | 2026-06-22 to 2026-06-30 |
| Process safety and hazmat | EV-034 to EV-041 | RMP and process safety files; MOC system; EHS files; ERP shipping records; legacy CSAT records | 2026-06-23 to 2026-06-30 |
| Suppliers, contracts and insurance | EV-042 to EV-046, EV-058 | CFO files; ERP accounts payable; contract register; vendor management files | 2026-06-24 to 2026-07-08 |
| Applications, data and facilities | EV-047 to EV-051 | SaaS and cloud admin consoles; file services; productivity suite; physical security systems; disposal records | 2026-06-30 to 2026-07-01 |
| Business volume and TTRS | EV-052 to EV-055 | ERP general ledger and reports; TTRS account and code repository | 2025-12-31 to 2026-06-30 |
| AI tools and benefits | EV-056, EV-057 | Accounts payable, identity provider app list and web proxy logs; HR benefits files | 2026-01-01 to 2026-06-29 |

## 3. Observations by area
**Users and access.** Workforce accounts in the identity provider come from the HR system feed, and MFA is registered on every active IT user account. Push with number matching is the only MFA method, including for administrators (EV-001, EV-002). Directory and cloud administrator credentials sit in a vault. OT administrators use credentials separate from their IT accounts, and no ERP account works outside single sign-on (EV-003). HR recorded 850 employees, 96 terminations and 41 internal transfers in the 12 months to 2026-06-30 (EV-004). The termination checklist disables identity provider accounts automatically, while DCS, SIS and terminal accounts and loading bay driver cards are manual steps (EV-005). The DCS has 186 local user accounts. Engineering accounts have been named since 2024, and operators share one account per console position (EV-006). At the Inland plant, operators share HMI logins and PLC and HMI passwords follow vendor default-style patterns (EV-007). OT accounts and driver cards are reviewed once a year, last in 2025-11 (EV-008). The remote access gateway has 41 named accounts with MFA, per-session approval and recording, and a written justification for each vendor path. No session review records were provided (EV-009).

**Devices, OT networks and patching.** All 640 office endpoints run EDR monitored by the MSSP (EV-010). Of 74 OT workstations, the 8 Port operator stations and 2 EWS have application allowlisting. Nine OT workstations run an end-of-support operating system, and no approved hardware, firmware and software list was provided (EV-011). The Port OT sensor has found 412 assets. Its alerts go by email to the OT Security Engineer, and the Inland plant has no sensor (EV-012). The 2023 architecture puts the Port plant into zones behind a firewall pair. The network map leaves out the loading bay controllers and a second tank gauging interface (EV-013). There are 214 firewall rules, three conduits cross the IT/OT boundary, and no Port OT address is reachable from the internet (EV-014). At the Inland plant, an access list lets the office VLAN reach the SCADA server, and the integrator's remote desktop tool runs at all times with no MFA (EV-015). The DCS is one major release behind. OT patches go in at the annual turnaround (last 2025-10), and no record compares OT assets with the KEV catalog (EV-016). IT and the OT DMZ are scanned quarterly (EV-017). The March 2026 penetration test covered internet-facing IT only (EV-018).

**Cloud and backups.** The landing zone has 5 accounts with guardrails, an organization trail and posture monitoring in each (EV-019). Cloud backups go to a separate account in a second region with write-once retention. LIMS was restored in 6 hours in 2026-04, and no restore test is recorded for TTRS or file services (EV-020). DCS, batch and SIS configurations are exported nightly and copied weekly to media in the Port plant fire safe. One operator station restore (2025-03) is the only OT restore on record (EV-021).

**Monitoring and incidents.** The SIEM collects IT, cloud, identity, firewall, gateway and historian logs. The MSSP watches IT and cloud alerts around the clock, its statement of work excludes OT, and there are no review records for the IT/OT conduit logs (EV-022, EV-023). DCS audit trails are local, roll over after 90 days, and can be cleared by a DCS administrator (EV-024). The 2024 incident response plan covers IT incidents. The OT runbook is a draft, and OT sensor events are kept in email (EV-025).

**Maritime security and the USCG rule.** The Coast Guard-approved FSP covers the whole Port plant. Its reporting procedures cover breaches of security, suspicious activity and TSIs, with no report under 33 CFR 6.16-1, and its quarterly drills have had no cyber scenario (EV-026). The barge dock receives sulfuric acid and caustic soda in bulk under a Part 154 operations manual (EV-027). The Information Security Manager was designated CySO in writing on 2025-10-01 (EV-028). The Cybersecurity Plan draft has 4 of 14 sections drafted, about 30% complete by the tracker, and the Cybersecurity Assessment has not started (EV-029). 371 of 430 Port employees completed the USCG training module by the 2026-01-12 deadline, and the training platform holds no contractor records (EV-030).

**Contractors, policies and governance.** 40 contractors have OT access. Their files hold safety evaluations and no cyber evaluation (EV-031). The 2024 policy set has no standards for OT security, configuration, logging or vendors, and the acceptable use policy is the only rule on AI (EV-032). A vCISO has run the program since 2023 and reports to the audit committee each quarter. The co-sourced internal audit firm performs an annual IT audit (EV-033).

**Process safety and hazmat.** The Port plant's RMP update was submitted 2024-06-20 (Program 3, responding source), and the process safety information sets the maximum intended inventories. The Inland plant buys products below the RMP and legacy CFATS concentrations (EV-034). The HAZOPs (Ammonia Unit 2023-05-18, Peroxide Unit 2022-10-12) list no cyber-initiated scenarios (EV-035). SIS logic is compared with the approved copy at the yearly proof test (last 2025-11-04). Procedures cover loss of DCS view but not suspected manipulation (EV-036). MOC has covered DCS and SIS changes since 2024, and terminal PLC and firewall changes are not listed as MOC-controlled (EV-037). The 2025-04-15 compliance audit has 2 of 14 findings open (EV-038). Release notification runs from the emergency response plan. The community notification service is launched from a web console, and the 2026 calendar lists the RMP tabletop for 2026-11-17 (EV-039). The DOT security plan dates from 2019, was last revised in 2021, and has no 2025 review entry (EV-040). Legacy CFATS records show a Top-Screen in 2008 and a Site Security Plan until the authority lapsed on 2023-07-28 (EV-041).

**Suppliers, contracts and insurance.** Cyber insurance has a $15 million limit and a $500,000 retention (EV-042). The company paid about 260 vendors in 12 months (EV-043). 52 have system or data access, and reviews are recorded only at onboarding (EV-044). The TTRS master services agreement commits 99.5% monthly availability and 72-hour incident notice, and 40 older customer agreements lack the notice term (EV-045). SOC 2 reviews were on file for the cloud provider and ERP vendor at intake. The identity provider review followed on 2026-07-08, so 3 of 11 key vendors have been reviewed (EV-046, EV-058).

**Applications, data and facilities.** A second approval has been required for hydrogen peroxide customer master data changes since 2025 (EV-047). Shares holding the FSP, the Facility Security Assessment, legacy CVI and formulations are open to 65 users, file access logging is off, and there is no data loss prevention tool (EV-048). The generative AI assistant is enabled for 640 users and searches whatever each user can reach (EV-049). The control room, OT server room and rack rooms are badge-controlled. The video management server sits on the business network (EV-050). Returned TTRS gateways have no wipe entries (EV-051).

**Business volume and TTRS.** FY2025 revenue was about $410 million over 250 shipping days, about $1.64 million per shipping day (EV-052). The company serves about 2,400 customers, including 160 water utilities, and TTRS monitors 420 customer tanks (EV-053). 37% of TTRS gateways run outdated firmware with one shared local password per model. TTRS runs in one region, and availability against the 99.5% commitment is not reported (EV-054). Replenishment rule and code changes have no peer review, test or approval records (EV-055).

**AI tools and benefits.** Five AI uses were found (AI-001 to AI-005), none with a risk assessment on file. Web proxy logs show staff visiting public generative AI sites (EV-056). The employee health plan is fully insured (EV-057).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Identity provider SOC 2 review | GRC Analyst | 2026-06-22 | Received 2026-07-08 (EV-058) |
| Number of staff using public generative AI sites, and what they enter | Information Security Manager | 2026-06-29 | Not established at intake; P10 treats it as unknown |
| Port OT asset register reconciled to the sensor inventory | Controls Engineering Manager | 2026-06-30 | Reconciliation in progress at intake; the 2026-08-01 register is EV-069 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-004), revenue and volumes (EV-052, EV-053), backup and recovery records (EV-020, EV-021), the ERP vendor's recovery objectives (EV-046), TTRS commitments (EV-045), and dependencies from the asset and vendor registers |
| P02 SSP | The PCBMS boundary from the asset inventory; as-found OT configuration from EV-006, EV-009, EV-011 to EV-014, EV-021, EV-024 and EV-036 |
| P04 Cloud mapping | Cloud and SaaS components (EV-019, EV-020, EV-047 to EV-049, EV-054) and provider assurance (EV-046, EV-058) |
| P01 Risk register | Likelihood inputs from the configuration exports, the OT sensor and scan records, the incident register (EV-025) and the threat briefing record (EV-026) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2024 policy set and the existing standards (EV-032) |
| P07 Control assessment | Populations to sample from (EV-004, EV-006, EV-009, EV-012, EV-014, EV-021, EV-030, EV-031) |
| P08 IR runbooks | Notification duties from the obligations register; FSP reporting (EV-026); contacts and contract terms from the vendor register and EV-045 |
| P09 SOC 2 | TTRS records (EV-054, EV-055), contracts (EV-045) and vendor assurance on file (EV-046, EV-058) |
| P10 AI governance | AI tools found (EV-043, EV-056) |
