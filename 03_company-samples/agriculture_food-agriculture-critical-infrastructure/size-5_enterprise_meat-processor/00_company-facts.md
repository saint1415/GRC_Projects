# Scenario facts: Cris Santos Company | Food and Agriculture | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or agency publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23), govinfo.gov, federalregister.gov, and uscode.house.gov between 2026-09-26 and 2026-10-04.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; further-processed meat products) |
| Business | Further processing of purchased beef and pork carcasses and primals (NAICS 311612, Meat Processed from Carcasses): bacon, hams, fresh and smoked sausage, hot dogs, deli meats, fully cooked entrees, and marinated cuts, sold under company brands and as private label. No slaughter. One plant also makes **plant-based protein products** (FDA-regulated food) in a separate room |
| Location | Headquartered in Florida. 8 processing plants (PLT-01 to PLT-08) in Florida, Georgia, Alabama, North Carolina, Tennessee, and Texas; 4 refrigerated distribution centers (DC-01 to DC-04) in Florida, Georgia, Tennessee, and Texas; 2 colocation data center sites (COLO-1 Florida, COLO-2 Georgia). **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 9,450 at the plants (production, sanitation, maintenance, FSQA), about 1,250 in distribution and transportation (including about 420 drivers), and about 1,300 at headquarters and regional offices. Up to 900 agency temporary workers are added for the holiday ham and summer grilling seasons |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day and about $18.8 million per production day (255 production days). About 1.6 billion pounds of finished product a year |
| Customers | National and regional grocery chains, club stores, foodservice distributors, and quick-service restaurant chains (about 94% of sales); about 25 private-label and co-manufacturing customers (service line SL-2); about 40 food companies that use the company's cold storage and transportation (service line SL-1); and an online store for gift boxes with about 140,000 consumer accounts nationwide (hosted payment page) |
| SEC status | Publicly traded; large accelerated filer. SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106) apply. SOX IT general controls over the ERP and payroll are tested annually by the SOX program |
| SBA size status | Not small: 12,000 employees against the 1,000-employee SBA size standard for NAICS 311612 (13 CFR 121.201) |
| USDA FSIS status | All 8 plants are **official establishments** under federal grants of inspection (Federal Meat Inspection Act), each with FSIS inspection program personnel assigned, HACCP plans (9 CFR Part 417), Sanitation SOPs (9 CFR Part 416), and written recall procedures (9 CFR 418.3). Each plant runs an annual mock recall |
| FDA status | **PLT-07 (Tennessee) is a registered food facility** (FD&C Act section 415; 21 CFR 1.225) since its plant-based room opened in March 2022. The registration exemption in 21 CFR 1.226(g) covers only facilities "regulated exclusively, throughout the entire facility" by USDA, so it does not cover PLT-07. The other 7 plants make only FSIS-inspected meat products and are exempt from registration under 1.226(g). DC-01 and DC-02 also hold PLT-07's FDA-regulated products; their FDA registration and 21 CFR Part 117 duties are managed by the corporate FSQA program and are outside this analysis |
| FSMA Intentional Adulteration rule | **Applies to PLT-07** (21 CFR 121.1). Not a very small business (121.5(a)) and not a small business (121.3: fewer than 500 full-time equivalent employees, including subsidiaries and affiliates). Businesses other than small and very small businesses had to comply 3 years after the rule's July 26, 2016 effective date (81 FR 34166, May 27, 2016), so the rule applied in full from the first day of plant-based production in 2022. Holding at the DCs is exempt (121.5(b)). The other 7 plants follow **voluntary** functional food defense plans (FSIS guidance), which are not scored as Part 121 compliance |
| FDA preventive controls | PLT-07 is also subject to 21 CFR Part 117 (current good manufacturing practice and preventive controls for human food). The FSQA program owns it; only its record requirements that depend on electronic systems (117.305, 117.315(c)) are analyzed here |
| Ammonia refrigeration | 12 anhydrous ammonia systems (8 plants, 4 DCs), from about 12,000 lb to about 48,000 lb each, all above the 10,000 lb threshold quantity in OSHA process safety management (29 CFR 1910.119, Appendix A) and EPA risk management program rules (40 CFR 68.130). PSM and RMP programs are owned by the Director of Refrigeration and Process Safety. Ammonia is a CERCLA hazardous substance with a 100 lb reportable quantity (40 CFR 302.4); release reporting is in P08. These programs are context for risk and incident response; they are not analyzed in P03 beyond release reporting |
| Not in scope | USCG MTS cyber rule (C-FOOD-AG-R03): no MTSA-regulated facility. CFATS: authority lapsed in July 2023. FAR 52.204-21 and 52.204-25: no federal prime contracts or subcontracts (school and institutional sales go through distributors). PCII: the company has never submitted information to DHS under the PCII program |
| CIRCIA | C-FOOD-AG-R02 is a **proposed** rule only (final rule not published as of 2026-10-04). As proposed (226.2(a)), the company would be covered because it exceeds the SBA size standard for its NAICS code. Tracked as a pending change; reporting to CISA is voluntary today |
| Payment cards | The online store uses the e-commerce vendor's hosted payment page; plant employee stores use vendor-managed encrypting terminals. No card numbers are stored or processed on company systems. PCI DSS obligations are contractual through the acquirer and are not analyzed here |
| Regulatory driver IDs | C-FOOD-AG-R01 (21 CFR Part 121) is the primary driver. Binding rules outside the vertical registry are cited directly after being read on eCFR: 9 CFR Parts 416, 417, and 418 (FSIS), 21 CFR 117.305 and 117.315 (FDA records), 21 U.S.C. 350f (Reportable Food Registry), 40 CFR 302.6 and 355.40-355.42 (release reporting), 17 CFR 229.106 and Form 8-K Item 1.05 (SEC). NIST CSF 2.0 and SP 800-82 Rev. 3 are the voluntary OT benchmark |
| Growth | PLT-08 (Texas) was acquired in October 2025 and is still being integrated (see gap 1) |

