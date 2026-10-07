# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (investor-owned water utility) |
| Business | Community water system (NAICS 221310): groundwater supply, treatment, storage, and distribution of drinking water. No wastewater service (a county utility collects and treats wastewater in the service area) |
| Location | Florida. One service area with two treatment plants: **WTP-1** (main plant, 6.0 million gallons per day (MGD) capacity, control room, lab, administration office next door) and **WTP-2** (satellite plant, 2.5 MGD, about 9 miles away, staffed day shift only and monitored remotely from WTP-1 at night) |
| Source and treatment | 14 groundwater wells. Aeration, disinfection with sodium hypochlorite, pH adjustment with sodium hydroxide (caustic), and a phosphate corrosion inhibitor. Average day demand 5.2 MGD; maximum day 7.4 MGD. 4 storage tanks (4.6 million gallons total) and 6 booster pump stations |
| Customers | **Population served: 46,200 persons** (about 18,400 metered connections: 17,150 residential, 1,250 commercial and irrigation). This is the population the company reports to the state drinking water primacy agency |
| Workforce | 60 employees: 8 management and administration, 18 treatment operations (2 Chief Plant Operators, 14 licensed operators, 2 SCADA and Instrumentation Technicians), 3 water quality laboratory, 20 distribution and field services, 9 customer service and billing, 2 IT |
| Revenue | $24.6 million a year (fictional): water rates, service fees, and connection charges. Under the SBA standard of $41.0 million for NAICS 221310 (13 CFR 121.201), so SBA-small |
| Rate regulation | Rates are set by the state utility regulator. Rate filings are outside the scope of these deliverables |
| SDWA section 1433 status | **Covered.** A community water system (42 U.S.C. 300f(15)) serving a population greater than 3,300 persons (42 U.S.C. 300i-2(a)(1)). Size category **3,301-49,999**. First-cycle RRA certified in June 2021 and ERP in December 2021. **Five-year RRA review certified to EPA on 2026-06-26** (deadline June 30, 2026). **ERP review certification due no later than 2026-12-26**: EPA states ERP certifications are due six months from the date of the RRA certification (EPA AWIA section 2013 page) |
| Not in scope | Wastewater (POTW) requirements: the company runs no wastewater system. Federal contracts: none. HIPAA: not a covered entity. Card data: customers pay by card or bank draft through the payment processor's hosted payment page, so card numbers never touch company systems (contractual PCI DSS duties sit with the processor arrangement) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (customer data breach notice, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and resilience duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; approves the security budget |
| General Manager | Executive owner of the program; accepts risk up to Moderate; signs policies; signs the EPA RRA and ERP certifications |
| Operations Manager | Owns the SCADA system and the treatment process; **RRA and ERP lead**; holds the highest-class state operator license on staff |
| IT Manager | Runs business IT and the IT side of the IT/OT boundary; part-time **security and compliance lead** for IT and OT |
| IT Support Technician | Help desk, endpoint patching, account changes |
| SCADA and Instrumentation Technicians (2) | Maintain PLCs, RTUs, HMIs, radios, and analyzers with the SCADA integrator |
| Chief Plant Operators (2) | Shift supervision at WTP-1 and WTP-2; manual operations; incident first response at the plant |
| Water Quality Supervisor | Compliance sampling, lab, public notification content; business owner of the anomaly detection pilot (P10) |
| Field Services Supervisor | Distribution system, main breaks, flushing, booster and tank site visits |
| Customer Service and Billing Manager | Customer information system (CIS), payments, call center, customer notices |
| Controller | Finance, insurance, payment processor relationship |
| HR Manager | Onboarding, terminations, background checks |
| Safety and Compliance Coordinator | Chemical safety, local emergency planning committee (LEPC) liaison, ERP document control |
| SCADA system integrator (contractor) | Programs PLCs and HMIs; remote support. No security terms in its contract (see gaps) |

## 3. Systems

| ID | System | Hosting | Holds sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | SCADA servers and HMIs: primary and standby SCADA/HMI servers, 4 operator HMI stations (3 at WTP-1, 1 at WTP-2), 1 engineering workstation, 1 process historian server | On-premises, WTP-1 control room and WTP-2 | Yes (process data, SCADA configuration) | Commissioned 2017. Servers and engineering workstation run an operating system past end of support |
| SYS-02 | PLCs and RTUs: 6 PLCs (4 at WTP-1, 2 at WTP-2) including chemical feed control; 24 RTUs (14 wells, 6 booster stations, 4 tanks) | On-premises, plants and remote sites | Yes (control logic) | Chemical feed pumps have hardwired stroke limits and independent high/low pH and chlorine alarms that do not depend on SCADA |
| SYS-03 | Telemetry: licensed radio to 18 remote sites; cellular modems (private network plan) at 6 remote sites | Radio and carrier network | No | 4 cellular modems at well sites had web administration reachable from the internet (found in P07) |
| SYS-04 | Remote access: IT-managed VPN appliance used by on-call operators (password only); the integrator's commercial remote desktop agent on the engineering workstation (always on) | On-premises appliance; vendor cloud relay | No | The P08 incident path |
| SYS-05 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts the historian replica and water quality analytics workloads, including the anomaly detection model (P10), plus the backup vault for business servers |
| SYS-06 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-05, SYS-07, SYS-08, SYS-09, SYS-10, SYS-12. **OT accounts are local and not federated** |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (RRA and ERP drafts are stored here) | |
| SYS-08 | Customer information and billing system (CIS) with customer portal | Vendor SaaS | Yes (customer PII, online account credentials) | 18,400 accounts. Vendor has a SOC 2 Type 2 report (P09). Payments through the processor's hosted page |
| SYS-09 | Advanced metering infrastructure (AMI) head-end and meter data management | Vendor SaaS | Yes (interval usage by account) | 11,000 of 18,400 meters on AMI |
| SYS-10 | Laboratory information management system (LIMS) | Vendor SaaS | Yes (compliance results) | Compliance samples also go to a contracted certified laboratory |
| SYS-11 | Business network and endpoints | On-premises (administration office, both plants) | Yes (cached) | 58 workstations and laptops, 30 rugged tablets and phones for field crews. An IT/OT firewall separates this network from the OT network |
| SYS-12 | GIS and work order and asset management | Vendor SaaS | Yes (system maps, critical asset locations) | |
| SYS-13 | Physical security: card access and cameras at both plants; intrusion alarms at well sites reported through RTUs | On-premises | No | |

