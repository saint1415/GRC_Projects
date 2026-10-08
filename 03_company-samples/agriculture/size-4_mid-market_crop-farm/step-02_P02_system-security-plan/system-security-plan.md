# System Security Plan: Farm Management and Irrigation Control Platform (FMICP)

**Organization:** Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) | **Tier:** Mid-Market | **Vertical:** Agriculture, Forestry, Fishing and Hunting
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Farm Management and Irrigation Control Platform (**FMICP**), identifier CSC-FMICP-01. The FMICP is the company's major system. It comprises the components listed for the SSP system in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv).

## 2. System Overview
The FMICP plans, controls, and records the company's crop production and packing: irrigation and fertigation on three farms (about 15,400 acres), freeze protection at Farm 2, harvest crew dispatch and field tally, packing, cooling, and ripening at the central packinghouse, cold-chain monitoring, food safety and traceability records, and the Grower Services portal and weekly settlement for about 30 contract growers. It supports the High and Moderate processes in the BIA (P05). Users are about 230 year-round staff, 60 crew leads on tablets, about 140 grower portal users, and named vendor technicians.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | FMIS with irrigation module: field and crop plans, pesticide and Produce Safety records, harvest tally and traceability data, irrigation schedules | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-02 | Identity provider with SSO, MFA, and conditional access, as it protects the FMICP | SaaS |
| SYS-04 | Cloud landing zone: identity and security, shared services, operations workloads (farm data hub, imagery data lake), Grower Services workloads, and backup accounts | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-05 | Networks at 6 sites (headquarters, packinghouse, 3 farm offices, H-2A housing), SD-WAN, pump-station radio and fiber, pivot cellular, LoRaWAN gateways | On-premises; SD-WAN managed service; cellular carriers |
| SYS-06 | Endpoints used to run the farms and the packinghouse: about 140 laptops and desktops, 160 tablets and phones, 20 packinghouse line PCs | Company-managed |
| SYS-07 | OT: irrigation SCADA (2 servers, 4 HMIs, historian, alarm dialer), 54 well pumps, 14 fertigation skids, about 1,500 valve controllers, 46 pivots (manufacturer cloud), about 900 soil probes, 120 flow meters, 14 weather stations; packinghouse cooling, ripening, cold storage, 4 packing lines, 2 optical graders, 140 cold-chain sensors | On-premises; pivot and alarm vendor clouds |
| SYS-12 | Grower portal and settlement service | Company-owned application in the Grower Services account, built by a contract development firm |
| SYS-14 | SIEM (MSSP-operated), EDR, vulnerability scanner, cloud posture service, as they monitor the FMICP | SaaS and cloud |