## 2. People (role titles only)

| Role | Security, food safety, and compliance duties |
|---|---|
| Board of directors (audit committee and a risk committee) | Cyber risk oversight (risk committee); Internal Audit, SOX, and disclosure controls (audit committee); Item 106 governance |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CEO and quarterly to the board risk committee |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Senior Vice President, Food Safety and Quality Assurance (SVP FSQA) | Corporate FSQA program; enterprise Food Defense Coordinator; decides product holds, recalls, FSIS and FDA notifications with the plant FSQA managers |
| Chief Operating Officer (COO) | Business owner of the 8 plants and 4 DCs; authorizing official for the PPCM (P02) |
| GRC team (10), Security Operations Center (24x7, in-house plus MSSP overflow), OT Security team (6), Internal Audit (in-house, with an OT specialist co-sourced) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Plant process control networks (OT, Purdue levels 0-2) at the 8 plants | About 2,600 PLCs and controllers and 680 HMIs: brine injection and cure (sodium nitrite) dosing skids, CIP valve manifolds, 64 smokehouses and ovens, chilling, slicers, packaging, metal detectors, X-ray inspection, checkweighers. **118 HMIs run an unsupported operating system** |
| SYS-02 | Plant SCADA servers, historians, engineering workstations, and MES edge servers (OT level 3) | One set per plant. **Historian audit trails are disabled at PLT-02, PLT-05, and PLT-08.** 9 engineering workstations run an unsupported operating system |
| SYS-03 | Ammonia refrigeration control systems (12) | Vendor-maintained by three refrigeration contractors. **At PLT-05 one contractor keeps an always-on cellular modem on the controller** |
| SYS-04 | Cold-chain monitoring service | About 3,400 wireless sensors at the 12 sites, telematics on 380 refrigerated trailers, gateways at each site, and the vendor's SaaS dashboard and alerting. One vendor for all sites |
| SYS-05 | Central MES: recipe, formulation, batch, label, and lot management, plus the enterprise historian | Migrated to Cloud provider A between 2025-06 and 2026-02. Holds every formulation (including cure and brine), pushes approved recipes and setpoint ranges to the plant MES edge servers, and prints lot codes and labels. Two-person approval is enforced centrally. **Plant supervisors can override cure and brine setpoints at the HMI within the pushed range without a second approval, and overrides raise no alert** |
| SYS-06 | ERP and payroll (SaaS) | Orders, procurement, inventory, finance, payroll. SOX-relevant |
| SYS-07 | Warehouse management and transportation management systems (WMS and TMS) | DC-01 to DC-04 and fleet dispatch; about 2,100 handheld scanners |
| SYS-08 | Identity platform (SSO, MFA, privileged access management, identity governance) | Covers all IT users at 7 plants, the DCs, and headquarters. **Plant OT uses separate OT directories per plant, federated for named engineering access at 6 plants.** PLT-08 still runs a legacy directory |
| SYS-09 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus COLO-1 and COLO-2 | Cloud provider A: central MES, enterprise historian, food safety records platform, traceability platform, data lake and AI services. Cloud provider B: SL-1 and SL-2 customer portals, e-commerce integration. Colocation: network core, legacy applications, offline backup copies |
| SYS-10 | Enterprise network (SD-WAN at 14 sites) and IT endpoints | About 6,800 IT endpoints including 1,900 shared floor terminals; EDR on IT endpoints |
| SYS-11 | Food safety records platform (Cloud provider A) | Electronic HACCP, Sanitation SOP, food defense (PLT-07), and preventive controls (PLT-07) records with e-signatures; pre-shipment review. Live at 7 plants; **PLT-08 still uses a legacy local eHACCP application with shared accounts** |
| SYS-12 | Traceability and recall platform (Cloud provider A) | Lot genealogy from receiving to customer shipment; recall execution |
| SYS-13 | Customer portals and online store | SL-1 cold storage customer portal and SL-2 co-manufacturing portal (Cloud provider B); online store (e-commerce SaaS with hosted payment page) |
| SYS-14 | AI portfolio (10 use cases) | Governed by an AI council formed in 2025 (see P10) |
| SYS-15 | OT remote access | Enterprise OT remote access gateway (named accounts, MFA, approval, session recording) at 6 plants. **PLT-05 and PLT-08 still have legacy vendor paths** |
| SYS-16 | Third parties | About 1,400 vendors; 65 with OT remote access (controls integrators, equipment makers, refrigeration contractors); tiered third-party risk program |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: the enterprise plant OT standard as deployed at the 8 plants (SYS-01, SYS-02, SYS-03), the central MES and enterprise historian (SYS-05), cold-chain monitoring (SYS-04), the food safety records platform (SYS-11), and OT remote access (SYS-15), inheriting common controls from the enterprise platform.

