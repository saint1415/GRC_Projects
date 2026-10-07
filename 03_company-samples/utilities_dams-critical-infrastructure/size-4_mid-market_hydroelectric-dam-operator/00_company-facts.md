# Scenario facts: Cris Santos Company | Dams | Mid-Market

All 10 deliverables in this folder use the facts below. The company, its four hydroelectric projects, the rivers, the client projects, and the downstream communities are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a NERC Reliability Standard, or a FERC program document, the citation is given. Regulatory text was checked on 2026-10-05 against eCFR (version date 2026-09-23), the FERC Security Program for Hydropower Projects Revision 3A PDF and FAQ on ferc.gov, the NERC Bulk Electric System Definition Reference Document (version 3, April 30, 2026), the NERC Glossary of Terms web page, and the NERC standard PDFs for CIP-002-5.1a, CIP-003-9, CIP-012-2, and EOP-004-4.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | Owner and operator of 4 FERC-licensed hydroelectric projects (NAICS 221111, Hydroelectric Power Generation), with a second business line, **Hydro Services**: field services for other dam owners and contract **Remote Monitoring and Operations Services (RMOS)** for small hydro projects owned by other licensees |
| Location | Florida. Headquarters campus in north Florida with the **Remote Operations Center (ROC)**, the corporate data room, and the security operations desk. All 4 projects are on fictional rivers in north Florida. Hydropower at this scale does not exist in Florida; the projects are invented for the sample and do not describe any real dam |
| Projects | See the project table below. 300 MW installed in total, 20 spillway gates, 12 generating units |
| Remote operation | The ROC is staffed 24x7 and supervises and controls all 4 projects. A backup ROC sits in the Cedar Shoals powerhouse control room. Blackwater Bend is also staffed on site 24x7; Cedar Shoals and Pine Hollow are staffed on day shift; Sawgrass Run is unstaffed and visited by a roving operator |
| Offtakers | A regional investor-owned utility buys the output of Blackwater Bend and Cedar Shoals under a long-term power purchase agreement (PPA). That utility is also the Balancing Authority (BA) and Transmission Operator (TOP) for both plants, and the ROC exchanges real-time data with its control center over an encrypted inter-control-center link (ICCP) on a leased circuit. An electric cooperative buys the output of Pine Hollow and Sawgrass Run |
| NERC registration | Registered on the NERC Compliance Registry as a **Generator Owner (GO) and Generator Operator (GOP)** because Blackwater Bend and Cedar Shoals are Bulk Electric System (BES) generating resources under Inclusion I2 (units over 20 MVA gross nameplate, or a plant over 75 MVA, connected at 100 kV or above). Pine Hollow (69 kV) and Sawgrass Run (69 kV) are not BES. The ROC monitors and controls BES generation at two locations, so it meets the NERC Glossary definition of a GOP **Control Center**. All BES Cyber Systems are **low impact** (CIP-002-5.1a Attachment 1 criteria 3.1 and 3.3): aggregate BES generation of 264 MW is far below the 1,500 MW lines in criteria 2.1 and 2.11, no Planning Coordinator or Transmission Planner has designated either plant under criterion 2.3, and neither plant is a Blackstart Resource |
| Workforce | **850 employees:** 270 generation operations (ROC 36; plant operations and maintenance 210; controls engineering and I&C 24); 64 dam safety and civil; 248 Hydro Services (field services 226; RMOS desk and client support 22); 104 recreation and lands (including 38 seasonal); 18 environmental and license compliance; 42 corporate security; 37 IT, OT security, GRC, NERC compliance, and data analytics; 67 corporate (7 executives, 18 finance, 12 HR, 4 legal, 14 procurement and supply chain, 4 communications and community relations, 8 administration) |
| Revenue | **$186.0 million a year** (fictional): energy and capacity sales $128.0M; renewable energy credits $7.5M; Hydro Services $41.0M (field services $29.5M, RMOS $11.5M); recreation $6.0M; other (leases, timber, a raw-water supply contract at Cedar Shoals) $3.5M. Generation is 73% of receipts, so NAICS 221111 is the primary industry. With 850 employees the company exceeds the SBA size standard of 750 employees for NAICS 221111 (13 CFR 121.201), so it is **not SBA-small** |
| RMOS | The ROC monitors 6 small hydro projects (45 MW in total) owned by 4 client companies, all FERC licensees, and operates units and gates at 4 of them under written operating orders. Client site gateways connect to the ROC over site-to-site VPN tunnels. Clients see dashboards, alarms, and monthly operations and dam safety instrument reports in the **RMOS client portal** (cloud). Clients remain the licensees responsible for their own dams. Client contracts renewing in 2027 require a **SOC 2 Type 2** report (P09) |
| Field services | Crews service spillway gates, hoists, trashracks, governors, and turbines for other dam owners in the Southeast. On-site mechanical and electrical work; crews carry company laptops that connect to client equipment only under the client's supervision |
| Federal contracts | None. FAR 52.204-21, 52.204-23, and 52.204-25 do not apply |
| Sensitive data | CEII (18 CFR 388.113(c)(2)): design drawings, EAP inundation maps, gate and unit control details, network diagrams. Security-sensitive documents marked "Privileged - Security Sensitive Material" (Security Program Rev. 3A 8.0): the Blackwater Bend Vulnerability Assessment, Security Assessments, Security Plans, Section 9 determinations, and certification letters. BES Cyber System Information for the low impact BES Cyber Systems (protected as CEII; CIP-011 does not apply at low impact). RMOS client data: client control details, instrument data, and inundation maps, held under confidentiality terms. Employee personal information (Florida breach law applies). Recreation customers pay through the reservation vendor's hosted payment page, so the company stores no card data. No PCII has been submitted |
| Not in scope | NERC CIP-004 to CIP-011, CIP-013, and CIP-015 (they apply to high and medium impact BES Cyber Systems; the company has none). CIP-014 (applies to Transmission Owners). HIPAA, NISPOM, CMMC, PCI DSS assessment (no such data or contracts). SEC cyber disclosure rules (privately held). CIRCIA reporting: the final rule is not published (proposed only); see P03 |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). A few field services and Pine Hollow staff live in Georgia and Alabama, so breach notices would also follow the law of each state where affected individuals reside, with Florida as the worked example |

