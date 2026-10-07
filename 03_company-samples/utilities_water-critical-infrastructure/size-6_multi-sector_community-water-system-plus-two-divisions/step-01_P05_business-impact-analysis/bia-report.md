# Business Impact Analysis: Cris Santos Company Holdings | Water and Wastewater Systems | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and the Water Utility Emergency Management Director | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC and OT monitoring, network, cloud and data platform, OT remote access, finance, HR).
- **Division BIAs:** Water Utility (focus), Infrastructure Construction, and Environmental Services. They are rows in one workbook (`bia.csv`, `division` column), so cross-division dependencies are visible in one place.

It supports:
- the RRA and ERP that each of the 42 covered water systems must keep under SDWA section 1433, especially the assessment of automated systems and of operation and maintenance (42 U.S.C. 300i-2(a)(1)(A)(ii) and (vi)) and the ERP plans and procedures (300i-2(b)(2));
- the integrity and availability ratings of the SSP system, RS1-SCADA (P02);
- impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08) and the availability commitments of the Environmental Services monitoring service (P09).

## 2. System and business description
The Water Utility runs 58 community water systems serving about 3.37 million people. Its largest, Regional System 1 (RS-1), serves about 640,000 people from three plants (WTP-A, WTP-B, WTP-C) supervised by RS1-SCADA from a regional operations center. Construction builds and commissions water infrastructure, including the WTP-A expansion, and keeps DoD work in a separate CUI enclave (SYS-C2). Environmental Services runs remediation, hazardous waste transport, two liquid waste treatment facilities, and a hosted monitoring service for about 210 client treatment systems (SYS-E1). Corporate provides SYS-G1 to SYS-G5. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: the Water Utility about $6.6 million per day, Construction about $25.8 million per day, and Environmental Services about $17.0 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (safe water, construction progress, waste and monitoring services), or customers lose water or pressure in a large area | One plant, pressure zone, region, project, or facility stops | Staff slowed but working |
| Regulatory | Tier 1 public notice situation, treatment technique or MCL violation, missed DFARS report, permit violation, or SEC disclosure | Missed internal or contractual deadline; Tier 2 or 3 notice | Internal policy deviation |
| Public health and safety | Plausible illness or injury from unsafe water, a chemical release, or a hazmat event | Precautionary boil water notice for a limited area; delayed but safe work | None |
| Reputation | National media, regulator enforcement, loss of federal or monitoring clients | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 10 Water Utility, 5 Construction, and 5 Environmental Services. 14 are High, 11 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-W01 Water treatment and chemical feed | Water Utility | High | 8 h | 1 h | 24 h |
| BP-W02 Distribution pumping, pressure, and storage | Water Utility | High | 6 h | 2 h | 24 h |
| BP-W09 Operations at the 19 acquired systems | Water Utility | High | 12 h | 2 h | 24 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-W05 Public notification and emergency customer communications | Water Utility | High | 24 h | 4 h | 24 h |
| BP-W04 Water quality monitoring and compliance sampling | Water Utility | High | 24 h | 12 h | 4 h |
| BP-G03 Cloud landing zones and data platform | Group | High | 8 h | 4 h | 1 h |
| BP-E03 Liquid waste treatment facility operations | Environmental Services | High | 12 h | 4 h | 24 h |
| BP-E01 Remote monitoring and compliance data service | Environmental Services | High | 24 h | 4 h | 1 h |
| BP-C02 Project delivery and document control | Construction | High | 24 h | 8 h | 4 h |
| BP-E02 Hazardous waste transport and manifests | Environmental Services | High | 24 h | 8 h | 4 h |
| BP-W03 Supervisory monitoring and control (RS1-SCADA and regional SCADA) | Water Utility | High | 48 h | 24 h | 1 h |
| BP-W06 Field operations, main breaks, and work orders | Water Utility | Moderate | 24 h | 8 h | 24 h |
| BP-E05 Fleet routing and dispatch | Environmental Services | Moderate | 24 h | 8 h | 24 h |
| BP-G05 OT secure remote access | Group | Moderate | 24 h | 8 h | 24 h |
| BP-W07 Customer service and call center | Water Utility | Moderate | 48 h | 24 h | 4 h |
| BP-C01 Commissioning and controls integration | Construction | Moderate | 72 h | 24 h | 24 h |
| BP-C03 DoD project work in the CUI enclave | Construction | Moderate | 72 h | 24 h | 24 h |
| BP-E04 Remediation system operations at client sites | Environmental Services | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 72 h | 48 h | 24 h |
| BP-C04 Job cost and certified payroll | Construction | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-W08 Billing, payments, and AMI meter data | Water Utility | Moderate | 120 h | 72 h | 24 h |
| BP-W10 Water-quality anomaly detection (AI-001) | Water Utility | Low | 72 h | 24 h | 24 h |
| BP-C05 Equipment fleet telematics and maintenance | Construction | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Public health drives the Water Utility's shortest times.** Treatment (BP-W01) has an 8-hour MTD because RS-1's storage covers about 8 hours of average demand while holding fire reserve, and a 1-hour RTO because operators can move to local control within the hour. Pressure (BP-W02) has a 6-hour MTD because loss of pressure risks backflow and forces boil water notices.
- **Supervision is not the same as treatment.** SCADA (BP-W03) has a 48-hour MTD because licensed operators can run RS-1's plants and boosters manually, with roving crews and mutual aid, for about two days. Its RPO is 1 hour because the historian holds turbidity and residual records that support compliance.
- **The 19 acquired systems are more fragile** (BP-W09): smaller storage and on-call operators who depend on remote access at night, through tools that are not behind the group gateway (gap 1).
- **Notice clocks are processes too.** Public notification (BP-W05) has a 4-hour RTO so a Tier 1 notice can go out well inside 24 hours. The SOC (BP-G02) and financial close (BP-G06) carry regulatory weight because the P08 clocks (Tier 1 notice, DFARS 72 hours, Form 8-K) depend on them.
- **Client commitments drive Environmental Services.** The monitoring service (BP-E01) has a 1-hour RPO for the platform database because clients rely on complete records for their own permit reports; gateways buffer 72 hours of readings, which is why its MTD is 24 hours.
- **Remote access is rated Moderate on purpose** (BP-G05). The large plants are staffed around the clock, and in an incident the gateway is the first thing switched off (P08). Its recovery comes after the systems it reaches are proven clean.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in and MFA (SYS-G1) | Group | Every IT process; MFA for the 14 regional OT directories | An identity outage stops all three divisions' IT at once; plants keep running on local sessions and control-room emergency accounts |
| OT remote access (SYS-G4) | Group | Water Utility operators and integrators; Construction commissioning; Environmental Services technicians | One shared path into three divisions' OT. It is both a dependency and the P08 attack path |
| SOC and OT monitoring (SYS-G2) | Group | All divisions; P08 notice clocks | OT monitoring covers only the 6 largest water systems |
| Data platform and hosting (SYS-G3) | Group | SYS-E1 (Environmental Services); historian replicas and AI-001 (Water Utility) | A platform outage is a client-facing outage for Environmental Services |
| Commissioning at WTP-A (BP-C01) | Construction | Water Utility RS-1 | 34 commissioning engineers connect to RS1-SCADA through SYS-G4; their changes must follow Water Utility change approval |
| Treatment residuals hauling | Environmental Services | Water Utility plants | Residual solids must leave the plants on schedule; a long hauling outage limits plant operations after several days |
| Incident facts | Group SOC | Water Utility public notices; Construction DFARS report; Environmental Services client notices; SEC filing | Every notice in P08 depends on the SOC establishing what happened |

