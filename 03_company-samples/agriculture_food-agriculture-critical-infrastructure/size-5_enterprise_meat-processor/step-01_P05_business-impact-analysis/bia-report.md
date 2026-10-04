# Business Impact Analysis: Cris Santos Company | Food and Agriculture | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded further processor of meat products: 8 plants, 4 distribution centers; FL, GA, AL, NC, TN, TX) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired plant (PLT-08). It feeds:
- the availability rating and recovery objectives in the Plant Production and Cold-Chain Monitoring System (PPCM) SSP (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08) and the quantitative factors in the SEC materiality worksheet (P08 section 6);
- HACCP corrective action planning for unforeseen deviations at every plant (9 CFR 417.3(b)), because a control-system or monitoring outage is one;
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 9 are High criticality, 7 Moderate, and 1 Low. 2 processes need recovery within 4 hours and 7 within 8 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies: 9 are single points of failure, 2 more are partial single points of failure, and 2 have never been tested.

## 2. System and business description
Cris Santos Company further processes purchased beef and pork into bacon, hams, sausage, hot dogs, deli meats, and fully cooked entrees at 8 FSIS-inspected plants, and stores and ships them through 4 refrigerated distribution centers and its own fleet. It has 12,000 employees and about $4.8 billion in annual revenue, about $18.8 million per production day. PLT-07 also makes FDA-regulated plant-based products. The technology estate is described in `../00_company-facts.md` section 3: plant OT (SYS-01 to SYS-03), cold-chain monitoring (SYS-04), the central MES in Cloud provider A (SYS-05), ERP and payroll (SYS-06), WMS and TMS (SYS-07), the identity platform (SYS-08), the multi-cloud estate and two colocation sites (SYS-09), the network (SYS-10), the food safety records and traceability platforms (SYS-11, SYS-12), and customer portals (SYS-13). PLT-08 was acquired in October 2025 and is not yet integrated.

**What is different about a food company.** Downtime is not only lost revenue. Product that sits in a smokehouse, a brine injector, or a cooler while controls or monitoring are down may have to be held, evaluated, and possibly destroyed, and it cannot ship without complete CCP records (9 CFR 417.5(c)). Recovery objectives are set so product can be protected, not only so systems come back.

## 3. Impact categories and values
Dollar thresholds are scaled to about $18.8 million of revenue per production day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative (lost production plus product loss) | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | Two or more plants, or all cold storage at a site, stop | One line, one shift, or one DC stops | Staff slowed but working |
| Regulatory | Adulterated product in commerce, FSIS enforcement action, FDA prohibited act, or a missed SEC filing | Missing or late required records; a single-plant noncompliance record | Internal procedure deviation |
| Safety | Plausible consumer illness (temperature abuse, undercooking, cure error) or worker harm (ammonia release) | Product held for evaluation | None |
| Reputation | Public recall notice, national media, or loss of a national customer | Customer chargebacks or complaints; regional media | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Cold-chain temperature control and monitoring | High | 2 h | 1 h | 15 min | $9.50M |
| BP-02 Thermal processing CCPs (cooking, smoking, chilling) | High | 8 h | 4 h | 1 h | $11.30M |
| BP-03 Formulation, curing, and brine dosing | High | 12 h | 8 h | 24 h | $6.60M |
| BP-04 Processing, packaging, labeling, and lot coding | High | 12 h | 8 h | 4 h | $18.80M |
| BP-17 Production at PLT-08 (legacy systems) | High | 12 h | 8 h | 4 h | $1.60M |
| BP-07 Traceability and recall | High | 24 h (4 h during a recall) | 8 h | 4 h | $0.40M |
| BP-06 Food safety records and pre-shipment review | High | 24 h | 12 h | 1 h | $15.00M |
| BP-08 Customer order management and EDI | High | 24 h | 12 h | 4 h | $4.20M |
| BP-09 Distribution center warehousing and shipping | High | 24 h | 12 h | 4 h | $5.10M |
| BP-12 SL-1 cold storage and logistics services | Moderate | 24 h | 8 h | 1 h | $0.45M |
| BP-05 Prepared foods and plant-based production at PLT-07 | Moderate | 24 h | 12 h | 4 h | $1.40M |
| BP-10 Transportation and fleet dispatch | Moderate | 24 h | 12 h | 4 h | $1.80M |
| BP-11 Raw material purchasing and receiving | Moderate | 24 h | 12 h | 24 h | $1.10M |
| BP-13 SL-2 co-manufacturing and private label services | Moderate | 48 h | 24 h | 4 h | $1.70M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-16 Online store and consumer service | Low | 72 h | 48 h | 24 h | $0.12M |

The quantified impacts overlap (BP-04 is the whole production day, and BP-02, BP-03, and BP-06 are parts of it), so they are not added together. For the materiality worksheet, Finance uses BP-04 for lost production and BP-01 and BP-06 for product at risk.