**The four projects (fictional)**

| Project | Dam and works | Units | Interconnection and BES | Hazard potential (18 CFR 12.3(b)(13)) | FERC Security Group | Staffing |
|---|---|---|---|---|---|---|
| **Blackwater Bend (BWB)** | 118-foot concrete gravity dam with earthen wing dikes; gated spillway with 8 radial gates; reservoir of about 31,000 acres | 4 Francis units of 45 MW (about 50 MVA gross nameplate each); 180 MW | 230 kV switchyard; **BES** | High: a city of about 38,000 lies 2 to 9 miles downstream inside the EAP inundation zone | **Group 1** | 24x7 on site plus ROC |
| **Cedar Shoals (CDS)** | Earth embankment dam with a concrete spillway and 5 Tainter gates, 22 river miles below Blackwater Bend; hosts the backup ROC; supplies raw water to a county water plant intake in the reservoir | 2 Kaplan units of 42 MW (about 46 MVA each); 84 MW | 115 kV; **BES** | High: two towns of about 6,500 combined lie downstream | **Group 2** | Day shift plus ROC |
| **Pine Hollow (PNH)** | 61-foot earthen dam with 4 spillway gates on a second river | 3 Kaplan units of 8 MW; 24 MW | 69 kV; not BES | High: a rural community of about 1,100 lies 1 to 3 miles downstream | **Group 2** | Day shift plus ROC |
| **Sawgrass Run (SGR)** | Low run-of-river dam with 3 crest gates on a third river | 3 units of 4 MW; 12 MW | 69 kV; not BES | Significant | **Group 3** | Unstaffed; roving operator; ROC |

