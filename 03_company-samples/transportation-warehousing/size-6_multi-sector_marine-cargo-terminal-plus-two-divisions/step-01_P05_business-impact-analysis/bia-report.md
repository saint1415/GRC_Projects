# Business Impact Analysis: Cris Santos Company Holdings | Transportation and Warehousing | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. (port logistics group) | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads, the Marine Terminals Division Cybersecurity Officer (CySO) and the nine Facility Security Officers (FSOs) | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform, WAN and backup vault (SYS-G3), the B2B integration hub (SYS-G4), ERP and payroll (SYS-G5) and the productivity suite (SYS-G6).
- **Division BIAs:** Marine Terminals (focus), Freight Trading and Port Real Estate. They are kept as rows in one workbook (`bia.csv`, `division` column) so that cross-division dependencies are visible in one place.

It supports:
- the resilience measures in the USCG cyber rule for all 9 terminals: protected and tested backups of critical IT and OT systems (33 CFR 101.650(g)(4)) and the Cyber Incident Response Plan (101.650(g)(2)). It also gives the first Cybersecurity Assessments, due 2027-07-16 (101.650(e)(1)), a view of which systems are critical IT or OT systems (101.615);
- the group contingency plan and the division contingency plans (P02 CP-2);
- the availability and integrity ratings in the SSP for the Terminal Operations Platform (P02 section 6);
- impact ratings in the group and division risk registers (P01) and the recovery order in the incident runbook (P08);
- the Freight Trading division's incident reporting readiness under its DoD contracts (DFARS 252.204-7012), and the group's SEC disclosure controls (Form 8-K Item 1.05).

