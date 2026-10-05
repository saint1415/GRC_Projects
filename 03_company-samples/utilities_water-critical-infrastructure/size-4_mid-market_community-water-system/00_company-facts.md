# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, or standard, the citation is given. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed investor-owned water utility; board with an audit committee) |
| Business | Investor-owned water utility (NAICS 221310). It owns and operates **11 community water systems** in Florida, each with its own public water system identification number (PWSID): groundwater supply, treatment, storage, and distribution of drinking water. It also sells **Utility Services** (contract operations, remote monitoring, and billing) to 3 municipal water systems. No wastewater service |
| Location | Florida only. Headquarters and the **Regional Operations Center (ROC)**, a 24x7 control room, are in the administration building next to the North Plant of the Regional System |
| Covered systems (population served over 3,300) | **Regional System**: 171,400 persons, 66,800 connections. North Plant (WTP-R1, 22 million gallons per day (MGD), lime softening, 18 wells) and South Plant (WTP-R2, 10 MGD, brackish groundwater reverse osmosis, 8 wells); 9 storage tanks (24 million gallons), 12 booster stations; sells about 1.2 MGD wholesale to one neighboring city (a consecutive system). **Lakes System** (acquired 2023): 63,500 persons, 25,100 connections; WTP-L1 (9 MGD, aeration and chlorination, 10 wells), 3 tanks, 4 boosters. **Ridge System** (acquired April 2025): 27,400 persons, 11,200 connections; WTP-G1 (3.5 MGD, staffed 6:00 a.m. to 10:00 p.m.) and WTP-G2 (1.5 MGD, unstaffed, monitored remotely), 7 wells, 2 tanks, 2 boosters |
| Small systems (population 3,300 or fewer) | **8 small systems** acquired 2024-2025: 11,600 persons in total (600 to 2,900 each), 4,700 connections. Each has 1-3 wells, a chlorination skid with a well controller, a hydropneumatic or ground storage tank, and a cellular modem reporting to the ROC. Roving operators visit daily |
| Treatment chemicals | Sodium hypochlorite at every plant; liquid ammonium sulfate (chloramination) and lime at WTP-R1; sulfuric acid, antiscalant, and sodium hydroxide (caustic) at WTP-R2; phosphate corrosion inhibitor at WTP-L1 and WTP-G1. No gaseous chlorine anywhere |
| Customers | **273,900 persons served** by the 11 owned systems (107,800 metered connections). The customer information system (CIS) also bills **15,600 accounts** for the 3 municipal Utility Services clients, so it holds **123,400 accounts** |
| Utility Services (contract) | 3 municipal clients (Municipal Clients 1-3, about 41,000 persons). The company supplies 24 licensed operators who work at the clients' plants, monitors the clients' plants from the ROC after hours (read-only monitoring, alarm acknowledgment within 15 minutes, call-out of the client's on-call staff), and runs billing and customer service in the company CIS under each client's name. The clients remain the owners of their water systems and keep their own SDWA duties |
| Workforce | **600 employees**: executive and administration 45; treatment operations 140 (including 24 assigned to clients); ROC operators 22; SCADA and controls engineering and instrumentation 18; distribution and field services 160; meter services 35; water quality laboratory 20; engineering and capital projects 30; customer service center 70; IT and security 22; finance, HR, legal, and regulatory 38 |
| Revenue | About **$100 million** a year (fictional): regulated water service $88 million, Utility Services $9 million, other $3 million. Above the SBA standard of $41.0 million for NAICS 221310 (13 CFR 121.201), so **not SBA-small** |
| Rate regulation | Rates are set by the state utility regulator. Rate filings are outside the scope of these deliverables |
| SDWA section 1433 status | **Covered for 3 PWSIDs** (community water systems serving more than 3,300 persons, 42 U.S.C. 300i-2(a)(1)). EPA states that systems certify the RRA and ERP "for every individual PWSID number". Regional System: size category 100,000 or more. Lakes System: 50,000-99,999. Ridge System: 3,301-49,999. The 8 small systems are **not required to certify** (EPA guidance only, 300i-2(e)). Certification dates are in section 6 |
| Not in scope | Wastewater: none operated. HIPAA: not a covered entity. Federal contracts: none. SEC disclosure rules: privately held. EPA Risk Management Program (40 CFR Part 68): not triggered, because no plant stores a listed substance above its threshold (no gaseous chlorine or anhydrous ammonia). Payment cards: customers pay through the payment processor's hosted page and the processor's phone payment line, so card numbers never touch company systems (contractual PCI DSS duties sit with that arrangement; noted, not assessed) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (customer data breach notice, Fla. Stat. 501.171). All customers have Florida service addresses; about 6% have out-of-state billing addresses (seasonal residents), so other states' breach laws are handled generically |

## 2. People (role titles only)

| Role | Security and resilience duties |
|---|---|
| Board audit committee | Quarterly cyber and resilience risk reporting; includes the private equity sponsor's operating partner |
| Chief Executive Officer | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer | Executive sponsor of the security program and owner of the water operations SCADA system (P02); accepts Moderate risks; signs the EPA RRA and ERP certifications for the 3 covered systems |
| General Counsel | Legal lead for incidents, breach determinations, contract notices, and privilege |
| Chief Financial Officer | Insurance, payment processor, lenders, Utility Services contracts |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; audit committee reporting |
| IT Director | Runs business IT and the IT side of the IT/OT boundary; designated **security officer** for the program day to day |
| Security Manager plus 2 security analysts (one IT, one OT) and 1 GRC analyst | Security operations, MSSP oversight, vulnerability management, OT monitoring, GRC |
| Director of Water Operations | Runs treatment at all plants and the ROC; day-to-day system owner of SCADA operations |
| SCADA and Controls Engineering Manager | Leads 18 SCADA engineers and instrumentation technicians; owns PLC and HMI configuration, OT backups, and integrator work |
| ROC Supervisor | 24x7 control room; approves vendor remote sessions at the Regional System; first response to OT alarms |
| Plant Managers (Regional North, Regional South, Lakes, Ridge) and Chief Operators | Plant operation, manual-mode procedures, incident first response at the plant |
| Emergency Management and Resilience Manager | **RRA and ERP program lead** for all 3 covered systems; local emergency planning committee (LEPC) liaison; ERP document control |
| Water Quality and Compliance Manager | Laboratory, compliance monitoring, state reporting, and public notification content; business owner of AI-001 (P10) |
| Director of Customer Service | Customer service center, CIS, billing for own and client accounts; customer notices |
| Director of Utility Services | Relationship owner for the 3 municipal clients; SOC 2 sponsor (P09) |
| Distribution and Field Services Director | Distribution systems, main breaks, booster and tank sites, field crews |
| Engineering and Capital Projects Director | Capital plan, asset management, GIS; business owner of AI-005 (P10) |
| HR Director | Onboarding, terminations, background checks, training records |
| Co-sourced internal audit firm | Annual IT and OT audit; performs the P07 assessment. Reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR and SIEM for business IT; receives OT sensor alerts from the Regional plants (no OT playbooks yet) |
| SCADA integrators (2 contractors) | **Integrator A** programs and supports the Regional System platform under a 2025 contract with security terms. **Integrator B** supports the older Lakes and Ridge platforms under contracts inherited at acquisition with no security terms |

## 3. Systems

| ID | System | Hosting | Holds sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Regional SCADA (platform A): redundant SCADA servers at the ROC, a standby server at WTP-R2, 14 HMI stations (ROC 6, WTP-R1 4, WTP-R2 4), 2 engineering workstations, a process historian, and an alarm notification server | On-premises (ROC, WTP-R1, WTP-R2) | Yes (process data, SCADA configuration) | Commissioned 2021 on supported operating systems. Named HMI accounts. Quarterly offline backups of PLC logic and HMI projects |
| SYS-02 | Field controllers: 41 PLCs (Regional 24, Lakes 4, Ridge 5, small systems 8) including all chemical feed control, and 75 RTUs (Regional 47, Lakes 17, Ridge 11) at wells, boosters, and tanks | On-premises, plants and remote sites | Yes (control logic) | Chemical feed pumps at every plant have hardwired stroke limits, and chlorine and pH analyzers have hardwired high/low alarms that do not depend on SCADA |
| SYS-03 | Telemetry: licensed radio (Regional), fiber between WTP-R1 and WTP-R2, and 25 cellular modems on a private carrier network (Lakes 6, Ridge 11, small systems 8) | Radio and carrier networks | No | 3 small-system modems were found with web administration reachable from the internet (P07) |
| SYS-04 | OT remote access: the OT remote access gateway in the Regional OT DMZ (MFA through the identity provider, per-session approval by the ROC Supervisor, session recording; since 2025); site-to-site VPNs from Lakes and Ridge to the ROC (since March 2026); on-call operator VPN at Lakes (password only); Integrator B's commercial remote desktop agent on the Ridge engineering workstation (always on, password only) | On-premises appliances; vendor cloud relay for the agent | No | The Ridge agent is the path in the P08 HMI runbook |
| SYS-05 | Acquired-system SCADA: Lakes (platform B, 2016: 2 servers, 3 HMIs, 1 engineering workstation, historian) and Ridge (legacy platform, 2014: 1 server, 2 HMIs, 1 engineering workstation; operating system past end of support) | On-premises (WTP-L1, WTP-G1) | Yes | The ROC sees both through read-only clients over the site-to-site VPNs. Shared operator logins at both |
| SYS-06 | OT networks and OT DMZ: segmented control networks at WTP-R1 and WTP-R2 behind the IT/OT firewall with an OT DMZ (historian replica, patch server, remote access gateway); flat control networks at WTP-L1 and WTP-G1 | On-premises | No | Passive OT network monitoring sensors at WTP-R1 and WTP-R2 only (since 2025), alerting to the MSSP |
| SYS-07 | Cloud landing zone: 4 accounts (identity, shared services, workloads, backup) | Public cloud provider (vendor-agnostic) | Yes | Workloads: historian replica and water quality analytics (AI-001, AI-002), data lake, file services. Daily backups to a separate backup account with 35-day write-once retention |
| SYS-08 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | All workforce users; also the MFA source for the OT remote access gateway. OT accounts at Lakes, Ridge, and small systems are local and not federated |
| SYS-09 | Productivity suite (email, files, chat) and enterprise generative AI assistant (AI-006) | SaaS | Yes (RRA and ERP drafts) | |
| SYS-10 | Customer information and billing system (CIS) with customer portal, interactive voice response (IVR), and the contact center virtual agent (AI-004) | Vendor SaaS | Yes (customer PII for 123,400 accounts, online account credentials, bank account numbers for automatic payments) | Vendor SOC 2 Type 2. Card payments through the processor's hosted page and phone line |
| SYS-11 | Advanced metering infrastructure (AMI) head-end and meter data management, with leak analytics (AI-003) | Vendor SaaS | Yes (interval usage by account) | 81,000 of 107,800 meters on AMI |
| SYS-12 | Laboratory information management system (LIMS) | Vendor SaaS | Yes (compliance results) | In-house state-certified laboratory at WTP-R1 |
| SYS-13 | GIS, work order, and asset management, with the main-break likelihood model (AI-005) | Vendor SaaS | Yes (system maps, critical asset locations) | |
| SYS-14 | Finance, HR, and payroll suite | Vendor SaaS | Yes (employee PII) | |
| SYS-15 | Business network and endpoints: 640 workstations and laptops, 260 tablets and phones for field crews, at headquarters, all plants, and 3 field operations centers | On-premises and managed devices | Yes (cached) | EDR on all managed Windows and Mac endpoints |
| SYS-16 | SIEM and EDR consoles operated by the MSSP | SaaS | Yes (security logs) | IT logs complete; OT sensor alerts from the Regional plants only |
| SYS-17 | Physical security: card access and cameras at all plants and the ROC; intrusion alarms at wells and tanks reported through RTUs | On-premises | No | Small-system sites have locks and fences only |
| SYS-18 | AI tools: AI-001 water quality anomaly detection; AI-002 chemical dose recommender (pilot); AI-003 AMI leak analytics; AI-004 contact center virtual agent and call summaries; AI-005 main-break likelihood model; AI-006 enterprise generative AI assistant | Vendors and the cloud workloads account | Varies | Inventory in P10 |

**SSP system (P02):** the *Integrated Water Operations SCADA (IWOS)*: SYS-01 to SYS-06 (Regional SCADA and the ROC, field controllers, telemetry, OT remote access, the Lakes and Ridge SCADA, and the OT networks and OT DMZ), with their interfaces to the historian replica and analytics workloads in SYS-07 and to the business network (SYS-15) through the IT/OT firewall.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A security program since 2024 (after the private equity acquisition), led by a vCISO with an IT Director as security officer; policies adopted in 2024; quarterly reports to the audit committee
- MFA for all workforce users through the identity provider; privileged access management for cloud administrators
- EDR on all managed endpoints with 24x7 MSSP monitoring and a SIEM for business IT
- At the Regional System: an OT DMZ and deny-by-default IT/OT firewall (2025), an OT remote access gateway with MFA, session approval, and recording (2025), passive OT network monitoring at both plants (2025), named HMI accounts, and quarterly offline backups of PLC logic and HMI projects
- Hardwired stroke limits on chemical feed pumps and hardwired analyzer alarms at every plant; manual-mode operation drilled twice a year at the Regional System, once a year at Lakes
- Daily immutable backups of cloud workloads in a separate backup account
- 2025 RRA review for the Regional System with a cyber element based on EPA's cybersecurity checklist; ERP cyber annex for the Regional System (2025)
- Annual security awareness training and quarterly phishing simulations for workforce users with email
- Annual co-sourced internal IT audit; annual enterprise risk assessment
- Membership in the water-sector information sharing and analysis center and the state water and wastewater agency response network (WARN) for mutual aid
- Card access and cameras at all plants and the ROC; standby generators at all plants and at 30 of 41 wells
- Tier 1 public notice templates and boil water notice procedures for each system

**Missing or weak, found in the 2026 assessments:**
1. The acquired systems are outside most of the program. Lakes (2023) and Ridge (2025) run older SCADA platforms with flat control networks, and the Ridge SCADA server and engineering workstation run an operating system past end of support.
2. Integrator B's commercial remote desktop agent on the Ridge engineering workstation is always on, uses a password only, has no session approval, and is not logged by the company. On-call operator VPN access at Lakes uses a password only.
3. The site-to-site VPNs from Lakes and Ridge into the ROC (March 2026) allow broad any-to-any rules, so a compromise at an acquired plant can reach the Regional control network.
4. The OT asset inventory is complete only for the Regional System. Lakes, Ridge, and the small systems rely on integrator drawings; cellular modems are not inventoried.
5. OT monitoring covers only WTP-R1 and WTP-R2. The MSSP has no OT playbooks and no escalation path to the ROC. No logs are collected from Lakes, Ridge, or the small systems.
6. There are no in-house offline backups of PLC logic and HMI projects for Lakes, Ridge, or the small systems; the only copies are on the engineering workstations and at Integrator B.
7. Lakes, Ridge, and the small systems use shared HMI logins, and some small-system controllers and modems still have default or commissioning credentials.
8. RRA and ERP quality is uneven. The Regional 2025 RRA predates the March 2026 connection of the acquired systems to the ROC; the Lakes RRA cyber element was copied from the Regional one; the Ridge ERP (due 2026-12-24) has no cyber procedures yet; no ERP has been exercised with an OT cyber scenario.
9. Third-party risk: 14 OT vendors have remote access; vendor reviews happen only at onboarding; Integrator B's contracts have no security terms.
10. Recovery is proven only for the Regional SCADA servers (2025 rebuild test). Recovery at Lakes and Ridge, and of the CIS beyond the vendor's own disaster recovery, is untested.
11. Privileged access management covers only cloud administrators and the OT remote access gateway. Directory and SaaS administrators have standing rights, and 23 service accounts have non-expiring passwords.
12. Access reviews are annual, not quarterly, and the 3 municipal clients require a SOC 2 Type 2 report on Utility Services by their 2027 contract renewals.
13. There is no AI governance. Six AI tools or features are in use or in pilot without a security, safety, or privacy review (P10).
14. Policies exist, but supporting standards are thin: there is no OT security standard and no standard for bringing an acquired system into the program.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 system | Integrated Water Operations SCADA (IWOS). The registry default "Water treatment SCADA" is kept, widened to all 3 covered systems and the small systems because they share the ROC and its remote access paths |
| P03 regulations | Primary: SDWA section 1433 (42 U.S.C. 300i-2) for the 3 covered PWSIDs, with the RRA's cyber element benchmarked against NIST CSF 2.0 and SP 800-82 Rev. 3. Also analyzed at requirement level: SDWA public notification (40 CFR Part 141 Subpart Q), state reporting and records (40 CFR 141.31, 141.33), Ground Water Rule compliance monitoring and reporting (40 CFR 141.403(b)(3), 141.405(a)(1)), and Florida customer data security and breach notice (Fla. Stat. 501.171). CIRCIA is tracked as proposed only |
| P08 incidents | Two runbooks: (1) remote-access compromise of a treatment-plant HMI at the Ridge System through Integrator B's remote desktop agent, with an unauthorized change to the sodium hypochlorite feed (registry default, kept); (2) ransomware with customer data theft in business IT, affecting the CIS, billing, and Utility Services |
| P09 SOC 2 | The company is a service organization for Utility Services. Readiness for a SOC 2 Type 2 examination requested by the 3 municipal clients (Security, Availability, Processing Integrity, Confidentiality), plus a vendor SOC 2 review program |
| P10 AI | Portfolio of 6 use cases (AI-001 to AI-006). Water quality anomaly detection (registry default) is AI-001 |
| Cloud | Multi-account landing zone, vendor-agnostic, hybrid with on-premises OT. Provider names appear only in an equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-03-24 | Regional System RRA five-year review certified to EPA (deadline March 31, 2025) |
| 2025-09-19 | Regional System ERP review certified (six months after the RRA certification: 2025-09-24) |
| 2025-12-17 | Lakes System RRA five-year review certified (deadline December 31, 2025) |
| 2026-06-12 | Lakes System ERP review certified (six months after the RRA certification: 2026-06-17) |
| 2026-06-24 | Ridge System RRA five-year review certified (deadline June 30, 2026) |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (site visits 2026-08-11 to 2026-08-14) |
| 2026-09-15 | Deliverables approved; results presented to the audit committee |
| 2026-10-01 | Revised policies take effect |
| 2026-12-04 | Internal target to certify the revised Ridge System ERP |
| 2026-12-24 | Latest Ridge System ERP certification date (six months after the 2026-06-24 RRA certification) |
| 2027-04-01 | Planned start of the SOC 2 Type 2 observation period |
| 2030-03-31 | Next Regional System RRA review deadline (five years after the March 31, 2025 cycle deadline) |

## 7. Facts added during the build (fictional; used across P01-P10)

| Topic | Added fact |
|---|---|
| Demand and storage | Regional average day demand 26 MGD, maximum day 34 MGD; Lakes 7.2 MGD average; Ridge 3.6 MGD average. Usable storage after fire reserve covers about 8 hours of average demand at Regional, 10 hours at Lakes, and 12 hours at Ridge |
| Revenue per day | About $274,000 per day overall; regulated water revenue is billed monthly in arrears, so short outages defer cash rather than lose it |
| Ground Water Rule | All 11 owned systems are groundwater systems that provide 4-log treatment of viruses and do compliance monitoring under 40 CFR 141.403(b). The 3 covered systems monitor disinfectant residual continuously (systems serving more than 3,300 people, 141.403(b)(3)(i)(A)) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before incident vendors are engaged |
| Utility Services contracts | Each client contract requires notice to the client within 24 hours of a security incident affecting client data or client plant monitoring, ROC alarm acknowledgment within 15 minutes, billing cycles within 2 business days of schedule, and an annual SOC 2 Type 2 report starting with the 2027 renewals |
| Workforce activity | 96 terminations and 51 internal transfers in the 12 months to 2026-06-30. The last access review was completed in February 2026. The June 2026 phishing simulation click rate was 6.4% |
| OT vendors | 14 OT vendors hold remote access: Integrator A and Integrator B, 4 analyzer and instrument vendors, 3 pump and drive vendors, the RO membrane vendor, the AMI vendor's field service team, the cellular carrier, the radio vendor, and the generator service vendor |
| Additional role titles | Controller; Purchasing Manager; Laboratory Manager; Field Operations Managers (3 field operations centers); Communications Manager; Safety Manager |
| FY2027 security plan | Approved by the CEO 2026-09-15: about $2.1 million one-time (including the $850,000 Ridge SCADA replacement in the 2027 capital plan), $350,000 a year, and $240,000 for SOC 2 readiness and the Type 2 examination across 2027 (P01 section 4) |
| Security standards | STD-01 to STD-10 (P06 `standards-index.md`). Existing from 2024: STD-03 configuration and encryption, STD-04 authenticator and privileged access, STD-05 media sanitization, STD-09 vulnerability and patch (IT only). New drafts: STD-01 OT security, STD-02 logging and monitoring, STD-06 contingency and recovery, STD-07 acquisition integration, STD-08 vendor and OT remote access, STD-10 AI use |
| Assessment populations | 38 privileged accounts across the gateway, firewalls, cloud, and SCADA servers; 412 gateway sessions from April to June 2026; 31 security incidents in 2025-2026; 162 operators and ROC staff; 4 drinking water violations in 2025-2026 (all small-system missed monitoring), each reported within 48 hours |
| P07 stop-and-notify | The exposure scan (2026-08-10) found 3 small-system modems with web administration reachable from the internet and default credentials; credentials changed 2026-08-13; move to the private carrier network due 2026-10-15 |
| AI deployment details | AI-001 in advisory production at the Regional System since 2026-01, using 14 distribution monitoring stations (no Lakes or Ridge data); AI-002 pilot at WTP-R2 since 2026-06; AI-003 since 2025-03; AI-004 since 2026-04; AI-005 since 2025-09; AI-006 enabled for 120 users since 2026-05. In July 2026 the AI-004 virtual agent told 11 callers that no boil water notice was active during a precautionary notice at a small system |
| Customer language | Customer language data show a large Spanish-speaking population in the Lakes and Ridge service areas; Regional notice templates include a Spanish statement, Lakes and Ridge templates do not (P03 G-060) |