Telematics (SYS-08), drones (SYS-09), the ERP (SYS-10), and HR and payroll (SYS-11) connect to the FMICP as external systems (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the FMICP |
|---|---|---|---|
| Benchmark | NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (2024-02-26) | Voluntary benchmark for the control program (P03); no binding federal cybersecurity rule applies to the company |
| Benchmark | NIST SP 800-82 Rev. 3, Guide to OT Security | NIST SP 800-82r3 (September 2023) | OT architecture (section 5), CSF application to OT (section 6), and the Appendix F OT overlay consulted for SYS-07 |
| Binding | Produce Safety Rule, records | 21 CFR 112.161-112.166 | Records in SYS-01 must be created at the time, accurate, legible, indelible, signed by the person, kept 2 years, and available to FDA (24 hours if offsite) |
| Binding (not enforced before 2028-07-20) | Food Traceability Rule | 21 CFR 1.1315-1.1455 | Harvest, cooling, initial packing, and shipping records for tomatoes, peppers, and watermelons; electronic sortable spreadsheet within 24 hours of an FDA request (1.1455(c)(3)(ii)) |
| Binding | H-2A earnings records and statements | 20 CFR 655.122(j)-(k) | Field tally in SYS-01 is part of the earnings record; records kept 3 years, safe and accessible |
| Binding | Worker Protection Standard, application information | 40 CFR 170.311(b) | Application records in SYS-01 must support display within 24 hours and 2-year retention |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security for personal information (tally names, operator geolocation in telematics, grower bank details where linked to individuals); breach notice (P08) |
| N11-R01 | FSMA intentional adulteration rule | 21 CFR Part 121 | **Not applicable** (farm; 21 CFR 1.226(b), 121.5(d)). Used as a voluntary checklist for the food defense plan retail customers require (fertigation, packinghouse water, ripening rooms) |
| Contract | Marketing agreements with contract growers | Contract | Availability and settlement commitments; SOC 2 Type 2 report requested by 2027-12-31 (P09) |
| Contract | Retail supplier agreements | Contract | Food safety audit, traceability, food defense plan; notice within 24 hours of events affecting product safety, traceability, or committed volumes |
| Internal | Security policies POL-01 to POL-05 and the standards index | P06 | Policy basis for every control |

Not applicable:
- **SEC cybersecurity disclosure rules:** privately held.
- **FAR cyber clauses:** no federal contracts or subcontracts.
- **CIRCIA (proposed 6 CFR Part 226):** no final rule as of 2026-09-25. As proposed, the company would be covered because it exceeds its SBA size standard; tracked in P03 and P08.
- **PCI DSS scope:** card payments at the on-farm market and online store use P2PE terminals and a hosted payment page outside the FMICP.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the FMICP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:**
  1. Vendor remote access to SCADA moves to brokered, per-session, recorded access with MFA by 2026-12-31 (POAM-003).
  2. Default credentials on packinghouse controllers are changed and the broad packinghouse firewall rule is removed by 2026-10-15 (POAM-013, POAM-018).
  3. The freeze-night manual start procedure and standalone alarm are in place and tested by 2026-11-30, before the first freeze night (POAM-012).
  4. The audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- OT segmentation of the Farm 1 and Farm 2 pump-station and fertigation networks (due 2027-03-31)
- Passive OT monitoring feeding the SIEM, with setpoint and recipe change alerts (due 2027-03-31)
- Privileged access management for directory, SYS-01, ERP, and SCADA administrators (due 2027-03-31)
- Secure development standard and pipeline controls for the grower portal (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the FMICP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security lead | Security Manager, with 2 security analysts | Designated security lead; vulnerability management; MSSP liaison; GRC |
| IT control owner | IT Director | Identity, networks, IT/OT boundary, endpoints, cloud landing zone, backups |
| OT control owner | Director of Irrigation and Water Resources | SCADA, PLCs, pivots, sensors, freeze protection, water use reporting |
| Packinghouse OT owner | Packinghouse Manager | Cooling, ripening, cold storage, packing lines, graders, cold-chain alarms |
| Records owner | Director of Food Safety and Quality | Produce Safety, pesticide, and traceability records in SYS-01 |
| Grower Services owner | Vice President of Grower Services | Grower portal, settlement service, grower access |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring of IT components |

## 6. System Information Types and System Categorization
SP 800-60 Vol. 2 Rev. 1 is built around federal mission areas and has no farm production or packing type. The information types below are author-defined following the SP 800-60 method; impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Irrigation, fertigation, and freeze-protection control (schedules, setpoints, recipes, PLC programs) | Low | Moderate | Moderate | Wrong commands can burn or drown crops, exceed label or permit limits, or expose workers. Hand operation at every panel limits the availability impact to Moderate, except on freeze nights (P05 BP-02, MTD 2 hours), which is why the freeze procedure is a condition of operation |
| Packinghouse process control and cold-chain data | Low | Moderate | Moderate | Wrong ripening or cooling settings spoil product or send temperature-abused produce; hardwired safety shutoffs and manual rounds bound the harm (P05 MTD 2 to 4 hours) |
| Food safety and traceability records | Low | Moderate | Low | Must be accurate and indelible (21 CFR 112.161(a)); a 24-hour outage is tolerable with paper forms |
| Worker tally and earnings records | Moderate | Moderate | Low | Names with piece-rate counts; errors cause wage disputes and program findings |
| Grower business and settlement data | Moderate | Moderate | Moderate | Commercially sensitive yields, grades, and prices; settlement errors misstate payments; weekly schedule (P05 BP-12) |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for incident investigation |
| **FMICP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** Fertigation and ethylene ripening involve chemicals. The team kept integrity at Moderate for three reasons: injection skids have mechanical maximum-rate limits and backflow prevention, ripening rooms have gas detectors with hardwired shutoffs that software cannot override, and operators check rates and room settings at each shift. To compensate, the plan adds integrity tailoring: CM-3, CM-4, and SI-7 cover PLC programs, recipes, and settlement code, and SI-4 adds setpoint change alerting once OT monitoring is in place.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). The endpoint counts are the CMDB and endpoint console totals (EV-012: 210 laptops and desktops, of which about 140 are used to run the farms and the packinghouse, 160 tablets and phones, and 20 line PCs). The OT count of about 2,900 devices comes from installer invoices and purchasing records (EV-014); about 1,600 of them are in the OT inventory (EV-013).

**Inside the boundary:**
- the company's SYS-01 tenant configuration, roles, and integrations;
- the identity provider tenant as it protects the FMICP;
- all 5 cloud accounts and their workloads (farm data hub, imagery data lake, grower portal, settlement service, backups);
- networks at 6 sites, pump-station radio and fiber links, pivot cellular modems, and LoRaWAN gateways;
- endpoints used to run the farms and the packinghouse;
- the irrigation SCADA system, PLCs, field devices, and packinghouse controls (about 2,900 OT and IoT devices);
- the company's SIEM tenant and use cases.

**Outside the boundary (external services, interconnected):**
- the FMIS vendor's platform;
- the cloud provider's infrastructure;
- the pivot manufacturer's cloud service and the cold-chain alarm service;
- the equipment dealer's telematics portal (SYS-08);
- the ERP and EDI providers (SYS-10) and the payroll provider (SYS-11);
- the MSSP's platform;
- the agronomy analytics vendor (AI-001);
- the SCADA integrator's and the development firm's own systems;
- contract growers' sensor gateways.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| FMIS vendor (SYS-01) and farm data hub | Bidirectional API over TLS | Schedules, field records, tally, traceability data | SaaS agreement; SOC 2 Type 2 |
| Pivot manufacturer cloud service | Bidirectional | Pivot commands and status for 46 pivots | Click-through terms only; **no security terms (gap, CA-3)** |
| Cold-chain alarm service | Outbound sensor data; inbound alerts | Temperatures | Service agreement |
| ERP and EDI provider (SYS-10) | Bidirectional | Orders, shipments, prices for settlements | SaaS agreement |
| Payroll provider (SYS-11) | Outbound tally hours and piece counts | Worker names and earnings data | SaaS agreement; third-party agent under Fla. Stat. 501.171 |
| Equipment dealer telematics (SYS-08) | Inbound as-applied and yield data; dealer remote diagnostics | Machine data with operator location | Dealer terms; **standing dealer access (EV-010)** |
| Agronomy analytics vendor (AI-001) | Outbound imagery; inbound yield estimates | Drone imagery, block yields | Click-through terms; **data-use terms under review (P10)** |
| Contract growers' sensor gateways (18 growers) | Inbound | Soil moisture and flow data | Marketing agreement schedule; **no interconnection terms** |
| SCADA integrator | Inbound remote support | Full SCADA access | Services agreement; **no security terms; shared account (EV-048, EV-008)** |
| Development firm | Inbound deployments to the Grower Services account | Code and configuration | Development contract; **no secure development terms (EV-053)** |
| MSSP | Inbound logs; remote response actions | Security logs | Contract; SOC 2 Type 2 |
| Bank (settlement ACH) | Outbound | Grower payment files | Treasury agreement; dual approval |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 FMIS tenant and irrigation module | SaaS | FMIS vendor | Chief Operating Officer |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Farm data hub (historian replica, integration services) | Virtual machines and managed database | Operations workloads account | Director of Irrigation and Water Resources |
| Imagery data lake | Object storage | Operations workloads account | Precision Agriculture Manager |
| Grower portal and settlement service | Containers, managed database, web application firewall | Grower Services workloads account | Vice President of Grower Services |
| Backup vault | Backup service with write-once retention | Backup account (second region) | IT Director |
| Network hub, cloud firewall, site VPN, privileged access broker, log archive | Network and management services | Shared services account | IT Director |
| Cloud identity federation, guardrails, posture service | Identity and policy services | Identity and security account | Security Manager |
| SD-WAN edges, IT/OT firewalls, switches, Wi-Fi | Network | 6 sites | IT Director |
| Pump-station radio and fiber links, pivot cellular modems, LoRaWAN gateways | Network | Farms 1-3 | Director of Irrigation and Water Resources |
| Irrigation SCADA servers (2), HMIs (4), historian, alarm dialer | OT | Irrigation Operations Center | Director of Irrigation and Water Resources |
| Well pumps and VFDs (54), fertigation skids (14), valve controllers (about 1,500), pivots (46), soil probes (about 900), flow meters (120), weather stations (14) | OT and IoT | Farms 1-3 | Director of Irrigation and Water Resources |
| Packing line PLCs (4), optical graders (2), cooling and cold storage controls, ripening room controllers (12), cold-chain sensors (140) | OT and IoT | Packinghouse | Packinghouse Manager |
| Laptops and desktops (about 140 in scope), tablets and phones (160), packinghouse line PCs (20) | Endpoint | All sites | IT Director |
| SIEM tenant, EDR console, vulnerability scanner | Security tooling | MSSP and SaaS | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The FMICP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), with the SP 800-82 Rev. 3 Appendix F OT overlay consulted for SYS-07. Tailoring:
- **Documented here: 115 controls** in `control-implementation.csv`: 110 from the Moderate baseline and 5 added by tailoring. They cover the Moderate controls that address the risks in P01 (remote access, segmentation, recovery, change control, monitoring, vendors) and the CSF 2.0 High-priority subcategories in P03.
- **Selected by tailoring (added):** CA-8 (annual penetration test of the internet-facing grower portal), PM-1, PM-2, PM-9, and PM-30. They are not in the Moderate baseline but are needed for program governance and supply chain strategy.
- **Integrity tailoring:** CM-3, CM-4, SI-7, and SI-10 statements cover PLC programs, fertigation and ripening recipes, and settlement calculations.
- **OT compensating controls:** where OT devices cannot meet a control as written (unique accounts on legacy HMIs, MFA on PLCs, screen lock in a staffed control room), the statement names the compensating control, following SP 800-82 Rev. 3 section 6.2.1.
- **Inherited without separate statements:** physical and environmental controls for vendor and cloud data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the FMIS vendor, identity vendor, cloud provider, and MSSP and evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no Moderate-or-higher risk in P01, recorded as tailoring decisions and reviewed yearly.

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 31 |
| Partially implemented | 77 |
| Planned | 7 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 75 | Company |
| Hybrid | 33 | FMIS vendor, identity vendor, cloud provider, MSSP |
| Common/Inherited | 7 | Identity vendor (AC-2(1), AC-7, AC-12), cloud provider (CP-6, SC-12, SC-13), MSSP (IR-7) |

