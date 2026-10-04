# Business Impact Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) | **Tier:** Mid-Market (600 employees at peak) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the three farms, irrigation and water resources, the central packinghouse, food safety, sales and logistics, Grower Services, human resources, finance, and corporate IT. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and safety (worker safety and food safety).

The results feed:
- the contingency and disaster recovery plan (STD-07 in P06), including the manual irrigation and freeze-night procedures;
- the FIPS 199 availability rating and contingency controls in the SSP for the Farm Management and Irrigation Control Platform (FMICP, P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for Grower Services (P09).

No regulation requires this company to perform a BIA. The analysis follows CSF 2.0 GV.OC-04 (critical services others depend on) and SP 800-82 Rev. 3 section 5.3.2 (availability considerations for OT). It also supports record duties that are binding: Produce Safety records on FDA request (21 CFR 112.166(a)), pesticide application information display within 24 hours (40 CFR 170.311(b)(5)), and H-2A earnings statements on each payday (20 CFR 655.122(k)).

## 2. System and business description
The company farms about 15,400 acres on three Florida farms and packs about 78% of its own produce plus the produce of about 30 contract growers at a central packinghouse next to headquarters. Farm operations run on the FMICP described in the SSP (P02): the FMIS SaaS with its irrigation module (SYS-01), the identity provider (SYS-02), the 5-account cloud landing zone with the farm data hub and the grower portal (SYS-04, SYS-12), networks and SD-WAN at 6 sites (SYS-05), 390 endpoints (SYS-06), and about 2,900 OT and IoT devices: irrigation SCADA, 54 well pumps, 14 fertigation skids, 46 center pivots, about 1,500 valve controllers, and the packinghouse cooling, ripening, packing line, and cold-chain controls (SYS-07). The ERP (SYS-10), HR and payroll (SYS-11), telematics (SYS-08), and drones (SYS-09) connect to it. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual receipts. About 85% of produce ships from November to June, over about 180 shipping days: about $490,000 of shipments per shipping day on average, and more than $800,000 on peak spring days. Grower settlements average about $900,000 a week in season.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event at MTD) | More than $100,000 of lost crop, product, or revenue, or more than $500,000 of cash delayed | $20,000 to $100,000 | Less than $20,000 |
| Operations | A farm, the packinghouse, or the sales desk cannot perform its core work, or a freeze night is missed | One process or one farm slows by more than 30% | Staff slowed but working |
| Regulatory | Records required by FDA, EPA, or DOL cannot be produced or were not created, or a reportable breach under Fla. Stat. 501.171 | Late or incomplete records; a contract notice to a retail customer | Internal policy deviation |
| Safety | Plausible worker injury or unsafe food reaching customers (temperature abuse, contamination, wrong lot data in a recall) | Elevated exposure that is controlled by manual procedures | None |
| Reputation | Loss of a retail program, a grower association complaint, or regional media | Customer chargebacks or grower complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is lost crop or product value, plus lost or discounted sales and extra labor, over the MTD. The process owners supplied the assumptions: about 2% to 4% of affected crop value per day of missed irrigation in spring heat; about 30% of a day's shipments lost or discounted when the packinghouse stops for 4 hours at peak; chargebacks of about 10% on missed retail delivery windows. Delayed cash (grower settlements, receivables) is shown separately, not as loss.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-02 Freeze protection (overhead irrigation) | Farm 2 | High | 2 | 1 | 24 | $250,000 (worst case $1.5M to $2M for a fully failed night) |
| 2 | BP-05 Cold-chain monitoring and alarms | Packinghouse | High | 2 | 1 | 0.25 | $40,000 |
| 3 | BP-04 Packing, cooling, and ripening | Packinghouse | High | 4 | 2 | 1 | $150,000 |
| 4 | BP-01 Irrigation and fertigation control | Farms 1-3 | High | 24 | 8 | 1 | $120,000 |
| 5 | BP-03 Harvest planning, crew dispatch, and field tally | Farms 1-3 | High | 12 | 4 | 1 | $60,000 |
| 6 | BP-06 Order management, shipping, and EDI | Sales and logistics | High | 12 | 8 | 1 | $120,000 |
| 7 | BP-07 Traceability, lot coding, and recall support | Food safety | Moderate | 24 | 12 | 1 | $20,000 |
| 8 | BP-08 Produce Safety and pesticide application records | Food safety | Moderate | 24 | 24 | 4 | $5,000 |
| 9 | BP-11 Grower irrigation monitoring and agronomy alerts | Grower Services | Moderate | 24 | 8 | 1 | $15,000 |
| 10 | BP-18 Email, collaboration, and identity | Corporate | Moderate | 24 | 8 | 4 | $10,000 |
| 11 | BP-09 Precision application and GNSS guidance | Farms 1-3 | Moderate | 48 | 24 | 24 | $40,000 |
| 12 | BP-13 Payroll, H-2A earnings statements, and timekeeping | Human resources | Moderate | 72 | 48 | 24 | $30,000 |
| 13 | BP-12 Grower pack-out reporting and pool settlement | Grower Services | Moderate | 72 | 48 | 4 | $25,000 (plus about $900,000 of grower payments delayed) |
| 14 | BP-15 Accounts payable, receivable, and treasury | Finance | Moderate | 72 | 48 | 24 | $20,000 |
| 15 | BP-16 Direct retail sales | Sales and logistics | Low | 72 | 24 | 24 | $15,000 |
| 16 | BP-10 Crop scouting, drone imagery, and yield forecasting | Farms 1-3 | Low | 168 | 72 | 24 | $5,000 |
| 17 | BP-14 Water use permit reporting | Irrigation and water resources | Low | 336 | 168 | 24 | $2,000 |
| 18 | BP-17 USDA program, crop insurance, and acreage reporting | Finance | Low | 336 | 168 | 24 | $2,000 |

