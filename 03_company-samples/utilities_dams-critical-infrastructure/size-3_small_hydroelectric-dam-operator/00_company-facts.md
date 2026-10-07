# Scenario facts: Cris Santos Company | Dams | Small

All 10 deliverables in this folder use the facts below. The company, the hydroelectric project, the river, and the downstream community are fictitious. Where a fact comes from a regulation or a FERC program document, the citation is given. Regulatory text was checked on 2026-09-26 against eCFR (version date 2026-09-23), the FERC Security Program for Hydropower Projects Revision 3A PDF on ferc.gov, FERC's Revision 3/3A change notice and FAQ on ferc.gov, and the NERC Bulk Electric System Definition Reference Document (version 3, April 30, 2026).

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner) |
| Business | Owner and operator of a small hydroelectric project with a regulated dam (NAICS 221111, Hydroelectric Power Generation) |
| The project | **Cypress Fork Hydroelectric Project** (fictional), a FERC-licensed project on the fictional Cypress Fork River in north Florida. Hydropower is rare in Florida; this project is invented for the sample and does not describe any real dam |
| Project works | A 48-foot earthen embankment dam about 4,200 feet long; a concrete gated spillway with 4 radial (Tainter) gates; a powerhouse with 3 Kaplan units of 10 MW each (30 MW total; gross nameplate about 11 MVA per unit); the Cypress Fork Reservoir (about 11,500 acres at normal pool); a 69 kV switchyard. No black start capability |
| Location | Florida. Everything is on one site: powerhouse and control room, administration building, field services shop, and the recreation facilities around the reservoir (2 campgrounds, a marina, 6 boat ramps, 3 day-use areas) |
| License history (fictional) | Dam completed 1962; current FERC license issued 2004 to a prior licensee; license transferred to Cris Santos Company in 2019 with FERC approval |
| Hazard potential | **High** (18 CFR 12.3(b)(13)(i)): a town of about 2,400 residents lies 2 to 4 miles downstream, inside the Emergency Action Plan (EAP) inundation zone |
| FERC Security Group | **Security Group 2**, per FERC's January 2010 regrouping letter to the prior licensee, confirmed by the FERC engineer at the 2025-10-21 inspection. Group criteria are not public (Security Program Rev. 3A, 3.3.2) |
| Offtaker | A regional electric cooperative buys all energy and capacity under a long-term contract and receives unit telemetry through a remote terminal unit (RTU) at the switchyard |
| Grid status | Interconnected at 69 kV. Not part of the Bulk Electric System under NERC inclusion I2 (units are not over 20 MVA, the plant is not over 75 MVA, and the connection is below 100 kV) and not a blackstart resource. The company is not on the NERC Compliance Registry, so NERC CIP does not apply (see P03) |
| Workforce | **187 employees:** 33 generation operations (1 Plant Manager, 3 Operations Supervisors, 12 control room operators, 14 mechanics and electricians, 1 Controls Engineer, 2 instrumentation and control technicians); 17 dam safety and civil maintenance (Chief Dam Safety Engineer, 4 dam safety technicians, 12 civil and grounds crew); 36 hydro field services; 62 recreation and lands (including 22 seasonal); 6 environmental and license compliance; 7 security (Compliance and Security Coordinator plus 6 site security officers); 26 corporate (3 executives, 6 finance, 4 HR, 4 IT, 7 administration and procurement, 2 community relations) |
| Revenue | $21.8 million a year (fictional): energy and capacity sales $12.6M, renewable energy credits $1.2M, hydro field services $4.4M, recreation fees $3.1M, other (leases, timber) $0.5M. Hydroelectric generation is 63% of receipts, so NAICS 221111 is the primary industry. Under the SBA size standard of 750 employees for NAICS 221111 (13 CFR 121.201), the company is SBA-small |
| Hydro field services | Crews service spillway gates, hoists, trashracks, and stop logs for other dam owners in the Southeast. The work is mechanical and on-site. The company does not host, process, or remotely access customer systems or data |
| Federal contracts | None. FAR 52.204-21 and 52.204-25 do not apply |
| Sensitive data | Critical energy infrastructure information (CEII, 18 CFR 388.113(c)(2)): design drawings, EAP inundation maps, spillway and unit control details. Security-sensitive documents marked "Privileged - Security Sensitive Material" per Security Program Rev. 3A 3.4.3.4 and 8.0: Security Assessment, Security Plan, and annual certification letters. Dam safety instrumentation data. Employee personal information (Florida breach law applies). Recreation customers pay through the reservation vendor's hosted payment page, so the company stores no card data. No PCII has been submitted. No BES Cyber System Information exists (not a BES facility) |
| Not in scope | NERC CIP (not BES, not registered). NISPOM, CMMC, HIPAA (no such data). CIRCIA reporting: the final rule is not published (proposed only), and the company is below the SBA size standard used in the proposed scope |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (majority owner) | Accepts High and Very High risks; approves the budget |
| Vice President of Operations | Executive owner of the security program; accepts Moderate risks; signs policies; signs the Annual Security Compliance Certification Letter with the Chief Dam Safety Engineer |
| Chief Dam Safety Engineer | Licensed professional engineer designated under 18 CFR 12.61(a); owns the Owner's Dam Safety Program, EAP, instrumentation, and 18 CFR 12.10 reports; business owner of the AI anomaly detection pilot (P10) |
| Plant Manager | System owner of the Plant Control and Dam Monitoring System (P02); owns the control room, unit and gate operations, and the rapid-recovery actions |
| Compliance and Security Coordinator | **FERC primary security contact** (Security Program Rev. 3A, 3.2); physical security, site security officers, key control, Security Assessment and Security Plan upkeep, suspicious activity reporting |
| Operations Supervisors (3) | Shift leads; alternate FERC security contacts; incident commander on shift for OT incidents until the Plant Manager arrives |
| IT Manager | Security program lead for IT; runs the identity provider, cloud tenant, corporate network, and endpoints; maintains the risk register; incident commander for IT incidents |
| Controls Engineer | Administers the OT network, SCADA, PLCs, historian, and OT firewall with 2 instrumentation and control technicians; OT cyber lead |
| Environmental and License Compliance Manager | License articles, recreation restrictions (Security Program Rev. 3A, 3.3.4), FERC correspondence |
| HR Manager | Screening, onboarding, terminations, training records |
| Controller | Finance, ERP, cyber insurance policy holder, offtaker settlements |
| Managed service provider (MSP) | After-hours help desk and patching for **corporate IT only**. No OT access |
| SCADA integrator and governor/excitation vendor | Remote support for OT through always-on connections (gap 5) |
| Independent assessor | Contracted for the P07 control assessment; not involved in operating controls |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | SCADA and HMI: 2 redundant SCADA servers, 3 operator HMI workstations, 1 engineering workstation | On-premises OT (control room) | Controls gates and units. **HMI servers run an operating system past vendor support; the engineering workstation is dual-homed to the corporate network** |
| SYS-02 | Spillway gate control: 1 gate PLC, 4 local gate control panels, hoist motors, standby diesel generator | On-premises OT (spillway) | Gates can be operated from the HMI (local or remote) or from each local panel. Annual gate operation and standby power load tests are done (18 CFR 12.54) |
| SYS-03 | Unit control: 3 unit PLCs, 3 digital governors, 3 excitation systems | On-premises OT (powerhouse) | Governors and exciters are maintained by the OEM vendor through remote access |
| SYS-04 | Dam safety instrumentation and early warning: automated data acquisition for 64 instruments (piezometers, seepage weirs, reservoir and tailwater levels), 2 upstream river gauges on cellular modems, downstream warning sirens | On-premises OT plus field devices | Sirens are activated from the control room under the EAP |
| SYS-05 | OT network: control LAN, OT firewall, DMZ with a historian replica, OT historian, OT backup NAS | On-premises OT | One flat control LAN for the dam and powerhouse (one cyber system for Section 9 purposes) |
| SYS-06 | Remote access paths | OT firewall VPN; vendor connections | (a) After-hours remote operation by on-call operators since March 2024: a separate OT VPN profile with local passwords (no MFA), then a **shared operator account** on the HMI; (b) always-on vendor connections for the SCADA integrator and the governor/excitation vendor |
| SYS-07 | Corporate network and endpoints | On-premises | 150 laptops and desktops, 40 tablets (recreation and field crews), corporate firewall and Wi-Fi; EDR on corporate endpoints |
| SYS-08 | Identity provider (single sign-on and MFA) | SaaS | MFA for all corporate users; not used by OT |
| SYS-09 | Productivity suite (email, files, chat) | SaaS | **CEII and security documents sit in general file shares** (gap 13) |
| SYS-10 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Historian reporting replica and dashboards (VM plus managed database), backup vault for corporate servers, log workspace (created, not yet used for OT) |
| SYS-11 | Dam safety instrumentation data platform with an AI anomaly detection module | Vendor SaaS | Receives instrument data one-way from the DMZ historian replica. The AI module has run in "shadow mode" since April 2026 (P10). The vendor has a SOC 2 Type 2 report (P09) |
| SYS-12 | Business applications | Vendor SaaS | ERP and maintenance management, payroll and HR, recreation reservations (vendor-hosted payments) |
| SYS-13 | Offtaker telemetry | RTU at switchyard; leased circuit | Unit status and MW output to the cooperative's control center; dispatch schedules by email and portal |

