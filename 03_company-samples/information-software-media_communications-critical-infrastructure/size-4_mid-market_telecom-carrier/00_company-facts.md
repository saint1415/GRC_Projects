# Scenario facts: Cris Santos Company | Communications | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, court decision, or Federal Register document, the citation is given. Legal status was checked against eCFR (point in time 2026-09-23) and the Federal Register API on 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed since 2022; board with an audit committee) |
| Business | Regional broadband and wired telecommunications carrier (NAICS 517111). The company is the incumbent local exchange carrier (ILEC) for a rural and suburban territory in north-central and northeast Florida, rebuilt mostly with fiber. In 2023 it acquired a competitive carrier (CLEC) that serves business customers in two metro areas; the CLEC entity was merged into the company on 2025-07-01. Service lines: fiber and DSL broadband; wireline voice (legacy copper local exchange with resold long distance) and interconnected VoIP; business data services (dedicated internet access, Ethernet, wholesale backhaul and dark fiber); and **Business Services**, a managed services line (hosted voice for businesses, managed SD-WAN and firewall, and a small colocation data hall). **No** video service, **no** wireless (CMRS) service, **no** submarine cable or cable landing station |
| Location | Florida only. Headquarters campus with central office **CO-1** (primary network operations center, the Business Services data hall, and the main customer care center); 8 more central offices (**CO-2** to **CO-9**; **CO-4** also houses the secondary NOC and the second voice core node); 2 metro points of presence from the CLEC (**POP-A**, **POP-B**); 3 retail stores; 2 warehouses with fleet yards; 268 remote fiber and DSL cabinets. Service area: parts of 11 counties |
| Workforce | 850 employees: 290 field technicians and construction crew, 48 NOC staff, 52 network engineering and planning, 140 customer care agents and supervisors, 24 retail, 58 sales and marketing, 62 billing and finance, 34 IT (including the 4-person security team), 46 Business Services engineering and support, 30 warehouse and fleet, 66 executive, HR, legal, regulatory, and facilities |
| Customers | About 205,000 accounts (189,000 residential, 16,000 business). About 197,000 broadband subscribers. About 74,000 voice lines on about 61,000 accounts: 19,500 legacy copper lines and 54,500 interconnected VoIP lines (including 14,200 hosted voice seats for about 600 Business Services customers). 320 enterprise and government accounts have a dedicated account representative and a contract that addresses CPNI protection. About 8% of residential accounts belong to seasonal residents who also have an address in another state |
| Revenue | $318 million annual receipts (fictional), about $871,000 per day: residential broadband $150 million, voice $46 million, business data services $72 million, Business Services $38 million, other $12 million |
| Size status | Mid-Market tier. The SBA size standard for NAICS 517111 is 1,500 employees (13 CFR 121.201), so at 850 employees the company is still SBA-small; it is sized at 500-999 employees per the tier rule and flagged (see README) |
| Regulatory status | **Telecommunications carrier** for local exchange and toll service (47 U.S.C. 153; 47 CFR 64.2003(o)). **Interconnected VoIP provider**, treated as a carrier by the CPNI rules (64.2003(o)). **Broadband internet access provider**: broadband is an information service after *Ohio Telecom Ass'n v. FCC* (6th Cir. Jan. 2, 2025); the FCC conformed its rules on 2025-08-08 (90 FR 38406). **Wireline and interconnected VoIP provider** for outage reporting (47 CFR 4.3(g), (h)). **Covered 911 service provider**: five of its central offices (CO-1, CO-3, CO-5, CO-6, CO-8) are the last service-provider facility through which 911 trunks or administrative lines pass before reaching 7 PSAPs (47 CFR 9.19(a)(4)(i)(B)). **Voice service provider** under the caller ID authentication rules (47 CFR 64.6300 et seq.). **Provider of advanced communications service** for the Secure Networks Act reporting rule (47 CFR 1.50001(a), 1.50007). **Telecommunications carrier under CALEA** (47 U.S.C. 1001(8)(A)) |
| Customer commitments | Online privacy policy and CPNI notice; residential terms of service; business data contracts with a 99.99% monthly availability SLA on protected circuits; Business Services contracts with a 99.99% hosted voice availability SLA; enterprise contracts that set CPNI authentication terms (47 CFR 64.2010(g)). Several Business Services customers (a regional hospital system, two county governments, a school district, and three credit unions) have asked for a SOC 2 Type 2 report |
| Not in scope | SEC cybersecurity disclosure rules (privately held; C-COMMUNICATIONS-R06). FCC submarine cable landing license rules (no cable or SLTE; C-COMMUNICATIONS-R04). CMRS-only rules, including SIM change authentication (47 CFR 64.2010(h)). Emergency Alert System rules (no video or broadcast service). FAR 52.204-25 and 52.204-23 reporting (no federal prime contracts or subcontracts; government customers are state and local). Payment card data: cards are taken through the payment processor's hosted pages and a tokenized IVR; PCI DSS duties are contractual and outside this sample |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification (Fla. Stat. 501.171) and all-party consent for recorded calls (Fla. Stat. 934.03(2)(d)). Seasonal residents are handled generically: "the law of each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and compliance reporting; receives the vCISO directly |
| Chief Executive Officer | Accepts High risks; approves POL-01, the risk appetite, and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; system owner of the OSS/BSS platform; accepts Moderate risks; approves POL-02 to POL-05 and these deliverables |
| Chief Financial Officer (CFO) | Billing, vendor contracts, cyber insurance |
| General Counsel | Legal lead in incidents; engages breach counsel and forensics under privilege; contract terms |
| Vice President of Regulatory Affairs | Corporate officer. **CPNI compliance officer**; signs the annual CPNI certification (47 CFR 64.2009(e)) and the Robocall Mitigation Database certification (64.6305(d)); privacy lead for breach determinations with counsel |
| Chief Technology Officer (CTO) | Owns network engineering, network operations, and IT; **certifying official** for 911 reliability filings (47 CFR 9.19(a)(3)); the Security Manager reports to the CTO |
| Vice President of Network Operations | **CALEA senior officer** (47 CFR 1.20003(a)); authorizes NORS filings; owns the NOC |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, risk appetite, and board reporting; reports to the audit committee as well as the COO |
| Security Manager, 2 security analysts, 1 GRC analyst | Security operations, MDR oversight, vulnerability management, policies and standards, GRC |
| IT Director | Identity provider, endpoints, cloud landing zone, corporate applications |
| NOC Director | 24x7 NOC; outage escalation; NORS and DIRS submissions; PSAP notifications |
| Director of Network Engineering | Routers, OLTs, DSLAMs, SBCs, softswitch, TACACS+ policy, network element patching |
| Director of Customer Operations | Care center, retail stores, the overflow call center vendor, the AI chatbot, and the agent assist tool (business owner) |
| Director of Business Services | Hosted voice, managed SD-WAN, and colocation; owner of the SOC 2 service commitments |
| Billing Director | BSS and the legacy CLEC billing system; mediation and rating |
| Marketing Director | Campaigns that use CPNI; opt-out notices; the churn prediction model (business owner) |
| HR Director | Onboarding, terminations, training records, sanctions |
| Co-sourced internal audit firm | Annual IT audit; performed the P07 control assessment; reports to the audit committee |
| Managed detection and response (MDR) provider | 24x7 monitoring of the SIEM and EDR since 2025-06 |
| Outside telecommunications regulatory counsel | CPNI, CALEA, 911, and robocall rule advice |