FERC assigned the Security Groups (letters to the company in 2019 after the acquisition of Pine Hollow and Sawgrass Run; confirmed at the 2025-11-04 inspection). Group criteria are not public (Security Program Rev. 3A 3.3.1 to 3.3.3).

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting from the vCISO; oversees the co-sourced internal audit firm |
| Chief Executive Officer | Accepts High risks (temporarily, with a dated plan); approves the risk appetite and the security budget |
| Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risks; **CIP Senior Manager** (CIP-003-9 R3); approves policies; authorizing official equivalent for the HCDMS |
| General Counsel | Legal lead for incidents, regulator correspondence, and breach decisions; the NERC Compliance Manager reports here so compliance is independent of operations |
| Chief Financial Officer | Cyber insurance policy holder; finance and energy settlements |
| Vice President of Generation Operations | **System owner** of the Hydro Control and Dam Monitoring System (P02); owns the ROC, the 4 plants, and controls engineering |
| Vice President of Hydro Services | Owner of field services and RMOS; SOC 2 service owner (P09) |
| Chief Dam Safety Engineer | Licensed professional engineer designated under 18 CFR 12.61(a) and 12.62(a); owns the Owner's Dam Safety Program, the 4 EAPs, instrumentation, and 18 CFR 12.10 reports; signs the Annual Security Compliance Certification Letter; business owner of AI-001 (P10) |
| Corporate Security Manager | **FERC primary security contact** (Rev. 3A 3.2); Vulnerability Assessment, Security Assessments, Security Plans; site security officers; security operations desk |
| vCISO (part-time contractor) | Program strategy, risk register owner, board reporting |
| IT Director | IT security lead: identity provider, cloud landing zone, corporate network, endpoints; incident commander for IT incidents |
| OT Security Manager (with 3 OT security engineers) | OT cyber lead: Section 9 measures, CIP-003-9 low impact plan implementation, OT jump hosts, OT monitoring, OT vulnerability management |
| Manager of Controls Engineering | SCADA, PLC, governor, and historian engineering; OT change management; OT backups |
| ROC Manager and 6 ROC shift supervisors | ROC operations; the ROC shift supervisor is incident commander on shift for OT incidents until the Vice President of Generation Operations takes over |
| Plant Managers (4) | Plant operations and local control at each project |
| GRC Manager (with 2 GRC analysts) | Policies and standards, gap analysis, POA&M, vendor risk program, SOC 2 readiness |
| NERC Compliance Manager (with 1 analyst) | CIP-002, CIP-003, CIP-012, and EOP-004 compliance; Regional Entity correspondence |
| Environmental and License Compliance Manager | License articles, recreation restrictions (Rev. 3A 3.3.4), FERC filings |
| Data Analytics Lead (with 2 data scientists) | Builds and runs AI-001 and AI-002 (P10) |
| HR Director | Screening, onboarding, terminations, training records |
| Co-sourced internal audit firm | Annual IT audit; performed the P07 control assessment; reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 monitoring of the SIEM and of OT sensor alerts from the ROC and Blackwater Bend |
| OT vendors | SCADA platform vendor (also the integrator), governor and excitation OEM for Blackwater Bend and Cedar Shoals, governor OEM for Pine Hollow, turbine controls OEM for Sawgrass Run, instrumentation hardware vendor |