The Partially implemented statements trace to the intake observations cited in the `evidence` column of `control-implementation.csv` (for example EV-008, EV-013, EV-024 and EV-053) and to the P07 findings. IT controls are mostly in place; the shortfalls concentrate in OT, vendors, recovery, and the grower portal's development process.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 33 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** Office users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. This is appropriate for a Moderate system that can change irrigation settings and settlement data.
- **Administrators.** Cloud administrators use just-in-time elevation through the privileged access broker. Directory, SYS-01, ERP, and SCADA administrators will move to brokered access with phishing-resistant authenticators by 2027-03-31 (P01 R-009).
- **Crew leads.** Crew leads will use named SYS-01 accounts with a device PIN on managed tablets in kiosk mode by 2026-11-15 (POAM-001). That is proportionate for entering tally records on a company-owned device and makes each record attributable (21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1)).
- **OT.** HMIs that cannot support unique accounts with MFA use named operator PINs, a staffed control room, and network isolation as compensating controls. Remote access to OT will require MFA at the access broker (POAM-003).
- **Growers.** Grower portal users have unique accounts with email verification. MFA will be required for any user who can view settlements or change bank details by 2027-03-31 (P01 R-011).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **FMICP:** Farm Management and Irrigation Control Platform
- **FMIS:** farm management information system
- **FTR:** FDA Food Traceability Rule (21 CFR Part 1, Subpart S)
- **HMI:** human-machine interface
- **IOC:** Irrigation Operations Center
- **LoRaWAN:** long-range wide area network used by soil probes
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **OT:** operational technology
- **P2PE:** point-to-point encryption
- **PLC:** programmable logic controller
- **RTK:** real-time kinematic (GNSS correction)
- **SCADA:** supervisory control and data acquisition
- **VFD:** variable-frequency drive
- **WPS:** EPA Worker Protection Standard (40 CFR Part 170)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager with the vCISO |