**What drives the values:**
- **Food safety drives BP-01 and BP-02.** Refrigeration keeps running on local controllers when SCADA or the monitoring service is lost, but *knowing* the temperature does not. Without monitoring for more than 2 hours, cold storage CCP records have a gap and each plant FSQA manager must evaluate the product under 9 CFR 417.3(b). Hourly manual readings keep the gap closed, but that procedure has been exercised at only 3 of 12 sites.
- **BP-03 has a long RPO but a hard integrity requirement.** Formulations change rarely, so the last approved release is an acceptable recovery point. What matters is that restored recipes are *verified* against the signed masters before use, because a changed cure setpoint is exactly what an attacker would leave behind (P01 R-003, R-004).
- **BP-06 gates shipping.** Product can wait in the cooler for a day, but it cannot ship without pre-shipment review, so a records outage quickly becomes a warehouse and delivery problem.
- **BP-07 changes during a recall.** The 24-hour FSIS notification clock (9 CFR 418.2) means lot tracing must be available within hours once a recall is under way.
- **Regulation** tightens financial close (BP-15) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.
- **Contracts** set the SL-1 and SL-2 objectives (BP-12, BP-13), because external customers rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Central MES recovery (DEP-01).** Since the 2025-2026 migration, every plant except PLT-08 takes recipes, setpoint ranges, and labels from one central MES. It recovered in 7.5 hours against its 4-hour RTO in the 2026-05-16 DR test. Plant edge servers cache 72 hours of approved recipes, which protects BP-03 and BP-04 for a short outage but not for a compromise of the central system itself (P01 R-004, R-008; POAM-010).
2. **Cold-chain monitoring concentration (DEP-08).** One vendor serves all 12 sites and 380 trailers. The vendor's contract states no recovery time, its SOC 2 Type 2 report has an exception on alert delivery, and the manual log fallback has been exercised at only 3 of 12 sites. This is P01 risk R-005 and POA&M item POAM-008.
3. **Acquired plant (DEP-21, DEP-22).** PLT-08's legacy directory, recipe system, and eHACCP application back up nightly, so its real RPO is 24 hours against a 4-hour target, and its support contract states a 24-hour restore against an 8-hour BIA RTO. Neither restore has been tested.
4. **Plant OT recovery.** Plant SCADA, historian, and MES edge server restores have been demonstrated at 4 of 8 plants (PLT-01, PLT-03, PLT-04, PLT-06). The other 4 RTOs for BP-02 to BP-04 are targets, not demonstrated capability.
5. **Single providers the company cannot easily replace:** the EDI network (DEP-17), the telematics carrier (DEP-23), and the meat packers that supply about 70% of primals (DEP-16). The workarounds are procedural.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-03 Refrigeration controls (12) | Compressors, evaporators, ammonia detection | BP-01 |
| SYS-04 Cold-chain monitoring | About 3,400 sensors, site gateways, trailer telematics, vendor SaaS | BP-01, BP-09, BP-10, BP-12 |
| SYS-01 and SYS-02 Plant OT | PLCs, HMIs, dosing skids, smokehouses, SCADA, historians, MES edge servers | BP-02 to BP-05, BP-17 |
| SYS-05 Central MES and enterprise historian | Formulations, recipe release, labels, lot codes | BP-03, BP-04, BP-13 |
| SYS-11 and SYS-12 Records and traceability platforms | eHACCP, pre-shipment review, lot genealogy | BP-06, BP-07 |
| SYS-06 ERP and payroll | Orders, purchasing, finance, payroll | BP-08, BP-11, BP-14, BP-15 |
| SYS-07 WMS and TMS | DC operations and fleet dispatch | BP-09, BP-10, BP-12 |
| SYS-08 Identity platform | SSO, MFA, PAM | All except PLT-08 |
| SYS-09 Cloud A, Cloud B, COLO-1, COLO-2 | Workload hosting and backup copies | Recovery of all |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to COLO-2 | RPO for cloud workloads |
| OT backups | Plant backup appliances with offline copies (PLT-08 excluded) | RPO for plant OT |
| People | Refrigeration technicians, plant controls engineers, QA technicians, SOC, OT Security team | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Refrigeration running and temperatures recorded at all sites (SYS-03, SYS-04) | 1 h | Local controllers; hourly manual logs; product to shore-powered trailers |
| 2 | Safe state for in-process product (SYS-01 smokehouses, ovens, chilling) | 2 h | Finish or abort cycles locally; hold product for FSQA evaluation |
| 3 | Identity platform and break-glass accounts (SYS-08) | 1 h after decision to restore | Sealed break-glass accounts; secondary region |
| 4 | Network core, SD-WAN, OT DMZ, and security tooling for clean-room validation | 2 h | Cellular failover; MSSP tooling |
| 5 | Plant SCADA and historians from verified clean backups (SYS-02) | 4 h | Chart recorders and manual probe readings |
| 6 | Central MES restored and formulations verified against signed masters (SYS-05) | 8 h (7.5 h demonstrated) | Edge-server recipe cache; hand-weighed batches from signed sheets |
| 7 | Packaging, labeling, and lot coding (SYS-01, SYS-05) | 8 h | Pre-printed labels with manual lot codes and second-person check |
| 8 | Traceability platform (SYS-12) | 8 h | Daily offline export; paper shipping records |
| 9 | Food safety records platform (SYS-11) | 12 h | Paper CCP forms and paper pre-shipment review |
| 10 | ERP order management, EDI, WMS, and TMS (SYS-06, SYS-07) | 12 h | Email and phone orders; paper pick lists and dispatch sheets |
| 11 | SL-1 and SL-2 customer portals (SYS-13) | 8 h and 24 h | Email reports from the last export |
| 12 | PLT-08 legacy systems | 8 h target (24 h per support contract) | Paper CCP forms; pre-printed labels |
| 13 | Payroll, financial close, online store | 48 h to 72 h | Repeat prior payroll |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Central MES recovered in 7.5 h against a 4 h RTO | P01 R-008; P02 CP-10; POAM-010 |
| Plant OT restores demonstrated at 4 of 8 plants | P01 R-008; P07 CP-4; POAM-010 |
| Cold-chain monitoring vendor concentration; manual log fallback exercised at 3 of 12 sites | P01 R-005; P03 G-099; POAM-008 |
| PLT-08 actual RPO 24 h and restore 24 h against BIA targets | P01 R-002; POAM-001; POAM-007 |
| Disclosure playbook lacks a method for product holds and recall costs | P01 R-010; P08 section 6; POAM-014 |