**Registry defaults kept.** The registry's primary system, incident (ransomware halting processing lines and cold-chain monitoring), and AI use case (AI quality inspection on processing lines) all fit this business. At this size each is broadened: the PPCM covers 8 plant instances plus central services, the incident spans several plants and triggers the SEC materiality step, and AI quality inspection is one use case in a 10-item portfolio.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0 for IT and OT, with an OT Security team under the CISO
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC (in-house plus MSSP overflow); passive OT network monitoring at 6 plants
- OT DMZ and the enterprise OT remote access gateway at 6 plants
- PAM; quarterly access certification for IT systems
- Immutable backups for cloud workloads; annual DR tests for tier-1 systems
- Central MES with two-person formulation approval and a signed master for every formulation
- HACCP plans, Sanitation SOPs, and recall procedures under FSIS inspection at all 8 plants; annual mock recalls
- A Part 121 food defense plan at PLT-07 (reanalyzed 2025-03) and voluntary functional food defense plans at the other 7 plants
- PSM and RMP programs for the 12 ammonia systems
- Tiered vendor reviews
- An SOC 2 Type 1 report (Security, Availability) for SL-1 as of 2025-12-31
- SEC Item 106 disclosure in the 10-K; a disclosure committee with a materiality playbook
- Cyber insurance

