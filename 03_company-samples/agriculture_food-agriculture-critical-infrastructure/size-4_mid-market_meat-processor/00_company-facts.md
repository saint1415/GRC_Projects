# Scenario facts: Cris Santos Company | Food and Agriculture | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or agency publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23 through the eCFR versioner API), uscode.house.gov, and federalregister.gov between 2026-09-25 and 2026-10-04.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Further processing of purchased beef and pork carcasses, primals, and trim (NAICS 311612, Meat Processed from Carcasses). No slaughter. Two USDA-inspected plants make bacon, smoked sausage and franks, hams, sliced deli meats, fresh sausage, case-ready beef and pork cuts, and ground beef and pork, sold under the company's brand and as private label |
| Location | Florida only. **Plant 1 (Central Florida, headquarters campus):** 9 processing lines, 8 smokehouses, 2 continuous spiral ovens, 2 brine injectors fed by an automated brine and cure dosing skid, 3 slicing lines, 9 packaging lines, an ammonia refrigeration engine room, coolers, a freezer warehouse, and shipping docks. Corporate offices share the campus. **Plant 2 (North Florida, acquired 2025-03-03):** 2 grinding and blending lines with inline fat analysis, 3 case-ready cutting and tray-packaging lines, a smaller engine room, coolers, and docks. Neither site is on navigable water or has a Coast Guard (MTSA) facility security plan |
| Workforce | 850 employees: Plant 1 about 520 (production 340, sanitation 45, maintenance, refrigeration, and controls 40, food safety and quality assurance 30, warehouse and shipping 45, supervision and administration 20); Plant 2 about 240; corporate about 90 (including 14 in IT and security). Up to 120 agency temporary workers are added for the holiday ham season (October to December). About 40 Plant 2 employees live in Georgia |
| Revenue | About $480 million a year in sales (fictional): Plant 1 about $330 million, Plant 2 about $150 million, over about 250 production days. That is about $1.32 million per production day at Plant 1 and $600,000 at Plant 2 |
| SBA size | The SBA size standard for NAICS 311612 is 1,000 employees (13 CFR 121.201). SBA counts all employees, including agency temporaries, averaged over the pay periods of the preceding 24 completed calendar months, and adds the employees of affiliates (13 CFR 121.106(a), (b)(1); 121.103(a)(6)). On its own count (about 870 on average with temporaries) the company is SBA-small, as the folder README states. Whether the sponsor fund's other portfolio companies are affiliates (common control, 121.103(a)(1)) has not been determined. It matters only for CIRCIA as proposed (P03 section 1), so it is an open item for counsel, not a current obligation |
| Customers | National and regional grocery chains (about 70% of sales, branded and private label), foodservice distributors (about 25%), and club stores (about 5%). Orders, advance ship notices, and invoices move by EDI. 38 customer organizations use the company's customer traceability portal. The largest grocery chain (about 22% of sales) requires an annual third-party food safety certification under a GFSI-benchmarked scheme, a food defense plan, notice within 24 hours of any event that could affect product safety or committed volumes, and, from its 2026 supply agreement, a SOC 2 Type 2 report on the portal and EDI services by 2027-12-31 (P09). No consumer sales, no card payments, no federal contracts or subcontracts |
| USDA FSIS status | Both plants are **official establishments** under federal grants of inspection (Federal Meat Inspection Act), with FSIS inspection program personnel assigned. HACCP plans (9 CFR Part 417) at Plant 1 cover raw product, ground (fresh sausage); raw product, not ground (marinated and injected cuts); heat treated but not fully cooked, not shelf stable (bacon); and fully cooked, not shelf stable (franks, smoked sausage, hams, deli meats) (417.2(b)(1)). Plant 2 covers raw product, ground and raw product, not ground. Sanitation SOPs (9 CFR 416.11-416.17) and written recall procedures (9 CFR 418.3) at both plants. Plant 1 makes post-lethality exposed ready-to-eat products and controls *Listeria monocytogenes* under 9 CFR 430.4(b)(2) (Alternative 2: an antimicrobial agent in the formulation plus food contact surface testing) |
| FDA status | **Not a registered food facility.** Both plants make only FSIS-inspected meat products and are "regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture" (21 CFR 1.226(g)), so they are exempt from FDA registration. The FSMA Intentional Adulteration rule (21 CFR Part 121) applies only to facilities required to register (21 CFR 121.1), so it **does not apply** (P03 section 1). The company follows FSIS food defense guidance voluntarily and uses Part 121's structure as a benchmark for its food defense plans |
| Ammonia refrigeration | Plant 1 holds about 42,000 lb and Plant 2 about 18,000 lb of anhydrous ammonia, each above the 10,000 lb threshold quantity in OSHA process safety management (29 CFR 1910.119(a)(1)(i) and Appendix A) and EPA risk management program rules (40 CFR 68.130). Both processes are subject to PSM, so both are RMP Program 3 (40 CFR 68.10(l)(2)). The Director of Engineering and Maintenance owns both PSM programs. The cyber-relevant PSM and RMP duties (refrigeration controls, alarms, interlocks, management of change, incident investigation, emergency response) are analyzed in P03 |
| Not in scope | **21 CFR Part 121 (C-FOOD-AG-R01):** see FDA status. **Reportable Food Registry (21 U.S.C. 350f):** the duty falls on the responsible party that registers a food facility; the company registers none. **CIRCIA (C-FOOD-AG-R02):** proposed rule only; not in effect. **USCG MTS cyber rule (C-FOOD-AG-R03):** no MTSA facility. **CFATS:** authority lapsed in July 2023. **SEC disclosure rules:** privately held. **FAR cyber clauses:** no federal contracts. **PCI DSS:** no card payments. **HIPAA:** not a covered entity; the employee health plan is fully insured. **PCII:** the company has never submitted information to DHS under the PCII program |
| Regulatory driver labels | C-FOOD-AG-R01 does not apply, so `regulatory_driver` columns cite binding rules by their own citation (for example "9 CFR 417.5(d)", "9 CFR 416.16(b)", "9 CFR 418.2", "9 CFR 430.4(c)(7)", "29 CFR 1910.119(l)", "40 CFR 68.95", "Fla. Stat. 501.171(2)"), the voluntary benchmark as "CSF 2.0 <subcategory> (benchmark)" with SP 800-82 Rev. 3, and contracts as "Customer contract". C-FOOD-AG-R01 is cited only as "C-FOOD-AG-R01 (benchmark: 21 CFR 121.xxx)" where Part 121 is used as a voluntary checklist for the food defense plans, and C-FOOD-AG-R02 only for the proposed CIRCIA duty |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (data security, disposal, and breach notification for employee data, Fla. Stat. 501.171). Plant 2 employees who live in Georgia are handled under "each state where affected individuals reside" in P08, with Florida as the worked example |

