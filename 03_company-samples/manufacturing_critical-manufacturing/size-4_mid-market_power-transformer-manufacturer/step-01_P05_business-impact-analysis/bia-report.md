# Business Impact Analysis: Cris Santos Company | Critical Manufacturing | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the OT Security Engineer with the vCISO, the process owners named in `bia.csv`, and both Plant Managers | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Plant 1 (distribution transformers), Plant 2 (power transformers), engineering, supply chain, field service, Digital Services (the Fleet Monitoring Service, FMS), sales, and corporate functions. It rates 18 business processes and puts a dollar value on what an outage costs, along with its operational, contractual, regulatory, and safety effects.

No law requires this company to have a contingency plan. The BIA supports:
- the CSF 2.0 benchmark outcomes ID.AM-05, ID.IM-04, and RC.RP-01 to RC.RP-05 (P03);
- the FIPS 199 availability rating and contingency controls in the SSP for the ERP and Production Scheduling Platform (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery objectives for each landing zone account in the cloud control map (P04);
- the recovery order in both incident runbooks (P08);
- the FMS availability commitment and the Availability criteria in the SOC 2 readiness assessment (P09);
- delivery commitments in utility supply agreements, the storm-restoration slot program, and the three federal contracts.

## 2. System and business description
The company builds liquid-filled transformers for about 120 utilities and three federal sites, on two Florida campuses with two production shifts each. Revenue is about $360 million a year over about 250 production days. Work flows from the ERP and APS (SYS-01) through the integration platform (SYS-03) to the MES at each plant (SYS-05), then to the plant control systems (SYS-06) and test systems (SYS-07). Designs live in the PLM vault (SYS-04). The FMS (SYS-13) runs in its own cloud account. Plant 2 was acquired in 2024 and is not yet integrated: its OT network is flat and its MES is dual-homed (see `../00_company-facts.md` sections 3, 4, and 7, and the SSP in P02).

## 3. Impact categories and values
Dollar values are scaled to about $360 million of annual revenue: about $836,000 of Plant 1 shipments and $520,000 of Plant 2 shipments per production day, about $68,000 of field service and repair, and about $16,000 of FMS subscription revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $1,500,000 (about 1 production day of shipments) | $300,000 to $1,500,000 | Less than $300,000 |
| Operations | A plant stops, or storm-restoration orders slip | One work center, one product line, or one support function stops | Staff slowed but working |
| Regulatory and contractual | A missed utility addendum notice, a certified test report whose data integrity is in doubt, a missed FAR reporting clock, or an FMS service commitment breached for a subscriber | A missed contractual date or record-keeping requirement | Internal policy deviation |
| Safety | Plausible worker injury (heat, vacuum, hot oil, high voltage) or an unsafe product or advisory reaching a utility | Safety control degraded, manual safeguards in use | None |
| Reputation | A utility suspends a supply agreement or FMS subscription, or regional media coverage during storm response | Customer complaints or a supplier scorecard downgrade | Internal only |

**How loss at MTD was estimated.** The company is capacity-constrained with a long backlog, so most lost production is deferred rather than lost. Estimated loss is the part that is not recovered in the fiscal year plus extra labor, restart costs, and penalties, over the MTD. The process owners estimated that about 30% of lost Plant 1 output and 20% of lost Plant 2 output is not recovered, because both plants already run overtime. Delayed shipments and invoicing are shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-06 Vapor-phase drying and vacuum oil processing | Plant 2 | High | 24 | 12 | 24 | $225,000 |
| 2 | BP-03 Drying, tanking, and oil fill | Plant 1 | High | 24 | 12 | 24 | $290,000 |
| 3 | BP-14 FMS ingestion, analytics, and advisories | Digital Services | High | 24 | 8 | 1 | $50,000 |
| 4 | BP-13 Field service, storm response, and utility access notices | Field service | High | 24 | 12 | 24 | $45,000 |
| 5 | BP-04 Routine testing and certified test reports | Plant 1 | High | 24 | 12 | 1 | $90,000 |
| 6 | BP-01 Production scheduling and work order release | Both plants | High | 48 | 24 | 4 | $150,000 |
| 7 | BP-07 High-voltage testing and certified test reports | Plant 2 | High | 48 | 24 | 1 | $160,000 |
| 8 | BP-02 Core cutting and coil winding | Plant 1 | High | 48 | 24 | 24 | $310,000 |
| 9 | BP-05 Core, winding, and core-coil assembly | Plant 2 | High | 72 | 48 | 24 | $210,000 |
| 10 | BP-10 TMU configuration and product software release | Engineering | Moderate | 72 | 48 | 24 | $40,000 |
| 11 | BP-11 Procurement, inventory, and supplier EDI | Supply chain | Moderate | 72 | 48 | 4 | $75,000 |
| 12 | BP-12 Shipping, heavy-haul logistics, and export screening | Supply chain | Moderate | 72 | 48 | 4 | $140,000 |
| 13 | BP-09 Order engineering and design | Engineering | Moderate | 72 | 48 | 24 | $60,000 |
| 14 | BP-15 Order entry, quoting, and customer service | Sales | Moderate | 72 | 48 | 4 | $30,000 |
| 15 | BP-18 Federal contract and trade compliance | Corporate | Moderate | 72 | 48 | 24 | $15,000 |
| 16 | BP-08 Tank fabrication and welding | Both plants | Moderate | 120 | 72 | 24 | $120,000 |
| 17 | BP-16 Finance, billing, and collections | Corporate | Moderate | 120 | 72 | 24 | $40,000 (plus $7.2 million of invoicing delayed) |
| 18 | BP-17 Payroll, HR, and recruiting | Corporate | Low | 120 | 72 | 24 | $20,000 |

**Summary:** 9 High, 8 Moderate, and 1 Low process (18 in total). The sum of estimated losses at each process's MTD is $2,070,000.

**Enterprise-wide scenario.** If ransomware stopped both plants and the ERP for 5 production days, about $6.8 million of shipments would be deferred. About $1.8 million of that would not be recovered this fiscal year (Plant 1 about $1,254,000; Plant 2 about $520,000). Restarted drying cycles, overtime, heavy-haul rebooking, and service credits would add about $0.5 million. About $7.2 million of invoicing would also be delayed. Incident response and notification costs come on top (see P01 R-001 and R-002).

**What drives the values:**
- **Worker safety drives BP-03 and BP-06.** Every transformer passes through a drying oven and oil processing. An interrupted drying cycle must restart, and a control system whose integrity is in doubt creates heat, vacuum, and hot oil hazards. Their 12-hour RTOs are the shortest on the plant floor.
- **Product integrity drives BP-04 and BP-07.** No transformer ships without a certified test report signed by Quality. The 1-hour RPO reflects that losing test data means repeating tests that take hours.
- **Customer commitments drive BP-13 and BP-14.** Storm crews and FMS urgent alerts matter to utilities within a day. The FMS also carries a written 99.5% monthly availability commitment.
- **Contract clocks keep running during an outage.** BP-10, BP-13, and BP-18 are rated Severe for regulatory and contractual impact because the utility addendum notices (24 or 48 hours for incidents; 1 business day for access) and the FAR reporting clocks do not pause while systems are down.
- **Work-in-process buffers set the production MTDs.** The MES holds about 2 shifts of released work (BP-01, 48 hours). Plant 1 has about 1 day of cut cores and coils ahead of assembly (BP-02, 48 hours); Plant 2 has about 2 days (BP-05, 72 hours).

## 5. Key findings
1. **Plant 2 cannot meet its RPO or RTO today.** BP-05 and BP-06 assume a 24-hour RPO for PLC programs and recipes, but Plant 2 programs exist only as hand copies on the Plant 2 Controls Lead's laptop, and no OT restore has ever been tested (gap 4; P01 R-006). Plant 1 has nightly automated OT backups, but they have not been restore-tested either.
2. **The ERP RTO of 24 hours is a target, not a demonstrated capability.** Immutable copies sit in the separate backup account, which is the strongest recovery control in the company, but only a file-level restore has been tested (2025). A full rebuild of the ERP account from the backup account has never been exercised (P01 R-002; P07 CP-4).
3. **The Plant 2 MES is a single point of failure that bridges office and plant.** It serves BP-01, BP-05, and BP-07 and is dual-homed, so an office incident at Plant 2 can take the plant down with it (gap 1; P01 R-001).
4. **The FMS availability commitment has no tested recovery behind it.** BP-14 needs an 8-hour RTO and 1-hour RPO. Daily backups to the backup account support neither, and the FMS has no recovery runbook (gap 9; P01 R-024; P09 A1.2 and A1.3).
5. **There are no written OT manual-operation procedures at Plant 2.** The workarounds for BP-05 to BP-07 were described by the process owners but are not documented or exercised. Plant 1 wrote its procedures with the 2025 OT DMZ project.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 ERP and APS (ERP production account) | Orders, bills of materials, purchasing, inventory, shipping, export screening, finance, finite-capacity schedule | BP-01, BP-09, BP-11, BP-12, BP-15, BP-16, BP-18 |
| SYS-02 Identity provider | Single sign-on and MFA for email, ERP, cloud consoles, VPN, FMS administration | All office processes; BP-14 |
| SYS-03 Integration platform | Work orders to both MES instances and confirmations back; EDI exchange | BP-01, BP-11 |
| SYS-04 PLM vault and CAD | Designs, calculations, winding specifications, customer drawings; nightly backup to the backup account | BP-02, BP-05, BP-09 |
| SYS-05 MES (Plant 1 in the OT DMZ; Plant 2 dual-homed) and 62 kiosks | Dispatch, electronic travelers, confirmations, test data collection | BP-01 to BP-08 |
| SYS-06 Plant control systems | Core lines, winding machines, drying ovens, oil processing, cranes, weld cells, 90 HMIs and engineering workstations | BP-02, BP-03, BP-05, BP-06, BP-08 |
| SYS-07 Test systems | 8 Plant 1 test stations; Plant 2 high-voltage test bay with 6 test PCs | BP-04, BP-07 |
| SYS-08 Plant historians | Oven, winder, and test process records | BP-03, BP-06 |
| SYS-09 IT endpoints and networks | 640 laptops and desktops, SD-WAN, site firewalls, file servers | All |
| SYS-10 EDI network provider | Purchase orders, advance ship notices, invoices | BP-11, BP-12 |
| SYS-11 Productivity suite | Email, files, chat | BP-09, BP-10, BP-13, BP-15 to BP-18 |
| SYS-12 Product software and firmware pipeline | Configuration software source, build, signing, firmware library, download portal | BP-10, BP-13 |
| SYS-13 FMS (FMS production account) | Ingestion, time-series data, AI-003 analytics, customer portal; daily backups to the backup account | BP-14 |
| SYS-14 SIEM and EDR (MSSP) | Detection and validation of clean recovery | Recovery of all processes |
| SYS-16 HR, payroll, and applicant tracking SaaS | Payroll, HR records, recruiting | BP-17 |
| Backup account (second region) | ERP, FMS, and PLM copies with 35-day write-once retention and separate administrator credentials | BP-01, BP-09, BP-14, and all ERP-dependent processes |
| Plant 1 OT backup server (OT DMZ) and offline media | Nightly controller program backups, weekly offline copy | BP-02, BP-03 |
| Third parties | Cloud provider, SD-WAN provider, ERP software vendor, MSSP, EDI provider, OEMs (ovens, winders, core lines, test systems), TMU electronics supplier, heavy-haul carriers, payroll provider | As listed in `bia.csv` |
| Facilities and people | HQ and Plant 2 server rooms, standby generators at both plants, the two Controls Leads (single points of OT knowledge per plant), the OT Security Engineer, test engineers, reliability engineers | All |

## 7. Recovery priorities
The order puts worker safety first, then the shared services everything else needs, then the processes with the shortest RTO. The FMS recovers in parallel because it runs in its own cloud account and has its own team.

| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 drying ovens and oil processing at both plants (BP-03, BP-06): confirm safe state, run stored recipes from local PLCs | 12 h | Safe shutdown if HMI integrity is in doubt; reload verified programs (Plant 1 from the OT backup server; Plant 2 from the laptop copy until POAM-006 closes) |
| 2 | SYS-02 identity provider, break-glass accounts, and the corporate directory (Plant 2 trust kept disabled) | 2 h | Two sealed break-glass accounts per administrative plane |
| 3 | SYS-09 SD-WAN, site firewalls, and the cloud hub; IT/OT firewalls rebuilt deny-by-default | 4 h | Cellular failover at both plants; second internet carrier at HQ |
| 4 | SYS-13 FMS (BP-14), restored in its own account | 8 h | Reliability engineers call subscribers about known urgent cases |
| 5 | SYS-14 SIEM and EDR console | 8 h | The MSSP runs from its own platform; needed to validate clean recovery |
| 6 | SYS-07 test systems (BP-04, BP-07) | 12 h (Plant 1), 24 h (Plant 2) | Test systems run offline; Quality signs from raw data |
| 7 | Field laptops and contact lists (BP-13) | 12 h | Printed utility contact list; offline laptops |
| 8 | SYS-01 ERP and APS (BP-01) | 24 h | Printed 5-day schedules; restore from the backup account into a clean ERP account |
| 9 | SYS-05 MES (Plant 1 from its OT DMZ backup; Plant 2 rebuilt single-homed on the plant side) | 24 h | Paper travelers from the traveler kits |
| 10 | SYS-03 integration platform | 24 h | Manual work order release by planners |
| 11 | SYS-06 core and winding HMIs (BP-02, BP-05) | 24 h (Plant 1), 48 h (Plant 2) | Manual recipe entry from printed winding sheets with an engineering double-check |
| 12 | SYS-12 firmware library and configuration software (BP-10) | 48 h | Verified offline copy held by the VP Engineering |
| 13 | SYS-04 PLM vault (BP-09) | 48 h | Released drawings in the traveler kits; hold new designs |
| 14 | SYS-10 EDI connectivity (BP-11, BP-12) | 48 h | Phone and email orders to the top 20 suppliers; paper bills of lading |
| 15 | SYS-06 plasma cutters and weld cells (BP-08) | 72 h | Manual welding; outside tank fabricator |
| 16 | Finance (BP-16) and payroll and HR SaaS (BP-17) | 72 h | Manual invoices; repeat prior payroll |

The recovery order is carried into both P08 runbooks and is to be proved in the restore tests on the P07 POA&M (POAM-005 and POAM-006).
