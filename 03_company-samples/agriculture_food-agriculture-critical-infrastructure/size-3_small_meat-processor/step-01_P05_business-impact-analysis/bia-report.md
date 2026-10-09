# Business Impact Analysis: Cris Santos Company | Food and Agriculture | Small

**Organization:** Cris Santos Company, LLC (meat processing plant with a smoked seafood room) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Operations Manager, FSQA Manager, Maintenance and Refrigeration Manager, and Warehouse and Logistics Manager | **Approved:** General Manager, 2026-09-04
**Sources:** process owner interviews 2026-07-13 to 2026-07-14 (EV-046), FY2025 sales and inventory reports (EV-039), cloud and OT backup job reports (EV-016, EV-017), cold-chain monitoring configuration (EV-035), HACCP plans and recall procedure (EV-022). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the General Manager.

## 1. Overview and purpose
This BIA identifies which plant processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating of the Plant Production and Cold-Chain Monitoring System (PPCM) in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08);
- HACCP corrective action planning for unforeseen deviations (9 CFR 417.3(b)), because a control-system outage is one.

## 2. System and business description
One Florida plant with 250 employees runs four processing lines, five smokehouses, an ammonia refrigeration system, coolers, a freezer warehouse, and shipping docks. Human food sales are about $148 million a year. Production and cold storage run on the PPCM: process controls, SCADA and historian, the recipe and batch system (MES), refrigeration controls, cold-chain monitoring, and a cloud tenant for food safety records. Business systems (ERP, WMS) are SaaS. See the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

**What is different about a food plant.** Downtime is not only lost revenue. Product that sits in a smokehouse, a brine tank, or a cooler while controls or monitoring are down may have to be held, evaluated, and possibly destroyed, and it cannot ship without complete CCP records (9 CFR 417.5(c)). Recovery time objectives are set so that product can be protected, not only so that systems come back.

## 3. Impact categories and values
Dollar values are scaled to about $148 million in human food sales across 250 production days, about $590,000 in revenue per production day (EV-039).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 (lost production plus product loss) | $100,000 to $500,000 | Less than $100,000 |
| Operations | Plant or cold storage stops | One line or one shift stops | Staff slowed but working |
| Regulatory | Adulterated product in commerce, FSIS action, or FDA prohibited act | Missing or late required records | Internal procedure deviation |
| Safety | Plausible consumer illness (temperature abuse, undercooking, cure error) or worker harm (ammonia) | Product held for evaluation | None |
| Reputation | Recall with public notice or loss of a grocery chain customer | Customer chargebacks or complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Cold-chain temperature control and monitoring | High | 2 h | 1 h | 15 min |
| BP-02 Cooking, smoking, and chilling (thermal CCPs) | High | 8 h | 4 h | 1 h |
| BP-03 Formulation, curing, and brine dosing | High | 12 h | 8 h | 24 h |
| BP-04 Processing, packaging, lot coding, and labeling | High | 12 h | 8 h | 4 h |
| BP-05 Smoked seafood production | Moderate | 24 h | 12 h | 4 h |
| BP-06 Food safety records and pre-shipment review | High | 24 h | 12 h | 1 h |
| BP-07 Order management, warehouse, and shipping | High | 24 h | 12 h | 4 h |
| BP-08 Traceability and recall | Moderate | 24 h (4 h during a recall) | 8 h | 24 h |
| BP-09 Receiving | Moderate | 24 h | 12 h | 24 h |
| BP-10 Finance, payroll, outlet and online store | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Food safety drives BP-01 and BP-02.** Refrigeration itself keeps running on its local controller when SCADA is lost, but *knowing* the temperature does not. Without monitoring for more than 2 hours, cold storage CCP records have a gap, and the FSQA Manager must evaluate the product under 9 CFR 417.3(b). Hourly manual readings keep the gap closed.
- **BP-03 has a long RPO but a hard integrity requirement.** Formulations change rarely, so the last approved release is an acceptable recovery point. What matters is that the restored recipes are *verified* against the signed master before use, because a changed cure setpoint is exactly what an attacker would leave behind (P01 R-003).
- **BP-06 gates shipping.** Product can wait in the cooler for a day, but it cannot ship without pre-shipment review. Paper review is the workaround.
- **BP-08 changes during a recall.** The 24-hour FSIS notification clock (9 CFR 418.2) means lot tracing must be available within hours once a recall is under way.