**SSP system (P02):** the *Plant Control and Dam Monitoring System (PCDMS)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, and SYS-06, with their interfaces to SYS-10, SYS-11, and SYS-13, plus the control room, spillway, powerhouse, and instrument locations that house them.

## 4. Current security posture: partially compliant

**In place today:**
- EAP filed with the Regional Engineer, reviewed annually, with an annual readiness test of key staff (18 CFR 12.24(d), 12.25(b)); downstream sirens tested monthly
- Owner's Dam Safety Program filed; Chief Dam Safety Engineer designated (18 CFR 12.60 to 12.64)
- Annual spillway gate operation and standby power load test (18 CFR 12.54)
- Security Assessment (Group 2) dated June 2017, prepared by the prior licensee; annual update inserts through 2022
- Site Security Plan (physical) covering restricted areas, key control, threat-level procedures, and communications; last updated 2022
- Annual Security Compliance Certification Letters filed by December 31 each year since 2019
- Perimeter fencing, locked gates, card access to the powerhouse and control room, cameras at the spillway and powerhouse monitored from the control room, night patrols by site security officers
- Law enforcement and county emergency management numbers posted in the control room; annual meeting with the county sheriff
- A firewall between the corporate network and the OT network, with a DMZ historian replica
- MFA for corporate email, the identity provider, and the cloud console; EDR on corporate endpoints
- Daily backups of corporate servers to the cloud backup vault
- Annual security awareness training for corporate users
- Background checks at hire for operators, security officers, and IT staff

