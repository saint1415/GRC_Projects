# Business Impact Analysis: Cris Santos Company | Food and Agriculture | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, the Controls Engineering Manager, and the Director of Engineering and Maintenance | **Fieldwork:** 2026-07-06 to 2026-07-24 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Plant 1 (Central Florida, further processing and ready-to-eat products), Plant 2 (North Florida, ground and case-ready products, acquired 2025-03-03), and the corporate functions that serve both. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and food and worker safety.

The results feed:
- the availability rating of the Plant Production and Cold-Chain Monitoring System (PPCM) in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- HACCP corrective action planning for unforeseen deviations (9 CFR 417.3(b)), because losing control or monitoring of a CCP is one;
- the PSM and RMP emergency response plans for the two ammonia systems (section 7);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company processes purchased beef and pork into branded and private-label products for grocery chains, foodservice distributors, and club stores, with about $480 million in sales. Production and cold storage at both plants run on the PPCM described in the SSP (P02): process controls, SCADA and historians, the recipe and batch systems (MES), the refrigeration controllers, cold-chain monitoring, OT remote access, and the cloud landing zone that holds the food safety records application and the traceability database. Business systems (ERP, WMS, HR and payroll) are SaaS. See `../00_company-facts.md` sections 1, 3, and 7.

**What is different about a food plant.** Downtime is not only lost revenue. Product that sits in a smokehouse, a brine injector, a blender, or a cooler while controls or monitoring are down may have to be held, evaluated, and destroyed, and it cannot ship without complete CCP records (9 CFR 417.5(c)). Recovery objectives are set to protect product and people, not only to bring systems back.

## 3. Impact categories and values
Dollar values are scaled to about $1.32 million of sales per production day at Plant 1 and $600,000 at Plant 2 (about 250 production days a year), with about $9 million of product in Plant 1 coolers and freezers and $3 million at Plant 2 on a typical day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $250,000 of unrecovered sales, product loss, or penalties | $50,000 to $250,000 | Less than $50,000 |
| Operations | A plant or its cold storage stops | One line, one shift, or one corporate function stops | Staff slowed but working |
| Regulatory | Adulterated or misbranded product in commerce, an FSIS enforcement action, or a PSM or RMP release event | Missing or late required records | Internal procedure deviation |
| Food and worker safety | Plausible consumer illness (temperature abuse, undercooking, cure error, Listeria) or worker harm (ammonia) | Product held for evaluation | None |
| Reputation | A recall with public notice, or loss of a grocery chain customer | Customer chargebacks or complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is unrecovered sales plus product loss, extra labor, and customer penalties over the MTD. Process owners estimated that about 30% of lost packaging output is not recovered through Saturday shifts (BP-04, BP-08). For BP-16 the loss is overtime and interest; the delayed cash is shown separately. Revenue per day is assigned to the packaging processes (BP-04, BP-08), because every product passes them, so it is not double counted.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-13 Ammonia refrigeration process safety monitoring and emergency response | Both plants | High | 1 | 0.5 | 0.25 | $15,000 |
| 2 | BP-01 Cold storage, refrigeration, and cold-chain monitoring | Plant 1 | High | 2 | 1 | 0.25 | $40,000 |
| 3 | BP-06 Cold storage, refrigeration, and cold-chain monitoring | Plant 2 | High | 2 | 1 | 0.25 | $25,000 |
| 4 | BP-02 Cooking, smoking, and chilling (thermal CCPs) | Plant 1 | High | 8 | 4 | 1 | $180,000 |
| 5 | BP-03 Formulation, cure and brine dosing, and injection | Plant 1 | High | 12 | 8 | 24 | $120,000 |
| 6 | BP-07 Grinding, blending, and fat analysis | Plant 2 | High | 12 | 8 | 4 | $90,000 |
| 7 | BP-04 Slicing, packaging, foreign material inspection, lot coding, and labeling | Plant 1 | High | 12 | 8 | 4 | $330,000 |
| 8 | BP-08 Case-ready cutting, tray packaging, metal detection, and labeling | Plant 2 | High | 12 | 8 | 4 | $150,000 |
| 9 | BP-09 Food safety records and pre-shipment review | Both plants | High | 24 | 12 | 1 | $80,000 |
| 10 | BP-10 Order management, EDI, warehouse, and shipping | Enterprise | High | 24 | 12 | 4 | $150,000 |
| 11 | BP-11 Traceability, recall, and customer traceability portal | Enterprise | Moderate | 24 (4 during a recall) | 8 | 4 | $20,000 |
| 12 | BP-05 Sanitation, CIP, and Listeria environmental monitoring | Plant 1 | Moderate | 24 | 12 | 24 | $60,000 |
| 13 | BP-12 Receiving of carcasses, primals, trim, and ingredients | Both plants | Moderate | 24 | 12 | 24 | $30,000 |
| 14 | BP-18 Customer service, complaints, and regulatory communications | Enterprise | Moderate | 24 | 8 | 24 | $15,000 |
| 15 | BP-14 Production planning, scheduling, and demand forecasting | Enterprise | Moderate | 48 | 24 | 24 | $40,000 |
| 16 | BP-17 Payroll, HR, timekeeping, and staffing agencies | Enterprise | Moderate | 72 | 48 | 24 | $30,000 |
| 17 | BP-16 Finance, accounts receivable, and customer billing | Enterprise | Moderate | 72 | 48 | 24 | $25,000 (plus about $3.9 million of cash delayed) |
| 18 | BP-15 Procurement and supplier management | Enterprise | Low | 72 | 48 | 24 | $10,000 |

