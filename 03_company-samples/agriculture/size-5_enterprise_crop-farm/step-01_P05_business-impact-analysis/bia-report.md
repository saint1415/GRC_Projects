# Business Impact Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm: 48 farms, 17 packing sites, and 6 irrigation control centers in FL, GA, SC, and NC) | **Tier:** Enterprise (up to 12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, field OT, and the two acquired operations. It feeds:
- the regional contingency plans, the manual irrigation and freeze-protection procedures, and the packing site downtime procedures;
- the availability and integrity ratings and recovery objectives in the FMICP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09);
- the record-retrieval objectives for Produce Safety and traceability records (P03).

**Results in one line:** 20 processes were analyzed; 9 are High criticality, 8 Moderate, and 3 Low. 5 processes need recovery within 4 hours, and freeze protection needs it within 1 hour on a freeze night. The dependency map (`dependency-map.csv`) lists 27 dependencies, 11 of them single points of failure and 3 never tested.

## 2. System and business description
Cris Santos Company farms about 310,000 acres on 48 farms in 6 regions across Florida, Georgia, South Carolina, and North Carolina. It grows fresh vegetables, berries, and melons and rotates them with peanuts, cotton, and field corn. It packs and cools produce at 14 on-farm packinghouses and 3 regional hubs, and sells mainly to national retail and foodservice customers. It has up to 12,000 employees at the seasonal peak (about 5,600 of them H-2A workers) and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: the enterprise FMIS (SYS-01), the irrigation and fertigation control system with about 45,500 OT and IoT devices (SYS-02), the identity platform (SYS-03), two public clouds and two company data center campuses (SYS-04), SD-WAN and OT DMZs (SYS-05), endpoints and rugged tablets (SYS-06), packing and cold-chain OT (SYS-07), drying OT (SYS-08), telematics and GNSS (SYS-09), drones (SYS-10), ERP and payroll (SYS-11), and sales systems (SYS-12). Two farm operations were acquired in 2025-2026 (AQ-01 and AQ-02) and are not yet integrated.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day (more than $25 million in peak harvest weeks) and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | Irrigation, harvest, packing, or shipping stops in more than one region, or more than 5 packing sites stop | One region, one service line, or up to 5 packing sites stop | Staff slowed but working |
| Regulatory | Records not produced to FDA or DOL within the required time; missed earnings statements; missed SEC filing; reportable breach of 500 or more | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible worker injury or chemical exposure (fertigation, chemigation, dryer fire, equipment) | Elevated but controlled risk | None |
| Reputation | National media, analyst action, or loss of a major retail customer | Regional media; customer complaints or fines | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-02 Freeze protection for strawberries and blueberries | High | 2 h | 1 h | 1 h | Up to $40.0M per unprotected freeze night |
| BP-01 Irrigation and fertigation operations | High | 12 h | 6 h | 1 h | $6.50M |
| BP-04 Packing, cooling, and lot labeling | High | 8 h | 4 h | 15 min | $11.00M |
| BP-05 Cold storage and cold-chain monitoring | High | 6 h | 2 h | 15 min | $3.20M |
| BP-06 Order management, EDI, and shipping | High | 12 h | 4 h | 15 min | $10.40M |
| BP-03 Harvest operations and field tally | High | 24 h | 8 h | 1 h | $5.80M |
| BP-13 Grower packing, cooling, and traceability services (SL-2) | High | 12 h | 4 h | 15 min | $0.60M |
| BP-07 Food safety and traceability records | High | 24 h | 12 h | 1 h | $0.30M |
| BP-11 Grain and peanut drying and storage | Moderate | 12 h | 6 h | 24 h | $0.90M |
| BP-08 Crop protection and nutrient application records | Moderate | 24 h | 12 h | 1 h | $0.40M |
| BP-09 Precision field operations | Moderate | 24 h | 8 h | 24 h | $1.90M |
| BP-18 Farm operations at AQ-01 and AQ-02 (legacy systems) | High | 12 h | 8 h | 1 h | $1.20M |
| BP-12 Grower data platform (SL-1) | Moderate | 24 h | 8 h | 1 h | $0.25M |
| BP-14 Payroll, timekeeping, and H-2A earnings statements | Moderate | 72 h | 48 h | 24 h | $0.35M |
| BP-15 Labor planning and H-2A program administration | Moderate | 72 h | 24 h | 24 h | $0.20M |
| BP-17 Procurement, inputs, and inventory | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-16 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-19 Direct-to-consumer produce box | Low | 72 h | 24 h | 4 h | $0.12M |
| BP-20 Water-use reporting and permit compliance | Low | 168 h | 72 h | 24 h | $0.02M |
| BP-10 Drone imaging and crop scouting | Low | 120 h | 72 h | 24 h | $0.05M |

