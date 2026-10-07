# Scenario facts: Cris Santos Company | Utilities | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held electric distribution utility) |
| Business | Electric power distribution (NAICS 221122). Buys all of its power from a wholesale supplier under a full-requirements contract and delivers it over its own 13.2 kV and 23 kV distribution system to residential and commercial customers |
| Location | Florida. Headquarters with the Distribution Control Center (DCC); a North operations center with the backup DCC and a line crew yard; a South crew yard. 22 substations |
| Customers and load | About 72,000 meters (61,500 residential, 10,500 commercial and small industrial). 2025 summer peak load 410 MW |
| Workforce | 250 employees: 118 line and field operations, 16 substation and protection, 14 system operations (12 system operators on a 24x7 rotation, the SCADA/OT Administrator, and an OT technician), 12 engineering and GIS, 8 IT, 46 customer service and billing, 4 power supply and rates, 22 finance, HR, procurement and administration, 10 executives and managers |
| Revenue | $158 million a year (fictional). The SBA standard for NAICS 221122 is 1,100 employees (13 CFR 121.201), so the company is SBA-small |
| Grid connection | Takes delivery at four delivery-point substations fed at 115 kV from the neighboring transmission owner. At two of them (**Substation N** and **Substation E**) the company owns the 115 kV line protection relays for the Bulk Electric System (BES) line terminals. Those relays are a required transmission Protection System subject to PRC-005. At the other two, the transmission owner owns all 115 kV protection |
| NERC registration | **Registered Distribution Provider (DP)** on the NERC Compliance Registry. Registration criteria met: III.a.1 (DP system serving more than 75 MW of peak Load directly connected to the BES) and III.a.2 (owns Facilities that are part of a required transmission Protection System), NERC Rules of Procedure Appendix 5B. Not registered for any other function |
| Regional Entity | SERC Reliability Corporation. The former FRCC Regional Entity was dissolved in 2019 and its registered entities, including those in Florida, were transferred to SERC (FERC approvals in Docket RR19-4) |
| CIP impact rating | **Low impact only.** The Substation N and Substation E relays are low impact BES Cyber Systems under CIP-002-5.1a Attachment 1, criterion 3.6 (for DPs, Protection Systems specified in Applicability section 4.2.1). No high or medium impact BES Cyber Systems. Last CIP-002 review and approval: 2025-11-18 |
| Not in CIP scope | **UFLS:** the company's feeder underfrequency load shedding relays (about 125 MW in stages under the regional UFLS program, PRC-006-SERC-03) act independently at each substation. They are not under a common control system and total less than 300 MW, so they do not meet CIP-003-9 section 4.2.1.1. **Distribution SCADA and OMS:** a DP is not one of the four functions in the NERC "Control Center" definition, and DP systems not listed in section 4.2.1 are exempt (section 4.2.3.4). They are protected under the voluntary benchmark instead (NIST CSF 2.0 with SP 800-82 Rev. 3). No Remedial Action Schemes and no Blackstart Cranking Paths |
| Other regimes considered and not applicable | TSA pipeline security directives (no pipelines), NRC 10 CFR 73.54 (no reactors), SDWA 1433 (no water system), SEC disclosure rules (privately held) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). Customer records in the CIS include Social Security numbers collected for credit and deposit decisions and bank account numbers for automatic payment. The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner (Cris Santos) | Chairs the board of managers; accepts High and Very High risks |
| President and CEO | Executive owner of the security program; accepts Moderate risks; signs policies |
| Vice President of Operations | **CIP Senior Manager** (identified by name in the CIP-003-9 R3 designation record; this sample uses the title only). System owner of the Distribution Operations Platform |
| Chief Financial Officer | Security budget, cyber insurance, vendor contracts |
| Manager of System Operations | Runs the 24x7 DCC; operational incident commander for OT incidents |
| Manager of Engineering and Protection | Owns relays and Protection Systems (PRC-005), substation physical access, CIP-002 identifications. Delegate for CIP-002 R2.2 approval (delegation dated 2024-03-01 under CIP-003-9 R4) |
| NERC Compliance Coordinator | Part-time duty of a senior protection engineer. Maintains CIP and EOP-004 evidence, the compliance calendar, and SERC submissions |
| IT Manager | Information Security Lead for IT and OT (part-time duty). Runs the IT team of 8 |
| SCADA/OT Administrator | Day-to-day SCADA, OT network, OT accounts, and OT backups |
| Customer Service Manager | Owns CIS data, customer communications, and breach notice logistics |
| Manager of Power Supply and Rates | Wholesale scheduling with the supplier; business owner of the load-forecasting model (P10) |
| Load Forecasting Analyst | Built and runs the load-forecasting model |
| HR Manager | Onboarding, terminations, background checks, key and badge return |
| External parties | SCADA vendor (support and patches, remote access); relay testing contractor (PRC-005 testing with its own laptops); OMS software vendor; AMI vendor (SaaS head-end); CIS vendor (SaaS); card payment processor; wholesale power supplier; transmission owner, Balancing Authority, and Reliability Coordinator for the area; cyber insurer and its incident response panel |

