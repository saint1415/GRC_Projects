# Business Impact Analysis: Cris Santos Company Holdings | Agriculture | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees at seasonal peak) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 (off-season for Florida strawberries) | **Approved:** board risk committee, 2026-09-10
**Sources:** process owner interviews by division, 2026-05-04 to 2026-05-29 (EV-074 group, EV-075 Crop Farming, EV-076 Food Processing, EV-077 Farm Supply), FY2025 revenue by division (EV-003), workforce and H-2A counts (EV-002), farm scale and freeze protection acreage (EV-034), backup and recovery records (EV-021, EV-047, EV-060, EV-062), and recovery and notice terms (EV-049, EV-050, EV-065, EV-069, and the FMIS vendor's SOC 2 report, EV-078). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the board risk committee.

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, ERP, payroll and HR, financial close).
- **Division BIAs:** Crop Farming (focus division), Food Processing, and Farm Supply. They are kept as rows in one workbook (`bia.csv`, `division` column) so the dependencies along the chain from field to packed product to farm inputs are visible in one place.

It supports:
- the availability rating of the Farm Management and Irrigation Control Platform (FMICP) in the SSP (P02) and the impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08), including the order in which farm OT, plant OT, and corporate systems come back;
- the records-availability duties that continue during an outage: Produce Safety records (21 CFR 112.166), food safety and food defense records (21 CFR 117.315(c); 121.315(c)), records access for FDA (21 CFR 1.361), and H-2A earnings records and statements (20 CFR 655.122(j)-(k));
- the Grower Agronomy Portal's availability commitments, which matter for its SOC 2 readiness (P09).

## 2. System and business description
Corporate shared services run SYS-G1 (identity), SYS-G2 (SOC, SIEM, EDR, passive OT monitoring), SYS-G3 (cloud platform on two providers, WAN, and group data platform), and SYS-G4 (ERP on cloud IaaS and the HR and payroll SaaS). Division systems are SYS-D1 (the FMICP: FMIS tenant, 3 regional irrigation operations centers (ROCs) with SCADA, field OT at 38 farms, farm data hub, imagery store), SYS-D2 (connected equipment, GNSS guidance, and drones), SYS-D3 (plant MES and OT, ammonia refrigeration controls, quality and food defense records, traceability, warehouse management), SYS-D4 (branch POS, e-commerce, distribution center warehouse management, blending plant controllers), and SYS-D5 (Grower Agronomy Portal). The full list, with the evidence behind each entry, is in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