**What drives the values:**
- **Weather and biology** set the shortest MTDs. A freeze night gives about an hour between the trigger temperature and damage (BP-02). In summer heat, produce under drip and pivots shows stress within a day (BP-01).
- **Worker safety** shapes how irrigation recovers: fertigation and chemigation stay off until the interlocks and PLC logic are verified, even when water is restored by hand.
- **Perishability and customer terms** drive packing, cooling, and shipping (BP-04 to BP-06). Retailers fine missed ship windows and reject cases without traceability labels.
- **Regulation** sets the record objectives. Offsite Produce Safety records must reach FDA within 24 hours (21 CFR 112.162(a)); application and hazard information must be displayed within 24 hours of an application (40 CFR 170.311(b)(5)); H-2A earnings statements are due each payday (20 CFR 655.122(k)); financial close tightens to 48 hours in the quarter-end window.
- **Contracts** set the SL-1 and SL-2 objectives, because external growers rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **SCADA master recovery (DEP-03).** The SCADA masters restored in 9.5 hours against a 6-hour RTO in the 2026-05-19 DR test. Regional control centers can run local schedules for about 12 hours, which covers the gap in mild weather but not during a freeze event or a heat wave. This is P01 risk R-012 and POA&M item POAM-011.
2. **Field network concentration (DEP-04).** One carrier's private APN carries about 80% of field OT traffic. A carrier outage in 2026-03 at R2 was handled by manual operation; licensed radio covers most freeze pump stations (DEP-05). This is P01 R-021.
3. **Single FMIS tenant (DEP-01).** The vendor's contract RTO (8 hours) and RPO (1 hour) meet the BIA for records and tally, and the vendor's failover test was observed in April 2026. Paper forms and monthly regional exports are the main workaround for BP-03 and BP-07.
4. **OT vendors outside the gateway (DEP-12, DEP-13, DEP-16).** INT-4, INT-5, and the AQ-02 pivot cloud service connect outside the OT remote access gateway; two packing line vendors' sessions are not recorded. These paths support freeze pump stations in R3 and all of AQ-02 (P01 R-004, R-005).
5. **Acquired operations (DEP-23, DEP-24).** AQ-01's farm servers back up nightly, so the real RPO is 24 hours against a 1-hour target, and no restore has been tested. AQ-02's pivots depend on a vendor service with a 24-hour restoration objective against the 8-hour BIA RTO.
6. **Outside the company's control (DEP-15, DEP-22).** GNSS signals and electric utilities cannot be made redundant by contract; the workarounds are procedural (manual steering, generators at packing sites and freeze stations).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Enterprise FMIS | Vendor-hosted system of record for field, application, Produce Safety, and tally records | BP-01, BP-03, BP-07, BP-08, BP-13, BP-15 |
| SYS-02 Irrigation and fertigation control | SCADA masters at DC-1 and DC-2, 6 regional control centers, about 45,500 field devices | BP-01, BP-02, BP-20 |
| SYS-03 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-04 Cloud provider A workloads | Farm data hub and historian replica, traceability data service, SL-1 platform | BP-07, BP-12, BP-13, BP-20 |
| SYS-04 Cloud provider B workloads | Imagery pipeline, AI services, data warehouse | BP-10, BP-15, BP-16 |
| SYS-04 DC-1 and DC-2 | SCADA masters, OT DMZ, network core, offline backup copies | BP-01, BP-02; recovery of all |
| SYS-05 SD-WAN, APN, licensed radio, LoRaWAN | Site and field connectivity | All site and field processes |
| SYS-06 Endpoints and rugged tablets | Office, packing, and field devices | BP-03, BP-04, BP-08 |
| SYS-07 Packing and cold-chain OT | Packing lines, graders, refrigeration controllers, label printers | BP-04, BP-05, BP-13 |
| SYS-08 Drying OT | Dryer and bin controls | BP-11 |
| SYS-09 Telematics, GNSS, RTK | Guidance and as-applied data | BP-08, BP-09 |
| SYS-11 ERP and payroll | Finance, payroll, HR, H-2A records | BP-14 to BP-17 |
| SYS-12 Sales systems | EDI, order management, transport management, e-commerce | BP-06, BP-19 |
| Backups | Immutable cloud backups in separate accounts (RPO for Cloud A and B workloads); SCADA configuration and PLC program library replicated between DC-1 and DC-2 every hour (RPO 1 h for BP-01 and BP-02); packing site databases replicated to DC-2 every 15 minutes (RPO for BP-04, BP-05, BP-13) | RPO for all |
| People | Irrigation technicians and freeze crews, crew leads, packing staff, SOC, SCADA engineering, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual irrigation and freeze crews (people first, not systems) | Immediate | Written manual procedures; standalone alarm dialers |
| 2 | SYS-03 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 3 | Network core, SD-WAN, OT DMZ firewalls, DNS | 2 h | Cellular failover at sites; OT zones isolated |
| 4 | Security tooling (EDR console, SIEM, OT monitoring) for clean-room validation | 2 h | MSSP tooling |
| 5 | Packing site systems, label printing, and cold-chain alarm path | 4 h | Manual packing mode; pre-printed lot labels; hourly temperature checks |
| 6 | EDI, order management, and transport management | 4 h | Phone and email orders for the top 20 customers |
| 7 | SCADA masters and regional control center HMIs (verified PLC logic before automatic control) | 6 h (9.5 h demonstrated) | Local schedules at control centers; manual operation |
| 8 | FMIS access, tally, and Produce Safety records (vendor-hosted) | 8 h (vendor) | Paper forms; monthly exports |
| 9 | Traceability data service and SL-2 hub data | 8 h | Paper receiving and lot logs |
| 10 | Drying controls and telematics | 8 h | Local panels; manual steering |
| 11 | AQ-01 and AQ-02 systems | 8 h target (24 h actual) | Manual pivots; paper tally |
| 12 | SL-1 grower data platform | 8 h | Status page; email reports |
| 13 | ERP and payroll | 48 h | Repeat prior payroll |
| 14 | Data warehouse, AI services, imagery pipeline, produce box | 72 h | Last exports; skip one produce box cycle |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| SCADA master recovery 9.5 h against a 6 h RTO | P01 R-012; P02 CP-10 and CP-10(4); POAM-011 |
| Single carrier APN for about 80% of field OT | P01 R-021; P03 G-102 |
| OT vendors outside the remote access gateway (INT-4, INT-5, AQ-02 pivot cloud, packing line vendors) | P01 R-004, R-005; POAM-002, POAM-004 |
| AQ-01 nightly backups and untested restore (RPO 24 h against 1 h) | P01 R-019; POAM-017 |
| Cold-chain monitoring SaaS without a SOC report | P01 R-030; POAM-015 |
| Traceability records not yet producible as a sortable spreadsheet within 24 hours for all FTL foods | P01 R-026; P03 G-126 to G-133; POAM-020 |
