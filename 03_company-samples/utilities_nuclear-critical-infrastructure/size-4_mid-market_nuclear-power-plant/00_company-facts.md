# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given and was checked against the primary source on the date shown in P03. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Owns and operates one nuclear electric generating station (NAICS 221113), called **the Station**: a single-unit pressurized water reactor rated about 1,020 MW net. The company sells all of its output at wholesale |
| Location | Florida only. The Station site (protected area, owner-controlled area, administration building, warehouse, and a training center with the plant-referenced simulator) and an offsite Emergency Operations Facility (EOF) about 15 miles away. No operations in other states |
| Workforce | 850 employees: Operations 190 (including 70 licensed operators), Maintenance 170, Engineering 120, Security 140, Radiation Protection and Chemistry 60, Work Management and Outage 35, Training 40, Regulatory Affairs, Emergency Preparedness, Corrective Action Program, and Nuclear Oversight 30, IT and cybersecurity 28, business functions (finance, HR, supply chain, energy marketing, legal, communications) 37. About 300 long-term contractors work on site year-round, and about 1,000 supplemental contractors arrive for each refueling outage |
| Revenue | About $450 million a year (fictional), roughly $1.23 million per day when the unit is generating. The SBA size standard for NAICS 221113 is 1,150 employees (13 CFR 121.201), so the company is SBA-small by headcount; the tier is set by headcount under the repository's Mid-Market rule and flagged in the README |
| NRC license | Operating license under 10 CFR Part 50, renewed under Part 54. The NRC-approved **cyber security plan (CSP)** is a license condition. It follows the NEI 08-09 Rev. 6 template, and full implementation (the final milestone) was completed in 2017. NRC Regulatory Guide 5.71 Rev. 1 (February 2023) is the NRC's current acceptable approach and is used in P03 as the requirement-level benchmark for the CSP's controls |
| License transfer and ownership | Background fact, not scored in P03. The private equity sponsor's investment was an indirect transfer of control of the Part 50 license, so it needed the NRC's prior written consent (10 CFR 50.80(a)), with the transferee's technical and financial qualifications (10 CFR 50.80(b)(1)(i)). Any future change of control needs consent again. The owners are U.S. persons; foreign ownership, control, or domination would bring in 10 CFR 50.38 |
| NERC registration | Generator Owner and Generator Operator. Under CIP-002-5.1a Attachment 1, the Station's BES Cyber Systems are **low impact** (criterion 3.3): the unit is below the 1,500 MW medium-impact threshold (criterion 2.1), and its Planning Coordinator and Transmission Planner have not designated it under criterion 2.3 or 2.6. The switchyard Transmission Facilities belong to the interconnecting transmission owner. Systems, structures, and components covered by the 73.54 CSP are exempt from CIP-002 (Applicability 4.2.3.3) |
| Power sales | Two long-term wholesale power purchase agreements (PPAs): **PPA-1** with a regional electric utility for 60% of output, and **PPA-2** with a large technology company's energy subsidiary for 40% of output plus the associated clean energy attributes. PPA-2 requires hourly generation and attribute data and an annual SOC 2 Type 2 report on that data service starting with calendar 2027 (P09) |
| Refueling outages | Every 18 months. The last outage ended 2025-11-04 (32 days). The next outage starts 2027-03-08 (planned 30 days) |
| Not in scope | **SEC disclosure rules** (the company is private). **10 CFR 73.110** (not a Part 53 licensee). **CIRCIA** (proposed only; as proposed it would cover the company through the nuclear reactor sector criterion regardless of size). **Form DOE-417** as a filer (the instructions exclude commercial power reactors that are subject to the 10 CFR Part 73 event notification rules from the "Generating Entities" respondent group; the Balancing Authority files and the company supports it). **HIPAA** (the company is not a covered entity; the employee health plan is fully insured). **10 CFR Part 810 and Part 110** export controls (handled by the export compliance program; not analyzed here) |
| State law approach | Florida is cited for breach notification (Fla. Stat. 501.171). The company operates in Florida only |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` defines C-NUCLEAR-R01 to R05. This sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S06)** for the other rules that bind or commit the company. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC protection of digital computer and communication systems and networks | 10 CFR 73.54 (CSP license condition; RG 5.71 Rev. 1 benchmark) | **Applies (primary regulation in P03)** |
| C-NUCLEAR-R02 | Part 53 technology-inclusive cybersecurity | 10 CFR 73.110 | Not applicable (Part 50 licensee) |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Applies |
| C-NUCLEAR-R04 | NERC CIP Reliability Standards | 16 U.S.C. 824o; 18 CFR Part 40; CIP-002-5.1a; CIP-003-9 | Applies (low impact only) |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Not in effect; would apply through the nuclear sector criterion |
| C-NUCLEAR-S01 | Protection of Safeguards Information | 10 CFR 73.21 and 73.22 | Applies (power reactor licensee) |
| C-NUCLEAR-S02 | Personnel access authorization, including individuals with electronic access | 10 CFR 73.56 | Applies |
| C-NUCLEAR-S03 | Safety/security interface and security program reviews | 10 CFR 73.58; 10 CFR 73.55(m) | Applies |
| C-NUCLEAR-S04 | Florida breach notification | Fla. Stat. 501.171 | Applies to personal information (employees, contractors, access authorization records) |
| C-NUCLEAR-S05 | PPA-2 data service assurance | PPA-2 contract (SOC 2 Type 2, Security, Availability, Processing Integrity, Confidentiality) | Contractual |
| C-NUCLEAR-S06 | NIST CSF 2.0 and SP 800-53 Rev. 5 Moderate baseline | Voluntary | Adopted by management for the business network (P02) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and POA&M reporting |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and the security budget |
| Site Vice President | Senior licensee officer at the Station. Executive sponsor of the security programs; accepts Moderate risk; **NERC CIP Senior Manager** (CIP-003-9 R3); SSP system owner (P02) |
| Plant General Manager | Operations, maintenance, engineering, work management; receives the 73.55(m) program review reports with corporate management |
| Director of Security | Physical protection program, access authorization (73.56), Safeguards Information program; the Cyber Security Program Manager reports to this role |
| Cyber Security Program Manager | Owns the 73.54 program and the CSP; leads the Cyber Security Team (CST: 3 plant cyber engineers, 2 I&C cyber specialists, 1 cyber analyst) |
| Virtual CISO (vCISO, part-time contractor) | Enterprise security strategy across IT and the CSP interface; board reporting |
| IT Director | Business network, WMS, CAP/EDMS, and cloud operations; technical owner of the SSP system |
| IT Security Manager (with 2 security analysts) | Business network security operations, vulnerability management, MSSP oversight; **information system security officer** for the SSP |
| Compliance and GRC Lead (with 1 NERC compliance analyst) | Risk register, gap analysis, NERC CIP compliance evidence, policy management |
| Regulatory Affairs Manager | NRC interface, licensing correspondence, reportability reviews with the Shift Manager |
| Shift Manager (on shift, 24x7) | Makes NRC Operations Center notifications under 10 CFR 50.72 and 73.77 |
| Emergency Preparedness Manager | Emergency plan, ERO callout, EOF readiness |
| Director of Engineering | Design changes and configuration management, including the 73.54(d)(3) cyber evaluation of modifications |
| Director of Work Management | WMS business owner; refueling outage scheduling |
| Maintenance Manager | Balance-of-plant equipment; business owner of the predictive maintenance pilot (P10 AI-001) |
| Radiation Protection Manager | RWP and dose tracking system owner |
| Energy Marketing and Settlements Manager | PPA scheduling, settlement, and the generation data service (SOC 2 scope) |
| Chief Financial Officer, General Counsel, HR Director, Supply Chain Manager, Communications Director | Business process owners; General Counsel leads legal and notification decisions |
| Nuclear Oversight (independent assessment group) | 73.55(m) security program reviews, including the cyber security program; independent of program management |
| Co-sourced internal audit firm | Annual IT audit; P07 assessment with Nuclear Oversight |
| Managed security service provider (MSSP) | 24x7 monitoring of the business network and cloud (SIEM and EDR). No access to Level 3 or Level 4 |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Work management system (WMS) with the clearance and tagging module | On-premises, site data center (Level 2) | Work orders, equipment clearances (tagouts), maintenance history, outage schedule. The clearance and tagging module runs on 2 servers with Windows Server 2012 R2 |
| SYS-02 | Corrective action program (CAP) and electronic document management system (EDMS) | On-premises, site data center | CAP is the record system for 10 CFR 73.77(b) 24-hour recordable events. EDMS holds procedures, drawings, and licensing basis documents |
| SYS-03 | Identity: on-premises directory, cloud identity provider (SSO and MFA), cloud privileged access broker | Hybrid | All workforce and contractor identities |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | |
| SYS-05 | ERP (finance, supply chain, HR, payroll) and applicant tracking | SaaS | Supply chain records for safety-related parts; HR personal information |
| SYS-06 | Plant business network (Level 2), site data center, EOF business LAN, endpoints | On-premises | About 90 servers, 1,150 workstations and laptops, 220 rugged field tablets |
| SYS-07 | Cloud landing zone: 4 accounts (identity and security, shared services, workloads, recovery) | Public cloud (vendor-agnostic) | Plant analytics platform, generation data and settlement reporting (GDSR) application, backup vault, and pilot-light disaster recovery for SYS-01 and SYS-02 |
| SYS-08 | Security tooling: SIEM (MSSP-operated), EDR, vulnerability scanner | SaaS and on-premises | Business network and cloud only |
| SYS-09 | Plant data historian replica and the one-way device receive server (Level 2 side) | On-premises | Receives plant data from Level 3 through a one-way deterministic device; feeds engineering, AI-001, and GDSR |
| SYS-10 | Radiation protection RWP and dose tracking system | On-premises | Radiation work permits and dose records; classified as not a CDA in the CSP analysis |
| SYS-11 | Access authorization records system | Restricted enclave on the business network | 73.56 files, background checks, fitness-for-duty results; also connects to the industry shared access data system |
| SYS-12 | Level 3 and Level 4 critical digital assets (CDAs): plant process computer, balance-of-plant distributed control system, safety-related instrumentation and control, radiation monitoring | On-premises, isolated | About 1,050 CDAs in total (with SYS-13 and parts of SYS-14). Under the CSP; managed by the CST |
| SYS-13 | Security systems: physical access control, central and secondary alarm stations, video | On-premises, Level 4 | CDAs |
| SYS-14 | Emergency preparedness systems: Emergency Response Data System (ERDS) link, EP communications, ERO callout service | Mixed | ERDS and EP communications are CDAs. The ERO callout service (SaaS, adopted 2024) was never evaluated by the CST |
| SYS-15 | NERC low-impact BES Cyber Systems: dispatch telemetry RTU, dispatch workstation, interconnection revenue metering | Separate dispatch network | Outside the 73.54 CSP scope; CIP-003-9 applies |
| SYS-16 | Safeguards Information stand-alone computers | Security building | Meet 73.22(g); never connected to any network |
| SYS-17 | AI tools | Vendors | AI-001 predictive maintenance pilot (with a vendor sensor gateway), AI-002 enterprise generative AI assistant, AI-003 CAP screening assistant, AI-004 applicant ranking feature in the applicant tracking SaaS, AI-005 power price forecasting |
| SYS-18 | About 210 third-party vendors with network or data access | Various | 24 are Tier 1 under the P09 approach |

**SSP system (P02):** the *Plant Business Network and Work Management System (PBN-WMS)*: SYS-01 to SYS-11, the non-safety business systems at Level 2 and below, Moderate baseline with tailoring. The CDAs (SYS-12, SYS-13, the CDA parts of SYS-14), the NERC low-impact systems (SYS-15), and the SGI computers (SYS-16) are interconnected or separate systems outside the boundary.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- NRC-approved CSP, fully implemented since 2017, with a 6-person CST and about 1,050 CDAs assessed
- Defensive architecture with 5 levels: Level 4 and Level 3 isolated from the business network, only one-way data flow from Level 3 to Level 2 through a one-way deterministic device, no remote access to Level 4
- Portable media and mobile device (PMMD) kiosks that scan media before use at Levels 3 and 4
- 73.55(m) security program review every 24 months by Nuclear Oversight (last completed 2025-06, including the cyber security program)
- Safeguards Information program with stand-alone computers and locked containers (73.22)
- Access authorization program (73.56); CST and I&C staff with CDA administrative rights are in the program
- Business network: MFA for remote access, email, and cloud; EDR on endpoints and servers with 24x7 MSSP monitoring; SIEM; quarterly vulnerability scans; annual penetration test (last 2026-03)
- Immutable backups in a separate cloud recovery account
- Annual security awareness training and phishing simulations (June 2026 click rate 5.9%)
- Security policies adopted in 2022
- NERC CIP-003-9 low-impact cyber security plan adopted 2026-03-17

**Missing or weak, found in the 2026 assessments:**
1. Privileged access on the business network: 16 standing domain administrator accounts (14 IT staff, 2 vendor accounts). Privileged access management covers only the cloud consoles. Administrators use push MFA, not phishing-resistant MFA.
2. The server layer is flat. WMS, CAP/EDMS, the historian replica, and general file and print servers share one server VLAN, and any workstation can reach the WMS database port.
3. CDA analysis is not current (73.54(b)(1), (d)(3)). Three changes since 2023 were never evaluated by the CST: the analytics feed from the historian replica to the cloud, the predictive maintenance vendor's sensor gateway on balance-of-plant equipment, and the ERO callout service that replaced the old paging system.
4. Vendor remote access: the WMS vendor and the predictive maintenance vendor connect through a VPN with shared vendor accounts. For the dispatch RTU vendor's remote access, CIP-003-9 Attachment 1 Section 6.1 and 6.2 methods exist, but there is no method to detect known or suspected malicious communications (Section 6.3; effective 2026-04-01).
5. Recovery: the cloud pilot-light disaster recovery design for WMS and CAP/EDMS has never been failover-tested. Restores are tested only for file shares. There is no written manual fallback for recording 73.77(b) events in the CAP within 24 hours if CAP is down.
6. Logging: WMS, EDMS, and CAP application logs and the one-way device receive server do not go to the SIEM. There is no alert for business network attempts to reach Level 3 boundary addresses.
7. Incident response is split: the IT incident plan (with the MSSP) and the CSP incident response (CST, 73.77) are separate documents. The last joint drill was 2024-02. The Shift Manager's 73.77 decision aid has not been exercised with IT. IT has no out-of-band communications.
8. Third-party risk: about 210 vendors have network or data access. Only CDA suppliers get a security review (engineering procurement under the CSP). Business IT vendors are reviewed only at onboarding, and 9 of 24 Tier 1 vendors have no current SOC 2 report or equivalent on file.
9. Security-Related Information handling: documents marked "Security-Related Information" were found on general engineering shares during P03 sampling. There is no data loss prevention, and EDMS restricted-folder access is reviewed once a year.
10. Legacy: the 2 clearance and tagging servers run Windows Server 2012 R2, which is out of vendor support; the application vendor supports only that version until the 2027 upgrade.
11. AI governance: none. The predictive maintenance pilot (AI-001) went in with a vendor gateway and no CST review (see gap 3). The applicant tracking vendor enabled an AI ranking feature by default (AI-004). Staff use public generative AI tools.
12. The generation data and settlement reporting service (GDSR) runs on informal controls: meter-data scripts change without change control, and the service has never been externally assured.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| Registry defaults | Kept. The primary system, the P08 incident, and the P10 use case all fit a single-unit station at this size |
| P03 regulation | Primary: 10 CFR 73.54, decomposed by paragraph, with the CSP controls benchmarked against RG 5.71 Rev. 1 Appendices B and C. Also analyzed: 73.77, 73.21-73.22, 73.56, 73.58, 73.55(m), NERC CIP-002-5.1a and CIP-003-9 (low impact), Fla. Stat. 501.171. Applicability decided for 73.110, CIRCIA, DOE-417, and SEC rules |
| P08 | **Two incident types:** (1) cyber attack on the plant business network with an attempted pivot to digital assets (`ir-runbook.md`); (2) insider compromise of security-related information and Safeguards Information (`ir-runbook-insider-information-compromise.md`). Both integrate the crisis management team, legal, and the Shift Manager's NRC notifications |
| P09 | Readiness for a SOC 2 Type 2 examination of the generation data and settlement reporting service required by PPA-2 (Security, Availability, Processing Integrity, Confidentiality); plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio of 5 (AI-001 to AI-005), with a full assessment of AI-001 predictive maintenance for non-safety plant equipment |
| Cloud | Multi-account landing zone, vendor-agnostic. No Safeguards Information and no CDA data paths in the cloud |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (Station walkthrough 2026-07-21 to 2026-07-23) |
| 2026-08-03 to 2026-08-21 | Control assessment fieldwork (co-sourced internal audit firm with Nuclear Oversight) |
| 2026-09-17 | Deliverables approved by the Site Vice President (High risks and the appetite by the CEO); results presented to the audit committee |

## 7. Facts added during the build (fictional; used across P01-P10)

| Topic | Added fact |
|---|---|
| Revenue per day | Online: about $1.23 million per day. During a refueling outage, each day of extension costs about $1.23 million of lost generation plus about $0.8 million of contractor standby cost |
| Cyber insurance | $25 million aggregate limit, $1 million retention. Panel breach counsel and forensics; notice through the carrier hotline before incident vendors are engaged |
| Users and accounts | About 1,150 active business network accounts outside an outage, rising to about 2,150 during an outage. 96 terminations and 58 transfers in the 12 months to 2026-06-30. Last access review: January 2026 |
| Backups | Daily backups of on-premises servers and cloud workloads to the recovery account: 35-day write-once retention, separate administrator credentials |
| MSSP | Call to the IT Security Manager within 30 minutes of a high-severity alert |
| GDSR service | Hourly net generation and clean energy attribute data to the PPA-2 buyer by 10:00 each day for the prior day; monthly settlement statements to both buyers |
| Terminology | "Plant Business Network and Work Management System (PBN-WMS)" is the SSP system, identifier CSC-PBN-01. "Level 2" means the business network side of the CSP defensive architecture |
| Security organization | A Security Operations Manager reports to the Director of Security and is the backup incident lead for the insider runbook (P08) |
| GDSR data and team | Hourly net generation comes from settlement-quality revenue meter data downloaded daily from the interconnecting transmission owner's meter data portal (no connection between the dispatch network and GDSR); historian replica data (SYS-09) is used for validation and estimates. Run by the Energy Marketing and Settlements Manager, 3 settlements analysts, and 2 IT application developers |
| SOC 2 timeline | The PPA-2 buyer accepted in writing (2026-09-10): interim Type 1 report as of 2027-03-31; first Type 2 period 2027-04-01 to 2027-12-31 with the report by 2028-03-15; calendar-year periods after that. The service auditor is an independent CPA firm other than the co-sourced internal audit firm |
| AI tools | AI-001 pilot since 2026-02-02 on 38 balance-of-plant assets; AI-003 is an optional module of the CAP software running on the company's CAP server; AI-004 ranking was enabled by the vendor by default in 2026-03; the AI review group meets monthly from 2026-10-06 |