## 3. Impact categories and values
Dollar values use the FY2025 revenue by division (EV-003) divided by 365 days: Food Processing about $10.6 billion, or about $29 million per day; Farm Supply about $4.8 billion, or about $13 million per day (concentrated in planting season); and Crop Farming about $4.1 billion including intercompany sales, or about $11 million per day (concentrated in the harvest season; the strawberry crop alone is worth about $310 million a season, EV-034).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue, or loss of a season's crop on a block | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core output (irrigated crop, packed product, inputs to growers) | One farm, plant, region, or service stops | Staff slowed but working |
| Regulatory | Missed FDA records request, food released without required monitoring records, reportable release, missed SEC or state breach deadline | Missed contractual notice (buyer, customer, cooperative) | Internal policy deviation |
| Safety | Plausible harm to workers, consumers, or the community (unexpected pump or pivot start, ammonia release, adulterated food) | Degraded but controlled conditions | None |
| Reputation | National media, loss of major retail customers or cooperatives, regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 8 Crop Farming, 6 Food Processing, and 6 Farm Supply. 16 are High, 10 Moderate, and 1 Low. Rows are in recovery priority order.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-CF01 Irrigation and freeze protection control | Crop Farming | High | 4 h | 2 h | 1 h |
| BP-FP02 Ammonia refrigeration and cold storage | Food Processing | High | 4 h | 2 h | 1 h |
| BP-FP01 Plant production lines | Food Processing | High | 8 h | 4 h | 1 h |
| BP-CF06 Cold chain monitoring at farm packing sheds and field coolers | Crop Farming | Moderate | 8 h | 4 h | 1 h |
| BP-FP03 Food safety and food defense monitoring records | Food Processing | High | 24 h | 8 h | 1 h |
| BP-CF03 Harvest tally, labor, and H-2A earnings records | Crop Farming | High | 24 h | 8 h | 1 h |
| BP-CF04 Harvest lot records and shipping | Crop Farming | High | 24 h | 8 h | 4 h |
| BP-FP04 Traceability and FDA records access | Food Processing | High | 24 h | 8 h | 4 h |
| BP-FP05 Order fulfillment and shipping | Food Processing | High | 24 h | 8 h | 1 h |
| BP-FS02 Distribution center warehouse management and delivery | Farm Supply | High | 24 h | 8 h | 1 h |
| BP-FS01 Branch ordering and point of sale | Farm Supply | High | 24 h | 8 h | 1 h |
| BP-FS04 Grower Agronomy Portal | Farm Supply | High | 24 h | 8 h | 1 h |
| BP-G05 ERP order-to-cash and procure-to-pay | Group | High | 48 h | 24 h | 1 h |
| BP-CF02 Fertigation and chemigation control | Crop Farming | Moderate | 72 h | 24 h | 1 h |
| BP-CF05 Produce Safety, field, and pesticide application records | Crop Farming | Moderate | 72 h | 24 h | 4 h |
| BP-FS03 Liquid fertilizer blending | Farm Supply | Moderate | 48 h | 24 h | 4 h |
| BP-FS06 E-commerce ordering | Farm Supply | Moderate | 48 h | 24 h | 4 h |
| BP-FP06 Grower receiving and settlement | Food Processing | Moderate | 72 h | 24 h | 4 h |
| BP-CF07 Precision equipment guidance and drone operations | Crop Farming | Moderate | 72 h | 24 h | 24 h |
| BP-G06 Payroll and HR, including H-2A records | Group | Moderate | 72 h | 48 h | 24 h |
| BP-FS05 Grower credit and accounts receivable | Farm Supply | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-CF08 Crop yield forecasting (AI-001) | Crop Farming | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Freeze nights** drive the shortest farm values (BP-CF01). From about December to February, overhead irrigation protects about 4,200 acres of strawberries. ROC-1 operators start it from SCADA at a trigger temperature; if SCADA is lost, crews must start each system by hand. The 4-hour MTD applies in freeze season; the rest of the year it is about 24 hours. The FMIS vendor's stated RTO of 8 hours is longer than this, which is why ROC SCADA, not the FMIS, must be able to run irrigation on its own (P02).
- **Integrity, not availability, drives fertigation** (BP-CF02). Turning injection off is the safe state, so its availability rating is Moderate. A wrong rate is the real danger, and that is rated in P02 and P01, not here.
- **Worker and community safety** drive ammonia refrigeration (BP-FP02): the two frozen vegetable plants run EPA Risk Management Program and OSHA Process Safety Management processes (anhydrous ammonia above the 10,000 lb threshold in 40 CFR 68.130 and 29 CFR 1910.119 Appendix A). Licensed operators can run the system at the panels, so the control system RTO is 2 hours, but no remote command may be trusted after a compromise until it is verified.
- **Records that must exist at the time of the activity** drive Food Processing monitoring records (BP-FP03) and Crop Farming tally (BP-CF03). Paper is an acceptable workaround only if it captures the same fields and is signed by the person who did the work.
- **24-hour clocks** drive harvest lot records and traceability (BP-CF04, BP-FP04): buyers and customers expect notice within 24 hours, and FDA can require records within 24 hours (21 CFR 1.361).
- **Revenue more than time** drives ERP, credit, and settlements (BP-G05, BP-FS05, BP-FP06): orders can ship on paper, and invoices and settlements can lag a few days.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. ROC HMIs and the farm operations directory still sign in locally, which keeps irrigation running but sits outside group PAM (P02 gap) |
| Farm data hub on the corporate cloud network | Crop Farming | Group cloud platform | Telemetry, harvest lot files, and payroll tally all flow through it. It also gives a network path from the corporate cloud into ROC SCADA (P01 CF-004, GR-01) |
| Harvest lot file (nightly) | Crop Farming | Food Processing traceability (BP-FP04) | About 40% of Food Processing produce and peanuts come from group farms. Nobody has tested producing traceability records for FDA within 24 hours while the hub is down (EV-045, EV-062) |
| Payroll tally export | Crop Farming | Group payroll (BP-G06) | H-2A earnings statements depend on accurate tally reaching payroll each week |
| Inputs (seed, fertilizer, crop protection, irrigation parts) | Farm Supply | Crop Farming (BP-CF02, BP-CF07) | A distribution center outage in planting season delays group farms as well as outside growers |
| Yield estimates (AI-001) | Crop Farming | Food Processing production plans; forward sales; financial close (BP-G07) | Not time critical (Low), but errors spread to three functions without change control (P10) |
| SOC facts | Group | Every notice in P08 | Every notice clock depends on the SOC establishing what happened, including in farm OT where monitoring covers only 9 of 38 farms |
| ERP orders and payables | Group | Food Processing shipping; Farm Supply sales; grower settlement | Paper workarounds hold for about 2 days |