**Missing or weak, found in the 2026 assessments:**
1. The Security Plan was last updated in 2022 and has no Information Technology/SCADA section; there is no separate Cyber/SCADA Security Plan (Security Program Rev. 3A, 3.3.2, 7.2, 7.5; Form 3 Q7a-7b).
2. Security Assessment annual updates lapsed after 2022, and the 2017 assessment does not cover the March 2024 remote-operation change. The December 2025 certification letter stated the Security Assessment and Security Plan were current and did not address Section 9 (6.4, 8.0).
3. No Section 9 determination (Form 3 Q1-4, Table 9.1c) and no OT cyber asset inventory or criticality designation (9.1.1, 9.2; Form 3 Q9a-9b, Q19a).
4. After-hours remote operation uses an OT VPN profile with passwords only and a shared HMI operator account (Table 9.3a and 9.3b access control; Form 3 Q18g-18h, Q21).
5. The SCADA integrator and the governor/excitation vendor have always-on remote connections; their activity is not logged or reviewed (Form 3 Q12a-12c).
6. IT/OT segregation is weak: the engineering workstation is dual-homed, and the OT firewall has broad rules from the corporate network (Table 9.3a; Form 3 Q11a-11b, Q22).
7. No logging, monitoring, or anomaly detection inside the OT network (Table 9.3a intrusion detection; Form 3 Q14a-14c).
8. No OT vulnerability assessment has ever been done; there is no OT patch or configuration management, and the HMI servers run an unsupported operating system (Table 9.3a system lifecycle, Table 9.3b vulnerability assessment; Form 3 Q15, Q18i).
9. PLC logic and HMI configurations are backed up irregularly to a NAS on the same OT network and have never been restore-tested; there is no documented OT recovery procedure (Table 9.3a restoration and recovery; Form 3 Q16).
10. No cyber incident response procedure for OT; the Internal Emergency Response sub-element does not connect a cyber event to the EAP or to 18 CFR 12.10 reporting; no cyber exercise has been held (7.4.1; Form 3 Q25-28).
11. Security training covers corporate users only; operators and OT support staff get no role-based control system security training (Table 9.3a training; 3.2).
12. No removable media policy; technicians move files to OT devices with USB drives (Form 3 Q17).
13. CEII and security-sensitive documents (inundation maps, drawings, the Security Assessment) are stored in general file shares open to all staff, including seasonal recreation staff (18 CFR 388.113; Form 1 Q22; 3.2 OPSEC).
14. The risk approach does not address cyber supply chain or insider threat; the annual threat assessment is not coordinated with law enforcement in writing; the company is not a member of the HSIN Dams portal (Form 3 Q23, Q32a-32b, Q33a-33b; 4.2).
15. Manufacturer default passwords on the web interfaces of 2 spillway gate local panels and on the 2 cellular modems of the upstream river gauges (found during P07 testing, 2026-08-05).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FERC Security Program for Hydropower Projects, Revision 3A (March 30, 2016), as applied to a Security Group 2 dam, fetched from ferc.gov on 2026-09-26. No newer revision could be confirmed (ferc.gov program page returned 403 to automated fetch). Secondary: 18 CFR Part 12 incident reporting (12.10) and related Part 12 duties. NERC CIP recorded as not applicable |
| P08 incident | Unauthorized access to spillway and turbine control systems through the password-only OT VPN and the shared HMI account |
| P09 SOC 2 | The company is not a service organization for its customers (field services are on-site mechanical work). Part A is a Security-only self-benchmark against the Trust Services Criteria; Part B reviews the instrumentation data platform vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: dam-safety sensor anomaly detection in the instrumentation data platform (shadow-mode pilot). AI-002: staff use of generative AI assistants near CEII |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents only where needed |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2017-06-15 | Security Assessment (Group 2) completed by the prior licensee |
| 2022-11-30 | Last Security Assessment update insert and last Security Plan update |
| 2024-03-01 | After-hours remote operation by on-call operators enabled |
| 2025-10-21 | FERC dam safety inspection; the FERC engineer asked for Form 3 (Questions 1-4) and the cyber/SCADA plan |
| 2025-12-18 | Annual Security Compliance Certification Letter filed (gap 2) |
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork, including the Section 9 determination |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (independent assessor; site walkthrough 2026-08-05) |
| 2026-08-31 | Deliverables approved by the Vice President of Operations; High risks and budget approved by the President |
| 2026-09-30 | Plan and schedule for Form 3 negative responses sent to the FERC Regional Engineer, with a corrected statement on the 2025 certification letter |
| 2026-11-17 | Next FERC dam safety inspection (security portion included) |
| 2026-12-31 | 2026 Annual Security Compliance Certification Letter due (Security Program Rev. 3A, 8.0) |

