# Scenario facts: Cris Santos Company | Energy | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (interstate natural gas transmission pipeline operator; private; private equity-backed; board with an audit committee) |
| Business | Interstate natural gas transmission pipeline (NAICS 486210), regulated by FERC under the Natural Gas Act, with a FERC gas tariff for firm and interruptible transportation. The company also operates two third-party laterals from its Gas Control Center under operations services agreements (section 7) |
| Location | Headquarters and **Gas Control Center (GCC)** in Florida. The pipeline runs from receipt interconnects in southern Alabama and southwest Georgia into north and central Florida. Facilities: 5 compressor stations (Compressor Station 1 to 5), a **Backup Control Center (BCC)** at Compressor Station 3, and 6 area offices (2 in Georgia and Alabama, 4 in Florida) |
| Pipeline assets | About 780 miles of steel transmission pipeline (16 to 36 inches) in 3 states; 5 compressor stations with 14 compressor units (about 118,000 horsepower); 4 receipt interconnects with upstream interstate pipelines; 46 delivery meter and regulator (M&R) stations; 62 remote-control mainline valve sites. About 310 remote terminal units (RTUs) and programmable logic controllers (PLCs) in the field. Design capacity about 1.0 million dekatherms per day (above the 100,000 Mcf per day threshold in 18 CFR 260.8). Class 1 to 3 locations, with Class 3 segments in suburban areas near 4 cities |
| Customers (shippers) | 9 local distribution companies (LDCs) serving about 1.3 million homes and businesses, 7 gas-fired power plants (5 owned by electric utilities that are NERC-registered entities), 22 industrial customers, and 6 marketers |
| Workforce | 600 employees: gas control 36, SCADA and OT engineering 14, field operations 330, engineering, integrity, and measurement 62, commercial and scheduling 32, pipeline safety and regulatory compliance 24, IT 30, cybersecurity and GRC 8, executive, finance, legal, HR, supply chain, and administration 64 |
| Revenue | About $100 million a year (fictional): about $92 million firm transportation reservation revenue, $5 million interruptible and other services, and $3 million operations services fees. Not SBA-small (standard $41.5 million for NAICS 486210; 13 CFR 121.201) |
| Pipeline safety regulator | Interstate pipeline: PHMSA's Office of Pipeline Safety inspects and enforces 49 CFR Parts 191 and 192 directly. The company has controllers who monitor and control the pipeline through SCADA and has compressor stations, so **all of 49 CFR 192.631** applies (the reduced-procedure exception in 192.631(a)(1)(ii) covers only transmission without a compressor station) |
| TSA status | **Designated.** TSA notified the company in 2021 that its pipeline system is critical. It is subject to Security Directive Pipeline-2021-01G (effective 2026-01-16 to 2027-01-15) and Security Directive Pipeline-2021-02G (effective 2026-05-03 to 2027-05-02) (see P03 section 1) |
| FERC status | Natural gas company under the Natural Gas Act. Posts customer and capacity information on its website under 18 CFR 284.13 and follows the NAESB WGQ standards incorporated by 18 CFR 284.12, including the WGQ Cybersecurity Related Standards. Files Form No. 567 system flow diagrams each year (18 CFR 260.8) with a request for CEII treatment (18 CFR 388.113) |
| Not in scope | NERC CIP (the company is not a NERC-registered entity and owns no Bulk Electric System assets; its power plant customers are registered); DOE Form OE-417 (electric only); SEC disclosure (privately held); payment cards (shippers pay by wire and ACH); HIPAA (the employee health plan is fully insured and the company receives only summary information) |
| State law approach | Employees live in Florida, Georgia, and Alabama. State law is treated generically ("each state where affected individuals reside"), with Florida as the worked example (Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board audit committee | Receives the quarterly cyber risk report; approves the risk appetite each year |
| Chief Executive Officer (CEO) | Accepts High risk; approves POL-01, the risk appetite, and the security budget; decides on any ransom question with the board chair |
| Chief Operating Officer (COO) | Executive sponsor of the security program; **system owner** of the Pipeline SCADA and Gas Control System; accepts Moderate risk; **approves any precautionary shutdown** for cyber reasons; Accountable Executive for TSA matters |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, board reporting, and annual review of the TSA plans |
| Security Manager | Leads security operations and GRC; **primary TSA Cybersecurity Coordinator** (U.S. citizen); incident commander for cyber incidents |
| OT Security Engineers (2) | OT monitoring, OT access, OT patch mitigations; one is the **alternate Cybersecurity Coordinator** |
| Security analysts (3) and GRC lead plus 1 GRC analyst | Vulnerability management, MSSP liaison, risk register, POA&M, TSA Cybersecurity Assessment Plan schedule |
| IT Director | Business IT and cloud; second alternate Cybersecurity Coordinator |
| Director of Gas Control | Owns the control room management procedures (49 CFR 192.631) and alarm management; operations lead in any cyber incident; may isolate OT from IT at any time |
| SCADA and OT Engineering Manager | Administers the SCADA servers, HMIs, historian, OT network, and field device configuration |
| VP Operations | Owns the operations and maintenance manual (192.605) and emergency plan (192.615); field operations and compressor stations |
| Director of Pipeline Safety and Compliance | PHMSA compliance and incident notices under 49 CFR Part 191; operator qualification records |
| Director of Regulatory Affairs | FERC tariff and filings, Form No. 567 and CEII requests, Informational Postings |
| VP Commercial | Shipper relations, nominations and scheduling, critical notices, operations services customers |
| General Counsel | Legal privilege, breach determinations, contract notices, SSI questions with TSA |
| Chief Financial Officer | Cyber insurance, reservation charge credit exposure, fraud controls |
| Internal audit (co-sourced firm) | Annual IT audit; performs the P07 assessment and the annual TSA assessment work under the Cybersecurity Assessment Plan |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR (business IT), the SIEM, and the OT monitoring sensors; may isolate business endpoints, never OT devices |

## 3. Systems
| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Primary SCADA at the GCC: redundant SCADA servers, 10 HMI consoles, historian, 2 engineering workstations | On-premises, GCC | Primary system. Separate OT Windows domain with no trust to the business domain |
| SYS-02 | Backup Control Center: hot-standby SCADA servers, 6 HMI consoles, historian | On-premises, Compressor Station 3 | Failover tested annually (192.631(c)(4)); last test 2025-11-04 |
| SYS-03 | Field control devices: about 310 RTUs and PLCs, flow computers, gas chromatographs at 46 M&R stations, 62 valve sites, and 4 receipt interconnects | Field | Flow computers keep about 35 days of measurement data locally |
| SYS-04 | Compressor station control systems: station control PLCs, unit control panels, 22 station HMIs, and hardwired emergency shutdown (ESD) systems | 5 compressor stations | ESD is independent of SCADA and PLC logic |
| SYS-05 | SCADA telecommunications: private microwave backbone between the GCC, BCC, and compressor stations; licensed radio; carrier MPLS circuits; cellular gateways at 41 field sites; satellite backup at 12 critical sites | Field | |
| SYS-06 | IT/OT DMZ at the GCC and BCC: firewall pairs, historian replica, patch and anti-malware staging server, remote access gateway with MFA and session recording | On-premises | Remote access gateway in service since 2024 for staff and vendors |
| SYS-07 | OT security monitoring: passive network sensors | GCC, BCC, Compressor Stations 1 and 3 | Deployed 2025; alerts to the MSSP. Not at Compressor Stations 2, 4, and 5 or at field sites |
| SYS-08 | Business network and endpoints | HQ, 6 area offices, 5 compressor station offices | About 720 laptops and desktops, 260 rugged field tablets |
| SYS-09 | Identity provider (SSO and MFA) | SaaS | Business systems, cloud, and the DMZ remote access gateway. Not used inside the OT domain |
| SYS-10 | Productivity suite (email, files, chat) | SaaS | |
| SYS-11 | Cloud landing zone: 5 accounts (security and identity, shared services, business workloads, OT analytics, backup and log archive) | Public cloud (vendor-agnostic) | Gas measurement and accounting application, GIS and integrity data, leak-detection model, immutable backups (P04) |
| SYS-12 | Customer activities website: nominations, scheduling, capacity release, and Informational Postings | Vendor SaaS | FERC-required postings (18 CFR 284.13); NAESB WGQ standards (18 CFR 284.12) |
| SYS-13 | Business SaaS: ERP and gas accounting, HR and payroll | SaaS | Employee personal information |
| SYS-14 | Physical access control and CCTV | GCC, BCC, compressor stations, area offices | Badge access and CCTV at staffed sites; intrusion alarms at M&R stations |
| SYS-15 | SIEM and EDR (MSSP-operated) | SaaS | Business IT, cloud, identity, firewall, DMZ, and OT sensor alerts |
| SYS-16 | About 85 third parties with system or data access | Various | Includes the SCADA software vendor, the SCADA integrator, the telecom carrier, the compressor OEM, the MSSP, and the model vendor |

**SSP system (P02):** the *Pipeline SCADA and Gas Control System (PSGCS)*: SYS-01 to SYS-07 and physical access control at the GCC, BCC, and compressor stations (part of SYS-14), with interfaces to the cloud OT analytics account (SYS-11), the customer activities website (SYS-12), and the MSSP (SYS-15).

## 4. Current security posture: defined program with gaps in scale
**In place today:**
- TSA-approved Cybersecurity Implementation Plan (first approved 2023, last amended 2024); Cybersecurity Incident Response Plan exercised each year; Cybersecurity Assessment Plan last approved by TSA on 2025-11-20
- Cybersecurity Coordinator and alternates designated and reachable 24x7 (SD 01G)
- IT/OT segmentation: firewall pairs and a DMZ at the GCC and BCC; separate OT domain with no trust to the business domain
- MFA for business IT, cloud, and all remote access to OT through the DMZ remote access gateway (staff and vendors), with session recording
- MSSP 24x7 monitoring of EDR and the SIEM; OT network monitoring at the GCC, BCC, and 2 of 5 compressor stations
- Immutable cloud backups for business workloads (35-day write-once retention); monthly offline SCADA backups stored at the BCC
- Annual failover to the Backup Control Center; tested internal communication plan for manual operation
- Written control room management procedures and alarm management plan; controller training that includes 3 cyber-caused abnormal operating conditions
- Patch management strategy with CISA Known Exploited Vulnerabilities prioritization (IT patched within targets; OT on a quarterly cycle with documented mitigations)
- Third-party cybersecurity architecture design review completed in 2025
- Policies adopted in 2024; annual training and quarterly phishing simulations; co-sourced internal audit

**Gaps found in the 2026 assessments:**
1. Shared accounts remain on the station HMIs at Compressor Stations 2, 4, and 5. About 40% of field devices are past the password reset schedule in the Cybersecurity Implementation Plan, and the documented mitigation timeframe for them expired on 2026-06-30.
2. OT monitoring does not cover Compressor Stations 2, 4, and 5 or any field site, and field telecommunications traffic has no documented baseline.
3. The compressor OEM keeps remote diagnostics connections to unit control panels that are not documented in the Cybersecurity Implementation Plan (see P07 for what testing found).
4. The OT asset inventory is about 85% complete for field devices; firmware versions are unknown for about 20% of RTUs and PLCs.
5. OT patching lags: 14 station HMIs run an operating system past end of support, and 6 CISA KEV entries on OT components are past the mitigation timeline.
6. OT and field device access is reviewed once a year, not quarterly. OT accounts of departing staff are removed in 5 business days on average, against a 1-business-day standard.
7. IT/OT isolation has been exercised in tabletops but never performed live. The criteria for a precautionary shutdown are not tied to the BIA, and the 2025 tabletop showed executives defaulting to shutdown.
8. A full rebuild of the SCADA servers from backup has not been tested in the last 12 months, and PLC logic backups are missing for Compressor Stations 2, 4, and 5.
9. Third-party risk: about 60% of the 85 vendors with access have security terms in their contracts; SOC 2 reports have been reviewed for 4 of 14 Tier 1 vendors; the SCADA software vendor has no SOC 2 report.
10. OT security logs are kept 90 days in the SIEM against the company's 12-month standard; field device logs are not collected.
11. The Cybersecurity Assessment Plan schedule is behind: 28% of Cybersecurity Implementation Plan measures were assessed in the plan year to date, against the one-third minimum.
12. Two permanent changes (the OT analytics cloud account and the replacement of the remote access gateway vendor) were not submitted to TSA as Cybersecurity Implementation Plan amendments within 50 days (SD 02G Section VI).
13. SSI handling: copies of TSA plans and the assessment report were found on a general file share without SSI markings.
14. AI governance: the leak-detection model and a compressor predictive maintenance model are in production without an AI standard, and vendor model updates bypass management of change.

## 5. Scenario choices
| Deliverable | Scenario choice |
|---|---|
| P03 | **All rules for the primary business line:** TSA SD Pipeline-2021-02G (primary, binding), TSA SD Pipeline-2021-01G (binding), 49 CFR 192.631 control room management (SCADA-relevant duties), and the 49 CFR Part 1520 SSI duties that the directives trigger. FERC CEII and NAESB WGQ cybersecurity standards are recorded in the applicability table |
| P08 | **Two incident types:** (1) ransomware on business IT forcing a precautionary pipeline shutdown decision (registry default kept); (2) suspected OT compromise through a vendor remote connection with untrusted SCADA data. Integrated with the emergency plan (192.615), crisis management, and legal |
| P09 | Readiness for a SOC 2 Type 2 examination of the **contract operations services** (Security, Availability, Processing Integrity, Confidentiality), requested by the two lateral owners; plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio: AI-001 leak-detection anomaly model (registry default kept), AI-002 compressor predictive maintenance, AI-003 right-of-way imagery change detection, AI-004 enterprise generative AI assistant, AI-005 EDR machine learning detection |
| Cloud | Multi-account landing zone (5 accounts), vendor-agnostic |

The registry defaults for the primary system, the P08 incident, and the P10 use case fit this business and were kept. A second incident type and four more AI use cases were added because the Mid-Market tier calls for two runbooks and an AI portfolio.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (TSA designation status and directive versions confirmed 2026-07-07) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (Compressor Station 4 and two M&R stations visited 2026-08-12) |
| 2026-09-17 | Deliverables approved by the COO; High risks and the risk appetite approved by the CEO; results to the audit committee the same day |
| 2026-11-20 | Annual Cybersecurity Assessment Plan update and annual report due to TSA (12 months after the 2025-11-20 approval) |

## 7. Facts added during the build (fictional; used across P01-P10)
| Topic | Added fact |
|---|---|
| Operations services | Under operations services agreements, the GCC monitors and controls a 60-mile intrastate lateral owned by a municipal gas utility and a 35-mile lateral owned by a power generator. Fees are about $3 million a year. Both owners asked for a SOC 2 Type 2 report by 2027 (P09) |
| Revenue per day | Firm reservation revenue is about $252,000 per day. Under the tariff, an outage that is not force majeure can require reservation charge credits to affected shippers; a force majeure outage can require partial credits |
| Critical Cyber Systems (TSA) | CCS-1 primary SCADA (SYS-01); CCS-2 Backup Control Center (SYS-02); CCS-3 field devices and SCADA telecommunications (SYS-03, SYS-05); CCS-4 compressor station control systems (SYS-04); CCS-5 IT/OT DMZ and remote access gateway (SYS-06); CCS-6 OT security monitoring (SYS-07); CCS-7 customer activities website and scheduling (SYS-12); CCS-8 identity provider (SYS-09) because it controls remote access to OT |
| Cyber insurance | $20 million aggregate limit, $500,000 retention. The policy requires notice through the carrier hotline before incident vendors are engaged |
| Workforce activity | 74 terminations and 41 internal transfers in the 12 months to 2026-06-30. The last OT access review was completed in February 2026. The June 2026 phishing simulation click rate was 6.1% |
| Vendor tiers | 14 of the 85 vendors with access are Tier 1 (OT access, Restricted or SSI data, or support for a High-criticality BIA process) |
| Shared accounts | The station HMIs at Compressor Stations 2, 4, and 5 (12 of the 22 station HMIs) use one shared operator login per station. Primary and backup control center HMIs use individual logins |
| OEM connections | The compressor OEM's remote diagnostics service collects unit vibration and performance data for its predictive maintenance model (AI-002) |
| Cloud | OT analytics account added 2025-05; remote access gateway vendor replaced 2025-09 |
| Terminology | "Pipeline SCADA and Gas Control System (PSGCS)" is the SSP system in P02, identifier CSC-PSGCS-01 |
| Additional role titles | Shift supervisors (5); gas controllers (28); Area Managers (6); Compressor Station Supervisors (5); Measurement Manager; Director of Engineering and Integrity; GIS Manager; HR Director; Supply Chain Manager; Director of Corporate Communications |
