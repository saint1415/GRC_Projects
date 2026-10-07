# Scenario facts: Cris Santos Company | Critical Manufacturing | Mid-Market

All 10 deliverables in this folder use the facts below. The company, its plants, its customers, and its suppliers are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Regulatory text was checked on 2026-10-05 against eCFR (version date 2026-09-23), the Federal Register API, the NERC standards pages on nerc.com, and the NIST CSRC publication pages.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed since 2023; board with an audit committee) |
| Business | Designs, builds, tests, and services liquid-filled transformers for the electric grid (NAICS 335311, Power, Distribution, and Specialty Transformer Manufacturing). **Distribution transformers (Plant 1):** single-phase and three-phase pad-mounted units, 25 kVA to 5 MVA, about 21,000 units a year. **Power transformers (Plant 2):** substation units from 10 MVA to 300 MVA and up to 230 kV class, about 240 units a year. **Service:** field commissioning, repair, and storm response. **Fleet Monitoring Service (FMS):** a subscription condition-monitoring service for installed power transformers, launched in 2025 |
| Location | Florida only. **Main campus:** headquarters (HQ) office building, the HQ server room, and Plant 1. **Plant 2:** a power transformer plant and repair center in another Florida city, about 150 miles away, acquired in 2024 with its own server room. Field service technicians travel to customer sites across the Southeast |
| Workforce | **850 employees:** 6 executives; 542 production (Plant 1 about 320, Plant 2 about 222, on two shifts with Saturday overtime in storm season); 46 maintenance and controls (Director of Manufacturing Engineering, a Controls Lead at each plant, 6 controls technicians, 37 mechanics and electricians); 64 engineering (including a 6-person product software team); 12 Digital Services (FMS); 28 quality; 38 supply chain and production planning; 36 field service; 30 sales and customer service; 26 general and administrative (finance, HR, contracts and trade compliance); 22 IT and security |
| Revenue | About $360 million a year (fictional): distribution transformers 58%, power transformers 36%, field service and repair 5%, FMS subscriptions 1%. The SBA size standard for NAICS 335311 is **800 employees** (13 CFR 121.201, checked on eCFR 2026-09-23), so with 850 employees the company is **not SBA-small** |
| Customers | About 120 electric utilities in the Southeast and Mid-Atlantic (investor-owned utilities, municipal utilities, and electric cooperatives), plus renewable energy, battery storage, and data center developers. Power transformer backlog is about 70 weeks; distribution backlog about 30 weeks. Utilities place emergency storm-restoration orders each hurricane season, and the company reserves production slots for them |
| Utility contract security terms | **31 utilities** (those that operate medium impact BES Cyber Systems) have added a **Supplier Cyber Security Addendum** to their purchase agreements since 2023. The addenda cover the transformer monitoring units (TMUs), the TMU configuration software the company writes, field service access to utility sites and systems, and, for FMS subscribers, the FMS. Their terms follow the six topics in NERC CIP-013-2 Requirement R1 Part 1.2. Deadlines differ by utility: **22 require incident notice within 48 hours and 9 within 24 hours** of confirming a cyber incident related to the products or services supplied; all require notice within 1 business day when a company representative's access should no longer be granted, disclosure of known vulnerabilities in supplied firmware and software within 30 days, hashes or signatures for all firmware, software, and patches, and only utility-controlled, MFA-protected, per-session remote access. **These deadlines are contract terms, not NERC requirements** |
| NERC status | **Not a NERC-registered entity.** CIP-013-2 ("Mandatory Subject to Enforcement" on nerc.com; effective 2022-10-01) applies to the Responsible Entities in its section 4.1, not to their suppliers. CIP-013-3 is "Subject to Future Enforcement" (FERC order 2026-03-19; effective 2028-07-01) |
| Federal contracts | **Three civilian federal contracts** (no DoD), about $9 million in total, awarded 2025-2026: pad-mounted transformers for two federal facilities and two power transformers for a federal water project. Built to agency specifications (not COTS). Each contract includes FAR 52.204-21, 52.204-23, 52.204-25, and 52.204-30. Federal contract information (FCI) in company systems: agency specifications and drawings, delivery schedules, test reports, and correspondence. No DFARS clauses and no CUI |
| DoD work | None. Sales bids on military installation projects through construction primes. A **bid review gate** (2025) stops any bid whose terms would flow down DFARS 252.204-7012 or require a CMMC level until leadership approves a compliance plan |
| Exports | About 6% of revenue: distribution and power transformers to utilities in the Caribbean and Central America. Products and technology are classified **EAR99** (Contracts and Trade Compliance Manager, 2025). Export orders are screened against U.S. government restricted-party lists in the ERP before release. Export records must be kept 5 years (15 CFR 762.6(a)) |
| Transformer monitoring unit (TMU) | Every power transformer ships with a TMU (dissolved gas, temperature, and load monitoring) bought from a monitoring electronics supplier. The company's product software team writes the **TMU configuration software** that utilities install on their engineering laptops, and loads supplier firmware plus a customer-specific configuration at final test. At customer sites the TMU is under utility control |
| Fleet Monitoring Service (FMS) | **14 utility subscribers, about 1,150 monitored power transformers** (about 180 of them made by other manufacturers). Each utility pushes TMU data from its own data platform to the FMS ingestion interface (utility-initiated, one-way, mutually authenticated TLS). **The FMS has no connection into utility networks or to TMUs.** Company reliability engineers review condition alerts from the AI-003 analytics model and publish advisories in a customer portal used by about 260 utility users. Subscription agreements commit to 99.5% monthly portal availability and confidentiality of utility data. The two largest subscribers require a **SOC 2 Type 2 report** (Security, Availability, Confidentiality) before their renewals on 2027-12-31 |
| Sensitive data | Transformer designs, electromagnetic design calculations, and winding specifications (trade secrets); customer specifications and substation drawings under NDA; utility asset health data in the FMS; certified test reports; TMU firmware images, configuration software source code, and the code signing key; FCI; export classification and screening records; supplier pricing and bills of materials; employee and applicant personal information (HR, payroll, applicant tracking) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel, forensics, and an OT-capable response firm. The policy requires notice through the carrier hotline before incident vendors are engaged |
| Not in scope | NERC CIP as a direct obligation (not registered). DFARS 252.204-7012 and CMMC (no DoD contracts or subcontracts; C-CRITICAL-MFG-R04). ICTS connected vehicles rule, 15 CFR Part 791 Subpart D (no vehicles or vehicle systems; C-CRITICAL-MFG-R02). SEC disclosure rules (privately held). Payment cards (customers pay by bank transfer). HIPAA (no such data; the employee health plan is fully insured). CIRCIA reporting (C-CRITICAL-MFG-R01): proposed only; see P03 for how the proposed scope would treat the company |
| Regulatory driver IDs | C-CRITICAL-MFG-R01 (CIRCIA, proposed; readiness only), C-CRITICAL-MFG-R03 (EAR recordkeeping and screening), and C-CRITICAL-MFG-R04 (DFARS; not applicable, recorded once) are the vertical IDs. The primary benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding rules outside the vertical registry are cited directly: FAR 52.204-21, 52.204-23, 52.204-25, 52.204-30, the utility addenda ("Utility addendum sec. N (CIP-013-2 R1.2.N flow-down)"), and the FMS subscription agreements |
| State law approach | The company operates only in Florida. Florida law is cited where a Florida duty applies (breach notice for employee and applicant personal information, Fla. Stat. 501.171). Employees who live in other states are handled under "the law of each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives the POA&M and top risks |
| Chief Executive Officer (CEO) | Accepts High risk; approves the risk appetite and the security budget; ransom and precautionary plant shutdown decisions on the crisis management team's recommendation |
| Chief Operating Officer (COO) | Executive sponsor of the security program; accepts Moderate risk; system owner of the ERP and Production Scheduling Platform (P02); chairs the crisis management team |
| Chief Financial Officer (CFO) | Cyber insurance; finance and payroll; ERP financial modules |
| General Counsel | Contracts, utility addenda, federal clauses, breach and notice decisions with outside counsel; chairs the obligations register review |
| vCISO (part-time contractor) | Program strategy, risk appetite drafting, board reporting, AI review group member |
| IT Director | IT operations, landing zone, ERP technical ownership, SD-WAN, endpoints; recovery lead |
| Security Manager plus 2 security analysts and 1 GRC analyst | Security operations, MSSP oversight, vulnerability management, the risk register, policies and standards; incident commander for cyber incidents |
| OT Security Engineer (hired 2025) | OT security architecture, OT inventory, OT monitoring, remote access gateway; reports to the Security Manager with a dotted line to the Director of Manufacturing Engineering |
| Director of Manufacturing Engineering | Owns plant control systems at both plants; approves OT changes; OT incident lead with the OT Security Engineer |
| Plant 1 Manager; Plant 2 Manager | Production, safe shutdown, and manual operations decisions at each plant |
| Controls Lead (one per plant) | PLCs, HMIs, CNC and winding controllers, drying oven and oil processing controls, historians |
| VP Engineering | Designs and the PLM vault; product security for the TMU configuration software and supplied firmware (vulnerability intake, signing, and disclosure to utilities) |
| Director of Digital Services | FMS business and service owner; business owner of AI-003 |
| Director of Quality | ISO 9001 quality system; integrity of test data and certified test reports |
| Director of Supply Chain; Production Planning Manager | Supplier onboarding, EDI, the TMU electronics supplier; the production schedule (business owner of AI-001) |
| Maintenance Manager (Plant 1) | Maintenance program and OEM visits; business owner of AI-002 |
| Contracts and Trade Compliance Manager | Utility addenda tracking, federal clause compliance (SAM.gov FASCSA checks, covered equipment inquiries), export classification and screening; sends contractual notices |
| Director of Field Service | Field technicians, storm response, access-revocation notices to utilities |
| HR Director | Onboarding, transfers, terminations, training records; business owner of AI-005 |
| Co-sourced internal audit firm | Annual IT audit; performed the P07 assessment with an OT specialist subcontractor |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR, the SIEM, identity, cloud, and the Plant 1 OT sensor; must call the Security Manager within 30 minutes of a high-severity alert |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | ERP with advanced planning and scheduling (APS) module | Cloud landing zone, ERP production account (IaaS/PaaS, vendor-agnostic) | Orders, bills of materials, purchasing, inventory, shipping, export screening, finance, and the finite-capacity schedule for both plants. About 300 office users |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | Email, ERP, cloud console, VPN, FMS administration. Synchronized from the corporate directory (2 domain controllers at HQ). **Plant 2 still runs its own legacy directory domain with a two-way trust to the corporate domain** |
| SYS-03 | Integration platform | Cloud, ERP production account | Work orders from the ERP to both MES instances and confirmations back; EDI with the EDI network provider |
| SYS-04 | PLM vault and CAD workstations | On premises (HQ server room) | Designs, calculations, winding specifications, customer drawings; nightly backup to the cloud backup account |
| SYS-05 | Manufacturing execution systems (MES) and kiosks | Plant 1: MES in the Plant 1 OT DMZ (since 2025) with 40 kiosks. Plant 2: legacy MES product on a server in the Plant 2 server room with 22 kiosks | Dispatch, electronic travelers, confirmations, test data collection. About 420 MES users (badge and PIN). **The Plant 2 MES server is dual-homed on the Plant 2 office and plant networks.** Plant 2 moves to the Plant 1 MES in 2027 |
| SYS-06 | Plant control systems (OT) | On premises | Plant 1: 4 core cutting lines, 36 winding machines, 2 vapor-phase drying ovens, tank welding robots, paint line, 56 HMIs and engineering workstations, zoned behind the OT DMZ. Plant 2: 2 step-lap core cutting lines, 12 vertical winding machines, 2 vapor-phase drying ovens, vacuum oil processing, overhead crane controls, 34 HMIs and engineering workstations on one flat network. **Plant 2 OEM remote access uses 4 always-on cellular routers** |
| SYS-07 | Test systems | On premises | Plant 1 automated routine test stations (8 test PCs); Plant 2 high-voltage test bay with impulse, applied voltage, and loss measurement systems (6 test PCs) |
| SYS-08 | Plant historians | On premises, one per plant | Process data. The Plant 1 historian replicates to a read-only copy in the OT DMZ, which feeds the AI-002 predictive maintenance SaaS |
| SYS-09 | IT endpoints and networks | On premises and remote | 640 laptops and desktops with EDR and full-disk encryption; SD-WAN linking HQ and Plant 1, Plant 2, and the cloud hub; next-generation firewalls at each site; file servers at HQ and Plant 2 |
| SYS-10 | EDI network provider | SaaS | Purchase orders, advance ship notices, invoices |
| SYS-11 | Productivity suite (email, files, chat) | SaaS | Customer drawings and FCI are exchanged by email and in labeled project sites |
| SYS-12 | Product software and firmware pipeline | SaaS code repository; build server and firmware library in the non-production cloud account | TMU configuration software source, build pipeline, supplier firmware images, the code signing key (stored on the build server), and the customer download portal |
| SYS-13 | Fleet Monitoring Service (FMS) | Cloud, FMS production account | Ingestion interface, time-series database, AI-003 analytics, customer portal |
| SYS-14 | SIEM and EDR | SaaS, operated by the MSSP | EDR, identity, cloud, firewall, and the Plant 1 OT sensor feed the SIEM. **MES, historian, Plant 2 OT, and FMS application logs do not** |
| SYS-15 | Physical security systems | On premises | Badge access, visitor management, 180 CCTV cameras. The 2024 acquisition review found 9 covered cameras at Plant 2; they were reported under FAR 52.204-25(d) and replaced by 2025-06 |
| SYS-16 | HR, payroll, and applicant tracking | SaaS | Employee and applicant records. The applicant tracking system includes the AI-005 match-score feature |
| SYS-17 | AI services | Cloud ML service (AI-001); vendor SaaS (AI-002, AI-004, AI-005); FMS (AI-003) | See P10 |

