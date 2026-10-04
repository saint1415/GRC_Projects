# Business Impact Analysis: Cris Santos Company Holdings | Food and Agriculture | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and the Group Chief Food Safety and Quality Officer | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity and the corporate directory, the SOC, cloud and WAN, the cold-chain monitoring platform, the group ERP, OT security services, and payroll and finance.
- **Division BIAs:** Meat Processing (focus), Food Distribution, and Grocery Retail. They are rows in one workbook (`bia.csv`, `division` column) so the dependencies along the group's own supply chain (plant to DC to store) are visible in one place.

It supports:
- HACCP corrective action planning for unforeseen deviations at each plant (9 CFR 417.3(b)), because a control-system or monitoring outage is one;
- the DCs' temperature control, corrective action, and verification duties for refrigerated packaged food (21 CFR 117.206(a)) and sanitary transportation temperature control (21 CFR 1.908);
- the availability commitments of the Food Distribution 3PL service (P09);
- impact ratings in the risk registers (P01), the availability rating of the PPCM in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Six plants, five DCs with a refrigerated fleet, and 120 stores share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and colocation, SYS-G4 ERP, SYS-G5 OT security services, and SYS-G6 cold-chain monitoring. Division systems are SYS-M1 to SYS-M6 (plants), SYS-D1 to SYS-D3 (distribution), and SYS-R1 to SYS-R3 (stores). See `../00_company-facts.md` sections 1, 3, and 7.

**What is different about a food supply chain.** Downtime is not only lost revenue. Product that sits in a smokehouse, cooler, trailer, or display case while controls or monitoring are down may have to be held, evaluated, and possibly destroyed, and plant product cannot ship without complete CCP records (9 CFR 417.5(c)). Recovery objectives are set so that product can be protected, not only so that systems come back.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Meat Processing about $28 million per production day (250 days), Food Distribution about $16 million per day, and Grocery Retail about $16.5 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 1 day of a division's revenue | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot deliver its core service (production, deliveries, store sales) | One plant, DC, region, or line stops | Staff slowed but working |
| Regulatory | Adulterated product in commerce, FSIS or FDA action, reportable breach, or SEC disclosure | Missing or late required records; contractual breach (acquirer, 3PL customer) | Internal procedure deviation |
| Safety | Plausible consumer illness (temperature abuse, undercooking, cure error) or worker harm (ammonia) | Product held for evaluation | None |
| Reputation | Recall with public notice, national media, or loss of a major customer | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 25 processes: 7 group shared services, 8 Meat Processing, 5 Food Distribution, and 5 Grocery Retail. 16 are High, 8 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G04 Cold-chain monitoring and alerting service | Group | High | 2 h | 1 h | 15 min |
| BP-M08 Ammonia refrigeration control | Meat Processing | High | 2 h | 1 h | 24 h |
| BP-M01 Plant cold storage temperature control and monitoring | Meat Processing | High | 2 h | 1 h | 15 min |
| BP-D01 DC refrigerated and frozen storage temperature control | Food Distribution | High | 2 h | 1 h | 15 min |
| BP-R02 Store refrigerated case and walk-in monitoring | Grocery Retail | High | 2 h | 1 h | 15 min |
| BP-G01 Workforce identity and directory | Group | High | 4 h | 2 h | 1 h |
| BP-G03 Cloud landing zones, colocation data center, and WAN | Group | High | 4 h | 2 h | 1 h |
| BP-R01 Store checkout and card payments | Grocery Retail | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-M02 Cooking, smoking, and chilling (thermal CCPs) | Meat Processing | High | 8 h | 4 h | 1 h |
| BP-D03 Refrigerated transportation | Food Distribution | High | 8 h | 4 h | 1 h |
| BP-M03 Formulation, curing, and brine dosing | Meat Processing | High | 12 h | 8 h | 24 h |
| BP-M04 Processing, packaging, lot coding, and labeling | Meat Processing | High | 12 h | 8 h | 4 h |
| BP-D02 Order picking and shipping | Food Distribution | High | 12 h | 8 h | 1 h |
| BP-G05 Group ERP: orders, production orders, and procurement | Group | High | 24 h | 8 h | 1 h |
| BP-M05 Food safety records and pre-shipment review | Meat Processing | High | 24 h | 12 h | 1 h |
| BP-M07 Traceability and recall | Meat Processing | Moderate | 24 h (4 h during a recall) | 8 h | 24 h |
| BP-D05 Receiving and regulatory records | Food Distribution | Moderate | 24 h | 12 h | 4 h |
| BP-R05 Store replenishment and meat-counter records | Grocery Retail | Moderate | 24 h | 12 h | 4 h |
| BP-M06 Plant-based protein production (Plant 6) | Meat Processing | Moderate | 24 h | 12 h | 4 h |
| BP-R03 Online ordering, pickup, and delivery | Grocery Retail | Moderate | 24 h | 8 h | 1 h |
| BP-D04 3PL customer service | Food Distribution | Moderate | 24 h | 12 h | 1 h |
| BP-G06 OT remote access and OT monitoring | Group | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Payroll, HR, financial close, and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-R04 Loyalty program, pricing, and promotions | Grocery Retail | Low | 48 h | 24 h | 4 h |

