# Business Impact Analysis: Cris Santos Company | Transportation and Warehousing | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator, 8 terminals at 6 U.S. ports) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with the process owners and the Terminal General Managers, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on across its 8 terminals, its enterprise planning center and its two outside service lines, how long each can be down, how much data each can lose, and what each depends on, including third parties, port partners and the acquired terminal T-08. It feeds:
- the resilience measures in the Cybersecurity Plans: backups of critical IT and OT systems that are protected and tested (33 CFR 101.650(g)(4)) and the Cyber Incident Response Plan (101.650(g)(2));
- the continuity sections of the 8 Facility Security Plans, so that TWIC access control and the dangerous cargo location list keep working during an IT outage (33 CFR Part 105);
- the availability rating and recovery objectives in the ETOP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), following NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09);
- the materiality worksheet of the disclosure committee (P08 section 6), which uses the dollar values in section 4.

**Results in one line:** 16 processes were analyzed; 9 are High criticality, 6 Moderate and 1 Low. 7 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies: 12 are single points of failure, 3 are partial single points of failure, and 3 have never been tested.

## 2. System and business description
Cris Santos Company operates 8 container, ro-ro and multipurpose terminals (T-01 to T-08) at 6 U.S. ports in Florida, Georgia, South Carolina and Texas under concessions from landlord port authorities. It handles about 8.8 million container moves, 4.1 million tons of breakbulk and 640,000 vehicles a year, with about 85 vessel calls a week and about 22,000 truck gate transactions a day. Revenue is about $4.8 billion a year, about $13.2 million per calendar day. It has 12,000 employees and orders 2,500 to 4,500 longshore workers a day through the hiring halls.

