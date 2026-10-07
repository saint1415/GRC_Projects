# Business Impact Analysis: Cris Santos Company Holdings | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and the Group OT Security Director | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and WAN, OT remote support access, the group data platform, finance, HR).
- **Division BIAs:** Crude Oil Production (focus), Power Generation, and Crude Logistics. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It feeds:
- each division's contingency and emergency plans, including the Crude Logistics emergency procedures under 49 CFR 195.402 and the control room procedures under 195.446;
- the Power Generation low impact Cyber Security Incident response plan (CIP-003-9 Attachment 1 Section 4);
- the availability rating in the SSP (P02), impact ratings in the risk registers (P01), and the recovery order in the incident runbook (P08);
- the availability commitments the Crude Logistics shipper services platform will make in its SOC 2 report (P09).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity (including the shared OT support jump servers), SYS-G2 SOC with its OT desk, SYS-G3 cloud and WAN, SYS-G4 ERP and HR, SYS-G5 productivity, and SYS-G6 the group data platform. Each division runs its own control systems on premises: Production's enterprise field SCADA (SYS-P1, SYS-P2) and the Mid-Continent legacy SCADA (SYS-P5); Power Generation's plant control systems and Generation Control Center (SYS-E1, SYS-E2); and Crude Logistics' pipeline SCADA and Pipeline Control Center (SYS-M1) with measurement (SYS-M2). See `../00_company-facts.md` sections 3 and 7.

**Control does not depend on corporate IT.** Every control room keeps local logons and its own OT network, so the loss of SYS-G1 or the WAN does not stop control. What stops is everything around control: volumes, tickets, market offers, and the facts the SOC needs.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Production about $38.9 million per day (about $1.6 million per hour), Power Generation about $5.8 million per day, and Crude Logistics about $4.7 million per day from third parties.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 12 hours of a division's revenue | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot produce, generate, or move crude | One operating area, plant, or line stops | Staff slowed but working |
| Regulatory | Missed PHMSA, EPA, NERC, or SEC deadline; reportable release or reportable cyber incident | Missed internal or contractual deadline | Internal policy deviation |
| Safety and environment | Plausible injury, H2S exposure, fire, or a release reaching land or water | Degraded but safe operation | None |
| Reputation | National media, regulator attention, or loss of a major shipper | Regional media or shipper complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists **26 processes**: 7 group shared services, 8 Crude Oil Production, 5 Power Generation, and 6 Crude Logistics. **12 are High, 13 Moderate, and 1 Low.**

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, WAN, and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-PD02 Safety and environmental alarming | Production | High | 4 h | 2 h | 1 h |
| BP-PG02 Generation dispatch and market interface | Power Generation | High | 2 h | 1 h | 1 h |
| BP-PG01 Plant operations and control | Power Generation | High | 4 h | 2 h | 24 h |
| BP-ML01 Trunk line operation | Crude Logistics | High | 4 h | 2 h | 1 h |
| BP-PD01 Field production monitoring and control | Production | High | 12 h | 4 h | 1 h |
| BP-ML02 Gathering system operation and leak detection | Crude Logistics | High | 8 h | 4 h | 1 h |
| BP-PD06 Mid-Continent legacy field operations | Production | High | 12 h | 8 h | 24 h |
| BP-PD03 Water injection and disposal | Production | High | 24 h | 8 h | 4 h |
| BP-ML04 Truck dispatch and electronic run tickets | Crude Logistics | High | 24 h | 4 h | 1 h |
| BP-G04 OT remote support access | Group | Moderate | 24 h | 12 h | 24 h |
| BP-ML03 Custody transfer measurement for shippers | Crude Logistics | Moderate | 24 h | 8 h | 1 h |
| BP-PG03 Market bidding and settlement | Power Generation | Moderate | 12 h | 8 h | 4 h |
| BP-ML06 Fleet telematics and hours-of-service records | Crude Logistics | Moderate | 24 h | 12 h | 4 h |
| BP-PD04 Field data capture and volume integration | Production | Moderate | 72 h | 24 h | 4 h |
| BP-PG04 Plant maintenance and outage management | Power Generation | Moderate | 72 h | 24 h | 24 h |
| BP-PG05 NERC compliance evidence and event reporting | Power Generation | Moderate | 24 h | 12 h | 24 h |
| BP-G05 Group data platform and engineering analytics | Group | Moderate | 72 h | 24 h | 4 h |
| BP-ML05 Shipper portal and allocation statements | Crude Logistics | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-PD07 Well servicing and maintenance work orders | Production | Moderate | 72 h | 48 h | 24 h |
| BP-PD05 Hydrocarbon accounting and revenue distribution | Production | Moderate | 120 h | 72 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-PD08 Seismic and reservoir data | Production | Low | 168 h | 120 h | 24 h |

