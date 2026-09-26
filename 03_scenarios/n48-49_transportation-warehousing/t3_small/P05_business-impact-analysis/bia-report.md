# Business Impact Analysis: Cris Santos Company | Transportation and Warehousing | Small

**Organization:** Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (proposed Cybersecurity Officer) with the Operations Manager, Maintenance Manager, Security and Safety Manager (FSO) and Finance and Administration Manager, 2026-07-20 to 2026-07-31 | **Approved:** General Manager, 2026-09-04

## 1. Overview and purpose
This BIA identifies the terminal's business processes, how long each can be down, and how much data each can lose. It supports:
- the resilience measures in the USCG cyber rule: backups of critical IT and OT systems that are protected and tested (33 CFR 101.650(g)(4)), and the Cyber Incident Response Plan (101.650(g)(2));
- the contingency plan for TOS, gate and OT loss, due 2026-12-31 (P02 CP-2);
- the availability rating in the SSP (P02 section 6);
- the impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08).

It also gives the Cybersecurity Assessment due 2027-07-16 (101.650(e)(1)) a first view of which systems are critical IT or OT systems (101.615).

## 2. System and business description
The company runs one container and breakbulk terminal at a Florida port: 2 berths, about 5 vessel calls a week, about 160,000 container moves and 350,000 tons of breakbulk a year, and about 800 truck gate transactions a day. Operations run on the Terminal Operations and Gate Platform (TOGP): the terminal operating system (TOS) in a cloud tenant, gate automation on premises, EDI with carriers and the customs data exchange, the identity provider, and the terminal network. Cranes and yard equipment run on their own controllers (OT) and take job instructions from the TOS. See the SSP (P02) and `../scenario-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to $28.2 million in annual revenue, about $77,000 per day on average (vessel days earn more).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (about 3 days of revenue), or a carrier contract penalty | $50,000 to $250,000 | Less than $50,000 |
| Operations | A vessel cannot be worked, or the truck gate stops | One berth, some gate lanes or the yard slowed to manual working | Staff slowed but working |
| Regulatory | A transportation security incident, a failure of FSP access control, a container released while on a customs hold, or a cyber incident not reported under 33 CFR 6.16-1 | A missed record, drill or reporting timeliness requirement | Internal policy deviation |
| Safety | Plausible injury: unsafe crane or RTG motion, a heavy or hazardous container mis-stowed, or responders cannot locate hazardous cargo | Unsafe conditions controlled by stopping work | None |
| Reputation | A carrier moves a service to another terminal, or regional media coverage | Complaints from carriers, trucking companies or the port authority | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Vessel operations (discharge and load) | High | 8 h | 4 h | 1 h |
| BP-02 Truck gate processing | High | 8 h | 4 h | 1 h |
| BP-03 Yard and equipment operations | High | 12 h | 6 h | 1 h |
| BP-04 Security and hazardous cargo control | High | 4 h | 2 h | 1 h |
| BP-05 Customs status and carrier EDI exchange | Moderate | 12 h | 8 h | 4 h |
| BP-06 Vessel, berth and yard planning | Moderate | 24 h | 12 h | 4 h |
| BP-07 Crane and equipment maintenance and OT support | High | 8 h | 4 h | 24 h |
| BP-08 Customer service and truck appointments | Moderate | 24 h | 8 h | 24 h |
| BP-09 Billing, demurrage and collections | Low | 72 h | 48 h | 24 h |
| BP-10 Payroll, HR and finance | Low | 120 h | 72 h | 24 h |

Totals: 5 High, 3 Moderate and 2 Low processes.

**What drives the values:**
- **Safety and security drive BP-04.** The FSO and emergency responders must be able to find hazardous cargo at any time. Today that list exists only in the TOS (P01 R-030). A printed list at every shift change makes the 4-hour MTD achievable.
- **The berth window drives BP-01 and BP-07.** A vessel works for about 18 to 30 hours. Past about one shift of manual working, the carrier misses its window and the next port call. An MTD of 8 hours equals one shift.
- **Road congestion and customs holds drive BP-02.** Trucks back up onto port roads within about 2 hours. The gate can run manually on one lane, but only for containers confirmed released.
- **Partners can resend data, which drives BP-05.** Carriers and the customs data exchange can resend the last 24 hours of messages, so a 4-hour RPO is enough. Timeliness matters more than data loss.
- **Revenue drives BP-09 more than time does.** Charges can be rebuilt from TOS move history, so billing can wait 72 hours.
- **The OT RPO means a program version, not hours of data.** PLC programs and HMI settings change rarely. The 24-hour RPO means the last approved version must be held by the company, not only by the crane vendor.

**Key findings:**
1. **The TOS recovery targets are unproven.** BP-01 to BP-04 need the TOS back in 4 hours with no more than 1 hour of data lost. Database snapshots offer 7-day point-in-time restore, but they sit in the production cloud account. The weekly export sits on a domain-joined device on the office LAN. A ransomware actor with administrator rights could destroy both. In that case, the real RPO would be up to 7 days and the RTO would be unknown. **No restore test has ever been performed** (P01 R-004; the first test is scheduled 2026-10-20).
2. **The gate cannot be rebuilt within its RTO.** Gate server and OCR configurations are not backed up, so a rebuild would take days of vendor work (P01 R-010).
3. **The company does not hold its own PLC programs.** A crane controller wiped by malware depends on the crane vendor's copy and schedule (gap 13 in `../scenario-facts.md`).
4. **Single points of failure:** one internet circuit (P01 R-016), one cloud region for the TOS (P01 R-017, accepted), and one gate server room (P01 R-015 hurricane).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Identity provider | Single sign-on and MFA for the TOS, email and cloud administration | BP-01 to BP-06, BP-08 |
| SYS-07 Terminal networks and internet | Firewall, office LAN, gate and yard network, VMT Wi-Fi, site-to-site VPN; one internet circuit | All |
| SYS-10 Cloud tenant | TOS application servers and database, EDI gateway, integration server | BP-01 to BP-06, BP-08, BP-09 |
| SYS-01 TOS | System of record for containers, locations, holds and hazardous cargo | BP-01 to BP-06, BP-08, BP-09 |
| SYS-02 Gate automation | OCR portals, TWIC readers, driver kiosks, gate transaction server | BP-02, BP-04 |
| SYS-03 Crane and yard equipment controllers (OT) | STS and RTG PLCs, HMIs, VMTs | BP-01, BP-03, BP-07 |
| SYS-04 EDI and data exchange | Carriers, trucking companies, port community system, customs data exchange | BP-01, BP-02, BP-05 |
| SYS-08 Endpoints | Operations and gate booth workstations, checker tablets, VMTs | BP-01 to BP-03, BP-08 |
| SYS-09 CCTV and PACS | TWIC access control and video | BP-04 |
| SYS-12 Scheduling optimization (pilot) | Advisory berth and yard plans | BP-06 (not required for recovery) |
| SYS-06 and SYS-11 | Email, finance, payroll and HR SaaS | BP-08 to BP-10 |
| People and facilities | Planners, superintendents, clerks, security officers, mechanics, longshore labor, IT Manager, MSP; the gate server room and crane electrical houses | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and break-glass administrator accounts | 1 h | Two break-glass accounts stored offline in the FSO safe (to be created; P07 POA&M) |
| 2 | SYS-07 Firewall, internet and core network, with the OT zone isolated | 2 h | Cellular backup router (with the second circuit due 2026-12-31) |
| 3 | SYS-09 PACS and TWIC readers; printed dangerous cargo list | 2 h | PACS runs on its own server; security officers check TWICs visually and log entries by hand |
| 4 | SYS-10 and SYS-01: TOS database and application servers | 4 h | Restore from isolated backups (after P01 R-004 treatment); paper vessel and gate procedures meanwhile |
| 5 | SYS-08 Clean operations endpoints and gate booth workstations | 4 h | 6 pre-imaged spare laptops kept in the IT office (to be prepared) |
| 6 | SYS-03 Crane and RTG controllers verified clean and reconnected to the TOS | 4 h | Cranes run in local mode with radio dispatch; crane vendor reloads programs on site |
| 7 | SYS-02 Gate automation: gate servers, OCR, kiosks | 4 h (target; not achievable today, see finding 2) | Manual gate on one lane with printed release list |
| 8 | SYS-04 EDI gateway and customs data exchange feed | 8 h | Customs data exchange web portal; carrier email |
| 9 | TOS vendor hosted truck appointment and customer portal | 8 h | Phone and email appointments |
| 10 | SYS-11 Finance, payroll and billing | 48 to 72 h | Queue invoices; repeat prior payroll |
| 11 | SYS-12 Scheduling optimization service | Not required; reconnect only after a security review | Manual planning |

The contingency plan due 2026-12-31 will turn these priorities into procedures and test them. It must test the restore of the TOS database and the rebuild of one gate server before the Cybersecurity Plan is submitted.