**SSP system (P02):** the *Water Treatment SCADA System (WTSS)*: SYS-01, SYS-02, SYS-03, SYS-04, and the OT networks at WTP-1 and WTP-2, with their interfaces to the historian replica and anomaly detection workload in SYS-05 and to the business network (SYS-11) through the IT/OT firewall.

## 4. Current security posture: partially compliant

**In place today:**
- Operators can run both plants in manual (local) mode. Manual-operations drills are held twice a year, most recently before the 2026 hurricane season
- Chemical feed pumps have hardwired stroke limits, and pH and chlorine analyzers have independent hardwired high/low alarms to the control room
- An IT/OT firewall separates the business network from the OT network (rules are too broad; see gaps)
- MFA through the identity provider for email, the cloud console, the CIS, AMI, LIMS, and GIS
- Card access and cameras at both plants; fenced and alarmed well sites
- Standby generators at both plants and at 10 of 14 wells; fuel supply contract; membership in the state water and wastewater agency response network (WARN) for mutual aid
- Boil water notice and Tier 1 public notice templates, used after the 2024 hurricane season
- Emergency interconnect with the neighboring county utility (1.5 MGD) and a bottled water supply contract
- ERP hurricane annex updated in 2025 after the 2024 storms (the rest of the ERP is the 2021 version)
- On-call VPN limited to 9 named users, with lockout after 10 failed attempts
- First-cycle RRA and ERP (2021) on file; RRA five-year review certified 2026-06-26
- Signature antivirus and automatic OS patching on business endpoints
- Daily backups of business servers to the cloud backup vault (same account as production)
- Background checks for all new hires; security awareness training at hire
- Subscription to CISA advisories

**Missing or weak, found in the 2026 assessments:**
1. The RRA's cybersecurity element (automated systems) was carried forward from a 2021 checklist in the 2026 review. It has no OT asset inventory, network diagram, or vulnerability assessment behind it.
2. The SCADA integrator's commercial remote desktop agent on the engineering workstation is always on, uses a password only, has no session approval, and is not logged by the company.
3. On-call operator VPN access to the HMIs uses a password only (no MFA). The VPN appliance firmware is 14 months behind.
4. HMIs use a shared "operator" login, and HMI and PLC administrator passwords have not changed since commissioning in 2017.
5. The OT network is flat (HMIs, PLCs, and historian on one subnet). The historian is dual-homed to the business network, and the IT/OT firewall allows broad rules for historian traffic.
6. There is no current OT asset inventory or network diagram. The latest drawings are the integrator's 2017 as-builts.
7. The SCADA servers and engineering workstation run an operating system past end of support. OT patches have not been applied since 2023.
8. There is no OT logging or monitoring. HMI and PLC changes are not logged centrally, and no one watches OT network traffic.
9. PLC logic and HMI project files are not backed up offline. The only copies are on the engineering workstation and at the integrator.
10. The ERP's cybersecurity section is one page ("call the IT Manager"). There is no cyber incident response plan or OT playbook, and none has been exercised.
11. PLCs at WTP-1 are left in remote-program mode, and 4 cellular modems at well sites had internet-reachable web administration with default credentials (found during P07 testing).
12. Security training happens only at hire. There is no OT-specific training for operators and no phishing exercise.
13. The 2026 RRA review was not coordinated with the local emergency planning committee (LEPC); the last coordination was in 2021.
14. The SCADA integrator's contract has no security terms (incident notice, remote access rules, personnel screening).
15. The water quality anomaly detection pilot went live in May 2026 without a documented validation, change review, or approved-use rule for AI tools.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | Primary: SDWA section 1433 (42 U.S.C. 300i-2), with the RRA's cybersecurity element benchmarked against NIST CSF 2.0 and SP 800-82 Rev. 3. Secondary: SDWA public notification rule, 40 CFR Part 141 Subpart Q (Tier 1 notice for a cyber-caused treatment interruption) |
| P08 incident | Remote-access compromise of a treatment-plant HMI through the integrator's remote desktop agent, with an unauthorized change to the sodium hydroxide dose setpoint |
| P09 SOC 2 | The company is not a service organization. (a) Security-only (CC1-CC9) self-benchmark; (b) review of the CIS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | Water quality anomaly detection model (pilot) on the historian replica in the cloud tenant |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-26 | RRA five-year review certified to EPA (deadline 2026-06-30) |
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (site visits to WTP-1, WTP-2, and 6 remote sites on 2026-08-05) |
| 2026-08-31 | Deliverables approved by the General Manager (High risks by the majority owner) |
| 2026-12-11 | Internal target to certify the revised ERP |
| 2026-12-26 | Latest ERP certification date (six months after the 2026-06-26 RRA certification) |