## 3. Systems

| ID | System | Hosting | Customer PI? | Notes |
|---|---|---|---|---|
| SYS-01 | Distribution SCADA: master station (primary server at the DCC, standby server at the backup DCC), 6 operator HMI consoles, historian, engineering workstation | On-premises OT network | No | Monitors and controls substation breakers, feeder reclosers, and capacitor banks. Separate OT Windows domain |
| SYS-02 | Outage management system (OMS) and GIS | Vendor software run by the company on SYS-09 | Yes (names, addresses, phone numbers) | Receives SCADA breaker status and AMI outage events; dispatches crews |
| SYS-03 | Substation automation and field network | 22 substations; company fiber to 9, licensed radio and private cellular to 13 | No | Substation RTUs and gateways, routers, about 160 reclosers and capacitor controls. DNP3 over IP to the SCADA master |
| SYS-04 | Low impact BES Cyber Systems and their access control gateways | Substation N and Substation E | No | Eight 115 kV line protection relays (the low impact BES Cyber Systems) and the substation gateway at each site that enforces the CIP-003-9 Attachment 1 Section 3.1 electronic access controls |
| SYS-05 | Advanced metering infrastructure (AMI): head-end, collectors, 72,000 meters | Vendor SaaS head-end | Yes (usage data) | Meters can be remotely connected and disconnected. The AMI vendor provides a SOC 2 Type 2 report (P09) |
| SYS-06 | Customer information system (CIS) and billing, customer portal, IVR | Vendor SaaS | Yes (SSNs, bank account numbers) | Card payments use the processor's hosted payment page; no card data in company systems |
| SYS-07 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-06, SYS-08, SYS-09, and SYS-05 administration. Not used for the OT domain |
| SYS-08 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-09 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes (via SYS-02) | Hosts the OMS and GIS, the analytics workspace (load-forecasting model), the backup vault, and the log workspace |
| SYS-10 | Corporate network, 230 laptops and desktops, remote access VPN | On-premises | Cached | EDR on corporate endpoints since 2025 |
| SYS-11 | Mobile workforce: 110 rugged tablets in trucks | Cellular to SYS-09 | Limited | OMS mobile and GIS maps |
| SYS-12 | OT DMZ | On-premises | No | Remote access jump host (vendor and engineer access), historian replica, OMS-SCADA integration server, file transfer server |
| SYS-13 | Electric load-forecasting model | Built in-house on SYS-09 | No (aggregated AMI data only) | Day-ahead and 7-day hourly forecasts (see P10) |