## 7. Facts added while completing the deliverables (fictional)

| Fact | Used in |
|---|---|
| Additional role titles: Field Services Manager and Recreation and Lands Manager (process owners) | P05 |
| About $59,700 of revenue per day ($21.8 million over 365 days); generation about $37,800 per day; field services about $17,600 per working day | P05 |
| Remediation budget of $265,000 for 2026 Q4 to 2027 Q2, approved by the President on 2026-08-31; about $24,600 of related costs (training, kiosk, retainer, outside review, carrier fee) come from the 2027 operating budget | P01, P07 |
| Section 9 determination on 2026-07-16: Form 3 Q1-3 Yes, Q4 No; the gate release scenario exceeds the Table 9.1c threshold of more than 60 people within 3 miles; the whole PCDMS is treated as Critical | P02, P03 |
| An upstream county-owned water control structure is the only other dam in the basin; no contact procedure exists yet | P03, P08 |
| A 2023 gate hoist failure was reported under 18 CFR 12.10 with a written report; in 2025 operators isolated the OT network and ran gates locally during a SCADA server failure | P03, P07 |
| Instrumentation monitoring plan (rev. 2025-03) defines trigger points for all 64 instruments; annual sheriff meeting held 2026-02-10 | P03 |
| Corporate server backups are restore-tested quarterly; immutable retention is not yet enabled | P03, P04 |
| SCADA event journal keeps 90 days; SCADA locks accounts after 5 failed sign-ins; SCADA passwords require 12 characters | P02, P07 |
| Interim control from 2026-09-15: after-hours remote HMI access is view-only; gate and unit commands only from the control room or local panels | P02, P07, P08 |
| P07 test details: 1,412 gate and unit commands in July 2026 attributed to the shared account; last PLC and HMI backup 2026-04-11 and 2 governor configurations never backed up; 11 of 38 control network devices missing from the 2018 drawings; a test laptop on the control LAN undetected for 2 hours; 3 unlabeled USB drives in the control room; 3 of 8 staff interviewed unaware of cyber reporting; 2 of 4 gate enclosure keys not in the key register | P07 |
| Instrumentation vendor SOC 2 Type 2: period ending 2026-03-31, unqualified, 1 exception; RTO 8 hours, RPO 1 hour; AI module released after the period | P09 |
| AI-001 pilot results: back-test detected 21 of 23 historical events (open-standpipe piezometers 4 of 6); 214 shadow-mode alerts from 2026-04-01 to 2026-08-15, 9 confirmed; wet-season false alarms 1.9 a day vs 0.6 in the dry season. Staff briefed on generative AI rules on 2026-08-28 | P10 |
