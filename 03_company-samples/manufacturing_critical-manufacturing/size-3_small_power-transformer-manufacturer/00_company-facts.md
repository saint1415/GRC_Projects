# Scenario facts: Cris Santos Company | Critical Manufacturing | Small

All 11 deliverables in this folder use the facts below. The company, its plant, and its customers are fictitious. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Regulatory text was checked on 2026-09-26 against eCFR (version date 2026-09-23), the Federal Register API, the NERC standards pages on nerc.com, the CIP-013-2 PDF published by NERC, and the NIST CSRC publication pages.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held power and distribution transformer manufacturer; Cris Santos is majority owner) |
| Business | Designs, builds, and tests liquid-filled transformers for the electric grid (NAICS 335311, Power, Distribution, and Specialty Transformer Manufacturing). **Distribution transformers:** three-phase pad-mounted units, 75 kVA to 5 MVA (about 5,500 units a year). **Power transformers:** substation units up to 50 MVA and 138 kV class (about 60 units a year). Field service: commissioning, repairs, and storm response |
| Location | Florida. One campus: the headquarters office building, the plant (Bay A distribution line, Bay B power transformer line, tank fabrication shop, vapor-phase drying and oil processing area, high-voltage test bay), and the plant server room. The HQ server room is in the office building |
| Workforce | **200 employees:** 3 executives; 122 production (core cutting, coil winding, tank fabrication and welding, core-coil assembly, oil processing, test); 14 maintenance (Maintenance Manager, Controls Engineer, 2 controls technicians, 10 mechanics and electricians); 15 engineering; 8 quality; 9 supply chain and production planning; 8 field service; 8 sales and customer service; 10 general and administrative (Controller and 4 finance staff, HR Manager and 2 HR staff, Contracts and Compliance Manager and 1 analyst); 3 IT. Two production shifts, five days a week, with Saturday overtime during storm season |
| Revenue | $84 million a year (fictional): distribution transformers 70%, power transformers 25%, field service and parts 5%. The SBA size standard for NAICS 335311 is 800 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | 38 electric utilities in the Southeast (investor-owned utilities, municipal utilities, and electric cooperatives), plus solar and battery storage developers. Backlog is about 38 weeks. Utilities place emergency storm-restoration orders each hurricane season, and the company reserves production slots for them |
| Utility contract security terms | 12 of the 38 utility customers (the ones that operate medium impact BES substations) have added a **Supplier Cyber Security Addendum** to their purchase agreements since 2023. The addenda cover the monitoring electronics and software the company ships with power transformers. Their terms follow the six topics in NERC CIP-013-2 Requirement R1 Part 1.2 (see P03): notify the utility within 48 hours of confirming a cyber incident related to the products or services supplied; coordinate the response; notify the utility within 1 business day when a company field representative's remote or onsite access should no longer be granted; disclose known vulnerabilities in supplied firmware and software within 30 days; provide hashes or signatures for all firmware, software, and patches; and use only utility-controlled, MFA-protected, per-session remote access. These deadlines are contract terms, not NERC requirements (EV-031) |
| NERC status | **Not a NERC-registered entity**, recorded in the intake obligations register (NERC-CIP-013) and confirmed by a registration check on 2026-07-15 (EV-058). CIP-013-2 (in effect since 2022-10-01) applies to Responsible Entities listed in its section 4.1 (for example Transmission Owners and Generator Owners), not to their suppliers. The company is bound only by the contract addenda above |
| Federal contract | **One civilian federal contract** (awarded 2025-11): 14 pad-mounted distribution transformers and 2 spares for a federal facility in Florida, built to the agency's specifications (not COTS), deliveries through 2027-03. The contract includes FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems), 52.204-23, and 52.204-25. Federal contract information (FCI) in company systems: the agency's specifications and drawings, delivery schedules, and test reports. The contract has no DFARS clauses and no CUI (EV-032). The company holds no DoD contracts or subcontracts |
| Exports | About 4% of revenue: distribution transformers shipped to two Caribbean utilities. The Contracts and Compliance Manager classified the products and their technology as EAR99 in 2024. Export orders are screened against U.S. government restricted-party lists in the ERP before release. Export records must be kept 5 years (15 CFR 762.6) (EV-049) |
| Transformer monitoring unit (TMU) | Every power transformer ships with an intelligent electronic device (dissolved gas, temperature, and load monitoring) bought from a monitoring electronics supplier. The company loads the supplier's firmware and a customer-specific configuration at final test and gives utilities a configuration software tool. At customer sites the TMU is under utility control. Field service technicians commission TMUs on site and sometimes support them through the utility's remote access system |
| Sensitive data | Transformer designs, electromagnetic design calculations, and winding specifications (trade secrets); customer specifications and substation drawings shared under NDA; certified test reports; TMU firmware images and configuration files; FCI; export classification and screening records; supplier pricing and bills of materials; employee personal information (HR and payroll) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): NERC CIP as a direct obligation (not registered). DFARS 252.204-7012 and CMMC (no DoD contracts; C-CRITICAL-MFG-R04). ICTS connected vehicles rule, 15 CFR Part 791 Subpart D (the company makes no vehicles or vehicle systems; C-CRITICAL-MFG-R02). SEC disclosure rules (privately held). Payment cards (customers pay by bank transfer or check). HIPAA (no such data). CIRCIA reporting (C-CRITICAL-MFG-R01): proposed only; see P03 for how the proposed scope would treat the company |
| Regulatory driver IDs | C-CRITICAL-MFG-R01 (CIRCIA, proposed; readiness only), C-CRITICAL-MFG-R03 (EAR recordkeeping and screening), and C-CRITICAL-MFG-R04 (DFARS; not applicable, recorded once) are the vertical IDs. The primary benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding rules outside the vertical registry are cited directly: FAR 52.204-21, FAR 52.204-25, FAR 52.204-23, and the utility contract addenda ("Utility addendum (CIP-013-2 R1.2.x flow-down)") |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President and majority owner (Cris Santos) | Accepts High and Very High risks; approves the security budget; ransom and precautionary plant shutdown decisions with the VP Operations |
| VP Operations | Executive owner of the security program; accepts Moderate risks; signs policies; system owner of the ERP and Production Scheduling Platform (P02) |
| VP Engineering | Owns designs and the PLM vault; product security for the TMU integration (vulnerability intake and disclosure to utilities) |
| Controller | Finance, billing, payroll; cyber insurance policy; ERP financial modules |
| IT Manager | Security program lead with part-time security and compliance duties; runs the identity provider, cloud tenant, IT network, and endpoints; manages the MSP; maintains the risk register; incident commander for IT incidents |
| Controls Engineer | OT lead in the maintenance department: PLCs, HMIs, CNC and winding machine controllers, drying oven controls, historian, OT network, and OEM remote access; incident lead for OT |
| Plant Manager | Production lines and shifts; safe shutdown and manual operations decisions; approves any change on the plant floor |
| Production Planning Manager | Owns the production schedule, work order release, and sales and operations planning; business owner of AI-001 (P10) |
| Maintenance Manager | Maintenance program and OEM service visits; business owner of AI-002 (P10) |
| Quality Manager | ISO 9001 quality system; integrity of test data and certified test reports |
| Contracts and Compliance Manager | Customer contracts and utility security addenda; the federal contract clauses; export compliance; sends contractual and regulatory notices |
| Field Service Manager | TMU commissioning, field technicians, storm response; access-revocation notices to utilities |
| Supply Chain Manager | Supplier onboarding, EDI, the TMU electronics supplier |
| HR Manager | Onboarding, transfers, terminations, training records |
| Managed service provider (MSP) | IT help desk after hours, server patching, firewall management, and backup monitoring. Holds a remote monitoring and management (RMM) tool with administrator rights on IT servers and endpoints. Has a SOC 2 Type 2 report (Security) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | ERP with advanced planning and scheduling (APS) module | Public cloud tenant (IaaS/PaaS), vendor-agnostic | Orders, bills of materials, purchasing, inventory, shipping, finance, and the finite-capacity production schedule. Commercial ERP software installed on virtual machines with a managed database |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | Protects email, ERP, cloud console, and the IT VPN. Synchronized from on-premises directory servers. **MES kiosks and OT systems are not integrated** (EV-002) |
| SYS-03 | Integration service | Cloud tenant (virtual machine) | Moves work orders from the ERP to the MES and production confirmations back; exchanges EDI messages with the EDI network provider |
| SYS-04 | PLM vault and CAD/design workstations | On premises (HQ server room) | Designs, electromagnetic calculations, winding specifications, and customer drawings |
| SYS-05 | Manufacturing execution system (MES) and 25 shop-floor kiosks | On premises (plant server room and plant floor) | Work order dispatch, electronic travelers, labor and material confirmations, test data collection. **The MES server has network interfaces in both the office network and the plant network** (EV-016) |
| SYS-06 | Plant control systems (OT) | On premises (plant floor) | 2 CNC core cutting lines, 14 coil winding machines, the vapor-phase drying oven and 2 conventional ovens, the vacuum oil fill station, a CNC plasma cutter, 2 robotic welding cells, and 18 HMI and engineering workstations. Three OEM cellular remote access routers (drying oven, core cutting line 1, welding cell 2) (EV-034, EV-065) |
| SYS-07 | High-voltage test bay | On premises | Impulse, applied voltage, and loss measurement systems controlled by 4 test PCs; test data flows to the MES and into certified test reports |
| SYS-08 | Plant historian | On premises (plant server room) | Process data from ovens, winders, and test bay. Since 2026-04, a vendor connector sends selected tags to the AI-002 predictive maintenance SaaS (EV-039) |
| SYS-09 | IT endpoints and network | On premises and remote | 140 laptops and desktops (office and engineering) with EDR and full-disk encryption on laptops (EV-008, EV-009); firewalls; site-to-site VPN to the cloud tenant; directory servers; file server; backup appliance |
| SYS-10 | EDI network provider | SaaS | Purchase orders, advance ship notices, and invoices with utilities and major suppliers |
| SYS-11 | Productivity suite (email, files, chat) | SaaS | Customer drawings and FCI are often exchanged by email (EV-044) |
| SYS-12 | TMU firmware and configuration library | On premises (engineering file share) | Supplier firmware images, customer configuration files, and the configuration software tool given to utilities (EV-069) |
| SYS-13 | Physical security systems | On premises | Badge access, visitor management, and 46 CCTV cameras. **Four legacy yard cameras were made by a manufacturer named in the FAR 52.204-25 definition of covered telecommunications equipment (found 2026-07-20; EV-073)** |
| SYS-14 | AI services | Cloud tenant ML service (AI-001); vendor SaaS (AI-002) | AI-001 demand forecasting; AI-002 predictive maintenance pilot (see P10; EV-018, EV-039) |

