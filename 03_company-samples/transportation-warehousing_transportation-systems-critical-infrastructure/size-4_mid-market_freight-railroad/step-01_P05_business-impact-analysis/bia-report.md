# Business Impact Analysis: Cris Santos Company | Transportation Systems | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Cybersecurity Manager with the vCISO, the process owners named in `bia.csv`, and the Director of Network Operations | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the board audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Network Operations (dispatch and the PTC program), Shared Services (contract dispatching for affiliated short lines), Transportation, Engineering, Mechanical, Customer Service and Car Management, Safety, Security, and Hazmat, Finance, Human Resources, and IT. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and safety.

The results feed:
- the list of **Critical Cyber Systems** in the TSA-approved Cybersecurity Implementation Plan (SD 1580/82-2022-01E III.A) and the business critical functions that the Cybersecurity Incident Response Plan must protect (SD 1580-21-01E II.D.1);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the shared dispatch service (P09).

## 2. System and business description
The company runs 512 route miles of track in north and central Florida, plus 52 miles of trackage rights over a Class I railroad's PTC-equipped main line. It moves about 214,000 carloads a year, including about 5,200 tank cars of chlorine and anhydrous ammonia, most of them interchanged with 2 Class I railroads at Jacksonville Terminal Yard inside the Jacksonville HTUA. About 26 trains run each day. Since 2025-07 the company also dispatches 2 affiliated short lines.

