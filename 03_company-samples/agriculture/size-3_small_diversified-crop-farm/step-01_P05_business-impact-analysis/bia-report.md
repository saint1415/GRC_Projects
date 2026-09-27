# Business Impact Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Small

**Organization:** Cris Santos Company, LLC (diversified precision-agriculture crop farm) | **Tier:** Small (15 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations and Technology Manager (security lead) with the Farm Manager, Irrigation Technician, and Food Safety and Packing Lead | **Approved:** Majority owner and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which farm processes depend on technology, how long each can be down, and how much data each can lose. It supports:
- the recovery objectives in the SSP (P02) and the availability rating of the Farm Management and Irrigation Control Platform (FMICP);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08);
- CSF 2.0 subcategories ID.AM-05 (assets prioritized by criticality) and RC.RP-01 to RC.RP-03 in the gap analysis (P03).

It covers all ten business processes. Interviews were held on 2026-07-14 and 2026-07-15 with the process owners named in `bia.csv`.

## 2. System and business description
The farm grows peanuts, strawberries, and vegetables and melons on about 640 acres in two blocks, with 15 employees and $1.5 million in receipts. Most revenue arrives between December and June, about $7,500 per in-season day. Field and packing work runs on the FMICP: a farm management and irrigation SaaS platform (SYS-01), the pump-house PLC and SCADA HMI, pivot panels and field sensors (SYS-07), a cloud tenant with the farm data hub (SYS-04), the farm networks (SYS-05), and endpoints and tablets (SYS-06). See `../00_company-facts.md` sections 3 and 4.

**What is different about a farm:** the biggest losses come from **time-critical physical processes**, not from data. A freeze night without overhead irrigation, a day without water on drip beds in May, or a cooler failure in peak season destroys crop that cannot be re-created. Every critical process therefore has a manual workaround, and the question for recovery is how long staff can sustain it.

## 3. Impact categories and values
Dollar values are scaled to $1.5 million in annual receipts, concentrated in about 200 in-season days.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $40,000 (about 5 in-season days of receipts, or loss of a strawberry block) | $10,000 to $40,000 | Less than $10,000 |
| Operations | Harvest or irrigation stops on a whole block | One crop, channel, or crew slowed or stopped | Staff slowed but working |
| Regulatory | Records required by the Produce Safety Rule or the H-2A program cannot be produced or are unreliable; permit exceedance; reportable breach | Late or incomplete record that can be corrected | Internal procedure deviation |
| Safety | Worker injury or chemical exposure (for example, fertigation or spray equipment misbehaving) | Unsafe condition caught before harm | None |
| Reputation | Loss of the distributor account or local media coverage | Customer complaints or buyer escalation | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Irrigation and fertigation | High | 12 h | 6 h | 24 h |
| BP-02 Harvest, field tally, and packing | High | 24 h | 12 h | 4 h |
| BP-03 Cold storage and cold-chain monitoring | High | 4 h | 2 h | 1 h |
| BP-04 Wholesale orders and fulfillment | Moderate | 48 h | 24 h | 24 h |
| BP-05 Direct sales | Moderate | 24 h | 8 h | 24 h |
| BP-06 Crop, application, and food safety records | Moderate | 72 h | 48 h | 24 h |
| BP-07 Precision field operations | Moderate | 72 h | 48 h | 168 h |
| BP-08 Payroll, H-2A records, and HR | Moderate | 72 h | 48 h | 24 h |
| BP-09 Accounting, USDA program and crop insurance reporting | Low | 240 h | 120 h | 24 h |
| BP-10 Yield forecasting and harvest planning | Low | 168 h | 120 h | 168 h |

Counts: 3 High, 5 Moderate, 2 Low.

**What drives the values:**
- **BP-01 (irrigation):** the 12-hour MTD assumes the Irrigation Technician can run pumps and pivots by hand. On freeze-protection nights the real limit is 1 hour, so freeze nights are staffed on site whenever the forecast approaches the trigger temperature. Manual operation of 5 pivots 6 miles apart plus the pump house needs at least two people, so it cannot be sustained for more than a few days.
- **BP-02 (harvest and tally):** the 4-hour RPO reflects that field tally is the H-2A earnings record (20 CFR 655.122(j)) and the Produce Safety harvest record (21 CFR 112.161(a)(2)). Lost tally entries mean wage disputes and records that cannot be re-created honestly.
- **BP-03 (cooler):** the refrigeration keeps running in an IT outage. What stops is monitoring. Hourly manual checks cover the gap.
- **BP-06 and BP-08 (records):** regulatory, not revenue, drives these. Produce Safety records kept off site must be produced within 24 hours of an FDA request (21 CFR 112.166(a)). H-2A earnings records kept at a central office must be produced within 72 hours of a DOL request (20 CFR 655.122(j)(2)).