**Where roles overlap.** The vCISO is part-time, so day-to-day OT security decisions sit with the OT Security Manager, who reports to the Vice President of Generation Operations (the system owner). That is a do-and-check overlap. It is compensated by the co-sourced internal audit firm's independent assessment (P07), the NERC Compliance Manager's separate reporting line to the General Counsel, and the vCISO's direct reporting to the audit committee.

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | ROC SCADA: redundant SCADA servers (primary at the ROC, standby at the backup ROC), 12 operator consoles at the ROC and 4 at the backup ROC, 3 engineering workstations, OT historian, ICCP server for the BA/TOP link | On-premises OT (ROC and backup ROC) | Supervises and controls all 4 projects and the RMOS client sites. Named operator accounts |
| SYS-02 | Plant control: 12 unit PLCs, 12 digital governors, 12 excitation systems, local plant HMIs | On-premises OT (4 powerhouses) | **Plant HMIs at Pine Hollow and Sawgrass Run use shared operator accounts; 9 of 29 Windows-based OT hosts at those two plants run unsupported operating systems** |
| SYS-03 | Spillway gate control: gate PLCs and 20 local gate panels, hoists, standby generators | On-premises OT (4 spillways) | Gates can be operated from the ROC, the plant HMI, or the local panel. Annual gate operation and standby power tests (18 CFR 12.54) |
| SYS-04 | Dam safety instrumentation and early warning: automated data acquisition for 410 instruments, 9 upstream river gauges (cellular), downstream sirens (14 at BWB, 6 at CDS, 3 at PNH) | On-premises OT plus field devices | Sirens are activated from the ROC or locally under each EAP |
| SYS-05 | OT wide-area network and site networks: private fiber and licensed microwave between the ROC and the projects; OT firewall at each site; OT DMZ at the ROC with historian replica, jump hosts, and patch server; OT backup server | On-premises OT | **The OT WAN is routed flat between sites: a host at any plant can reach controllers at the others; RMOS client tunnels terminate in the same ROC SCADA zone** |
| SYS-06 | Remote access: OT jump hosts with MFA (since 2025) for staff and most vendors; RMOS client site-to-site VPN tunnels | OT DMZ | **Two OEM vendors (Pine Hollow governors, Sawgrass Run turbine controls) keep always-on direct VPN connections to plant OT firewalls that bypass the jump hosts** |
| SYS-07 | OT security monitoring: passive OT network sensors and log collection | ROC and BWB only (since 2025); alerts to the MSSP | **No OT monitoring at CDS, PNH, or SGR** |
| SYS-08 | Corporate network and endpoints: 780 laptops and desktops, 160 tablets; EDR on all managed endpoints | On-premises and remote | Field services crews use company laptops at client sites |
| SYS-09 | Identity provider with SSO, MFA, and conditional access | SaaS | All corporate users; also the MFA source for the OT jump hosts |
| SYS-10 | Productivity suite (email, files, chat) | SaaS | **EAP inundation maps and design drawings sit in engineering shares open to about 400 users** |
| SYS-11 | Cloud landing zone: 6 accounts (management and identity; security tooling and log archive; network hub; OT data and analytics; Hydro Services client portal; backup) | Public cloud (vendor-agnostic) | See P04 |
| SYS-12 | Business applications | Vendor SaaS | ERP and enterprise asset management (EAM), HR and payroll, energy scheduling and settlement, recreation reservations (vendor-hosted payments) |
| SYS-13 | SIEM operated by the MSSP | SaaS | Identity provider, cloud, corporate firewall, EDR, and OT sensor alerts (ROC and BWB) |
| SYS-14 | Dam safety data platform: instrument data lake, dashboards, and the in-house AI models (AI-001, AI-002) | Cloud, OT data and analytics account | Receives data one-way from the OT DMZ historian replica |
| SYS-15 | RMOS client portal | Cloud, Hydro Services account | Client dashboards, alarm history, monthly reports; client users sign in through the company identity provider as guests |
| SYS-16 | Physical security systems: cameras, card access, intrusion detection at all 4 projects and the ROC, monitored by the security operations desk | Separate security network | Video analytics (AI-003) on 64 cameras at BWB and CDS |

**SSP system (P02):** the *Hydro Control and Dam Monitoring System (HCDMS)*: SYS-01 to SYS-07 at the ROC, the backup ROC, and the 4 projects, with their interfaces to SYS-11, SYS-14, SYS-15, the RMOS client sites, and the BA/TOP control center.

## 4. Current security posture: a defined program with gaps in scale