**Summary:** 10 High, 7 Moderate, and 1 Low process (18 in total). The sum of estimated losses at each process's MTD is $1,410,000.

**Enterprise-wide scenario.** If the PPCM were down at both plants for 72 hours (for example, ransomware that reaches SCADA and the MES), about $5.76 million of output would be lost (3 production days at $1.92 million). About $1.73 million of it would not be recovered. Held product that cannot be shown safe would add an estimated $1.0 million to $1.5 million, and customer fill-rate penalties about $300,000. Incident response costs come on top (see P01 R-001).

**What drives the values:**
- **Worker safety drives BP-13.** Refrigeration keeps running on local controllers when SCADA is lost, and the hardwired ammonia detectors do not depend on the network. The 1-hour MTD covers the time engine room staff can safely run without supervisory visibility before switching compressors to manual operation under the PSM procedures.
- **Food safety drives BP-01, BP-02, BP-03, and BP-06.** Without cold storage monitoring for more than 2 hours, the cold storage CCP records have a gap and the FSQA managers must evaluate the product under 9 CFR 417.3(b). Manual hourly readings keep the gap closed.
- **BP-03 has a long RPO but a hard integrity requirement.** Formulations change rarely, so the last approved release is an acceptable recovery point. What matters is that restored formulations are *verified* against the signed master before use, because a changed cure setpoint is exactly what an attacker would leave behind (P01 R-003).
- **BP-09 gates shipping.** Product can wait in the cooler for a day, but it cannot ship without pre-shipment review. Paper review is the workaround.
- **BP-11 changes during a recall.** The 24-hour FSIS notification (9 CFR 418.2) means lot tracing must be available within hours once a recall is under way.
- **Cash flow, not time, drives BP-16.** Customers pay on EDI invoices; about $3.9 million is delayed for each 72 hours of outage.

## 5. Key findings
1. **OT recovery is unproven at both plants.** Plant 1 SCADA and MES backups sit on an OT backup server that is neither offline nor immutable, and only the Plant 1 SCADA server has been restore-tested (2025). Plant 2 PLC programs exist only on the integrator's laptops (gap 7). The 4-hour and 8-hour RTOs for BP-02, BP-03, BP-04, BP-07, and BP-08 are targets, not demonstrated capabilities (P01 R-007, R-008; P07 CP-4, CP-9).
2. **Plant 2 cold-chain monitoring has one alert path** (SMS to one supervisor), its gateways depend on the Plant 2 office Wi-Fi, and Plant 2 has no written manual log procedure (gap 9). The 1-hour RTO for BP-06 cannot be met reliably today (P01 R-012).
3. **Blend recipes at Plant 2 exist only in the blender HMIs.** There is no recovery point for BP-07 other than the integrator's laptop copies (P01 R-008).
4. **Plant 1 x-ray and metal detection run standalone**, which keeps the foreign material CCP working during an MES outage. The AI vision system (AI-001) is not a CCP and can be bypassed (P10).
5. **Cloud workloads are the best-protected layer.** The records application, traceability database, and EDI gateway have isolated, write-once backups. Their restore tests ran in 2026-04 for the records application only (P04 finding 3).
6. **The cold-chain monitoring vendor's commitments are unknown.** It has not provided a SOC 2 report (gap 10; P09 vendor review).

