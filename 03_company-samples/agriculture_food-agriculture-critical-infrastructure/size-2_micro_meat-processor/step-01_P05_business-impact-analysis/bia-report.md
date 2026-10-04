# Business Impact Analysis: Cris Santos Company | Food and Agriculture | Micro

**Organization:** Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security and compliance lead) with the owner, the Production Supervisor, the Maintenance and Sanitation Technician, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the plant, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the food safety fallbacks the gap analysis (P03) found missing: what the plant does when electronic CCP monitoring or records are unavailable (9 CFR 417.2(c)(4), 417.3(b), 417.5(c)).

No federal rule requires this plant to have a contingency plan. FSIS rules require that CCPs are monitored and recorded and that product is not shipped until its records are reviewed, whatever happens to the systems. The BIA is how the plant keeps those duties during an outage.

## 2. System and business description
One Florida plant, 7 employees, about 40 wholesale accounts and a retail counter, about $4,400 of sales per production day. The plant runs two automated lines (stuffer and linker; thermoforming packager with label printer), a programmable smokehouse, and a cold-chain monitoring service with wireless sensors. Food safety records live in a SaaS records app on two floor tablets. Office work runs in SaaS (productivity suite, accounting, payroll). An MSP runs the office computers, firewall, and backup; equipment vendors support the plant machines. See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual sales and about $25,000 to $40,000 of product and raw material in cold storage at any time.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (product loss or about 3 production days) | $4,000 to $15,000 | Less than $4,000 |
| Operations | Production or shipping stops | One line or function stops; work slowed | Staff slowed but working |
| Regulatory | Product shipped without CCP records, a recall, or an FSIS finding that the HACCP system is inadequate | Missed or late SSOP or HACCP record; a noncompliance to correct | Internal procedure deviation |
| Safety | Plausible consumer illness (undercooked or temperature-abused product, undeclared allergen) | Product held and safely disposed of | None |
| Reputation | Recall publicity or loss of the grocery chain account | Customer complaints or late deliveries | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Cooking, smoking, and chilling (cooking and chilling CCPs) | High | 8 h | 4 h | 1 h |
| BP-02 Cold storage temperature control and monitoring | High | 2 h | 1 h | 1 h |
| BP-03 Raw processing, stuffing, and linking (Line 1) | Moderate | 24 h | 8 h | 24 h |
| BP-04 Packaging, labeling, and lot coding (Line 2) | High | 24 h | 8 h | 24 h |
| BP-05 Food safety records and pre-shipment review | High | 24 h | 8 h | 1 h |
| BP-06 Order taking, delivery, and invoicing | Moderate | 48 h | 24 h | 24 h |
| BP-07 Retail counter sales | Low | 72 h | 24 h | 24 h |
| BP-08 Payroll, purchasing, and office administration | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Cold storage (BP-02) has the shortest clock.** A cooler can drift out of range within a couple of hours of a refrigeration fault. If nobody is watching, the whole inventory is at risk. The RTO of 1 hour is met by starting the manual temperature log, not by fixing the system.
- **Cooking and chilling (BP-01) is a food safety decision, not a production one.** The smokehouse controller finishes a cycle without the network, but a cycle with no trusted record must be held and reviewed (9 CFR 417.3(b)). The 1-hour RPO reflects that a lost hour of chilling data can put a whole batch on hold.
- **Labels (BP-04) carry allergen statements.** A wrong template or missing statement is misbranding. Manual labeling is possible but slow and error-prone, so it needs a second-person check.
- **Records (BP-05)** do not stop production, but nothing ships until the pre-shipment review is done (9 CFR 417.5(c)). Paper forms keep the plant compliant for a day or two.
- **Orders and invoices (BP-06)** tolerate 48 hours, but the invoices hold the lot numbers that the recall procedure relies on.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Smokehouse controller | Cook and smoke cycles; core-probe log (90 days on the device) | Cycles exist only on the controller. **No backup.** Cook logs exported to the labeling PC, which is backed up | BP-01 |
| SYS-02 Line controls | Stuffer HMI; packager PLC, HMI, and label printer | Settings and packager recipes exist only on the machines. **No backup** | BP-03, BP-04 |
| SYS-03 Labeling PC | Label templates, lot-code software, smokehouse vendor software | Nightly cloud backup (SYS-09), never restore-tested | BP-01, BP-04 |
| SYS-04 Cold-chain monitoring service | Sensors, product probe, gateway, SaaS dashboard, text alerts | Vendor SaaS keeps history; sensors buffer readings while the gateway is offline (vendor documentation) | BP-01, BP-02 |
| SYS-05 Food safety records app | SSOP and HACCP records on 2 floor tablets | Vendor SaaS (SOC 2 not yet requested) | BP-05 |
| SYS-06 Productivity suite | Email, HACCP plans, SSOPs, formulations, recall procedure | Vendor service resilience; nightly backup (SYS-09) | BP-03, BP-06, BP-08 |
| SYS-07 Accounting and invoicing | Orders, invoices with lot numbers, customers | Vendor SaaS | BP-06, BP-08 |
| SYS-08 Office network and internet | Firewall, one flat network, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All except BP-07 |
| SYS-09 Cloud backup | Office desktop, labeling PC, productivity suite; 30 days | **Never restore-tested** | BP-01, BP-04, BP-08 |
| People | 7 employees | Only the Production Supervisor is HACCP-trained and knows the smokehouse cycles; the owner is the backup for record review | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Cold-chain monitoring vendor | BP-02 alerts; BP-01 chilling log | SOC 2 Type 2 report reviewed (P09); stated availability commitment meets this BIA if the plant's own gateway and network stay up |
| Food safety records app vendor | BP-05 | None requested yet (P01 R-018) |
| Smokehouse manufacturer | Remote service for SYS-01 | None; service by phone and site visit |
| Packaging machine vendor | Remote support for SYS-02 and SYS-12 | None |
| MSP | Recovery of office computers, the labeling PC, the firewall, and backups | No written recovery commitment; the contract has a next-business-day response time and excludes plant equipment |
| Internet provider | BP-02 alerts, BP-05 records, BP-06 orders | None; single line |
| Refrigeration contractor | Repair of refrigeration (BP-02) | 4-hour emergency response in the service agreement |