**In place today:**
- Information security policies adopted in 2024 (written mainly for IT); a CIP-003 low impact cyber security plan covering the ROC, Blackwater Bend, and Cedar Shoals, reviewed and approved by the CIP Senior Manager within 15 calendar months
- CIP-002 identifications reviewed and approved within 15 calendar months (last 2026-02-10)
- FERC documents for every Group 1 and 2 dam: the Blackwater Bend Vulnerability Assessment (reprinted 2022-06-30, updated each year), Security Assessments for Cedar Shoals and Pine Hollow, Security Plans with an Internal Emergency Response sub-element for all three and a Rapid Recovery sub-element for Blackwater Bend; Annual Security Compliance Certification Letters filed by December 31 each year
- Section 9 determinations completed in May 2023 for Blackwater Bend, Cedar Shoals, and Pine Hollow
- EAPs for the 3 high hazard dams and Sawgrass Run, reviewed annually with annual readiness tests (18 CFR 12.24, 12.25); Owner's Dam Safety Program with a Chief Dam Safety Engineer (18 CFR 12.60 to 12.64); independent external audit of the Owner's Dam Safety Program in 2024 (12.65)
- 24x7 staffed ROC with named SCADA accounts; OT jump hosts with MFA for staff; OT firewalls at every site; an OT DMZ with a historian replica
- MFA for all corporate users; EDR on all managed endpoints and on ROC Windows servers; SIEM with 24x7 MSSP monitoring; passive OT monitoring at the ROC and Blackwater Bend
- Immutable corporate backups in a separate cloud backup account; PLC and HMI configurations backed up monthly to the OT backup server and quarterly to offline media; a restore test at Blackwater Bend in 2025
- Annual OT vulnerability assessment by an outside firm at the ROC and Blackwater Bend (last 2025-10)
- Annual awareness training; quarterly CIP-003 security awareness reinforcement; role-based OT security training for ROC operators
- Cyber security incident response plan (2024) tested by a tabletop on 2024-09-18 (CIP-003-9 Attachment 1 Section 4.5)
- Annual internal IT audit by the co-sourced firm since 2024; cyber insurance with a $15 million limit

