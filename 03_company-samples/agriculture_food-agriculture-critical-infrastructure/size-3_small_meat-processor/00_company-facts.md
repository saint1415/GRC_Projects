# Scenario facts: Cris Santos Company | Food and Agriculture | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a statute, regulation, or agency publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23), uscode.house.gov, federalregister.gov, and fda.gov on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Business | Further processing of purchased beef and pork carcasses and primals (NAICS 311612, Meat Processed from Carcasses): fresh sausage, smoked sausage, bacon, hams, deli meats, and marinated and injected cuts. No slaughter. A separate **smoked seafood room** (opened March 2023) hot-smokes Florida finfish and makes smoked fish dip |
| Location | Florida. One inland plant: processing building with four lines (Line 1 grinding and stuffing, Line 2 injection and marinating, Line 3 smoked and cooked products with slicing and packaging, Line 4 smoked seafood room), five smokehouses (four meat, one seafood), an ammonia refrigeration engine room, coolers and a freezer warehouse, shipping docks, and a small factory outlet store at the front of the site. The site is not on navigable water and has no Coast Guard (MTSA) security plan |
| Workforce | 250 employees (242 full-time equivalents by the 21 CFR 121.3 method): 150 production, 20 sanitation (third shift), 14 maintenance and refrigeration, 12 food safety and quality assurance, 22 warehouse and shipping, 6 outlet store and customer service, 26 management and administration (including 2 IT staff and 1 controls engineer). Up to 25 agency temporary workers are added for the holiday ham season |
| Revenue | $148 million a year in human food sales (fictional); the smoked seafood room is about $11 million of that. The SBA size standard for NAICS 311612 is 1,000 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | Regional grocery chains and food service distributors in the Southeast (about 85% of sales), the outlet store and a small online store for gift boxes (about 3%), and private-label production for two retailers. No federal contracts or subcontracts |
| USDA FSIS status | **Official establishment** under a federal grant of inspection (Federal Meat Inspection Act). FSIS inspection program personnel are assigned to the plant. HACCP plans (9 CFR Part 417) cover four processing categories under 9 CFR 417.2(b)(1): raw product, ground; raw product, not ground; heat treated but not fully cooked, not shelf stable (bacon); fully cooked, not shelf stable (smoked sausage, hams, deli meats). Sanitation SOPs and a written recall procedure (9 CFR 418.3) are in place |
| FDA status | **Registered food facility** under FD&C Act section 415 (21 CFR 1.225) since February 2023, because the seafood room makes FDA-regulated food. The registration exemption in 21 CFR 1.226(g) covers only facilities "regulated exclusively, throughout the entire facility" by USDA, so it no longer applies. The seafood room operates under FDA's seafood HACCP regulation (21 CFR Part 123). Registration renewal is due between 2026-10-01 and 2026-12-31 (21 CFR 1.230(b), even-numbered years) |
| FSMA Intentional Adulteration rule | **Applies** (21 CFR 121.1). Not a very small business (121.3, 121.5(a)): human food sales are about 15 times the $10 million base figure. A small business under 121.3 (fewer than 500 FTE), whose compliance period ended in 2020. The food defense plan covers the FDA-regulated seafood process and the shared plant systems that can reach it. See P03 section 1 for scope and exemptions |
| Ammonia refrigeration | About 16,000 lb of anhydrous ammonia, above the 10,000 lb threshold quantity in both OSHA process safety management (29 CFR 1910.119, Appendix A) and EPA risk management program rules (40 CFR 68.130). A PSM program exists and is owned by the Maintenance and Refrigeration Manager. These rules are context for risk and incident response here; they are not analyzed in P03 |
| Not in scope | CIRCIA (C-FOOD-AG-R02): proposed rule only; as proposed, the company would be below the size criterion (250 employees against a 1,000-employee SBA standard) and Food and Agriculture has no sector criterion. USCG MTS cyber rule (C-FOOD-AG-R03): no MTSA facility. CFATS: authority lapsed in July 2023 (vertical notes). SEC rules: privately held. FAR 52.204-21/-25: no federal contracts. PCII: the company has never submitted information to DHS under the PCII program |
| Payment cards | The online store uses the e-commerce vendor's hosted payment page, and the outlet uses a vendor-managed encrypting card terminal. No card numbers are stored or processed on company systems. PCI DSS obligations are contractual through the acquirer and are not analyzed here |
| Regulatory driver IDs | C-FOOD-AG-R01 (21 CFR Part 121) is the primary driver. Binding rules outside the vertical registry are cited directly after being read on eCFR: 9 CFR Part 417 (HACCP) and 418 (recalls), 21 CFR Part 123 (seafood HACCP), 21 CFR 1.225-1.230 (registration), 21 U.S.C. 350f (Reportable Food Registry). NIST CSF 2.0 and SP 800-82 Rev. 3 are the voluntary OT benchmark |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice for employee and online customer data, Fla. Stat. 501.171). The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security, food safety, and compliance duties |
|---|---|
| Majority owner (Cris Santos) | Approves the security budget; accepts High and Very High risks |
| General Manager | Executive owner of the security program; accepts Moderate risks; signs policies. The FDA "agent in charge" who signs and dates the food defense plan (121.310) and the "responsible establishment official" who signs HACCP plans (9 CFR 417.2(d)) |
| Food Safety and Quality Assurance (FSQA) Manager | HACCP coordinator (trained under 9 CFR 417.7 and for seafood HACCP); **Food Defense Coordinator and qualified individual** for the vulnerability assessment and plan (completed FDA intentional adulteration training, 121.4(c)); recall procedure owner; decides product holds and FSIS and FDA notifications |
| IT Manager | Security lead for IT and OT, with part-time security and compliance duties; runs the identity provider, cloud tenant, corporate network, and endpoints. One IT Technician reports to the IT Manager |
| Controls Engineer | Owns PLCs, HMIs, SCADA, historian, and the recipe and batch system (MES). Reports to the Maintenance and Refrigeration Manager |
| Maintenance and Refrigeration Manager | Plant equipment and the ammonia refrigeration system; PSM program owner; manages the refrigeration contractor and controls integrator |
| Operations Manager | Production lines and line supervisors; downtime decisions |
| Sanitation Supervisor | Third-shift sanitation and clean-in-place (CIP) of the brine systems |
| Warehouse and Logistics Manager | Coolers, freezer warehouse, trailers, shipping, warehouse management system |
| HR Manager | Onboarding, terminations, training records, temporary staffing agency |
| Controller | Finance, cyber insurance, outlet and online store, payroll vendor |
| External parties | Controls integrator (remote SCADA and PLC support), refrigeration contractor, cold-chain monitoring SaaS vendor, AI vision inspection vendor, EDR vendor's managed detection service (office endpoints only), cyber insurer |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Process control network (OT, Purdue levels 0-2) | On premises | PLCs and 12 HMIs for Lines 1-4, the automated brine and cure dosing skid, the seafood brine tank, CIP valve manifolds, five smokehouse controllers, chilling, slicers, packaging, metal detectors, and checkweighers. **Two HMIs run an unsupported operating system** |
| SYS-02 | SCADA server, process historian, and engineering workstation (OT, level 3) | On premises (plant server room) | Collects CCP data (cook, chill, cold storage temperatures) from SYS-01. The historian audit trail is disabled. PLC program backups are kept only on the engineering laptop |
| SYS-03 | Ammonia refrigeration control system | On premises | Vendor-maintained controller for compressors, evaporators, and ammonia detection. **The refrigeration contractor keeps an always-on cellular modem on it** |
| SYS-04 | Cold-chain monitoring service | Wireless sensors and gateway on premises; vendor SaaS dashboard | 64 sensors in coolers, freezers, the seafood room, and trailers. Alerts by SMS to one on-call supervisor. The gateway sits on the corporate Wi-Fi |
| SYS-05 | Recipe, batch, and lot-coding system (MES) | On premises (plant server room) | Holds formulations (including cure and brine), sends setpoints to the dosing skid and smokehouses, prints lot codes and labels. **Dual-homed on the corporate and control networks.** Shared operator logins |
| SYS-06 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Hosts the food safety records application (electronic HACCP, seafood HACCP, and food defense monitoring records), a historian replica, the traceability and recall database, and the backup vault |
| SYS-07 | Enterprise resource planning (ERP) | SaaS | Orders, purchasing, inventory, accounting |
| SYS-08 | Warehouse management system (WMS) | SaaS | Receiving, putaway, picking, shipping; 30 handheld scanners |
| SYS-09 | Identity provider (single sign-on and MFA) | SaaS | Protects email, ERP, WMS, the cloud console, the records application, and the IT VPN. **Not used by OT systems** |
| SYS-10 | Productivity suite (email, files, chat) | SaaS | The food defense plan and formulations sit on a general file share open to all office staff |
| SYS-11 | Corporate network and endpoints | On premises | Firewall, switches, Wi-Fi; 85 office laptops and desktops, 40 shared production-floor terminals and tablets. EDR with the vendor's managed detection service on office endpoints only |
| SYS-12 | Online store and outlet point of sale | SaaS; vendor-managed terminal | Online customer accounts (name, address, email, password); hosted payment page |
| SYS-13 | AI vision inspection (pilot) | Cameras and edge inference server on Line 3; vendor cloud for model training | Inspects sliced and packaged products for foreign material, seal defects, and label and lot-code errors. Vendor has remote access to the edge server (see P10) |
| SYS-14 | OT remote access paths | Internet-facing | Controls integrator: one shared, always-on VPN account into SCADA without MFA. Refrigeration contractor: cellular modem on SYS-03 |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: SYS-01 to SYS-06 and SYS-14, with their interfaces to SYS-07, SYS-08, SYS-09, SYS-11, and SYS-13.

