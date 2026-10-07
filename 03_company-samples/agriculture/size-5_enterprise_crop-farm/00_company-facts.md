# Scenario facts: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | Diversified precision-agriculture crop farm (NAICS 111998, All Other Miscellaneous Crop Farming). Fresh vegetables (tomatoes, bell peppers, cucumbers, sweet corn, green beans), berries (strawberries, blueberries), melons (watermelons, cantaloupes), and row crops in rotation (peanuts, cotton, field corn). No single crop family is the majority of crop value. Runs connected irrigation and fertigation, GNSS-guided equipment, camera drones, and an enterprise farm management platform |
| Location | Headquartered in Florida. 48 farms (primary production farms) in 6 operating regions across Florida, Georgia, South Carolina, and North Carolina, about 310,000 farmed acres (about 118,000 acres of produce and 192,000 acres of row crops; about 205,000 acres irrigated). 14 on-farm packinghouses and coolers, 3 regional packing and cooling hubs, grain and peanut drying and storage on 5 farms, 6 regional irrigation control centers, and 2 company data center campuses. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | Up to 12,000 employees at the seasonal peak: about 4,700 year-round employees (about 1,050 of them in corporate and regional offices) and up to 7,300 seasonal workers, of whom about 5,600 are employed under the H-2A temporary agricultural worker program (about 60 labor certifications a year) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day on average, concentrated in the November to July harvest seasons (peak harvest weeks exceed $25 million a day). Above the SBA size standard of $2.5 million for NAICS 111998 (13 CFR 121.201) |
| Sales channels | National and regional retail grocery chains (about 52% of revenue), foodservice distributors (about 24%), terminal markets and wholesalers (about 6%), row crop buyers such as peanut buying points, cotton merchants, and grain elevators (about 11%), grower services for contract and independent growers (about 5%; see P09), and a direct-to-consumer produce box subscription (about 2%) |
| Customer terms | Retail and foodservice supplier agreements require notice within 24 hours of any event that could affect product safety, lot traceability, or committed volumes; an annual third-party food safety audit at every packing site; case-level traceability labels; and EDI ordering and advance ship notices |
| Card payments | The produce box subscription (about 38,000 active subscribers, all in Florida and Georgia) runs on an e-commerce SaaS with the processor's hosted payment page. No card numbers are stored on or pass through company-managed systems. The acquirer requires an annual PCI DSS self-assessment questionnaire |
| USDA programs | Farm Service Agency farm records and acreage reports; federal crop insurance on peanuts, cotton, field corn, and some vegetables through approved insurance providers; Natural Resources Conservation Service conservation contracts that cost-share irrigation efficiency upgrades |
| Food safety status | A **covered farm** under the FDA Produce Safety Rule (21 CFR Part 112): produce sales far exceed the inflation-adjusted $25,000 threshold (112.4(a)), and the farm is not eligible for the qualified exemption, which requires all food sales under $500,000, adjusted for inflation (112.5(a)(2)). Peanuts and sweet corn are on the rarely-consumed-raw list (112.2(a)(1)), and cotton and field corn are not produce, so the Rule's standards apply to the other crops. Produce Safety records live in the farm management platform (SYS-01) |
| Food Traceability Rule | The company grows, cools, and initially packs foods on FDA's Food Traceability List (fresh tomatoes, peppers, cucumbers, and melons), so 21 CFR Part 1, Subpart S applies to it. The original compliance date was 2026-01-20. FDA proposed to extend it to 2028-07-20 (90 FR 38084, 2025-08-07), and Pub. L. 119-37 directed FDA not to enforce the rule before 2028-07-20 (as FDA states at 91 FR 31723, 2026-05-28). The company runs a readiness program (P03) |
| Farm status under FD&C Act section 415 | Every site meets the farm definition in 21 CFR 1.227: the 48 farms are primary production farms, and the 3 regional hubs are **secondary activities farms**, because company farms grow the majority of the raw agricultural commodities they pack and hold and own a majority interest in the hubs. Farms do not register (21 CFR 1.226(b)). The hubs also pack produce for contract growers (SL-2), so the third-party share at each hub is monitored (section 4, gap 9) |
| Water use | Groundwater and surface water withdrawals under permits from regional water management districts and state agencies. Flow meter data from SYS-02 is the evidence for permit reporting |
| Drones and aerial application | About 140 camera drones (RGB and multispectral) flown under FAA Part 107 by about 58 company remote pilots holding remote pilot certificates (14 CFR 107.12). Aerial application of crop protection products is contracted to commercial agricultural aircraft operators certificated under 14 CFR Part 137; the company flies no application aircraft |
| Cybersecurity regulation | No binding sector-specific federal cybersecurity rule applies (P03 section 1). The company benchmarks against **NIST CSF 2.0**, with **NIST SP 800-82 Rev. 3** for operational technology (OT). As an SEC registrant it must meet the SEC cybersecurity disclosure rules (Form 8-K Item 1.05; 17 CFR 229.106). SOX IT general controls cover ERP and payroll |
| Binding rules that reach farm data | Produce Safety Rule records (21 CFR 112, Subpart O); Food Traceability Rule records (21 CFR 1.1315-1.1455, enforcement from 2028-07-20); H-2A earnings records and statements (20 CFR 655.122(j)-(k)); Worker Protection Standard application and hazard information (40 CFR 170.311(b)); state data security, disposal, and breach notification laws (Florida worked example: Fla. Stat. 501.171) |
| Not in scope | **21 CFR Part 121 (N11-R01):** applies only to facilities required to register under FD&C Act section 415 (21 CFR 121.1); farms do not register (21 CFR 1.226(b)), and farm activities subject to the Produce Safety standards are also exempt (121.5(d)). **Reportable Food Registry (21 U.S.C. 350f):** the duty falls on the responsible party that registers a food facility; the company registers none. **HIPAA:** not a covered entity; the employee group health plan is a separate covered entity handled by the benefits program and is outside these deliverables. **FAR 52.204-21, -23, -25:** no federal prime contracts or subcontracts (the company stopped bidding on USDA commodity purchases in 2024). **State comprehensive consumer privacy laws:** none is enacted in Georgia, South Carolina, or North Carolina according to the repository's cross-sector register (as of 2026-09-25); Florida's Digital Bill of Rights is reported to reach only businesses with more than $1 billion in revenue that also meet further criteria (not verified here); subscribers are only in Florida and Georgia. **CIRCIA:** no final rule as of 2026-09-25 |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; growth by acquisition (2 farm operations acquired in 2025-2026); grower services offered to other farms (two service lines that need SOC 2 reports); Food Traceability Rule readiness; multi-state operations |
| Regulatory driver labels | N11-R01 does not apply (above). `regulatory_driver` columns cite the benchmark as "CSF 2.0 <subcategory> (benchmark)", the OT guide as "SP 800-82r3 <section>", SEC duties as "SEC Form 8-K Item 1.05" or "17 CFR 229.106(<paragraph>)", and binding rules by their own citation, for example "21 CFR 112.161(a)", "21 CFR 1.1455(c)", "20 CFR 655.122(j)", "40 CFR 170.311(b)", and "Fla. Stat. 501.171(<subsection>)". N11-R01 is cited only where 21 CFR 121 is used as a voluntary food defense checklist for fertigation tampering, or where the farm-status monitoring row explains when it would start to apply |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board (audit committee plus a risk committee) | Cyber oversight (Item 106 governance); the risk committee receives quarterly cyber and OT risk reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; chairs the policy governance committee |
| Director of Security Operations | Runs the 24x7 SOC (in-house, with MSSP overflow) |
| Director of OT Security | Reports to the CISO with a dotted line to the Vice President, Irrigation and Water Resources; owns the OT remote access gateway, OT monitoring, and the OT patch program |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Internal Audit (third line); reports functionally to the audit committee |
| General Counsel | Chairs the disclosure committee; breach notification decisions with the Chief Privacy Officer |
| Chief Privacy Officer (in the Legal department) | Employee, H-2A worker, grower, and consumer personal information; breach determinations |
| Chief Operating Officer | Business owner of farm operations; authorizing official for the FMICP (P02) |
| Chief Food Safety and Quality Officer | Produce Safety program, traceability readiness, retailer audits, and farm-status monitoring |
| GRC team (7), SOC (24x7), Internal Audit (in-house, with a co-sourced OT assessment firm) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Formed in 2025; reviews and tiers every AI use case (P10) |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise farm management information system (FMIS), vendor-hosted SaaS, one enterprise tenant | Field and crop plans, crop protection and nutrient application records, Produce Safety records, harvest and field tally (H-2A earnings records), lot codes, yield maps, and the irrigation planning module. About 2,900 year-round users plus up to 3,900 seasonal crew leads and scouts. Single vendor for all 48 farms. The vendor issues a SOC 2 Type 2 report |
| SYS-02 | Irrigation and fertigation control system (OT) | Central SCADA master servers (primary at DC-1, standby at DC-2); 6 regional irrigation control centers with operator HMIs and engineering workstations; about 410 pump station PLCs; about 140 fertigation and chemigation injection skids with safety interlocks; about 2,300 center-pivot control panels with cellular modems; about 18,000 drip-zone valve controllers on about 520 LoRaWAN gateways; about 22,000 soil moisture probes; about 1,900 flow meters; about 260 weather stations (about 45,500 OT and IoT devices). Field links: one carrier's private cellular APN (about 80% of field devices), company licensed radio, LoRaWAN, and fiber near facilities |
| SYS-03 | Identity platform (SSO, MFA, privileged access management, identity governance) | Acquired operations AQ-01 and AQ-02 still use legacy directories |
| SYS-04 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 company data center campuses (DC-1 Florida headquarters, DC-2 Georgia operations center) | Cloud provider A: farm data hub and historian replica, traceability data service, grower data platform (SL-1). Cloud provider B: drone imagery pipeline, analytics, and AI services. DC-1 and DC-2: SCADA masters, OT DMZ, packing site servers' backups, network core |
| SYS-05 | Enterprise network: SD-WAN to about 64 sites; OT DMZ and OT firewalls at the 6 regional control centers | Legacy flat networks at 6 AQ-01 farm offices |
| SYS-06 | About 6,200 laptops, desktops, and servers; about 6,500 rugged tablets and phones | Seasonal tablets are reissued each season |
| SYS-07 | Packing, cooling, and cold-chain OT at 17 packing sites (14 on-farm packinghouses and 3 hubs) | Packing line controllers, optical graders, refrigeration controllers, cold-chain sensors, case label printers, packing line management software |
| SYS-08 | Grain and peanut drying and storage OT (5 farms) | Dryer and bin monitoring controllers |
| SYS-09 | Equipment telematics, GNSS guidance, and the company RTK network | About 1,450 connected tractors, harvesters, and sprayers on 3 equipment dealers' telematics portals (dealer technicians have remote diagnostic access); 64 company RTK base stations |
| SYS-10 | Drones and imagery | About 140 drones; imagery to Cloud provider B |
| SYS-11 | ERP, payroll, HR, and H-2A program records (SaaS) | SOX-relevant; payroll provider holds Social Security numbers, bank accounts, and H-2A passport and visa data |
| SYS-12 | Sales and customer systems: EDI with retail and foodservice customers, order management, transport management with refrigerated carriers, and the e-commerce SaaS for the produce box | About 1,100 vendors in total, 190 with system access or sensitive data, tiered by the third-party risk program |