**SSP system (P02):** the *ERP and Production Scheduling Platform (EPSP)*: SYS-01, SYS-02, SYS-03, and SYS-05 at both plants, the landing zone accounts that host them (management and security, shared services, ERP production, and backup), about 180 planning, purchasing, quality, and finance endpoints in SYS-09, the SD-WAN and the IT/OT boundary firewalls at both plants, and the EPSP use cases in the SIEM (SYS-14); interconnections to SYS-04, SYS-06, SYS-07, SYS-08, SYS-10, SYS-13, and SYS-16 are outside the boundary.

## 4. Current security posture: a defined program with gaps in scale

**In place today:**
- MFA through the identity provider for all office users; FIDO2 security keys for the 18 cloud, identity, and domain administrators
- EDR on all 640 IT endpoints and on IT servers, with 24x7 MSSP monitoring and a SIEM
- Plant 1 OT DMZ (2025): zoned OT network, deny-by-default IT/OT firewall, a remote access gateway with MFA, per-session approval, and recording for OEMs, a passive OT monitoring sensor, and automated backups of Plant 1 controller programs
- Immutable backups of the ERP and FMS in a separate backup account and region (35-day write-once retention, separate administrator credentials); nightly PLM backups to the same account
- A cloud landing zone with 6 accounts and organization guardrails
- Annual risk assessment since 2024 (the last one was July 2025); policies adopted in 2024; annual co-sourced IT audit
- Monthly authenticated vulnerability scanning of IT systems; quarterly access reviews for the ERP
- Annual security awareness training and phishing simulations for office staff
- An obligations register (2025) listing the 31 utility addenda, the federal clauses, and EAR record duties
- TMU firmware hash verification on receipt from the supplier (2025)
- FCI kept in labeled, access-restricted project sites; SAM.gov representations reviewed by the Contracts and Trade Compliance Manager
- Restricted-party screening of export orders in the ERP
- ISO 9001 quality system with calibrated test equipment and certified test reports
- Cyber insurance with breach counsel, forensics, and an OT-capable response firm on the panel

