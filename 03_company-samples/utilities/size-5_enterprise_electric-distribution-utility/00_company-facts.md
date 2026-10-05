# Scenario facts: Cris Santos Company | Utilities | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded investor-owned electric utility; SEC registrant, not a smaller reporting company) |
| Business | Electric power distribution (NAICS 221122, primary) with an owned transmission system (NAICS 221121, secondary). Distribution produces about 95% of retail revenue and most of the asset base. The company owns no generation: it sold its generating plants in 2019 and buys energy under long-term power purchase agreements and in the wholesale market. Retail rates are set by the state public service commissions; transmission service is provided under a FERC-approved open access transmission tariff |
| Service territory | Headquartered in Florida. Northern and central Florida (about 1.68 million meters) and south Georgia (about 270,000 meters). **State law is handled generically:** breach notices follow the law of each state where affected individuals reside, with Florida as the worked example |
| Facilities | **Headquarters campus** (Florida): corporate offices, the Transmission Control Center (TCC), and Data Center 1 (DC-1). **Grid Operations Center (GOC)** (Florida): the Distribution Control Center (DCC), the 24x7 Security Operations Center (SOC) for IT and OT, and the storm command center. **Operations Center North (OCN)** (Florida, about 140 miles from headquarters): the backup TCC, the backup DCC, and Data Center 2 (DC-2). **Georgia Operations Center**: regional dispatch and crews for south Georgia. 38 district operations centers and crew yards |
| Customers and load | About 1.95 million meters: 1.72 million residential and 230,000 commercial and industrial. 2025 summer peak load 8,650 MW |
| Grid | 3,380 distribution feeders at 12.47 kV and 23 kV from 418 distribution substations. About 5,900 circuit miles of transmission at 500 kV, 230 kV, and 115 kV, with 146 transmission substations: 2 at 500 kV (**Substations P and R**), 33 at 230 kV (including **Substation K**), and 111 at 115 kV. About 41,000 field devices (reclosers, automated switches, capacitor controls, line sensors) |
| Workforce | 12,000 employees (breakdown in section 7) |
| Revenue | About $4.8 billion a year (fictional): $4.56 billion retail electric sales, $150 million transmission service, $50 million Utility Services fees (SL-1), $40 million fleet charging services (SL-2). Retail revenue is about $12.5 million per calendar day. The SBA standard for NAICS 221122 is 1,100 employees (13 CFR 121.201), so the company is not small |
| NERC registration | **Distribution Provider (DP), Transmission Owner (TO), and Transmission Operator (TOP)** on the NERC Compliance Registry. Regional Entity: SERC Reliability Corporation. The Reliability Coordinator and the Balancing Authority for the area are other, unaffiliated entities |
| CIP impact rating (CIP-002-5.1a, last approved 2026-03-12) | **High impact:** the BES Cyber Systems of the energy management system (EMS) at the TCC and the backup TCC, because they perform TOP functional obligations for assets that meet medium impact criteria 2.4 and 2.5 (Attachment 1 criterion 1.3). **Medium impact with External Routable Connectivity:** the BES Cyber Systems at Substations P and R (500 kV Transmission Facilities, criterion 2.4) and at Substation K (230 kV, connected to five other Transmission stations by five 230 kV lines, aggregate weighted value 3,500, criterion 2.5). **Low impact:** the other 143 transmission substations (criterion 3.2). No high or medium impact system at any distribution substation. The largest other 230 kV station has four 230 kV lines (aggregate weighted value 2,800, below the 3,000 threshold) |
| Not in CIP scope | **UFLS:** feeder underfrequency relays at 212 substations shed about 2,600 MW in stages under the regional program, but each relay acts on its own with no common control system, so criterion 2.10 is not met. **Distribution SCADA and OMS (the ADMS at the DCC):** they monitor and control distribution facilities, which are not BES Facilities. The DCC is not a "Control Center" in the NERC Glossary sense because it does not perform TOP reliability tasks for transmission Facilities; TOP-directed manual load shedding is directed by the TCC and carried out by DCC operators through the ADMS. This determination is recorded in a 2024 compliance memo that is re-read in each CIP-002 review. The ADMS is protected voluntarily to the company's OT security standard (OT-STD-01), which mirrors the medium impact CIP controls, but it is not audited by SERC. No Remedial Action Schemes; no Blackstart Resources or Cranking Paths in the company's area |
| CIP-014-3 | Applies: the company is a TO that owns 500 kV Transmission stations (Applicability 4.1.1.1). The R1 risk assessment of 2025-02-20 identified **Substation P** as a station that, if rendered inoperable or damaged, could result in instability, uncontrolled separation, or Cascading. R2 verification by an unaffiliated Planning Coordinator was completed 2025-04-17; R4 evaluation 2025-07-30; R5 physical security plan approved 2025-09-18; R6 third-party review 2025-10-29. Primary control center for Substation P: the company's own TCC |
| CIP-012-2 | Applies (TOP that operates Control Centers; in effect since 2026-07-01). Real-time data moves between the TCC and the backup TCC, and from both to the Reliability Coordinator and the Balancing Authority over ICCP |
| Credit and identity data | The company obtains consumer reports to set deposits for new residential accounts and furnishes information on unpaid final bills to consumer reporting agencies, so it is a creditor under 15 U.S.C. 1681m(e)(4). Utility accounts are covered accounts (16 CFR 681.1(b)(3)), so the FTC Identity Theft Red Flags Rule (16 CFR 681.1) and the Disposal Rule (16 CFR Part 682) apply. The CIS holds Social Security numbers, driver license numbers, and bank account numbers |
| Payment cards | Utility bill payments use the payment processor's hosted page and IVR payment service; no card data in company systems. Fleet charging card payments at public-access chargers go through the charging platform vendor's payment service. PCI DSS is a contractual obligation, noted and not assessed |
| Other regimes considered and not applicable | TSA pipeline security directives (no pipelines), NRC 10 CFR 73.54 (no reactors), SDWA section 1433 (no water system). CIRCIA reporting is not in effect (final rule not published as of 2026-09-25) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; high and medium impact CIP programs including CIP-013 supply chain and CIP-014 physical security; two service lines offered to external clients (SOC 2) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee and the risk and reliability committee | Audit committee: Internal Audit, SOX, disclosure controls. Risk and reliability committee: cyber and physical security oversight, CIP compliance, risk appetite (Item 106 governance) |
| Chief Executive Officer; Chief Financial Officer | Jointly accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | Business owner for grid operations and customer operations; authorizing official for the Distribution Operations Platform (P02) |
| Senior Vice President, Transmission and System Operations | **CIP Senior Manager** (identified by name in the CIP-003-9 R3 record; this sample uses the title only) |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CIO with a direct line to the risk and reliability committee |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Compliance Officer | Second-line compliance, including the NERC compliance program (independent of operations) |
| General Counsel | Chairs the disclosure committee; legal privilege; regulator correspondence |
| Chief Audit Executive | Heads Internal Audit; reports functionally to the audit committee; leads the P07 assessment |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| GRC team (12), Security Operations Center (24x7, in-house, IT and OT), OT Security team (18), Internal Audit (in-house with a co-sourced OT specialist firm) | Three lines model |