AI portfolio: 11 use cases governed by the AI governance committee (P10).

**SSP system (P02):** the *Farm Management and Irrigation Control Platform (FMICP)*: the company-managed configuration of the FMIS tenant (SYS-01), the irrigation and fertigation control system (SYS-02: SCADA masters, the 6 regional control centers, and field OT at pump stations, pivots, drip zones, and fertigation skids), the farm data hub and historian workload on Cloud provider A, and the OT network zones, inheriting common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A program aligned to CSF 2.0 (current CSF Tier 3 Repeatable for IT, Tier 2 Risk Informed for OT)
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC, with passive OT network monitoring at the 6 regional control centers
- PAM for IT administrators, and an OT remote access gateway (jump hosts with MFA and session recording) in the OT DMZ
- Quarterly access certification for corporate systems
- Immutable backups for cloud workloads; SCADA configuration and PLC program backups at DC-1 and DC-2
- Annual DR tests for tier-1 systems
- Tiered vendor reviews
- Annual SOC 2 Type 2 report for the grower data platform (SL-1) since 2025
- SEC Item 106 disclosure in the 10-K
- IT and OT segmentation through OT DMZs at the 6 regional control centers for all legacy company farms
- Written manual irrigation and freeze-protection procedures for every region, drilled each November
- Produce Safety records in the FMIS; third-party food safety audits passed at all 17 packing sites in 2026