The technology estate is described in `../00_company-facts.md` section 3. The center of it is the Enterprise Terminal Operating and Gate Platform (ETOP, the P02 system): one TOS platform in Cloud provider A that runs 11 terminal environments (T-01 to T-07 and the 4 SL-2 client terminals), gate automation at T-01 to T-07, and the EDI and integration hub. Around it sit the OT at each terminal (54 STS cranes, the T-01 automated stacking crane yard, RTGs, straddle carriers, about 1,900 VMTs), the physical security systems that support the Facility Security Plans, the SL-1 platform in Cloud provider B, two colocation data centers, and SaaS for finance, payroll and labor ordering. T-08, acquired on 2025-11-03, still runs a legacy on-premises TOS and gate system until it migrates in 2027.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the materiality framework of the disclosure committee (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Vessel or gate work stops at 2 or more terminals, or at any terminal for more than one shift; a missed carrier berth window | One terminal, one service line or one process degraded but working | Staff slowed but working |
| Regulatory | Reportable cyber incident, breach of security or transportation security incident (33 CFR 101.305); a container on customs hold released; a missed SEC filing; breach notice to 500 or more residents of a state | Missed contractual notice to a carrier, SL-1 or SL-2 customer; breach notice to fewer than 500 people; MTSA record deficiency | Internal policy deviation |
| Safety | Plausible injury or hazardous cargo event: crane or automated equipment moving on bad data, responders unable to locate hazardous cargo | Unsafe condition caught before work starts | None |
| Reputation | National media; a carrier moves a service to another terminal; a port authority reviews a concession; analyst or ratings action | Regional media; trucker and customer complaints; port partner escalation | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Listed in recovery priority order.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-04 Maritime security, TWIC access control and hazardous cargo control | High | 4 h | 2 h | 15 min | $0.20M |
| BP-01 Vessel operations at container terminals | High | 8 h | 4 h | 15 min | $5.80M |
| BP-02 Truck gate processing | High | 8 h | 4 h | 15 min | $2.40M |
| BP-05 Customs status and carrier EDI exchange | High | 12 h | 4 h | 1 h | $0.90M |
| BP-10 SL-1 Cargo Visibility and Appointment Platform | High | 12 h | 4 h | 1 h | $0.30M |
| BP-11 SL-2 Hosted terminal technology services | High | 8 h | 4 h | 15 min | $0.70M |
| BP-03 Yard and equipment operations | High | 12 h | 6 h | 15 min | $1.60M |
| BP-07 Crane, automation and equipment maintenance and OT engineering | High | 8 h | 4 h | 24 h | $1.10M |
| BP-16 T-08 terminal operations on legacy systems | High | 12 h | 8 h | 15 min | $0.90M |
| BP-12 Longshore labor ordering and timekeeping | Moderate | 24 h | 12 h | 4 h | $0.80M |
| BP-06 Vessel, berth and yard planning | Moderate | 24 h | 12 h | 1 h | $0.40M |
| BP-08 Ro-ro, breakbulk and project cargo operations | Moderate | 24 h | 12 h | 1 h | $1.50M |
| BP-09 On-dock rail operations | Moderate | 24 h | 12 h | 1 h | $0.50M |
| BP-13 Billing, demurrage and collections | Moderate | 120 h | 72 h | 24 h | $0.35M |
| BP-14 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-15 Payroll, HR and timekeeping (employees) | Low | 72 h | 48 h | 24 h | $0.25M |

**What drives the values:**
- **Safety and maritime security** set the shortest objectives. Emergency responders must be able to locate hazardous cargo at any time, and FSP access control must continue at every MARSEC level, so BP-04 has a 4-hour MTD and a 2-hour RTO. Its workaround (manual TWIC checks and a printed dangerous cargo list at every shift change) is what keeps the MTD that long.
- **Vessel berth windows** drive BP-01 and BP-11. A container vessel call has a fixed window of about 18 to 36 hours, and a missed window delays the carrier's service at its next ports. Manual working sustains about one shift at about 40% productivity, so the MTD is 8 hours.
- **Customs holds** drive BP-02 and BP-05. Releasing a container on a customs hold is a regulatory failure, so the gate stops rather than guesses. Partners can resend 24 hours of EDI, so a 1-hour RPO is enough for BP-05, but gate transactions must not be lost (15 minutes).
- **OT is different.** Cranes can run in local mode without the TOS, so the RPO for BP-07 is the last approved controller program (24 hours). What matters is that the program vault holds a clean copy; T-07 and T-08 depend on OEM copies.
- **Contracts** set the SL-1 and SL-2 objectives (BP-10, BP-11). SL-2 clients set 4-hour RTOs in their own BIAs and rely on the company for systems they have delegated (101.615).
- **Cash, not time,** drives billing (BP-13): about $12.8 million a day of invoicing is deferred, not lost. **Regulation** tightens financial close (BP-14) to a 48-hour MTD in the quarter-end window because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **One TOS platform for 11 terminals (DEP-01).** ETOP is the system of record for every container, hold and hazardous cargo class at T-01 to T-07 and at the 4 SL-2 client terminals. In the 2026-05-16 DR test, 3 environments were restored in 7.5 hours against a 4-hour RTO, because restores run one environment at a time. Cross-region failover has never been tested for the other 8 environments. This is the largest single concentration in the estate and drives the Very High ransomware risk (P01 R-001) and the recovery risk R-008.
2. **Customs data exchange service (DEP-08).** One provider delivers 100% of electronic release and hold status from U.S. Customs and Border Protection. The contract has no security or incident notification terms, there is no RTO in the contract, and the portal fallback has never been tested at volume. Without reliable hold status, import deliveries fall to about 30% of normal at every terminal (P01 R-010).
3. **Port community systems (DEP-09).** Each of the 6 ports runs its own system, operated by the port authority, for vessel schedules and gate status. None of the 6 data exchanges has security or notification terms (P01 R-011).
4. **OEM and automation vendors (DEP-11, DEP-12).** The crane OEM for T-03, T-07 and T-08 and the automation vendor for the T-01 automated yard use their own remote tools outside the vendor access gateway. The company holds a program vault for T-01 to T-06; T-07 and T-08 depend on OEM copies to reload a corrupted controller (P01 R-004, R-058).
5. **T-08 legacy estate (DEP-21).** The legacy TOS backs up nightly to storage on the same network, so the real RPO is about 24 hours against a 15-minute target, and no restore has been tested. T-08 also has a single SD-WAN carrier (DEP-15) and its own PACS server (P01 R-031, R-024).
6. **OCR at the gates (DEP-13).** 22 OCR servers at T-01 to T-07 reach end of vendor support in 2026-12 (P01 R-026).
7. **Longshore labor (DEP-14).** The hiring halls supply all vessel and yard labor. Their members use OT and VMTs, and training or supervised-access arrangements exist at 4 of 6 halls (P01 R-027).
8. **Utilities and hurricane exposure (DEP-05, DEP-20).** DC-1 is in Florida with a 72-hour generator fuel contract; cranes cannot run on generators, so a regional power loss stops vessel work whatever the state of IT (P01 R-023).

## 6. Resource requirements
| Resource / component | Description | Supports process | Backup or replication behind the RPO |
|---|---|---|---|
| SYS-01 ETOP TOS platform (11 environments) | TOS on IaaS and managed database in Cloud provider A | BP-01 to BP-03, BP-05, BP-06, BP-08, BP-09, BP-11, BP-13 | Database log shipping to the second region (15 min); immutable snapshots in a separate backup account |
| SYS-02 Gate automation (T-01 to T-07) | OCR portals, TWIC readers, kiosks, gate transaction servers | BP-02 | Gate transactions written to the TOS in real time; server images in the backup account |
| SYS-03 OT | STS cranes, ASCs, RTGs, straddle carriers, PLCs, HMIs, reefer monitoring, VMTs | BP-01, BP-03, BP-07 | Approved controller programs in the company program vault (T-01 to T-06) or OEM copies (T-07, T-08) |
| SYS-04 EDI and integration hub | B2B gateway, API gateway, customs and port partner links | BP-02, BP-05 | Partner resend of 24 h; message store replicated hourly |
| SYS-05 Identity platform | SSO, MFA, PAM, identity governance | All | SaaS provider replication; PAM standby in the second region; sealed break-glass accounts |
| SYS-06 Cloud provider A and B workloads; DC-1 and DC-2 | Landing zones, network core, central PACS and video servers, offline backup vault | All; BP-04 | Immutable backups in separate accounts; offline copy in DC-2 |
| SYS-07 Networks | SD-WAN, terminal LANs, OT zones, private LTE and Wi-Fi, vendor access gateway | All site-based processes | Configuration backups nightly |
| SYS-09 Physical security systems | PACS, TWIC readers, CCTV, video management | BP-04 | PACS standby in DC-2; local recording at cameras |
| SYS-10 ERP, payroll, HR and labor ordering SaaS | Finance and HR | BP-12 to BP-15 | Provider backups (contract RPO 24 h) |
| SYS-11 SL-1 platform | Availability, holds, appointments, APIs | BP-02, BP-10 | Managed database replication to the second region (1 h) |
| SYS-13 T-08 legacy estate | Legacy TOS, gate, directory | BP-16 | Nightly backup on the same network (about 24 h; gap) |
| People | Planners, superintendents, gate clerks, FSOs and security officers, OT engineers, SOC, platform teams | All | Cross-terminal staff pool; enterprise planning center |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; PAM standby in the second region |
| 2 | Network core, SD-WAN, DNS, colocation links; OT kept isolated | 2 h | Cellular failover for gate lanes |
| 3 | PACS, TWIC readers and the dangerous cargo location list (BP-04) | 2 h | Manual TWIC checks; printed list at every shift change |
| 4 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Retainer incident response firm |
| 5 | ETOP environments for T-01 to T-07, in vessel-schedule order | 4 h per environment (7.5 h demonstrated for 3; gap) | Paper bay plans, radio dispatch, manual gate |
| 6 | SL-2 client environments C-01 to C-04 | 4 h (client contracts) | Client manual procedures; printed exports |
| 7 | EDI hub and customs data exchange feed; refresh of all holds before any automated release | 4 h | Portal lookups; broker confirmations |
| 8 | Gate automation (OCR, kiosks, gate servers) | 4 h | Manual lanes at about one third capacity |
| 9 | SL-1 platform and appointments | 4 h | Appointments by phone and email; walk-ins for confirmed releases |
| 10 | OT reconnection to the TOS after controller verification | 4 h after the TOS | Cranes in local mode; manual straddle carrier blocks at T-01 |
| 11 | T-08 legacy TOS and gate | 8 h target (about 24 h of data at risk; gap) | Paper procedures |
| 12 | Labor ordering, planning tools, rail and ro-ro processes | 12 h | Phone orders; spreadsheets |
| 13 | ERP, payroll and billing | 48 to 72 h | Repeat the prior payroll; rebuild charges from TOS history |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| ETOP recovery 7.5 h against a 4 h RTO; failover untested for 8 of 11 environments | P01 R-001, R-008, R-025; P02 CP-10; P03 G-059; POAM-005 |
| T-08 real RPO about 24 h against 15 min; restore never tested | P01 R-031; P03 G-059; POAM-020 |
| Customs data exchange service: single provider, no security or notice terms, untested fallback | P01 R-010; P03 G-054; POAM-022 |
| Port community systems at 6 ports without security or notice terms | P01 R-011; P03 G-054; POAM-022 |
| OEM and automation vendor remote tools outside the vendor access gateway | P01 R-004; P03 G-051, G-055; POAM-002 |
| 22 OCR servers reach end of vendor support in 2026-12 | P01 R-026; POAM-013 |
| Longshore and contractor OT training arrangements incomplete | P01 R-027; P03 G-039, G-041; POAM-016 |
| T-07 OT and gate logs and T-08 logs not in the SIEM | P01 R-041; P03 G-036; POAM-008 |
| SL-2 client notice terms do not support the clients' immediate reporting | P01 R-013; P03 G-057; POAM-011 |
| DC-1 hurricane exposure | P01 R-023 |