**Key findings:**
1. **OT recovery is unproven.** SCADA and MES backups have never been restore-tested and sit in the same server room; PLC programs exist only on one laptop (P01 R-007). The 4-hour and 8-hour RTOs for BP-02 to BP-04 are targets, not demonstrated capability.
2. **Cold-chain monitoring has one alert path** (SMS to one person) and its gateway depends on the corporate Wi-Fi and internet (P01 R-005, R-018). The 1-hour RTO for monitoring can only be met with the manual log procedure.
3. **The cold-chain monitoring vendor's commitments are unknown.** Its SOC 2 report is reviewed in P09.

## 5. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-03 Refrigeration controls | Compressors, evaporators, ammonia detection | BP-01 | Controller configuration export (to be taken quarterly); hardwired ammonia alarms |
| SYS-04 Cold-chain monitoring | 64 sensors, gateway, vendor SaaS | BP-01, BP-05, BP-09 | Gateway buffers 24 hours locally; vendor SaaS retention |
| SYS-01 Process control network | PLCs, HMIs, dosing skid, smokehouse controllers, packaging | BP-02 to BP-05 | PLC programs on the engineering laptop only (**gap**); repository planned |
| SYS-02 SCADA, historian, engineering workstation | Supervisory control and CCP data | BP-01, BP-02, BP-06 | Nightly backup to a network storage device in the same room (**gap**); historian replica to the cloud tenant every 15 minutes |
| SYS-05 Recipe, batch, and lot-coding system | Formulations, setpoints, labels | BP-03, BP-04 | Nightly backup (same device as SYS-02); signed paper formulation master in the FSQA office |
| SYS-06 Cloud tenant | Records application, historian replica, traceability database, backup vault | BP-06, BP-08 | Daily backups, 35-day retention, same account (**gap**) |
| SYS-07 ERP and SYS-08 WMS | Orders, inventory, shipping | BP-07, BP-09, BP-10 | Vendor-managed SaaS backups |
| SYS-09 Identity provider | Sign-in for all business and cloud systems | BP-06 to BP-10 | Vendor-managed; break-glass accounts planned |
| SYS-11 Corporate network | Firewall, switches, Wi-Fi, single ISP | All | Cellular failover planned |
| Utilities | Grid power, standby generator (refrigeration, SCADA, server room) | BP-01, BP-02 | Generator with about 72 hours of fuel |
| People | Refrigeration technicians, Controls Engineer, QA technicians, line supervisors | All | Controls integrator as backup for the Controls Engineer |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Refrigeration running and temperatures being recorded (SYS-03, SYS-04) | 1 h | Local controller keeps running; manual hourly temperature log; move product to shore-powered trailers |
| 2 | Safe state for in-process product (SYS-01 smokehouses and chilling) | 2 h | Finish or abort cycles on local controllers; hold product for FSQA evaluation |
| 3 | SCADA and historian from a verified clean backup (SYS-02) | 4 h | Chart recorders and manual probe readings |
| 4 | Recipe system restored and formulations verified against the signed master (SYS-05) | 8 h | Hand-weighed batches from signed sheets |
| 5 | Packaging, labeling, and lot coding (SYS-01, SYS-05) | 8 h | Pre-printed labels with manual lot codes and second-person check |
| 6 | Identity provider and corporate network (SYS-09, SYS-11) | 8 h | Break-glass accounts (to be created) |
| 7 | Food safety records application and traceability database (SYS-06) | 12 h | Paper CCP forms and paper pre-shipment review |
| 8 | ERP and WMS access for shipping (SYS-07, SYS-08) | 12 h | Paper pick lists and bills of lading from the last export |
| 9 | Seafood room (Line 4) | 12 h | Pause intake; hold raw fish refrigerated |
| 10 | Finance, payroll, outlet, online store | 48 h | Repeat prior payroll |