## 4. Current security posture: partially compliant

**In place today:**
- HACCP plans, Sanitation SOPs, and a written recall procedure under FSIS inspection; a mock recall is run each year
- A seafood HACCP plan for the smoked seafood room
- A written food defense plan (2023) for the seafood process, signed by the General Manager, focused on physical access: badge access to the plant, a locked cure and ingredient room, CCTV at docks, visitor sign-in and escort
- MFA for email, ERP, WMS, the cloud console, the records application, and the IT VPN
- EDR with managed detection on office endpoints; automatic OS patching on office endpoints
- A firewall between the corporate and control networks (with broad rules; see gaps)
- A hardwired CIP interlock on the Line 2 meat brine system that blocks CIP chemical valves while the system is in production mode
- Daily backups of the cloud tenant workloads with 35-day retention
- Nightly backups of SCADA and MES servers to a network storage device
- Cold-chain SaaS alerting for all coolers, freezers, and trailers
- Annual security awareness training for office staff
- Same-day account disablement for office staff through HR tickets
- A cyber insurance policy with a breach hotline

**Missing or weak, found in the 2026 assessments:**
1. The 2023 food defense vulnerability assessment covers physical access only. It does not consider remote or insider manipulation of the brine dosing skid, CIP valve control, or smokehouse setpoints, and it was not reanalyzed after the 2025 changes (new recipe system release and the integrator VPN) (121.130, 121.157).
2. Food defense monitoring, corrective action, and verification procedures exist only for the physical mitigation strategies. Monitoring records are incomplete (3 of 12 sampled weeks missing) and no verification review is recorded (121.140-121.150).
3. There is no OT asset inventory or network diagram. The corporate-to-OT firewall allows broad rules, and the MES server is dual-homed on both networks.
4. The controls integrator uses one shared, always-on VPN account into SCADA without MFA. The refrigeration contractor keeps an always-on cellular modem on the refrigeration controller.
5. HMIs and the recipe system use shared operator logins. Recipe and setpoint changes, including cure (sodium nitrite) and brine formulations, are not attributed to individuals and need no second approval.
6. No security monitoring in OT: no EDR on the SCADA, historian, MES, or engineering hosts; two HMIs run an unsupported operating system; firewall, identity, and cloud logs are kept 30 to 90 days and nobody reviews them.
7. SCADA and MES backups sit on a domain-joined storage device in the same server room and have never been restore-tested. PLC program backups exist only on the engineering laptop.
8. No incident response plan. Nothing links a cyber incident to food safety decisions (product hold, CCP record gaps, FSIS and FDA notification).
9. Electronic CCP records have no documented integrity controls (9 CFR 417.5(d), 21 CFR 123.9(f)): the historian audit trail is disabled, the records application has a shared administrator account, and "signatures" are typed initials.
10. Cold-chain alerts go by SMS to one on-call supervisor with no escalation. The sensor gateway sits on the corporate Wi-Fi. There is no manual temperature log procedure for monitoring outages.
11. Security training reaches office staff only. Production, sanitation, maintenance, and temporary workers get none, and food defense awareness training for seafood room temporary workers lapsed in 2025 (121.4(b)(2)).
12. IT policies are a 2020 manual that was never updated. There is no data classification: the food defense plan and formulations are on a file share open to all office staff.
13. No security requirements or reviews for OT vendors, the cold-chain monitoring vendor, or the AI vision vendor. No vendor SOC 2 report has been reviewed.
14. The AI vision inspection pilot went live on Line 3 in May 2026 without a validation protocol, a defined relationship to the metal detector CCP, or an AI use policy.
15. The refrigeration controller's web interface still uses the manufacturer default administrator password (found during P07 testing on 2026-08-14).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | Plant Production and Cold-Chain Monitoring System (PPCM) |
| P03 regulation | Primary: FSMA Intentional Adulteration rule, 21 CFR Part 121 (applies; the seafood room makes the plant a registered facility). Secondary: FSIS HACCP and recall rules (9 CFR 417.2-417.5, 418.2-418.3) where they touch electronic CCP monitoring and records, with the parallel seafood HACCP record rule (21 CFR 123.9(f)). OT control benchmark: NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) |
| P04 cloud | The cloud tenant (SYS-06) plus the SaaS services around the PPCM, and the on-premises OT connections to it. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | 10 business processes (BP-01 to BP-10). Cold-chain temperature control and monitoring: MTD 2 h, RTO 1 h |
| P07 assessment | 22 controls on the PPCM; testing of OT during the weekend sanitation window |
| P08 incident | Ransomware halting processing lines and cold-chain monitoring |
| P09 SOC 2 | The company is not a service organization. (a) Security-only self-benchmark against the TSC Common Criteria, used to answer grocery-chain customer security questionnaires; (b) review of the cold-chain monitoring vendor's SOC 2 Type 2 report |
| P10 AI | AI-001 AI vision quality inspection on Line 3 (pilot). Also inventoried: AI-002 ERP demand forecasting, AI-003 public generative AI tools (prohibited for restricted data) |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (plant walkthrough 2026-07-15) |
| 2026-08-10 to 2026-08-15 | Control assessment fieldwork (OT testing during the sanitation window on 2026-08-14 and 2026-08-15) |
| 2026-08-21 | SOC 2 self-benchmark and cold-chain vendor report review completed |
| 2026-08-26 | AI risk assessment completed |
| 2026-09-04 | Deliverables approved by the General Manager (Moderate and below) and the majority owner (High) |