## 2. People (role titles only)

| Role | Security, food safety, and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting (chaired by an independent director; two sponsor partners sit on the board) |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and security budget |
| Chief Operating Officer | Executive sponsor of the security program; **system owner of the Plant Production and Cold-Chain Monitoring System (PPCM)**; accepts Moderate risk; chairs the crisis management team |
| Chief Financial Officer | Cyber insurance, treasury, ERP owner; executive sponsor of the SOC 2 effort (P09) |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; SSP review |
| IT Director | IT infrastructure, identity provider, cloud landing zone, networks (including the IT/OT boundary firewalls), endpoints; day-to-day control owner for IT |
| Security Manager plus 1 security analyst and 1 OT security engineer | **Designated security lead** and incident commander; vulnerability management; MSSP liaison. The OT security engineer (hired 2026-03) reports to the Security Manager with a dotted line to the Director of Engineering and Maintenance |
| GRC Analyst | Policies and standards, risk register, vendor reviews, SOC 2 readiness |
| Vice President of Food Safety and Quality Assurance (VP FSQA) | Corporate HACCP authority (trained under 9 CFR 417.7); **food defense coordinator** for the voluntary food defense plans; chairs the recall committee; decides product holds and FSIS notifications with the plant FSQA managers |
| Plant 1 FSQA Manager and Plant 2 FSQA Manager | HACCP coordinators; pre-shipment review; Listeria program (Plant 1) |
| Plant Manager, Plant 1 and Plant Manager, Plant 2 | Each is the "responsible establishment official" who signs HACCP plans (9 CFR 417.1, 417.2(d)) and Sanitation SOPs (416.12(b)); downtime and line restart decisions |
| Director of Engineering and Maintenance | Plant equipment, both ammonia refrigeration systems, and both **PSM programs**; manages the refrigeration contractors |
| Controls Engineering Manager (with 3 controls engineers) | **OT system owner:** PLCs, HMIs, SCADA, historians, the recipe and batch system (MES), and engineering workstations at both plants; manages the controls integrators |
| Director of Supply Chain and Logistics | Coolers, freezer warehouse, shipping, WMS, cold-chain monitoring service, carriers |
| HR Director | Onboarding, terminations, training records, staffing agencies, HR and payroll SaaS |
| General Counsel | Legal decisions, breach determinations with outside counsel, regulatory and customer notices, contracts |
| Vice President of Sales and Customer Service | Customer notices; business owner of the customer traceability portal and EDI services |
| Director of Communications | Staff, customer, and media statements |
| Internal audit (co-sourced firm) | Annual IT audit; independent P07 assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring of IT systems. OT is not monitored by the MSSP today |
| External parties | Plant 1 controls integrator; Plant 2 controls integrator (inherited from the prior owner); two refrigeration contractors (one per plant); cold-chain monitoring SaaS vendor; AI vision inspection vendor; cyber insurer (breach hotline; panel counsel and an OT-capable forensic firm); outside counsel |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Plant 1 process control network (OT, Purdue levels 0-2) | On premises | About 180 PLCs and 64 HMIs: smokehouses, spiral ovens, chillers, brine injectors, the brine and cure dosing skid, CIP systems, slicers, packaging, metal detectors, and x-ray inspection (foreign material CCP on Lines 5-7). **6 HMIs run an unsupported operating system** |
| SYS-02 | Plant 2 process control network (OT, levels 0-2) | On premises | About 60 PLCs and 22 HMIs: grinders, blenders with inline fat analyzers, case-ready cutting, tray packaging, metal detectors. **Flat network shared with the Plant 2 office and the cold-chain gateways.** **3 HMIs run an unsupported operating system** |
| SYS-03 | SCADA servers, process historians, and engineering workstations (OT, level 3) | On premises at each plant | Collect CCP data (cook, chill, cold storage). Plant 1 is behind an OT DMZ (built 2024). **Plant 2's historian audit trail is disabled.** Historian replicas go to the cloud landing zone every 15 minutes |
| SYS-04 | Ammonia refrigeration control systems (one per plant) | On premises | Vendor-maintained controllers for compressors, evaporators, and ammonia detection. Plant 1 contractor access goes through the remote access gateway. **The Plant 2 refrigeration contractor keeps an always-on cellular modem on the controller** |
| SYS-05 | Cold-chain monitoring service | Wireless sensors and gateways on premises; vendor SaaS | About 260 sensors (Plant 1 about 180, Plant 2 about 60, yard trailers about 20). Plant 1 alerts escalate through three roles by app and phone. **Plant 2 alerts go by SMS to one on-call supervisor, and its gateways sit on the office Wi-Fi** |
| SYS-06 | Recipe, batch, lot-coding, and labeling systems (MES) | On premises | Plant 1 MES (virtual servers in the level 3 zone) holds formulations, including cure and brine, sends setpoints to the dosing skid, injectors, and smokehouses, and prints lot codes and labels; formulation releases need two approvals. Plant 2 uses blend recipes stored in the blender HMIs and a standalone label and lot-code server on the flat network. **Shared operator logins at both plants** |
| SYS-07 | Cloud landing zone (4 accounts: identity and security, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Workloads: food safety records application (electronic HACCP, Sanitation SOP, Listeria, and food defense monitoring records), historian replicas, traceability and recall database, customer traceability portal, EDI gateway, data warehouse. Daily backups to the backup account with 35-day write-once retention |
| SYS-08 | Enterprise resource planning (ERP) | SaaS | Orders, purchasing, inventory, costing, accounting. Plant 2 moved onto it on 2026-02-02 |
| SYS-09 | Warehouse management system (WMS) | SaaS | Receiving, putaway, picking, shipping at both plants; 110 handheld scanners |
| SYS-10 | Identity provider (single sign-on and MFA) | SaaS | About 560 workforce accounts (office, supervisors, maintenance, FSQA, IT). Protects email, ERP, WMS, the cloud console, the records application, and VPN. **Not used by OT systems.** Plant 2 OT logins and file shares still use the prior owner's on-premises directory |
| SYS-11 | Corporate and plant IT networks and endpoints | On premises; SD-WAN between sites | Firewalls, switches, Wi-Fi; about 520 laptops and desktops and 160 shared production-floor terminals and tablets. EDR on all managed endpoints (Plant 2 since 2025-11) |
| SYS-12 | SIEM and EDR monitoring | SaaS, operated by the MSSP | Identity provider, cloud, firewall, email, and EDR logs. No OT logs |
| SYS-13 | Productivity suite (email, files, chat) | SaaS | Food defense plans and formulation masters sit in a restricted FSQA library (Plant 1) and a general Plant 2 share open to all Plant 2 office staff |
| SYS-14 | OT remote access | Internet-facing | Plant 1: remote access gateway with MFA, named vendor accounts, and session recording (2025); 2 vendor accounts are always enabled rather than enabled per session. Plant 2: the controls integrator's **shared, always-on VPN account without MFA**, and the refrigeration contractor's modem (SYS-04) |
| SYS-15 | OT network monitoring | On premises, Plant 1 only | Passive sensor installed 2026-01. Alerts go to a local console that the OT security engineer checks weekly; **not sent to the MSSP** |
| SYS-16 | AI systems | Vendors | AI vision inspection on Plant 1 Lines 5-7 (production since 2025-09), ERP demand forecasting, refrigeration predictive maintenance analytics, an enterprise generative AI assistant (pilot), and an applicant ranking feature in the HR SaaS (see P10) |
| SYS-17 | HR, payroll, and timekeeping | SaaS | Employee personal information (Social Security numbers, bank accounts, benefits enrollment) for about 850 employees and agency temporaries' time records |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: SYS-01 to SYS-07, SYS-14, and SYS-15 at both plants, with interfaces to SYS-08 to SYS-12 and the AI vision system in SYS-16.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A security program charter (2024) led by the vCISO, with quarterly reporting to the audit committee since 2025
- Five security policies adopted in 2024; an incident response plan (2024) for IT incidents
- MFA through the identity provider for all workforce accounts, the cloud console, and VPN
- EDR on all managed endpoints with 24x7 MSSP monitoring; SIEM for IT logs
- Plant 1 OT DMZ and firewall rules (2024); remote access gateway with MFA for Plant 1 vendors (2025); passive OT monitoring sensor at Plant 1 (2026)
- Immutable daily backups of cloud workloads in a separate backup account, 35-day write-once retention
- HACCP plans, Sanitation SOPs, recall procedures, and a Listeria program under FSIS inspection; mock recalls twice a year
- Voluntary food defense plans: Plant 1 (2022, physical security) and Plant 2 (the prior owner's 2019 plan)
- PSM and RMP programs for both ammonia systems; hardwired ammonia detection and alarms
- Annual enterprise risk assessment (last July 2025); annual co-sourced internal IT audit
- Annual security awareness training and phishing simulations for workforce members with accounts
- Two-person approval for formulation releases in the Plant 1 MES
- Cyber insurance with a breach hotline

**Missing or weak, found in the 2026 assessments:**
1. Plant 2 is not integrated. Its office, OT, and cold-chain gateways share one flat network, and the prior owner's directory still runs Plant 2 OT logins and file shares.
2. Plant 2 OT remote access uses a shared, always-on integrator VPN account without MFA and an always-on cellular modem on the refrigeration controller. At Plant 1, 2 vendor accounts on the gateway stay enabled between sessions.
3. HMIs and MES use shared operator logins at both plants. HMI setpoint edits (cook cycles, chill targets, dosing rates, fat targets) are not attributed to individuals, and Plant 2 blend recipe changes need no second approval.
4. Electronic CCP and Sanitation SOP records have no documented integrity controls (9 CFR 417.5(d), 416.16(b)). The Plant 2 historian audit trail is disabled, the records application uses typed initials as signatures, and it has a shared administrator account.
5. The OT asset inventory is about 75% complete at Plant 1 (from the passive sensor) and does not exist at Plant 2. 9 HMIs and 2 engineering workstations run unsupported operating systems.
6. OT is not monitored by the MSSP. Plant 1 passive sensor alerts stay on a local console, OT Windows hosts have no EDR or allowlisting, and no OT logs reach the SIEM.
7. OT recovery is unproven. Plant 1 SCADA and MES backups go to an OT backup server that is not offline or immutable, and only the Plant 1 SCADA server has been restore-tested (2025). Plant 2 PLC programs exist only on the integrator's laptops. Disaster recovery tests cover the cloud workloads only.
8. The 2024 incident response plan is IT-only. It has no OT playbook and no link to product holds (9 CFR 417.3(b)), FSIS notification (418.2), or the PSM and RMP emergency response plans. No plant tabletop has been held.
9. Plant 2 cold-chain alerts go by SMS to one supervisor with no escalation, the Plant 2 gateways sit on the office Wi-Fi, and Plant 2 has no manual temperature log procedure for monitoring outages.
10. Third-party risk: 26 vendors have OT, cloud, or data access. OT vendors have never been security-reviewed, no SOC 2 report has been obtained from the cold-chain or AI vision vendors, and most OT vendor contracts lack security and incident notice terms.
11. Access reviews are annual. Privileged access management covers cloud and domain administrators only, not OT or SaaS administrator consoles.
12. The 2024 policies have no OT standards (remote access, change, backup, monitoring). Supporting standards are thin.
13. There is no AI policy or standard. The AI vision system went into production on Plant 1 Lines 5-7 without a defined relationship to the x-ray and metal detection CCP, the HR SaaS vendor enabled applicant ranking by default in 2026-04, and staff use public generative AI tools.
14. Both food defense plans cover physical access only. Neither considers remote or insider manipulation of the dosing skid, injectors, smokehouses, CIP, or blenders, and Plant 2's plan was not updated after the acquisition.
15. Production, sanitation, and maintenance workers and agency temporaries receive food defense awareness at orientation but no security awareness. The June 2026 phishing simulation click rate was 9.4%.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P05 BIA | 18 business processes (BP-01 to BP-18) across Plant 1, Plant 2, and corporate functions, with dollar impact |
| P02 SSP | Plant Production and Cold-Chain Monitoring System (PPCM), identifier CSC-PPCM-01. Categorized High (integrity), SP 800-53B High baseline tailored with the SP 800-82 Rev. 3 OT overlay |
| P04 cloud | Multi-account landing zone (SYS-07) plus the SaaS services around the PPCM and the on-premises connections to it. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P01 risk | One enterprise register with system-level views (PPCM, Plant 2 integration, AI portfolio) and risk appetite statements |
| P03 regulation | All rules that bind the primary business line: FSIS Sanitation SOPs, HACCP, recalls, and Listeria rules (9 CFR 416, 417, 418, 430.4) where they touch electronic monitoring, records, and process control; the cyber-relevant parts of OSHA PSM (29 CFR 1910.119) and EPA RMP (40 CFR Part 68); and Florida data security and disposal (Fla. Stat. 501.171(2), (8)). Applicability decisions for C-FOOD-AG-R01 to R03. NIST CSF 2.0 with SP 800-82 Rev. 3 as the OT benchmark. Evidence sampling |
| P06 policies | 5 policies plus a standards index (including OT standards) |
| P07 assessment | 32 controls on the PPCM by the co-sourced internal audit firm, with sampling; OT testing during sanitation windows |
| P08 incidents | Two incident types: (1) ransomware halting processing lines and cold-chain monitoring (registry default, kept); (2) suspected tampering with process setpoints or formulations through the control system. Integrated with crisis management, legal, food safety, and PSM emergency response |
| P09 SOC 2 | SOC 2 Type 2 readiness for the Customer Traceability and EDI Services (Security, Availability, Processing Integrity), required by the largest customer; plus a vendor SOC 2 review program |
| P10 AI | Portfolio: AI-001 AI vision quality inspection (registry default, kept; in production on Plant 1 Lines 5-7), AI-002 ERP demand forecasting, AI-003 refrigeration predictive maintenance, AI-004 enterprise generative AI assistant, AI-005 applicant ranking in the HR SaaS |

**Registry defaults kept:** the primary system, the ransomware incident, and the AI quality inspection use case all fit a two-plant processor and were kept. P08 adds a second incident type because the tier calls for two, and P10 covers a portfolio because the tier calls for one.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-24 | Risk assessment and gap analysis fieldwork (walkthroughs: Plant 1 on 2026-07-08, Plant 2 on 2026-07-14) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (OT testing in the sanitation windows: Plant 1 2026-08-08 to 2026-08-09; Plant 2 2026-08-15 to 2026-08-16) |
| 2026-08-28 | SOC 2 readiness assessment and vendor SOC 2 reviews completed |
| 2026-09-04 | AI risk assessment completed |
| 2026-09-15 | Results to the audit committee; deliverables approved by the Chief Operating Officer (Moderate and below) and the Chief Executive Officer (High and above) |

## 7. Facts added during the build (fictional; used across P01-P10)

| Topic | Added fact | Used in |
|---|---|---|
| Inventory at risk | Product in coolers and freezers is worth about $9 million at Plant 1 and about $3 million at Plant 2 on a typical day | P05, P01 |
| Sanitation windows | Plant 1: Saturday 22:00 to Sunday 14:00. Plant 2: Saturday 14:00 to Sunday 18:00. OT changes and tests happen only in these windows unless an emergency change is approved | P02, P07 |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and an OT-capable forensic firm. Notice must go through the carrier hotline before incident vendors are engaged | P01, P08 |
| MSSP | 24x7 monitoring; the contract requires a call to the Security Manager within 30 minutes of a high-severity alert | P02, P07, P08 |
| Workforce activity | 74 terminations and 31 transfers of identity provider account holders in the 12 months to 2026-06-30. The last access review finished in January 2026 | P03, P07 |
| Sampling populations | 186 OT change records at Plant 1 and 41 at Plant 2 in 2026 Q1-Q2; 22 privileged identity provider and cloud accounts; 47 OT privileged or engineering accounts (Plant 1 31, Plant 2 16); 64 Critical and High vulnerability findings in 2026 Q1-Q2; 17 security incidents in the 12 months to 2026-06-30; 26 vendors with OT, cloud, or data access | P03, P07, P09 |
| Assessment findings | The x-ray inspection unit on Plant 1 Line 6 still accepts the manufacturer default administrator password on its web service (found 2026-08-08); 4 of 25 sampled terminations were disabled late; 3 Plant 2 operators who left kept working shared passwords that were never changed; 23 of 41 Plant 2 OT change records had no approval; the MSSP test alert was escalated in 22 minutes | P01, P07 |
| Customer traceability and EDI services | The portal and EDI gateway (in the workloads account) serve 38 customer organizations: lot lookups, certificates of analysis, recall notices, and about 1,900 EDI purchase orders and advance ship notices a week | P05, P09 |
| Terminology | "Plant Production and Cold-Chain Monitoring System (PPCM)" is the SSP system in P02, identifier CSC-PPCM-01. "Customer Traceability and EDI Services (CTES)" is the SOC 2 system in P09 | P02, P09 |
| Food safety program details | Mock recalls in 2026-02 and 2026-06 traced lots in 2.5 and 3 hours. 7 Listeria hold-and-test events in 2026 H1. A Plant 1 CIP sequence was changed by OT ticket in 2026-03. Plant 2 HMI and historian clocks drift up to 6 minutes. The Plant 1 Injector 1 brine system has a hardwired interlock that blocks CIP chemical valves in production mode; **Injector 2 does not** | P01, P03, P08 |
| PSM and RMP details | Last PHAs: Plant 1 2022 (revalidation due 2027-04), Plant 2 2021 (due 2026-12). Last compliance audits: Plant 1 2025; Plant 2 2024 by the prior owner, with 3 findings still open. Plant 2 RMP update after the change of ownership filed 2025-08. 24 management of change records in 2025-2026 (18 Plant 1, 6 Plant 2). The Plant 2 ammonia detection panel is not on a generator circuit | P03, P05 |
| Recovery tests | Records application restore-tested 2026-04; Plant 1 SCADA server 2025; no other OT or CTES restore tests | P04, P05, P07, P09 |
| Identity details | 9 accounts with unknown owners in the prior owner's Plant 2 directory; 7 of 31 transfers kept prior OT access; customer portal MFA enforced since 2026-06 | P01, P07, P09 |
| Vendors | Of 26 vendors with OT, cloud, or data access: 12 Tier 1, 8 Tier 2, 6 Tier 3. The cold-chain monitoring vendor and the AI vision vendor have no SOC 2 report; the EDI network provider's report was requested 2026-08-12 | P09 |
| AI details | AI-001 in production on Plant 1 Lines 5-7 since 2025-09; AI-003 since 2026-03; AI-004 pilot for 40 office users from 2026-10; the HR SaaS applicant ranking feature (AI-005) was enabled by the vendor in 2026-04 and disabled 2026-08-20 | P10 |
| FY2027 security budget | Approved by the CEO 2026-09-15: $1.44 million one-time and $260,000 a year, plus $240,000 for SOC 2 across 2027 | P01 |
