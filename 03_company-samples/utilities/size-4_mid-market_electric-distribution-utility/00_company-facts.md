# Scenario facts: Cris Santos Company | Utilities | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held investor-owned electric distribution utility; private equity-backed; board with an audit committee) |
| Business | Electric power distribution (NAICS 221122). Buys power under a full-requirements contract with one wholesale supplier and a 150 MW solar power purchase agreement, and delivers it over its own 69 kV sub-transmission lines (not part of the Bulk Electric System) and 13.2 kV and 23 kV distribution system to residential, commercial, and industrial customers. Owns no generation |
| Second business line | **Utility Services:** contract billing, customer information system (CIS) hosting, after-hours outage call handling, and meter data management for 4 client utilities (2 municipal utilities and 2 electric cooperatives, about 58,000 meters). About $14 million a year in fees. Client contracts renewing in 2027 require a SOC 2 Type 2 report (P09) |
| Location | Florida only. Headquarters with the Distribution Control Center (DCC) and the primary data room; the West Operations Center with the backup DCC; North, South, and East Operations Centers with crew yards. 74 substations: 68 distribution substations and 6 delivery-point substations |
| Customers and load | About 265,000 meters (232,000 residential, 33,000 commercial and industrial). 2025 summer peak load 1,480 MW |
| Workforce | 850 employees (breakdown in section 7) |
| Revenue | About $610 million a year (fictional): about $596 million in retail sales and $14 million in Utility Services fees. The SBA standard for NAICS 221122 is 1,100 employees (13 CFR 121.201), so the company is SBA-small even though it is sized as Mid-Market (see the README sizing note) |
| Grid connection | Takes delivery at 6 delivery-point substations from 2 neighboring transmission owners: 230 kV from Transmission Owner A at Substations N and E, and 115 kV from Transmission Owner B at Substations L, H, W, and S. At **Substations N, E, L, and H** the company owns the BES line protection relays, which are part of a required transmission Protection System maintained under PRC-005. At Substations W and S the transmission owner owns all BES protection. The company took ownership of the protection at Substations L and H from Transmission Owner B on 2025-06-01 |
| NERC registration | **Registered Distribution Provider (DP)** on the NERC Compliance Registry, meeting criteria III.a.1 (more than 75 MW of peak Load directly connected to the BES) and III.a.2 (owns Facilities that are part of a required transmission Protection System) of the NERC Statement of Compliance Registry Criteria (Rules of Procedure Appendix 5B). Not registered for any other function. Regional Entity: SERC Reliability Corporation |
| CIP impact rating | **Low impact only, today.** The relays at Substations N, E, L, and H (26 relays in total) are low impact BES Cyber Systems under CIP-002-5.1a Attachment 1 criterion 3.6 (Protection Systems specified in Applicability section 4.2.1.3). No high or medium impact BES Cyber Systems. Last CIP-002 review and approval: 2025-12-09 (4 assets) |
| Not in CIP scope today | **UFLS:** feeder underfrequency load shedding relays at 41 substations shed about 440 MW in stages under the regional UFLS program. Each relay acts on its own, with no common control system, so the program does not meet CIP-002-5.1a Applicability 4.2.1.1 or Attachment 1 criterion 2.10. **Distribution SCADA, OMS, and the ADMS pilot:** a DP is not one of the four functions in the NERC "Control Center" definition, and DP systems not listed in section 4.2.1 are exempt (section 4.2.3.4). They are protected under the voluntary benchmark instead (NIST CSF 2.0 with SP 800-82 Rev. 3). No Remedial Action Schemes and no Blackstart Cranking Paths |
| Pending CIP scope change | The **advanced distribution management system (ADMS)** project (go-live planned 2027-06) includes a centralized adaptive load-shedding module. As designed, operators would arm it and it would then shed 300 MW or more automatically under a common control system. CIP-002-5.1a Attachment 1 criterion 2.10 and its guidance treat an operator-armed scheme that then trips automatically as not requiring human operator initiation, so the ADMS would make that system a **medium impact** BES Cyber System. The project gate did not include a CIP-002 review (gap 1) |
| Credit and identity data | The company obtains consumer reports to decide deposits for new residential accounts and reports unpaid final bills to a collection agency. Utility accounts are covered accounts, so the FTC Identity Theft Red Flags Rule (16 CFR 681.1) and Disposal Rule (16 CFR Part 682) apply (P03). The CIS holds Social Security numbers, driver license numbers, and bank account numbers for automatic payment |
| Other regimes considered and not applicable | TSA pipeline security directives (no pipelines), NRC 10 CFR 73.54 (no reactors), SDWA section 1433 (no water system), SEC cybersecurity disclosure rules (privately held), NERC CIP-014 (not a Transmission Owner) |
| Payment cards | Card payments use the payment processor's hosted page and IVR payment service. No card data is stored in company systems. PCI DSS is a contractual obligation, noted and not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (customer personal information, Fla. Stat. 501.171). About 6% of residential accounts have an out-of-state mailing address (seasonal residents), so breach notices follow the law of each state where affected individuals reside, with Florida as the worked example |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors and its audit committee | Quarterly cyber risk reporting; approves the Identity Theft Prevention Program (16 CFR 681.1(e)(1)); receives the risk appetite and POA&M status |
| President and CEO | Accepts High risks (temporary, with dated plans); approves the risk appetite, POL-01, and the security budget |
| Chief Operating Officer | **CIP Senior Manager** (identified by name in the CIP-003-9 R3 record; this sample uses the title only). System owner of the Distribution Operations Platform. Executive sponsor of the security program; accepts Moderate risks |
| Chief Financial Officer | Security budget, cyber insurance, vendor contracts; executive sponsor of the SOC 2 engagement |
| General Counsel | Legal privilege, breach determinations with outside counsel, regulator correspondence. The NERC Compliance Manager reports to this role, so compliance is independent of operations |
| Vice President of Customer Operations | Owner of customer data in the CIS; **Identity Theft Prevention Program administrator** (designated senior management employee); customer notices |
| Director of Utility Services | Runs the contract services for the 4 client utilities; owner of the SOC 2 system description (P09) |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, board reporting, risk appetite proposals |
| Director of Information Technology | IT operations, identity provider, cloud landing zone, corporate network |
| Information Security Manager, with 3 security analysts (one focused on OT) and a GRC analyst | Day-to-day security lead for IT and OT: security operations, vulnerability management, MSSP oversight, policies and standards, GRC |
| Director of System Operations | Runs the 24x7 DCC; operational incident commander for OT incidents; files DOE-417 |
| Director of Engineering and Protection | Owns relays and Protection Systems (PRC-005), substation physical access, and CIP-002 identifications. Delegate for CIP-002 R2.2 approval (delegation dated 2024-02-15 under CIP-003-9 R4) |
| OT Engineering Manager | Leads the SCADA and OT team of 8: SCADA, OT network, OT domain accounts, OT DMZ, OT backups |
| ADMS Program Manager | Runs the ADMS project and the FLISR pilot |
| NERC Compliance Manager, with a compliance analyst | CIP, EOP-004, and DOE-417 evidence; the compliance calendar; SERC submissions and self-reports |
| Director of Power Supply and Rates | Wholesale scheduling; business owner of the load-forecasting model (P10) |
| Lead Load Forecasting Analyst | Builds and runs the load-forecasting model, with one data analyst |
| HR Director | Onboarding, terminations, background checks, key and badge return |
| Director of Corporate Communications | Customer, media, and staff messages in incidents and storms |
| Internal audit (co-sourced firm with an OT specialist subcontractor) | Annual IT audit; the P07 assessment; reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR and SIEM alerts for IT, and of alerts from the OT network sensors at the DCC, backup DCC, and OT DMZ |
| External parties | SCADA and ADMS vendor (support, patches, remote access); relay testing contractor (PRC-005 testing with its own laptops); AMI vendor (SaaS head-end); CIS vendor (SaaS); contact center platform vendor; payment processor; consumer reporting agency; collection agency; wholesale supplier; solar PPA counterparty; Transmission Owners A and B; the Balancing Authority and Reliability Coordinator for the area; cyber insurer and its incident response panel |