**Gaps (found in the 2026 assessments):**
1. Plant 2 (acquired 2024) is not integrated: its OT network is flat, its MES server is dual-homed on the office and plant networks, and its legacy directory domain has a two-way trust with the corporate domain.
2. Plant 2 OEM remote access runs through 4 always-on cellular routers with shared OEM logins, no MFA, and no logging.
3. The OT asset inventory is complete for Plant 1 but about 50% for Plant 2. 23 of the 90 HMIs and engineering workstations run operating systems past vendor support (19 of them at Plant 2). OT patching is ad hoc at Plant 2.
4. Recovery is unproven: Plant 2 controller programs are copied by hand to a laptop; no OT restore has ever been tested at either plant; the ERP has had only a file-level restore test (2025), and there has been no full recovery test of the landing zone.
5. Monitoring stops at IT: MES, historians, Plant 2 OT, and FMS application logs do not reach the SIEM; OT monitoring covers Plant 1 only.
6. Access control is uneven: Plant 2 MES uses shared supervisor accounts and HMIs use shared operator logins; quarterly access reviews cover the ERP only; privileged access management covers cloud and domain administrators but not OT engineering workstations.
7. Third-party and customer obligations: about 190 suppliers have system access or company data, and they are reviewed only at onboarding. The obligations register exists, but in 2026 two access-revocation notices to utilities were late and one vulnerability disclosure (TMU configuration software) went out on day 41 against a 30-day term.
8. Product security: the TMU configuration software is built without a documented secure development process, no software bill of materials (SBOM) is delivered to utilities, and the code signing key sits on the build server rather than in a hardware-backed key store.
9. The FMS has no tested disaster recovery behind its 99.5% availability commitment, its application logs are not monitored, and analytics model updates have no formal change control. Two subscribers require a SOC 2 Type 2 report by the end of 2027.
10. Incident response: the 2024 IT incident response plan was tested once (2025 IT tabletop). There is no tested OT playbook, no product security incident process, and no defined crisis management team.
11. AI tools were adopted without review: the AI-002 pilot, the AI-005 applicant match score (turned on by HR in 2026-05), and personal use of public generative AI tools. There is no AI standard beyond acceptable use.
12. Supporting standards (configuration, logging, OT security, secure development, vendor risk) are thin or missing.
13. Production workers and field technicians receive only orientation-level security training, and field technicians are not trained on utility access rules.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | ERP and Production Scheduling Platform (EPSP), the registry's "ERP and production scheduling system", with the MES at both plants inside the boundary because work order release depends on it |
| P03 regulation | Primary: NIST CSF 2.0 with NIST SP 800-82 Rev. 3 as the OT guide (voluntary benchmark), assessed as a **full profile of all 106 CSF 2.0 subcategories** with evidence sampling. Secondary (binding by contract): FAR 52.204-21 for the three federal contracts, FAR 52.204-23, -25, and -30, and the 31 utility Supplier Cyber Security Addenda. Applicability rows for the vertical requirements, CIP-013-2, EAR recordkeeping, and Florida breach notice |
| P04 cloud | A 6-account landing zone (management and security, shared services, ERP production, FMS production, non-production, backup) plus SaaS. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | All business units: Plant 1, Plant 2, engineering, supply chain, field service, Digital Services (FMS), and corporate functions; 18 processes with dollar impact |
| P07 assessment | 33 controls on the EPSP and its IT/OT boundaries, with sampling, by the co-sourced internal audit firm and an OT specialist subcontractor |
| P08 incidents | **Two incident types:** (1) ransomware disrupting production of grid equipment (registry default), and (2) a compromise of products or services supplied to utilities (TMU configuration software or the FMS). Both runbooks are integrated with the crisis management team and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the FMS (Security, Availability, Confidentiality) requested by two subscribers, plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 demand forecasting and AI-002 predictive maintenance (the registry default, kept), AI-003 FMS transformer condition analytics, AI-004 enterprise generative AI assistant, AI-005 applicant match score in the applicant tracking system |
| Cloud | Vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork (Plant 1 walkthrough 2026-07-14; Plant 2 walkthrough 2026-07-15 and 2026-07-16) |
| 2026-08-03 to 2026-08-21 | Control assessment fieldwork by the co-sourced internal audit firm (OT tests in the Saturday maintenance windows: Plant 1 on 2026-08-08, Plant 2 on 2026-08-15) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness assessment, vendor SOC 2 reviews, and AI risk assessment |
| 2026-09-15 | Results to the audit committee; deliverables approved by the COO (Moderate and below) and the CEO (High and Very High, risk appetite, budget) |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue per production day | About 250 production days a year: Plant 1 about $836,000 of shipments per day, Plant 2 about $520,000, field service and repair about $68,000, FMS about $16,000 (subscription revenue accrues daily) |
| Workforce activity | 214 terminations (168 production), 71 internal transfers, and 236 new hires in the 12 months to 2026-06-30. The June 2026 phishing simulation click rate was 6.9% |
| Suppliers | About 190 suppliers have system access or company data; 22 are Tier 1 under the P09 tiering approach |
| Utility addenda history | 2026 events in the obligations register: 2 late access-revocation notices (field technicians who left in 2026-02 and 2026-05, notified on business days 4 and 6), and 1 vulnerability disclosure for the TMU configuration software sent 41 days after the company learned of the flaw |
| FCI review | The Contracts and Trade Compliance Manager last searched SAM.gov for FASCSA orders on 2026-03-02; FAR 52.204-30(c)(1) asks for a review at least once every three months |
| Plant 2 integration | The two-way domain trust and the dual-homed MES date from the acquisition. The Plant 2 OT DMZ and the move to the Plant 1 MES are budgeted for 2027 |
| Backups | ERP database: continuous point-in-time recovery for 7 days in the ERP account, plus daily copies to the backup account with 35-day write-once retention. FMS: daily copies to the backup account. Plant 1 controller programs: nightly automated OT backups to a server in the Plant 1 OT DMZ, copied weekly to offline media |
| FMS subscription terms | Notice to each affected subscriber within 72 hours of confirming a security incident affecting its data or the service; status page update within 1 hour of an outage; service credits when monthly availability falls below 99.5% |
| Privileged accounts | 41 privileged accounts across cloud, identity, directory, ERP, and network planes: 18 use FIDO2 keys, 23 use push MFA with number matching. 6 MES administrator accounts and the local administrator accounts on 24 OT engineering workstations have no MFA |
| P07 finding | On 2026-08-12 the assessors found the Plant 2 MES service account in the corporate Domain Admins group through the two-way trust, password last set in 2019. Rights removed and password rotated 2026-08-19; trust to become one-way by 2026-10-31 |
| Plant 2 details | 4 always-on OEM cellular routers (drying oven, vacuum oil processing, a winding line, a core cutting line); 2 unmanaged wireless access points on the plant network; 41 federal drawings found on the Plant 2 file server (2026-07-16); the Plant 2 server room uses a shared key held by 9 people |
| FCI subcontractors | 3 subcontractors received federal drawings in 2026; the outside tank fabricator's purchase order lacked the FAR 52.204-21 flow-down. SAM.gov FASCSA check repeated 2026-08-24 (no applicable order) |
| Incident response support | The insurer's panel OT-capable response firm was confirmed on 2026-08-20. The 2025 IT tabletop produced 6 actions (4 closed) |
| AI use cases | AI-001 in production since 2025-01; AI-002 pilot since 2026-04 on 2 drying ovens and 8 winding machines at Plant 1; AI-003 in production since 2025-06 with the FMS; AI-004 enterprise generative AI assistant pilot since 2026-03 (120 users); AI-005 turned on by HR in 2026-05 and switched off 2026-09-15 |
| Product security | The TMU supply agreement has no deadline for supplier vulnerability or compromise notices. A public security contact for product vulnerability reports goes live 2026-11-15 |
| Terminology | "ERP and Production Scheduling Platform (EPSP)" is the SSP system in P02, identifier CSC-EPSP-01 |
| Additional role titles | VP Sales; Controller; IT infrastructure manager; ERP applications manager; Director of Marketing and Communications |