**Single points of failure found:**
- **ROC-1** controls freeze protection for all Florida strawberries. There is no warm standby for its SCADA servers (P01 CF-003; POAM-008).
- **The FMIS vendor** serves all 38 farms from one tenant (P01 CF-011). Its SOC 2 report (P09) supports the stated RTO of 8 hours and RPO of 1 hour, but the farms keep no copy of their own records.
- **The legacy farm operations directory** authenticates every ROC HMI and SCADA server (P01 CF-002).
- **One refrigeration contractor** supports both frozen vegetable plants remotely (P01 FP-002), mitigated by group PAM and on-site licensed operators.

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B, restore-tested quarterly |
| SYS-G4 ERP (cloud IaaS) | BP-G05, BP-FS05, BP-FP06 | Database log shipping to provider B; immutable daily backups |
| FMIS tenant (vendor SaaS) | BP-CF01 (schedules), BP-CF03, BP-CF04, BP-CF05 | Vendor replication (RPO 1 hour per its SOC 2 report). No farm-held export yet (POAM-013) |
| ROC SCADA servers and HMIs | BP-CF01, BP-CF02 | Weekly image backups to a server in the same ROC; PLC and controller programs held partly by the integrator (acquired farms). Not immutable (POAM-008, POAM-013) |
| Farm data hub and imagery store (provider A) | BP-CF04, BP-CF08, BP-G06 feed | Daily backups to the provider B vault |
| Plant MES, OT, and ammonia refrigeration controls | BP-FP01, BP-FP02 | Versioned PLC and HMI backups in the plant OT backup server, tested yearly |
| Traceability system (provider A) | BP-FP04 | Daily immutable backups; DR replica in provider B |
| Grower Agronomy Portal (provider B) | BP-FS04 | Database replicas across zones; daily backups |
| People | All | Licensed refrigeration operators on every shift; freeze-night crews at ROC-1 farms; paper procedures in farm and plant binders |

## 7. Recovery priorities
The full order is in `bia.csv` (`recovery_priority`). In short:
1. to 4. Identity and break-glass access, cloud hubs, WAN, and SOC visibility.
5. Irrigation and freeze protection (in freeze season it may be run by hand before anything else is restored; people first).
6. Ammonia refrigeration control, verified before any remote command is trusted.
7. to 13. Plant production lines, farm cold chain, food safety monitoring records, harvest tally, harvest lot records, traceability, and Food Processing shipping.
14. to 16. Farm Supply distribution, branch sales, and the Grower Agronomy Portal (the portal runs in provider B and often recovers in parallel).
17. to 27. ERP, fertigation (returns last on each farm, after a supervised low-rate test), Produce Safety records, blending, e-commerce, grower receiving, equipment and drones, payroll, credit, financial close, and the yield model.

## 8. Key findings
1. **Shared services have the shortest RTOs, as they must.** The group identity RTO of 1 hour was met in two 2026 tests. The farm OT estate is the exception: ROC SCADA signs in through a legacy directory that has never been included in those tests.
2. **The FMICP's availability depends on ROC SCADA, not on the cloud.** The FMIS vendor's RTO of 8 hours and the cloud hub's RTO of 2 hours are both longer than the 4-hour freeze-season MTD for BP-CF01. Irrigation must keep running from the ROCs, or by hand, when both are down.
3. **ROC-1 is a single point of failure for the strawberry crop** and has no tested failover (POAM-008).
4. **Traceability crosses divisions and has never been tested under outage** (BP-CF04 to BP-FP04). Producing records within 24 hours (21 CFR 1.361) with the farm data hub down depends on paper lot tags at 38 farms.
5. **Notice capacity is itself a process** (BP-G02, BP-G07, BP-FS04). If the SOC or email is down during an incident, buyer, customer, cooperative, and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