**Key findings:**
1. **The PLC program has no farm-held backup.** It exists only on the integrator's laptop (gap 5). If the PLC or HMI were lost, the 6-hour RTO for BP-01 depends entirely on the integrator's availability.
2. **Backups are unproven.** The data hub and file share backups have never been restore-tested and sit in the same cloud account as production (gap 6), so the RTOs for BP-01 (flow history), BP-06, and BP-08 are unproven. This is risk R-003 in P01.
3. **SYS-01 recovery commitments must be checked.** The FMIS vendor's SOC 2 report (P09) states an RTO of 8 hours and an RPO of 1 hour. That RTO is longer than the 6-hour RTO for BP-01, so manual irrigation, not the vendor, carries that process for the first hours of a vendor outage. The 1-hour RPO meets every process that depends on SYS-01.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 FMIS (SaaS) | Farm records, harvest tally, Produce Safety records, irrigation control module | BP-01, BP-02, BP-04, BP-06, BP-07, BP-08 |
| SYS-02 Identity provider | Single sign-on and MFA for SYS-01 web, SYS-03, SYS-04 | All |
| SYS-05 Farm networks and internet | Headquarters firewall, switches, Wi-Fi; pivot cellular modems; LoRaWAN gateway; one fiber internet circuit (no backup) | BP-01 to BP-06 |
| SYS-06 Endpoints and tablets | 8 laptops, 3 desktops, 11 rugged tablets and phones | All |
| SYS-07 Irrigation, pump, and cold-room OT | PLC, HMI, pivot panels, valve controllers, sensors, cooler alarms | BP-01, BP-03 |
| SYS-04 Farm data hub and backup vault | Flow and pump history; backups | BP-01, BP-06, BP-08 |
| SYS-08 Telematics and RTK base station | Guidance corrections, as-applied data | BP-07 |
| SYS-10 Accounting and payroll | Payroll, invoicing, general ledger | BP-04, BP-08, BP-09 |
| SYS-11 Sales systems | Card terminals (processor), online store | BP-05 |
| People | Irrigation Technician (single point of knowledge for manual operation), Crew Leads, Food Safety and Packing Lead, Office and HR Manager, Operations and Technology Manager, MSP, integrator | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual irrigation operation (people, not systems) | Immediate | Hand operation at each panel; written procedure to be created (POAM-004) |
| 2 | SYS-02 identity provider and break-glass accounts | 1 h | Two break-glass administrator accounts stored offline (to be created) |
| 3 | SYS-07 cooler alarm service and headquarters network | 2 h | Hourly manual checks; cellular hotspot kit (to be purchased) |
| 4 | SYS-07 pump-house PLC and HMI | 6 h | PLC runs its last logic in local control; HMI rebuilt from a farm-held image with the farm-held PLC program backup (both to be created) |
| 5 | SYS-01 irrigation module and harvest tally | 6 h (irrigation), 12 h (tally) | Vendor-hosted; paper tally cards |
| 6 | SYS-06 clean endpoints and tablets for crew leads and the office | 12 h | 2 spare tablets and 1 spare laptop kept pre-enrolled (to be purchased) |
| 7 | SYS-10 payroll | 48 h | Repeat prior payroll through the payroll provider |
| 8 | SYS-04 farm data hub | 48 h | Flow read from meter faces; rebuild from immutable backup |
| 9 | SYS-11 sales systems | 8 h (processor and SaaS managed) | Cash and mobile reader app |
| 10 | SYS-08, SYS-09, SYS-12 | 48 to 120 h | Manual steering; hand counts |

Priority follows the BIA order in `bia.csv` except where a shared resource must come first (identity, network).

## 7. Approval
Approved by the majority owner and General Manager on 2026-08-31. Review each July before the season, or after a major change such as new irrigation automation.