**Targeted gaps:**
1. **Acquisition integration.** PLT-08 (acquired 2025-10) is still on a legacy directory and a flat IT and OT network, its controls integrator uses a VPN account without MFA, it has no OT monitoring, and its electronic HACCP records sit in a legacy application with shared accounts. Integration is due 2027-03-31.
2. **OT boundary and remote access.** The OT DMZ and remote access gateway are live at 6 of 8 plants. At PLT-05 a refrigeration contractor keeps an always-on cellular modem on the refrigeration controller. 14 of 65 OT vendors still use legacy paths.
3. **Legacy OT.** 118 of 680 HMIs and 9 engineering workstations run unsupported operating systems. The OT asset inventory is about 91% complete.
4. **Recipe and setpoint integrity.** Plant supervisors can override cure and brine setpoints within the pushed range without a second approval, and overrides raise no alert. The PLT-07 food defense reanalysis (2025-03) predates the central MES migration (completed 2026-02), which was not treated as a reanalysis trigger (21 CFR 121.157(b)(1)).
5. **Cold-chain concentration.** One monitoring vendor serves all 12 sites and 380 trailers. The manual temperature log fallback has been exercised at only 3 of 12 sites, and the vendor's SOC 2 report has an exception on alert delivery.
6. **OT recovery.** Plant OT restores have been demonstrated at 4 of 8 plants. The central MES recovered in 7.5 hours against a 4-hour RTO in the 2026-05-16 DR test.
7. **Electronic CCP records.** Historian audit trails are disabled at PLT-02, PLT-05, and PLT-08, and PLT-08's eHACCP application uses shared accounts (9 CFR 417.5(d)).
8. **Third parties.** Tier-1 OT vendors with a current security review: 71%. Two refrigeration contractor contracts have no security terms.
9. **Materiality.** The 2025-11 disclosure committee tabletop did not include a production halt with product holds and recalls, and the playbook has no method for adding product loss and recall costs to the quantitative factors.
10. **AI.** 10 use cases; 6 have completed council review. At PLT-03, two packaging lines cut manual visual inspection from two inspectors to one in 2026-04 after AI vision inspection went live, without HACCP reassessment or council approval. Three use cases have been tested only on vendor data.
11. **Workforce training.** Plant workforce security awareness completion is 78% (multilingual modules launched 2026-03). At PLT-07, 3 of 25 sampled agency temporary workers at actionable process steps had no food defense awareness training record (21 CFR 121.4(b)(2)).
12. **Default credentials.** P07 testing on 2026-08-13 found the manufacturer default administrator password on the refrigeration controller web interface at DC-03 and on two X-ray inspection systems at PLT-04.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 SSP | Plant Production and Cold-Chain Monitoring System (PPCM), one plan for the enterprise plant standard with 8 plant instances, High categorization, and common control inheritance |
| P03 regulation | All applicable regulations across the enterprise: FSMA Intentional Adulteration rule (21 CFR Part 121, PLT-07) as the primary regulation; FSIS Sanitation SOP, HACCP, and recall rules where they touch electronic records and notification (9 CFR 416.16, 417, 418) at all 8 plants; FDA record rules at PLT-07 (21 CFR 117.305, 117.315(c)); SEC Item 1.05 and Item 106; hazardous substance release reporting; state breach and data security laws (Florida worked example); the NIST CSF 2.0 and SP 800-82 Rev. 3 OT benchmark |
| P04 cloud | Multi-cloud enterprise architecture (two providers, vendor-agnostic) with platform, landing zone, workload, SaaS, and colocation layers, plus the plant OT connections |
| P05 BIA | 17 enterprise business processes (BP-01 to BP-17) with quantified impact and a dependency map |
| P07 assessment | 42 controls on the PPCM and its common controls; Internal Audit; statistical sampling; OT testing at 4 plants during sanitation windows |
| P08 incident | Ransomware halting processing lines and cold-chain monitoring at several plants, with the SEC materiality step and food safety notifications |
| P09 SOC 2 | Type 2 readiness across two service lines: SL-1 cold storage and logistics services and SL-2 co-manufacturing and private label |
| P10 AI | Enterprise AI portfolio (10 use cases) under the AI council, with a full assessment of AI-001 AI quality inspection on processing lines |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (plant walkthroughs 2026-06-15 to 2026-07-10) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit; OT testing during sanitation windows at PLT-03, PLT-05, PLT-07, and PLT-08) |
| 2026-08-21 | SOC 2 readiness review completed |
| 2026-08-26 | AI council portfolio review |
| 2026-09-08 | Executive risk committee approval |
| 2026-09-10 | Results to the risk committee and audit committee of the board |

## 7. Facts added for the deliverables

These facts were added while building the deliverables. They do not change sections 1-6.