**Targeted gaps:**
1. **Acquisition integration.** AQ-01 (acquired 2025-09) and AQ-02 (acquired 2026-03) still run legacy identity directories. AQ-01's 6 farm offices are on flat networks. AQ-02's center pivots are controlled through a pivot manufacturer's cloud service with shared logins and no MFA, outside the OT remote access gateway.
2. **OT third-party remote access.** 2 of the 5 irrigation integrators still connect through their own remote tools outside the gateway, and the 3 equipment dealers keep standing remote diagnostic access to the telematics portals.
3. **OT visibility and vulnerabilities.** Passive monitoring covers the control centers and 120 of 410 pump stations. The field device inventory is about 78% complete. About 1,300 pivot panel modems run firmware with known vulnerabilities.
4. **Seasonal workforce identity.** Up to 7,300 seasonal accounts a season. Deprovisioning lags after season end, and AQ-01 crews still share tally tablet logins, so some H-2A earnings records cannot be tied to a person.
5. **Concentration.** One FMIS vendor serves all 48 farms; one carrier's private APN carries about 80% of field OT traffic; the SCADA master restore took 9.5 hours against a 6-hour RTO in the 2026-05 DR test.
6. **Traceability readiness.** Key data elements for Food Traceability List foods are split across the FMIS, packing line software, and EDI. A 2026 mock FDA request produced the 24-hour sortable spreadsheet for only 2 of the 4 FTL commodity groups.
7. **AI.** 11 AI use cases, 7 reviewed by the AI governance committee. The yield prediction model (AI-001) now feeds crew planning and draft H-2A job orders, so it was re-tiered High in 2026-07, and its bias testing is incomplete.
8. **Materiality.** The materiality playbook has never been exercised with an OT outage scenario, and the disclosure committee has 3 new members since 2026-02.
9. **Farm status monitoring.** The third-party share of produce packed at each hub is tracked in a spreadsheet. The grower services growth plan would push Hub 2 above a majority of third-party produce in 2027, which would end its farm status and require FDA registration.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | NIST CSF 2.0 (all 106 subcategories) as the benchmark, with SP 800-82 Rev. 3 applied to OT, plus every binding rule that reaches the company's data and disclosures: SEC Form 8-K Item 1.05 and Item 106, Produce Safety records, Food Traceability Rule readiness, H-2A records, Worker Protection Standard records, FAA Part 107 records, state breach and data security laws (Florida worked example), and PCI DSS by contract. N11-R01 documented as not applicable, with the farm-status trigger that would change that |
| P08 | Ransomware on farm-management and irrigation control systems during the strawberry freeze season, with theft of payroll and H-2A worker files, an OT safe-state step, an **SEC materiality assessment and 8-K Item 1.05** step, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients: SL-1 grower data platform and SL-2 grower packing, cooling, and traceability services |
| P10 | Enterprise AI portfolio (11 use cases), with the AI governance committee operating model and a full assessment of AI-001 computer-vision crop yield prediction |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; AWS, Azure, and Google Cloud names appear only in the P04 equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit with a co-sourced OT assessment firm; OT testing in scheduled maintenance windows) |
| 2026-09-10 | Results to the risk committee of the board |