**Risk acceptance.** Low and Very Low: the risk owner (director level). Moderate: Chief Operating Officer. High: President and CEO, for up to 12 months with a dated treatment plan. Very High: not acceptable; the CEO may approve a temporary exception of up to 90 days after notifying the audit committee chair. A known noncompliance with a NERC Reliability Standard is never accepted as a risk; it is remediated and self-reported.

**Where roles overlap.** The Chief Operating Officer is both the CIP Senior Manager and the owner of the system the CIP program protects, and the Information Security Manager both runs and helps design many controls. The company compensates in three ways: the NERC Compliance Manager reports to the General Counsel, the co-sourced internal audit firm performs the control assessment and reports to the audit committee, and the vCISO reports program status to the board directly.

## 3. Systems

| ID | System | Hosting | Customer PI? | Notes |
|---|---|---|---|---|
| SYS-01 | Distribution SCADA: master station (primary at the DCC, hot standby at the backup DCC), 14 HMI consoles (10 at the DCC, 4 at the backup DCC), historian, 2 engineering workstations | On-premises OT network | No | Monitors and controls substation breakers, feeder reclosers, and capacitor banks. Separate OT Windows domain. EDR agents approved by the SCADA vendor since 2025 |
| SYS-02 | Outage management system (OMS) and GIS | Vendor software run by the company in the operations workloads account of SYS-09 | Yes (names, addresses, phone numbers, premise locations) | Receives SCADA breaker status and AMI outage events; predicts outages; dispatches crews; includes the switching order and clearance module |
| SYS-03 | Substation automation and field network | 74 substations; company fiber to 40, licensed radio and private LTE to 34 | No | Substation RTUs and gateways, routers, about 1,900 field devices (reclosers, capacitor controls, line sensors, FLISR switches). DNP3 over IP to the SCADA master |
| SYS-04 | Low impact BES Cyber Systems and their access control gateways | Substations N, E, L, and H | No | 26 relays (230 kV and 115 kV line protection) and the substation gateway at each site that enforces the CIP-003-9 Attachment 1 Section 3.1 electronic access controls |
| SYS-05 | Advanced metering infrastructure (AMI): head-end, collectors, 265,000 meters, plus a separate tenant for the 58,000 meters of the Utility Services clients | Vendor SaaS head-end | Yes (usage data) | Meters can be remotely connected and disconnected. AMI vendor SOC 2 Type 2 (P09) |
| SYS-06 | Customer information system (CIS) and billing, customer portal, IVR, with partitions for the 4 Utility Services clients | Vendor SaaS | Yes (SSNs, driver license numbers, bank account numbers) | Card payments use the processor's hosted page and IVR service; no card data in company systems |
| SYS-07 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects all SaaS, the cloud console, the VPN, and the OT jump hosts (federated for vendor and engineer access since 2026-03). Not used for the OT Windows domain |
| SYS-08 | Productivity suite (email, files, chat) and contact center platform | SaaS | Yes (call recordings, case notes) | The contact center platform includes a generative AI agent assistant (AI-003) |
| SYS-09 | Cloud landing zone: 6 accounts (management, security and log archive, network hub, operations workloads, analytics, backup) | Public cloud (vendor-agnostic) | Yes (OMS, meter data warehouse) | Hosts the OMS and GIS, the mobile workforce back end, the meter data warehouse, the load-forecasting workspace, logs, and backups (P04) |
| SYS-10 | Corporate network: headquarters and 4 operations centers, 980 laptops and desktops, remote access VPN | On-premises | Cached | EDR on all corporate endpoints; VPN authenticates through SYS-07 with MFA since 2024 |
| SYS-11 | Mobile workforce: 310 rugged tablets in trucks | Cellular to SYS-09 | Limited | OMS mobile, switching orders, and GIS maps |
| SYS-12 | OT DMZ | On-premises at headquarters, with a replica at the West Operations Center | No | 2 jump hosts (vendor and engineer access with MFA), historian replica, OMS-SCADA integration server, file transfer server, patch staging server, OT sensor collector |
| SYS-13 | Security monitoring: SIEM and EDR (MSSP-operated), passive OT network sensors | SaaS and on-premises sensors | Incidental | OT sensors cover the DCC, the backup DCC, and the OT DMZ only, not substations or the field network |
| SYS-14 | ADMS: FLISR pilot on 40 feeders today; full ADMS with the adaptive load-shedding module planned for 2027-06 | On-premises OT network at headquarters | No | Vendor-integrated with SYS-01 and SYS-02; ADMS Program Manager owns it |
| SYS-15 | AI and analytics models | Built in-house in SYS-09 or embedded in vendor SaaS | Varies | Six use cases in P10, including the load-forecasting model (AI-001) |
| SYS-16 | Third parties with system or data access | Various | Varies | About 85 vendors; 14 have remote access paths into OT |