## 6. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-04 Refrigeration controllers | Compressors, evaporators, ammonia detection at each plant | BP-01, BP-06, BP-13 | Controller configuration export (quarterly, planned); hardwired ammonia alarms |
| SYS-05 Cold-chain monitoring | About 260 sensors, gateways, vendor SaaS | BP-01, BP-06, BP-12 | Gateways buffer 24 hours locally; vendor SaaS retention |
| SYS-01 Plant 1 process control network | PLCs, HMIs, smokehouses, ovens, dosing skid, injectors, slicers, packaging, x-ray | BP-02 to BP-05 | PLC programs in the Plant 1 OT repository (about 75% of PLCs) |
| SYS-02 Plant 2 process control network | PLCs, HMIs, grinders, blenders, tray packaging | BP-07, BP-08 | PLC programs on the integrator's laptops only (**gap**) |
| SYS-03 SCADA, historians, engineering workstations | Supervisory control and CCP data | BP-01, BP-02, BP-06, BP-09, BP-13 | Plant 1 nightly to the OT backup server (not immutable, **gap**); historian replicas to the cloud every 15 minutes |
| SYS-06 MES and Plant 2 label server | Formulations, setpoints, lot codes, labels | BP-03, BP-04, BP-07, BP-08 | Plant 1 nightly to the OT backup server; signed formulation masters in the FSQA library; Plant 2 label server has no backup (**gap**) |
| SYS-07 Cloud landing zone | Records application, historian replicas, traceability database, customer portal, EDI gateway | BP-05, BP-09, BP-10, BP-11, BP-16 | Daily backups to the backup account, 35-day write-once retention |
| SYS-08 ERP and SYS-09 WMS | Orders, inventory, shipping, billing | BP-10, BP-12, BP-14 to BP-16 | Vendor-managed SaaS backups |
| SYS-10 Identity provider | Sign-in for business and cloud systems | BP-09 to BP-18 | Vendor-managed; break-glass accounts sealed for the cloud only |
| SYS-11 Networks and endpoints | SD-WAN, firewalls, Wi-Fi, terminals, scanners | All | Dual ISP at Plant 1; single ISP at Plant 2 with cellular failover planned |
| SYS-17 HR and payroll SaaS | Payroll and time records | BP-17 | Vendor-managed |
| Utilities | Grid power; standby generators for refrigeration, SCADA, and server rooms at both plants | BP-01, BP-06, BP-13 | Generators with about 72 hours of fuel |
| People | Refrigeration operators, controls engineers, QA technicians, line supervisors, sanitation crews | All | Controls integrators and refrigeration contractors as backup |

## 7. PSM and RMP emergency response linkage
Both ammonia processes are covered by OSHA PSM (29 CFR 1910.119) and EPA RMP Program 3 (40 CFR 68.10(l)(2)). Their emergency plans were written for mechanical failures and leaks. The BIA supplies the cyber content they lack:

| Requirement (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| 1910.119(e)(3)(iii)-(iv): the process hazard analysis addresses engineering and administrative controls, including monitoring and control instrumentation with alarms, and the consequences of their failure | Loss or manipulation of the refrigeration controller and SCADA alarm views as a failure mode, with the 1-hour MTD for BP-13 | Added to the next PHA revalidation (Plant 1 due 2027-04; Plant 2 2026-12) |
| 1910.119(j)(1)(v) and 40 CFR 68.73(a)(5): controls, monitoring devices, sensors, alarms, and interlocks are mechanical integrity equipment | Refrigeration controllers, ammonia detection inputs, and remote access paths listed as dependencies of BP-13 | Controller configuration backups planned (P07 POAM-010) |
| 1910.119(l) and 68.75: management of change for technology and equipment | Controller firmware, logic, remote access, and network changes treated as changes that need the PSM MOC review | Gap: the Plant 2 modem was never reviewed under MOC (P03) |
| 1910.119(n): emergency action plan, including procedures for small releases; 68.95: emergency response program with procedures for informing the public and response agencies | Manual operation procedure when supervisory control is lost; contact tree in the P08 runbooks | To be added to both plans by 2026-12-31 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Refrigeration controllers supervised and ammonia alarms visible (SYS-04) | 0.5 h | Hardwired alarms; engine room staffed; manual compressor control under PSM procedures |
| 2 | Temperatures recorded at both plants (SYS-05) | 1 h | Manual hourly log (Plant 1 procedure; Plant 2 procedure due 2026-10-31); trailers on shore power |
| 3 | Safe state for in-process product (SYS-01, SYS-02) | 2 h | Finish or abort cycles on local controllers; hold product for FSQA evaluation |
| 4 | SCADA and historians from a verified clean backup (SYS-03) | 4 h | Chart recorders and manual probe readings |
| 5 | MES restored and formulations verified against the signed master (SYS-06) | 8 h | Hand-weighed batches from signed sheets; manual blend calculation at Plant 2 |
| 6 | Packaging, labeling, and lot coding at both plants (SYS-01, SYS-02, SYS-06) | 8 h | Pre-printed labels with manual lot codes and a second-person check |
| 7 | Identity provider, SD-WAN, and corporate network (SYS-10, SYS-11) | 8 h | Cloud break-glass accounts; break-glass for the identity provider to be created |
| 8 | Records application, traceability database, and EDI gateway (SYS-07) | 12 h | Paper CCP forms and paper pre-shipment review; customer orders by email |
| 9 | ERP and WMS for shipping (SYS-08, SYS-09) | 12 h | Paper pick lists and bills of lading from the last export |
| 10 | Customer traceability portal (SYS-07) | 8 h during a recall; otherwise 24 h | Phone and email to customer quality contacts |
| 11 | Payroll and finance (SYS-17, SYS-08) | 48 h | Repeat the prior payroll; manual invoices to the largest customers |
