# Scenario facts: Cris Santos Company | Critical Manufacturing | Micro

All 10 deliverables in this folder use the facts below. The company, its customers, and its vendors are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Regulatory text was checked on 2026-10-05 against eCFR (version date 2026-09-23) for FAR 4.1903, 4.2004, 4.2105, 52.204-21, 52.204-23, and 52.204-25 and for 13 CFR 121.201; the CIRCIA proposed rule text (89 FR 23644); the Federal Register API (no CIRCIA final rule published as of 2026-10-05); the CIP-013-2 and CIP-013-3 pages on nerc.com; and the Florida Statutes site for section 501.171.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held transformer repair and remanufacturing shop; single-member LLC owned by Cris Santos) |
| Business | Repairs, rewinds, and remanufactures liquid-filled distribution transformers: single-phase pole-mounted units (10 to 167 kVA) and three-phase pad-mounted units (75 to 2,500 kVA). Sells remanufactured units from stock, rewinds and retests customers' failed units, and provides field service (oil sampling, oil processing, bushing and gasket replacement, and testing) on customer transformers, including substation power transformers up to 10 MVA. About 420 units a year (about 35 a month). Receipts: remanufactured unit sales 45%, customer repairs and rewinds 35%, field service and oil testing 20%. The company classifies itself in NAICS 335311 (Power, Distribution, and Specialty Transformer Manufacturing) because most receipts come from transformers it rebuilds and rewinds |
| Location | Florida. One leased industrial building: a front office, the repair bay (teardown, core and coil work, one coil winding machine, tanking), a vacuum drying oven with an oil processing rig, a test bay, and a fenced yard for cores and units awaiting repair |
| Workforce | **7 employees:** the Owner (President, who also estimates and sells), the Shop Manager, a Lead Winder, 2 Repair Technicians, a Field Service and Test Technician, and an Office Manager. One shift, five days a week, with Saturday overtime during hurricane season (June 1 to November 30) |
| Revenue | About $1.1 million a year (fictional), about $4,200 per working day. The SBA size standard for NAICS 335311 is 800 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | About 25 active customers: 6 municipal utilities and electric cooperatives in Florida (about 55% of receipts), industrial plants and property managers, 2 solar farm operators, and electrical contractors. After a hurricane, utilities buy remanufactured units from stock to restore service, so the shop keeps about 30 units in storm stock from June to November |
| Customer security terms | One customer, a generation and transmission (G&T) electric cooperative that is NERC-registered, added a **Vendor Cyber Security Exhibit** to its master service agreement in 2025 for all vendors that work in its substations. The exhibit covers the three CIP-013-2 Requirement R1 Part 1.2 topics that fit a service vendor with onsite access: notify the cooperative within **72 hours** of confirming a cyber incident related to the services supplied (Part 1.2.1); coordinate the response with the cooperative (Part 1.2.2); and notify the cooperative within **1 business day** when a company technician's onsite access should no longer be granted (Part 1.2.3). The shop supplies no software, firmware, or remote access, so Parts 1.2.4 to 1.2.6 are not in the exhibit. The Shop Manager and the Field Service and Test Technician each hold a cooperative-issued substation access badge. These deadlines are contract terms, not NERC requirements. The cooperative is about 20% of receipts |
| NERC status | **Not a NERC-registered entity.** CIP-013-2 ("Mandatory Subject to Enforcement" since 2022-10-01) applies to the Responsible Entities in its section 4.1, such as the cooperative, not to their vendors. CIP-013-3 is "Subject to Future Enforcement" with an effective date of 2028-07-01 (FERC order 2026-03-19). The shop is bound only by the exhibit |
| Federal purchase order | **One civilian federal purchase order** (awarded 2026-03-10): rewind and retest two 750 kVA pad-mounted transformers from a federal facility in Florida and supply one remanufactured spare, built to the agency's specifications (not COTS), delivery by 2026-12-15. The order incorporates FAR 52.204-21, 52.204-23, and 52.204-25. Federal contract information (FCI) in company systems: the agency's site drawings and unit history records, the delivery schedule, and the shop's test reports for the units. No DFARS clauses, no CUI, and no DoD contracts or subcontracts. The agency arranges its own freight pickup, and the shop has placed no subcontracts under the order |
| Exports | None. The shop sells only to customers in Florida and neighboring states and has never exported |
| Sensitive data | The rewind data sheet library (about 1,800 sheets of winding calculations and coil dimensions recovered from failed units; a trade secret); customer test reports and failure analyses; customer site and substation details, including the cooperative's substation access information; FCI; quotes and pricing; supplier bank details; employee personal information (HR and payroll files for 7 current and about 15 former employees) |
| Not in scope | NERC CIP as a direct obligation (not registered). DFARS 252.204-7012 and CMMC (no DoD work; C-CRITICAL-MFG-R04). ICTS connected vehicles rule (no vehicles or vehicle systems; C-CRITICAL-MFG-R02). EAR export controls (no exports; C-CRITICAL-MFG-R03). SEC disclosure rules (privately held). Payment cards (customers pay by bank transfer or check). HIPAA (no such data). CIRCIA reporting (C-CRITICAL-MFG-R01): proposed only; see P03 for how the proposed scope would treat the shop |
| Regulatory driver IDs | C-CRITICAL-MFG-R01 (CIRCIA, proposed; readiness only) is the one vertical ID with work attached; R02, R03, and R04 are recorded once as not applicable in P03. The primary benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding rules outside the vertical registry are cited directly: FAR 52.204-21, FAR 52.204-25, FAR 52.204-23, Fla. Stat. 501.171, and the cooperative exhibit ("Co-op exhibit sec. N (CIP-013-2 R1.2.x flow-down)") |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: reasonable security measures and breach notice for employee personal information (Fla. Stat. 501.171) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner (President) | Accepts Moderate and higher risks; approves policies and spending; signs customer and federal contracts; system owner of the ERP and Job Scheduling Platform (P02); ransom and shutdown decisions; calls the cyber insurer; business owner of AI-001 (P10) |
| Office Manager | **Security Coordinator** (part-time, designated in writing on 2026-07-01); bookkeeping, purchasing, payroll, and HR; ERP and productivity suite administrator; manages the MSP; keeps the risk register, the obligations list, and the incident log; sends contract and breach notices with counsel |
| Shop Manager | Runs the shop floor and the job schedule in the ERP; owns the shop equipment (drying oven and oil rig, winding machine, test bay); signs test reports; holds a cooperative substation badge |
| Field Service and Test Technician | Runs the test bay and test PC; field service and oil sampling; operates the AI-001 health-scoring portal; holds a cooperative substation badge |
| Lead Winder | Winding machine programs and the rewind data sheet library |
| Repair Technicians (2) | Teardown, core and coil work, tanking; use the shop-floor PC and tablets |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, productivity suite administration on request, and the suite backup. Holds a remote monitoring and management (RMM) tool with administrator rights on the 6 managed computers. No SOC 2 report; answered a security questionnaire in 2025 |
| Drying oven OEM | Remote troubleshooting of the oven controls through an OEM cellular modem |
| Test set vendor | Test software support and annual calibration of the test set |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Cloud ERP for job shops | Vendor SaaS | Quotes, repair work orders, the job scheduling board, inventory (cores, copper, oil, bushings), purchasing, invoicing, accounting, and a customer portal for job status. 6 named users; the Owner and Office Manager are administrators. **MFA is available but not enforced.** Vendor SOC 2 Type 2 report (Security and Availability) |
| SYS-02 | Productivity suite (email, shared drive, chat) | SaaS | MFA for every user since 2025. The shared drive holds the rewind data sheet library, test reports, customer drawings, FCI, and HR files, and is synced to the office desktops |
| SYS-03 | Endpoints | MSP-managed | 3 office desktops (Owner, Office Manager, Shop Manager), 2 laptops (Owner; Field Service and Test Technician), 1 shop-floor PC (job board and traveler printing, signed in with a shared "shop" login), and 2 shop tablets (photos of failed units, job updates). Antivirus and patching by the MSP; laptops encrypted, desktops not |
| SYS-04 | Office and shop network | On premises | One business internet line, a small-business firewall and router, and **one Wi-Fi network for the office and the shop**. The test PC, oven HMI, and camera recorder sit on the same network as office computers and staff phones. The Wi-Fi password is posted in the break area and given to customer truck drivers |
| SYS-05 | Test bay | On premises | Transformer test set (turns ratio, winding resistance, insulation resistance, and power factor) and an applied and induced voltage test station, run from a **test PC** with an operating system past vendor support, a shared local administrator login, and the test set vendor's software. Not managed by the MSP at the test set vendor's request. Its local test database (about 6 years of results) is **not backed up**; finished test reports are copied by hand to the shared drive |
| SYS-06 | Vacuum drying oven and oil processing rig | On premises | PLC with an HMI touch panel. Drying recipes (temperature and vacuum profiles) are stored only in the PLC. The HMI has a status web page on the shop network. An **OEM cellular modem is always on** for remote support; the shop does not hold its credentials and gets no record of sessions |
| SYS-07 | Coil winding machine | On premises | CNC controller, not networked. Programs are loaded from a USB stick; copies are on the Lead Winder's USB stick and some in the shared drive |
| SYS-08 | Backups | SaaS | SaaS-to-SaaS backup of the productivity suite, operated by the MSP (daily, 1-year retention). The ERP vendor backs up its own platform; the shop has never exported its ERP data |
| SYS-09 | Security cameras | On premises | 4-camera kit with a network video recorder on the shop network and a phone app on the Owner's phone. A white-label kit bought online in 2022; its manufacturer could not be identified in the FAR 52.204-25 reasonable inquiry (2026-07-14) |
| SYS-10 | AI health-scoring portal (AI-001) | Vendor SaaS | The oil laboratory's analytics portal that scores transformer condition from dissolved gas analysis (DGA) results. Pilot since 2026-04 (see P10) |