**Key findings:**
1. **The cold-chain alert path has single points of failure.** Alerts depend on the gateway, the office network, one internet line, and one person's phone. Any one of them failing silently leaves BP-02 unwatched (P01 R-004, R-013).
2. **Plant equipment settings have no backup.** Smokehouse cycles, stuffer HMI settings, and packager recipes exist only on the machines. If a controller is wiped or encrypted, the RTOs for BP-01, BP-03, and BP-04 depend on vendors rebuilding them from memory (P01 R-006).
3. **The office backup is unproven.** SYS-09 has never been restore-tested, so the 24-hour RPO for label templates and documents is an assumption (P01 R-006).
4. **The MSP contract has no recovery commitment and does not cover the plant.** A next-business-day response cannot meet a 1-hour or 4-hour RTO. The contract amendment in P01 (R-012) adds one.
5. **Paper fallbacks exist in practice but not on paper.** Staff described manual CCP forms and temperature logs, but there is no written procedure or downtime binder. Building one is the cheapest fix in this BIA (P03 417.2(c)(4)).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Temperature monitoring for coolers, freezer, blast chill cooler, and truck (SYS-04) | 1 h | Manual hourly log; cellular backup for the gateway (to be installed by 2026-10-31) |
| 2 | Smokehouse cycle completion and CCP records (SYS-01, SYS-05) | 4 h | Controller runs locally; paper CCP forms; hold product with no trusted record |
| 3 | Labeling PC and label printer (SYS-03, SYS-02) | 8 h | Pre-printed labels with a second-person check |
| 4 | Line 1 stuffer and linker (SYS-02) | 8 h | Manual mode; printed formulations |
| 5 | Food safety records app (SYS-05) | 8 h | Paper forms; enter later |
| 6 | Accounting and email (SYS-07, SYS-06) | 24 h | Paper orders and delivery tickets with lot numbers |
| 7 | Payroll and office files (SYS-10, SYS-06, SYS-09) | 48 h | Repeat prior payroll |
| 8 | Retail counter (SYS-11) | 24 h | Provider-managed terminal works without the company network |