**Where roles overlap and how it is compensated.** The Security Manager reports to the CTO, who also runs the network the Security Manager assesses for risk. The vCISO's direct line to the audit committee, the co-sourced internal audit firm (which tests controls it does not operate), and the CEO's role as High-risk acceptor compensate for that reporting line. The Vice President of Regulatory Affairs signs the CPNI certification and also leads breach determinations; counsel reviews both.

## 3. Systems

| ID | System | Hosting | Holds CPNI or subscriber PII? | Notes |
|---|---|---|---|---|
| SYS-01 | Billing and customer care system (BSS): accounts, CPNI approval flags, account passwords, bills with toll call detail, agent desktop | Vendor SaaS | Yes | System of record for about 198,000 accounts. Vendor SOC 2 Type 2 (P09) |
| SYS-02 | OSS: network inventory, provisioning and activation, trouble ticketing, workforce dispatch | Cloud landing zone (SYS-13), production account | Yes (service configuration, addresses) | Company-managed application |
| SYS-03 | Voice mediation and rating: collects call detail records (CDRs) from SYS-07, rates toll calls, feeds SYS-01 and SYS-18; CDR archive (36 months) | Cloud landing zone, production account | Yes (call detail for every voice line) | Object-level read logging not enabled |
| SYS-04 | Customer portal and mobile app | Cloud landing zone, PaaS web app behind an API gateway | Yes | Password reset by one-time code to the telephone number or email of record since 2025-03 |
| SYS-05 | Identity provider (workforce single sign-on and MFA) | SaaS | No (identities only) | Also backs the TACACS+ servers for core network elements |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-07 | Voice core: two geo-redundant softswitch nodes (CO-1, CO-4), 4 session border controllers (SBCs), legacy TDM host switches at CO-3, CO-5, and CO-7 (vendor support ended 2024; retirement 2028), SS7 through a third-party SS7 hub, STIR/SHAKEN signing service, 911 trunks to the state NG911 system service provider | On-premises | Yes (CDRs generated here) | 2 SBCs reach vendor end of support on 2026-12-31 |
| SYS-08 | IP/MPLS core and access network: core routers, broadband network gateways, 4 internet edge routers, OLTs, DSLAMs, 268 cabinet aggregation switches, CLEC metro switches at POP-A and POP-B, DNS and DHCP | On-premises and outside plant | Yes (subscriber IP assignments) | |
| SYS-09 | Network management plane: NOC monitoring and alarm correlation, element management systems, 2 TACACS+ servers, syslog collectors (90-day retention), configuration backup servers (CO-1, copy at CO-4), 4 jump hosts | On-premises (CO-1, CO-4) | Indirect | TACACS+ with MFA covers core and edge only |
| SYS-10 | Lawful-intercept (CALEA) mediation: softswitch intercept function and a mediation appliance linked to a CALEA trusted third party (TTP) | On-premises (CO-1), restricted room | Yes (intercept content and court orders) | 4 named employees have access. Outside the SSP boundary; covered by the CALEA SSI plan |
| SYS-11 | Contact center platform (CCaaS): ACD, IVR (tokenized card payments), call recording, agent assist feature (AI-002) | Vendor SaaS | Yes | Used by in-house agents and an after-hours overflow call center vendor (U.S.-based, 35 agents) |
| SYS-12 | Customer-service AI chatbot with account access (web and app chat); reads and updates account data through an API to SYS-01 | Vendor SaaS (large language model platform) | Yes | In production since 2026-03-02 (AI-001, P10) |
| SYS-13 | Cloud landing zone: 5 accounts (management, security and log archive, network hub, production workloads, backup) hosting SYS-02, SYS-03, SYS-04, the API gateway, a reporting data warehouse, and the backup vault | Public cloud provider (vendor-agnostic) | Yes | Site-to-cloud VPN to CO-1 and CO-4 |
| SYS-14 | Endpoints: 860 Windows laptops and desktops, 420 field technician tablets, 64 on-premises servers | Company-managed | Cached | EDR on laptops, desktops, and servers; tablets under mobile device management |
| SYS-15 | Business Services platform: hosted voice (UCaaS) cluster in the CO-1 data hall, the managed SD-WAN and firewall orchestrator (vendor SaaS), customer self-service portal, colocation (42 racks) | On-premises (CO-1) and vendor SaaS | Yes (business customers' call records and configurations) | SOC 2 scope (P09) |
| SYS-16 | SIEM (SaaS) monitored 24x7 by the MDR provider | SaaS | Incidental (logs) | Sources: IdP, cloud, EDR, firewalls, VPN, BSS audit logs. Not yet: network element syslog and TACACS+ accounting, CDR archive reads, SYS-15, SYS-18 |
| SYS-17 | Third parties: about 180 vendors, 34 with access to CPNI, subscriber PII, or the network | Various | Varies | 12 are Tier 1 under the P09 tiering approach |
| SYS-18 | Legacy CLEC billing system: bills about 6,800 CLEC business accounts until migration to SYS-01 (planned 2027-06-30) | On-premises (POP-A) | Yes (CPNI) | Shared administrator accounts; no account-change notices; not logged to the SIEM |

**SSP system (P02):** the *Network Operations and Customer Billing Platform (OSS/BSS)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-09, SYS-13, SYS-16, and SYS-18, with their interfaces to SYS-07 and SYS-08 (element management and CDR feeds), SYS-11, SYS-12, and SYS-15. Moderate baseline with tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- MFA through the identity provider for email, single sign-on applications, VPN, and the cloud console; hardware security keys for cloud and identity administrators
- EDR on all laptops, desktops, and servers; a SIEM monitored 24x7 by an MDR provider since 2025-06
- TACACS+ with MFA on core routers, broadband network gateways, and internet edge routers
- Five security policies adopted in 2024; an incident response plan (2024) and one IT-only tabletop (2025)
- Monthly authenticated vulnerability scans of servers and cloud workloads; quarterly external scans
- A 5-account cloud landing zone with a separate backup account and write-once retention
- CPNI program: annual certification filed by March 1 (most recent 2026-02-27, for calendar year 2025); approval flags in the BSS; opt-out process with a 30-day wait; per-account passwords for telephone release of call detail; photo ID at the 3 retail stores; the business customer exemption for 320 enterprise accounts
- Portal and app password reset by one-time code to the telephone number or email of record (fixed 2025-03)
- CALEA SSI policies filed for the ILEC (2019) and a CALEA TTP contract
- NOC procedures for PSAP notification, NORS, and DIRS; 6 NORS reports filed in the 12 months to 2026-06-30
- 911 reliability: legacy 911 circuits tagged; annual diversity audits; annual 911 reliability certifications filed through 2025
- STIR/SHAKEN on the IP voice network; a Robocall Mitigation Database (RMD) certification on file
- Secure Networks Act certification that the network contains no covered communications equipment (filed 2022)
- Badge access, cameras, and alarms at central offices, POPs, and the data hall; locked and alarmed cabinets
- Annual security awareness and CPNI training for employees; quarterly phishing simulations
- Co-sourced internal audit; cyber insurance with a breach response panel

**Missing or weak, found in the 2026 assessments:**
1. The AI chatbot's "verify me" fallback for customers who are not signed in accepts the last 4 digits of the SSN plus the service address before showing call detail and account data (47 CFR 64.2010(c), (e)).
2. The legacy CLEC billing system (SYS-18) sends no account-change notices and uses shared administrator accounts (64.2010(f)).
3. The CPNI breach procedure in the 2024 incident response plan applies the 2023 amendments as if they were in effect (30-day customer notice, FCC as a recipient) and omits the 7-business-day hold; nobody has tested access to the FCC reporting facility (64.2011).
4. Overflow call center agents released call detail without the account password in 2 of 25 sampled calls; vendor agents have had no CPNI training (64.2009(b), 64.2010(b)).
5. The management plane is only partly protected: OLTs, DSLAMs, cabinet switches, CLEC metro switches, and SBCs use shared local administrator accounts without MFA; the management network can be reached from corporate VLANs at POP-A and POP-B; privileged access management covers servers only.
6. Network elements are outside vulnerability scanning. Two internet edge routers missed the 30-day patch target for critical advisories, 2 SBCs reach end of support on 2026-12-31, and the TDM switches are unsupported.
7. SIEM coverage gaps: network element syslog and TACACS+ accounting, CDR archive object reads, the Business Services platform, and SYS-18 do not reach the SIEM.
8. Third-party risk: 22 of the 34 vendors with CPNI, PII, or network access have never had a security review; the chatbot and agent assist contracts do not bar training on company data.
9. Recovery is proven only for the OSS. Mediation, portal, and data warehouse restores are untested; network element configuration restore at scale is untested; the BSS vendor's 12-hour RTO exceeds the 8-hour BIA RTO for customer care.
10. CALEA: the amended SSI policies covering the merged CLEC were not filed with the FCC within 90 days of the 2025-07-01 merger, and the 24x7 contact appendix is out of date (47 CFR 1.20005(a), 1.20003(b)(4)).
11. 911 reliability: the 2025 diversity audit found 2 of 14 legacy 911 circuit pairs sharing a fiber segment, not yet re-routed; the CO-6 generator failed a full-load test in 2026-05; PSAP contacts for POP-served areas were last confirmed in 2024 (47 CFR 9.19(c), 4.9(h)(1)).
12. The RMD certification still names a robocall mitigation contact who left in 2026-04; it was not updated within 10 business days (64.6305(d)(5)).
13. AI governance is informal: the chatbot went live after a limited review, the agent assist tool and the churn model were adopted by departments without review, and staff use public generative AI tools.
14. No SOC 2 report for Business Services, and change management for the hosted voice platform is informal.
15. Policies exist, but supporting standards (configuration, logging, vendor, network device hardening) are thin.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | All applicable rules for the primary business line: FCC CPNI rules, 47 CFR 64.2001-64.2011 (primary; the 2023 amendments to 64.2011 are not yet effective); CALEA SSI rules (47 CFR 1.20000-1.20008); outage reporting (47 CFR Part 4); 911 reliability (47 CFR 9.19-9.20, as amended by FCC 26-39, 91 FR 42794); caller ID authentication and robocall mitigation (47 CFR 64.6301-64.6305); Secure Networks Act reporting (47 CFR 1.50007). Voluntary network security benchmark: NIST CSF 2.0 with the CISA Cross-Sector Cybersecurity Performance Goals |
| P08 incidents | **Two incident types:** (1) network intrusion exposing CPNI (registry default): exploitation of an internet edge router, movement through the management plane, and theft of call detail records; (2) ransomware on corporate IT and the cloud landing zone that disrupts operations and triggers outage and PSAP clocks. Integrated with crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the **Business Services** system (hosted voice, managed SD-WAN and firewall, colocation) requested by enterprise and government customers: Security, Availability, and Confidentiality. Plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 customer-service chatbot with account access (registry default, kept); AI-002 contact center agent assist; AI-003 NOC alarm correlation and predictive maintenance; AI-004 churn prediction and next-best-offer model; AI-005 enterprise generative AI assistant for staff |
| Cloud | Multi-account landing zone (5 accounts), vendor-agnostic. AWS, Azure, and Google Cloud equivalents noted only in P04 |

The registry defaults (primary system OSS/BSS, CPNI intrusion incident, chatbot with account access) all fit the business at this size and are kept. The second incident type and the other four AI use cases were added because the tier calls for two incident types and a use-case portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (walkthroughs of CO-1, CO-4, CO-6, POP-A, and 4 cabinets on 2026-07-21 to 2026-07-23) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm |
| 2026-08-24 to 2026-09-04 | AI portfolio assessment and SOC 2 readiness assessment |
| 2026-09-17 | Results to the audit committee; deliverables approved by the COO; High risk treatment plans and the risk appetite approved by the Chief Executive Officer |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| PSAPs | 7 PSAPs receive 911 trunks or administrative lines whose last service-provider facility is a company central office: 2 at CO-1, 2 at CO-3, 1 at CO-5, 1 at CO-6, 1 at CO-8. The selective routing and NG911 core services are provided by the state NG911 system service provider, not by the company. 14 legacy 911 circuit pairs serve those PSAPs |
| Power | All central offices have generators with at least 72 hours of fuel and battery plant for about 8 hours. Remote cabinets have about 8 hours of battery. The CO-6 generator failed its full-load test on 2026-05-14; a replacement transfer switch is on order |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; the policy requires notice through the carrier hotline before incident vendors are engaged |
| MDR | 24x7 monitoring of the SIEM and EDR; contract requires a call to the Security Manager within 30 minutes of a high-severity alert |
| Backups | Daily backups of the production account to the backup account (second region), 35-day write-once retention, separate administrator credentials. Network element configurations are backed up nightly to CO-1 with a copy at CO-4 |
| Vendor recovery commitments | The BSS vendor's SOC 2 system description states RTO 12 hours and RPO 1 hour |
| Workforce activity | 142 terminations and 77 internal transfers in the 12 months to 2026-06-30. Access reviews are semiannual; the last was completed in February 2026. The June 2026 phishing simulation click rate was 6.1% |
| Chatbot | About 41,000 sessions a month; 12% in Spanish |
| Robocall traceback | 18 traceback requests from the industry traceback consortium in the 12 months to 2026-06-30; 16 answered within 24 hours |
| Covered equipment | The 2022 Secure Networks Act certification stated that the network contains no covered communications equipment or services; purchasing has no check against the FCC Covered List for used or refurbished equipment |
| Additional role titles | Controller; Director of Retail; Director of Facilities; Manager of Field Operations; Customer Care Manager; Data Analytics Manager (reports to the Marketing Director) |
| Terminology | "Network Operations and Customer Billing Platform (OSS/BSS)" is the SSP system in P02, identifier CSC-OSSBSS-01. "Business Services system" is the SOC 2 system in P09 |
| Other operating details | Business data services reach 3,400 business and government sites, including 112 cell site backhaul circuits; managed SD-WAN covers about 1,900 customer edge devices; about 2,100 access elements (OLTs, DSLAMs, cabinet and POP switches); 118 privileged accounts across all administration planes; 412 changes in 2026 Q2; 41 security incidents logged in the 12 months to 2026-06-30; about 9,500 customer contacts a day; about 120,000 paper bills a month; about 410 of the SYS-18 business accounts are small businesses outside the 64.2010(g) contracts; the chatbot "verify me" fallback was used in about 2,300 sessions from 2026-03-02 to 2026-07-24; counsel approved new call-recording notice wording on 2026-09-02 |