## 2. System and business description
Three divisions share corporate services. Marine Terminals runs 9 terminals at 5 ports in Florida, Georgia, Louisiana and Texas: T1 to T6 on the standard terminal operating system (SYS-T1, in cloud provider A) and T7 to T9, the Gulf terminals acquired in 2024, on a legacy TOS on local servers (SYS-T1L). Gate automation (SYS-T2), crane and yard equipment OT (SYS-T3), site networks (SYS-T4), the berth and yard optimization service (SYS-T5) and the customer portal (SYS-T6) complete the terminal estate. Freight Trading runs its commodity trading platform (SYS-F1), 38 distribution yards (SYS-F2) and a federal sales workspace (SYS-F3). Port Real Estate runs property management (SYS-R1) and building systems at 46 warehouses and 3 yards (SYS-R2). See `../00_company-facts.md` section 3 and the SSP (P02).

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Marine Terminals about $9.3 million per day, Freight Trading about $37 million per day (mostly pass-through commodity cost, so margin at risk is far smaller), and Port Real Estate about $2.7 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's gross margin | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (vessels and gates, trading and yards, building security) | One terminal, port, region or service line stops | Staff slowed but working |
| Regulatory | A transportation security incident, a failure of FSP access control, a container released while on a customs hold, a missed Coast Guard, DoD or SEC reporting duty | A missed internal, contractual or record-keeping deadline | Internal policy deviation |
| Safety | Plausible injury: unsafe crane, ASC or RTG motion, a hazardous container mis-stowed or lost, responders unable to locate hazardous cargo, building life-safety systems down | Unsafe conditions controlled by stopping work | None |
| Reputation | A carrier moves a service to a competing terminal, national media, regulator attention or a Federal Maritime Commission complaint | Regional media or complaints from carriers, truckers or tenants | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists **26 processes**: 7 group shared services, 10 Marine Terminals, 4 Freight Trading and 5 Port Real Estate. **13 are High, 12 Moderate and 1 Low.**

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G02 Cloud landing zones, WAN and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-MT04 Facility security, access control and hazardous cargo control | Marine Terminals | High | 4 h | 2 h | 1 h |
| BP-G03 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 B2B integration hub | Group | High | 8 h | 4 h | 1 h |
| BP-MT01 Vessel operations (discharge and load) | Marine Terminals | High | 8 h | 4 h | 1 h |
| BP-MT02 Truck gate processing | Marine Terminals | High | 8 h | 4 h | 1 h |
| BP-MT05 Crane, ASC and yard equipment OT | Marine Terminals | High | 8 h | 4 h | 24 h |
| BP-MT09 Gulf terminal operations on the legacy TOS (T7 to T9) | Marine Terminals | High | 8 h | 4 h | 1 h |
| BP-RE01 Building access control and CCTV | Port Real Estate | High | 8 h | 4 h | 24 h |
| BP-MT03 Yard and equipment operations | Marine Terminals | High | 12 h | 6 h | 1 h |
| BP-FT01 Commodity trading, orders and order-to-cash | Freight Trading | High | 24 h | 8 h | 1 h |
| BP-FT02 Distribution yard shipping and receiving | Freight Trading | High | 24 h | 12 h | 4 h |
| BP-MT06 Customs status and carrier EDI | Marine Terminals | Moderate | 12 h | 8 h | 4 h |
| BP-G07 Email, files and collaboration | Group | Moderate | 24 h | 8 h | 4 h |
| BP-MT08 Truck appointments and customer portal | Marine Terminals | Moderate | 24 h | 8 h | 4 h |
| BP-RE05 Truck staging and container depot yards | Port Real Estate | Moderate | 24 h | 8 h | 4 h |
| BP-RE02 Building management systems | Port Real Estate | Moderate | 24 h | 8 h | 24 h |
| BP-MT07 Vessel, berth and yard planning | Marine Terminals | Moderate | 24 h | 12 h | 4 h |
| BP-FT03 Procurement and import logistics | Freight Trading | Moderate | 48 h | 24 h | 4 h |
| BP-FT04 Federal (DoD) order fulfillment | Freight Trading | Moderate | 72 h | 24 h | 24 h |
| BP-RE03 Lease administration, rent billing and tenant portal | Port Real Estate | Moderate | 72 h | 24 h | 24 h |
| BP-G06 Financial close, treasury and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-RE04 Property acquisitions, closings and wire payments | Port Real Estate | Moderate | 72 h | 48 h | 24 h |
| BP-G05 Payroll and HR, including longshore payroll | Group | Moderate | 120 h | 72 h | 24 h |
| BP-MT10 Terminal billing, demurrage and collections | Marine Terminals | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Safety and security drive BP-MT04.** FSOs and responders must be able to find hazardous cargo at any time, and FSP access control must continue at every MARSEC level. The dangerous cargo list is printed at every shift change at T1 to T6; at T7 to T9 it exists only in the legacy TOS (P01 MT-023).
- **The berth window drives BP-MT01, BP-MT05 and BP-MT09.** A vessel works for about 18 to 36 hours. Past one shift of manual working the carrier misses its window and the next port call, and with about 55 calls a week across the group a one-day outage at all terminals affects most of the group's carrier customers at once.
- **Road congestion and customs holds drive BP-MT02.** Trucks back up onto port roads within about 2 hours. The gate can run manually on reduced lanes, but only for containers confirmed released.
- **The T5 automated stack has no manual mode.** The 48 automated stacking cranes need the equipment control system and the TOS link. If either is down, T5 stops and vessels shift to T6 where berth space allows (BP-MT03).
- **The integration hub carries three divisions' clocks (BP-G04).** Customs status for the gates, carrier messages, trading orders and tenant rent files all pass through SYS-G4. Partners can resend recent messages, so its RPO matters less than its RTO.
- **Trading positions drive BP-FT01's RPO of 1 hour.** Trades must not be lost even though the order desk can work from paper for a day.
- **Building security drives BP-RE01.** Tenants store high-value cargo, and the container freight station at T3 is inside a regulated secure area. Doors fail secure and guards stand in, so the MTD is 8 hours.
- **The OT RPO is a program version, not hours of data** (BP-MT05, BP-RE01). PLC programs, HMI settings and access controller configurations change rarely; the RPO means the last approved version must be held by the company, not only by vendors and integrators.
- **Revenue more than time drives billing, rent and payroll** (BP-MT10, BP-RE03, BP-G05). Longshore payroll is the exception within payroll: a missed weekly run risks a work stoppage, which is why its reputation impact is Severe.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system, held by each terminal FSO, are the fallback |
| WAN and provider A hub (SYS-G3) | Group | T1 to T6, SYS-T6, Freight Trading and Port Real Estate SaaS | The standard TOS is only as available as the terminal links and the cloud hub |
| B2B integration hub (SYS-G4) | Group | Customs status and carrier EDI (BP-MT06), gates (BP-MT02), trading orders (BP-FT01, BP-FT03), tenant rent files (BP-RE03), depot yards (BP-RE05) | One hub for three divisions. It is the start point of the P08 incident and a single point of failure (P01 GR-16) |
| SOC facts (SYS-G2) | Group | Coast Guard reports for each terminal, DoD reports, SEC filing, state notices | Every notice clock in P08 depends on the SOC establishing what happened. The Gulf terminals are blind spots (local logs only) |
| Group terminals | Marine Terminals | Freight Trading imports (BP-FT03) | About 30% of Freight Trading tonnage moves through group terminals. The terminal must treat it like any other cargo owner (scenario gap 1) |
| T3 PACS | Marine Terminals | Port Real Estate container freight station (BP-RE01) | The CFS warehouse inside the T3 secure area reports to the T3 PACS and is covered by the T3 FSP |
| Truck appointment system (SYS-T6) | Marine Terminals | Depot yards (BP-RE05); Freight Trading truckers | Empty returns and trading deliveries are booked through the same portal |
| Leased warehouses | Port Real Estate | Freight Trading (9 warehouses) | Building access and BMS outages affect an internal tenant as well as about 180 external tenants |
| ERP and treasury (SYS-G5) | Group | All divisions; closings (BP-RE04) | Payments, longshore payroll and SEC reporting |