**What drives the values:**
- **Food safety drives the 2-hour MTDs.** Refrigeration keeps running on local controllers when supervisory systems fail, but *knowing* the temperature does not. A plant monitoring gap of more than 2 hours means FSQA must evaluate every lot in storage (9 CFR 417.3(b)); at a DC, a loss of temperature control that may affect safety requires corrective action and evaluation of all affected food (21 CFR 117.206(a)(3)). Hourly manual readings keep the gap closed.
- **BP-M03 has a long RPO but a hard integrity requirement.** The last approved formulation release is an acceptable recovery point. Restored recipes must be *verified* against the signed master before any dosing, because a changed cure setpoint is exactly what an attacker would leave behind (P01 MT-003).
- **BP-M05 gates shipping** from all six plants. Product can wait in the cooler for a day but cannot ship without pre-shipment review.
- **Store checkout (BP-R01) drives the shortest revenue clock.** Lanes can run store-and-forward for a limited time, and the CDE must stay segmented during recovery, so recovery cannot cut corners on PCI DSS scope.
- **BP-M07 changes during a recall.** The 24-hour FSIS clock (9 CFR 418.2) means lot tracing across plants, DCs, and stores must be available within hours.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Corporate directory (SYS-G1) | Group | Every process; OT at Plants 2 and 5; DC automation | A directory compromise reaches plant OT at two plants and DC automation directly. This is the path the P08 scenario uses |
| Cold-chain alert integration server (SYS-G6) | Group | Plant cold storage, DC rooms, trailers, store cases | One server routes every alert in all three divisions. Its loss blinds all 6 plants, 5 DCs, 900 trailers, and 120 stores at once |
| Group ERP (SYS-G4) | Group | MES production orders, WMS, store replenishment | Plants 1, 3, 4, and 6 keep running on standing schedules for about 24 hours |
| Plant output to DCs | Meat Processing | Food Distribution | About 30% of Meat Processing volume ships through the group's DCs |
| DC deliveries to stores | Food Distribution | Grocery Retail | Stores carry 1 to 3 days of perishables; about 40% of store fresh and deli meat comes from the group's plants |
| Lot data across the chain | All divisions | Traceability and recall (BP-M07) | A recall needs plant lots, DC shipments, and store receiving records together |
| SOC facts (SYS-G2) | Group | FSIS, FDA, state breach, acquirer, and SEC notices | Every clock in P08 depends on the SOC establishing what happened |

**Single points of failure found:** the cold-chain alert integration server (no tested failover; P01 GR-02); the corporate directory for OT at Plants 2 and 5 and DC automation (P01 GR-01); one controls integrator for Plants 2 and 5 (P01 MT-006).

## 6. Resource requirements
| Resource | Supports | Recovery method |
|---|---|---|
| SYS-G1 directory and SSO | All | Directory restore from offline system-state backups (tested once, 2025); cloud SSO vendor multi-region service |
| SYS-G6 cold-chain platform | BP-G04, BP-M01, BP-D01, BP-D03, BP-R02 | Vendor SaaS; gateways buffer 24 hours locally; integration server rebuilt from code (**no tested failover**) |
| SYS-M1, SYS-M2 plant OT | BP-M02 to BP-M04 | PLC program repository and offline OT backups at Plants 1, 3, 4, and 6 (restored quarterly); **Plants 2 and 5 back up to domain-joined storage, never restore-tested** |
| SYS-M3 MES and recipe master library | BP-M03, BP-M04 | Library replicated to provider B; signed paper formulation masters at each plant |
| SYS-M5 food safety records | BP-M05 | Provider A database with immutable backups in provider B |
| SYS-D1 WMS and DC automation | BP-D02, BP-D05 | WMS vendor SaaS; automation server images (DC-1 and DC-3) |
| SYS-R1 POS | BP-R01 | Store servers rebuilt from gold images; P2PE terminals keep no card data |
| SYS-G4 ERP | BP-G05 | Vendor backups (RPO 1 hour per contract) |
| People | All | Licensed refrigeration operators at every ammonia site; cross-trained controls engineers; escorted vendor on-site support |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access (rebuild the directory before reconnecting any domain-joined OT)
2. Cloud hubs, colocation network, and WAN
3. Cold-chain monitoring and alerting (manual logs until restored)
4. SOC visibility
5. to 8. Ammonia refrigeration control, plant cold storage, DC storage, and store cases
9. Store checkout
10. to 14. Thermal CCPs, refrigerated transportation, formulation (verified against signed masters), packaging and lot coding, DC picking and shipping
15. to 25. ERP, food safety records, traceability, receiving, store replenishment, the Plant 6 plant-based line, online ordering, the 3PL portal, OT remote access, payroll and finance, and loyalty.

## 8. Key findings
1. **The shared cold-chain platform is the group's most important single point of failure.** It is High in every division, and one untested server routes all alerts (P01 GR-02; POAM-005).
2. **OT recovery is proven at four plants and unproven at two.** Plants 2 and 5 have never restore-tested SCADA or MES and keep backups on domain-joined storage (P01 MT-004).
3. **The directory sits upstream of OT at two plants and five DCs' automation.** A directory outage alone would stop lines at Plants 2 and 5. Moving them to the OT domain is a recovery measure, not only a security one (POAM-001).
4. **Notification capacity is itself a process** (BP-G02, BP-M07). FSIS and FDA 24-hour clocks start at determination, so the food safety decision must not wait for IT recovery. The P08 runbook puts it first.