**Summary:** 6 High, 8 Moderate, and 4 Low processes (18 in total). The sum of estimated losses at each process's MTD is $929,000.

**Enterprise-wide scenario.** If the FMICP and the IT systems around it were down for 72 hours at the spring peak (for example, ransomware), the estimated unrecovered loss is about $1.4 million: about $590,000 of lost or discounted shipments, $350,000 of packinghouse spoilage, $300,000 of crop stress while irrigation runs by hand at half capacity, and $160,000 of overtime and retail chargebacks. About $900,000 of grower settlements and one payroll cycle would also be delayed. If the outage covered a freeze night at Farm 2 and the manual start failed, up to $1.5 million to $2 million more would be at risk. Incident response and breach notification costs come on top (see P01 R-001 and R-003).

**What drives the values:**
- **Weather and biology, not systems, set the shortest clocks.** Freeze protection (BP-02) and cold-chain alarms (BP-05) have 2-hour MTDs because frost and heat damage crops and berries within hours.
- **Cash and contracts** drive BP-06 and BP-12. Retail delivery windows are fixed, and growers and their lenders depend on the weekly settlement date.
- **Regulatory record duties** drive BP-03, BP-07, BP-08, and BP-13. A short outage is tolerable only if records are created on paper at the time and keyed in later, which keeps them "created at the time an activity is performed" (21 CFR 112.161(a)(2)).