**Plants and distribution centers.**
| Site | State | Products and notes | Employees |
|---|---|---|---|
| PLT-01 | Florida | Bacon, hams, smoked meats; SL-2 private label | About 1,500 |
| PLT-02 | Florida | Fresh and smoked sausage | About 1,100 |
| PLT-03 | Georgia | Sliced deli meats and fully cooked products; AI vision inspection on 4 lines; SL-2 private label | About 1,600 |
| PLT-04 | Georgia | Hot dogs and dinner sausages; SL-2 private label | About 1,200 |
| PLT-05 | Alabama | Cured and cook-in hams | About 1,000 |
| PLT-06 | North Carolina | Bacon and precooked bacon | About 1,300 |
| PLT-07 | Tennessee | Fully cooked entrees and meatballs; plant-based protein room (FDA); SL-2 private label | About 900 |
| PLT-08 | Texas | Sausage and marinated meats (acquired 2025-10) | About 850 |
| DC-01 to DC-04 | FL, GA, TN, TX | Refrigerated and frozen distribution; SL-1 cold storage customers use about 20% of capacity | About 830 (plus about 420 drivers) |

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Vice President, Engineering | Owner of the plant OT standard and the central MES (SYS-05); PPCM system owner |
| Director of OT Security | Leads the OT Security team (reports to the CISO); OT security common controls |
| Director of Security Operations | Runs the SOC; incident commander for security incidents |
| Director of Identity and Access Management | Identity platform (SYS-08) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, site and plant boundary firewalls, OT DMZ (with the OT Security team) |
| Director of Third-Party Risk Management | Vendor tiering, security terms, SOC report reviews (in the GRC team) |
| Director of Refrigeration and Process Safety | The 12 ammonia systems; PSM and RMP programs; refrigeration contractors |
| Plant Managers (8) | Plant operations; the PLT-07 Plant Manager is the agent in charge who signs the food defense plan (21 CFR 121.310) |
| Plant FSQA Managers (8) | HACCP coordinators; the PLT-07 FSQA Manager is the qualified individual for the food defense plan (121.4(c)) and the preventive controls qualified individual (Part 117) |
| Plant Controls Engineers | Day-to-day OT administration under the Vice President, Engineering |
| Vice President, Distribution and Transportation | DC-01 to DC-04, the fleet, WMS and TMS; owner of SL-1 |
| Vice President, Co-Manufacturing and Private Label | Owner of SL-2 and its customer portal |
| Vice President, Integration Management Office | Integration of PLT-08 |
| Vice President, Facilities and Corporate Security | Physical security of plants, DCs, and headquarters; badge systems and CCTV (common control provider) |
| Chief Human Resources Officer | Onboarding, terminations, training records, temporary staffing agencies |
| Deputy General Counsel, Privacy | Privacy program; breach determinations for personal information |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Controller | SOX program owner for financial reporting controls |
| Vice President, Corporate Communications | Media and customer communications during incidents |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Data science lead | AI model development and monitoring (P10) |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, SVP FSQA, and Vice President, Investor Relations, advised by outside securities counsel. The SVP FSQA joined in 2026-06 so that product holds and recalls are represented.

**PPCM volumes.** About 4,100 formulations in the central MES; about 1,900 recipe and setpoint-range changes a year; about 210 OT user accounts with write access across the plants; about 3.2 million CCP monitoring records a year across the 8 plants.

**Service lines offered to external clients (P09).** SL-1 cold storage and logistics services: about 40 food company customers, about $160 million a year in revenue, customer portal with inventory, temperature history, and lot data. SOC 2 Type 1 report (Security, Availability) as of 2025-12-31. SL-2 co-manufacturing and private label: about 25 customers, about $620 million a year in revenue, production at PLT-01, PLT-03, PLT-04, and PLT-07; customer portal for production orders, specifications, CCP record packages, and certificates of analysis. Two national retail customers require a SOC 2 Type 2 report including Confidentiality and Processing Integrity by the end of 2027.

**Plant-based room at PLT-07.** Separate room with its own entrance, blending tanks, and forming line; shares the central MES, the plant SCADA and historian, the CIP system, and the ammonia refrigeration with the meat lines. The FSQA program confirmed that none of its products is on FDA's Food Traceability List.

**Online store.** About 140,000 consumer accounts (name, address, email, order history; passwords handled by the e-commerce vendor). Employee personal information (12,000 employees, including Social Security numbers and bank details) sits in the ERP and payroll SaaS.
