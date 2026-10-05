# Business Impact Analysis: Cris Santos Company | Transportation Systems | Micro

**Organization:** Cris Santos Company, LLC (short line freight railroad, 16 route miles, north Florida) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Security Lead) with the Owner and General Manager, the Roadmaster, the Conductor, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the railroad, how long each can be down, and how much data each can lose. It supports:
- the contingency plan the railroad does not yet have (P01 R-002, R-013; P03 benchmark rows for RC.RP);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No binding rule requires this railroad to have a cyber contingency plan. The TSA rail directives that require one do not apply (P03 section 1). The BIA is done because a ransomware event or a long outage would stop movement authority, and because the connecting Class I's questionnaire asks about recovery (P09).

## 2. System and business description
One office and enginehouse at Junction, 16 miles of dark-territory main track, 3 locomotives, 7 employees, and one interchange turn a day to a Class I railroad. Movement authority comes from the short line operations system (SYS-01, vendor SaaS) and is passed to crews by radio (SYS-06). Crews use 3 tablets (SYS-03). Email and the shared drive are SaaS (SYS-02); the MSP runs the office network and endpoints (SYS-03, SYS-04) and the backup (SYS-05). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $4,400 per operating day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $13,000 (about 3 operating days) | $4,000 to $13,000 | Less than $4,000 |
| Operations | No trains move, or interchange stops | One function stops; trains run late | Staff slowed but working |
| Regulatory | Missed TSA, FRA, or hazmat duty, or a reportable breach | Late record or report that can be corrected | Internal policy deviation |
| Safety | Plausible collision, derailment, roadway worker injury, or hazmat release | Delayed but safe operation | None |
| Reputation | Loss of a customer or of the Class I's confidence; local news | Customer complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Train dispatching and movement authority | High | 8 h | 4 h | 1 h |
| BP-02 Train and yard operations | High | 24 h | 8 h | 4 h |
| BP-03 Car management, waybills, and interchange EDI | Moderate | 24 h | 8 h | 4 h |
| BP-04 Hazmat shipment handling and security | High | 24 h | 8 h | 4 h |
| BP-05 Track inspection and maintenance | Moderate | 72 h | 24 h | 24 h |
| BP-06 Locomotive and car mechanical | Low | 72 h | 48 h | 24 h |
| BP-07 Security and regulatory reporting | High | 4 h | 1 h | 24 h |
| BP-08 Billing, customer service, payroll, and office administration | Low | 72 h | 48 h | 24 h |

Totals: 4 High, 2 Moderate, 2 Low.

**What drives the values:**
- Safety drives BP-01. Paper dispatch is safe if the dispatcher knows every active authority at the moment of the switch. That is why the RPO is 1 hour, and why the first step in any outage is a radio roll call.
- An MTD of 8 hours for BP-01 is one shift. Paper dispatch can carry one operating day; a second day without the system stops interchange and switching (BP-02).
- BP-07 has the shortest MTD because the TSA Security Coordinator must be reachable 24/7 (49 CFR 1570.201(f)(2)) and a cyber attack must be reported within 24 hours of discovery (1570.203). It depends on phones and a printed contact card, not on company systems.
- Billing and payroll (BP-08) tolerate 72 hours because invoices can be issued late and the payroll service can repeat the prior payroll.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Short line operations system (SaaS) | Authorities, train sheets, slow orders, car inventory, waybills, EDI, hazmat car list | Vendor replication and backups (SOC 2 report states RTO 4 h and RPO 1 h; see P09). No company-held copy (gap) | BP-01 to BP-05 |
| SYS-06 Radio dispatch system | Base station and console at the desk; mile 8 repeater; mobile and handheld radios | Handhelds work through the repeater without the console; spare base radio in the enginehouse | BP-01, BP-02 |
| SYS-03 Endpoints | Dispatch desktop (runs the radio console), office and shop desktops, 2 laptops, 3 crew tablets | Nothing stored locally by design except synced shared-drive files | All |
| SYS-02 Productivity suite (SaaS) | Email and the shared drive (timetable, track charts, security plan, employee files) | Vendor resilience; nightly copy to SYS-05 | BP-04, BP-05, BP-07, BP-08 |
| SYS-05 Suite backup (SaaS) | Nightly copy of the shared drive and mailboxes, 30 days of versions | **Never restore-tested** | BP-08 |
| SYS-04 Office network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | BP-01, BP-03, BP-08 |
| SYS-07 Locomotive telematics | Location, fuel, and engine fault alerts | Not needed for operations | BP-06 |
| People | 7 employees; the General Manager and Roadmaster are the only qualified dispatchers | Roadmaster relieves the General Manager; the Mechanic relieves the Conductor | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Security terms in contract | Evidence of recovery capability |
|---|---|---|---|
| Operations SaaS vendor | BP-01 to BP-05 | Standard SaaS terms; incident notice in the vendor's terms only | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 1 h meet this BIA |
| MSP | Recovery of every on-site device; operates the backup | None | No written recovery commitment; the contract has only a 4-business-hour response time |
| Productivity suite vendor | BP-07 contact lists, BP-08 | Standard terms | Vendor service commitments |
| Backup service (held by the MSP) | Restore of the shared drive and mailboxes | Through the MSP | None until the first restore test |
| Radio service vendor | Repair of the base station and repeater | Service call agreement | Spare base radio on site |
| Internet provider | SYS-01 from the desk; EDI; email | Standard terms | None; single line |
| Connecting Class I | Interchange (BP-02, BP-03) | Interchange agreement | Its own operations; can accept waybills through its web portal |

**Key findings:**
1. **The operations SaaS vendor meets the BIA.** Its stated RTO (4 h) and RPO (1 h) meet the targets for BP-01. The company still holds no copy of its own operations data (P01 R-005).
2. **The real single point of failure is the dispatch desk.** The dispatch desktop runs the radio console on an unsupported operating system (P01 R-007), uses the one internet line (R-010), and sits on the same network as the office computers a phishing email would reach first (R-001).
3. **Paper dispatch is the true recovery strategy**, but it is a habit, not a written procedure, and has never been exercised (R-002).
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. The contract amendment in P01 (R-004) adds one.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Radio contact with all trains (SYS-06) | 1 h | Handheld radios through the repeater; spare base radio |
| 2 | Paper dispatch and the security contact card (BP-01, BP-07) | 1 h | Printed forms, timetable, track chart, slow orders, and contact card at the desk and in the incident binder |
| 3 | Internet and office network (SYS-04) | 2 h | Cellular failover router (to be installed by 2026-11-30); General Manager's phone hotspot until then |
| 4 | Clean dispatch endpoint with access to SYS-01 (SYS-03) | 4 h | General Manager's encrypted laptop; MSP reimages the desktop |
| 5 | Crew tablets (SYS-03) | 8 h | Paper switch lists and bulletins |
| 6 | Email and phones (SYS-02) | 8 h | Office line forwarded to the General Manager's cell phone |
| 7 | Shared drive restore (SYS-05 to SYS-02) | 48 h | Printed timetable and security plan copies in the binder |
| 8 | Accounting, payroll, and telematics (SYS-08, SYS-07) | 72 h | Payroll service repeats prior payroll; manual fuel checks |