**SSP system (P02):** the *ERP and Job Scheduling Platform (EJSP)*: SYS-01, SYS-02, SYS-03, SYS-04, the test PC in SYS-05, and SYS-08; the oven controls (SYS-06), the winding machine (SYS-07), the cameras (SYS-09), and the AI portal (SYS-10) are outside the boundary.

## 4. Current security posture: early to partial

**In place today:**
- MFA on the productivity suite for every user
- MSP patching and antivirus on the 6 managed computers; MSP-managed firewall
- Laptop encryption
- Daily SaaS-to-SaaS backup of the productivity suite with 1-year retention
- ERP vendor SOC 2 Type 2 report (Security and Availability)
- Locked office, monitored building alarm, and a fenced yard with a locked gate
- A small-business cyber insurance policy (bought 2025) with a breach hotline
- Annual test set calibration; test reports signed by the Shop Manager
- Office Manager phones suppliers back before changing bank details (informal habit; it stopped a fraudulent request in 2026-03)

**Missing:**
1. No documented risk assessment, policies, or security owner before 2026-07. The Office Manager was designated Security Coordinator on 2026-07-01.
2. ERP MFA is not enforced, and both ERP administrators use their administrator accounts for daily work.
3. The network is flat: office computers, the shop-floor PC, the test PC, the oven HMI, the camera recorder, and visitors' phones share one Wi-Fi network.
4. The test PC runs an unsupported operating system with a shared administrator login, is not managed by the MSP, and its test database is not backed up.
5. The oven OEM's cellular modem is always on; the shop does not control or see remote sessions.
6. The shop holds no copy of its ERP data, oven recipes exist only in the PLC, winding programs exist only on USB sticks, and no restore has ever been tested.
7. No incident response plan. Only the Owner knows the insurer's hotline number.
8. Shared "shop" login on the shop-floor PC and tablets; no access reviews. A Field Service Technician who left on 2026-05-08 still had suite and ERP access when found on 2026-07-15, and the cooperative was not told his access should end until 2026-07-16.
9. No security awareness training or phishing exercises.
10. The cooperative exhibit and the FAR clauses are not tracked, and FCI is not identified; it sits in email and the shared drive.
11. No inventory of devices or of where sensitive data lives.
12. AI-001 started in 2026-04 without review. Cooperative transformer and substation data is uploaded under the vendor's standard terms, which allow the vendor to use customer data to improve its models.
13. Desktops are unencrypted; an office PC retired in 2025 has no disposal record.
14. The MSP contract has no security terms: no incident notice, no MFA requirement for the MSP's own access, and no recovery time.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | ERP and Job Scheduling Platform (EJSP). This is the registry's "ERP and production scheduling system" at micro scale: a SaaS job-shop ERP with a scheduling board, plus the test PC that produces the test reports every shipment needs |
| P03 regulation | Primary: NIST CSF 2.0 with NIST SP 800-82 Rev. 3 as the OT guide (voluntary benchmark; no binding sector cyber rule), 37 subcategories. Secondary (binding by contract): FAR 52.204-21 for the federal purchase order and the cooperative exhibit that flows down CIP-013-2 R1 Parts 1.2.1 to 1.2.3. Also FAR 52.204-25 and 52.204-23, Fla. Stat. 501.171(2), and applicability rows for CIP-013-2 and the four vertical requirements |
| P04 cloud | SaaS-first: the ERP, the productivity suite, and the AI portal, plus one cloud workload, the SaaS-to-SaaS backup operated by the MSP. Vendor-agnostic |
| P05 BIA | 8 business processes (BP-01 to BP-08), rated for hurricane season |
| P07 assessment | 13 controls on the EJSP, its network, and the OEM remote access path; independent consultant; MSP evidence requested |
| P08 incident | Ransomware disrupting production of grid equipment: a phishing email leads to ransomware that encrypts the office computers and synced shared drive and reaches the test PC and oven HMI over the flat network, stopping shipments of storm-stock transformers in hurricane season. The MSP and the insurer are in the notification chain |
| P09 SOC 2 | The shop sells products and repair services, not a hosted service, so it is not a SOC 2 service organization. (a) Security plus Availability self-assessment used to answer the cooperative's vendor security questionnaire; (b) review of the ERP vendor's SOC 2 Type 2 report |
| P10 AI | **Adapted from the registry default** ("Demand forecasting and predictive maintenance"). A 7-person shop builds no models. It uses one vendor AI service that covers both halves: AI-001, the oil laboratory's health-scoring portal, scores customers' transformers from DGA results (predictive maintenance) and the shop uses the scores to recommend repair or replacement and to forecast storm-season rebuild demand. AI-002 (the ERP vendor's AI stock forecast add-on, offered but not enabled) and AI-003 (public generative AI chatbots) are in the inventory |
| Cloud | Vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis with the MSP (shop walkthrough and FAR 52.204-25 reasonable inquiry 2026-07-14) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11) |
| 2026-08-20 | SOC 2 readiness self-assessment and ERP vendor SOC 2 report review |
| 2026-08-25 | AI risk assessment |
| 2026-08-31 | Deliverables approved by the Owner |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Former technician | The Field Service Technician who left on 2026-05-08 returned his cooperative badge on his last day, but nobody told the cooperative. His suite and ERP accounts were found active on 2026-07-15 and disabled that day; sign-in logs showed no use after his last day. The Office Manager notified the cooperative on 2026-07-16, more than two months after the 1-business-day deadline | P01, P03, P07 |
| Camera recorder | The Owner disconnected the camera recorder from the network on 2026-07-17 and ordered a replacement kit whose manufacturer is documented, to be installed by 2026-10-31. Nothing was reported to the contracting officer because no covered equipment was identified; if the old kit is later identified as covered, a report is due within 1 business day (52.204-25(d)) | P01, P03, P08 |
| Firewall rule found in testing | P07 testing on 2026-08-11 found a firewall port-forwarding rule, left from a 2024 test set vendor support session, that exposed remote desktop on the test PC to the internet. The MSP removed it the same day. The firewall keeps only 7 days of logs, so earlier use cannot be ruled out; an offline malware scan of the test PC on 2026-08-12 found nothing | P01, P04, P07 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, suite administration on request, and the suite backup, with a 4-business-hour response time. No incident notice term, no recovery time, and the MSP's technicians share one firewall administrator login without MFA | P01, P04, P05, P07 |
| ERP vendor | The ERP vendor's SOC 2 Type 2 report covers 12 months ending 2026-03-31 with no exceptions; its stated recovery objectives are RTO 8 hours and RPO 1 hour. It offers a scheduled full data export that the shop has not set up | P02, P05, P09 |
| Internet | One business cable line; no failover. Staff phones can act as hotspots | P01, P05 |
| Storm stock | About 30 remanufactured units are held from June to November. Every unit ships with a test report from the test PC; no unit ships without one | P01, P05, P08 |
| Cyber insurance | Small-business cyber policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics). The policy requires notice as soon as practicable and use of panel vendors, and asks at renewal whether MFA protects email and remote access | P08 |
| AI-001 pilot | Since 2026-04 the Field Service and Test Technician has uploaded DGA results and nameplate data for about 900 transformers belonging to 2 cooperative customers (one of them the G&T cooperative) and 1 municipal utility. The cooperative's master service agreement treats substation locations and equipment data as its confidential information | P01, P10 |
| Payroll and cash | Payroll runs biweekly through an outside payroll service. A cash reserve covers about 45 days of expenses | P01, P05 |
| Cooperative questionnaire | The G&T cooperative sent a vendor security questionnaire in 2026-07 asking for a SOC 2 report or an equivalent self-assessment; the response is due 2026-09-30 | P09 |
| Assessor | The P07 assessor is an independent consultant engaged for a fixed fee, not involved in the risk or gap analysis and operating no control | P07 |