**SSP system (P02):** the *Distribution Operations Platform (DOP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-11, SYS-12, the ADMS FLISR pilot (SYS-14), and the operations workloads account of SYS-09, with their interfaces to SYS-05, SYS-06, and SYS-13.

## 4. Current security posture: a defined program with gaps in scale

**In place today:**
- NERC DP registration; CIP Senior Manager designated in writing (CIP-003-9 R3) and delegations documented (R4)
- CIP-002 low impact identifications reviewed and approved on 2025-12-09 (Substations N, E, L, and H)
- Low impact cyber security policy (last approved 2026-02-26, including the vendor remote access topic) and cyber security plan
- Vendor remote access to OT through 2 jump hosts with named accounts, MFA through the identity provider, access enabled per request by the DCC, and IDS signatures on the OT DMZ firewall (implemented 2026-03-25 for CIP-003-9 Attachment 1 Section 6)
- A security team (Information Security Manager, 3 analysts, a GRC analyst), a part-time vCISO, and a 24x7 MSSP
- MFA for all IT users, the VPN, the cloud console, and the OT jump hosts; EDR on corporate endpoints and on SCADA servers and HMIs
- Passive OT network monitoring at the DCC, backup DCC, and OT DMZ since 2025
- Named HMI operator accounts since 2024
- Annual risk assessment (last in July 2025); policies adopted in 2022 and updated in 2025
- Quarterly vulnerability scanning of IT; quarterly review of SCADA vendor security advisories
- Weekly offline SCADA backups at the backup DCC; immutable cloud backups in a separate backup account
- Annual CIP awareness for all staff; phishing simulations for office staff
- A 24x7 DCC with a backup DCC, and a storm restoration plan exercised every May
- An EOP-004-4 event reporting Operating Plan (reviewed 2026-01)
- A written Identity Theft Prevention Program (board approved 2010)
- Cyber insurance with an incident response panel
- An annual IT audit by the co-sourced internal audit firm

**Missing or weak, found in the 2026 assessments:**
1. **ADMS and CIP scope.** The ADMS adaptive load-shedding module would put 300 MW or more of automatic load shedding under a common control system, making it a medium impact BES Cyber System (CIP-002-5.1a criterion 2.10). The project gate has no CIP-002 review, and the company has no medium impact program (CIP-004 to CIP-011, CIP-013) to meet that outcome by the planned 2027-06 go-live.
2. **Substation H cellular modem.** The relay testing contractor installed a cellular modem at Substation H in 2025 for remote relay testing. It gives routable access to the relays that bypasses both the substation gateway access lists (CIP-003-9 Attachment 1 Section 3.1) and the jump host controls (Section 6). Found in P07 testing on 2026-08-19 and disconnected on 2026-08-20.
3. **Substations L and H were not fully brought into the low impact program** when they became low impact assets on 2025-06-01. Contractor laptops are not reviewed before connection there (Attachment 1 Section 5.2), and 2 control house keys from the former owner are unaccounted for (Section 2).
4. **IT/OT boundary.** 6 legacy firewall rules allow the corporate server administration subnet to reach the historian and the engineering workstations by remote desktop, bypassing the OT DMZ.
5. **OT privileged access.** 3 shared administrator accounts on the SCADA servers have non-expiring passwords and are also used by the SCADA vendor. Privileged access management covers IT and cloud only.
6. **OT monitoring stops at the DCC.** There is no visibility at substations or on the field network, and substation gateway logs are not collected.
7. **SCADA recovery is slower than the target.** The 2025-11 restore test took 6 hours against a 2-hour RTO, and failover to the backup DCC was last tested in 2024-04.
8. **OT asset inventory is about 75% complete.** Firmware versions for field devices are unknown, and 2 HMI consoles and the historian run an operating system past vendor support.
9. **Third-party risk does not scale.** About 85 vendors have system or data access, 34 of the contracts have security terms, reviews happen only at onboarding, and there is no supply chain review for OT purchases.
10. **AMI bulk disconnect.** Bulk-command limits and two-person approval are not enabled in the AMI head-end, and 22 users can issue bulk remote disconnects, including for client utilities' meters.
11. **Identity Theft Prevention Program is stale.** It was last updated in 2019. It does not cover portal account takeover or IVR red flags, staff training lapsed in 2023, and there is no oversight of the CIS vendor and the collection agency as service providers.
12. **Customer data minimization and disposal.** SSNs and driver license numbers are kept indefinitely for closed accounts, CIS bulk export rights are broad (41 users), and paper deposit applications at the operations centers are not disposed of consistently.
13. **AI governance is informal.** Six AI or model-based uses exist; the load-forecasting model has no validation, drift monitoring, or change control, and a generative AI assistant was turned on in the contact center without a security or privacy review.
14. **SOC 2 readiness for Utility Services.** There is no system description, CIS configuration changes for client partitions lack approval evidence, and client utilities' data is not covered by the availability testing.
15. **Field and DCC staff phishing exposure.** Phishing simulations cover office staff only (8.6% click rate in 2026-06); field and DCC staff get only the CIP awareness module.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | All applicable regulations for the primary business line: NERC CIP-002-5.1a and CIP-003-9 (low impact, with the CIP-004 to CIP-014 applicability decisions recorded); NERC EOP-004-4 and Form DOE-417 (incident and event reporting); the FTC Identity Theft Red Flags Rule (16 CFR 681.1) and Disposal Rule (16 CFR Part 682); and Fla. Stat. 501.171 (data security, breach notice, disposal). The distribution SCADA, OMS, and ADMS outside CIP scope are benchmarked against NIST CSF 2.0 with SP 800-82 Rev. 3 in P02 and P07 |
| P08 | **Two incident types:** (1) intrusion into distribution control systems (OT): unauthorized SCADA commands through a compromised vendor support path, with probing of the Substation H relay network; and (2) ransomware on corporate IT with theft of customer data from the CIS export area, affecting the Utility Services clients. Both are integrated with crisis management, the storm and emergency plan, and legal |
| P09 | SOC 2 Type 2 readiness for the Utility Services system (Security, Availability, Processing Integrity, Confidentiality), requested by the 4 client utilities; plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio: AI-001 load-forecasting model (in-house; registry default kept), AI-002 AMI theft and tamper analytics, AI-003 contact center generative AI assistant, AI-004 vegetation risk model, AI-005 enterprise generative AI assistant, AI-006 deposit risk score |
| Cloud | Six-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

**Registry defaults kept.** The primary system ("Distribution SCADA and outage management system"), the incident ("Intrusion into distribution control systems (OT)"), and the AI use case ("Electric load-forecasting model") all fit a company of this size, so they were kept. At this size the SSP system also includes the ADMS FLISR pilot, the second incident type covers the customer data exposure that a larger customer base and the Utility Services line create, and the load-forecasting model is one item in a portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (substation walkthroughs 2026-07-21 to 2026-07-23) |
| 2026-08-10 to 2026-08-28 | Control assessment by the co-sourced internal audit firm with its OT specialist (substation testing 2026-08-18 to 2026-08-20, coordinated with the DCC) |
| 2026-09-17 | Deliverables approved by the President and CEO and the Chief Operating Officer (CIP Senior Manager); results presented to the board audit committee |
| 2026-09-30 | Planned self-report to SERC of the potential CIP-003-9 noncompliances (gaps 2 and 3; P03) |
| 2026-12-10 | Board decision on the ADMS load-shedding design (gap 1) and approval of the updated Identity Theft Prevention Program (gap 11) |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Workforce breakdown | 330 line and field operations; 62 substation, protection, and metering; 36 system operations (28 system operators and distribution dispatchers on a 24x7 rotation, 6 shift supervisors, the Director of System Operations, and a training coordinator); 9 OT engineering (the OT Engineering Manager, 4 SCADA and ADMS engineers, an OT network engineer, 2 OT technicians, and the ADMS Program Manager); 44 engineering, planning, and GIS; 38 information technology and security; 2 NERC compliance; 160 customer operations; 42 Utility Services; 12 power supply and rates; 95 finance, HR, procurement, legal, communications, facilities, and fleet; 20 executives and senior managers |
| Daily values | Retail revenue is about $1.63 million a day. Utility Services fees are about $1.17 million a month; client contracts give a 5% monthly fee credit for each missed service level. Wholesale imbalance charges for a missed or poor day-ahead schedule run about $150,000 on a normal day and up to $1.2 million on a peak day |
| Daily volumes | About 1,100 move-ins and 1,000 move-outs a day; about 900 remote connects and disconnects a day; about 9,000 calls a day to the contact center in normal weather and up to 90,000 in a hurricane |
| Cyber insurance | $25 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics, including an OT-capable firm. Notice goes through the carrier hotline before incident vendors are engaged |
| Vendor access to OT | 14 vendors have remote access paths into OT. 11 use the jump hosts; the SCADA and ADMS vendor uses the jump hosts plus the 3 shared server administrator accounts; the relay testing contractor used the Substation H cellular modem (gap 2) |
| CIS export area | A file share in the analytics account receives nightly CIS extracts (about 410,000 customer records, including closed accounts and the client utilities' customers) for reporting and the meter data warehouse |
| Recovery facts | SCADA database replication to the hot standby is continuous. Weekly offline SCADA backups are kept at the backup DCC. The 2025-11 restore test took 6 hours. The OMS restore test on 2026-05-19 took 3 hours 10 minutes |
| Workforce activity | 96 terminations and 58 internal transfers in the 12 months to 2026-06-30 |
| Utility Services clients | Client A and Client B (municipal utilities) and Client C and Client D (electric cooperatives). As governmental entities and covered entities under Fla. Stat. 501.171, the clients rely on the company as their third-party agent for customer data |
| Terminology | "Distribution Operations Platform (DOP)" is the SSP system in P02, identifier CSC-DOP-01. "Utility Services system" is the SOC 2 system in P09 |
| Additional role titles | Controller; Director of Customer Service; Credit and Collections Manager; Director of Vegetation Management; Facilities Manager; Procurement Manager |