## 5. Key findings
1. **Freeze protection has no tested fallback.** BP-02 depends on SCADA automation, one alarm dialer, and a radio link. The manual night-start procedure is unwritten (gap 9). Action: a standalone freeze alarm path, a written manual start procedure tested each November, and a staffed freeze-night roster (P01 R-004; P07 POAM-012).
2. **Company-managed OT recovery is unproven.** SCADA servers are backed up weekly to a local storage device on the same network, and some PLC and HMI programs exist only with the integrator (gap 3). The BIA needs BP-01 back within 8 hours and BP-04 within 2 hours. Neither has been demonstrated (P01 R-007, R-008; P07 CP-4, CP-10).
3. **The FMIS vendor's recovery objectives do not meet the BIA for harvest.** The vendor's SOC 2 report states RTO 8 hours and RPO 1 hour. BP-03 needs RTO 4 hours. Paper tally cards make the MTD of 12 hours achievable, but only if crews have the cards and the training (P01 R-013; P09 vendor review).
4. **The packinghouse can run by hand, but not for long.** Manual grading cuts throughput by about 60%, and manual cold-chain rounds need one person per shift. Both workarounds are known to supervisors but are not written into downtime procedures (P01 R-022).
5. **Regulated records depend on one SaaS copy.** Produce Safety, pesticide application, H-2A tally, and harvest traceability records live in SYS-01, and a full export for a 24-hour FDA request has never been tested (gap 10; P01 R-024, R-025).
6. **Grower Services has explicit commitments.** Marketing agreements promise 99.5% monthly availability of irrigation alerts in season and a fixed settlement schedule. These are the system commitments for the SOC 2 Availability and Processing Integrity criteria (P09).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 FMIS with irrigation module (SaaS) | Field records, schedules, Produce Safety and pesticide records, tally, harvest traceability | BP-01, BP-03, BP-07, BP-08, BP-09 |
| SYS-02 Identity provider | SSO and MFA for office users and administrators | BP-06, BP-11 to BP-13, BP-15, BP-18 |
| SYS-04 Landing zone: farm data hub | Historian replica, integrations between SCADA, SYS-01, and SYS-12 | BP-01, BP-07, BP-11, BP-14 |
| SYS-04 Landing zone: backup account | Daily write-once backups, 35-day retention, second region | Recovery of SYS-04 and SYS-12 workloads |
| SYS-05 Networks and SD-WAN | 6 sites; radio and fiber to pump stations; cellular for pivots; single internet circuit at Farm 2 | All |
| SYS-06 Endpoints | 210 laptops and desktops, 160 tablets and phones, 20 packinghouse line PCs | BP-03, BP-04, BP-06, BP-08 |
| SYS-07 Irrigation OT | SCADA servers and HMIs, PLCs, well pumps, fertigation skids, valves, pivots, sensors, alarm dialer | BP-01, BP-02, BP-14 |
| SYS-07 Packinghouse OT | Packing line PLCs, optical graders, cooling and ripening controls, cold-chain sensors and alarm service | BP-04, BP-05, BP-07, BP-12 |
| SYS-08 Telematics and GNSS | 85 machines, 3 RTK base stations, dealer portal | BP-09 |
| SYS-10 ERP | Orders, EDI, invoicing, payables, prices for settlements | BP-06, BP-12, BP-15, BP-17 |
| SYS-11 HR, payroll, timekeeping | Payroll, H-2A statements, biometric time clocks | BP-13 |
| SYS-12 Grower portal and settlement service | Grower alerts, pack-out, statements, settlement calculation | BP-11, BP-12 |
| SYS-13 Retail sales | P2PE terminals; e-commerce SaaS | BP-16 |
| Third parties | FMIS vendor, SCADA integrator, pivot cloud service, refrigeration contractor, ERP and EDI providers, payroll provider, development firm, cloud provider, MSSP, utilities, cellular carrier | As listed in `bia.csv` |
| People and facilities | Irrigation Technicians and the Irrigation Operations Center; packinghouse shifts; crew leads; Food Safety Coordinators; settlement analysts; IT and security team | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Farm 2 freeze protection pumps and weather alarms (in freeze season) | 1 h | Manual pump starts by the freeze-night crew from a standalone thermometer alarm |
| 2 | Cold-chain sensors and alarm service | 1 h | Hourly manual rounds with paper logs |
| 3 | Packinghouse controls (cooling, ripening, packing line PLCs) on a clean, isolated OT network | 2 h | Local controller operation; manual grading; pre-printed lot labels |
| 4 | SYS-02 identity provider and break-glass accounts | 2 h | Break-glass accounts sealed offline |
| 5 | SCADA servers and HMIs (restored from offline PLC and HMI backups) | 8 h | Hand operation at each pump panel from a printed schedule |
| 6 | SYS-05 site networks and SD-WAN, OT segments first | 4 h | Cellular failover kits at the packinghouse and farm offices |
| 7 | SYS-01 FMIS access and crew tablets | 4 h | Paper tally cards and field binders |
| 8 | SYS-10 ERP and EDI | 8 h | Phone and email orders from the top 10 customers; manual bills of lading |
| 9 | SYS-04 farm data hub and integrations | 8 h | Direct SCADA operation; manual exports |
| 10 | SYS-12 grower portal (alerts) | 8 h | Phone and text alerts by agronomists |
| 11 | SYS-14 SIEM feeds and EDR console | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 12 | SYS-08 telematics and RTK | 24 h | Manual steering |
| 13 | SYS-11 payroll and timekeeping | 48 h | Repeat prior payroll; paper statements for H-2A workers |
| 14 | SYS-12 settlement service | 48 h | Spreadsheet settlement by the Controller |
| 15 | SYS-13 retail sales | 24 h | Cash only |
| 16 | Imagery data lake and yield model | 72 h | Hand counts |
