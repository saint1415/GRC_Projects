# Scenario facts: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a diversified precision-agriculture crop farm) |
| Business | Diversified crop farm (NAICS 111998, All Other Miscellaneous Crop Farming): peanuts, strawberries, and vegetables and melons (sweet corn, green beans, bell peppers, watermelons), grown in rotation so that no single crop family is the majority of crop value. Uses connected irrigation, GNSS-guided equipment, camera drones, and farm management software |
| Location | Florida. About 640 farmed acres in two blocks. **Home Block** (about 100 acres: 14 acres of strawberries and about 70 acres of vegetables and melons on drip irrigation, plus the headquarters: office, equipment shop, pump house, packing shed, cooler, and farm stand). **North Block** (about 540 acres of peanuts in rotation under 5 center pivots, 6 miles away, no buildings) |
| Workforce | 15 employees: 8 year-round staff (listed in section 2), 2 crew leads, 1 year-round farm worker, and 4 seasonal farm workers employed under the H-2A temporary agricultural worker program (November to June) |
| Revenue | $1.5 million a year in receipts (fictional), about $4,100 per calendar day on average but concentrated in the December to June harvest season (EV-037). Under the SBA standard of $2.5 million in average annual receipts for NAICS 111998 (13 CFR 121.201), so SBA-small |
| Sales channels | Wholesale produce distributor (about 45% of receipts: strawberries, vegetables, and melons); a peanut buying point (about 35%); direct sales (about 20%: farm stand, online pre-order with on-farm pickup, and weekend U-pick strawberries). Direct sales are paid by card. The distributor's supplier agreement requires notice within 24 hours of any event that could affect product safety, lot traceability, or committed volumes |
| Card payments | Farm stand card terminals are a processor-managed, point-to-point encrypted service. The online store uses the e-commerce vendor's hosted payment page. No card numbers are stored on or pass through farm-managed systems (EV-034). The acquirer requires an annual PCI DSS self-assessment questionnaire, which the Sales and Farm Stand Coordinator completes with the processor's help |
| USDA programs | Federal crop insurance on peanuts through a private crop insurance agent; Farm Service Agency farm records and acreage reports; a 2024 Natural Resources Conservation Service (NRCS) conservation contract that cost-shared the irrigation automation upgrade (soil moisture probes, pivot control panels, flow meters). The farm keeps its own copies of these program documents (EV-036) |
| Food safety status | A **covered farm** under the FDA Produce Safety Rule (21 CFR Part 112), determined in the intake obligations register (FDA-112-O), because its average annual produce sales over the previous 3 years are well above the $25,000 inflation-adjusted threshold in 21 CFR 112.4(a). Produce Safety records (worker training, agricultural water, soil amendments, cleaning and sanitizing, harvest and packing) are kept electronically in the farm management platform (SYS-01). The distributor requires an annual third-party food safety (GAP) audit, passed in March 2026 (EV-035) |
| Water use | Groundwater from 3 wells under a water use permit from the regional water management district. Flow meter records in SYS-01 and SYS-04 are how the farm shows its withdrawals stayed within the permit |
| Cybersecurity regulation | **No binding federal cybersecurity rule applies**, as decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) and restated in P03 section 1. The farm uses **NIST CSF 2.0** as its benchmark, with **NIST SP 800-82 Rev. 3** for the irrigation and pump-house operational technology (OT) |
| Binding rules that reach farm data | From the obligations register: Produce Safety Rule record requirements (21 CFR 112 Subpart O); H-2A earnings records (20 CFR 655.122(j)); Florida's data security, disposal, and breach notice duties (Fla. Stat. 501.171) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **21 CFR Part 121 (N11-R01, FSMA intentional adulteration):** Part 121 applies only to facilities required to register under FD&C Act section 415 (21 CFR 121.1). Farms are exempt from registration (21 CFR 1.226(b)), and this operation meets the primary production farm definition in 21 CFR 1.227 because it only grows, harvests, packs, and holds its own raw agricultural commodities. It would also fall under the very small business exemption (21 CFR 121.3, 121.5(a)) and the exemption for farm activities subject to the Produce Safety Rule (121.5(d)). **Reportable Food Registry (21 U.S.C. 350f):** the duty falls on a "responsible party," the person who registers a food facility (350f(a)(1)); the farm registers no facility. **SEC disclosure rules:** privately held. **FAR 52.204-21 and 52.204-25:** no federal contracts or subcontracts (the NRCS contract is a conservation cost-share agreement, not a procurement contract). **HIPAA:** not a covered entity. **State comprehensive privacy laws:** not analyzed. The farm sells only in Florida, and Florida's Digital Bill of Rights is reported to reach only businesses with more than $1 billion in revenue (threshold not verified here) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (data security, disposal, and breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |
| Regulatory driver labels | The vertical requirement N11-R01 does not apply (above). `regulatory_driver` columns therefore cite the benchmark as "CSF 2.0 <subcategory> (benchmark)", the OT guide as "SP 800-82r3 <section>", and binding rules by their own citation: "21 CFR 112.<section>", "20 CFR 655.122(j)", and "Fla. Stat. 501.171(<subsection>)". N11-R01 is cited only where 21 CFR 121 is used as a voluntary food defense checklist |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner and General Manager (Cris Santos) | Executive owner of the program; signs policies; accepts High and Very High risks; approves the security budget |
| Farm Manager (minority member of the LLC) | Runs field operations, crop plans, harvest, and labor; accepts Moderate risks; business owner of the yield prediction pilot (P10) |
| Operations and Technology Manager | The farm's IT manager. Designated **security lead** (part-time security and compliance duties, about 20% of the role). Administers SYS-01 to SYS-04, manages the MSP and the irrigation integrator, and accepts Low risks |
| Office and HR Manager | Bookkeeping (SYS-10), payroll, onboarding and terminations, H-2A paperwork and earnings records, program documents for USDA |
| Food Safety and Packing Lead | Produce Safety records and the GAP audit; packing shed and cooler; cooler temperature alarms |
| Irrigation Technician | Day-to-day operation of pivots, drip zones, fertigation, and the pump house; can run every pump and pivot manually |
| Equipment and Drone Specialist | Tractors, GNSS guidance, telematics; FAA Part 107 certificated remote pilot who flies the imagery missions for the yield model |
| Sales and Farm Stand Coordinator | Online store, farm stand card terminals, distributor orders, PCI self-assessment questionnaire |
| Crew Leads (2) | Harvest crews and field tally entry on tablets; supervise the 5 farm workers |
| Managed service provider (MSP) | Part-time help desk, endpoint patching, office firewall, backup job monitoring (about 10 hours a month under contract) |
| Irrigation integrator | Installed the pump-house PLC and SCADA human-machine interface (HMI) in 2024; supports them remotely under a time-and-materials agreement |
| Outside parties | Cyber insurance carrier (breach hotline), outside counsel through the insurer panel, CPA firm (tax and annual review), crop insurance agent, H-2A filing agent |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds personal or regulated data? | Notes |
|---|---|---|---|---|
| SYS-01 | Farm management and irrigation software (FMIS): field records, crop plans, application records, harvest field tally, Produce Safety records, yield maps, work orders, and the **irrigation control module** (remote pivot and drip-zone control, schedules, alarms) | Vendor SaaS, web and mobile app | Yes: Produce Safety records, H-2A field tally records (worker names and piece-rate counts) | System of record for farm operations. The vendor provides a SOC 2 Type 2 report (EV-031, reviewed in P09) that states an RTO of 8 hours and an RPO of 1 hour |
| SYS-02 | Identity provider (single sign-on and MFA), included in the productivity suite subscription | SaaS | No (identities only) | Protects SYS-03, the cloud tenant (SYS-04), and the SYS-01 web console. The SYS-01 mobile app does not use single sign-on (EV-004) |
| SYS-03 | Productivity suite (email, files, chat) | SaaS | Yes: payroll exports, H-2A documents, program documents | The shared "Office" file library holds personnel and H-2A files (EV-039) |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes: flow and pump history; drone imagery | Three farm-managed workloads: the **farm data hub** virtual machine (historian that collects PLC, flow meter, and weather station data and syncs it to SYS-01), **imagery object storage** (drone orthomosaics for AI-001), and the **backup vault** (office file share export and data hub backups) (EV-022, EV-023) |
| SYS-05 | Farm networks | On-premises and cellular | In transit | Headquarters firewall, switches, office Wi-Fi, and a packing shed access point; the pump house connects over a buried fiber run to the same switch, on one internal network (EV-010); North Block pivots use cellular modems; a LoRaWAN gateway on the pump house collects soil probe and flow meter data |
| SYS-06 | Endpoints | On-premises and field | Yes (cached) | 8 laptops and 3 desktops (office and packing shed), and 11 rugged tablets and phones (crew leads, scouting, irrigation). Managed by the MSP's endpoint tool, except the tablets, which are enrolled in the productivity suite's basic mobile management (EV-007, EV-008) |
| SYS-07 | Irrigation, pump, and cold-room OT | On-premises (pump house, fields, cooler) | No | Pump-house PLC controlling 3 well pumps (variable-frequency drives) and 2 fertigation injection pumps; SCADA HMI workstation; 5 center-pivot control panels with cellular modems; 24 drip-zone valve controllers; 96 soil moisture probes; 8 flow meters; 2 weather stations; 6 cooler temperature sensors with alarm service. About 145 OT and IoT devices, counted at the intake walk-throughs (EV-015, EV-016) |
| SYS-08 | Equipment telematics and GNSS guidance | Equipment dealer SaaS portal and on-machine displays | Yes: operator sign-in with machine location history (geolocation) | 4 tractors with auto-steer, a sprayer with section control, and a planter with variable-rate control; an on-farm RTK base station; as-applied and yield-monitor data sync to SYS-01. Dealer technicians have remote diagnostic access (EV-030) |
| SYS-09 | Drones and imagery | On-premises devices; imagery to SYS-04 | Incidental (people in fields may appear in images) | 2 camera drones (RGB and multispectral) and a ground-station tablet |
| SYS-10 | Accounting and payroll | Accounting SaaS and payroll provider SaaS | Yes: Social Security numbers, bank accounts, H-2A passport and visa numbers, home-country addresses, earnings records | Payroll provider is a third-party agent under Fla. Stat. 501.171(1)(h) |
| SYS-11 | Sales systems | Card processor service (farm stand) and e-commerce SaaS (online store) | Yes: online customer names, emails, phone numbers, pickup addresses (no card data) | About 2,400 online customer accounts (EV-046) |
| SYS-12 | Agronomy analytics SaaS (computer-vision yield prediction) | Vendor SaaS | Farm operational and yield data | Pilot for the 2025-26 season (EV-029; see P10) |

**SSP system (P02):** the *Farm Management and Irrigation Control Platform (FMICP)*: SYS-01 (farm-managed configuration of the FMIS and its irrigation module), SYS-02 as it protects the platform, SYS-04, SYS-05, the SYS-06 endpoints used to run the farm, SYS-07, and the interfaces to SYS-08, SYS-09, and SYS-12.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the CSF 2.0 benchmark and the binding record rules** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 (all 106 subcategories), with SP 800-82 Rev. 3 applied to the OT subcategories. Secondary: the Produce Safety Rule record requirements (21 CFR 112 Subpart O). Also checked: Fla. Stat. 501.171 and H-2A earnings records (20 CFR 655.122(j)). N11-R01 documented as not applicable |
| P08 incident | Ransomware on farm-management and irrigation control systems, entering through the integrator's remote access account during strawberry harvest, with theft of payroll and H-2A files |
| P09 SOC 2 | The farm is not a service organization. (a) Security-only self-benchmark against the Trust Services Criteria; (b) review of the SYS-01 vendor's SOC 2 Type 2 report |
| P10 AI | Computer-vision crop yield prediction (AI-001) from drone imagery, piloted on strawberries and watermelons in the 2025-26 season |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, walk-throughs of both blocks, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork (off-season; no H-2A workers on site) |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (OT testing on 2026-08-05, outside irrigation run times): operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 | Deliverables and policies approved by the majority owner and General Manager |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