## 3. Systems

| ID | System | Hosting | Customer PI? | Notes |
|---|---|---|---|---|
| SYS-01 | Energy management system (EMS): transmission SCADA, network applications, ICCP links, historian | On-premises at the TCC and the backup TCC | No | **High impact BES Cyber Systems.** Separate CIP OT domain; Electronic Security Perimeters with Electronic Access Points; Intermediate Systems for Interactive Remote Access |
| SYS-02 | Advanced distribution management system (ADMS): distribution SCADA, DMS applications (FLISR on 1,900 feeders, volt-VAR optimization), 96 operator consoles, historian | On-premises at the DCC (primary) and the backup DCC | No | Separate ADMS OT domain. Protected under OT-STD-01 (voluntary CIP-equivalent). 22 consoles and the DCC historian run an operating system past vendor support |
| SYS-03 | Outage management system (OMS), GIS, and mobile workforce (4,100 rugged tablets) | OMS on-premises at the GOC with a warm standby at OCN; GIS on Cloud provider A | Yes (names, addresses, phone numbers, premise locations, medical-priority flags) | Receives ADMS breaker status and AMI outage events; predicts outages; dispatches crews; switching orders |
| SYS-04 | Substation and field networks | 418 distribution substations (fiber to 255, private LTE and licensed radio to 163) and 146 transmission substations | No | 159 distribution substations still use legacy serial RTUs behind serial-to-IP gateways without authentication |
| SYS-05 | Transmission substation BES Cyber Systems | Substations P, R, K (medium impact); 143 other transmission substations (low impact) | No | Relays, RTUs, substation HMIs, EAP firewalls. Low impact sites use CIP-003-9 Attachment 1 Section 3.1 access controls at substation gateways |
| SYS-06 | Advanced metering infrastructure (AMI) head-end and meter data management (MDM): 1.95 million meters | AMI head-end: vendor SaaS. MDM: Cloud provider A | Yes (interval usage data) | Remote connect and disconnect. AMI vendor SOC 2 Type 2 reviewed annually |
| SYS-07 | Customer information system (CIS) and billing, customer portal and mobile app, IVR, contact center platform | CIS: commercial software customer-managed on Cloud provider A. Contact center: SaaS | Yes (SSNs, driver license numbers, bank account numbers, call recordings) | About 2.1 million active and 3.4 million closed accounts |
| SYS-08 | Identity: enterprise identity platform (SSO, MFA, PAM, identity governance); separate OT identity stores (EMS domain, ADMS domain) with OT PAM | SaaS and on-premises | No (identities only) | OT domains do not trust the corporate domain |
| SYS-09 | Multi-cloud estate: Cloud provider A and Cloud provider B (vendor-agnostic) plus DC-1 and DC-2 | IaaS, PaaS | Yes | Cloud A: CIS, MDM, GIS, Utility Services platform, data platform. Cloud B: analytics and AI platform, mobile app back end, fleet portal |
| SYS-10 | Enterprise network and endpoints: WAN to 46 offices and operations centers, about 15,800 endpoints | On-premises | Cached | EDR on all corporate endpoints |
| SYS-11 | ERP (finance, supply chain, work and asset management) and payroll | DC-1 and DC-2 | Employee data | SOX IT general controls tested annually |
| SYS-12 | OT DMZs and remote access: CIP Intermediate Systems for the EMS (EACMS); ADMS DMZ with 4 jump hosts; OT PAM; OT file transfer and patch staging | On-premises at the TCC, backup TCC, DCC, and backup DCC | No | All vendor and engineer remote access to OT is meant to pass through these |
| SYS-13 | Security operations: SIEM, EDR, passive OT network sensors, vulnerability management | SaaS and on-premises | Incidental | OT sensors cover the TCC, backup TCC, DCC, backup DCC, Substations P, R, and K, and 171 of 418 distribution substations (41%) |
| SYS-14 | Utility Services platform (SL-1): CIS and MDM partitions for 7 client utilities, outage call overflow | Cloud provider A | Yes (clients' customer data) | SOC 2 Type 2 (Security, Availability, Confidentiality) since 2024 |
| SYS-15 | Fleet charging platform (SL-2): vendor charging management SaaS, company-built fleet portal, 1,450 company-operated chargers at 62 client sites | SaaS and Cloud provider B | Yes (fleet driver names, vehicle and session data) | No SOC 2 report yet |
| SYS-16 | AI and analytics portfolio (12 use cases) | Cloud provider B and vendor SaaS | Varies | Governed by the AI council formed in 2025 (P10) |
| SYS-17 | Third parties with system or data access | Various | Varies | About 1,400 vendors; 310 with system or data access; 64 with remote access paths into OT (19 of them into CIP-scope systems, all through Intermediate Systems) |

**SSP system (P02):** the *Distribution Operations Platform (DOP)*: the ADMS (SYS-02), the OMS, GIS, and mobile workforce (SYS-03), the distribution substation and field networks (distribution portion of SYS-04), and the ADMS DMZ and jump hosts (part of SYS-12), with interfaces to the EMS (SYS-01), AMI and MDM (SYS-06), the CIS (SYS-07), and security operations (SYS-13).

## 4. Current security posture: mature, with residual gaps

**In place today:**
- A mature security program aligned to NIST CSF 2.0 for IT and OT, with SP 800-82 Rev. 3 as the OT benchmark
- High, medium, and low impact CIP programs (CIP-002 to CIP-014); CIP Senior Manager designated (CIP-003-9 R3) with documented delegations (R4); last SERC compliance audit 2024-10 (2 findings, both mitigated)
- Annual enterprise risk analysis tied to ERM (NIST IR 8286 Rev. 1)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 in-house SOC for IT and OT, with passive OT network monitoring at both control centers, both DCCs, and the three medium impact substations
- Privileged access management for IT and for the EMS and ADMS domains
- Quarterly CIP access verification (CIP-004-7 R4.2) and quarterly access certification for other critical systems
- Immutable backups for cloud and data center workloads; offline EMS and ADMS backups at OCN
- Annual disaster recovery tests for tier-1 systems; annual hurricane exercise every May
- A tiered third-party risk program and a CIP-013 supply chain cyber security risk management plan
- An annual SOC 2 Type 2 report for the Utility Services platform (SL-1) since 2024
- SEC Item 106 disclosure in the annual report on Form 10-K
- Membership in the E-ISAC; cyber insurance with an incident response panel

**Residual gaps found in the 2026 assessments:**
1. **Legacy distribution substations.** 159 of 418 distribution substations use legacy serial RTUs behind serial-to-IP gateways without authentication, and OT network monitoring covers only 171 of 418 distribution substations (41%).
2. **ADMS vendor remote support path.** The ADMS vendor's remote support appliance at the DCC kept a persistent outbound tunnel that bypassed the ADMS jump hosts and OT PAM (found in P07 testing on 2026-08-12; disabled 2026-08-13 pending a redesign).
3. **ADMS recovery.** Failover to the backup DCC on 2026-04-21 took 5 hours 20 minutes against a 2-hour RTO.
4. **AMI bulk remote disconnect.** The head-end allows a single command to disconnect up to 50,000 meters with one approver; 37 users hold the bulk disconnect role.
5. **Potential CIP noncompliance** found by internal reviews and the P03 and P07 sampling: one late physical access removal (CIP-004-7 R5.1); two missed 35-day patch evaluations for the physical access control system servers (CIP-007-6 R2.2); undocumented reasons for 9 of 212 rules on the Substation K Electronic Access Point (CIP-005-7 R1.3); EMS network diagrams (BES Cyber System Information) stored in a general collaboration site (CIP-011-3 R1.2); and relay vendor remote access at 12 low impact substations without the CIP-003-9 Attachment 1 Section 6 methods. Self-reports to SERC are planned for 2026-09-30.
6. **Supply chain.** 3 of 25 sampled procurements for CIP-scope systems in 2025-2026 lacked the CIP-013-2 R1.1 risk assessment, including the new OT remote access gateways (EACMS). Vendor tiering covers 72% of the 310 vendors with system or data access.
7. **CIP-012-2 availability parts.** The plan was updated for the new availability parts (1.2 and 1.3), but the backup ICCP path to the Reliability Coordinator shares a carrier entrance with the primary path at the backup TCC.
8. **CIP-014-3 timeline.** The Substation P perimeter barrier in the R5 physical security plan slipped from 2026-06-30 to 2027-03-31 without a documented plan revision.
9. **Independence.** The OT Security team performs the internal CIP compliance checks of controls it also operates, and Internal Audit had no OT specialist until the 2026 co-source contract.
10. **Legacy OT.** 22 of 96 ADMS consoles and the DCC historian run an operating system past vendor support; the EMS vendor requires a platform upgrade by 2027-12.
11. **AI.** 12 AI use cases, 8 reviewed by the AI council. The load-forecasting model lacks automated drift monitoring, and the AMI theft analytics have not been tested for uneven flag rates across neighborhoods.
12. **Materiality.** The SEC materiality playbook has never been exercised with an OT (grid) scenario, and its quantitative factors do not use BIA outage costs.
13. **Fleet charging SOC 2.** SL-2 has no SOC 2 report; client contracts renewing in 2027 require one.
14. **Customer data.** SSNs are kept indefinitely for closed accounts; the Identity Theft Prevention Program was last updated in 2021 and does not address portal account takeover; 63 users can export the full CIS customer table.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | All applicable regulations across the enterprise: NERC CIP (CIP-002 to CIP-014, high, medium, and low impact); NERC EOP-004-4 and Form DOE-417; SEC Form 8-K Item 1.05 and Reg S-K Item 106; FTC Identity Theft Red Flags Rule and Disposal Rule; state breach and data security laws (Florida worked example). The ADMS outside CIP scope is benchmarked against NIST CSF 2.0 with SP 800-82 Rev. 3 in P02 and P07 |
| P08 | Intrusion into distribution control systems (OT) through a compromised vendor support path, with unauthorized feeder breaker operations and probing of the TCC Electronic Access Point, including an **SEC materiality assessment and 8-K Item 1.05** step and the NERC, DOE, and state workflows |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients: SL-1 Utility Services and SL-2 fleet charging services |
| P10 | Enterprise AI portfolio (12 use cases) with the AI council operating model; full assessment of AI-001, the electric load-forecasting model |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; OT stays on-premises |

**Registry defaults kept.** The primary system ("Distribution SCADA and outage management system"), the incident ("Intrusion into distribution control systems (OT)"), and the AI use case ("Electric load-forecasting model") all fit a company of this size, so they were kept. At this size the distribution SCADA is part of an ADMS, so the SSP system is the Distribution Operations Platform (ADMS plus OMS). The CIP-scope EMS is covered by the CIP program and the P03 gap analysis, and the ADMS inherits many of its controls from the shared OT security program. The incident adds the SEC materiality step, and the load-forecasting model is one item in an enterprise portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and regulatory gap analysis (control center and substation walkthroughs 2026-07-14 to 2026-07-16) |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit with the co-sourced OT specialist firm (DCC and substation testing 2026-08-11 to 2026-08-13, coordinated with the DCC and TCC) |
| 2026-09-04 | Assessment report issued |
| 2026-09-10 | Results to the board risk and reliability committee and the audit committee |
| 2026-09-30 | Planned self-reports to SERC of the potential CIP noncompliances (P03) |
| 2026-11-18 | Disclosure committee tabletop with an OT scenario (P08) |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Workforce breakdown.** 4,900 line, substation, and field operations; 410 system operations (96 at the TCC, 210 at the DCC and backup DCC, the rest in regional dispatch, outage coordination, and training); 1,050 engineering, planning, and asset management; 780 information technology; 160 OT engineering and OT security; 115 cybersecurity outside OT (SOC, GRC, identity, architecture); 2,100 customer operations; 180 Utility Services; 90 fleet charging services; 1,950 finance, HR, legal, compliance, audit, supply chain, facilities, corporate security, and communications; 265 executives and senior managers.

**Daily values.** Retail revenue about $12.5 million per calendar day. A complete distribution outage of a large district costs far less in lost sales than in restoration cost and reputational harm; the BIA (P05) uses restoration cost, lost sales, regulatory penalties, and customer credits. Wholesale imbalance charges for a missed or poor day-ahead schedule run about $400,000 on a normal day and up to $3 million on a peak day. Utility Services fees are about $4.2 million a month with 5% monthly fee credits for each missed service level. Fleet charging fees are about $3.3 million a month.

**Daily volumes.** About 8,200 move-ins and 7,600 move-outs a day; about 6,500 remote connects and disconnects a day; about 52,000 contact center calls a day in normal weather and up to 600,000 in a hurricane.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Vice President, Distribution Operations | System owner of the Distribution Operations Platform (P02); runs the DCC |
| Director, Distribution Control Center | DCC operations; operational incident commander for distribution OT incidents |
| Director, Transmission Operations | Runs the TCC (TOP); delegate for CIP-002 R2.2 approval (delegation dated 2025-01-15 under CIP-003-9 R4) |
| Director, OT Engineering | ADMS, OMS, and substation automation engineering (common control provider for OT platforms) |
| Director, OT Security | OT security architecture, OT PAM, OT monitoring, CIP technical controls |
| Director, Security Operations | Runs the 24x7 SOC; enterprise incident commander for cyber incidents |
| Director, NERC Compliance | NERC compliance program, self-reports, SERC audits (reports to the Chief Compliance Officer) |
| Director, Identity and Access Management | Enterprise identity platform (SYS-08) |
| Director, Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director, Network Engineering | Enterprise WAN and data center networks (common control provider) |
| Director, Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews; CIP-013 plan coordinator (in the GRC team) |
| Director, Corporate Security | Physical security of control centers and substations; CIP-006 and CIP-014 programs |
| Vice President, Customer Operations | CIS data owner; **Identity Theft Prevention Program administrator** (designated senior management employee); customer notices |
| Chief Privacy Officer | Privacy program, breach determinations under state laws (reports to the General Counsel) |
| Vice President, Utility Services | SL-1 service line owner |
| Vice President, eMobility | SL-2 fleet charging service line owner |
| Director, Power Supply and Load Forecasting | Business owner of the load-forecasting model (AI-001) |
| Chief Data and Analytics Officer | Chairs the AI council; data platform owner |
| Chief Human Resources Officer | Onboarding, terminations, personnel risk assessments (CIP-004 R3), training records |
| Controller | SOX program owner for financial reporting controls |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Corporate Communications | Customer, media, and staff messages in incidents and storms |
| Director, Emergency Management | Storm and emergency plans; crisis management team coordinator |

**Risk acceptance.** Very Low and Low: risk owner (vice president or director) with GRC concurrence. Moderate: CISO with the accountable executive. High: executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the risk and reliability committee. Very High: CEO and CFO jointly, reported to the risk and reliability committee at its next meeting. A known or potential noncompliance with a NERC Reliability Standard is never accepted as a risk; it is mitigated and self-reported.

**Where roles overlap and how it is compensated.** The SVP, Transmission and System Operations is both the CIP Senior Manager and the executive over the systems the CIP program protects, and the OT Security team both operates OT controls and performs internal CIP checks (gap 9). Compensating measures: the NERC compliance program reports to the Chief Compliance Officer, not to operations; Internal Audit performs the independent assessment (P07) with a co-sourced OT specialist firm and reports to the audit committee; and the CISO reports program status directly to the risk and reliability committee.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, Chief Compliance Officer, SVP Transmission and System Operations, and Vice President, Investor Relations, advised by outside securities counsel.

**Service lines offered to external clients (P09).** SL-1 Utility Services: CIS hosting, billing, meter data management, and outage call overflow for 7 client utilities (4 municipal utilities and 3 electric cooperatives in Florida and Georgia, about 410,000 meters). SOC 2 Type 2 (Security, Availability, Confidentiality) issued annually since 2024; the clients rely on the company as their third-party agent for customer data. SL-2 fleet charging services: managed charging-as-a-service for 62 commercial fleet and municipal clients (1,450 chargers), with the vendor charging management SaaS as a subservice organization.

**Cyber insurance.** $150 million tower with a $10 million retention. Notice goes through the carrier hotline; panel breach counsel and an OT-capable forensics firm are pre-approved.

**Recovery facts.** EMS data replicates continuously from the TCC to the backup TCC; the last backup TCC transfer exercise (2026-05-12) took 48 minutes. ADMS replicates to the backup DCC; the 2026-04-21 failover test took 5 hours 20 minutes. Weekly offline ADMS and EMS backups are kept at OCN.

**Workforce activity.** 1,180 terminations and 640 internal transfers in the 12 months to 2026-06-30; 2,460 individuals hold authorized electronic or unescorted physical access to high or medium impact BES Cyber Systems.

**CIS export area.** A data platform zone in Cloud provider A receives nightly CIS extracts (about 5.5 million customer records, including closed accounts) for reporting and analytics.

**Terminology.** "Distribution Operations Platform (DOP)" is the SSP system in P02, identifier CSC-DOP-01. "BCSI" is BES Cyber System Information. "EACMS" is Electronic Access Control or Monitoring Systems; "PACS" is Physical Access Control Systems.