**SSP system (P02):** the *Distribution Operations Platform (DOP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-11, SYS-12, the OMS and GIS workloads of SYS-09, and their interfaces to SYS-05 and SYS-06.

## 4. Current security posture: partially compliant

**In place today:**
- NERC DP registration; CIP Senior Manager designated in writing (CIP-003-9 R3) and one delegation documented (R4)
- CIP-002 low impact identification reviewed and approved on 2025-11-18
- A low impact cyber security plan (adopted 2022) and a low impact cyber security policy (last approved 2025-06-20)
- Annual cyber security awareness reinforcement by computer-based module and posters (CIP-003-9 Attachment 1 Section 1), last delivered 2026-03
- Substations fenced, locked, and door-alarmed to the DCC; relay panels inside locked control houses
- Routable access to the Substation N relays restricted by gateway access lists to the SCADA master and the relay engineering workstation
- Company-managed relay laptops with antivirus and application allowlisting
- MFA through the identity provider for SaaS, the cloud console, and email; EDR on corporate endpoints
- A 24x7 staffed DCC with a backup DCC, and a storm restoration plan exercised every June
- An EOP-004-4 event reporting Operating Plan (reviewed 2026-02)
- Nightly SCADA database backups; daily backups of cloud workloads
- Card payments through the processor's hosted page; the CIS vendor's SOC 2 Type 2 report on file
- Cyber insurance with an incident response panel

**Missing or weak, found in the 2026 assessments:**
1. CIP-003-9 vendor electronic remote access controls (Attachment 1 Section 6), effective 2026-04-01, are not implemented. The SCADA vendor and the relay testing contractor share one standing account on the OT jump host, without MFA, and nothing detects malicious communications on those sessions. The low impact policy did not cover the new topic (R1 Part 1.2.6) until it was re-approved on 2026-09-04.
2. The low impact Cyber Security Incident response plan was last tested by tabletop on 2023-06-14. The 36-month test (Attachment 1 Section 4.5) was due by 2026-06-14 and was missed.
3. Contractor relay-test laptops are connected to low impact relays with no pre-connection review (Attachment 1 Section 5.2). There is no dedicated removable media scanning station (Section 5.3).
4. The firewall between the corporate network and the SCADA network holds 14 legacy "any" rules. The OT DMZ is bypassed for OMS and historian traffic.
5. The 6 SCADA HMI consoles use shared operator accounts. SCADA administrator accounts have never been reviewed.
6. No OT security monitoring. SCADA, gateway, and jump host logs are not collected or reviewed.
7. Two HMI consoles and the historian run an operating system version past vendor support. There is no OT patch or vulnerability process.
8. SCADA backups are kept on the standby server in the same OT network, offline copies do not exist, and no restore has been tested. Failover to the backup DCC was last tested in 2023.
9. The OT asset inventory is incomplete (substation gateways, radios, relay firmware versions).
10. Substation control house keys are not tracked. Keys held by 3 former employees were never recovered.
11. The legacy corporate VPN uses passwords only. 30 field supervisors and 6 engineers use it, and engineers use it to reach the OT jump host.
12. Phishing training and exercises cover office staff only. Field and DCC staff receive only the annual CIP awareness module.
13. The load-forecasting model has no documented validation, drift monitoring, or change control, although its output drives day-ahead power purchases and peak-day operating plans.
14. Contracts with the SCADA, OMS, and AMI vendors have no security requirements (incident notice, remote access terms). The AMI vendor's SOC 2 report had never been requested before this assessment.
15. The Substation E gateway access list permits any routable traffic from the OT network to the relays. It was left open after the 2025 commissioning (found during P07 testing on 2026-08-12 and corrected on 2026-08-13).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | Primary: NERC CIP, scoped to CIP-002-5.1a and CIP-003-9 (low impact). Secondary: electric incident and event reporting (NERC EOP-004-4 and DOE Form DOE-417). The distribution SCADA outside CIP scope is benchmarked against NIST CSF 2.0 with SP 800-82 Rev. 3 in P02 and P07 |
| P08 incident | Intrusion into distribution control systems (OT): unauthorized SCADA commands through the shared vendor account on the OT jump host, with probing of the Substation E relay network |
| P09 SOC 2 | The company is not a service organization for its customers. (a) Security-only self-benchmark; (b) review of the AMI vendor's SOC 2 Type 2 report |
| P10 AI | Electric load-forecasting model (in-house) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork (substation walkthroughs 2026-07-28) |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork (substation testing 2026-08-12, coordinated with the DCC) |
| 2026-09-04 | Deliverables approved by the President and CEO; CIP policy and plan documents approved by the CIP Senior Manager |
| 2026-09-30 | Planned self-report to SERC of the potential CIP-003-9 noncompliances (gaps 1, 2, 3, and 15; P03) |