Train movement depends on the Train Dispatch and PTC Operations Platform (TDPO) described in the SSP (P02): the CAD/CTC office system (SYS-01), the PTC tenant systems and back office server (SYS-02), the CTC field network (SYS-03), the radio network (SYS-04), identity (SYS-05), the dispatch zones and consoles (SYS-09), and the crew management application and backup vault in the cloud landing zone (SYS-07, SYS-08). The TMS (SYS-06) is a vendor SaaS outside the TDPO boundary but feeds it (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $214 million in annual revenue over 365 operating days: about $537,000 of carload freight revenue and $586,000 of total revenue per day. About 22% of freight revenue (about $118,000 a day) moves over the trackage-rights segment, and about 70% of carloads (about $376,000 a day) move through interchange.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 in unrecovered revenue and extra cost, or more than $1 million of billing delayed | $20,000 to $100,000 | Less than $20,000 |
| Operations | Trains cannot move on a subdivision or the trackage-rights segment, or interchange stops | Throughput drops by more than 30%, or one yard or service stops | Staff slowed but working |
| Regulatory | Missed TSA clock (30-minute RSSM request, 24-hour 1570.203 report, 72-hour SD report), FRA reportable event, or a TSA inspection finding against the approved CIP | Missed documentation or recordkeeping that can be back-entered | Internal policy deviation |
| Safety | Plausible harm to crews, roadway workers, or the public (conflicting authority, lost worker protection, hazmat release, PIH cars unlocated) | Degraded but safe operations | None |
| Reputation | Loss of a Class I partner's confidence, loss of an affiliate or contracted short line, regional media coverage, or TSA escalation | Shipper complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra cost (crew overtime, car hire and per diem, Class I delay charges, service credits), over the MTD. The process owners estimate that freight held for less than a day is almost all recovered, while about 20% of a day's freight is lost when the network is degraded for several days (shippers divert to truck or cut production). For billing (BP-13) the loss is cost of delay; the delayed billing is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-07 RSSM location, chain of custody, and TSA reporting | Safety, Security, and Hazmat | High | 0.5 | 0.5 | 4 | Not estimated (regulatory exposure) |
| 2 | BP-01 Train dispatching and movement authority | Network Operations | High | 4 | 2 | 0.25 | $60,000 |
| 3 | BP-02 Contract dispatching for short lines | Shared Services | High | 4 | 2 | 0.25 | $15,000 |
| 4 | BP-16 Safety and hazmat incident reporting | Safety, Security, and Hazmat | High | 1 | 1 | 24 | Not estimated (regulatory exposure) |
| 5 | BP-04 CTC field signal and code line operation | Engineering | High | 8 | 4 | 24 | $30,000 |
| 6 | BP-03 PTC tenant operations on the trackage-rights segment | Network Operations | High | 12 | 6 | 1 | $55,000 |
| 7 | BP-05 Crew calling and hours-of-service records | Transportation | High | 12 | 6 | 1 | $35,000 |
| 8 | BP-15 Email, collaboration, and file services | IT | Moderate | 24 | 12 | 24 | $5,000 |
| 9 | BP-06 Car management, waybills, and consists | Customer Service and Car Management | High | 12 | 8 | 1 | $40,000 |
| 10 | BP-09 Yard and terminal operations | Transportation | Moderate | 12 | 8 | 1 | $25,000 |
| 11 | BP-08 Interchange with the Class I railroads | Transportation | High | 24 | 12 | 1 | $90,000 |
| 12 | BP-12 Customer service, car tracing, shipper portal | Customer Service and Car Management | Moderate | 48 | 24 | 4 | $15,000 |
| 13 | BP-10 Locomotive and car maintenance records | Mechanical | Moderate | 72 | 24 | 24 | $20,000 |
| 14 | BP-11 Track and structures inspection records | Engineering | Moderate | 72 | 48 | 24 | $10,000 |
| 15 | BP-14 Payroll and HR | Human Resources | Moderate | 72 | 48 | 24 | $15,000 |
| 16 | BP-13 Billing, demurrage, revenue accounting | Finance | Low | 120 | 72 | 24 | $10,000 (plus about $2.9 million billing delayed) |
| 17 | BP-17 Procurement and accounts payable | Finance | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 9 High, 6 Moderate, and 2 Low processes (17 in total). The sum of estimated losses at each process's MTD is $430,000.

**Why the order is not strictly by MTD.** BP-07 and BP-16 are handled first because their clocks are regulatory and short, and their workarounds (printed RSSM list, printed contact lists, phones) need no system. BP-15 is restored before BP-06 because out-of-band coordination needs email back early in a long recovery; it is still Moderate.

**Enterprise-wide scenario.** If the TDPO were down for 72 hours (for example, ransomware that reaches the dispatch zone), the unrecovered loss would be about $640,000: lost and diverted traffic $320,000, crew overtime, car hire, and per diem $190,000, rerouting of trackage-rights traffic $90,000, and service credits to the short lines $40,000. Incident response costs come on top (P01 R-001). A 72-hour TMS vendor outage would cost about $260,000, mostly in interchange delay and manual car work (P01 R-014; P08 `ir-runbook-vendor-outage.md`).

**What drives the values:**
- **Safety** drives BP-01, BP-02, BP-04, BP-07, and BP-16. Movement authority, roadway worker protection, and PIH car location cannot fail open.
- **Regulatory clocks** drive BP-07 (30 minutes) and BP-16 (immediate and 12-hour telephone reports). These are the shortest MTDs in the company, and neither depends on a system once the fallbacks exist.
- **Revenue** drives BP-03 and BP-08: the trackage-rights segment and interchange carry most of the money.

## 5. Key findings
1. **CAD/CTC recovery is designed but unproven.** The hot standby at the backup NOC replicates in real time, so it protects against hardware and site loss but would replicate ransomware or database corruption. Recovery from the write-once backups in the cloud backup account has never been tested end to end (gap 6). The 2-hour RTO for BP-01 is a target, not a demonstrated capability (P01 R-003; P07 CP-4).
2. **Manual dispatch in CTC territory has never been drilled.** The manual dispatch procedure has been exercised only on the branch lines in track warrant territory. At the 4-hour MTD, unpracticed manual dispatch in CTC territory is the most likely place for a safety error (P01 R-005).
3. **The TMS vendor does not meet the BIA.** Its SOC 2 system description states an RTO of 24 hours and an RPO of 1 hour. The BIA needs an RTO of 8 hours for BP-06 and supports BP-07, BP-08, and the PTC consist feed. The printed RSSM list every 4 hours keeps the 30-minute TSA duty achievable, but car management and interchange degrade quickly (P01 R-014; P09 vendor review).
4. **The PTC back office has a standby but the vendor support SLA is 8 hours**, longer than the 6-hour RTO for BP-03. Failover to the standby BOS has been tested once (2025-11), not under incident conditions.
5. **Shared dispatch is now a contractual service.** The affiliates' agreements promise restoration within 2 hours, which equals the BP-01 RTO and leaves no margin. The SOC 2 Availability criteria in P09 depend on findings 1 and 2.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 CAD/CTC office system | Primary cluster (HQ data center), hot standby (backup NOC), 22 consoles | BP-01, BP-02, BP-07, BP-08 |
| SYS-02 PTC tenant systems | BOS pair, 3 PTC administration workstations, 46 onboard units, messaging link to the host | BP-03 |
| SYS-03 CTC field network | 150 signal locations, communication controllers, code line | BP-01, BP-04 |
| SYS-04 Radio and wayside monitoring | 38 towers, radio-over-IP gateways and consoles, 22 detectors, 118 crossing monitors | BP-01, BP-02, BP-04, BP-16 |
| SYS-05 Identity | Directory and identity provider; break-glass accounts | All |
| SYS-06 TMS (vendor SaaS) | Car management, waybills, consists, RSSM data, EDI, shipper portal | BP-02, BP-06 to BP-09, BP-12, BP-13 |
| SYS-07 Crew management (cloud) | Crew calling and hours of duty records | BP-05, BP-14 |
| SYS-08 Cloud landing zone | Operations workloads, backup vault (35-day write-once), file services, AI image store | BP-01 to BP-05 (recovery), BP-11, BP-15 |
| SYS-09 Networks and endpoints | Dispatch zones, IT/OT boundary firewalls, SD-WAN, consoles, 410 crew tablets | All |
| SYS-10 Security tooling | SIEM and EDR (MSSP), PAM jump hosts, OT sensors | Recovery validation |
| SYS-11 ERP | Payroll, HR, finance | BP-10, BP-13, BP-14, BP-17 |
| Third parties | CAD/CTC vendor, PTC vendor, TMS vendor, radio vendor, detector vendor, leased circuit carrier, host Class I, Class I partners, MSSP, cloud provider | As listed in `bia.csv` |
| People and facilities | 36 dispatchers, 70 signal and communications staff, PTC administrators, car management staff; primary NOC, backup NOC, HQ data center, Jacksonville Terminal Yard | All |

## 7. Link to the TSA directives
The BIA gives the facts the directives ask for:

| Directive requirement | What this BIA supplies | Status |
|---|---|---|
| SD 1580/82-2022-01E III.A: identify Critical Cyber Systems (systems or data whose compromise could cause operational disruption) | Every system that supports a High process (SYS-01 to SYS-07 and the operations parts of SYS-08 and SYS-09) is confirmed as a Critical Cyber System; the CIP list matches, except the crossing monitors, which are added (P03) | CIP amendment due within 50 days of the permanent change (SD VI.D) |
| SD 1580/82-2022-01E III.B: OT keeps operating safely if IT is compromised | Dependencies of BP-01, BP-03, and BP-04 on IT services (identity, TMS consists, cloud backups) | Dependencies listed; field segmentation gap remains (gap 1) |
| SD 1580/82-2022-01E III.D.4 and SD 1580-21-01E II.D.1.c: isolate OT when an IT incident threatens it | Manual dispatch, local control point operation, and the isolation order in P08 | Procedures written; CTC territory drill due 2026-12-10 |
| SD 1580-21-01E II.D.1.b: offline, scanned backups | RPOs for the TDPO and the backup scope in P04 | Backups exist; restore test due (gap 6) |
| SD 1580-21-01E II.D.2: positions responsible for the plan | Process owners in `bia.csv` match the P08 role tables | Done |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | RSSM fallback (printed list, offline laptop) and out-of-band communications | 0.5 h (procedural) | Phones independent of company systems; printed call trees at both NOCs |
| 2 | SYS-05 identity and break-glass accounts | 1 h | Two break-glass accounts per critical system, stored offline at each NOC |
| 3 | SYS-09 dispatch zones, IT/OT boundary firewalls, clean consoles (primary NOC or backup NOC) | 2 h | 6 pre-imaged spare consoles at each NOC |
| 4 | SYS-01 CAD/CTC office system (standby, or restore from write-once backup) | 2 h | Manual dispatch procedure |
| 5 | SYS-03 CTC code line and SYS-04 radio | 2 h (radio), 4 h (code line) | Local control point operation; voice radio on fixed channels |
| 6 | SYS-02 PTC back office (standby BOS) | 6 h | Hold or reroute trackage-rights trains |
| 7 | SYS-07 crew management | 6 h | Printed crew boards refreshed every 4 hours |
| 8 | SYS-06 TMS access (vendor) and consist feed | 8 h | Printed consists; partner consist files by email |
| 9 | SYS-10 SIEM, EDR console, and OT sensors | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 10 | Interchange EDI | 12 h | Paper interchange reports |
| 11 | Email and file services | 12 h | Out-of-band messaging group |
| 12 | ERP payroll | 48 h | Repeat prior payroll |
| 13 | Data warehouse and billing | 72 h | Bill from the last waybill extract |