## 7. Facts added for the deliverables

These facts were added while building the deliverables. They do not change sections 1-6.

**Sites and volumes.** About 64 SD-WAN sites: 48 farm offices, 3 regional hubs, 6 regional offices with irrigation control centers, DC-1 (headquarters campus), DC-2 (Georgia operations center), and 5 equipment and drone hubs. The 17 packing sites ship about 1,900 truckloads a week at peak. Revenue of about $4.8 billion a year is about $13.2 million per calendar day.

**Regions.** R1 Central Florida (headquarters, strawberries, tomatoes, peppers), R2 South Florida (winter vegetables and melons), R3 North Florida (blueberries, watermelons, row crops), R4 South Georgia (vegetables, peanuts, cotton; includes AQ-01), R5 Coastal Carolinas (tomatoes, peppers, sweet corn, row crops), R6 North Carolina (cucumbers, peppers, and row crops; includes AQ-02). Each region has one irrigation control center.

**Additional roles (titles only).**

| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Compliance Officer | Labor, environmental, and food regulatory compliance program; second line with the GRC team |
| Chief Human Resources Officer | Workforce onboarding, terminations, training records; owns the H-2A program |
| Controller | SOX program owner for financial reporting controls |
| Vice President, Irrigation and Water Resources | System owner of SYS-02 and of the FMICP; water permits |
| Vice President, Digital Agronomy | Business owner of the FMIS (SYS-01), drones (SYS-10), and AI-001; owner of service line SL-1 |
| Vice President, Grower Services | Owner of service line SL-2 and of contract grower relationships |
| Vice President, Packing and Cold Chain | The 17 packing sites and SYS-07 |
| Vice President, Integration Management Office | Integration of AQ-01 and AQ-02 |
| Vice President, Sales and Customer Operations | Retail and foodservice customers, EDI, the produce box |
| Vice President, Corporate Communications | Media, worker, and customer communications during incidents |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Facilities and Physical Security | Physical security of sites, control centers, and pump stations |
| Regional Farm Directors (6) | Farm operations in each region; activate manual irrigation and freeze procedures |
| Director of H-2A and Labor Compliance | H-2A certifications, earnings records, and three-fourths guarantee tracking |
| Director of Identity and Access Management | Identity platform (SYS-03) |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, OT DMZ firewalls, field radio and APN (common control provider) |
| Director of Endpoint and Mobility Engineering | Workstations, rugged tablets, EDR, endpoint baselines (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews (in the GRC team) |
| Director of Fleet and Precision Technology | Telematics, GNSS guidance, RTK network (SYS-09) |
| Chief Remote Pilot | Drone program under Part 107 (SYS-10) |
| FMIS Platform Manager | Day-to-day FMIS tenant administration (reports to the Vice President, Digital Agronomy) |
| Irrigation Control Center Managers (6) | Regional SCADA operations; approve PLC and setpoint changes for their region |
| SCADA Engineering Manager | SCADA masters, PLC program library, engineering workstations |
| Traceability Program Manager | Food Traceability Rule readiness (reports to the Chief Food Safety and Quality Officer) |
| Data Science Lead | Builds and monitors in-house models, including AI-001 |

**Acquired operations.** AQ-01: a South Georgia vegetable and row crop operation (9 farms, about 26,000 acres, about 310 year-round and 900 seasonal workers), acquired 2025-09, integration due 2027-03-31. AQ-02: a North Carolina row crop and cucumber operation (4 farms, about 14,000 acres, about 180 pivots, about 120 year-round and 350 seasonal workers), acquired 2026-03, integration due 2027-06-30. Both are among the 48 farms.

**Irrigation integrators and OT vendors.** 5 irrigation integrators support PLCs and HMIs under service agreements (INT-1 to INT-5). INT-4 and INT-5 still use their own remote tools. The pivot manufacturer's cloud control service (used only at AQ-02) and the 3 equipment dealers' telematics portals are external services.

**Service lines offered to external clients (P09).** SL-1: the grower data platform (agronomy analytics, irrigation scheduling recommendations, and yield reporting), licensed to about 420 contract and independent growers on Cloud provider A; annual SOC 2 Type 2 (Security, Availability, Confidentiality) since 2025. SL-2: grower packing, cooling, and traceability services at the 3 hubs for about 160 contract growers, including lot codes and traceability data that growers' buyers rely on (no SOC 2 report yet).

**Hub third-party shares (2026 year to date).** Hub 1 (Central Florida) 22%, Hub 2 (South Georgia) 31%, Hub 3 (Coastal Carolinas) 18% of raw agricultural commodities packed came from growers outside the company. The company's internal alert threshold is 40%; the farm-status limit is a majority (21 CFR 1.227).

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Chief Operating Officer, and Vice President, Investor Relations, advised by outside securities counsel. The General Counsel and two other members joined in 2026.

**Freeze-protection acreage.** About 9,400 acres of strawberries and blueberries in R1, R3, and R4 use overhead irrigation for freeze protection from December to February. A single unprotected freeze night can destroy most of the open blooms and fruit on those acres.

**Additions from steps 3 to 10 (built 2026-10).**
- **Enterprise risks (P01).** ER-01 Farm operations disruption from cyber and technology events; ER-02 Compromise of worker, grower, and customer information; ER-03 Third-party and concentration risk; ER-04 Integration of acquired operations; ER-05 Worker safety, food safety, and command integrity in OT (tolerance Low); ER-06 Regulatory and disclosure compliance (tolerance Low); ER-07 Financial reporting integrity and fraud (tolerance Low); ER-08 Responsible use of AI. Board-approved risk appetite statement dated 2026-02.
- **Disclosure exercise.** The enterprise ransomware tabletop with an OT outage and the full disclosure committee is set for 2026-11-17 (POAM-012); the November freeze drills in R1, R3, and R4 add a cyber outage injection (POAM-022).
- **Policy set (P06).** 5 policies, 23 standards, 14 procedures, and an exception register (EXC-YYYY-NNN). The policy governance committee is chaired by the CISO.
- **Internal Audit team (P07).** An IT audit manager and three IT auditors, with two OT specialists from the co-sourced OT assessment firm (no other engagement with the company; not an irrigation integrator).
- **SOC 2 (P09).** SL-1 report covers Security, Availability, and Confidentiality (third annual period 2027-01-01 to 2027-12-31). SL-2 first Type 2 adds Processing Integrity (period 2027-04-01 to 2027-09-30). Subservice organizations are carved out.
- **AI portfolio (P10).** 11 use cases: AI-001 yield prediction (in-house, High since 2026-07-15), AI-002 irrigation scheduling recommendations, AI-003 pest and disease detection, AI-004 optical grader classification, AI-005 variable-rate prescriptions (High), AI-006 crew planning and labor demand forecasting (High), AI-007 demand and price forecasting, AI-008 enterprise generative AI assistant, AI-009 SOC alert triage, AI-010 telematics predictive maintenance, AI-011 produce box chatbot (pilot). The AI governance committee is chaired by the Chief Risk Officer.
- **Registry defaults kept.** The primary system, the incident type, and the AI use case from the registry fit this business at Enterprise size and were kept: the FMICP combines the farm management platform and irrigation control (P02); the incident is ransomware on those systems during freeze season (P08); AI-001 is the computer-vision yield prediction model (P10).