**Gaps, found in the 2026 assessments:**
1. The Section 9 determinations were not re-evaluated in 2024 or 2025 as Table 9.3a requires (at least every 12 months), and they omit the RMOS client interconnections and the Sawgrass Run (Group 3) interconnection to the ROC (Rev. 3A 9.1, 9.1.1.2 note; FAQ Q10). The OT asset inventory is complete only for the ROC and Blackwater Bend (Rev. 3A 9.2).
2. The OT WAN is routed flat between projects, and RMOS client tunnels terminate in the same ROC SCADA zone that controls company gates (Table 9.3a access control and functional segregation; Form 3 Q11, Q22).
3. Two OEM vendors keep always-on direct VPN connections to the Pine Hollow and Sawgrass Run OT firewalls, outside the jump hosts, with no session recording or weekly log review (Table 9.3a; Form 3 Q12). At the BES assets, vendor remote access goes through the jump hosts, but there is no method to detect malicious communications for vendor sessions at Cedar Shoals (CIP-003-9 Attachment 1 Section 6.3).
4. OT network monitoring covers only the ROC and Blackwater Bend; Cedar Shoals, Pine Hollow, and Sawgrass Run have none (Form 3 Q14).
5. OT vulnerability assessments have been done only at the ROC and Blackwater Bend, although Cedar Shoals and Pine Hollow are also Critical (Table 9.3b, not to exceed 12 months). There is no OT patch cadence, and 9 of 29 Windows-based OT hosts at Pine Hollow and Sawgrass Run run unsupported operating systems.
6. Shared operator accounts on the Pine Hollow and Sawgrass Run plant HMIs; OT account reviews are annual; privileged access management covers only the cloud.
7. OT recovery is proven only at Blackwater Bend: configuration backups for Cedar Shoals, Pine Hollow, and Sawgrass Run are incomplete, the governor settings for 5 units are held only by the OEMs, and the Blackwater Bend Rapid Recovery sub-element does not cover recovery of the ROC SCADA after a cyber attack (Rev. 3A 7.4.2; Table 9.3a).
8. The incident response plan does not link a cyber event on gates or units to the EAPs and 18 CFR 12.10, and there is no crisis management plan for a ransomware event that forces IT/OT separation.
9. Third-party risk: OT vendors are not tiered, 9 of 14 OT vendor contracts have no security terms, and RMOS client contracts do not define security responsibilities or incident notice. Clients have asked for a SOC 2 Type 2 report.
10. CEII: the restricted library holds the Vulnerability Assessment, Security Assessments, and Security Plans, but EAP inundation maps and design drawings sit in engineering shares open to about 400 users, and copies of drawings and instrument data in the cloud data lake are not classified (18 CFR 388.113; Form 1 Q22).
11. The CIP-012 plan for the ICCP link (written in 2022) does not identify methods for loss of availability and for recovery of the communication link, which CIP-012-2 R1 Parts 1.2 and 1.3 require from 2026-07-01.
12. AI: two in-house models (AI-001, AI-002) went into use without model validation, version control, or monitoring rules, and there is no AI policy or inventory.
13. Found during P07 testing (2026-08-12): an undocumented cellular modem in the Sawgrass Run gate PLC panel, installed by the turbine controls OEM in 2023 for remote diagnostics, with a default password.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 system | The Hydro Control and Dam Monitoring System (HCDMS). The registry default ("Hydro plant control and dam monitoring system") fits; at this size it spans a central ROC and 4 projects, so the name was adjusted |
| P03 regulation | FERC Security Program for Hydropower Projects, Revision 3A (March 30, 2016), applied to 1 Group 1, 2 Group 2, and 1 Group 3 dam, including Section 9 and Form 3. Also all other rules for the primary business line: 18 CFR Part 12 (incident reporting and related duties), NERC CIP-002-5.1a, CIP-003-9 (low impact), CIP-012-2, and EOP-004-4, with the not-applicable CIP standards recorded; CEII handling; Florida breach law for employee data |
| P08 incidents | Two incident types: (1) unauthorized access to spillway and turbine control systems (registry default), entering through an RMOS client tunnel or an OEM connection; (2) ransomware in corporate IT with theft of RMOS client data, which forces IT/OT separation. Both integrate crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the RMOS service (Security, Availability, Confidentiality, Processing Integrity), plus a vendor SOC 2 review program |
| P10 AI | Portfolio of 5: AI-001 dam-safety sensor anomaly detection (registry default, built in-house), AI-002 reservoir inflow forecasting, AI-003 perimeter video analytics, AI-004 turbine predictive maintenance, AI-005 enterprise generative AI assistant |
| Cloud | Multi-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents only in an equivalents table |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2016-06-01 | NERC registration as GO and GOP for Blackwater Bend and Cedar Shoals |
| 2019-05-15 | Pine Hollow and Sawgrass Run acquired; FERC Security Group letters issued |
| 2021-10-20 | Last Blackwater Bend Security Plan exercise (drill level) |
| 2022-06-30 | Blackwater Bend Vulnerability Assessment reprinted (5-year cycle, Rev. 3A 5.4) |
| 2023-05-17 | Section 9 determinations for BWB, CDS, and PNH |
| 2024-09-18 | Cyber security incident response tabletop (CIP-003 36-month test) |
| 2025-11-04 | FERC dam safety inspection of BWB and CDS, security portion included |
| 2025-12-16 | Annual Security Compliance Certification Letter filed for all 4 dams |
| 2026-04-01 | CIP-003-9 effective (vendor electronic remote access for low impact) |
| 2026-07-01 | CIP-012-2 effective |
| 2026-06-29 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (Section 9 re-determinations 2026-07-14 to 2026-07-16) |
| 2026-08-03 to 2026-08-28 | Control assessment by the co-sourced internal audit firm (site walkthroughs and tests 2026-08-10 to 2026-08-14) |
| 2026-09-17 | Deliverables approved by the Chief Operating Officer; High risks, risk appetite, and the FY2027 security budget approved by the Chief Executive Officer; results presented to the audit committee |
| 2026-09-30 | Plan and schedule for Form 3 negative responses sent to the FERC Regional Engineer |
| 2026-10-28 | Blackwater Bend Security Plan drill (5-year cycle, Rev. 3A 3.3.1) |
| 2026-11-10 | Next FERC dam safety inspection of BWB and CDS (security portion included) |
| 2026-12-31 | 2026 Annual Security Compliance Certification Letter due (Rev. 3A 8.0) |
| 2027-04-01 to 2027-09-30 | Planned SOC 2 Type 2 observation period for RMOS |