**What drives the values:**
- **Safety and the environment** drive the alarming process (BP-PD02) and the pipeline processes (BP-ML01, BP-ML02). Hardwired shutdowns still act locally, but the control room loses sight of H2S and tank alarms, and about 250 tank batteries meet the SPCC overfill rule through high-level alarms that reach SCADA (40 CFR 112.9(c)(4)(iv)). Losing those alarms means shutting in or staffing gauging rounds.
- **Reliability obligations** drive the Generation Control Center (BP-PG02, MTD 2 hours). The backup GCC function at P1 and telephone dispatch keep the plants following instructions.
- **Takeaway** links the divisions. If the trunk line stops (BP-ML01), Permian tanks fill and Production must cut rates within about 12 hours; if trucks stop (BP-ML04), leases without pipeline connections fill in 2 to 3 days.
- **Revenue more than time** drives accounting (BP-PD05) and shipper statements (BP-ML05): payments and statements can be delayed a few days with estimates.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every business process | A group identity outage stops accounting, dispatch, and bidding in all three divisions at once. Control rooms are unaffected because they use local logons |
| Shared OT support jump servers (SYS-G1) | Group | OT DMZs of all three divisions | Convenient for support; also a single path into three divisions' OT (gap 1). P08 treats it as a spread path |
| Group data platform historian connector (SYS-G6) | Group | Historian brokers in all three OT DMZs | One service account reads from and can write to all three (gap 1). Not needed for control, so Moderate; still a top risk path (P01 GR-01) |
| SOC facts (SYS-G2) | Group | Every notice in P08; NERC, PHMSA, EPA, SEC | Every notice clock depends on the SOC establishing what happened |
| Trunk line and gathering (BP-ML01, BP-ML02) | Crude Logistics | Production takeaway (BP-PD01) | About 40% of Permian crude moves on the trunk line |
| Trucks and run tickets (BP-ML04) | Crude Logistics | Production leases without pipeline connections; volumes in SYS-P3 | Custody records for trucked crude |
| Residue gas | Third-party processor (from Production associated gas) | Power Generation plants (BP-PG01) | A long Production shut-in reduces associated gas supply; plants can switch to pipeline gas |
| Water hauling | Crude Logistics | Production water disposal (BP-PD03) | Workaround when injection plants are down |

**Single points of failure found:** SYS-G1 sign-in for business processes (mitigated by break-glass accounts, tested twice in 2026); the shared OT jump servers (to be split by division, P01 GR-02); the Mid-Continent legacy SCADA servers, whose backups sit on a local device and have never been restored (P01 PD-002); and the trunk line as the main Permian takeaway (accepted for capacity reasons; contracts with a third-party pipeline cover part of the volume).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All business processes | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-P1 enterprise field SCADA | BP-PD01, BP-PD02, BP-PD03 | Hot standby servers at the BCC; historian replication; nightly offline configuration copies |
| SYS-P5 Mid-Continent legacy SCADA | BP-PD06 | Nightly backup to a local network storage device (gap 2) |
| SYS-E1 plant control systems | BP-PG01 | Redundant controllers; daily configuration backups to an offline store at each plant |
| SYS-E2 GCC | BP-PG02 | Backup GCC function in the P1 control room |
| SYS-M1 pipeline SCADA | BP-ML01, BP-ML02 | Backup PCC with replicated SCADA servers (backup test overdue, gap 4) |
| SYS-M3 shipper services platform | BP-ML04, BP-ML05 | Managed database replicas; daily immutable backups |
| People | All | Cross-trained controllers; manual operations crews; remote work for business staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, WAN, and site connectivity
3. SOC visibility (SIEM, EDR, OT sensors)
4. Safety and environmental alarming (Production)
5. Generation dispatch (GCC) and 6. plant control
7. Trunk line operation and 9. gathering and leak detection
8. Field production monitoring and control
10. Mid-Continent legacy field operations (restored only after it is cleaned and segmented)
11. Water injection and disposal
12. Truck dispatch and run tickets
13. to 26. OT remote support access (rebuilt first), measurement, market bidding, telematics, field data capture, plant maintenance, NERC evidence, the group data platform, shipper portal, financial close, well servicing, hydrocarbon accounting, payroll, and seismic data.

## 8. Key findings
1. **Control rooms are more resilient than the business around them.** Local logons and separate OT networks mean a corporate ransomware event does not stop control directly. The risk is the paths that connect IT to OT: the group data platform connector and the shared jump servers (gap 1).
2. **The Mid-Continent legacy SCADA has the weakest recovery** (RPO 24 hours, local backups, never restored). It carries about 22% of production.
3. **The backup PCC is unproven.** Its last test was 2025-04-22, and 195.446(c)(4) requires a test of backup SCADA systems at least once each calendar year at intervals not over 15 months (gap 4).
4. **Notification capacity is itself a process** (BP-G02, BP-PG05, BP-G06). NERC, PHMSA, and EPA notices can be due within an hour, so the P08 runbook keeps contact lists and forms offline at each control center.