**Single points of failure found:** SYS-G1 (mitigated by break-glass and control-room emergency accounts, tested quarterly); SYS-G4 as the single remote path for 14 regional SCADA systems (acceptable, because plants are staffed and on-site work is the fallback); one cellular carrier for most SYS-E1 client gateways (P01 ES register).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| RS1-SCADA servers, HMIs, historian | BP-W01 to BP-W03 | Redundant servers at the ROC and backup control room; offline PLC and HMI project backups monthly and after change; historian replication to SYS-G3 every minute |
| Acquired-system local SCADA | BP-W09 | No offline backups yet (gap 2); integrator copies only |
| SYS-G1 identity platform | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, data platform, SYS-E1 | BP-G03, BP-E01, BP-W10 | Infrastructure as code; database replicas; immutable backups in provider B |
| SYS-C2 CUI enclave | BP-C03 | Provider-native backups inside the government-community tenant; daily |
| SYS-W2, SYS-W3, SYS-W4, SYS-C1, SYS-C4, SYS-G5 | Customer service, lab, field, projects, payroll | Vendor SaaS replication per contract; data exports weekly |
| People | All | Licensed operators cross-trained across plants in each region; mutual aid through state water and wastewater agency response networks |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. to 3. Safe water first: treatment and chemical feed, distribution pressure, and operations at the acquired systems, all in manual or local control if needed
4. to 6. Identity and break-glass access, network connectivity, and SOC visibility
7. to 8. Public notification capability and water quality monitoring
9. Cloud landing zones and the data platform (brings back SYS-E1 hosting)
10. to 13. Liquid waste facilities, the client monitoring service, Construction project delivery, and hazardous waste transport
14. RS1-SCADA and regional SCADA, rebuilt and verified, then returned to automatic control one process at a time
15. to 27. Field operations, fleet dispatch, OT remote access (only after the systems it reaches are proven clean), customer service, commissioning, CUI project work, remediation sites, payroll and HR, job cost, financial close, billing and AMI, anomaly detection, and equipment telematics.

## 8. Key findings
1. **Water safety does not depend on IT or SCADA availability, by design.** Every plant can run manually, and the 15 largest systems' plants have hardwired feed limits and alarms. The 19 acquired systems are the exception, because their night coverage relies on remote access (P01 WU register).
2. **The shared remote access gateway links all three divisions' OT.** It is Moderate for availability but High for integrity: a misuse of SYS-G4 can change treatment at RS-1 (P02, P08).
3. **SYS-G3 is client-facing.** For Environmental Services, a data platform outage is a breach of service commitments to about 210 clients, so the platform's RTO of 4 hours is set by BP-E01, not by internal analytics.
4. **Recovery of SCADA must be slow on purpose.** Returning to automatic control before PLC logic is verified against offline copies would reintroduce the risk. The 24-hour RTO for BP-W03 assumes verified offline copies, which exist at the 6 largest systems only.