## 7. Facts added while completing the deliverables (fictional)

| Fact | Used in |
|---|---|
| Revenue per day: total about $509,600; generation about $350,700 (BWB $203,400; CDS $98,200; PNH $31,600; SGR $17,500); field services about $118,000 per working day (250 days); RMOS about $31,500 per day | P05, P01 |
| Additional role titles: Field Services Director, Recreation and Lands Manager, Manager of Energy Scheduling and Settlements, Maintenance Manager, Director of Communications | P05, P08 |
| FY2027 security budget approved by the CEO on 2026-09-17: $1.86 million one-time and $540,000 a year | P01, P07 |
| Section 9 re-determinations on 2026-07-16: BWB, CDS, and PNH gate control exceed Table 9.1c population thresholds (Critical); BWB generation is Operational on capacity (180 MW); CDS generation and PNH and SGR generation are Non-critical on capacity; the ROC SCADA is one cyber system with all 4 projects and is treated as Critical; SGR is an interconnected Group 3 dam held to the same level | P02, P03 |
| RMOS: 6 client projects owned by 4 clients; units and gates operated at 4 of them under written operating orders; the client contract template has no security schedule | P03, P09 |
| P07 sample details and new findings (see P07 `assessment-plan.md`) | P07 |
| Cyber insurance: $15 million limit, $500,000 retention; carrier panel supplies breach counsel and forensics; notice through the carrier hotline before engaging vendors | P08 |
| AI pilot measures for AI-001 and AI-002 (see P10) | P10 |
| Operations detail: 86 critical instruments read manually every 4 hours when automation is lost; 22 qualified call-out gate operators for the 20 panels; 105 cameras (64 at BWB and CDS, 41 at PNH, SGR, and the ROC); satellite phones at the ROC and BWB only; the ICCP link runs on one leased circuit | P05, P01, P03 |
| Cedar Shoals raw-water contract: about $1.2 million a year; the county water plant serves about 21,000 customers with 1 day of treated storage; undetected full flows could draw the reservoir below the intake in about 30 hours | P05, P01 |
| RMOS commitments (draft): 99.5% monthly availability, alarm relay within 5 minutes, monthly reports by the 10th; service credits of 10% of the monthly fee per day of outage, capped at 30%; 2 of 4 operating orders lack handback times | P05, P09 |
| Compliance records: CIP-002 identifications approved 2025-01-14 and 2026-02-10; CIP Senior Manager designated 2024-05-02; CIP-003 policy updated for topic 1.2.6 on 2026-03-20; CIP-003 IR plan updated 2025-01-30; EOP-004 Operating Plan rev. 2025-02 with one report (2025-11 trespass at the BWB switchyard); Security Assessments CDS 2019 and PNH 2020; the 2024 and 2025 certification letters stated Section 9 compliance; Form 3 completed 2026-07-16 with 19 negative answers | P03 |
| OT detail: 612 inventoried assets at the ROC and BWB; 47 controllers and HMIs, with complete backups for 19; BWB restore test 2025-11 (unit PLC and HMI rebuilt in 6 hours); interim controls from 2026-09-15 (OEM VPNs disabled except during approved sessions); SGR modem disconnected 2026-08-13; RMOS client tunnel rules narrowed by 2026-10-15 | P02, P07, P08 |
| FY2027 budget allocation and staffing additions (1 OT security engineer, 1 GRC analyst) | P01 |
| Vendor reviews (8) for the MSSP, SCADA vendor, 3 OEMs, cloud provider, identity provider, and HR/payroll SaaS | P09 |
| AI-005 enterprise assistant rolled out to 300 users in 2026-05; AI-003 in production since 2024; AI-004 pilot at BWB since 2026-03 | P10 |
| Executive ransomware tabletop scheduled 2026-12-08 | P08, P07 |