**SSP system (P02):** the *ERP and Production Scheduling Platform (EPSP)*: SYS-01, SYS-02, SYS-03, SYS-05, the planning and purchasing endpoints in SYS-09, the site-to-site VPN and IT/OT firewall that connect them, and the ERP backups; interconnections to SYS-04, SYS-06, SYS-07, SYS-08, and SYS-10 are outside the boundary.

**Additional system facts (added 2026-09-26 while completing P02 and P04 to P10):**
- About 118 office users work in the ERP (EV-006); about 160 production workers, supervisors, and test technicians use MES accounts (badge number and PIN) on the 25 kiosks. Each shift also has a shared MES supervisor override account (EV-007).
- About 45 planning, purchasing, sales, quality, and finance endpoints are inside the EPSP boundary. The identity provider is fed by 2 directory servers in the HQ server room (EV-001).
- The MES server and the 25 kiosks have no malicious code protection (EV-009, EV-016); the MES database is backed up only to a local disk on the MES server (EV-016). ERP VMs are snapshotted weekly (EV-019).
- The ERP software vendor connects only through a VPN account enabled per support ticket (EV-015). AI-001 reads a nightly ERP extract under its own service identity (EV-018).
- After the P07 finding (EV-IA-5), the Controls Engineer blocked the drying oven HMI web port at the IT/OT firewall on 2026-08-17 (EV-078); the password change needs an OEM visit before 2026-09-30.
- The MSP's SOC 2 Type 2 report (Security only) covers 12 months ending 2026-03-31, with one remediated exception; the RMM software vendor is a carved-out subservice organization (EV-041). One addendum utility asked in 2026 whether the company has a SOC 2 report (EV-053).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the CSF 2.0 benchmark, FAR 52.204-21 and the utility addenda** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07), including the OT tests on 2026-08-15. Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | ERP and Production Scheduling Platform (EPSP) |
| P03 regulation | Primary: NIST CSF 2.0 with NIST SP 800-82 Rev. 3 as the OT guide (voluntary benchmark; no binding sector cyber rule). Secondary (binding by contract): FAR 52.204-21 for the federal contract and the utility Supplier Cyber Security Addenda that flow down CIP-013-2 R1.2 topics. Applicability rows for the vertical requirements (CIRCIA proposed, connected vehicles, EAR, DFARS) and FAR 52.204-25 |
| P04 cloud | The cloud tenant hosting the ERP, APS, and integration service, plus the SaaS services around it. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | 10 business processes (BP-01 to BP-10) |
| P07 assessment | 22 controls on the EPSP and its IT/OT boundary and remote access paths; fieldwork 2026-08-10 to 2026-08-15 (OT tests during the Saturday maintenance window on 2026-08-15) |
| P08 incident | Ransomware that encrypts the ERP, file and PLM servers, and the dual-homed MES server and HMIs, stopping production of grid equipment during hurricane season |
| P09 SOC 2 | The company sells products, not services to other businesses, so it is not a SOC 2 service organization. (a) Security-only (CC1-CC9) self-benchmark used to answer utility customer security questionnaires; (b) review of the MSP's SOC 2 Type 2 report |
| P10 AI | AI-001 demand forecasting (in production since 2025-11) and AI-002 predictive maintenance pilot (since 2026-04); AI-003 public generative AI tools (prohibited for Restricted data) |
| Cloud | Vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork (plant walkthrough 2026-07-16; covered telecommunications inquiry 2026-07-20) |
| 2026-07-21 | FAR 52.204-25(d) report to the contracting officer on the four covered cameras |
| 2026-07-27 to 2026-08-07 | Policies drafted from the gaps; SSP draft 0.1 (2026-08-07) |
| 2026-08-10 to 2026-08-15 | Control assessment fieldwork (OT tests 2026-08-15): operating tests of controls already in place; design review of the draft policies and runbook |
| 2026-08-21 | Security self-benchmark and MSP SOC 2 report review completed |
| 2026-08-26 | AI risk assessment completed |
| 2026-09-04 | Deliverables and policies approved by the VP Operations (Moderate and below) and the President (High) |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