**Single points of failure found:**
- SYS-G1 identity (mitigated by break-glass accounts, tested quarterly);
- the SYS-G4 integration hub for three divisions (P01 GR-16);
- one customs data exchange service provider for all 9 terminals (P01 MT-014 covers the integrity side);
- the T5 equipment control system, whose restore has never been tested (P01 MT-013);
- a single region of provider A for SYS-T1 and SYS-T6, with disaster recovery in provider B (P01 MT-026).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | All cloud-hosted processes | Infrastructure as code; immutable backups in the provider B vault |
| SYS-G4 integration hub (provider A) | BP-G04, BP-MT06, BP-FT01, BP-RE03 | Configuration backups daily; message stores replicated to provider B; full rebuild never tested (P01 GR-16) |
| SYS-T1 standard TOS (provider A) | BP-MT01 to BP-MT08 at T1 to T6 | Database replica in provider B; immutable backups every hour; quarterly restore tests since 2025 |
| SYS-T1L legacy TOS (local servers at T7 to T9) | BP-MT09 | Nightly backups to local disk at each terminal; no offsite or immutable copy (P01 MT-004) |
| SYS-T2 gate servers and OCR | BP-MT02 | Gate server images backed up weekly at T1 to T6; configurations not backed up at T7 to T9 |
| SYS-T3 PLC and HMI programs; T5 equipment control system | BP-MT05, BP-MT03 | Approved program versions held in the OT repository at T1 to T6; held only by vendors at T7 to T9; T5 equipment control system backed up nightly, restore not tested (P01 MT-013) |
| SYS-F1 CTRM and ERP extension (SaaS) | BP-FT01, BP-FT03 | Vendor replication; daily export to the provider B vault |
| SYS-F2 yard system (SaaS) and scale PCs | BP-FT02 | Vendor replication |
| SYS-R1 property management (SaaS) | BP-RE03 | Vendor replication; monthly rent roll export |
| SYS-R2 building systems | BP-RE01, BP-RE02, BP-RE05 | Controller configurations held by the 5 integrators only |
| People | All | Cross-trained planners and superintendents across the two Florida ports; longshore labor through the hiring halls; FSOs and security officers per terminal |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, WAN and the provider A hub, with OT zones isolated
3. SOC visibility (SIEM and EDR)
4. Facility security, PACS and the printed dangerous cargo lists at every terminal
5. Crane, ASC and yard equipment OT verified clean and reconnected (cranes run in local mode meanwhile)
6. to 7. Vessel operations and yard operations at T1 to T6
8. The B2B integration hub (rebuilt clean if it was the point of entry, as in P08)
9. to 11. Truck gates, the Gulf terminals on the legacy TOS, and customs status and carrier EDI
12. Port Real Estate building access control and CCTV
13. to 14. Freight Trading trading desk and distribution yards
15. to 26. Email, the customer portal, planning, depot yards, building management, procurement, finance and SEC reporting, federal orders, leases and rent, payroll, closings and terminal billing.

## 8. Key findings
1. **Shared-service RTOs are shorter than any division's**, as they must be. The group identity RTO of 1 hour was met in two tests in 2026. The integration hub's 4-hour RTO has not been tested by a full rebuild (P01 GR-16).
2. **The Gulf terminals cannot meet their RPO.** BP-MT09 needs no more than 1 hour of data loss; nightly backups to local disk give 24 hours at best, and a ransomware actor with domain rights could destroy them (P01 MT-004, scenario gap 2). Migration to SYS-T1 by 2027-06-30 fixes this; an interim offsite immutable copy is due 2026-12-31.
3. **The T5 automated stack is the least resilient operation.** It has no manual mode and its equipment control system restore has never been tested (P01 MT-013).
4. **Building systems recovery depends on outside integrators.** Port Real Estate does not hold the configurations of its access control or BMS controllers (P01 RE-002, scenario gap 5).
5. **Notification capacity is itself a process** (BP-G03, BP-G06, BP-G07). If the SOC or email is down during an incident, the Coast Guard, DoD and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
